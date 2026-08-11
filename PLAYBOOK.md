# Zero-Cost Wealth Playbook

Personal wealth acceleration using **only free tools**. No paid APIs. No subscriptions.

## 1. Track everything

Use the local ledger:

```bash
python tracker.py add 100 income freelance "template sale"
python tracker.py add 12.50 expense software "domain renewal"
python tracker.py summary
```

- Ledger: `data/ledger.csv` (or start from `data/sample_ledger.csv` / `data/sample_first_week_ledger.csv`)
- Import into **LibreOffice Calc** or **Google Sheets** for pivots
- Columns: `date, type, amount, category, note`

## 2. Free-tool stack only

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + CSV |
| Velocity / runway | `python runway.py` |
| Experiment ranking | `python scripts/income_experiment.py rank` |
| Quote / invoice | `python scripts/quote.py` → Markdown / Print PDF |
| Spreadsheet | LibreOffice Calc / Google Sheets |
| Print / PDF | Browser print → Save as PDF, or `python export.py` then print Markdown |
| Bank data | Manual CSV export from your bank (no aggregator APIs) |

## 3. First three monetization moves (zero fixed cost)

1. **Templates** — Package the tracker + this playbook as a consulting deliverable for freelancers who want a simple system.
2. **Customization** — Offer a one-time setup (categories, sample goals) billed hourly; still zero product cost. Generate the quote with `scripts/quote.py`.
3. **Open-source inbound** — Keep the repo public; answer issues; convert attention into paid help or referrals. Track those as experiments.

For client delivery, use the [onboarding checklist](templates/client_onboarding_checklist.md) and the first-week sample ledger so the client sees a full week on day 0.

## 4. Weekly loop

1. Log every inflow/outflow the same day (`tracker.py add`).
2. Run `python tracker.py summary` and `python runway.py` once a week.
3. Run `python scripts/income_experiment.py rank` and execute the top open experiment.
4. Run `python export.py` for a printable snapshot; issue quotes with `scripts/quote.py`.
5. Adjust one category or one income experiment — not ten.

## 5. Non-goals

- No paid analytics, no paid email sequences, no paid ads required to start.
- No simulated balances — only real rows you enter.
- No paid invoicing SaaS required for first sales.

---

*Iterate the playbook; keep the stack free.*
