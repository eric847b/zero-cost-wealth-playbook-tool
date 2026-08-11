# Local Services / Trades Cashflow Pack — Niche Playbook

Zero-cost money system for **local service operators and trades** (cleaning, handyman, landscaping, mobile detailing, tutoring in-person, pet care).  
Same toolkit — categories tuned for jobs, materials, travel, and deposits.

Build base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)

---

## 1. Track (Day 0)

```bash
cp templates/client_ledger_template.csv data/local_services_ledger.csv

python tracker.py add 180 income job "2hr cleaning"
python tracker.py add 25 expense materials "supplies"
python tracker.py summary
```

| Type | Categories |
|------|------------|
| Income | `job`, `deposit`, `recurring`, `tip`, `referral` |
| Expense | `materials`, `travel`, `tools`, `tax_setaside`, `ads` |

## 2. Free stack

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + Sheets / LibreOffice |
| Reports | `python export.py --client data/local_services_ledger.csv` |
| Booking | Free calendar + text/email |
| Marketing | Nextdoor / Facebook groups / flyers PDF |

## 3. First three monetization moves

1. **Sell this niche pack** — $29–69 to local operators.
2. **Job margin teardown** — one job gross → hours → effective hourly; export PDF.
3. **Recurring route** — convert one one-off into a weekly/biweekly `recurring` slot.

## 4. Weekly loop

1. Log every job and material purchase same day.
2. Sunday: `summary` + PDF; one line on utilization.
3. One action: raise a rate, drop a low-margin job, or fill an empty slot.
4. Set aside ~25–30% into `tax_setaside` (estimate; not tax advice).

## 5. Non-goals

- No paid booking SaaS required.
- No guaranteed lead volume.

---

*Same CLI. Same CSV. Local services language. Stack stays free.*
