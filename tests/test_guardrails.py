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


def test_user_unit_conversion_allowed():
    user = "school fees are 36,000 a year"
    assert unverified_amounts("I passed Rs 3,000 a month.", [TOOL, user], user_sources=[user]) == []
    assert unverified_amounts("I passed Rs 3,000 a month.", [TOOL, user]) != []  # no conversion allowance
    assert unverified_amounts("You'd earn Rs 4,321.", [TOOL, user], user_sources=[user]) != []


def test_tripwires():
    assert "approval_promise" in flag_phrases("You will definitely be approved!")
    assert "tax_advice_language" in flag_phrases("Rent is deductible under 80C")
    assert flag_phrases("Check the bank's terms.") == []


if __name__ == "__main__":
    for k, v in list(globals().items()):
        if k.startswith("test_"):
            v(); print("ok", k)