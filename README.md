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
Columns: `date, type, amount, category, note`

### Free-tool path
1. Run the CLI to log transactions (or copy sample ledger).
2. Open CSV in **LibreOffice Calc** or **Google Sheets**.
3. Pivot by `category` / `type` for budgets — no paid BI tools.

## Export (print / PDF)

```bash
python export.py --sample   # Markdown report from sample data
python export.py            # from data/ledger.csv
```

Writes `export_report.md`. Open it and use browser **Print → Save as PDF** (free). Stdlib only.

## Quick start
1. Clone this repo.
2. `python tracker.py add 50 income gift`
3. `python tracker.py summary`
4. `python export.py --sample`

## Monetization (zero fixed cost)
- Freelance: customize the playbook/tracker for clients.
- Templates: share or sell consulting around the free toolkit.
- Open-source visibility → inbound opportunities.

## Status
- MVP tracker shipped (issue #4).
- Playbook + sample ledger + export shipped (issue #5).
- Keep everything zero-cost.
