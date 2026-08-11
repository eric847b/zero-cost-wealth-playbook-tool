#!/usr/bin/env python3
"""
Income experiment board — track monetization experiments with expected revenue.
Zero-cost. Stdlib + local CSV. Rank by expected $ / effort.

Usage:
  python scripts/income_experiment.py add <name> <expected_revenue> <effort_1_to_5> [note...]
  python scripts/income_experiment.py list
  python scripts/income_experiment.py rank
  python scripts/income_experiment.py status <id> <planned|active|won|lost|paused>
  python scripts/income_experiment.py summary

Board file: data/income_experiments.csv
"""
from __future__ import annotations

import csv
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / "data" / "income_experiments.csv"
FIELDS = ["id", "date", "name", "expected_revenue", "effort", "status", "note", "score"]
VALID_STATUS = frozenset({"planned", "active", "won", "lost", "paused"})


def _ensure() -> None:
    BOARD.parent.mkdir(parents=True, exist_ok=True)
    if not BOARD.exists():
        with BOARD.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()


def _read() -> list[dict]:
    _ensure()
    with BOARD.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _write(rows: list[dict]) -> None:
    _ensure()
    with BOARD.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


def _score(expected: float, effort: int) -> float:
    # Higher expected $ and lower effort → higher score. Effort 1–5.
    effort = max(1, min(5, effort))
    return round(expected / effort, 2)


def cmd_add(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: add <name> <expected_revenue> <effort_1_to_5> [note...]")
        return 2
    name = argv[0]
    try:
        expected = float(argv[1])
        effort = int(argv[2])
    except ValueError:
        print("expected_revenue must be number; effort must be int 1–5")
        return 2
    if effort < 1 or effort > 5:
        print("effort must be 1–5")
        return 2
    note = " ".join(argv[3:]) if len(argv) > 3 else ""
    rows = _read()
    next_id = 1
    if rows:
        try:
            next_id = max(int(r.get("id") or 0) for r in rows) + 1
        except ValueError:
            next_id = len(rows) + 1
    sc = _score(expected, effort)
    rows.append({
        "id": str(next_id),
        "date": date.today().isoformat(),
        "name": name,
        "expected_revenue": f"{expected:.2f}",
        "effort": str(effort),
        "status": "planned",
        "note": note,
        "score": f"{sc:.2f}",
    })
    _write(rows)
    print(f"Added experiment #{next_id} '{name}' expected={expected:.2f} effort={effort} score={sc:.2f}")
    return 0


def cmd_list(_: list[str]) -> int:
    rows = _read()
    if not rows:
        print("(no experiments — add one)")
        return 0
    print(f"{'id':4} {'status':8} {'score':>8} {'expected':>10} {'effort':>6} name")
    print("-" * 72)
    for r in rows:
        print(
            f"{r.get('id',''):4} {r.get('status',''):8} {r.get('score',''):>8} "
            f"{r.get('expected_revenue',''):>10} {r.get('effort',''):>6} {r.get('name','')}"
        )
    return 0


def cmd_rank(_: list[str]) -> int:
    rows = _read()
    open_rows = [r for r in rows if (r.get("status") or "").lower() in ("planned", "active")]
    if not open_rows:
        print("(no planned/active experiments)")
        return 0
    open_rows.sort(key=lambda r: float(r.get("score") or 0), reverse=True)
    print("Ranked open experiments (expected $ / effort):")
    for i, r in enumerate(open_rows, 1):
        print(
            f"{i}. #{r.get('id')} score={r.get('score')} "
            f"expected={r.get('expected_revenue')} effort={r.get('effort')} — {r.get('name')}"
        )
    top = open_rows[0]
    print(f"\nNext action: execute experiment #{top.get('id')} ({top.get('name')}) first.")
    return 0


def cmd_status(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: status <id> <planned|active|won|lost|paused>")
        return 2
    eid = argv[0]
    st = argv[1].lower()
    if st not in VALID_STATUS:
        print(f"status must be one of {sorted(VALID_STATUS)}")
        return 2
    rows = _read()
    found = False
    for r in rows:
        if str(r.get("id")) == str(eid):
            r["status"] = st
            found = True
            break
    if not found:
        print(f"No experiment id={eid}")
        return 1
    _write(rows)
    print(f"Experiment #{eid} → {st}")
    return 0


def cmd_summary(_: list[str]) -> int:
    rows = _read()
    by_st: dict[str, int] = {}
    pipeline = 0.0
    won = 0.0
    for r in rows:
        st = (r.get("status") or "planned").lower()
        by_st[st] = by_st.get(st, 0) + 1
        try:
            exp = float(r.get("expected_revenue") or 0)
        except ValueError:
            exp = 0.0
        if st in ("planned", "active"):
            pipeline += exp
        elif st == "won":
            won += exp
    print(f"Experiments: {len(rows)}")
    for st, n in sorted(by_st.items()):
        print(f"  {st}: {n}")
    print(f"Open pipeline (planned+active expected $): {pipeline:.2f}")
    print(f"Won expected $ (marked won): {won:.2f}")
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
    if cmd == "rank":
        return cmd_rank(rest)
    if cmd == "status":
        return cmd_status(rest)
    if cmd == "summary":
        return cmd_summary(rest)
    print(f"Unknown command: {cmd}")
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
