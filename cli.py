"""Command-line chat.  Run: python cli.py"""
import bot

history: list = []
print(f"Great.cards assistant ({bot.PROVIDER}/{bot.MODEL}, prompt={bot.PROMPT_NAME}). Ctrl-C to quit.\n")
while True:
    try:
        q = input("you> ").strip()
    except (EOFError, KeyboardInterrupt):
        break
    if not q:
        continue
    try:
        r = bot.ask_sync(history, q)
    except Exception as e:
        print(f"  [error] {bot.explain(e)}\n")
        continue
    for t in r.tool_calls:
        print(f"  [tool] {t['name']} {t['args']}")
    print(f"\nbot> {r.reply}\n")
    for w in r.warnings:
        print(f"  [warn] {w}")