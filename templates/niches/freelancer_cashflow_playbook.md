# Freelancer / Solo Operator Cashflow Pack — Niche Playbook

Zero-cost money system for **freelancers and solo operators** (hourly, project, productized, retainer, referral).  
Same toolkit as the general pack — categories and weekly loop tuned for one-person service businesses.

Build base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)  
Sibling niches: [creator_cashflow_playbook.md](creator_cashflow_playbook.md) · [consultant_cashflow_playbook.md](consultant_cashflow_playbook.md) · [agency_cashflow_playbook.md](agency_cashflow_playbook.md)

---

## 1. Track (Day 0)

```bash
cp templates/client_ledger_template.csv data/freelancer_ledger.csv

python tracker.py add 750 income project "landing page milestone 1"
python tracker.py add 120 income hourly "2h support call"
python tracker.py add 25 expense tools "domain renewal"
python tracker.py summary
```

Suggested **categories**:

| Type | Categories |
|------|------------|
| Income | `hourly`, `project`, `productized`, `retainer`, `referral` |
| Expense | `tools`, `software`, `education`, `tax_setaside`, `overhead` |

## 2. Free stack

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + LibreOffice Calc / Google Sheets |
| Reports | `python export.py --client data/freelancer_ledger.csv` → browser Print → PDF |
| Invoices | Wave free tier or Markdown → PDF |
| Pipeline | Simple Markdown list or free Trello |
| Time log | Spreadsheet column or note field on each income row |

## 3. First three monetization moves

1. **Sell this niche pack** — ZIP + this playbook; price in the $49–99 band (solo-friendly).
2. **Solo setup session** — map one client’s work types → categories; produce first export PDF.
3. **Weekly capacity check** — flag one under-priced project or one task that should become a productized offer.

## 4. Weekly loop

1. Log every payment and billable hour the same day (or same evening).
2. Sunday: `summary` + export PDF; note utilization in one line.
3. One action only: raise a rate, drop a low-margin task, or productize one repeat deliverable.
4. Set aside ~25–30% of gross into `tax_setaside` (estimate; not tax advice).

## 5. Experiments (one at a time)

- Convert one recurring request into a fixed-scope productized offer (`productized`).
- Ask one happy client for a referral (log as `referral` when paid).
- Cut or renegotiate one tool that is not earning its keep.

## 6. Non-goals

- No paid time-tracking or invoicing SaaS required.
- No automated bank sync.
- No guaranteed utilization or billable-hour targets.

---

*Same CLI. Same CSV. Niche language for freelancers and solo operators. Stack stays free.*
