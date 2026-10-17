#!/usr/bin/env python3
"""
Income experiment board — track monetization experiments with expected revenue.
Zero-cost. Stdlib + local CSV. Rank by expected $ / effort.
Optional free-AI suggest (Pollinations no-key / local / free tiers) with pure heuristic fallback.

Usage:
  python scripts/income_experiment.py add <name> <expected_revenue> <effort_1_to_5> [note...]
  python scripts/income_experiment.py list
  python scripts/income_experiment.py rank
  python scripts/income_experiment.py status <id> <planned|active|won|lost|paused>
  python scripts/income_experiment.py summary
  python scripts/income_experiment.py suggest   # free-AI or heuristic next experiments

Board file: data/income_experiments.csv
"""
from __future__ import annotations

import csv
import json
import os
import sys
from datetime import date
from pathlib import Path
from typing import Any

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


def _heuristic_suggestions(rows: list[dict]) -> list[str]:
    """Always-available zero-cost suggestions. No network."""
    tips = [
        "Package tracker + PLAYBOOK as a $49–149 setup session (use scripts/quote.py).",
        "Ship one free public template this week → convert attention into paid customization.",
        "List the client pack on a free Gumroad/Lemon tier using PUBLIC_LISTING.md blurb.",
        "Offer a 45–60 min cashflow setup call; quote with scripts/quote.py --amount 149.",
        "Turn the highest-income category from runway.py into a repeatable productized service.",
    ]
    open_names = {(r.get("name") or "").lower() for r in rows if (r.get("status") or "").lower() in ("planned", "active")}
    filtered = [t for t in tips if not any(k in t.lower() for k in open_names if len(k) > 4)]
    return filtered[:4] or tips[:3]


def _try_free_ai_suggest(context: str) -> list[str] | None:
    """Optional free-AI path (Pollinations no-key first). Returns None on any failure."""
    try:
        import requests  # optional; stdlib fallback always works
    except ImportError:
        return None
    prompt = (
        "You are a zero-cost wealth catalyst. Given this experiment board context, "
        "return ONLY a JSON array of 3 short concrete next income experiments "
        "(each string under 120 chars). Prefer free tools, productized offers, open-source inbound.\n\n"
        f"CONTEXT:\n{context[:1200]}"
    )
    urls = [
        ("https://text.pollinations.ai/openai", {"model": "openai", "messages": [{"role": "user", "content": prompt}], "max_tokens": 400}),
    ]
    # Optional keyed free tiers if present
    if os.getenv("GROQ_API_KEY"):
        urls.append((
            "https://api.groq.com/openai/v1/chat/completions",
            {
                "model": os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 400,
            },
        ))
    for url, payload in urls:
        try:
            headers = {"Content-Type": "application/json"}
            if "groq.com" in url:
                headers["Authorization"] = f"Bearer {os.getenv('GROQ_API_KEY')}"
            resp = requests.post(url, headers=headers, json=payload, timeout=20)
            if resp.status_code >= 300:
                continue
            data = resp.json()
            content = (
                data.get("choices", [{}])[0].get("message", {}).get("content")
                or data.get("text")
                or ""
            )
            content = content.strip()
            # Extract JSON array
            start = content.find("[")
            end = content.rfind("]")
            if start >= 0 and end > start:
                arr = json.loads(content[start : end + 1])
                if isinstance(arr, list) and arr:
                    return [str(x).strip()[:160] for x in arr[:4] if str(x).strip()]
        except Exception:
            continue
    return None


def cmd_suggest(_: list[str]) -> int:
    rows = _read()
    summary_bits = []
    for r in rows[-12:]:
        summary_bits.append(
            f"#{r.get('id')} {r.get('status')} score={r.get('score')} "
            f"exp={r.get('expected_revenue')} effort={r.get('effort')} — {r.get('name')}"
        )
    context = "\n".join(summary_bits) if summary_bits else "(empty board)"
    ai = _try_free_ai_suggest(context)
    if ai:
        print("Free-AI suggested next experiments (zero cost path):")
        for i, s in enumerate(ai, 1):
            print(f"  {i}. {s}")
        print("\nAdd any with: python scripts/income_experiment.py add \"<name>\" <expected> <effort>")
        return 0
    print("Heuristic next experiments (no network / free-AI unavailable):")
    for i, s in enumerate(_heuristic_suggestions(rows), 1):
        print(f"  {i}. {s}")
    print("\nAdd any with: python scripts/income_experiment.py add \"<name>\" <expected> <effort>")
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
    if cmd == "suggest":
        return cmd_suggest(rest)
    print(f"Unknown command: {cmd}")
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
