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
    "PLAYBOOK.md",
    "LICENSE",
    "templates",
    "data/sample_first_week_ledger.csv",
    "data/sample_ledger.csv",
]

README_CLIENT = """# Zero-Cost Client Pack

Personal wealth tracker + playbook using **only free tools**. Offline-ready.

## 3-step delivery checklist

1. Unzip this pack. Confirm Python 3 is available (`python --version`).
2. Copy `templates/client_ledger_template.csv` → `data/ledger.csv` (create the `data/` folder if needed).
3. Run the first commands and hand over the onboarding checklist.

```bash
python tracker.py add 100 income freelance "first client payment"
python tracker.py add 12.50 expense software "domain"
python tracker.py summary
python export.py --client data/ledger.csv
```

Open the generated Markdown report → browser Print → Save as PDF (free).

## What's inside

| Item | Purpose |
|------|---------|
| `tracker.py` | Local CSV ledger CLI |
| `export.py` | Markdown/PDF-ready report |
| `PLAYBOOK.md` | Full zero-cost playbook |
| `templates/` | Client ledger template, onboarding checklist, playbook, pricing notes |
| `data/sample_first_week_ledger.csv` | Realistic first-week demo rows |
| `data/sample_ledger.csv` | Extra sample rows |
| `LICENSE` | MIT |

## Client onboarding

Hand the client [templates/client_onboarding_checklist.md](templates/client_onboarding_checklist.md).

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

    # Ensure data/ exists even if only samples are present
    (STAGING / "data").mkdir(parents=True, exist_ok=True)

    # Client-facing README
    (STAGING / "README_CLIENT.md").write_text(README_CLIENT, encoding="utf-8")

    zip_path = DIST / ZIP_NAME
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in STAGING.rglob("*"):
            if path.is_file():
                arcname = path.relative_to(STAGING)
                zf.write(path, arcname)

    # Clean staging
    shutil.rmtree(STAGING)

    print(f"Created: {zip_path}")
    print(f"Size:    {zip_path.stat().st_size} bytes")
    print("Hand the zip to a client — they unzip and follow README_CLIENT.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
