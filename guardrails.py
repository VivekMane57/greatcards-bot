"""Programmatic guardrails that do not depend on the LLM obeying the prompt.

1. unverified_amounts(): every rupee figure in the reply must appear in a tool
   result (or in what the user typed). Otherwise it is flagged / retried.
2. flag_phrases(): cheap regex tripwires for approval promises and tax advice.

Known limitation (say this in the note): a correct *derived* number (e.g. a sum)
is also flagged. That is intentional: the rule is "show only what tools returned".
"""
from __future__ import annotations
import re

_MULT = {"k": 1e3, "lakh": 1e5, "lakhs": 1e5, "lac": 1e5, "lacs": 1e5,
         "crore": 1e7, "crores": 1e7, "cr": 1e7}

# ₹15,000 | Rs. 1.5 lakh | INR 20k
_PREFIXED = re.compile(
    r"(?:₹|Rs\.?|INR)\s*(\d[\d,]*(?:\.\d+)?)\s*(lakhs?|lacs?|crores?|cr|k)?(?![A-Za-z])",
    re.I)
# 15,000 rupees
_SUFFIXED = re.compile(
    r"(\d[\d,]*(?:\.\d+)?)\s*(lakhs?|lacs?|crores?|cr|k)?\s*(?:rupees|rs\b)", re.I)
# any number, optionally with unit (used to build the allowed set)
_ANY = re.compile(r"(\d[\d,]*(?:\.\d+)?)\s*(lakhs?|lacs?|crores?|cr|k)?(?![A-Za-z])", re.I)


def _val(num: str, unit: str | None) -> float:
    v = float(num.replace(",", ""))
    if unit:
        v *= _MULT[unit.lower()]
    return v


def allowed_numbers(sources: list[str]) -> set[float]:
    out: set[float] = set()
    for s in sources:
        for m in _ANY.finditer(s or ""):
            try:
                out.add(_val(m.group(1), m.group(2)))
                out.add(_val(m.group(1), None))  # also the bare number
            except ValueError:
                pass
    return out


def amounts_in(text: str) -> list[tuple[str, float]]:
    found = []
    for pat in (_PREFIXED, _SUFFIXED):
        for m in pat.finditer(text or ""):
            try:
                found.append((m.group(0).strip(), _val(m.group(1), m.group(2))))
            except ValueError:
                pass
    return found


def unverified_amounts(reply: str, sources: list[str], user_sources: list[str] = ()) -> list[str]:
    """Rupee figures in `reply` that appear in none of `sources`.

    `user_sources` = what the user typed. Their own figures converted between monthly and annual
    (x12, /12) are also allowed, because the prompt lets the bot do that unit conversion for the
    tool call (and must say so). Nothing else derived is allowed.
    """
    allowed = allowed_numbers(sources)
    for v in list(allowed_numbers(list(user_sources))):
        allowed.update((v * 12, v / 12))
    bad = []
    for text, v in amounts_in(reply):
        if v == 0:
            continue
        if not any(abs(v - a) <= 0.51 for a in allowed):
            bad.append(text)
    return sorted(set(bad))


_APPROVAL = re.compile(
    r"(guarantee[sd]?\s+(?:approval|to be approved)|will (?:definitely |certainly )?be approved|"
    r"you(?:'| a)re (?:sure|certain) to (?:get|be)|100\s*%\s*approv|assured approval|"
    r"you will (?:definitely |surely )?get (?:this|the|a) card)", re.I)
_TAX = re.compile(
    r"(80\s*c\b|80\s*d\b|income tax|tax[- ]sav|tax deduct|deductible|tax benefit|"
    r"reduce your tax|\bGST (?:input|credit|refund))", re.I)


_REFUSAL = re.compile(r"(can't|cannot|can not|won't|will not|unable|not able|not allowed|never|no one can|outside what i|"
                      r"i'm sorry|i am sorry|not guarantee|no guarantee|couldn't|isn't allowed)", re.I)


def _real_hit(pattern, text: str) -> bool:
    """A tripwire only counts when the match is NOT inside a refusal such as "I can't promise you will be approved"
    or "tax questions like 80C are outside what I can help with" (checked in the 80 characters around the match)."""
    for m in pattern.finditer(text or ""):
        around = text[max(0, m.start() - 80): m.end() + 80]
        if not _REFUSAL.search(around):
            return True
    return False


def flag_phrases(reply: str) -> list[str]:
    flags = []
    if _real_hit(_APPROVAL, reply):
        flags.append("approval_promise")
    if _real_hit(_TAX, reply):
        flags.append("tax_advice_language")
    return flags