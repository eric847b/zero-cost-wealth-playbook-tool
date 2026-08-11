# Public Listing — Zero-Cost Client Cashflow Pack

**Status:** Public on GitHub (`eric847b/zero-cost-wealth-playbook-tool`). Ready to copy into Gumroad / Lemon Squeezy free tier / email.

## Product name
**Zero-Cost Client Cashflow Pack**

## One-liner
Offline wealth tracker + playbook + setup-session SOW — unzip, run Python, no subscriptions.

## Price anchors (first sales, zero fixed cost)
| Offer | Price | How to deliver |
|-------|-------|----------------|
| Pack only (ZIP) | $29–79 | `python scripts/pack_client.py` → send zip |
| Setup session | $99–199 | [templates/setup_session_sow.md](templates/setup_session_sow.md) + live call |
| Monthly review | $49–99/mo | Client sends `runway_report.md` / export; you comment |

Quote without paid SaaS:
```bash
python scripts/quote.py --client "Name" --item "Cashflow setup session (45–60 min)" --amount 149 --type quote
```

## What’s in the pack
- `tracker.py` — CSV ledger CLI
- `runway.py` — weekly velocity + runway
- `export.py` — Markdown → Print → PDF
- `scripts/quote.py` — free quotes/invoices
- `scripts/income_experiment.py` — rank monetization experiments
- `PLAYBOOK.md` + niche templates
- Setup session SOW + delivery checklist
- Sample ledgers

Build:
```bash
python scripts/pack_client.py
# → dist/zero-cost-client-pack.zip
```

## Short listing blurb (≤500 chars)
```
Zero-Cost Client Cashflow Pack — offline tracker, runway report, free quotes, setup-session SOW.
Python + CSV only. No bank APIs, no SaaS lock-in. Build: python scripts/pack_client.py
Repo: https://github.com/eric847b/zero-cost-wealth-playbook-tool
```

## Email CTA
Subject: Your offline cashflow pack

> Attached: zero-cost-client-pack.zip  
> 1) Unzip  2) Follow README_CLIENT.md  3) Optional: book a 45-min setup session ($149) using the SOW in templates/  
> Reply with your first `runway_report.md` if you want a free 10-min pointer.

## What not to promise
- Automated bank sync
- Guaranteed income
- Paid analytics or ads as a requirement

## Listing checklist (operator)
- [x] Repo public
- [x] PUBLIC_LISTING.md on main
- [x] Pack script includes currency tools + setup session templates
- [ ] Optional: paste blurb to Gumroad/Lemon free tier
- [ ] Optional: pin this file or README section on repo

---
*List the pack. Charge for setup and review — not for software lock-in.*
