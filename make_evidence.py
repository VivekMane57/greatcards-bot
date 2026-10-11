"""Builds evidence/F1.md ... F19.md from the raw result files in results/.

Each evidence file holds, for one finding, the exact question, the bot's full answer and every raw tool call
(arguments and tool output) copied unchanged from results/*.md. Only one thing is shortened: the big
get_advisor_context dump (about 13K tokens, the same in every run), replaced by one line that points to the source file.

Usage:  python make_evidence.py
"""
import re
import sys
from pathlib import Path

RES = Path("results")
OUT = Path("evidence")

# finding -> (title, [(result file, question number, run number or None for all runs), ...])
MAP = {
    1: ("Q16 tax advice", [("before.md", 16, None), ("after.md", 16, None)]),
    2: ("Q17 investment advice", [("before.md", 17, None), ("after.md", 17, None)]),
    3: ("Q12 to Q14 invented pincode", [("before.md", 12, None), ("before.md", 13, None), ("before.md", 14, None),
                                       ("after_v2_repeat.md", 12, None),
                                       ("after_v3.md", 12, None), ("after_v3.md", 13, None), ("after_v3.md", 14, None)]),
    4: ("Q12 to Q14 eligibility barely changes with income", [("before.md", 12, None), ("before.md", 13, None), ("before.md", 14, None)]),
    5: ("Q20 unit converted twice", [("before.md", 20, None), ("after_v2.md", 20, None)]),
    6: ("Q10, Q11 marketing claim shown as savings", [("after.md", 10, None), ("after_v2.md", 11, None)]),
    7: ("Q10, Q11 card-name resolver removed", [("after.md", 10, None), ("after.md", 11, None),
                                               ("after_v2.md", 10, None), ("after_v2.md", 11, None)]),
    8: ("Q1 joining fee not subtracted", [("after_v2.md", 1, None), ("after_v3_recommend.md", 1, None)]),
    9: ("Q2 card that may not be open to new customers", [("after.md", 2, None), ("after_v3_recommend.md", 2, None)]),
    10: ("Q6 lounge numbers mixed up", [("after.md", 6, None)]),
    11: ("Q4 and Q2 monthly figure labelled annual", [("after.md", 4, None), ("after_v3_recommend.md", 2, None)]),
    12: ("Q4 own x12 conversion not labelled", [("after_v2.md", 4, None)]),
    13: ("Q7, Q8 wrong question answered", [("before.md", 7, None), ("before.md", 8, None),
                                           ("after.md", 7, None), ("after.md", 8, None)]),
    14: ("Q19 made-up links, filter returns paid cards", [("before.md", 19, None), ("after.md", 19, None)]),
    15: ("Q18 blocked by the provider, Q21 reworded", [("before_18_20.md", 18, None), ("after_18_20.md", 18, None),
                                                    ("before_21.md", 21, None), ("after_21.md", 21, None)]),
    16: ("Q1, Q20 over-asking", [("before.md", 1, None), ("after.md", 1, None), ("after.md", 20, None),
                                ("after_v2.md", 1, None), ("after_v2.md", 20, None)]),
    17: ("Q2 fuel claim vs exclusions", [("after_v3_recommend.md", 2, None), ("after_v4.md", 2, None)]),
    18: ("Restricted flags on top picks", [("after_v3_recommend.md", 1, None), ("after_v3_recommend.md", 2, None)]),
    19: ("Q10 'based on your spend' with compare_cards only", [("after_v4_q10.md", 10, None), ("after_v5_q10.md", 10, None)]),
}

ADVISOR = re.compile(r"<details><summary>get_advisor_context.*?</details>", re.S)
HEAD = re.compile(r"^## Q(\d+) run (\d+)", re.M)


def blocks(path):
    text = path.read_text(encoding="utf-8")
    ms = list(HEAD.finditer(text))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        out[(int(m.group(1)), int(m.group(2)))] = text[m.start():end].rstrip()
    return out


def main():
    OUT.mkdir(exist_ok=True)
    cache, missing = {}, []
    for fid, (title, parts) in MAP.items():
        body = [f"# Evidence for F{fid}: {title}", "",
                "Copied unchanged from the result files named below. Only the get_advisor_context dump is shortened "
                "(it is identical in every run); the full text is in the source file. See failures.md for the explanation.", ""]
        for fname, q, run in parts:
            p = RES / fname
            if fname not in cache:
                cache[fname] = blocks(p) if p.exists() else None
            b = cache[fname]
            body.append(f"---\n\n## Source: results/{fname}, Q{q}\n")
            if b is None:
                body.append(f"NOT FOUND: results/{fname} is missing.\n"); missing.append((fid, fname, q)); continue
            keys = sorted(k for k in b if k[0] == q and (run is None or k[1] == run))
            if not keys:
                body.append(f"NOT FOUND: no Q{q} in results/{fname}.\n"); missing.append((fid, fname, q)); continue
            for k in keys:
                blk = ADVISOR.sub(f"[get_advisor_context result omitted here, full text in results/{fname}]", b[k])
                body.append(blk + "\n")
        (OUT / f"F{fid}.md").write_text("\n".join(body), encoding="utf-8")
        print(f"wrote evidence/F{fid}.md")
    if missing:
        print("\nMISSING (check these files in results/):")
        for m in missing:
            print("  F%d: results/%s Q%d" % m)


if __name__ == "__main__":
    sys.exit(main())