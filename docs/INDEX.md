# Master Index — Restaurant App Research

> **Status**: Research phase complete. Mock-up built. Backend skeleton in place.
> **Next**: Implementation phase — features 02 → 07 in `docs/INDEX.md` order.
> **Start here** (if you're the next agent): [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) → [`HANDOFF.md`](HANDOFF.md) → [`KIMI_K5_PROMPT.md`](KIMI_K5_PROMPT.md).

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
| [research/11-adjacent-categories-summary.md](research/11-adjacent-categories-summary.md) | v2 feature ideas — 10 new feature specs driven by owner-pains + AI/ML + adjacent OSS research |
| [research/12-ai-ml-summary.md](research/12-ai-ml-summary.md) | AI/ML extensions — menu engineering, waste prediction, recipe generation, sentiment analysis |

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

**v2 features (research complete, awaiting build decision):**

| # | Feature | File | Priority | Notes |
|---|---|---|---|---|
| 09 | Kitchen delay visibility | [features/09-kitchen-delay-visibility.md](features/09-kitchen-delay-visibility.md) | 🟢 | **Top v2 pick** — uses existing timestamps, no new deps |
| 10 | Allergen & dietary tracking | [features/10-allergen-tracking.md](features/10-allergen-tracking.md) | 🟢 | EUFIC 14-allergen standard |
| 11 | QR customer menu | [features/11-customer-qr-menu.md](features/11-customer-qr-menu.md) | 🟢 | Live stock display = differentiator |
| 12 | Pre-shift briefing | [features/12-pre-shift-briefing.md](features/12-pre-shift-briefing.md) | ⚪ | Cheapest feature in backlog (1–3 days) |
| 13 | Reservations & deposits | [features/13-reservations-deposits.md](features/13-reservations-deposits.md) | ⚪ | First feature touching real money (Stripe) |
| 14 | Split bills | [features/14-split-bills.md](features/14-split-bills.md) | 🟢 | #2 most-requested owner feature |
| 15 | Inventory variance | [features/15-inventory-variance.md](features/15-inventory-variance.md) | ⚪ | Builds on feature 03 ledger; data-discipline heavy |
| 16 | Supplier orders & receiving | [features/16-supplier-orders.md](features/16-supplier-orders.md) | ⚪ | Closes the inventory loop |
| 17 | ML demand forecasting | [features/17-demand-forecasting-ml.md](features/17-demand-forecasting-ml.md) | ⚪ | Prophet / NeuralForecast — needs 4+ weeks history |
| 18 | Gift cards & store credit | [features/18-gift-cards.md](features/18-gift-cards.md) | ⚪ | Append-only ledger pattern |

**v2 AI/ML features (research complete):**

| # | Feature | File | Priority | Notes |
|---|---|---|---|---|
| 19 | Menu engineering (Kasavana-Smith) | [features/19-menu-engineering.md](features/19-menu-engineering.md) | 🟡 | **Top AI/ML pick** — 2-3 days, pure SQL |
| 20 | Waste prediction | [features/20-waste-prediction.md](features/20-waste-prediction.md) | 🟡 | Uses prepared-item ledger; 5-10% food cost reduction |
| 21 | Recipe generation from leftovers | [features/21-recipe-generation.md](features/21-recipe-generation.md) | 🟡 | Local Qwen2.5-3B; "wow" demo |
| 22 | Sentiment analysis of reviews | [features/22-sentiment-analysis.md](features/22-sentiment-analysis.md) | ⚪ | "Weekend polish" — defer |

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

**v2 build order (after v1 ships):**

1. **Kitchen delay visibility** (09) — 5 days, no new deps. Uses existing timestamps.
2. **Pre-shift briefing** (12) — 2 days, Telegram-native. Cheapest win.
3. **Split bills** (14) — 5 days for ledger + UI; defer terminal integration.
4. **Allergen tracking** (10) — 4 days; needed before customer-facing menu.
5. **QR customer menu** (11) — 5 days; builds on allergen + stock display.
6. **Reservations** (13) — 7 days; first feature touching real money (Stripe).
7. **ML forecasting** (17) — 2 days to integrate Prophet; needs 4+ weeks of data first.
8. **Inventory variance** (15) + **Supplier orders** (16) — build together, ~3 weeks.
9. **Gift cards** (18) — 1 week. Append-only ledger pattern.

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
- `docs/HANDOFF.md` — repo tour + build order + constraints (read this if picking up).
- `docs/KIMI_K5_PROMPT.md` — ready-to-paste prompt for the next coding agent.
- `docs/PROJECT_CHARTER.md` — full project brief (scope, goals, deliverables, quality bar, risks). Read first.
- `index.html` (root) — the working mock-up (4 views, mobile-responsive, no build).
- `backend/` — FastAPI app skeleton (see `backend/README.md`).