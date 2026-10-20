# Currency Status (machine-readable fleet signal)

**Repo:** eric847b/zero-cost-wealth-playbook-tool  
**Version:** 1.0.1  
**Updated:** 2026-10-20  
**Preferred currency path:** true

## Capabilities
- tracker — local CSV ledger (`tracker.py`)
- runway — weekly velocity + runway weeks (`runway.py`)
- income_experiment_rank — expected $/effort ranking (`scripts/income_experiment.py rank`)
- income_experiment_suggest — free-AI optional + heuristic fallback (`scripts/income_experiment.py suggest`)
- quote — Markdown quote/invoice (`scripts/quote.py`)
- client_pack — offline pack (`scripts/pack_client.py`)
- public_listing — Gumroad/Lemon free-tier blurb (`PUBLIC_LISTING.md`)

## Ranking hints for continuous_roi_rank
1. Prefer work that increases real tracked income or reduces burn (runway positive velocity).
2. Prefer open experiments with highest score (expected_revenue / effort).
3. Prefer shipping public listing / client pack / quote tooling over simulated balances.
4. Never require paid APIs; free-AI suggest is optional.

## Status codes (for fleet)
- `healthy` — repo public, VERSION present, core scripts present
- `preferred` — CONTINUOUS_CONTEXT and SO continuous_roi_rank should bias toward this path

```json
{
  "source": "eric847b/zero-cost-wealth-playbook-tool",
  "version": "1.0.1",
  "preferred_currency_path": true,
  "status": "healthy",
  "capabilities": [
    "tracker",
    "runway",
    "income_experiment_rank",
    "income_experiment_suggest",
    "quote",
    "client_pack",
    "public_listing"
  ],
  "roi_note": "Prefer currency fleet work: runway velocity, experiment rank/suggest, quote, public listing. Zero paid APIs."
}
```
