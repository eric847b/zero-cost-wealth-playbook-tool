#!/usr/bin/env python3
"""
Free invoice / quote generator — Markdown only, zero cost.
No Stripe, no paid invoicing SaaS required for first sales.

Usage:
  python scripts/quote.py --client "Acme" --item "Cashflow setup" --amount 149 --type quote
  python scripts/quote.py --client "Acme" --item "Monthly review" --amount 79 --type invoice --due 14

Writes: quotes/quote_YYYYMMDD_<slug>.md  (or invoice_...)
"""
from __future__ import annotations

import argparse
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "quotes"


def _slug(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.strip().lower()).strip("-")
    return s[:40] or "client"


def build(client: str, item: str, amount: float, doc_type: str, due_days: int, notes: str) -> str:
    today = date.today()
    due = today + timedelta(days=due_days)
    title = "Quote" if doc_type == "quote" else "Invoice"
    lines = [
        f"# {title}",
        "",
        f"**Date:** {today.isoformat()}  ",
        f"**{'Valid until' if doc_type == 'quote' else 'Due'}:** {due.isoformat()}  ",
        f"**Client:** {client}  ",
        f"**Document:** {doc_type.upper()}-{today.strftime('%Y%m%d')}",
        "",
        "## Line items",
        "",
        "| Description | Amount |",
        "|-------------|--------|",
        f"| {item} | {amount:.2f} |",
        "",
        f"**Total: {amount:.2f}**",
        "",
        "## Payment (zero-cost options)",
        "",
        "- Bank transfer / Zelle / local transfer",
        "- Wave (free invoicing) or similar free tier",
        "- Cash / check where appropriate",
        "",
        "## Scope",
        "",
        notes or "Delivered per Zero-Cost Wealth Playbook Tool scope. No paid SaaS dependencies.",
        "",
        "---",
        "Generated with `scripts/quote.py` — free, offline, Markdown. Print → PDF if needed.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Free quote/invoice Markdown generator")
    p.add_argument("--client", required=True)
    p.add_argument("--item", required=True, help="Line item description")
    p.add_argument("--amount", type=float, required=True)
    p.add_argument("--type", choices=("quote", "invoice"), default="quote")
    p.add_argument("--due", type=int, default=14, help="Days until valid/due date")
    p.add_argument("--notes", default="")
    args = p.parse_args()

    text = build(args.client, args.item, args.amount, args.type, args.due, args.notes)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fname = f"{args.type}_{date.today().strftime('%Y%m%d')}_{_slug(args.client)}.md"
    path = OUT_DIR / fname
    path.write_text(text, encoding="utf-8")
    print(text)
    print(f"\n[wrote {path}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
