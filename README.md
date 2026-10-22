# Zero-Cost Wealth Playbook Tool

Personal wealth acceleration using **only free tools**. No paid APIs, no subscriptions required.

**Version:** 1.0.2 · **License:** MIT

## Primary offer — Cashflow Setup Session ($149)

**45–60 min live setup.** Offline ledger + runway + one ranked experiment. Same-day report.

→ **[Client-facing offer page](templates/setup_session_offer.md)** (paste-ready)  
→ SOW: [templates/setup_session_sow.md](templates/setup_session_sow.md) · Checklist: [templates/setup_session_checklist.md](templates/setup_session_checklist.md)

```bash
python scripts/quote.py --client "Name" --item "Cashflow setup session (45–60 min)" --amount 149 --type quote
```

Only mark the experiment `won` after real paid delivery. Never fake revenue.

## Fleet signal (for Singularity Operator)

Machine-readable status for `continuous_roi_rank`:
**[CURRENCY_STATUS.md](CURRENCY_STATUS.md)** — version, capabilities, ranked open experiments, JSON block.

Consumed by `eric847b/singularity-operator` via `GitHubSeamless.fetch_currency_signals()`.

## Windows single-file executables

Download the latest **Release** from the [Releases page](https://github.com/eric847b/zero-cost-wealth-playbook-tool/releases).

| Binary | Purpose |
|--------|---------|
| `wealth-tracker.exe` | Local CSV ledger CLI |
| `wealth-runway.exe` | Weekly velocity + runway report |
| `wealth-export.exe` | Markdown / PDF-ready report |
| `wealth-quote.exe` | Free quote & invoice generator |
| `wealth-experiment.exe` | Rank + suggest income experiments |
| `zero-cost-client-pack.zip` | Full offline client pack (Python source + templates) |

No Python install required for the `.exe` files. Place them next to a `data/` folder (created automatically on first run).

```text
wealth-tracker.exe add 100 income freelance "template sale"
wealth-tracker.exe summary
wealth-runway.exe
```

### How a release is built

Push a tag `v*` (or run the **Release** workflow manually). GitHub Actions builds the Windows one-file EXEs with PyInstaller and attaches them to a GitHub Release automatically.

```bash
git tag v1.0.2
git push origin v1.0.2
```

## Public listing

See **[PUBLIC_LISTING.md](PUBLIC_LISTING.md)** — blurb, price anchors, email CTA, pack build steps.  
Repo is public; paste the blurb to Gumroad/Lemon free tier when ready.

```bash
python scripts/pack_client.py   # → dist/zero-cost-client-pack.zip
```

## Playbook

Read **[PLAYBOOK.md](PLAYBOOK.md)** — track → free stack → monetization moves → weekly loop.

## Tracker (Python)

```bash
python tracker.py add 100 income freelance "template sale"
python tracker.py summary
```

## Runway / experiments / quotes

```bash
python runway.py --sample
python scripts/income_experiment.py rank
python scripts/income_experiment.py suggest   # free-AI optional + heuristic fallback
python scripts/quote.py --client "Acme" --item "Cashflow setup session (45–60 min)" --amount 149 --type quote
```

## Client pack contents

`tracker.py` · `runway.py` · `export.py` · `scripts/quote.py` · `scripts/income_experiment.py` · templates (incl. offer + SOW) · sample data · niches

## Status
- **v1.0.2:** CURRENCY_STATUS.md fleet signal with live ranked experiments for SO continuous_roi_rank.
- **Offer page:** `templates/setup_session_offer.md` — client-facing $149 CTA live on main.
- **v1.0.1:** `suggest` command — free-AI optional with heuristic fallback. Never requires a key.
- Keep everything zero-cost. Never log simulated income.
