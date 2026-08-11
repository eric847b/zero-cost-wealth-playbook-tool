# Setup Session — Delivery Checklist (operator)

Use during the live 45–60 min session. Pair with [setup_session_sow.md](setup_session_sow.md).

## Pre-call (5 min)

- [ ] Quote sent: `python scripts/quote.py --client "..." --item "Cashflow setup session (45–60 min)" --amount 149 --type quote`
- [ ] Client pack ready: `python scripts/pack_client.py` (or repo clone link)
- [ ] This checklist + SOW open

## Live session

### 1. Environment (5 min)
- [ ] Python 3 confirmed
- [ ] Toolkit or zip extracted
- [ ] `data/ledger.csv` created from template

### 2. First rows (10 min)
- [ ] 1–3 real income/expense rows logged (`tracker.py add`)
- [ ] `python tracker.py summary` runs clean

### 3. Velocity + report (10 min)
- [ ] `python runway.py` (or on their ledger path)
- [ ] `python export.py --client data/ledger.csv`
- [ ] Show Print → Save as PDF once

### 4. Experiment + habit (10 min)
- [ ] `python scripts/income_experiment.py add ...` for their top idea **or** rank existing board
- [ ] Write **one** next-week action in the export notes / chat
- [ ] Point at Day 1–7 section of `client_onboarding_checklist.md`

### 5. Close (5 min)
- [ ] Confirm they can add a row solo
- [ ] Send: report Markdown/PDF + checklist + invoice if not prepaid
- [ ] Optional: book monthly review

## Post-call

- [ ] Mark experiment `setup-session-offer` status → `won` if paid+delivered, else keep `active`
- [ ] Log fee as income: `python tracker.py add <amount> income consulting "setup session <client>"`
- [ ] Archive quote under `quotes/`

## Timing budget

| Block | Minutes |
|-------|--------|
| Pre-call | 5 |
| Live | 40–50 |
| Post-call | 5–10 |
| **Total** | **~60** |
