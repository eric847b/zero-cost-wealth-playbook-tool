# Zero-Cost Wealth Playbook Tool

Personal wealth acceleration using **only free tools**. No paid APIs, no subscriptions required.

## Public listing

See **[PUBLIC_LISTING.md](PUBLIC_LISTING.md)** — blurb, price anchors, email CTA, pack build steps.  
Repo is public; paste the blurb to Gumroad/Lemon free tier when ready.

```bash
python scripts/pack_client.py   # → dist/zero-cost-client-pack.zip (~42KB verified)
```

## Playbook

Read **[PLAYBOOK.md](PLAYBOOK.md)** — track → free stack → monetization moves → weekly loop.

## Tracker

```bash
python tracker.py add 100 income freelance "template sale"
python tracker.py summary
```

## Runway / experiments / quotes

```bash
python runway.py --sample
python scripts/income_experiment.py rank
python scripts/quote.py --client "Acme" --item "Cashflow setup session (45–60 min)" --amount 149 --type quote
```

## Setup session (sellable)

| File | Purpose |
|------|---------|
| [templates/setup_session_sow.md](templates/setup_session_sow.md) | SOW |
| [templates/setup_session_checklist.md](templates/setup_session_checklist.md) | Live delivery checklist |

## Client pack contents

`tracker.py` · `runway.py` · `export.py` · `scripts/quote.py` · `scripts/income_experiment.py` · templates (incl. SOW) · sample data · niches

## Status
- #21 closed (runway + experiments + quote CLI).
- **Listed publicly:** `PUBLIC_LISTING.md` + updated pack (commit `b072c38`).
- Experiment #1 **active** (GitHub listing surface live; optional marketplace paste still open).
- Experiment #2 **active** — SOW ready; **not** marked `won` (no paid delivery; ledger stays clean).
- Keep everything zero-cost. Never log simulated income.
