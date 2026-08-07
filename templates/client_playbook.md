# Client Playbook — Zero-Cost Wealth Starter

One-page adaptation of the free toolkit for freelancers / solopreneurs.

## 1. Track (Day 0)
- Copy `client_ledger_template.csv` → `data/ledger.csv` (or keep separate).
- Log every inflow and outflow the same day:
  ```bash
  python tracker.py add 250 income client "invoice #12"
  python tracker.py add 9.99 expense tools "domain"
  ```

## 2. Free stack (no subscriptions)
| Need | Free tool |
|------|-----------|
| Ledger | this repo + LibreOffice Calc / Google Sheets |
| Reports | `python export.py` → Markdown → browser Print → PDF |
| Invoicing | Wave (free tier) or plain PDF from Markdown |
| Banking view | CSV export from your bank → same ledger |

## 3. First three monetization moves
1. **Template delivery** — send this pack + a filled sample report.
2. **Custom ledger setup** — 30–60 min call, hand over a working CSV + export command.
3. **Weekly review loop** — client runs `summary` + export every Sunday; you review the Markdown once a month.

## 4. Weekly loop (client owns it)
- Sunday: `python tracker.py summary` + `python export.py`
- Keep net positive; cut any category that is not producing revenue or learning.
- Re-invest surplus into more client work or free-tool upgrades only.

Everything stays zero fixed cost. No paid APIs required.
