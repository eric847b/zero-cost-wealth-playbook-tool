# Setup Session — Statement of Work (45–60 min)

**Offer:** Cashflow system setup for one freelancer / solopreneur  
**Price anchor:** $99–199 (see `pricing_notes.md`; default quote $149)  
**Fixed cost to deliver:** $0 (Python + CSV + Markdown only)

Generate a quote:
```bash
python scripts/quote.py --client "CLIENT_NAME" --item "Cashflow setup session (45–60 min)" --amount 149 --type quote
```

---

## Scope (included)

1. Confirm Python 3 and a working copy of this toolkit (or the client pack zip).
2. Create the client’s `data/ledger.csv` from the template.
3. Log 2–3 real sample rows (or import from a bank CSV the client provides manually).
4. Run `tracker.py summary`, `runway.py`, and `export.py --client` once with the client watching.
5. Walk the Day-0 → Day-7 checklist (`client_onboarding_checklist.md`).
6. Rank one income experiment with `scripts/income_experiment.py` and write the top action into the client’s notes.
7. Deliver: `client_report.md` (or PDF via browser print) + filled checklist + quote/invoice Markdown.

## Out of scope

- Automated bank sync or paid aggregator APIs
- Ongoing bookkeeping or tax advice
- Custom SaaS, hosted dashboards, or paid email sequences
- Guaranteed income outcomes

## Client provides

- 45–60 minutes on a call or screen-share
- Optional: last 7–14 days of transactions as CSV or list
- Preferred categories (or accept defaults: freelance, consulting, software, tools, hosting)

## You deliver (same day)

| Artifact | How |
|----------|-----|
| Quote / invoice | `scripts/quote.py` |
| Ledger started | `data/ledger.csv` or client copy |
| First report | `export.py --client` → Print → PDF |
| Runway snapshot | `python runway.py` |
| Onboarding checklist | checked Day-0 items |
| One ranked experiment | `income_experiment.py rank` |

## Success criteria

- Client can run `tracker.py add`, `summary`, and `export.py` without help
- At least one real income and one real expense row exist
- One printable report and one next-week experiment are written down

## Follow-on (optional upsell)

- Monthly review: $49–99 — client sends `export_report.md` / `runway_report.md`; you comment once
- Niche pack: Creator / Consultant / Agency templates from `templates/niches/`

---
*Zero fixed cost. Charge for time and clarity — not software lock-in.*
