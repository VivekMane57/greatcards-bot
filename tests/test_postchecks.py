import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from postchecks import fee_notes, availability_notes, cards_to_check, exclusion_notes, label_notes, spend_notes

REC = json.dumps({"recommendations": [
    {"rank": 1, "card_name": "HDFC MILLENIA", "net_annual_savings": "₹9,000", "joining_fee": "₹1,180 (incl. GST)",
     "card_alias": "hdfc-millenia-credit-card"},
    {"rank": 2, "card_name": "ICICI Amazon Pay Credit Card", "net_annual_savings": "₹9,000", "joining_fee": "Free",
     "card_alias": "icici-amazon-pay-credit-card"}]})
TRACE = [{"name": "recommend_cards", "args": {"amazon_spends": 15000}, "result": REC, "is_error": False}]


def test_fee_note_for_card_with_joining_fee():
    n = fee_notes("The HDFC Millenia saves ₹9,000 a year.", TRACE)
    assert len(n) == 1 and "₹1,180 (incl. GST)" in n[0] and "does not subtract" in n[0]


def test_no_fee_note_for_free_card():
    assert fee_notes("ICICI Amazon Pay Credit Card is free.", TRACE) == []


def test_short_name_falls_back_to_top_row():
    assert len(fee_notes("The Millenia card is best.", TRACE)) == 1  # name not matched -> top row


def test_cards_to_check_and_availability():
    assert cards_to_check("HDFC MILLENIA is best", TRACE) == ["hdfc-millenia-credit-card"]
    det = json.dumps({"name": "HDFC Millenia Credit Card", "card_alias": "hdfc-millenia-credit-card",
                      "existing_customer_only": True, "invite_only": False})
    trace = TRACE + [{"name": "get_card_details", "args": {"card_alias": "hdfc-millenia-credit-card"},
                      "result": det, "is_error": False}]
    assert cards_to_check("HDFC MILLENIA is best", trace) == []
    n = availability_notes("HDFC MILLENIA is best", trace)
    assert n and "existing customers only" in n[0] and "invite" not in n[0]


def test_invite_only_and_not_mentioned():
    det = json.dumps({"name": "HDFC Infinia Credit Card", "card_alias": "hdfc-infinia-credit-card",
                      "invite_only": True, "existing_customer_only": False})
    trace = [{"name": "get_card_details", "args": {}, "result": det, "is_error": False}]
    assert "invite only" in availability_notes("Infinia is strong", trace)[0]
    assert availability_notes("Something unrelated", trace) == []


def test_bad_json_is_safe():
    t = [{"name": "recommend_cards", "args": {}, "result": "TOOL ERROR: x", "is_error": True}]
    assert fee_notes("x", t) == [] and cards_to_check("x", t) == [] and availability_notes("x", t) == []


SBI_REC = json.dumps({"recommendations": [{"rank": 1, "card_name": "SBI CASHBACK ", "net_annual_savings": "₹12,000",
    "annual_rewards_value": "₹12,000", "joining_fee": "₹1,179 (incl. GST)", "card_alias": "sbi-cashback-credit-card",
    "top_spend_categories": [{"category": "grocery_spends_online", "annual_value": "₹1,000"},
                             {"category": "flipkart_spends", "annual_value": "₹0"}]}]})
SBI_DET = json.dumps({"name": "SBI Cashback Credit Card", "card_alias": "sbi-cashback-credit-card",
    "rewards": {"exclusions": "Fuel Transactions, Rent Payments, Education Payments, Insurance Premium Payments"}})
SBI_TRACE = [{"name": "recommend_cards", "args": {"grocery_spends_online": 20000, "fuel": 5000, "rent": 0},
              "result": SBI_REC, "is_error": False},
             {"name": "get_card_details", "args": {}, "result": SBI_DET, "is_error": False}]


def test_exclusion_note_for_fuel():
    n = exclusion_notes("SBI Cashback is the top pick for groceries and fuel", SBI_TRACE)
    assert n and "Fuel Transactions" in n[0] and "fuel spend" in n[0] and "rent" not in n[0]


def test_no_exclusion_note_without_matching_spend():
    tr = [dict(SBI_TRACE[0], args={"grocery_spends_online": 20000}), SBI_TRACE[1]]
    assert exclusion_notes("SBI Cashback", tr) == []


def test_label_note_monthly_figure():
    n = label_notes("Grocery cashback: ₹1,000 annual value", SBI_TRACE)
    assert n and "per-month" in n[0] and "₹12,000" in n[0]
    assert label_notes("It saves ₹12,000 a year", SBI_TRACE) == []  # the figure is not quoted


def test_label_note_silent_when_numbers_do_not_prove_monthly():
    rec = json.loads(SBI_REC); rec["recommendations"][0]["annual_rewards_value"] = "₹5,000"
    tr = [dict(SBI_TRACE[0], result=json.dumps(rec)), SBI_TRACE[1]]
    assert label_notes("₹1,000 annual value", tr) == []


def test_spend_note_when_compare_only():
    tr = [{"name": "compare_cards", "args": {}, "result": "{}", "is_error": False}]
    assert spend_notes("A comparison based on your Rs 20,000 monthly online spending.", tr)
    assert spend_notes("A comparison of the two cards.", tr) == []
    assert spend_notes("based on your spending", tr + [{"name": "recommend_cards", "args": {}, "result": "{}", "is_error": False}]) == []


if __name__ == "__main__":
    for k, v in list(globals().items()):
        if k.startswith("test_"):
            v(); print("ok", k)