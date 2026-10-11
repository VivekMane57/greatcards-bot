"""Code-level checks that run AFTER the model has answered (they do not depend on the model obeying a prompt).

Why this file exists: in my repeat runs the prompt rules "say that net savings exclude the joining fee" and
"check get_card_details before naming a top pick" were ignored 2 out of 2 times by gpt-4o-mini. So these two
checks are done in code, using only text and flags that the tools returned.

  fee_notes(reply, trace)           -> notes about joining fees (tool's recommend_cards net figure ignores it)
  availability_notes(reply, trace)  -> notes when get_card_details says invite_only / existing_customer_only
  cards_to_check(reply, trace)      -> aliases of mentioned cards whose details were never fetched
  exclusion_notes(reply, trace)     -> notes when the card's rewards exclusions list a spend the user gave
  label_notes(reply, trace)         -> notes when a per-category "annual value" figure is really a monthly one
  spend_notes(reply, trace)         -> note when the answer says "based on your spend" but no spend-based tool ran

All figures in the notes are copied from tool output, so they also pass the amount check.
"""
from __future__ import annotations
import json
import re

MAX_DETAIL_CALLS = 3


def _json(text: str):
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None


def recommend_rows(trace: list[dict]) -> list[dict]:
    """All card rows from every recommend_cards result in this turn, in order."""
    rows = []
    for t in trace:
        if t.get("name") != "recommend_cards" or t.get("is_error"):
            continue
        data = _json(t.get("result", ""))
        if isinstance(data, dict):
            rows += [r for r in data.get("recommendations", []) if isinstance(r, dict)]
    return rows


def mentioned_rows(reply: str, rows: list[dict], fallback: bool = True) -> list[dict]:
    """Rows whose card name appears in the reply. If none matches (the model shortened a name),
    fall back to the first row returned, because the answer is almost always about the top card."""
    low = (reply or "").lower()
    hit = []
    seen = set()
    for r in rows:
        name = str(r.get("card_name", "")).strip().lower()
        alias = r.get("card_alias")
        if name and name in low and alias not in seen:
            seen.add(alias)
            hit.append(r)
    if not hit and rows and fallback:
        hit = [rows[0]]
    return hit


_GENERIC = {"credit", "card", "bank", "edition", "metal", "the", "of"}


def _name_mentioned(name: str, alias: str, low: str) -> bool:
    """Full name, alias, or the card's last distinctive word (the model often shortens names)."""
    n = name.strip().lower()
    if n in low or alias.lower() in low:
        return True
    words = [w for w in n.replace("(", " ").replace(")", " ").split() if w not in _GENERIC]
    return bool(words) and len(words[-1]) >= 4 and words[-1] in low


def _has_fee(value) -> bool:
    v = str(value or "").strip().lower()
    return bool(v) and not v.startswith(("free", "nil", "0", "₹0", "none"))


def fee_notes(reply: str, trace: list[dict]) -> list[str]:
    # if the model already fetched card details it looked at specific cards: no top-row fallback
    rows = mentioned_rows(reply, recommend_rows(trace), fallback=not _details(trace))
    notes = []
    for r in rows:
        if _has_fee(r.get("joining_fee")):
            notes.append(f"{str(r['card_name']).strip()}: joining fee {r['joining_fee']}")
    if not notes:
        return []
    return ["Note from the tool data: the net savings figure from the recommendation tool does not "
            "subtract the joining fee (" + "; ".join(notes) + ")."]


def _details(trace: list[dict]) -> dict[str, dict]:
    out = {}
    for t in trace:
        if t.get("name") not in ("get_card_details", "whatsapp_get_card_details") or t.get("is_error"):
            continue
        data = _json(t.get("result", ""))
        if isinstance(data, dict):
            alias = data.get("card_alias") or (t.get("args") or {}).get("card_alias")
            if alias:
                out[alias] = data
    return out


def cards_to_check(reply: str, trace: list[dict]) -> list[str]:
    """Aliases of the cards the answer is about that have no get_card_details result yet."""
    have = _details(trace)
    todo = []
    for r in mentioned_rows(reply, recommend_rows(trace), fallback=not have):
        alias = r.get("card_alias")
        if alias and alias not in have and alias not in todo:
            todo.append(alias)
    return todo[:MAX_DETAIL_CALLS]


