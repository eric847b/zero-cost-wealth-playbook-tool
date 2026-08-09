# Agency Cashflow Pack — Niche Playbook

Zero-cost money system for **agencies** (retainer clients, project pipelines, subcontractors).  
Same toolkit as the general pack — categories and weekly loop tuned for multi-client service businesses.

Build base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)  
Sibling niches: [creator_cashflow_playbook.md](creator_cashflow_playbook.md) · [consultant_cashflow_playbook.md](consultant_cashflow_playbook.md)

---

## 1. Track (Day 0)

```bash
cp templates/client_ledger_template.csv data/agency_ledger.csv

python tracker.py add 2500 income retainer "client A monthly"
python tracker.py add 1200 income project "landing page deposit"
python tracker.py add 400 expense subcontract "freelance designer week"
python tracker.py summary
```

Suggested **categories**:

| Type | Categories |
|------|------------|
| Income | `retainer`, `project`, `upsell`, `referral`, `productized`, `pass_through` |
| Expense | `subcontract`, `tools`, `software`, `ads`, `education`, `tax_setaside`, `overhead` |

## 2. Free stack

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + Calc / Sheets (one sheet per client or single with tags in note) |
| Reports | `python export.py --client data/agency_ledger.csv` → PDF |
| Invoices | Wave free tier or Markdown → PDF |
| Pipeline | Simple Markdown kanban or free Trello |
| Contracts | Plain Markdown + e-sign free tier only when needed |

## 3. First three monetization moves

1. **Sell this niche pack** — ZIP + this playbook; price above consultant ($79–149).
2. **Agency setup session** — map retainers + project stages → categories; first multi-client export.
3. **Monthly capacity review** — flag one under-priced retainer or one subcontract that should become productized.

## 4. Weekly loop

1. Log every retainer payment and project milestone the same day.
2. Sunday: `summary` + export PDF; split by client in notes if useful.
3. One action only: raise a retainer, cut a tool, or productize one repeat deliverable.
4. Set aside ~25–30% of net (after subcontract) into `tax_setaside` (estimate; not tax advice).

## 5. Experiments (one at a time)

- Convert one recurring project into a fixed-scope productized offer.
- Ask one retainer client for a referral (log as `referral` when paid).
- Drop or renegotiate one subcontract that erodes margin.

## 6. Non-goals

- No agency CRM SaaS required.
- No automated time-tracking or billing APIs.
- No guaranteed utilization or headcount math.

---

*Same CLI. Same CSV. Niche language for agencies. Stack stays free.*
