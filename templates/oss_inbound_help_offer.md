# OSS / GitHub inbound — scoped paid help ($99)

**Experiment:** oss-inbound-help · expected $99 · effort 2  
**Rule:** Help first where appropriate; offer paid only for *scoped extra* work. Never mark won without payment.

---

## When to use

- Someone opens an issue / discussion asking for setup, customization, or “can you help me wire this”
- A reply thread is drifting into unpaid consulting
- You spot a public question in your domain (userscripts, zero-cost tooling, autonomous agents) where a fixed-scope hour is fair

## What $99 buys (default scope)

| Include | Exclude |
|---------|--------|
| Up to ~60 min focused help (async or call) | Ongoing retainer |
| One concrete outcome (script working, checklist filled, pack configured) | Unlimited revisions |
| Short written notes + quote/invoice Markdown | Guaranteed business results |

Customize scope in the reply — keep it fixed-price and time-boxed.

## Paste-ready issue / discussion reply

```text
Happy to help point you at the free path first:
- [relevant file or README section]
- [one concrete next command or step]

If you want this done *for you* (wired, tested, notes handed off) I offer a scoped **$99 fixed** help block (~60 min) — same zero-cost stack, no SaaS required on your side.

Reply with:
1) What “done” looks like in one sentence
2) Your timezone / async vs call preference

I’ll send a one-line Markdown quote. Payment before or right after delivery; I only log revenue after paid work.
```

## Quote command

```bash
python scripts/quote.py --client "CLIENT_OR_GITHUB_HANDLE" --item "Scoped OSS/setup help (~60 min)" --amount 99 --type quote
```

## After paid delivery only

```bash
python tracker.py add 99 income consulting "oss inbound help CLIENT"
python runway.py
# then update data/income_experiments.csv status for oss-inbound-help → won if appropriate
```

## Anti-patterns

- Don’t soft-paywall basic docs that should stay free in the README
- Don’t mark experiment won on “interested” — only on payment
- Don’t expand scope mid-block without a new quote
