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
| [templates/niches/creator_cashflow_playbook.md](templates/niches/creator_cashflow_playbook.md) | Creator |
| [templates/niches/consultant_cashflow_playbook.md](templates/niches/consultant_cashflow_playbook.md) | Consultant |
| [templates/niches/agency_cashflow_playbook.md](templates/niches/agency_cashflow_playbook.md) | Agency |
| [templates/niches/freelancer_cashflow_playbook.md](templates/niches/freelancer_cashflow_playbook.md) | Freelancer / Solo |
| [templates/niches/saas_indie_cashflow_playbook.md](templates/niches/saas_indie_cashflow_playbook.md) | SaaS / Indie Hacker |
| [templates/niches/marketplace_seller_cashflow_playbook.md](templates/niches/marketplace_seller_cashflow_playbook.md) | Marketplace / digital seller |
| [templates/niches/coach_educator_cashflow_playbook.md](templates/niches/coach_educator_cashflow_playbook.md) | Coach / Educator |
| [templates/niches/coach_educator_sample_week.csv](templates/niches/coach_educator_sample_week.csv) | Coach sample week |

```bash
python scripts/pack_client.py   # → dist/zero-cost-client-pack.zip (all niches)
```

Niches: Creator · Consultant · Agency · Freelancer/Solo · SaaS/Indie · Marketplace Seller · Coach/Educator.

## Autonomy model
- **AI / software owns:** issues, niche templates, pack script, fleet workflows.
- **Owner is not required** for day-to-day currency artifacts.

## Status
- All listed niches shipped. Keep everything zero-cost.
