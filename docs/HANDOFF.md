# Handoff — Restaurant App Project

> **Audience**: any agent (or human) picking up this repo after the research phase.
> **Last updated**: 2026-07-24.
> **Research completed by**: Hermes (MiniMax-M3). Implementation handed off to next agent (Kimi K5).

## What this repo is

A two-role restaurant operations system:

- **Dining / Service** — waiters take orders, seat parties, close bills (web UI).
- **Kitchen** — cook drives daily menu + stock via a Telegram bot.

Plus management reports and demand forecasting.

## Repo layout

```
le31_mmm3_research/
├── README.md                       ← project pitch + folder map
├── index.html                      ← ⭐ MOCK-UP (single self-contained HTML, no build)
├── docs/
│   ├── INDEX.md                    ← master index, build order, open questions
│   ├── HANDOFF.md                  ← you are here
│   ├── research/                   ← 11 files: landscape survey, deep-dive, supplement
│   └── features/                   ← 8 files: per-feature spec (Goal / Scope / Data Model / etc.)
├── backend/                        ← ⭐ REAL APP STARTS HERE
│   ├── README.md                   ← backend-specific setup & layout
│   ├── requirements.txt
│   ├── .env.example
│   └── app/
│       ├── main.py                 ← FastAPI entry
│       ├── config.py               ← Settings
│       ├── db.py                   ← Engine + session
│       ├── models.py               ← SQLModel tables (matches research/09 schema)
│       ├── routers/
│       │   └── tables.py           ← Feature 01 done
│       └── bot/
│           └── cook_bot.py         ← Feature 04 stub (needs OCR wiring)
├── scripts/                        ← helper scripts (currently empty — add as needed)
└── .gitignore                      ← excludes .env, *.key, etc.
```

## What's done

✅ **Research phase** — broad survey + deep-dive of 30+ open-source projects, written-up as Markdown. See `docs/research/00-landscape-overview.md` for the verdict and `09-recommended-stack.md` for the architecture.

✅ **Mock-up** — `index.html` is a single self-contained HTML file showing 4 views:
- **Floor**: table grid with status colors (free/seated/ordered/billed/dirty)
- **Order**: menu picker + current order + bill panel with derived tip
- **Reports**: KPI cards + covers-by-hour chart + top items
- **Bot**: fake Telegram chat showing the cook's morning menu-upload flow

✅ **Backend skeleton** — FastAPI + SQLModel + aiogram, all runnable. The `tables` router works (list + seat).

## What's NOT done (the next agent's job)

Listed in priority order. See `docs/INDEX.md` for the full roadmap.

| # | Feature | Doc | Where it lives |
|---|---|---|---|
| 02 | Order taking | `docs/features/02-order-taking.md` | `backend/app/routers/orders.py` (new) |
| 03 | Kitchen stock tracker | `docs/features/03-kitchen-stock-tracker.md` | `backend/app/routers/stock.py` (new) + integration into order close |
| 04 | Menu photo OCR | `docs/features/04-menu-photo-bot.md` | `backend/app/bot/cook_bot.py` (extend) + `backend/app/ocr/` (new) |
| 05 | Payment + tip | `docs/features/05-payment-tip-reconciliation.md` | `backend/app/routers/bills.py` (new) |
| 06 | Guest demographics + reports | `docs/features/06-guest-demographics.md` | `backend/app/routers/reports.py` (new) |
| 07 | Demand estimation | `docs/features/07-demand-estimation.md` | `backend/app/services/forecast.py` (new) |
| 08 | index.html mock-up | `docs/features/08-index-mockup.md` | `index.html` (extend / replace) |

## Architectural decisions already made

These are **non-negotiable** unless the user explicitly changes them. They come from the research and the user has approved them via the clarifications.

1. **Build fresh, don't fork** — none of the existing open-source POSes match the spec (Telegram kitchen + prepared-item stock + table-side ordering + tip derived from `paid − consumed`). Forks would inherit opinionated frameworks.

2. **Stack**: Python 3.11+ · FastAPI · SQLModel · aiogram · Postgres (prod) / SQLite (dev) · RapidOCR + small LLM call.

3. **Batch + StockEntry ledger** for the killer feature. `StockEntry` is append-only; current stock = `SUM(qty_delta)` per batch. Never UPDATE or DELETE.

4. **Derived tip** = `total_paid − subtotal_items − subtotal_tax`. No manual tip entry. No tip pooling in v1.

5. **No PII in v1** — guest demographics skip gender (privacy / GDPR). Capture `party_size`, `adults`, `children` only.

6. **Single Telegram bot, role-based via chat_id allowlist** (cook + manager only; waiters use the web UI).

## How to run what exists

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # edit if you have a Telegram token / LLM key
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then:
- <http://localhost:8000/> — the mock-up (visualization of all features)
- <http://localhost:8000/docs> — auto-generated OpenAPI docs
- <http://localhost:8000/api/tables> — `GET` returns the empty tables list (DB initialized on startup)
- <http://localhost:8000/api/health> — liveness check

## Open questions still waiting on the user

These are in `docs/INDEX.md` under "Open questions for the user":

1. Menu language (drives OCR engine)
2. Currency (single or multi)
3. Tax (flat or per-category)
4. Waiter hardware (tablet / phone / desktop)
5. Single restaurant or chain
6. Service charge (auto-added %)
7. Tip pool (split tips across staff) — punted to v2

Defaults are listed in the INDEX; ask the user only if a decision is needed for the next feature you're building.

## What "good" looks like for the next agent

- Implement features in the order above (02 → 03 → 04 → 05 → 06 → 07).
- For each feature: read its spec file first (`docs/features/0X-*.md`).
- Wire it end-to-end before moving on: DB model → router → bot integration → tested manually.
- Update `docs/INDEX.md` to check off the feature when done.
- Push commits frequently; each commit should reference the feature ID.

## What NOT to do

- Don't introduce a heavy framework (Next.js, Django, Frappe). FastAPI is the boundary.
- Don't store tip as a manual entry. Derive it from `paid − consumed`.
- Don't UPDATE/DELETE StockEntry rows. Append only.
- Don't capture guest gender. v1 is adults/children/party_size only.
- Don't add per-item modifier UIs (size, extras). v1 menu is flat.
- Don't add multi-tenancy. One restaurant.

## Contact

Project owner: dorinaababii (github). Repo: https://github.com/dorinaababii/le31_mmm3_research