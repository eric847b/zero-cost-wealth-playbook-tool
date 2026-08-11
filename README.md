# Zero-Cost Wealth Playbook Tool

Personal wealth acceleration using **only free tools**. No paid APIs, no subscriptions required.

## Playbook

Read **[PLAYBOOK.md](PLAYBOOK.md)** — track → free stack → first three monetization moves → weekly loop.

## Tracker

Local CSV ledger + CLI — works offline, imports into LibreOffice Calc or Google Sheets.

```bash
python tracker.py add 100 income freelance "template sale"
python tracker.py add 12.50 expense software "domain renewal"
python tracker.py list
python tracker.py summary
```

Ledger path: `data/ledger.csv`  
Columns: `date, type, amount, category, note`

## Runway (currency velocity)

```bash
python runway.py --sample   # demo from sample ledger
python runway.py            # your data/ledger.csv → runway_report.md
```

Reports weekly in/out/net, conservative runway weeks, top income categories, and next currency moves. Stdlib only.

## Income experiments (rank by expected $ / effort)

```bash
python scripts/income_experiment.py list
python scripts/income_experiment.py rank
python scripts/income_experiment.py add "setup-session" 149 3 "45-min client setup"
python scripts/income_experiment.py status 2 active
python scripts/income_experiment.py summary
```

Board: `data/income_experiments.csv`

## Free quote / invoice

```bash
python scripts/quote.py --client "Acme" --item "Cashflow setup" --amount 149 --type quote
python scripts/quote.py --client "Acme" --item "Monthly review" --amount 79 --type invoice --due 14
```

Writes Markdown under `quotes/`. Template: [templates/invoice_quote.md](templates/invoice_quote.md).

## Export (print / PDF)

```bash
python export.py --sample
python export.py
python export.py --client path/to/client_ledger.csv
```

## Client / Monetization (zero fixed cost)

| File | Purpose |
|------|---------|
| [templates/client_ledger_template.csv](templates/client_ledger_template.csv) | Client starter ledger |
| [templates/client_playbook.md](templates/client_playbook.md) | One-page adaptation guide |
| [templates/client_onboarding_checklist.md](templates/client_onboarding_checklist.md) | Day-0 to Day-7 checklist |
| [templates/pricing_notes.md](templates/pricing_notes.md) | Packaging / pricing |
| [templates/sales_one_pager.md](templates/sales_one_pager.md) | Listing + email copy |
| [templates/invoice_quote.md](templates/invoice_quote.md) | Manual quote/invoice fill-in |
| [templates/niches/](templates/niches/) | Niche cashflow playbooks + sample weeks |

```bash
python scripts/pack_client.py   # → dist/zero-cost-client-pack.zip (all niches)
```

Niches: Creator · Consultant · Agency · Freelancer · SaaS/Indie · Marketplace · Coach · OSS · Newsletter · Local Services.

## Autonomy model
- **AI / software owns:** issues, niche templates, pack script, fleet workflows, runway/experiment CLIs.
- **Owner is not required** for day-to-day currency artifacts.

## Status
- Currency catalyst #21 closed: runway + income experiments + free quote CLI shipped and verified.
- Keep everything zero-cost.
