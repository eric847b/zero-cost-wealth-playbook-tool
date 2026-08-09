# Zero-Cost Wealth Playbook Tool

Personal wealth acceleration using **only free tools**. No paid APIs, no subscriptions required.

## Playbook

Read **[PLAYBOOK.md](PLAYBOOK.md)** — track → free stack → first three monetization moves → weekly loop.

## Tracker

Local CSV ledger + CLI — works offline, imports into LibreOffice Calc or Google Sheets.

```bash
# Add income / expense
python tracker.py add 100 income freelance "template sale"
python tracker.py add 12.50 expense software "domain renewal"

# Inspect
python tracker.py list
python tracker.py summary
```

Ledger path: `data/ledger.csv`  
Sample rows: `data/sample_ledger.csv`  
First-week sample: `data/sample_first_week_ledger.csv`  
Columns: `date, type, amount, category, note`

### Free-tool path
1. Run the CLI to log transactions (or copy a sample ledger).
2. Open CSV in **LibreOffice Calc** or **Google Sheets**.
3. Pivot by `category` / `type` for budgets — no paid BI tools.

## Export (print / PDF)

```bash
python export.py --sample   # Markdown report from sample data
python export.py            # from data/ledger.csv
python export.py --client path/to/client_ledger.csv   # ready-to-send client report
```

Writes `export_report.md` (or `client_report.md` with `--client`). Open it and use browser **Print → Save as PDF** (free). Stdlib only.

## Client / Monetization (zero fixed cost)

Reusable pack so you can customize and deliver the free toolkit as a paid service:

| File | Purpose |
|------|---------|
| [templates/client_ledger_template.csv](templates/client_ledger_template.csv) | Clean starter ledger for a new client |
| [templates/client_playbook.md](templates/client_playbook.md) | One-page adaptation guide |
| [templates/client_onboarding_checklist.md](templates/client_onboarding_checklist.md) | Day-0 to Day-7 checklist to hand the client |
| [templates/pricing_notes.md](templates/pricing_notes.md) | Packaging, pricing, delivery (no paid tools) |
| [templates/sales_one_pager.md](templates/sales_one_pager.md) | Paste-ready listing + email copy for the client pack |
| [data/sample_first_week_ledger.csv](data/sample_first_week_ledger.csv) | Realistic first-week rows for demos |

### One-command client pack (zip)

```bash
python scripts/pack_client.py
```

Produces `dist/zero-cost-client-pack.zip` — a client unzips it and follows `README_CLIENT.md`. Stdlib only; no new deps.

### 3-step delivery checklist
1. Run the pack script (or copy the template files + tracker.py + export.py into a client folder).
2. Walk the client through the [onboarding checklist](templates/client_onboarding_checklist.md) and `export.py --client`.
3. Hand over the first Markdown/PDF report and the weekly loop from the client playbook.

See [pricing notes](templates/pricing_notes.md) and the [sales one-pager](templates/sales_one_pager.md) for offer tiers and paste-ready listing copy. Everything stays zero fixed cost.

## Quick start
1. Clone this repo.
2. `python tracker.py add 50 income gift`
3. `python tracker.py summary`
4. `python export.py --sample`
5. `python scripts/pack_client.py`  # optional: build client zip

## Monetization (zero fixed cost)
- Freelance: customize the playbook/tracker for clients.
- Templates: share or sell consulting around the free toolkit.
- Listing copy: use `templates/sales_one_pager.md` on free Gumroad / email.
- Open-source visibility → inbound opportunities.

## Status
- MVP tracker shipped (issue #4).
- Playbook + sample ledger + export shipped (issue #5).
- Client-template pack shipped (issue #6).
- Client onboarding checklist + first-week sample shipped (issue #9).
- One-command client pack zip shipped (issue #11).
- Sales one-pager + listing copy shipped (issue #13).
- Keep everything zero-cost.
