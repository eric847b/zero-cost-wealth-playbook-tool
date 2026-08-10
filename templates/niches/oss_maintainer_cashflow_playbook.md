# OSS / Maintainer Cashflow Pack — Niche Playbook

Zero-cost money system for **open-source maintainers, library authors, and sponsored projects**.  
Same toolkit as the general pack — categories tuned for sponsorships, bounties, support retainers, and docs products.

Build base zip: `python scripts/pack_client.py`  
Sales copy: [sales_one_pager.md](../sales_one_pager.md)  
Sibling niches: [saas_indie](saas_indie_cashflow_playbook.md) · [freelancer](freelancer_cashflow_playbook.md) · [consultant](consultant_cashflow_playbook.md) · [coach_educator](coach_educator_cashflow_playbook.md)

---

## 1. Track (Day 0)

```bash
cp templates/client_ledger_template.csv data/oss_ledger.csv

python tracker.py add 200 income sponsorship "GitHub Sponsors monthly"
python tracker.py add 150 income bounty "upstream issue bounty"
python tracker.py add 0 expense tools "all free tier"
python tracker.py summary
```

Suggested **categories**:

| Type | Categories |
|------|------------|
| Income | `sponsorship`, `bounty`, `support_retainer`, `docs_product`, `affiliate` |
| Expense | `tools`, `infra`, `tax_setaside`, `platform_fees`, `education` |

## 2. Free stack

| Need | Free option |
|------|-------------|
| Ledger | `tracker.py` + LibreOffice / Google Sheets |
| Reports | `python export.py --client data/oss_ledger.csv` → Print → PDF |
| Sponsors | GitHub Sponsors / Open Collective free tier |
| Docs product | Markdown + PDF via export; free Gumroad listing |
| Support | Public issues + office-hours calendar (free)

## 3. First three monetization moves

1. **Sell this niche pack** — ZIP + playbook for maintainers; $29–79.
2. **Sponsor teardown** — map one sponsor tier’s value vs hours; export PDF.
3. **Productize docs** — turn a repeated FAQ into a fixed `docs_product` download.

## 4. Weekly loop

1. Log every sponsor payout and bounty the same day.
2. Sunday: `summary` + export PDF; one line on unpaid support hours.
3. One action only: raise a sponsor tier, close a low-value support channel, or ship a docs product.
4. Set aside ~25–30% of gross into `tax_setaside` (estimate; not tax advice).

## 5. Experiments (one at a time)

- Offer a paid support retainer for one enterprise user (`support_retainer`).
- Add an affiliate link in the README for a related free tool; log as `affiliate`.
- Cap unpaid support hours one week; measure sponsor conversion.

## 6. Non-goals

- No paid CI beyond free tiers required.
- No guaranteed sponsorship volume.
- No automated payout sync.

---

*Same CLI. Same CSV. Niche language for OSS maintainers. Stack stays free.*

_Cross-repo improvement from singularity-operator GitHubSeamless (issue #9)._
