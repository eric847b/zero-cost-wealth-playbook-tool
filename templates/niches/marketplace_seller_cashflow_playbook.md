# Marketplace / Digital Seller Cashflow Pack — Niche Playbook

Zero-cost money system for **marketplace and digital sellers** (Etsy, Gumroad, itch.io, Payhip, own store, print-on-demand).  
Same toolkit as the general pack — categories and weekly loop tuned for product + listing economics.

Build base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)  
Sibling niches: [creator_cashflow_playbook.md](creator_cashflow_playbook.md) · [freelancer_cashflow_playbook.md](freelancer_cashflow_playbook.md) · [saas_indie_cashflow_playbook.md](saas_indie_cashflow_playbook.md)

---

## 1. Track (Day 0)

```bash
cp templates/client_ledger_template.csv data/marketplace_ledger.csv

python tracker.py add 48 income sales "Gumroad template pack"
python tracker.py add 12 income sales "Etsy print listing"
python tracker.py add 3.20 expense fees "platform fee 6.5%"
python tracker.py add 9 expense ads "boosted listing"
python tracker.py summary
```

Suggested **categories**:

| Type | Categories |
|------|------------|
| Income | `sales`, `upsell`, `bundle`, `affiliate`, `refund_reversal` |
| Expense | `fees`, `ads`, `tools`, `materials`, `tax_setaside`, `shipping` |

## 2. Free stack

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + LibreOffice Calc / Google Sheets |
| Reports | `python export.py --client data/marketplace_ledger.csv` → Print → PDF |
| Listings | Platform free tier; Markdown drafts offline |
| Photos | Phone + free Canva / GIMP |
| Refunds | Log as expense `fees` or negative income note |

## 3. First three monetization moves

1. **Sell this niche pack** — ZIP + this playbook; $39–79 for digital-seller audience.
2. **One-listing teardown** — map one product’s gross → fees → net; export PDF.
3. **Kill or fix** — drop the lowest-margin listing or raise price on the top seller by 10%.

## 4. Weekly loop

1. Log every payout and fee the day it posts (or same evening).
2. Sunday: `summary` + export PDF; one line on conversion or refund rate.
3. One action only: new listing, price test, or cut ad spend on a loser.
4. Set aside ~20–30% of net into `tax_setaside` (estimate; not tax advice).

## 5. Experiments (one at a time)

- Bundle two low sellers into one `bundle` SKU.
- Pause paid ads for one week; measure organic-only net.
- Add an upsell link on the thank-you page; log as `upsell`.

## 6. Non-goals

- No paid analytics or inventory SaaS required.
- No automated marketplace API sync.
- No guaranteed ranking or ad ROAS.

---

*Same CLI. Same CSV. Niche language for marketplace and digital sellers. Stack stays free.*
