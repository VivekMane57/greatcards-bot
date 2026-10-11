# Great.cards card assistant (chatbot on top of the Great.cards MCP)

A small chatbot: the user describes their spending, the LLM calls the Great.cards MCP tools (https://bk-api.bankkaro.com/mcp, no key needed), and the answer goes through guardrails. There is a Streamlit web UI and a CLI. It works with Azure OpenAI, Anthropic, or any OpenAI-compatible endpoint.

Disclosure: the starter code was generated with AI help, and I tested, changed and documented it myself. The full AI chats are linked in my submission email.

## Run in 5 minutes
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # Windows: copy .env.example .env
# open .env and fill ONE provider (see .env.example). Never commit .env.
streamlit run app.py               # web UI   (or: python cli.py)
```
Try: `I spend 15k a month on Amazon and 8k on groceries. Which card?`
The UI shows every raw tool call under the answer, so you can see what the MCP returned.

Settings I used for the results in this repo (Azure OpenAI, gpt-4o-mini):
```
PROVIDER=azure
ALLOWED_TOOLS=recommend_cards,get_card_details,list_cards,compare_cards,check_eligibility,whatsapp_resolve_card_or_category
```
Other switches: `PROMPT=guarded|baseline`, `STRICT_AMOUNTS=1|0`, `USE_ADVISOR_CONTEXT=1|0`, `POSTCHECKS=1|0`.

## What is in the repo
| File | Purpose |
|---|---|
| `bot.py` | LLM and MCP loop, records every raw tool call, applies the guardrails |
| `prompts.py` | `baseline` (naive, the "before") and `guarded` (the "after") system prompts |
| `guardrails.py` | Code checks: every rupee figure must come from tool output or the user's own text; approval and tax tripwires |
| `postchecks.py` | Code notes added after the answer, from tool data only: joining fee, existing-customer-only / invite-only, rewards exclusions, monthly label |
| `probe.py` | Calls the MCP directly, without an LLM, to collect raw evidence |
| `questions.json`, `run_questions.py` | The test questions (20 plus one reworded, Q21) and the runner |
| `results/*.md` | Raw before/after outputs of every run |
| `failures.md` | Every wrong, made-up, missing or misleading answer, with cause and evidence |
| `docs/MCP_SPEC.md` | Fix spec for the top MCP issue (joining fee), with worked numbers |
| `docs/PRODUCT_NOTE.md` | One-page plain-language note for the product owner |
| `tests/` | Unit tests for the guardrails and the code notes |

## Reproduce the before/after results
```bash
python run_questions.py --prompt baseline --no-strict --out results/before     # naive prompt, all tools
python run_questions.py --out results/after                                    # guarded setup
python run_questions.py --only 10 11 12 --repeat 3 --out results/after_repeat  # chosen questions, repeated
```
Each run writes `results/<name>.md`. Every question hits the MCP server a few times, so please do not loop these.

## Tests
```bash
python -m pytest tests            # or: python tests/test_guardrails.py && python tests/test_postchecks.py
```

## Guardrails
Prompt level: see `GUARDED_PROMPT` in `prompts.py`. In my runs gpt-4o-mini ignored some prompt rules, so the important ones are also in code:
1. No rupee figure the tools did not return. Every amount in the reply is checked against tool output and the user's own text. One automatic rewrite, then a visible warning. A user's figure x12 or /12 is allowed, so an unlabelled conversion can pass.
2. No approval promise, no tax advice: prompt rules plus regex tripwires that warn. The tax tripwire also fires on a correct refusal (known false alarm).
3. Notes added by code from tool data: joining fee not subtracted by the tool, card marked existing-customer-only or invite-only, rewards exclusions that match the user's spend, per-month label.

## Known limits
- One model (gpt-4o-mini) and 1 to 3 runs per question, so a pass is evidence, not proof.
- The number check cannot tell whether a correct figure is relevant to the question.
- The bot can still name a card as "best" and then add a note that it is restricted. The ranking comes from the tool.
- Azure's content filter blocked my original Q18 wording, so Q21 is the same test, reworded.
- Details and evidence: `failures.md`.