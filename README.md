# Zero-Cost Wealth Playbook Tool

Personal wealth acceleration using **only free tools**. No paid APIs, no subscriptions required.

## Playbook

Read **[PLAYBOOK.md](PLAYBOOK.md)** — track → free stack → first three monetization moves → weekly loop.

## Tracker

Local CSV ledger + CLI — works offline, imports into LibreOffice Calc or Google Sheets.

```bash
# Add income / expense
python tracker.py add 100 income freelance "template sale"
python tracker.py add 12.50 expense software "domain renewal"

# Inspect
python tracker.py list
python tracker.py summary
```

Ledger path: `data/ledger.csv`  
Sample rows: `data/sample_ledger.csv`  
First-week sample: `data/sample_first_week_ledger.csv`  
Columns: `date, type, amount, category, note`

### Free-tool path
1. Run the CLI to log transactions (or copy a sample ledger).
2. Open CSV in **LibreOffice Calc** or **Google Sheets**.
3. Pivot by `category` / `type` for budgets — no paid BI tools.

## Export (print / PDF)

```bash
python export.py --sample   # Markdown report from sample data
python export.py            # from data/ledger.csv
python export.py --client path/to/client_ledger.csv   # ready-to-send client report
```

Writes `export_report.md` (or `client_report.md` with `--client`). Open it and use browser **Print → Save as PDF** (free). Stdlib only.

## Client / Monetization (zero fixed cost)

Reusable pack so you can customize and deliver the free toolkit as a paid service:

| File | Purpose |
|------|---------|
| [templates/client_ledger_template.csv](templates/client_ledger_template.csv) | Clean starter ledger for a new client |
| [templates/client_playbook.md](templates/client_playbook.md) | One-page adaptation guide |
| [templates/client_onboarding_checklist.md](templates/client_onboarding_checklist.md) | Day-0 to Day-7 checklist to hand the client |
| [templates/pricing_notes.md](templates/pricing_notes.md) | Packaging, pricing, delivery (no paid tools) |
| [templates/sales_one_pager.md](templates/sales_one_pager.md) | Paste-ready listing + email copy for the client pack |
| [templates/niches/creator_cashflow_playbook.md](templates/niches/creator_cashflow_playbook.md) | Creator niche weekly loop + categories |
| [templates/niches/creator_sample_week.csv](templates/niches/creator_sample_week.csv) | Creator first-week demo rows |
| [templates/niches/consultant_cashflow_playbook.md](templates/niches/consultant_cashflow_playbook.md) | Consultant niche weekly loop + categories |
| [templates/niches/consultant_sample_week.csv](templates/niches/consultant_sample_week.csv) | Consultant first-week demo rows |
| [templates/niches/agency_cashflow_playbook.md](templates/niches/agency_cashflow_playbook.md) | Agency niche weekly loop + categories |
| [templates/niches/agency_sample_week.csv](templates/niches/agency_sample_week.csv) | Agency first-week demo rows |
| [data/sample_first_week_ledger.csv](data/sample_first_week_ledger.csv) | Realistic first-week rows for demos |

### One-command client pack (zip)

```bash
python scripts/pack_client.py
```

Produces `dist/zero-cost-client-pack.zip` — includes all niches under `templates/niches/`. Stdlib only; no new deps.

### 3-step delivery checklist
1. Run the pack script.
2. Walk the client through the [onboarding checklist](templates/client_onboarding_checklist.md) and `export.py --client`.
3. Hand over the first Markdown/PDF report and the matching niche playbook.

See [pricing notes](templates/pricing_notes.md) and [sales_one_pager.md](templates/sales_one_pager.md). Niches: Creator · Consultant · Agency.

## Quick start
1. Clone this repo.
2. `python tracker.py add 50 income gift`
3. `python tracker.py summary`
4. `python export.py --sample`
5. `python scripts/pack_client.py`

## Monetization (zero fixed cost)
- Generic pack + sales one-pager.
- Niche upsells: Creator Cashflow · Consultant Cashflow · Agency Cashflow.
- Further niches: generate via LLM from existing niche templates (no human coding required).

## Autonomy model
- **AI / software owns:** issue creation, niche templates, pack script, PR merge on currency path, fleet workflows.
- **Owner is not required** for day-to-day currency artifacts.
- Ledger entries remain real-world (only the human who receives money can log truth) — optional and offline.

## Resource balance
- This repo: offline CLI + Markdown.
- LLMs: more niches and listing copy.
- Fleet agent: ROI ranking + draft remediation.
- No paid bank sync / BI.

## Status
- Client pack zip (#11), sales one-pager (#13), Creator niche (#15), Consultant niche (#17), Agency niche (#19) shipped.
- Keep everything zero-cost.
