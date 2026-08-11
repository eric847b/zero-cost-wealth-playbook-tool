#!/usr/bin/env python3
"""
Zero-cost runway & income-velocity report — stdlib only.
Reads the local CSV ledger and answers currency questions:
  - net / weekly velocity
  - runway weeks (if expenses exceed income)
  - top income categories to double down on

Usage:
  python runway.py
  python runway.py --sample
  python runway.py path/to/ledger.csv
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT = ROOT / "data" / "ledger.csv"
SAMPLE = ROOT / "data" / "sample_ledger.csv"


def _parse_date(s: str) -> date | None:
    try:
        return datetime.strptime((s or "")[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def _rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def analyze(rows: list[dict]) -> dict:
    income = expense = 0.0
    by_income_cat: dict[str, float] = defaultdict(float)
    by_expense_cat: dict[str, float] = defaultdict(float)
    dates: list[date] = []

    for r in rows:
        try:
            amt = float(r.get("amount") or 0)
        except ValueError:
            continue
        t = (r.get("type") or "").lower()
        cat = (r.get("category") or "uncategorized").strip() or "uncategorized"
        d = _parse_date(r.get("date") or "")
        if d:
            dates.append(d)
        if t == "income":
            income += amt
            by_income_cat[cat] += amt
        elif t == "expense":
            expense += amt
            by_expense_cat[cat] += amt

    span_days = 1
    if len(dates) >= 2:
        span_days = max(1, (max(dates) - min(dates)).days + 1)
    weeks = max(span_days / 7.0, 1.0)

    weekly_in = income / weeks
    weekly_out = expense / weeks
    weekly_net = weekly_in - weekly_out
    net = income - expense

    # Runway: if net cash were a buffer and weekly burn positive, how many weeks?
    # If weekly_net >= 0 → sustainable / growing (infinite runway label).
    if weekly_net >= 0:
        runway_weeks = None  # growing or break-even
    else:
        # Assume current net is the only buffer (conservative).
        buffer = max(net, 0.0)
        burn = abs(weekly_net)
        runway_weeks = (buffer / burn) if burn > 0 else None

    top_income = sorted(by_income_cat.items(), key=lambda x: x[1], reverse=True)[:5]
    top_expense = sorted(by_expense_cat.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        "rows": len(rows),
        "span_days": span_days,
        "weeks": round(weeks, 2),
        "income": round(income, 2),
        "expense": round(expense, 2),
        "net": round(net, 2),
        "weekly_in": round(weekly_in, 2),
        "weekly_out": round(weekly_out, 2),
        "weekly_net": round(weekly_net, 2),
        "runway_weeks": None if runway_weeks is None else round(runway_weeks, 1),
        "top_income": top_income,
        "top_expense": top_expense,
    }


def recommend(stats: dict) -> list[str]:
    tips: list[str] = []
    if stats["rows"] == 0:
        tips.append("Ledger empty — log one real income and one expense today with tracker.py add.")
        return tips
    if stats["weekly_net"] < 0:
        tips.append(
            f"Negative velocity ({stats['weekly_net']:+.2f}/wk). Cut top expense category "
            f"or ship one income experiment this week (see scripts/income_experiment.py)."
        )
        if stats["runway_weeks"] is not None:
            tips.append(f"Conservative runway from current net buffer: ~{stats['runway_weeks']} weeks.")
    else:
        tips.append(
            f"Positive velocity ({stats['weekly_net']:+.2f}/wk). Double down on top income category "
            f"and raise one price or one package (templates/pricing_notes.md)."
        )
    if stats["top_income"]:
        cat, amt = stats["top_income"][0]
        tips.append(f"Highest income category: {cat} ({amt:.2f}) — package that as a repeatable offer.")
    tips.append("Generate a free quote: python scripts/quote.py --help")
    return tips


def render(stats: dict, source: Path) -> str:
    lines = [
        "# Zero-Cost Runway Report",
        "",
        f"**Generated:** {date.today().isoformat()}  ",
        f"**Source:** `{source.as_posix()}`  ",
        f"**Rows / span:** {stats['rows']} rows · {stats['span_days']} days (~{stats['weeks']} wk)",
        "",
        "## Cash summary",
        "",
        f"| Metric | Amount |",
        f"|--------|--------|",
        f"| Income | {stats['income']:.2f} |",
        f"| Expense | {stats['expense']:.2f} |",
        f"| Net | {stats['net']:.2f} |",
        f"| Weekly in | {stats['weekly_in']:.2f} |",
        f"| Weekly out | {stats['weekly_out']:.2f} |",
        f"| Weekly net | {stats['weekly_net']:+.2f} |",
    ]
    if stats["runway_weeks"] is None:
        lines.append("| Runway | growing / break-even |")
    else:
        lines.append(f"| Runway (conservative) | ~{stats['runway_weeks']} weeks |")

    lines.extend(["", "## Top income categories", ""])
    if stats["top_income"]:
        for cat, amt in stats["top_income"]:
            lines.append(f"- **{cat}**: {amt:.2f}")
    else:
        lines.append("_No income rows._")

    lines.extend(["", "## Top expense categories", ""])
    if stats["top_expense"]:
        for cat, amt in stats["top_expense"]:
            lines.append(f"- **{cat}**: {amt:.2f}")
    else:
        lines.append("_No expense rows._")

    lines.extend(["", "## Next currency moves", ""])
    for t in recommend(stats):
        lines.append(f"- {t}")

    lines.extend([
        "",
        "---",
        "Stdlib only. No paid APIs. Pair with `python tracker.py summary` and `python export.py`.",
        "",
    ])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv and argv[0] == "--sample":
        path = SAMPLE
    elif argv:
        path = Path(argv[0])
    else:
        path = DEFAULT if DEFAULT.exists() else SAMPLE

    rows = _rows(path)
    stats = analyze(rows)
    text = render(stats, path)
    out = ROOT / "runway_report.md"
    out.write_text(text, encoding="utf-8")
    print(text)
    print(f"\n[wrote {out}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
