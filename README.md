# Zero-Cost Wealth Playbook Tool

Personal wealth acceleration using **only free tools**. No paid APIs, no subscriptions required.

## Tracker (shipped)

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
Columns: `date, type, amount, category, note`

### Free-tool path
1. Run the CLI to log transactions.
2. Open `data/ledger.csv` in **LibreOffice Calc** or upload to **Google Sheets**.
3. Pivot by `category` / `type` for budgets — no paid BI tools.

## Quick start
1. Clone this repo.
2. `python tracker.py add 50 income gift`
3. `python tracker.py summary`

## Monetization (zero fixed cost)
- Freelance: customize the playbook/tracker for clients.
- Templates: share or sell consulting around the free toolkit.
- Open-source visibility → inbound opportunities.

## Status
- MVP tracker shipped (issue #4).
- Iterate on playbook content next; keep everything zero-cost.
