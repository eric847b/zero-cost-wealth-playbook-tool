# Creator Cashflow Pack — Niche Playbook

Zero-cost money system for **creators** (YouTube, TikTok, Twitch, newsletters, digital products).  
Same toolkit as the general pack — categories and weekly experiments tuned for creator income.

Build the base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)

---

## 1. Track (Day 0)

```bash
# Prefer a dedicated ledger for creator work
cp templates/client_ledger_template.csv data/creator_ledger.csv

python tracker.py add 120 income platform "YouTube Partner payout"
python tracker.py add 45 income tips "Super Chat / memberships"
python tracker.py add 29.99 expense gear "USB mic foam + cable"
python tracker.py summary
```

Suggested **categories** (keep short):

| Type | Categories |
|------|------------|
| Income | `platform`, `tips`, `sponsors`, `digital_product`, `affiliate`, `services` |
| Expense | `gear`, `software`, `hosting`, `ads_test`, `education`, `tax_setaside` |

No paid bank aggregators. Export CSV from your bank/platform dashboards and paste rows by hand if needed.

## 2. Free stack (creators)

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + LibreOffice / Google Sheets |
| Reports | `python export.py --client data/creator_ledger.csv` → Print → PDF |
| Video walkthrough | OBS + YouTube unlisted or free Loom |
| Invoicing sponsors | Wave free tier or Markdown → PDF |
| Analytics | Native platform dashboards only (no paid BI) |

## 3. First three monetization moves (creator-shaped)

1. **Sell this niche pack** — ZIP + this playbook + sample week; price above generic pack ($49–99).
2. **Setup session** — 45–60 min: map their platforms → categories, first export PDF.
3. **Monthly review** — they run Sunday summary; you comment on one expense cut + one income experiment.

## 4. Weekly loop (creator owns it)

**Sunday (15–20 min)**
1. `python tracker.py summary` (or open CSV pivot by `category`).
2. `python export.py --client data/creator_ledger.csv` → save PDF.
3. Pick **one** of:
   - Cut or pause one non-producing expense (gear you do not use, software trial).
   - Run one income experiment (new short, affiliate link, digital product listing).
4. Move ~20–30% of platform/tips income to `tax_setaside` category (estimate only; not tax advice).

## 5. Sample experiments (rotate, do not stack ten)

- List one digital product on free Gumroad tier.
- One affiliate link in a pinned comment (disclose).
- One sponsor outreach email (Wave invoice if they say yes).
- Cut one unused SaaS trial before it converts to paid.

## 6. Non-goals

- No paid ad accounts required to start.
- No automated bank sync.
- No guaranteed follower or revenue outcomes.

---

*Same CLI. Same CSV. Higher price for niche language. Keep the stack free.*
