# Consultant Cashflow Pack — Niche Playbook

Zero-cost money system for **consultants** (hourly, project, retainers).  
Same toolkit as the general pack — categories and weekly loop tuned for services income.

Build base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)  
Sibling niche: [creator_cashflow_playbook.md](creator_cashflow_playbook.md)

---

## 1. Track (Day 0)

```bash
cp templates/client_ledger_template.csv data/consultant_ledger.csv

python tracker.py add 500 income project "discovery workshop deposit"
python tracker.py add 150 income hourly "2h strategy call"
python tracker.py add 0 expense software "LibreOffice — free"
python tracker.py summary
```

Suggested **categories**:

| Type | Categories |
|------|------------|
| Income | `hourly`, `project`, `retainer`, `productized`, `referral` |
| Expense | `tools`, `software`, `travel`, `education`, `subcontract`, `tax_setaside` |

## 2. Free stack

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + Calc / Sheets |
| Reports | `python export.py --client data/consultant_ledger.csv` → PDF |
| Invoices | Wave free tier or Markdown → PDF |
| Scheduling | Calendly free / Google Calendar |
| Contracts | Plain Markdown template (no paid e-sign required to start) |

## 3. First three monetization moves

1. **Sell this niche pack** — ZIP + this playbook; price above generic ($49–99).
2. **Setup session** — map service lines → categories; first client export.
3. **Monthly review** — client runs Sunday summary; you flag one rate increase or one non-billable cut.

## 4. Weekly loop

1. Log every hour/project payment the same day.
2. Sunday: `summary` + export PDF.
3. One action only: raise a rate, cut a tool, or productize one repeat deliverable.
4. Set aside ~25–30% of income into `tax_setaside` (estimate; not tax advice).

## 5. Experiments (one at a time)

- Productize a fixed-scope offer (e.g. “Cashflow setup — $199”).
- Ask one past client for a referral (log as `referral` when paid).
- Drop one unused paid tool trial before renewal.

## 6. Non-goals

- No CRM SaaS required.
- No automated time tracking APIs.
- No guaranteed billable utilization.

---

*Same CLI. Same CSV. Niche language for consultants. Stack stays free.*
