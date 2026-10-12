"""Great.cards chatbot core: LLM + MCP tools + guardrails.

One MCP connection is opened per user turn (simple, and avoids event-loop
problems in Streamlit). Every tool call is recorded raw in `TurnResult.tool_calls`
so failures can be traced to model / MCP / data with evidence.

Providers: anthropic | openai (any OpenAI-compatible endpoint, e.g. Gemini) | azure
Works with both the old (camelCase) and new (snake_case) `mcp` SDK objects.
"""
from __future__ import annotations
import asyncio, json, os, time
from dataclasses import dataclass, field

from dotenv import load_dotenv
from mcp import ClientSession
try:
    from mcp.client.streamable_http import streamable_http_client as _http_client  # newer SDK
except ImportError:
    from mcp.client.streamable_http import streamablehttp_client as _http_client  # older SDK

import postchecks
from guardrails import flag_phrases, unverified_amounts
from prompts import PROMPTS

load_dotenv()

MCP_URL = os.getenv("MCP_URL", "https://bk-api.bankkaro.com/mcp")
PROVIDER = os.getenv("PROVIDER", "anthropic").lower()
if PROVIDER == "anthropic":
    MODEL = os.getenv("MODEL") or "claude-sonnet-4-5"
elif PROVIDER == "azure":  # for Azure the "model" is your DEPLOYMENT name
    MODEL = os.getenv("AZURE_OPENAI_DEPLOYMENT") or os.getenv("MODEL") or "gpt-4o-mini"
else:
    MODEL = os.getenv("MODEL") or "gpt-4o-mini"
PROMPT_NAME = os.getenv("PROMPT", "guarded")
STRICT = os.getenv("STRICT_AMOUNTS", "1") == "1"
MAX_STEPS = 8

# The 5 tools the assignment documents. The server lists more (whatsapp_*, run_api_diagnostics,
# generate_content_brief, ...) that are not meant for an end-user bot.
DOCUMENTED_TOOLS = ["recommend_cards", "get_card_details", "list_cards", "compare_cards", "check_eligibility",
                    "whatsapp_resolve_card_or_category"]  # 5 documented tools + the card-name resolver (sixth tool, on purpose: prompt rules 8/8b use it)
# ALLOWED_TOOLS unset  -> guarded prompt: the 5 documented tools plus the resolver; baseline prompt: every tool the server lists
# ALLOWED_TOOLS=a,b,c  -> exactly those      ALLOWED_TOOLS=ALL -> everything, for any prompt
_allowed_env = os.getenv("ALLOWED_TOOLS", "").strip()

# The server's own guide: its get_advisor_context tool says chatbot developers should call it once at
# session start and put it in the system prompt. Used only with the guarded prompt. 0 = switch off.
USE_ADVISOR_CONTEXT = os.getenv("USE_ADVISOR_CONTEXT", "1") == "1"
# the tool's default topic is "tool_guide" (small); its own description recommends "full" (~13K tokens)
ADVISOR_ARGS = json.loads(os.getenv("ADVISOR_ARGS", '{"topic": "full"}') or '{"topic": "full"}')
_advisor_cache: str | None = None

# Code-level checks after the answer (see postchecks.py): joining-fee note and invite-only / existing-customer
# note, filled from tool data. Guarded prompt only. POSTCHECKS=0 switches them off.
POSTCHECKS = os.getenv("POSTCHECKS", "1") == "1"

CHECK_PREFIX = "SYSTEM CHECK:"


@dataclass
class TurnResult:
    reply: str
    tool_calls: list[dict] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


# ---------------------------------------------------------------- helpers
def explain(exc: BaseException) -> str:
    """One readable line for any error, unwrapping the SDK's 'unhandled errors in a TaskGroup'."""
    subs = getattr(exc, "exceptions", None)
    if subs:
        return " | ".join(explain(e) for e in subs)
    return f"{type(exc).__name__}: {exc}"


def _g(obj, *names, default=None):
    """First non-None attribute among `names` (old SDK camelCase vs new SDK snake_case)."""
    for n in names:
        v = getattr(obj, n, None)
        if v is not None:
            return v
    return default


def _schema(tool) -> dict:
    return _g(tool, "inputSchema", "input_schema", default={"type": "object", "properties": {}})


def _need(name: str) -> str:
    v = os.getenv(name)
    if not v:
        raise RuntimeError(f"{name} is not set. Put it in .env (see .env.example).")
    return v