def availability_notes(reply: str, trace: list[dict]) -> list[str]:
    """One note per card in the reply (or in the details we hold) that the tool marks as restricted."""
    low = (reply or "").lower()
    notes = []
    for alias, d in _details(trace).items():
        name = str(d.get("name", alias)).strip()
        mentioned = _name_mentioned(name, alias, low) or any(
            str(r.get("card_alias")) == alias
            for r in mentioned_rows(reply, recommend_rows(trace), fallback=False))
        if not mentioned:
            continue
        if d.get("existing_customer_only") is True:
            notes.append(f"{name} is marked existing customers only")
        if d.get("invite_only") is True:
            notes.append(f"{name} is marked invite only")
    if not notes:
        return []
    return ["Note from the card details tool: " + "; ".join(notes) + "."]


# spend key (recommend_cards argument) -> words to look for in the card's rewards exclusions text
_EXCL_WORDS = {
    "fuel": ["fuel"], "rent": ["rent"],
    "insurance_health_annual": ["insurance"], "insurance_car_or_bike_annual": ["insurance"],
    "life_insurance": ["insurance"], "school_fees": ["education", "school"],
    "mobile_phone_bills": ["utilit"], "electricity_bills": ["utilit"], "water_bills": ["utilit"],
    "grocery_spends_online": ["grocer"], "offline_grocery": ["grocer"],
}


def _user_spends(trace: list[dict]) -> dict:
    """Spend keys with a non-zero amount, from the last recommend_cards call."""
    for t in reversed(trace):
        if t.get("name") == "recommend_cards" and isinstance(t.get("args"), dict):
            return {k: v for k, v in t["args"].items() if isinstance(v, (int, float)) and v}
    return {}


def exclusion_notes(reply: str, trace: list[dict]) -> list[str]:
    spends = _user_spends(trace)
    if not spends:
        return []
    low = (reply or "").lower()
    notes = []
    rows = mentioned_rows(reply, recommend_rows(trace), fallback=True)
    for alias, d in _details(trace).items():
        name = str(d.get("name", alias)).strip()
        if not (_name_mentioned(name, alias, low)
                or any(str(r.get("card_alias")) == alias for r in rows)):
            continue
        excl = str((d.get("rewards") or {}).get("exclusions") or "")
        items = [i.strip() for i in excl.split(",") if i.strip()]
        for key in spends:
            for word in _EXCL_WORDS.get(key, []):
                hit = next((i for i in items if word in i.lower()), None)
                if hit:
                    notes.append(f"{name} lists '{hit}' under rewards exclusions, so your {key} spend may earn nothing on this card")
                    break
    if not notes:
        return []
    return ["Note from the card details tool: " + "; ".join(notes) + "."]


def _rupees(text) -> float | None:
    digits = "".join(ch for ch in str(text or "") if ch.isdigit() or ch == ".")
    try:
        return float(digits) if digits else None
    except ValueError:
        return None


def label_notes(reply: str, trace: list[dict]) -> list[str]:
    """top_spend_categories[].annual_value holds MONTHLY amounts (tested on 3 profiles). Only when the numbers
    prove it for this card (monthly x 12 matches the card's yearly rewards) and the reply quotes such a figure."""
    notes = []
    for r in mentioned_rows(reply, recommend_rows(trace), fallback=True):
        total = _rupees(r.get("annual_rewards_value"))
        cats = [c for c in r.get("top_spend_categories", []) if isinstance(c, dict)]
        vals = [(_rupees(c.get("annual_value")), str(c.get("annual_value"))) for c in cats]
        vals = [(v, raw) for v, raw in vals if v]
        if not total or not vals:
            continue
        if abs(sum(v for v, _ in vals) * 12 - total) > 0.02 * total:
            continue  # numbers do not prove "monthly" for this card: say nothing
        quoted = [raw for v, raw in vals if raw in (reply or "") and abs(v - total) > 1]
        if quoted:
            notes.append(f"{str(r.get('card_name')).strip()}: the category figure {', '.join(quoted)} is a per-month amount "
                         f"(the tool's yearly rewards value for this card is {r.get('annual_rewards_value')})")
    if not notes:
        return []
    return ["Note from the tool data: " + "; ".join(notes) + "."]


_BASED_ON_SPEND = re.compile(r"(based on|for|given|according to) your[^.\n]{0,40}(spend|spending)", re.I)


def spend_notes(reply: str, trace: list[dict]) -> list[str]:
    """compare_cards takes no spend input. If the answer says it is based on the user's spend and
    recommend_cards never ran, the sentence is not backed by any tool call (seen in Q10, 2 of 2 runs)."""
    names = [t.get("name") for t in trace if not t.get("is_error")]
    if "compare_cards" not in names or "recommend_cards" in names:
        return []
    if not _BASED_ON_SPEND.search(reply or ""):
        return []
    return ["Note: this comparison uses card details only. The comparison tool does not take your spending, "
            "so no savings were calculated for your spend. Ask for a recommendation with your spends to get that."]