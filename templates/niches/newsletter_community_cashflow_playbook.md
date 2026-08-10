# Newsletter / Community Cashflow Pack — Niche Playbook

Zero-cost money system for **newsletter operators, Substack/Ghost-style writers, and community leads** (Discord, Circle-free, forum, cohort list).  
Same toolkit as the general pack — categories tuned for sponsorships, paid tiers, affiliates, and list products.

Build base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)  
Sibling niches: [creator](creator_cashflow_playbook.md) · [coach_educator](coach_educator_cashflow_playbook.md) · [marketplace_seller](marketplace_seller_cashflow_playbook.md) · [oss_maintainer](oss_maintainer_cashflow_playbook.md)

---

## 1. Track (Day 0)

```bash
cp templates/client_ledger_template.csv data/newsletter_ledger.csv

python tracker.py add 400 income sponsorship "issue sponsor slot"
python tracker.py add 9 income paid_tier "monthly paid subscriber"
python tracker.py add 12 expense tools "email + form free tier overage"
python tracker.py summary
```

Suggested **categories**:

| Type | Categories |
|------|------------|
| Income | `sponsorship`, `paid_tier`, `affiliate`, `digital_product`, `consulting` |
| Expense | `tools`, `ads`, `tax_setaside`, `platform_fees`, `education` |

## 2. Free stack

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + LibreOffice / Google Sheets |
| Reports | `python export.py --client data/newsletter_ledger.csv` → Print → PDF |
| List | Free Substack / Buttondown / Ghost trial / plain Markdown archive |
| Community | Free Discord / Telegram / GitHub Discussions |
| Products | Free Gumroad / PDF via export |

## 3. First three monetization moves

1. **Sell this niche pack** — ZIP + playbook for newsletter/community operators; $39–89.
2. **Sponsor rate card** — one-page PDF of available slots + past open rates (honest, no hype).
3. **Productize one repeat** — turn a frequent reader question into a fixed `digital_product`.

## 4. Weekly loop

1. Log every sponsor payment and paid-tier renewal the same day.
2. Sunday: `summary` + export PDF; one line on net new free vs paid subs.
3. One action only: raise a sponsor rate, open a paid tier, or cut a low-margin channel.
4. Set aside ~25–30% of gross into `tax_setaside` (estimate; not tax advice).

## 5. Experiments (one at a time)

- Offer one consulting office-hour block for power readers (`consulting`).
- Add a single affiliate recommendation with disclosure; log as `affiliate`.
- Pause growth hacks one week; measure organic-only conversion to paid.

## 6. Non-goals

- No paid ESP required beyond free tiers.
- No guaranteed open rates or sponsor volume.
- No automated payment sync.

---

*Same CLI. Same CSV. Niche language for newsletters and communities. Stack stays free.*
