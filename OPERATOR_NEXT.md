# Operator next actions — currency path

**Preferred path:** real tracked income. Never fake won revenue. Zero paid APIs.

| Rank | Experiment | $ | Effort | Score | Status |
|------|------------|---|--------|-------|--------|
| 1 | setup-session-offer | 149 | 3 | 49.67 | active until paid delivery |
| 2 | oss-inbound-help | 99 | 2 | 49.50 | active |
| 3 | template-pack-listing | 79 | 2 | 39.50 | active |

Fleet: [CURRENCY_STATUS.md](CURRENCY_STATUS.md) · Singularity Operator stores next-action with provenance.

---

## Path A — Setup session ($149) — do when you have a name

1. Pick one real prospect (warm first).
2. Send [templates/setup_session_outreach.md](templates/setup_session_outreach.md).
3. On yes → quote + book:
   ```bash
   python scripts/quote.py --client "CLIENT_NAME" --item "Cashflow setup session (45–60 min)" --amount 149 --type quote
   ```
4. Deliver with [templates/setup_session_checklist.md](templates/setup_session_checklist.md).
5. **After payment only:**
   ```bash
   python tracker.py add 149 income consulting "setup session CLIENT_NAME"
   python runway.py
   ```

Assets: offer · SOW · checklist · outreach (all under `templates/`).

---

## Path B — OSS inbound ($99) — do from GitHub today

1. Open recent issues/discussions on **your** public repos or threads where you already reply.
2. Give the free pointer first; if they need hands-on, paste from [templates/oss_inbound_help_offer.md](templates/oss_inbound_help_offer.md).
3. Quote:
   ```bash
   python scripts/quote.py --client "HANDLE" --item "Scoped OSS/setup help (~60 min)" --amount 99 --type quote
   ```
4. Deliver fixed scope → log only after payment.

No warm personal prospect required — works on existing GitHub surface.

---

## Path C — Pack listing ($79) — optional parallel

1. `python scripts/pack_client.py`
2. Paste blurb from [PUBLIC_LISTING.md](PUBLIC_LISTING.md) to Gumroad/Lemon free tier.
3. Attach zip; sell pack-only or upsell setup session.

---

## Right now (no prospect name given)

**Default:** Path B on the next issue you touch + keep Path A outreach ready.  
**If you name one person:** Path A first (higher $).

*Updated for dual-path execution.*
