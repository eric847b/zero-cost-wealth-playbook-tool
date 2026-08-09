# Coach / Educator Cashflow Pack — Niche Playbook

Zero-cost money system for **coaches, course creators, and educators** (1:1, group, cohort, digital course, membership).  
Same toolkit as the general pack — categories and weekly loop tuned for session + content economics.

Build base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)  
Sibling niches: [creator](creator_cashflow_playbook.md) · [consultant](consultant_cashflow_playbook.md) · [freelancer](freelancer_cashflow_playbook.md) · [saas_indie](saas_indie_cashflow_playbook.md) · [marketplace_seller](marketplace_seller_cashflow_playbook.md)

---

## 1. Track (Day 0)

```bash
cp templates/client_ledger_template.csv data/coach_ledger.csv

python tracker.py add 250 income session "1:1 strategy call"
python tracker.py add 97 income course "self-paced module sale"
python tracker.py add 15 expense tools "Zoom + calendar share"
python tracker.py summary
```

Suggested **categories**:

| Type | Categories |
|------|------------|
| Income | `session`, `group`, `course`, `membership`, `affiliate` |
| Expense | `tools`, `ads`, `education`, `tax_setaside`, `platform_fees` |

## 2. Free stack

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + LibreOffice Calc / Google Sheets |
| Reports | `python export.py --client data/coach_ledger.csv` → Print → PDF |
| Sessions | Free Zoom/Meet tier; Markdown notes |
| Courses | Free Gumroad / own Markdown + PDF |
| Waitlist | Simple form (Google Forms) or plain list |

## 3. First three monetization moves

1. **Sell this niche pack** — ZIP + playbook; $49–99 for coaches/educators.
2. **Session teardown** — map one offer’s gross → time → effective hourly; export PDF.
3. **Productize one repeat** — turn a common 1:1 outcome into a fixed-scope `course` or group offer.

## 4. Weekly loop

1. Log every session payment and course sale the same day.
2. Sunday: `summary` + export PDF; one line on utilization or completion rate.
3. One action only: raise a rate, open a cohort, or cut a low-margin offer.
4. Set aside ~25–30% of gross into `tax_setaside` (estimate; not tax advice).

## 5. Experiments (one at a time)

- Convert one recurring request into a group program (`group`).
- Add an affiliate link on the thank-you page; log as `affiliate`.
- Pause paid ads one week; measure organic-only enrollments.

## 6. Non-goals

- No paid LMS or CRM required.
- No automated payment sync.
- No guaranteed enrollment or completion rates.

---

*Same CLI. Same CSV. Niche language for coaches and educators. Stack stays free.*