async def _call_tool(session: ClientSession, name: str, args: dict) -> tuple[str, bool, int]:
    t0 = time.time()
    try:
        r = await session.call_tool(name, args or {})
        text = "\n".join(c.text for c in (r.content or []) if getattr(c, "type", "") == "text")
        structured = _g(r, "structuredContent", "structured_content")
        if not text and structured:
            text = json.dumps(structured, ensure_ascii=False)
        return text, bool(_g(r, "isError", "is_error", default=False)), int((time.time() - t0) * 1000)
    except Exception as e:  # network / protocol errors surface to the model honestly
        return f"TOOL ERROR: {explain(e)}", True, int((time.time() - t0) * 1000)


# ---------------------------------------------------------------- providers
async def _loop_anthropic(session, tools, system, history, trace):
    import anthropic
    client = anthropic.AsyncAnthropic()
    a_tools = [{"name": t.name, "description": t.description or "", "input_schema": _schema(t)}
               for t in tools]
    for _ in range(MAX_STEPS):
        r = await client.messages.create(model=MODEL, max_tokens=1500, system=system,
                                         tools=a_tools, messages=history)
        blocks = []
        for b in r.content:
            if b.type == "text":
                blocks.append({"type": "text", "text": b.text})
            elif b.type == "tool_use":
                blocks.append({"type": "tool_use", "id": b.id, "name": b.name, "input": b.input})
        history.append({"role": "assistant", "content": blocks})
        uses = [b for b in blocks if b["type"] == "tool_use"]
        if r.stop_reason != "tool_use" or not uses:
            return "".join(b["text"] for b in blocks if b["type"] == "text").strip()
        results = []
        for u in uses:
            text, err, ms = await _call_tool(session, u["name"], u["input"])
            trace.append({"name": u["name"], "args": u["input"], "result": text, "is_error": err, "ms": ms})
            results.append({"type": "tool_result", "tool_use_id": u["id"], "content": text or "(empty)",
                            "is_error": err})
        history.append({"role": "user", "content": results})
    return "Sorry, I could not finish that request (too many tool steps)."


