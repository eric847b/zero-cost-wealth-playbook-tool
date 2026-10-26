# Autonomous mode

This repository is designed to participate in a **zero human-touch** fleet:

- Consumed by `eric847b/singularity-operator` via `CURRENCY_STATUS.md`
- Improved and reported by scheduled Actions / orchestrator cycles
- Never requires the repo owner to send outreach, book calls, or paste listings for the system to remain healthy

## Invariants

1. Zero paid APIs required for core loops
2. No simulated income in `data/ledger.csv`
3. Experiments stay `active` until real payment is logged by a deliberate ledger write after actual payment
4. Public templates remain complete so *inbound* or future human capacity can convert without rebuilding the offer

## Related

- [OPERATOR_NEXT.md](OPERATOR_NEXT.md) — autonomous default posture
- [CURRENCY_STATUS.md](CURRENCY_STATUS.md) — machine-readable fleet signal
