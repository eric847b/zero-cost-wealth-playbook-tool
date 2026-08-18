# Zero-Cost Wealth Playbook Tool

Personal wealth acceleration using **only free tools**. No paid APIs, no subscriptions required.

**Version:** see [VERSION](VERSION) · **License:** MIT

## Windows single-file executables

Download the latest **Release** from the [Releases page](https://github.com/eric847b/zero-cost-wealth-playbook-tool/releases).

| Binary | Purpose |
|--------|---------|
| `wealth-tracker.exe` | Local CSV ledger CLI |
| `wealth-runway.exe` | Weekly velocity + runway report |
| `wealth-export.exe` | Markdown / PDF-ready report |
| `wealth-quote.exe` | Free quote & invoice generator |
| `wealth-experiment.exe` | Rank income experiments |
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
git tag v1.0.0
git push origin v1.0.0
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
python scripts/quote.py --client "Acme" --item "Cashflow setup session (45–60 min)" --amount 149 --type quote
```

## Setup session (sellable)

| File | Purpose |
|------|---------|
| [templates/setup_session_sow.md](templates/setup_session_sow.md) | SOW |
| [templates/setup_session_checklist.md](templates/setup_session_checklist.md) | Live delivery checklist |

## Client pack contents

`tracker.py` · `runway.py` · `export.py` · `scripts/quote.py` · `scripts/income_experiment.py` · templates (incl. SOW) · sample data · niches

## Status
- #21 closed (runway + experiments + quote CLI).
- **Listed publicly:** `PUBLIC_LISTING.md` + updated pack.
- Release packaging + Windows single-file EXE workflow added.
- Keep everything zero-cost. Never log simulated income.
