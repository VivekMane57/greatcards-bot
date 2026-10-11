"""Run the 20 questions and save everything needed for failures.md.

  python run_questions.py                       # guarded prompt (after)
  python run_questions.py --prompt baseline --no-strict --out results/before
  python run_questions.py --only 7 16           # re-run selected ids

Outputs <out>.jsonl (machine) and <out>.md (read this, mark failures by hand).
"""
import argparse, json, sys, time, pathlib
import asyncio
import bot

# Windows: the default Proactor loop prints harmless 'Event loop is closed' noise after every turn.
# The Selector loop avoids it.
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Windows consoles/files default to cp1252 and crash on the rupee sign. Force UTF-8.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ap = argparse.ArgumentParser()
ap.add_argument("--prompt", default=None, choices=["baseline", "guarded"])
ap.add_argument("--no-strict", action="store_true")
ap.add_argument("--out", default="results/run")
ap.add_argument("--only", nargs="*", type=int)
ap.add_argument("--repeat", type=int, default=1, help="run each question N times to see if answers vary (model) or repeat (tool/data)")
a = ap.parse_args()

qs = json.loads(pathlib.Path("questions.json").read_text(encoding="utf-8"))
if a.only:
    qs = [q for q in qs if q["id"] in a.only]
out = pathlib.Path(a.out); out.parent.mkdir(exist_ok=True)
jl = open(f"{out}.jsonl", "w", encoding="utf-8")
md = open(f"{out}.md", "w", encoding="utf-8")
md.write(f"# Run: prompt={a.prompt or bot.PROMPT_NAME} strict={not a.no_strict} model={bot.PROVIDER}/{bot.MODEL}\n\n")

for q, rep in [(q, r) for q in qs for r in range(1, a.repeat + 1)]:
    history, turns = [], []
    for t in q["turns"]:
        try:
            r = bot.ask_sync(history, t, prompt_name=a.prompt, strict=not a.no_strict)
            turns.append({"user": t, "reply": r.reply, "tool_calls": r.tool_calls, "warnings": r.warnings})
        except BaseException as e:  # one bad question must not kill the whole run
            if isinstance(e, KeyboardInterrupt):
                raise
            # anyio wraps the real error inside ExceptionGroup(s): dig out the leaf error
            leaf = e
            while getattr(leaf, "exceptions", None):
                leaf = leaf.exceptions[0]
            e = leaf
            msg = str(e)
            if "content_filter" in msg or "content management policy" in msg:
                kind = "BLOCKED BY AZURE CONTENT FILTER (provider-side, before the model answered)"
            else:
                kind = "RUN ERROR"
            turns.append({"user": t, "reply": f"[{kind}] {type(e).__name__}: {msg[:600]}",
                          "tool_calls": [], "warnings": [kind]})
            print(f"Q{q['id']} -> {kind}")
            break
        time.sleep(1)  # be gentle with the production server
    jl.write(json.dumps({**q, "run": rep, "turns_out": turns}, ensure_ascii=False) + "\n")
    md.write(f"## Q{q['id']} run {rep} [{q['category']}]\n**What to check:** {q['check']}\n\n")
    for t in turns:
        md.write(f"**User:** {t['user']}\n\n**Bot:** {t['reply']}\n\n")
        if t["warnings"]:
            md.write("**Warnings:** " + "; ".join(t["warnings"]) + "\n\n")
        for c in t["tool_calls"]:
            md.write(f"<details><summary>{c['name']} {json.dumps(c['args'], ensure_ascii=False)}</summary>\n\n```\n{c['result']}\n```\n</details>\n\n")
    md.write("**Verdict (fill in):** OK / WRONG / MADE-UP / MISSING / MISLEADING → cause: model / MCP / data\n\n---\n\n")
    md.flush(); print(f"Q{q['id']} run {rep} done")