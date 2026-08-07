#!/usr/bin/env python3
"""
Zero-cost wealth tracker — local CSV ledger.
No paid APIs. Offline. Free-tool compatible (LibreOffice / Google Sheets import).

Usage:
  python tracker.py add <amount> <type> <category> [note...]
  python tracker.py list
  python tracker.py summary

Types: income | expense
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

LEDGER = Path(__file__).resolve().parent / "data" / "ledger.csv"
FIELDS = ["date", "type", "amount", "category", "note"]


def _ensure_ledger() -> None:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    if not LEDGER.exists():
        with LEDGER.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()


def _read_rows() -> list[dict]:
    _ensure_ledger()
    with LEDGER.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cmd_add(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: python tracker.py add <amount> <type:income|expense> <category> [note...]")
        return 2
    try:
        amount = float(argv[0])
    except ValueError:
        print("amount must be a number")
        return 2
    tx_type = argv[1].lower()
    if tx_type not in ("income", "expense"):
        print("type must be income or expense")
        return 2
    category = argv[2]
    note = " ".join(argv[3:]) if len(argv) > 3 else ""

    _ensure_ledger()
    with LEDGER.open("a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=FIELDS).writerow(
            {
                "date": date.today().isoformat(),
                "type": tx_type,
                "amount": f"{amount:.2f}",
                "category": category,
                "note": note,
            }
        )
    print(f"Tracked {tx_type} {amount:.2f} [{category}] {note}".rstrip())
    return 0


def cmd_list(_: list[str]) -> int:
    rows = _read_rows()
    if not rows:
        print("(ledger empty)")
        return 0
    print(f"{'date':12} {'type':8} {'amount':>10} {'category':16} note")
    print("-" * 60)
    for r in rows:
        print(
            f"{r.get('date',''):12} {r.get('type',''):8} "
            f"{r.get('amount',''):>10} {r.get('category',''):16} {r.get('note','')}"
        )
    return 0


def cmd_summary(_: list[str]) -> int:
    rows = _read_rows()
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
    print(f"Income:  {income:.2f}")
    print(f"Expense: {expense:.2f}")
    print(f"Net:     {income - expense:.2f}")
    print("\nBy category (net):")
    for cat, net in sorted(by_cat.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:20} {net:+.2f}")
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(__doc__)
        return 0
    cmd = argv[0].lower()
    rest = argv[1:]
    if cmd == "add":
        return cmd_add(rest)
    if cmd == "list":
        return cmd_list(rest)
    if cmd == "summary":
        return cmd_summary(rest)
    print(f"Unknown command: {cmd}")
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
