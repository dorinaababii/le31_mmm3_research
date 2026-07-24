# Restaurant App Research

Research, planning, and design documents for a small-restaurant operations system.

## Concept

A two-role app for a single restaurant:

- **Dining / Service** — floor staff (waiters AB, AC, …) take orders per table from a menu of available items, manage guests (count, adults/children, gender), and record payments (cash / card / tip).
- **Kitchen** — cooks run a daily menu via a Telegram bot, upload photos of what's on offer, track finite stock (e.g. *8 pieces of cake today* — each slice sold decrements stock), and get demand estimates based on yesterday's leftovers.

A `index.html` mock-up comes first; the real app follows.

## Folder layout

```
docs/
├── INDEX.md              ← you are here (start)
├── research/             ← broad survey of existing projects
│   ├── pos-systems.md
│   ├── kitchen-display.md
│   ├── inventory-stock.md
│   ├── menu-ocr.md
│   ├── telegram-bots.md
│   ├── payments-tips.md
│   └── guest-analytics.md
└── features/             ← one .md per feature/extension we could build
    ├── 01-table-management.md
    ├── 02-order-taking.md
    ├── 03-kitchen-stock-tracker.md
    ├── 04-menu-photo-bot.md
    ├── 05-payment-tip-reconciliation.md
    ├── 06-guest-demographics.md
    ├── 07-demand-estimation.md
    └── 08-index-mockup.md
scripts/                  ← helper scripts (build, lint, etc.)
```

## Status

- [ ] Broad sweep research (running)
- [ ] Deep-dive on top 3–5 open-source projects to fork/extend
- [ ] Per-feature Markdown files with Goal / Scope / Description / Data Model / Dependencies / Open Questions
- [ ] `INDEX.md` with priority ranking
- [ ] First commit & push