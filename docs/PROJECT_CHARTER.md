# Project Charter — Restaurant App

> **Document type**: project brief / scope-of-work for the implementation agent
> **Audience**: the coding agent (Kimi K5) that will implement the system
> **Predecessor**: Hermes (MiniMax-M3) ran the research + scaffolded the skeleton
> **Date**: 2026-07-24
> **Repository**: https://github.com/dorinaababii/le31_mmm3_research

---

## 1. Executive summary

We are building a **two-role restaurant operations system** for a single small
restaurant (≤40 seats). The product is split cleanly between two user surfaces:

1. **Dining / Service** — waiters use a web UI to seat parties, take orders,
   and close bills at the table.
2. **Kitchen** — the cook uses a **Telegram bot** to set up the daily menu
   (by uploading a single photo), track stock of prepared items, and get
   end-of-day summaries.

Plus a manager view for reports and demand forecasting.

The killer feature — and the reason we are building this rather than forking an
existing POS — is **first-class finite stock of prepared/cooked items**.
When the cook writes "today I baked 8 pieces of cake" in the morning, the system
keeps an append-only ledger; each slice sold during service decrements the
stock; when it hits zero, the item auto-hides from the waiters' UI and the cook
gets a Telegram alert.

The research phase concluded: **no open-source restaurant system implements
this as a first-class concept.** Most can do it indirectly via ERPNext's Batch
module (heavyweight) or manual workarounds. We will do it in ~150 lines of
Python + 4 SQL tables.

## 2. Project goals

In priority order (P0 = must ship, P1 = strongly desired, P2 = nice-to-have):

| Priority | Goal | Acceptance criteria |
|---|---|---|
| **P0** | Waiter can seat a party at any free table and capture `party_size`, `adults`, `children`. | `POST /api/tables/{id}/seat` works; UI shows table card turning yellow. |
| **P0** | Waiter can browse today's menu and add items to the active visit. | `POST /api/visits/{id}/items` works; menu hides sold-out items. |
| **P0** | Cook can upload a menu photo via Telegram, confirm parsed items, set per-item prep quantities, and the system creates batches. | `/start_today` flow completes end-to-end; batches visible in DB. |
| **P0** | Selling a prepared item decrements its active batch's `qty_remaining` and writes a `StockEntry(-1, reason='sale')` row. | Manual test: order a tiramisu → stock goes 8 → 7 → ledger has one entry. |
| **P0** | Cook can mark an item sold-out via `/sold_out`; menu auto-hides it. | After `/sold_out tiramisu`, the waiter's UI no longer shows it. |
| **P0** | Waiter can close a bill; tip is **derived** as `total_paid − subtotal_items − subtotal_tax`. | `tip` field appears on `DerivedTip` row; never manually entered. |
| **P1** | Manager dashboard shows covers today, sales, tips, avg dwell, top items. | `/api/reports/today` returns KPIs + top-items list. |
| **P1** | End-of-shift cash reconciliation computes expected vs counted cash and stores variance. | `POST /api/shifts/{id}/close` returns variance; `Shift` row updated. |
| **P1** | Cook gets a daily `/forecast` with prep quantities suggested from the last 14 days. | Forecast rounds `avg_14d × 1.1` per item, message sent to cook. |
| **P2** | Cook can manually record leftovers at end of day (`/leftover <item> <qty>`). | Stock entry written with `reason='waste'`; EOD summary reflects. |
| **P2** | Manager can export daily report as CSV. | `GET /api/reports/today.csv` returns text/csv. |

## 3. Scope

### 3.1 In scope (v1)

- **One restaurant, one location.** No multi-tenancy.
- **One Telegram bot, role-based via chat_id allowlist** (cook + manager).
- **Single-currency**, single-language menus (language TBD by user).
- **Flat tax** (single rate, e.g. 10%).
- **Prepared-item stock** with per-batch quantities and an append-only ledger.
- **Tip derived from total_paid − items_consumed − tax**. No manual tip entry.
- **Guest demographics**: `party_size`, `adults`, `children`. **No gender, no name, no phone.**
- **Mobile-responsive web UI** for waiters (works on a phone or tablet).
- **SQLite for dev**, Postgres for prod. Same SQLModel code for both.
- **One-click local dev setup** (pip install + uvicorn, no Docker required).

### 3.2 Out of scope (v1) — explicit non-goals

These were considered and **deliberately excluded** to keep v1 shippable:

- Multi-restaurant / multi-location.
- Online ordering, delivery, reservations.
- Payment gateway integration (Stripe, SumUp, etc.). We record `method = cash | card` only.
- Per-item modifier UIs (size, extras, add-ons). Menu is flat.
- Loyalty / repeat-customer tracking.
- Customer-facing receipts or surveys.
- Customer-facing waitlist app.
- Tip pooling / distribution across staff.
- Discount / promo codes.
- Service charge (auto-added %).
- Capture of guest gender, age, or any PII beyond counts.
- Per-user PIN auth in v1 (we'll use a hardcoded `server_id = 1` in the tables router — wire proper auth later).
- Real-time WebSocket push (waiter UI polls; v2 can add WebSockets).
- Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod).
- Docker / Kubernetes (single VPS + systemd unit is fine for v1).
- Internationalization of the UI (English only).

