# Feature 37 — Void Rationale Ledger Field

> **Priority**: P1 · **Effort**: XS (≤2 days) · **Source**: brainstorm 2026-08-06
> (cross-section pick A) · **Bucket**: v2 owner-pains
> **One-line**: Every negative `StockEntry` (void / 86 / substitution / comp /
> correction-downward) carries a required one-line `rationale` string set at
> insertion time; positive deltas keep the field optional. Owner can later
> `grep rationale` to answer "why did table 7 get a comp" without leaving the
> Telegram bot or web UI.

## Goal

Close the small-restaurant operator's #1 follow-up question after a comp, an
86, a substitution, or any other negative-delta event: *why did this happen?*
Currently `StockEntry.notes` is free-text optional and almost always empty, so
the `StockEntry` ledger is technically complete but practically unanswerable
on a per-row basis. A required one-line rationale on every negative delta
makes the ledger *self-explaining* — no new table, no new ledger, no new
infra, just a new column and a one-line bot prompt.

Inspired by today's brainstorm: GitHub `topic:append-only` repos
`mazze93/stratum` (pushed **today** 2026-08-06T06:48:55Z, "epistemic decision
ledger: append-only event log with evidence-gated trust") and
`S0tman/irp-capture` (pushed 2026-08-01, "An append-only ledger that records
why decisions were made"). Both come from outside hospitality — from
AI-trust / compliance engineering — and share the same primitive: an
append-only event log that records the rationale at insertion time, never
updated.

This is also the prerequisite for feature 39 (`owner-daily-recap-telegram`),
which reads `rationale` to summarise "voids with reasons" in the owner's
daily recap. Without this column, the recap is a count of voids; with it,
the recap is a list of *decisions*.

## Evidence / JTBD

When the owner reviews the books after a shift, the owner wants to know why
a comp or a substitution happened, but struggles because the `StockEntry`
ledger has no required rationale column and the cook types free-text "notes"
almost never, so that a required one-line "why" on every negative delta
makes "why did table 7 get a comp" answerable in one grep.

## Scope

**In scope (v2 owner-pains):**
- New nullable column `rationale: str` on the existing `StockEntry` SQLModel
  (max length 240 chars; trimmed at the model layer).
- A model-layer guard `assert_rationale_if_negative(stockentry: StockEntry)`
  called from every code path that writes a `StockEntry` with
  `qty_delta < 0`: refuses to insert if `rationale` is `None` or empty
  after trim.
- All existing negative-delta write paths audited and updated to pass a
  rationale:
  - Cook bot `/void <item> <reason>` (new command, see below)
  - Cook bot `/86 <item> <reason>` (new command, see below)
  - Waiter web UI void button (new required `<input>` in the void modal,
    surfaced inline; no extra page)
  - Manager web UI comp / correction-downward actions (new required input)
- New cook-bot command `/void <item> <reason>` — writes one negative
  `StockEntry` with the supplied `<reason>` as `rationale`. Chat-id
  allowlisted same as feature 04.
- New cook-bot command `/86 <item> <reason>` — same shape; `<reason>` is
  short-form rationale (e.g. "out of stock" / "burned" / "allergy").
- A migration that adds the column as NULL-able, with backfill of existing
  negative-delta rows to a sentinel `rationale = "(legacy — no rationale
  recorded)"` so the guard can never silently violate on existing data.
- A new route `GET /api/stock/rationale_search?q=<term>` (manager-only) that
  returns the 50 most recent negative-delta `StockEntry` rows whose
  `rationale` matches `<term>` (case-insensitive substring match, indexed
  via Postgres trigram if installed, else falls back to ILIKE — recorded
  in Open Questions).
- The new column is set at insertion time only; never updated (enforced by
  a SQLAlchemy event listener that raises on `UPDATE` of any `StockEntry`
  row, mirroring the existing append-only invariant; same listener as
  feature 30's audit chain).

**Out of scope (v2 owner-pains):**
- Required rationale on positive deltas (cook, receive, correction-upward) —
  optional only; positive deltas are usually self-evident (cooked X kg of
  flour).
- Free-form rationale longer than 240 chars — 240 is enough for "we got a
  comp because the customer said the lamb was cold" and prevents the cook
  from writing essays.
- Rationale on non-stock events (visit, order, bill, payment) — feature 30
  territory (audit chain), not rationale.
- Multi-language rationale translation — single-language input only.
- Editing rationale after the fact — explicitly forbidden by the append-only
  invariant. If the cook got the reason wrong, they write a new
  `StockEntry` with a positive delta (correction-upward) and a new rationale
  pointing at the original (e.g. "correction: previous void was actually
  served; see entry #1234").

## User flow

**Cook — 86 mid-service:**
1. Cook sends `/86 lamb burned the second batch` to the existing cook bot.
2. Bot parses `<item>=lamb`, `<reason>=burned the second batch`.
3. Bot writes one `StockEntry` row with `qty_delta = -1` (or the item's
   current batch quantity), `reason = "86"`, `rationale = "burned the
   second batch"`, `source = "telegram:cook"`.
4. Bot replies with one line: "86 lamb written. Rationale: burned the
   second batch. (StockEntry #1234)". Bot also pushes the event to the
   existing `CookChannel` SSE stream (no new event type needed — the
   existing `stock_change` event now carries the rationale field).

**Waiter — comp from the web UI:**
1. Waiter clicks "Void" on a paid order line.
3. Modal opens with a single required `<input>` "Why?" — placeholder
   "guest comp — birthday" / "kitchen error — undercooked" / "wrong
   table — duplicate order".
4. Waiter types "guest comp — birthday" and clicks "Confirm void".
5. Frontend POSTs to the existing `/api/orders/{id}/void` with the
   rationale in the body. Backend writes the corresponding negative
   `StockEntry` with `rationale` populated.

**Owner — answering "why did table 7 get a comp?" 24 hours later:**
1. Owner opens the manager dashboard → Stock → Search.
2. Types "table 7" in the search box.
3. Hits "Search rationale". The new endpoint
   `GET /api/stock/rationale_search?q=table%207` returns the matching
   `StockEntry` rows with their rationale text in context.

## Data model

The existing `StockEntry` table gets one new nullable column:

```python
# backend/app/models.py (additive patch to existing SQLModel)

class StockEntry(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    menu_item_id: int = Field(foreign_key="menu_item.id", index=True)
    qty_delta: Decimal = Field(...)              # existing
    reason: str = Field(max_length=40, index=True)  # existing — e.g. "void", "86", "cook", "receive"
    source: str = Field(max_length=40)               # existing — e.g. "telegram:cook", "web:waiter"
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    rationale: str | None = Field(default=None, max_length=240, index=True)  # NEW
```

Constraints:
- `rationale` is NULL-able in the DB so the backfill migration can set the
  sentinel value on existing rows.
- A model-layer check `assert_rationale_if_negative()` is called from every
  write path before the session is flushed. Failure raises
  `RationaleRequiredError` (HTTP 400 / bot reply "rationale required for
  negative delta").
- The existing append-only event listener (from feature 03) is extended to
  forbid any UPDATE of any `StockEntry` row, including its `rationale`
  column.

## API / bot / UI contract

**Bot (aiogram v3, existing webhook from feature 04):**
- New command: `/void <item> <reason...>` — bot handler in
  `backend/app/bot/cook_bot_void.py`. Argument parsing matches existing
  bot style (`/86` style).
- New command: `/86 <item> <reason...>` — same shape, different `reason`
  field on the `StockEntry` (`reason = "86"` vs `reason = "void"`).
- Both commands require chat-id in the existing
  `TELEGRAM_ALLOWED_USERS` allowlist (no change).

**API (FastAPI):**
- New route: `GET /api/stock/rationale_search?q=<term>&limit=50` in a new
  router `backend/app/routers/stock_rationale.py`. Manager-only
  (reuses the existing manager-cookie guard from feature 29).
- Existing routes unchanged. Existing `/api/orders/{id}/void` route gets
  one new required body field `rationale: str` (returns 400 if missing on
  a void that creates a negative `StockEntry`).

**UI (existing waiter web UI from feature 02):**
- Existing void modal gets one new required `<input>` at the top, label
  "Why?", placeholder examples. No layout change otherwise.

**SSE (existing `CookChannel` from feature 23):**
- The existing `stock_change` event payload gains one new optional field
  `rationale: str | None`. Clients that ignore unknown fields keep
  working; clients that display it (the prep board from feature 34, the
  no-account link from feature 29) can choose to render it.

## Dependencies

- **No new pip dependencies.**
- Reuses the existing `StockEntry` model, the existing append-only event
  listener (feature 03 / 30), the existing `CookChannel` SSE (feature 23),
  the existing cook-bot webhook (feature 04), the existing manager-cookie
  guard (feature 29), the existing `/api/orders/{id}/void` route.
- **Required upstream feature**: none. This feature is independent.
- **Required downstream feature**: feature 39 (`owner-daily-recap-telegram`)
  reads `rationale` to summarise voids in the recap.

## Failure / recovery

- **Cook forgets to add rationale**: the model-layer guard raises; the bot
  replies "rationale required for negative delta — try again with a
  reason" (same shape as the existing `/86` reply when the item is
  unknown). No silent write, no zero-quantity placeholder.
- **Database migration fails**: the backfill sentinel is a single
  transactional UPDATE; failure rolls back the migration. CI / pre-deploy
  must include the migration in the deploy script.
- **Postgres trigram extension unavailable**: the `rationale_search`
  endpoint falls back to `ILIKE %term%` (full-table scan on negative
  rows only, <10k rows in a 1-restaurant pilot, <100ms). Documented in
  Open Questions.
- **Reasonable rationales become too long**: hard-cap at 240 chars in the
  model layer; the cook bot reply trims and warns if input > 240.

## Definition of done

- [ ] `rationale` column added to `StockEntry` model + Alembic migration
      shipped, backfilled with sentinel for existing negative rows.
- [ ] Model-layer guard `assert_rationale_if_negative()` called from every
      existing negative-delta write path; new unit tests for each path
      (cook bot /void, cook bot /86, waiter UI void modal, manager UI
      comp).
- [ ] Cook bot commands `/void` and `/86` shipped, with rationale argument
      parsing.
- [ ] Waiter UI void modal has the required `<input>`.
- [ ] Manager `/api/stock/rationale_search` route shipped.
- [ ] Append-only listener extended to forbid UPDATE of `StockEntry.rationale`.
- [ ] `CookChannel` SSE `stock_change` event payload includes the new
      optional `rationale` field.
- [ ] Existing tests still green.
- [ ] End-to-end observed: cook sends `/86 lamb burned` → row appears in
      DB with `qty_delta=-1` and `rationale="burned"` → owner searches
      "burned" 24 hours later and finds the row in ≤200 ms.
- [ ] Backwards-compatibility check: a `StockEntry` row written before
      this migration (with `rationale = "(legacy — no rationale recorded)"`)
      is silently treated as "no rationale on file" by the search endpoint.

## Open questions

- Should the `reason` field stay as a coarse enum (`void` / `86` / `cook` /
  `receive` / `comp` / `correction` / `substitution`) and `rationale` be the
  free-text one? Or should `reason` become fully free-text and `rationale`
  merge into it? Decision: keep both; `reason` is the cheap-to-filter
  category, `rationale` is the rich-to-search text. This matches the way
  the existing `OwnerAuditEvent.source_table` + `OwnerAuditEvent.payload_json`
  work in feature 30.
- Postgres trigram extension `pg_trgm` for sublinear `rationale` search?
  Decision deferred: ship with `ILIKE` for v1; trigram is a 5-line follow-up
  if/when the pilot restaurant has >50k negative rows (unlikely in year 1).

## Why this matters

LE31's killer pattern is the append-only `StockEntry` ledger for prepared
items — the in-window peer review confirms no competitor implements this
primitive. This feature adds the missing *why* dimension to that ledger. The
two real-world in-window peers (`mazze93/stratum`, `S0tman/irp-capture`)
both come from AI-trust / compliance engineering — completely outside
hospitality — and they share the same primitive: an append-only event log
that records the rationale at insertion time, never updated.

Translated to LE31, this is the missing one-line column that makes every
negative-delta follow-up question answerable in one grep, and it is the
prerequisite for feature 39's daily recap (without `rationale`, the recap
is just a count of voids; with `rationale`, the recap is a list of
*decisions*). Tiny cost (one column + one model-layer check + two bot
commands), high value (closes the most-cited operator follow-up question).