#!/usr/bin/env python3
"""One-command client pack: produce dist/zero-cost-client-pack.zip

Stdlib only. No paid tools. No new dependencies.

Usage:
    python scripts/pack_client.py

Produces a zip a client can unzip and use offline.
"""

from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
STAGING = DIST / "_staging"
ZIP_NAME = "zero-cost-client-pack.zip"

# Files and dirs to include in the client pack
INCLUDE = [
    "tracker.py",
    "export.py",
    "runway.py",
    "PLAYBOOK.md",
    "PUBLIC_LISTING.md",
    "LICENSE",
    "templates",
    "scripts/quote.py",
    "scripts/income_experiment.py",
    "data/sample_first_week_ledger.csv",
    "data/sample_ledger.csv",
    "data/income_experiments.csv",
]

README_CLIENT = """# Zero-Cost Client Pack

Personal wealth tracker + playbook using **only free tools**. Offline-ready.

## 3-step start

1. Unzip this pack. Confirm Python 3 (`python --version`).
2. Copy `templates/client_ledger_template.csv` → `data/ledger.csv` (create `data/` if needed).
3. Run:

```bash
python tracker.py add 100 income freelance "first payment"
python tracker.py add 12.50 expense software "domain"
python tracker.py summary
python runway.py
python export.py --client data/ledger.csv
```

Open the Markdown report → browser **Print → Save as PDF** (free).

## Paid setup (optional)

If you booked a setup session, your operator follows:
- `templates/setup_session_sow.md`
- `templates/setup_session_checklist.md`

Free quote/invoice generator:
```bash
python scripts/quote.py --client "Your Name" --item "Cashflow setup session" --amount 149 --type quote
```

## What's inside

| Item | Purpose |
|------|---------|
| `tracker.py` | Local CSV ledger CLI |
| `runway.py` | Weekly velocity + runway |
| `export.py` | Markdown/PDF-ready report |
| `scripts/quote.py` | Free quotes & invoices |
| `scripts/income_experiment.py` | Rank income experiments |
| `PLAYBOOK.md` | Full zero-cost playbook |
| `templates/` | Onboarding, SOW, niches, pricing |
| `data/sample_*.csv` | Demo weeks |
| `LICENSE` | MIT |

## Client onboarding

See [templates/client_onboarding_checklist.md](templates/client_onboarding_checklist.md).

Everything stays zero fixed cost. No paid APIs or subscriptions required.
"""


def main() -> int:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)

    for item in INCLUDE:
        src = ROOT / item
        if not src.exists():
            print(f"WARN: missing {item}, skipping", file=sys.stderr)
            continue
        dest = STAGING / item
        if src.is_dir():
            shutil.copytree(src, dest)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)

    (STAGING / "data").mkdir(parents=True, exist_ok=True)
    (STAGING / "scripts").mkdir(parents=True, exist_ok=True)
    (STAGING / "README_CLIENT.md").write_text(README_CLIENT, encoding="utf-8")

    zip_path = DIST / ZIP_NAME
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in STAGING.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(STAGING))

    shutil.rmtree(STAGING)

    print(f"Created: {zip_path}")
    print(f"Size:    {zip_path.stat().st_size} bytes")
    print("Hand the zip to a client — they unzip and follow README_CLIENT.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
