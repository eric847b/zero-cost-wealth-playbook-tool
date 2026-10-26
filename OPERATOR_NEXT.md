# Operator next action — setup-session-offer

**Experiment:** setup-session-offer  
**Score:** 49.67 · **Expected:** $149 · **Effort:** 3 · **Status:** active until *real* paid delivery  
**Policy:** Never mark `won` or log income without payment. Zero paid APIs.

Fleet signal: [CURRENCY_STATUS.md](CURRENCY_STATUS.md)  
Singularity Operator maps this via `currency_next_action` → concrete steps + hub handoff.

---

## Do this now (order)

1. **Pick one real prospect** (warm first: past collab, GitHub reply, friend-of-friend, local freelancer).
2. **Send outreach** from [templates/setup_session_outreach.md](templates/setup_session_outreach.md) (short DM/email).
3. On yes → **quote**:
   ```bash
   python scripts/quote.py --client "CLIENT_NAME" --item "Cashflow setup session (45–60 min)" --amount 149 --type quote
   ```
4. **Book** 45–60 min screen-share; optional: ask for 7–14 day transaction list/CSV.
5. **Deliver** with [templates/setup_session_checklist.md](templates/setup_session_checklist.md) + [templates/setup_session_sow.md](templates/setup_session_sow.md).
6. **After payment only:**
   ```bash
   python tracker.py add 149 income consulting "setup session CLIENT_NAME"
   python runway.py
   ```
   Then update experiment status to `won` in `data/income_experiments.csv` (or via `scripts/income_experiment.py` if you use status updates there).

---

## Assets (already live)

| Asset | Path |
|-------|------|
| Client offer | `templates/setup_session_offer.md` |
| SOW | `templates/setup_session_sow.md` |
| Delivery checklist | `templates/setup_session_checklist.md` |
| Outreach copy | `templates/setup_session_outreach.md` |
| Quote CLI | `scripts/quote.py` |
| Ledger | `tracker.py` → `data/ledger.csv` |

---

## Parallel (if no reply in 48h)

- **#2 oss-inbound-help ($99):** turn one GitHub issue/reply into a scoped paid help offer.
- **#3 template-pack-listing ($79):** paste [PUBLIC_LISTING.md](PUBLIC_LISTING.md) to Gumroad/Lemon free tier + attach `python scripts/pack_client.py` zip.

---

*Updated for operator execution. Code path in singularity-operator already ranks and stores this next action with provenance.*