### 3.3 Open scope questions (blockers for some features)

These are listed in `docs/INDEX.md`. Decisions needed before code starts:

1. **Menu language** — drives OCR engine (PaddleOCR for CJK, RapidOCR for EU).
2. **Currency** — EUR / USD / other? Affects display formatting.
3. **Tax** — flat 10%? Per-category? Per-item?
4. **Waiter hardware** — tablet, phone, or laptop? Drives UI density decisions.
5. **Service charge** — auto-add a percentage? (Common in EU, not US.)

Defaults if user doesn't answer: English menus, EUR, flat 10% tax, tablet UI, no service charge.

## 4. Architecture (decided by research, do not deviate)

### 4.1 Stack

| Layer | Choice | Reason |
|---|---|---|
| HTTP API | **FastAPI** | async, type-hinted, auto OpenAPI docs |
| ORM | **SQLModel** | Pydantic + SQLAlchemy in one — same class for DB row and API model |
| DB | **SQLite (dev)** / **Postgres (prod)** | SQLModel is dialect-agnostic; switch via `DATABASE_URL` |
| Telegram bot | **aiogram v3** | MIT license, FSM, clean async API |
| Menu OCR | **RapidOCR** (`rapidocr-onnxruntime`) | Multi-language, CPU-runnable, no GPU required |
| LLM post-processing | any OpenAI-compatible API (GPT-4o-mini / Gemini Flash / local Ollama) | Pluggable via `LLM_BASE_URL` |
| UI mock-up | **vanilla HTML + JS** | No build step; serves directly from FastAPI |
| Future UI | **TBD** (likely a SPA: React or Svelte) | Not in scope for v1 |

### 4.2 Schema overview

See [`docs/research/09-recommended-stack.md`](research/09-recommended-stack.md)
for the full DDL sketch. The SQLModel classes already exist in
[`backend/app/models.py`](../backend/app/models.py). Tables:

```
menu_item        — what can be sold
batch            — a concrete prepared quantity of a menu_item for a day
stock_entry      — append-only ledger; current stock = SUM(qty_delta) per batch
table_           — physical tables in the restaurant
app_user         — staff (server / cook / manager)
visit            — a party seated at a table
order_item       — a line on a visit
bill             — payment record for a visit
derived_tip      — tip = total_paid − (subtotal_items + subtotal_tax)
shift            — cash reconciliation
```

### 4.3 The killer pattern: append-only stock ledger

```
EVERY change to batch stock is a new StockEntry row. Never UPDATE or DELETE.

batch.qty_remaining = SUM(stock_entry.qty_delta WHERE batch_id = X)
                     ─────────────────────────────────────────────
                     computed on read, not stored.

Insert paths:
  • Morning prep       → qty_delta = +N, reason = 'initial'    (one row per batch)
  • Order item served  → qty_delta = -1, reason = 'sale'       (one row per unit sold)
  • /sold_out          → qty_delta = -(remaining), reason = 'sold_out'
  • /leftover N        → qty_delta = -N, reason = 'waste'
  • /restock N         → qty_delta = +N, reason = 'restock'

When SUM(qty_delta) ≤ 0 for an active batch:
  • Mark menu_item as sold_out (in-memory cache or a `sold_out_today` table)
  • Hide from waiter UI
  • Send Telegram alert to cook (one-shot, not on every order attempt)
```

### 4.4 Folder layout

```
le31_mmm3_research/
├── README.md                       ← project pitch
├── index.html                      ← ⭐ working mock-up (open in browser)
├── docs/
│   ├── INDEX.md                    ← master index
│   ├── HANDOFF.md                  ← technical tour for the implementer
│   ├── KIMI_K5_PROMPT.md           ← paste-in instructions for this agent
│   ├── PROJECT_CHARTER.md          ← ⭐ you are here
│   ├── research/                   ← 11 files — read for context, do not modify
│   └── features/                   ← 8 files — one per feature, contract for each
└── backend/                        ← ⭐ code lives here
    ├── README.md
    ├── requirements.txt
    ├── .env.example
    └── app/
        ├── main.py                 ← FastAPI entry, serves /index.html
        ├── config.py               ← Settings (pydantic-settings)
        ├── db.py                   ← Engine + session
        ├── models.py               ← SQLModel classes (table=True)
        ├── routers/                ← one .py per feature group
        │   └── tables.py           ← Feature 01 working
        ├── services/               ← business logic (forecast, OCR, etc.)
        └── bot/
            └── cook_bot.py         ← aiogram FSM stub (Feature 04 to wire)
```

## 5. Task breakdown & dependencies

