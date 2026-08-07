# Client Onboarding Checklist — Day 0 to Day 7

Hand this one-pager to a new client with the toolkit. Everything stays free / offline.

## Day 0 — Install (5–10 min)

- [ ] Clone or copy the pack: `tracker.py`, `export.py`, `templates/`, `data/`
- [ ] Confirm Python 3 is available (`python --version`)
- [ ] Copy `templates/client_ledger_template.csv` → `data/ledger.csv` (or keep a separate client file)
- [ ] Optional: open `data/sample_first_week_ledger.csv` to see a filled week

## Day 0 — First three commands

```bash
python tracker.py add 100 income freelance "first client payment"
python tracker.py add 12.50 expense software "domain"
python tracker.py summary
```

- [ ] First income row logged
- [ ] First expense row logged
- [ ] `summary` prints without error

## Day 0 — First report

```bash
python export.py --client data/ledger.csv
```

- [ ] `client_report.md` (or equivalent) appears
- [ ] Open in browser → Print → Save as PDF (free)

## Days 1–7 — Daily habit

- [ ] Log every inflow/outflow the same day (or end of day)
- [ ] Use real categories only (no fictional balances)
- [ ] Keep notes short and specific

## Day 7 — Weekly loop (client owns it)

```bash
python tracker.py summary
python export.py --client data/ledger.csv
```

- [ ] Review the Markdown/PDF once
- [ ] Cut or reduce **one** expense category that is not producing revenue or learning
- [ ] Note **one** income experiment for next week

## Success after 7 days

- Ledger has real rows (not the starter placeholder)
- Client can run `summary` and export without help
- One printable report exists to share or archive
- Weekly loop is on the calendar (Sunday is fine)

## References

- Full adaptation guide: [client_playbook.md](client_playbook.md)
- Pricing / packaging: [pricing_notes.md](pricing_notes.md)
- Sample first week: `../data/sample_first_week_ledger.csv`

Everything remains zero fixed cost. No paid APIs or subscriptions required.
