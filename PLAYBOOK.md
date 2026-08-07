# Zero-Cost Wealth Playbook

Personal wealth acceleration using **only free tools**. No paid APIs. No subscriptions.

## 1. Track everything

Use the local ledger:

```bash
python tracker.py add 100 income freelance "template sale"
python tracker.py add 12.50 expense software "domain renewal"
python tracker.py summary
```

- Ledger: `data/ledger.csv` (or start from `data/sample_ledger.csv`)
- Import into **LibreOffice Calc** or **Google Sheets** for pivots
- Columns: `date, type, amount, category, note`

## 2. Free-tool stack only

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + CSV |
| Spreadsheet | LibreOffice Calc / Google Sheets |
| Print / PDF | Browser print → Save as PDF, or `python export.py` then print Markdown |
| Bank data | Manual CSV export from your bank (no aggregator APIs) |

## 3. First three monetization moves (zero fixed cost)

1. **Templates** — Package the tracker + this playbook as a consulting deliverable for freelancers who want a simple system.
2. **Customization** — Offer a one-time setup (categories, sample goals) billed hourly; still zero product cost.
3. **Open-source inbound** — Keep the repo public; answer issues; convert attention into paid help or referrals.

## 4. Weekly loop

1. Log every inflow/outflow the same day.
2. Run `python tracker.py summary` once a week.
3. Run `python export.py` for a printable snapshot.
4. Adjust one category or one income experiment — not ten.

## 5. Non-goals

- No paid analytics, no paid email sequences, no paid ads required to start.
- No simulated balances — only real rows you enter.

---

*Iterate the playbook; keep the stack free.*
