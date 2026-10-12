# MCP fix spec: recommend_cards does not subtract the joining fee, but its description says it does

Tool: `recommend_cards` (server version 1.6.1). Evidence: raw calls logged 2026-10-10 23:37 to 23:50 IST (logs/probe_calls.jsonl, calls #3, #7 and #9 of that file). Status: tested on 3 calls, 20 ranked rows (5 brief + 5 full + 10 full); the joining-fee check was done on the 15 full-format rows, which carry the fee fields.

## What's wrong
The tool description says cards are ranked by "NET ANNUAL SAVINGS (rewards earned + lounge value + milestone benefits - joining fee - annual fee)". The numbers it returns follow a different rule: rewards + milestone + lounge - annual fee. The joining fee is never subtracted. The server's own `_format_hint` in the response says the same shorter formula, so the description and the response disagree with each other.

In all 15 full-format ranked cards across calls #7 and #9, the returned net savings equals the shorter formula exactly (to the rupee). For every card with a joining fee, it differs from the description's formula by exactly the joining fee.

## Worked example 1 (amazon_spends = 15000, response_format = full)
| Tool rank | Card | Rewards | Joining fee | Annual fee charged | Tool net | Net per description | Rank per description |
|---|---|---|---|---|---|---|---|
| 1 | HDFC Millenia | 9,000 | 1,180 | 0 (waived at 1,00,000 spend; this profile spends 1,80,000) | 9,000 | 7,820 | 5 |
| 2 | ICICI Amazon Pay | 9,000 | 0 | 0 | 9,000 | 9,000 | 1 |
| 3 | Swiggy HDFC | 9,000 | 590 | 0 | 9,000 | 8,410 | 3 |
| 4 | BOB Cashback | 9,000 | 589 | 589 | 8,411 | 7,822 | 4 |
| 5 | CRED IndusInd | 9,000 | 0 | 589 | 8,411 | 8,411 | 2 |

Three cards tie at 9,000 and HDFC Millenia (joining fee 1,180) is shown first. Under the description's formula the user's best card is ICICI Amazon Pay and Millenia drops to last of these five.

Which rows are clear and which are ambiguous (correction to my first draft): the clear cases are cards whose ANNUAL fee is waived by spend but that still charge a JOINING fee: HDFC Millenia (1,180), Swiggy HDFC (590), and in example 2 SBI Aurum and Yes Bank Marquee (11,799 each) and Diners Black (11,800). Their tool net ignores a fee the user pays when the card is issued (the SBI Cashback details say "a one-time joining fee is charged at the time of card issuance"). The BOB Cashback and Magnus Burgundy rows are ambiguous: joining and annual fee are the same amount, so subtracting both (the literal description formula) may double count year one. The "Net per description" column for those rows is the literal arithmetic, not necessarily the right answer. That ambiguity is itself part of the issue: the tool never says whether it computes year-one or steady-state savings.

## Worked example 2 (amazon_spends = 100000, top_n = 10, full)
Tool net vs description net for cards with a joining fee: BOB Etihad Guest 56,000 vs 50,100 (joining 5,900); SBI Aurum 54,999 vs 43,200 (11,799); Yes Bank Marquee 54,000 vs 42,201 (11,799); HDFC Diners Black 46,000 vs 34,200 (11,800). Among the 10 cards returned, ixigo AU (free, 50,000) moves from tool rank 6 to rank 4, and Diners Black from 7 to 9.

## Expected behaviour
Decide and document one rule, and make the description, the `_format_hint` and the numbers agree. If the intent is year-one net savings, subtract the joining fee (and say whether welcome benefits are added back). If the intent is a recurring yearly figure, the description must stop mentioning the joining fee, and the response should label the figure as excluding it. Either way, show a separate "first-year cost" for cards with a joining fee.

## What I could not determine (not tested or not knowable from outside)
- Which of the two rules the product owner intends.
- Whether welcome benefits (the response has a `welcome_benefits` block with `cash_value`) were meant to offset the joining fee. They are not in either formula.
- Whether cards outside the returned top N would enter the top N after the change (I only re-ranked the cards returned).

## How to test
1. For a fixed profile (amazon_spends = 15000), assert for every returned card: net == rewards + milestone + lounge - annual_fee_charged - joining_fee (or the documented alternative).
2. Assert the tool description, `_format_hint` and the formula in code are the same sentence.
3. Same-rank tie-break: when two cards tie on net savings, the order should be defined (for example lower total fee first).
4. Regression: re-run this profile; ICICI Amazon Pay should be rank 1 under the description's formula.

## Impact
Premium cards with joining fees of 5,000 to 12,000 rupees look 5,000 to 12,000 rupees better than the description promises, so they can rank above free or low-fee cards. A user who trusts "net annual savings" sees a number that is higher than their first-year gain by the joining fee.

---
## Other findings from the same logs (shorter, each tested)
- `top_spend_categories[].annual_value` holds MONTHLY values: Amazon 15,000 gives "750" per card while annual_rewards_value is 9,000 (750 x 12). Same at 100,000 (5,000 vs 60,000). The label says annual.
- `recommend_cards` with no arguments returns 5 cards, all net 0, no error and no warning.
- `list_cards` says total_available 258 but showing 100 with limit=100; the `bank` field is empty for 100 of the 100 cards in brief format.
- `get_card_details` for SBI Cashback has `existing_customer_only: true`; `recommend_cards` output has no such flag, so a user can be shown a card they cannot get.
- Eligibility fields contradict each other (SBI Cashback and BOB Cashback): `income_salaried_lpa: 3` (25,000 a month) vs `min_income_monthly: 30000` (3.6 LPA).
- Lounge value is not annualised (one profile, tested; logs/probe_calls.jsonl line 13, logged 2026-10-11 02:00 IST, flights_annual 600000, hotels_annual 300000, domestic_lounge_usage_quarterly 3). Input domestic_lounge_usage_quarterly = 3 (12 visits a year). The description values a domestic visit at 750, so a year is 12 x 750 = 9,000. Every card with lounge access returns lounge_value "₹2,250" (3 x 750 = one quarter) and that figure is added into the annual net savings. The category line for the same card shows 750, which is the monthly value (3 visits per quarter = 1 a month), the same monthly-labelled-as-annual problem as above. Net savings for lounge cards are understated by about 6,750 in this example.
- Float noise is shown to users (same call, line 13; the 8,333.333 and 4,166.667 values are in rank 2 of that call): annual_rewards_value "₹2,42,999.994", "₹1,08,000.002", milestone "₹36,800.001", annual_value "₹8,333.333".
- Internal or odd values leak into output: category name `new_monthly_cat_1`, `all_pharmacy` (not one of the 21 input keys), a milestone value of "₹36,800.001", card names with typos ("Swiggy Ornge HDFC Bank Credit card ", "ixigo AU credot Card").