"""probe.py - talk to the Great.cards MCP server directly. No AI involved.

Commands
  python probe.py tools                       list every tool (name, description, input schema)
  python probe.py call TOOL key=value ...     call one tool, print and save the raw output
  python probe.py call TOOL --file args.json  same, with arguments read from a JSON file

Examples
  python probe.py tools
  python probe.py call list_cards
  python probe.py call recommend_cards monthly_spend=15000     (use the real argument names from `tools`)

Everything is saved under ./logs/ :
  logs/tools.json          the full tool list from the last `tools` run
  logs/probe_calls.jsonl   one line per call: time, tool, arguments, RAW result (never edited)

Needs: Python 3.10+, and `pip install mcp`. No API key needed.
"""
import argparse
import asyncio
import json
import os
import sys
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path

# Windows consoles often use a legacy encoding and crash on the rupee sign. Force UTF-8.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

from mcp import ClientSession

try:  # newer SDK
    from mcp.client.streamable_http import streamable_http_client as _http_client
except ImportError:  # older SDK
    from mcp.client.streamable_http import streamablehttp_client as _http_client

DEFAULT_URL = "https://bk-api.bankkaro.com/mcp"
LOG_DIR = Path(__file__).resolve().parent / "logs"
TOOLS_FILE = LOG_DIR / "tools.json"
CALL_LOG = LOG_DIR / "probe_calls.jsonl"
BUDGET_WARN = 200  # the assignment says "a few hundred calls is fine"
TIMEOUT = 60  # seconds to wait for the server before giving up


def now():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def dump(obj):
    """Turn an SDK result object into plain JSON-able data, losing nothing."""
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json", by_alias=True)
    return json.loads(json.dumps(obj, default=str))


def pretty(text):
    """Pretty-print text if it is JSON, otherwise return it unchanged (for reading only)."""
    try:
        return json.dumps(json.loads(text), indent=2, ensure_ascii=False)
    except Exception:
        return text


@asynccontextmanager
async def open_session(url):
    """Open one connection and yield (initialised session, initialize result)."""
    async with _http_client(url) as streams:
        # streams has 2 items (new SDK) or 3 items (old SDK); we only need the first two
        async with ClientSession(streams[0], streams[1]) as session:
            init = await session.initialize()
            yield session, init


def explain(exc):
    """One readable line for any error, including grouped errors from the SDK."""
    if isinstance(exc, BaseExceptionGroup):
        return " | ".join(explain(e) for e in exc.exceptions)
    return f"{type(exc).__name__}: {exc}"


async def list_all_tools(session):
    tools, cursor = [], None
    while True:
        if cursor is None:
            res = await session.list_tools()
        else:
            try:
                res = await session.list_tools(cursor=cursor)  # older SDK
            except TypeError:
                from mcp.types import PaginatedRequestParams
                res = await session.list_tools(params=PaginatedRequestParams(cursor=cursor))
        tools.extend(res.tools)
        cursor = getattr(res, "next_cursor", None) or getattr(res, "nextCursor", None)
        if not cursor:
            return tools


async def cmd_tools(url):
    try:
        async with open_session(url) as (session, init):
            info = dump(init)
            tools = [dump(t) for t in await asyncio.wait_for(list_all_tools(session), TIMEOUT)]
    except BaseException as e:
        if isinstance(e, KeyboardInterrupt):
            raise
        sys.exit(f"Could not read the tool list from {url}\n{explain(e)}")
    LOG_DIR.mkdir(exist_ok=True)
    TOOLS_FILE.write_text(
        json.dumps({"fetched_at": now(), "url": url, "initialize": info, "tools": tools},
                   indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Server: {info.get('serverInfo') or info.get('server_info')}")
    instr = info.get("instructions")
    if instr:
        print(f"\nServer instructions:\n{instr}")
    print(f"\n{len(tools)} tools found. Full detail saved to {TOOLS_FILE}\n")
    for i, t in enumerate(tools, 1):
        print("=" * 78)
        print(f"{i}. {t.get('name')}")
        print("-" * 78)
        print(t.get("description") or "(no description)")
        schema = t.get("inputSchema") or t.get("input_schema")
        print("\nInput schema:")
        print(json.dumps(schema, indent=2, ensure_ascii=False))
        extra = {k: v for k, v in t.items()
                 if k not in ("name", "description", "inputSchema", "input_schema") and v}
        if extra:
            print("\nOther fields:")
            print(json.dumps(extra, indent=2, ensure_ascii=False))
        print()


def parse_args(pairs, file):
    args = {}
    if file:
        args.update(json.loads(Path(file).read_text(encoding="utf-8")))
    for p in pairs:
        if "=" not in p:
            sys.exit(f"Bad argument '{p}'. Use key=value (values like 15000, true, [1,2] or \"text\" are read as JSON).")
        k, v = p.split("=", 1)
        try:
            args[k] = json.loads(v)  # numbers, booleans, lists, objects
        except json.JSONDecodeError:
            args[k] = v  # plain text
    return args


def calls_so_far():
    if not CALL_LOG.exists():
        return 0
    with CALL_LOG.open(encoding="utf-8") as f:
        return sum(1 for _ in f)


async def cmd_call(url, tool, args):
    record = {"time": now(), "url": url, "tool": tool, "arguments": args}
    try:
        async with open_session(url) as (session, _init):
            res = await asyncio.wait_for(session.call_tool(tool, args), TIMEOUT)
        record["result"] = dump(res)
        record["error"] = None
    except BaseException as e:  # keep failures as evidence too
        if isinstance(e, KeyboardInterrupt):
            raise
        record["result"] = None
        record["error"] = explain(e)

    LOG_DIR.mkdir(exist_ok=True)
    with CALL_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Tool: {tool}\nArguments: {json.dumps(args, ensure_ascii=False)}\n")
    if record["error"]:
        print(f"CALL FAILED: {record['error']}")
    else:
        result = record["result"]
        if result.get("isError") or result.get("is_error"):
            print("** The server marked this result as an ERROR **\n")
        for item in result.get("content") or []:
            if item.get("type") == "text":
                print(pretty(item.get("text", "")))
            else:
                print(json.dumps(item, indent=2, ensure_ascii=False))
        structured = result.get("structuredContent") or result.get("structured_content")
        if structured:
            print("\n[structuredContent]")
            print(json.dumps(structured, indent=2, ensure_ascii=False))
    n = calls_so_far()
    print(f"\nSaved to {CALL_LOG}  (call #{n} in this log)")
    if n >= BUDGET_WARN:
        print(f"WARNING: {n} calls logged. The assignment allows 'a few hundred'. Slow down.")


def main():
    ap = argparse.ArgumentParser(description="Talk to the MCP server directly (no AI).")
    ap.add_argument("--url", default=os.environ.get("MCP_URL", DEFAULT_URL),
                    help=f"MCP server URL (default: {DEFAULT_URL}, or env MCP_URL)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("tools", help="list all tools with descriptions and input schemas")
    c = sub.add_parser("call", help="call one tool")
    c.add_argument("tool")
    c.add_argument("pairs", nargs="*", help="arguments as key=value")
    c.add_argument("--file", help="JSON file with arguments")
    a = ap.parse_args()

    if a.cmd == "tools":
        asyncio.run(cmd_tools(a.url))
    else:
        asyncio.run(cmd_call(a.url, a.tool, parse_args(a.pairs, a.file)))


if __name__ == "__main__":
    main()