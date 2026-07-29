# Restaurant App Research

Research, planning, and design documents for a small-restaurant operations system.

## Concept

A two-role app for a single restaurant:

- **Dining / Service** — floor staff (waiters AB, AC, …) take orders per table from a menu of available items, manage guests (count, adults/children, gender), and record payments (cash / card / tip).
- **Kitchen** — cooks run a daily menu via a Telegram bot, upload photos of what's on offer, track finite stock (e.g. *8 pieces of cake today* — each slice sold decrements stock), and get demand estimates based on yesterday's leftovers.

A `index.html` mock-up comes first; the real app follows.

## Folder layout

```
.
├── README.md                       ← this file
├── index.html                      ← ⭐ working mock-up (open in browser)
├── docs/
│   ├── INDEX.md                    ← master index + build order
│   ├── HANDOFF.md                  ← repo tour + what to build next
│   ├── KIMI_K5_PROMPT.md           ← ready-to-paste prompt for the next agent
│   ├── research/   (11 files)      ← broad survey + deep-dive + supplement
│   └── features/   (8 files)       ← one per feature: Goal / Scope / Data Model
├── backend/                        ← ⭐ FastAPI + SQLModel + aiogram skeleton
│   ├── README.md
│   ├── requirements.txt
│   ├── .env.example
│   └── app/
│       ├── main.py / config.py / db.py / models.py
│       ├── routers/tables.py       ← Feature 01 (working)
│       └── bot/cook_bot.py         ← Feature 04 (stub)
└── scripts/                        ← helper scripts (add as needed)
```

## Status

- [x] Broad sweep research (11 files in `research/`)
- [x] Deep-dive on top 5 open-source projects
- [x] Per-feature Markdown files (8 files in `features/`)
- [x] `INDEX.md` with priority ranking + build order
- [x] `HANDOFF.md` for the next agent
- [x] `index.html` mock-up (4 views, mobile-responsive)
- [x] Backend skeleton (FastAPI + SQLModel + aiogram stub)
- [ ] Feature 02 — Order router
- [ ] Feature 03 — Stock tracker
- [ ] Feature 04 — Menu photo OCR
- [ ] Feature 05 — Payment + tip
- [ ] Feature 06 — Reports
- [ ] Feature 07 — Demand estimation