def _openai_client():
    if PROVIDER == "azure":
        from openai import AsyncAzureOpenAI
        return AsyncAzureOpenAI(azure_endpoint=_need("AZURE_OPENAI_ENDPOINT"),
                                api_key=_need("AZURE_OPENAI_API_KEY"),
                                api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21"))
    from openai import AsyncOpenAI
    return AsyncOpenAI()  # reads OPENAI_API_KEY / OPENAI_BASE_URL


async def _loop_openai(session, tools, system, history, trace):
    client = _openai_client()
    o_tools = [{"type": "function", "function": {"name": t.name, "description": t.description or "",
                                                  "parameters": _schema(t)}} for t in tools]
    for _ in range(MAX_STEPS):
        r = await client.chat.completions.create(
            model=MODEL, tools=o_tools or None,
            messages=[{"role": "system", "content": system}] + history)
        m = r.choices[0].message
        entry = {"role": "assistant", "content": m.content or ""}
        if m.tool_calls:
            entry["tool_calls"] = [{"id": tc.id, "type": "function",
                                    "function": {"name": tc.function.name,
                                                 "arguments": tc.function.arguments}} for tc in m.tool_calls]
        history.append(entry)
        if not m.tool_calls:
            return (m.content or "").strip()
        for tc in m.tool_calls:
            try:
                args = json.loads(tc.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}
            text, err, ms = await _call_tool(session, tc.function.name, args)
            trace.append({"name": tc.function.name, "args": args, "result": text, "is_error": err, "ms": ms})
            history.append({"role": "tool", "tool_call_id": tc.id, "content": text or "(empty)"})
    return "Sorry, I could not finish that request (too many tool steps)."


# ---------------------------------------------------------------- public API
def _user_texts(history) -> list[str]:
    """What the human actually typed (our own SYSTEM CHECK nudges are not user figures)."""
    out = []
    for m in history:
        if m["role"] == "user" and isinstance(m["content"], str) and not m["content"].startswith(CHECK_PREFIX):
            out.append(m["content"])
    return out


def _pick_tools(all_tools, prompt_name: str):
    """Returns (tools to expose, note or None)."""
    names = {t.name for t in all_tools}
    if _allowed_env.upper() == "ALL":
        return list(all_tools), None
    wanted = [x.strip() for x in _allowed_env.split(",") if x.strip()] or \
             (DOCUMENTED_TOOLS if prompt_name == "guarded" else [])
    if not wanted:
        return list(all_tools), None
    chosen = [t for t in all_tools if t.name in wanted]
    if not chosen:  # names did not match the server: do not leave the model with zero tools
        return list(all_tools), f"none of {wanted} exist on the server (has: {sorted(names)}); exposing all tools"
    return chosen, None


async def _advisor_context(session, all_tools, trace) -> str:
    """get_advisor_context once per process. Failure is not cached and is visible in the trace."""
    global _advisor_cache
    if _advisor_cache is not None:
        return _advisor_cache
    if not any(t.name == "get_advisor_context" for t in all_tools):
        _advisor_cache = ""
        return ""
    text, err, ms = await _call_tool(session, "get_advisor_context", ADVISOR_ARGS)
    trace.append({"name": "get_advisor_context", "args": ADVISOR_ARGS, "result": text, "is_error": err, "ms": ms})
    if err or not text.strip():
        return ""
    # the tool says: "inject the 'context' field into your system prompt" -> use it if the reply is JSON
    try:
        obj = json.loads(text)
        if isinstance(obj, dict) and isinstance(obj.get("context"), str) and obj["context"].strip():
            text = obj["context"]
    except (json.JSONDecodeError, TypeError):
        pass
    _advisor_cache = text
    return text


async def ask(history: list, user_text: str, prompt_name: str | None = None,
              strict: bool | None = None) -> TurnResult:
    """Run one user turn. `history` is mutated (provider-specific message dicts)."""
    prompt_name = prompt_name or PROMPT_NAME
    system = PROMPTS[prompt_name]
    strict = STRICT if strict is None else strict
    trace: list[dict] = []
    warnings: list[str] = []
    history.append({"role": "user", "content": user_text})
    loop = _loop_anthropic if PROVIDER == "anthropic" else _loop_openai

    async with _http_client(MCP_URL) as streams:
        read, write = streams[0], streams[1]
        async with ClientSession(read, write) as session:
            await session.initialize()
            all_tools = (await session.list_tools()).tools
            tools, note = _pick_tools(all_tools, prompt_name)
            if note:
                warnings.append(note)

            context = ""
            if USE_ADVISOR_CONTEXT and prompt_name == "guarded":
                context = await _advisor_context(session, all_tools, trace)
                if not context:
                    warnings.append("get_advisor_context returned nothing; running without the server playbook")
            if context:
                system = system + "\n\n## Server playbook (returned by the get_advisor_context tool; use it for how to call the tools, but the rules above win if they conflict)\n" + context

            reply = await loop(session, tools, system, history, trace)

            if strict:
                # the playbook is excluded on purpose: only figures from real answers count
                answers = [t["result"] for t in trace if t["name"] != "get_advisor_context"]
                typed = _user_texts(history)
                bad = unverified_amounts(reply, answers + typed, user_sources=typed)
                if bad:  # one corrective retry, then fall back to a visible warning
                    history.append({"role": "user", "content": (
                        f"{CHECK_PREFIX} your answer contained rupee figures that no tool returned: "
                        f"{', '.join(bad)}. Rewrite the answer using only figures from tool results "
                        "(or remove them / call a tool that returns them). Do not mention this check.")})
                    reply = await loop(session, tools, system, history, trace)
                    answers = [t["result"] for t in trace if t["name"] != "get_advisor_context"]
                    bad = unverified_amounts(reply, answers + typed, user_sources=typed)
                if bad:
                    warnings.append(f"Figures not returned by any tool: {', '.join(bad)}")
                    reply += ("\n\n⚠️ Some figures above were not returned by Great.cards tools "
                              f"and may be wrong: {', '.join(bad)}")
            if POSTCHECKS and prompt_name == "guarded":
                # make sure details exist for the cards the answer is about (max 3 extra tool calls)
                for alias in postchecks.cards_to_check(reply, trace):
                    text, err, ms = await _call_tool(session, "get_card_details", {"card_alias": alias})
                    trace.append({"name": "get_card_details", "args": {"card_alias": alias}, "result": text,
                                  "is_error": err, "ms": ms, "by": "postcheck"})
                notes = (postchecks.fee_notes(reply, trace) + postchecks.availability_notes(reply, trace)
                         + postchecks.exclusion_notes(reply, trace) + postchecks.label_notes(reply, trace)
                         + postchecks.spend_notes(reply, trace))
                if notes:
                    reply += "\n\n" + "\n".join(notes)
            for f in flag_phrases(reply):
                warnings.append(f"guardrail tripwire: {f}")
    return TurnResult(reply=reply, tool_calls=trace, warnings=warnings)


def ask_sync(history, user_text, **kw) -> TurnResult:
    return asyncio.run(ask(history, user_text, **kw))