Build in this order. Each step must be **end-to-end working** before moving on
(model → router → bot integration → manual verification → commit).

```
[✓ done]   F01 Table management    (basic — needs status column on Table)
[ ] P0     F02 Order taking        (routers/orders.py, touch OrderItem)
           ↓ needed for F03
[ ] P0     F03 Kitchen stock       (routers/stock.py + hook into order close)
           ↓
[ ] P0     F04 Menu photo OCR      (services/ocr.py + cook_bot.py wiring)
           ↓
[ ] P0     F05 Bill + derived tip  (routers/bills.py, DerivedTip model)
           ↓
[ ] P1     F06 Reports             (routers/reports.py, KPIs + top items)
           ↓
[ ] P1     F07 Demand forecast     (services/forecast.py, scheduled job)
           ↓
[ ] P2     EOD summary bot command (services/eod.py)
           ↓
[ ] P2     CSV export              (already half-done in feature 06)
```

Estimated effort: **6–10 working days** for a focused engineer.
Roughly 1 day per P0 feature, 0.5 day per P1, smaller for P2.

## 6. Deliverables

When you say "done", the repo must contain:

1. **All P0 features** implemented end-to-end (sections 5).
2. **All P1 features** working with at least manual test coverage.
3. **Updated `docs/INDEX.md`** with the checklist marked off.
4. **A short "what I built" note** committed at the end, describing:
   - which features shipped,
   - which open questions (section 3.3) you answered with what default,
   - any deviations from this charter and why.
5. **Working manual demo path**: a 5-step sequence (start app → seat party → order → close bill → cook confirms via bot) that the user can click through.

## 7. Quality bar

- **Money is `Decimal`, never `float`.** SQLModel fields with `max_digits=10, decimal_places=2`.
- **Time is UTC.** `datetime.now(timezone.utc)` everywhere.
- **Money sums use `Decimal` arithmetic.** No `float(qty * price)` anywhere.
- **No magic numbers.** Tax rate, tip rounding rules, buffer factors — all in `config.py` or `services/`.
- **Append-only ledger invariant.** Linter rule (or at minimum a code review checklist item) for `StockEntry` writes.
- **End-to-end before commit.** Don't commit a feature that "compiles but doesn't work in the UI".
- **No dead code.** If you write a helper and don't use it, delete it.
- **Tests are not required** for v1. Manual verification via curl + the mock-up is acceptable.

## 8. Verification protocol (use this for each feature)

```
1. Re-read the feature spec at docs/features/0X-*.md
2. Implement model (if new) in backend/app/models.py
3. Implement router in backend/app/routers/X.py
4. Wire bot handlers (if applicable) in backend/app/bot/cook_bot.py
5. cd backend && uvicorn app.main:app --reload
6. Open http://localhost:8000/docs — confirm endpoint appears
7. curl the endpoint with a realistic payload — confirm response shape
8. Open http://localhost:8000/ — confirm UI behavior (if any)
9. Inspect SQLite: sqlite3 backend/restaurant.db ".schema" + ".tables"
10. git add -p && git commit -m "Feature 0X: <short description>"
11. Tick the box in docs/INDEX.md
```

## 9. Communication & cadence

- **Push commits daily**, even partial ones. Each commit message should reference the feature ID.
- **Open a GitHub Issue** per blocker you can't solve in 30 min. Don't spin for hours.
- **If you must deviate** from this charter (different stack, added dependency, dropped feature), document it in the commit message and in the final "what I built" note.

## 10. Risks & mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| RapidOCR misreads menus in the user's language | medium | Fallback to manual item entry in the bot (always offer the "Add item manually" button). |
| aiogram v3 changes between docs and your version | low | Pin aiogram version in requirements.txt; document any API drift in commit messages. |
| SQLite + concurrent writes (kitchen + service both POST) | medium | SQLite handles it via file locks but is slow at scale. For dev this is fine; mention in README that prod should switch to Postgres. |
| Postgres-specific features creep into models | medium | Stick to SQLModel core types. Avoid `JSONB`, `ARRAY`, `UUID` columns — use `JSON` as TEXT, comma-separated strings, integers. |
| User has different open-question answers than defaults | low | If user replies with answers, apply them in a single "Apply user answers" commit before continuing. |

---

## 11. Sign-off

By starting work, you accept:

- The architecture in section 4 (FastAPI + SQLModel + aiogram + Postgres/SQLite).
- The killer pattern in section 4.3 (append-only stock ledger).
- The scope boundaries in section 3.2 (no multi-tenancy, no manual tip entry, etc.).
- The defaults in section 3.3 (English menus, EUR, flat 10% tax, tablet UI, no service charge) unless the user overrides.
- The quality bar in section 7.

If any of this is unclear, **ask before coding**. The doc tour in
`docs/HANDOFF.md` and the feature specs in `docs/features/` are the
authoritative contracts; this charter is the high-level framing.

Good luck. Ship the P0 list first.