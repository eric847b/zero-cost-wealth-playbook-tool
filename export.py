#!/usr/bin/env python3
"""
Zero-cost export — Markdown report from ledger + playbook path.
Stdlib only. Print or open in any Markdown viewer; browser Print → PDF.

Usage:
  python export.py              # uses data/ledger.csv
  python export.py --sample     # uses data/sample_ledger.csv
  python export.py --client [path]  # client-ready report (default: templates/client_ledger_template.csv)
  python export.py path/to.csv
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_LEDGER = ROOT / "data" / "ledger.csv"
SAMPLE_LEDGER = ROOT / "data" / "sample_ledger.csv"
CLIENT_TEMPLATE = ROOT / "templates" / "client_ledger_template.csv"
OUT = ROOT / "export_report.md"
CLIENT_OUT = ROOT / "client_report.md"


def _rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _summary(rows: list[dict]) -> tuple[float, float, dict[str, float]]:
    by_cat: dict[str, float] = defaultdict(float)
    income = expense = 0.0
    for r in rows:
        try:
            amt = float(r.get("amount") or 0)
        except ValueError:
            continue
        t = (r.get("type") or "").lower()
        cat = r.get("category") or "uncategorized"
        if t == "income":
            income += amt
            by_cat[cat] += amt
        elif t == "expense":
            expense += amt
            by_cat[cat] -= amt
    return income, expense, dict(by_cat)


def build_report(ledger: Path, client_mode: bool = False) -> str:
    rows = _rows(ledger)
    income, expense, by_cat = _summary(rows)
    title = "# Client Wealth Report" if client_mode else "# Zero-Cost Wealth Report"
    lines = [
        title,
        "",
        f"**Generated:** {date.today().isoformat()}  ",
        f"**Source:** `{ledger.as_posix()}`  ",
        f"**Rows:** {len(rows)}",
        "",
        "## Summary",
        "",
        f"| Metric | Amount |",
        f"|--------|--------|",
        f"| Income | {income:.2f} |",
        f"| Expense | {expense:.2f} |",
        f"| Net | {income - expense:.2f} |",
        "",
        "## By category (net)",
        "",
    ]
    if by_cat:
        lines.append("| Category | Net |")
        lines.append("|----------|-----|")
        for cat, net in sorted(by_cat.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"| {cat} | {net:+.2f} |")
    else:
        lines.append("_No categorized rows. Add entries with `python tracker.py add ...`_")

    lines.extend([
        "",
        "## Transactions",
        "",
    ])
    if rows:
        lines.append("| Date | Type | Amount | Category | Note |")
        lines.append("|------|------|--------|----------|------|")
        for r in rows:
            lines.append(
                f"| {r.get('date', '')} | {r.get('type', '')} | {r.get('amount', '')} | "
                f"{r.get('category', '')} | {r.get('note', '')} |"
            )
    else:
        lines.append("_Ledger empty._")

    if client_mode:
        lines.extend([
            "",
            "---",
            "",
            "Prepared with the Zero-Cost Wealth Playbook Tool.  ",
            "See the attached client_playbook.md for the weekly loop.  ",
            "Print this file or open in a browser and **Print → Save as PDF** (free).",
            "",
        ])
    else:
        lines.extend([
            "",
            "---",
            "",
            "Playbook: see [PLAYBOOK.md](PLAYBOOK.md).  ",
            "Print this file or open in a browser and **Print → Save as PDF** (free).",
            "",
        ])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    client_mode = False
    out_path = OUT

    if argv and argv[0] == "--sample":
        ledger = SAMPLE_LEDGER
    elif argv and argv[0] == "--client":
        client_mode = True
        out_path = CLIENT_OUT
        if len(argv) > 1:
            ledger = Path(argv[1])
        else:
            ledger = CLIENT_TEMPLATE if CLIENT_TEMPLATE.exists() else SAMPLE_LEDGER
    elif argv:
        ledger = Path(argv[0])
    else:
        ledger = DEFAULT_LEDGER if DEFAULT_LEDGER.exists() else SAMPLE_LEDGER

    text = build_report(ledger, client_mode=client_mode)
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote {out_path}")
    print(text[:500] + ("..." if len(text) > 500 else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
