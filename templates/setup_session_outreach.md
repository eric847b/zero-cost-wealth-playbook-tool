# Setup Session — Outreach (paste-ready)

Use with [setup_session_offer.md](setup_session_offer.md). Replace bracketed fields.

---

## Short DM / email (cold or warm)

Subject: Cashflow setup in one hour ($149)

Hi [Name] —

I run a one-time **45–60 min cashflow setup** for freelancers/solopreneurs who want a simple money system they control (Python + CSV + Markdown — no SaaS).

**$149 fixed.** Same day you leave with:
- Ledger started with real rows
- Runway / velocity snapshot
- One ranked next money move
- Quote + offline pack you keep

No bank sync, no subscriptions, no locked dashboard.

If useful: reply with **your name**, a **time window** (timezone), and optional last 7–14 days of transactions (CSV or list). I’ll send a short Markdown quote and a slot.

Offer detail: https://github.com/eric847b/zero-cost-wealth-playbook-tool/blob/main/templates/setup_session_offer.md

— [Your name]

---

## Follow-up (no reply in 3–5 days)

Hi [Name] — quick bump on the $149 cashflow setup session. Happy to hold a slot this week if you still want the offline ledger + runway walkthrough. No pressure either way.

---

## Reply when they say yes

Great — locking you in.

1. Quote attached / generated for **Cashflow setup session (45–60 min) — $149**
2. Proposed time: **[day/time + timezone]** (or send 2–3 options)
3. Optional: drop a CSV or list of last 7–14 days of income/expense so we use real rows on the call

Payment: bank transfer / Zelle / Wave (or agreed method) before or right after the session. I’ll only log the fee after paid delivery.

See you then.

---

## Generate quote (operator)

```bash
python scripts/quote.py --client "CLIENT_NAME" --item "Cashflow setup session (45–60 min)" --amount 149 --type quote
```

## After paid delivery only

```bash
python tracker.py add 149 income consulting "setup session CLIENT_NAME"
python scripts/income_experiment.py  # mark setup-session-offer won only if your rank/status flow supports it — never before payment
python runway.py
```
