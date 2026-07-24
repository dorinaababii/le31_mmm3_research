# Master Index — Restaurant App Research

> **Status**: Research phase complete (broad sweep + deep-dive done).
> **Next**: User picks priority features → we build `index.html` mock-up → backend.

---

## What we recommend

A **thin Python (FastAPI + aiogram + PostgreSQL) app** with three surfaces:

1. **Waiter UI** — `index.html` + REST API (FastAPI)
2. **Cook UI** — Telegram bot (aiogram)
3. **Manager UI** — `index.html` reports + CSV export

**Why not fork an existing project?** None of the open-source POS systems
match the spec (Telegram-driven kitchen + first-class prepared-item stock +
table-side ordering with demographics). TastyIgniter is the closest but
Laravel-heavy and lacks Telegram integration. URY is great but requires
ERPNext (overkill for one restaurant).

See [`research/09-recommended-stack.md`](research/09-recommended-stack.md) for the full architecture.

---

## Research findings (broad survey + deep-dive)

| File | Topic |
|---|---|
| [research/00-landscape-overview.md](research/00-landscape-overview.md) | Overview + verdict on the existing landscape |
| [research/01-pos-systems.md](research/01-pos-systems.md) | TastyIgniter, URY, Flutter POS, RestoPOS, ... |
| [research/02-kitchen-display.md](research/02-kitchen-display.md) | URY Mosaic, CampusBites, OpenKDS, ... |
| [research/03-inventory-stock.md](research/03-inventory-stock.md) | **The killer feature gap** — no one does prepared-item batches well |
| [research/04-menu-ocr.md](research/04-menu-ocr.md) | PaddleOCR, RapidOCR, donut, OCRmyPDF |
| [research/05-telegram-bots.md](research/05-telegram-bots.md) | python-telegram-bot vs aiogram |
| [research/06-payments-tips.md](research/06-payments-tips.md) | Tip derived from `paid − consumed` (cleaner than manual entry) |
| [research/07-guest-analytics.md](research/07-guest-analytics.md) | Demographic capture + privacy stance |
| [research/08-deep-dive-top-5.md](research/08-deep-dive-top-5.md) | Top 5 fork candidates — verdict each |
| [research/09-recommended-stack.md](research/09-recommended-stack.md) | **Architecture sketch + DDL** |
| [research/10-async-supplement.md](research/10-async-supplement.md) | 5 additional projects from the async subagent (chefcito, satisfecho, Umi-OCR, AstrBot, Tip_Reconciliation) + refined gaps list |

---

## Features we could build (one file each)

Priority: 🟢 high, 🟡 medium, ⚪ low.

| # | Feature | File | Priority | Notes |
|---|---|---|---|---|
| 01 | Table management | [features/01-table-management.md](features/01-table-management.md) | 🟢 | Visual floor grid |
| 02 | Order taking | [features/02-order-taking.md](features/02-order-taking.md) | 🟢 | Waiter-side core flow |
| 03 | **Kitchen stock tracker** | [features/03-kitchen-stock-tracker.md](features/03-kitchen-stock-tracker.md) | 🟢 | **The killer feature** — finite stock of prepared items |
| 04 | **Menu photo bot** | [features/04-menu-photo-bot.md](features/04-menu-photo-bot.md) | 🟢 | Cook's morning Telegram photo → today's menu |
| 05 | Payment + tip derivation | [features/05-payment-tip-reconciliation.md](features/05-payment-tip-reconciliation.md) | 🟢 | `tip = paid − consumed` |
| 06 | Guest demographics + reports | [features/06-guest-demographics.md](features/06-guest-demographics.md) | 🟡 | Privacy-respecting, no PII in v1 |
| 07 | Demand estimation | [features/07-demand-estimation.md](features/07-demand-estimation.md) | 🟡 | Simple 14-day average + 10 % buffer |
| 08 | index.html mock-up | [features/08-index-mockup.md](features/08-index-mockup.md) | 🟢 | **Build this first** — visualizes 01–03 + 06 |

---

## Suggested build order

1. **Mock-up** (08) — `index.html` showing floor + order + reports. Pure HTML/JS, no backend.
   *Iterate on UX with the user until happy.*
2. **Backend skeleton** — FastAPI app, PostgreSQL schema, auth (PIN per user).
3. **Table mgmt + order taking** (01, 02) — waiter can seat a party, take orders, close visit.
4. **Menu photo bot** (04) — cook's morning Telegram flow.
5. **Stock tracker** (03) — batches, ledger, sold-out alerts.
6. **Payment + tip** (05) — bill, derived tip, shift close.
7. **Reports** (06) — manager dashboard.
8. **Demand estimation** (07) — once we have 14 days of data.

---

## Open questions for the user (blocks before we code)

These are listed in `research/09-recommended-stack.md` — repeated here for visibility:

1. **Menu language**? Drives OCR engine choice (PaddleOCR for CN, RapidOCR for EU languages).
2. **Currency**? Single or multi.
3. **Tax**? Flat or per-category.
4. **Hardware** for waiters? Tablet / phone / desktop.
5. **Single restaurant or chain**? Drives tenancy.
6. **Service charge** (auto-added %)? EU common, US not. Decide before bill code.
7. **Tip pool** (split tips across staff)? In scope v1 or v2?

---

## Repo conventions

- `docs/research/` — broad surveys + deep dives (read first to get the lay of the land).
- `docs/features/` — one file per feature with Goal / Scope / Description / Data Model / Dependencies / Open Questions.
- `index.html` (root) — the actual mock-up, when built.
- Backend code (later) — `app/` (FastAPI), `bot/` (aiogram), `db/` (schema + migrations).