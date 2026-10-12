import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from guardrails import unverified_amounts, flag_phrases

TOOL = '{"annual_fee": 1000, "net_savings": 18450, "cap": "1.5 lakh"}'
USER = "I spend ₹15,000 a month"


def test_returned_figures_pass():
    assert unverified_amounts("Fee is ₹1,000 and you save Rs. 18,450.", [TOOL]) == []


def test_user_figure_passes():
    assert unverified_amounts("On ₹15,000 monthly spend...", [TOOL, USER]) == []


def test_invented_figure_flagged():
    assert unverified_amounts("You'd earn ₹7,777 in rewards", [TOOL, USER]) == ["₹7,777"]


def test_units():
    assert unverified_amounts("Cap is Rs 1.5 lakh", [TOOL]) == []
    assert unverified_amounts("Cap is Rs 2 lakh", [TOOL]) != []
    assert unverified_amounts("fee 1k rupees", [TOOL]) == []


def test_tripwires():
    assert "approval_promise" in flag_phrases("You will definitely be approved!")
    assert "tax_advice_language" in flag_phrases("Rent is deductible under 80C")
    assert flag_phrases("Check the bank's terms.") == []


def test_tripwires_ignore_refusals():
    assert flag_phrases("I can't promise you will be approved; the bank decides.") == []
    assert flag_phrases("Tax questions like 80C are outside what I can help with.") == []
    assert flag_phrases("Since your ITR income is 6 lakh, here are cards.") == []
    assert "approval_promise" in flag_phrases("You will definitely be approved!")


if __name__ == "__main__":
    for k, v in list(globals().items()):
        if k.startswith("test_"):
            v(); print("ok", k)