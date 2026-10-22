# Public Listing — Zero-Cost Client Cashflow Pack

**Status:** Public on GitHub (`eric847b/zero-cost-wealth-playbook-tool`). Ready to copy into Gumroad / Lemon Squeezy free tier / email.

## Product name
**Zero-Cost Client Cashflow Pack**

## One-liner
Offline wealth tracker + playbook + setup-session SOW — unzip, run Python, no subscriptions.

## Primary paid CTA
**Cashflow Setup Session — $149 (45–60 min)**  
Client-facing page: **[templates/setup_session_offer.md](templates/setup_session_offer.md)**

## Price anchors (first sales, zero fixed cost)
| Offer | Price | How to deliver |
|-------|-------|----------------|
| Pack only (ZIP) | $29–79 | `python scripts/pack_client.py` → send zip |
| Setup session | $99–199 (default **$149**) | [templates/setup_session_offer.md](templates/setup_session_offer.md) + live call |
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
- Setup session **offer**, SOW + delivery checklist
- Sample ledgers

Build:
```bash
python scripts/pack_client.py
# → dist/zero-cost-client-pack.zip
```

## Short listing blurb (≤500 chars)
```
Zero-Cost Client Cashflow Pack — offline tracker, runway report, free quotes, $149 setup session.
Python + CSV only. No bank APIs, no SaaS lock-in. Offer: templates/setup_session_offer.md
Repo: https://github.com/eric847b/zero-cost-wealth-playbook-tool
```

## Email CTA
Subject: Your offline cashflow pack

> Attached: zero-cost-client-pack.zip  
> 1) Unzip  2) Follow README_CLIENT.md  3) Optional: book a 45-min setup session ($149) — see templates/setup_session_offer.md  
> Reply with your first `runway_report.md` if you want a free 10-min pointer.

## What not to promise
- Automated bank sync
- Guaranteed income
- Paid analytics or ads as a requirement

## Listing checklist (operator)
- [x] Repo public
- [x] PUBLIC_LISTING.md on main
- [x] Pack script includes currency tools + setup session templates
- [x] Client-facing offer page: `templates/setup_session_offer.md`
- [ ] Optional: paste blurb to Gumroad/Lemon free tier
- [ ] Optional: pin offer link on repo / social

---
*List the pack. Charge for setup and review — not for software lock-in.*
