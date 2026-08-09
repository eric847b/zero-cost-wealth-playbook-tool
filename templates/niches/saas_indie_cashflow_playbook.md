# SaaS / Indie Hacker Cashflow Pack — Niche Playbook

Zero-cost money system for **SaaS founders and indie hackers** (MRR, one-time sales, trials, churn, infra).  
Same toolkit as the general pack — categories and weekly loop tuned for product-led solo/small-team builders.

Build base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)  
Sibling niches: [creator_cashflow_playbook.md](creator_cashflow_playbook.md) · [consultant_cashflow_playbook.md](consultant_cashflow_playbook.md) · [agency_cashflow_playbook.md](agency_cashflow_playbook.md) · [freelancer_cashflow_playbook.md](freelancer_cashflow_playbook.md)

---

## 1. Track (Day 0)

```bash
cp templates/client_ledger_template.csv data/saas_indie_ledger.csv

python tracker.py add 49 income mrr "plan pro monthly"
python tracker.py add 199 income onetime "lifetime deal"
python tracker.py add 12 expense infra "vercel + domain"
python tracker.py summary
```

Suggested **categories**:

| Type | Categories |
|------|------------|
| Income | `mrr`, `onetime`, `trial_convert`, `affiliate`, `upsell` |
| Expense | `infra`, `tools`, `ads`, `tax_setaside`, `support` |

## 2. Free stack

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + LibreOffice Calc / Google Sheets |
| Reports | `python export.py --client data/saas_indie_ledger.csv` → browser Print → PDF |
| MRR view | Pivot `mrr` rows by week/month in Sheets |
| Churn signal | Note cancelled customers in expense/support or a Markdown log |
| Stripe/Paddle | Export CSV manually into ledger (no paid BI) |

## 3. First three monetization moves

1. **Sell this niche pack** — ZIP + this playbook; price in the $49–149 band (builder-friendly).
2. **MRR clarity session** — map one product’s revenue streams → categories; produce first export PDF.
3. **Weekly unit-economics check** — flag one under-priced plan or one cost that is not earning its keep.

## 4. Weekly loop

1. Log every subscription charge, one-time sale, and infra bill the same day.
2. Sunday: `summary` + export PDF; note net new MRR vs churn in one line.
3. One action only: raise a plan price, cut a dead channel, or ship one retention tweak.
4. Set aside ~25–30% of gross into `tax_setaside` (estimate; not tax advice).

## 5. Experiments (one at a time)

- Convert one high-support customer segment into a higher-priced plan (`upsell`).
- Run one free-channel experiment (content, community) and log any affiliate or trial conversions.
- Cut or renegotiate one infra/tool cost that does not move retention or acquisition.

## 6. Non-goals

- No paid analytics or cohort SaaS required.
- No automated payment processor sync.
- No guaranteed MRR or churn targets.

---

*Same CLI. Same CSV. Niche language for SaaS / indie hackers. Stack stays free.*
