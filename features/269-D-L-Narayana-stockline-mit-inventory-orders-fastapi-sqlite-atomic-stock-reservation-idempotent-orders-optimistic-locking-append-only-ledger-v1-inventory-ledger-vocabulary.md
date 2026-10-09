# Feature 269 — `D-L-Narayana-stockline-mit-inventory-orders-fastapi-sqlite-atomic-stock-reservation-idempotent-orders-optimistic-locking-append-only-ledger-v1-inventory-ledger-vocabulary` (defer)

> **NEW observation (2026-10-09).** Documents in-window GitHub repo `D-L-Narayana/stockline` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Python, **pushed 2026-10-06T00:53:52Z**, in-window by `pushed_at` only, **created 2026-09-29T22:07:35Z** — 8-day-old repo with first in-window push, **294 KB modest repo**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-09): *"Multi-store inventory & order REST API — Python/FastAPI/SQLite. Atomic stock reservation, idempotent orders, optimistic locking, append-only ledger. Live in-browser demo."* Topics (verbatim, parent-verified): `concurrency, fastapi, inventory-management, pyodide, python, rest-api, retail, sqlite` — 8 topics including `fastapi` (LE31 stack match) + `inventory-management` (LE31 domain match) + `concurrency` (atomic stock reservation + idempotent orders + optimistic locking) + `pyodide` (in-browser demo = unexpected). Bucket: **v1 (inventory-ledger-vocabulary)** — Pick A of Daily Research 2026-10-09. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`multi-store + atomic stock reservation + idempotent orders + optimistic locking + append-only ledger`** quintuple-primitive as a persistent cross-section reference for the LE31 v1 *inventory-domain + atomic-StockEntry + idempotent-order + append-only-ledger* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (8-day-old repo with first in-window push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`multi-store + atomic stock reservation + idempotent orders + optimistic locking + append-only ledger`** quintuple-primitive: every inventory movement is an atomic, idempotent state transition; the current stock is derived from the append-only ledger; concurrent access is resolved by optimistic locking. This is the §3.1 explicit-state-transitions primitive applied to inventory with concurrency-safe write semantics.
- A written record of the **`FastAPI + SQLite + Python`** stack-shape: this is **3 of 4 LE31 backend stack primitives** matched (FastAPI + Python + SQLite is a transitive subset of Postgres); the *Pyodide in-browser demo* is OFF v1 charter (LE31 has no in-browser surface).
- A written record of the **`multi-store inventory + order REST API`** operator-surface-shape: every order is an idempotent operation; current inventory is derived from the ledger. Sister-shape to feature 12 (`stock-consistency`) + feature 14 (`prep-table-from-stockentry`) + feature 15 (`inventory-variance`) + feature 26 (`reorder-point-on-stockentry`).
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (8-day-old, first in-window push today); (2) the stack-shape match is the value, not the code (LE31 v1 uses HTMX + aiogram, not FastAPI + SQLite + Pyodide); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the stockline codebase (8-day-old single-maintainer repo with no observed production usage).
- Cross-pollination with `multi-store` (LE31 v1 charter is single-restaurant; v2 surface).
- Cross-pollination with the `Pyodide in-browser demo` (LE31 has no in-browser surface).

## Evidence / JTBD

When a future LE31 v1 surface proposes "the multi-store + atomic stock reservation + idempotent orders + optimistic locking + append-only ledger primitive" (e.g., a v1 polish that adds concurrent waiter-write protection on the `StockEntry` table, or a v2 surface that adds multi-tenant inventory), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "multi-store + atomic stock reservation + idempotent orders + optimistic locking + append-only ledger" is a real demand signal*, so that *the v1/v2 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31"*.

- **Evidence class**: observed (the stockline description + topics name the primitives explicitly: `concurrency, fastapi, inventory-management, pyodide, python, rest-api, retail, sqlite`).
- **Confidence**: medium-high for the vocabulary match (the verbatim description names the 5-primitive set + the tech-stack); low for transferability (LE31 v1 has aiogram + HTMX + Postgres; stockline has Pyodide + SQLite + REST; the operator-vocabulary is the value, not the code).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has minimal-HTML/HTMX + aiogram + single-restaurant single-tenant); the value is the *concurrent-write-protective inventory vocabulary* — when the first v1 PR that adds concurrent waiter-write protection on the `StockEntry` table lands, the stockline pattern is a ready-made *named primitive*.

## Description

GitHub `D-L-Narayana/stockline` (MIT, 0★/0⑂, Python, FastAPI + SQLite + Pyodide, pushed 2026-10-06T00:53:52Z, created 2026-09-29T22:07:35Z, 294 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-09): *"Multi-store inventory & order REST API — Python/FastAPI/SQLite. Atomic stock reservation, idempotent orders, optimistic locking, append-only ledger. Live in-browser demo."*

The architectural primitive has five sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **`Multi-store`** — every store has its own inventory partition; cross-store stock transfers are explicit ledger entries. The *multi-store* primitive is OFF v1 charter (LE31 is one restaurant) but the *primitive vocabulary* (partition + explicit ledger entry) is portable to any future v2 multi-tenant surface.
2. **`Atomic stock reservation`** — every order reserves stock atomically (the reserve is either committed or rolled back as a single transaction). The *atomic reservation* primitive maps 1:1 onto LE31's `StockEntry` schema (which already implements atomic ledger-entry insertion).
3. **`Idempotent orders`** — every order can be retried safely; an idempotency key prevents duplicate stock reservations. The *idempotency* primitive is OFF LE31 v1 today (the bot-driven workflow doesn't need retry protection) but applies to any future v1 polish that introduces a waiter-API retry layer.
4. **`Optimistic locking`** — concurrent writes are protected by an optimistic-locking version field on every stock row; the first writer wins, the second writer retries with the new version. The *optimistic-locking* primitive is OFF LE31 v1 today (LE31 v1 has no concurrent-writer surface on the `StockEntry` table) but applies to any future v1 polish that adds concurrent waiter-write protection.
5. **`Append-only ledger`** — current inventory is derived from the append-only ledger; the ledger is never updated or deleted, only appended. This is **§3.1 verbatim** — LE31 v1's `StockEntry` already implements this.

**The 1:1 mapping onto LE31 surface:**

| stockline primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Multi-store | (LE31 v1 is single-restaurant) | v2 (multi-tenant) | **Not implemented** — v2 surface |
| Atomic stock reservation | `StockEntry` (append-only atomic) | §3.1 ✓ | **Implemented (v1)** |
| Idempotent orders | (LE31 v1 has no waiter-API retry layer) | v1 polish | **Not implemented** — v1 polish surface |
| Optimistic locking | (LE31 v1 has no concurrent-writer surface) | v1 polish | **Not implemented** — v1 polish surface |
| Append-only ledger | `StockEntry` (append-only) | §3.1 ✓ | **Implemented (v1)** |
| FastAPI + SQLite | FastAPI + SQLModel + Postgres | §3.1 ✓ | **Implemented (v1)** |
| REST API | HTTP endpoints | §3.1 ✓ | **Implemented (v1)** |
| Pyodide in-browser demo | (LE31 has no in-browser surface) | not in v1 | **Not implemented** — different medium |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds concurrent waiter-write protection on the `StockEntry` table, or first v2 PR that introduces multi-store inventory), the implementation would add:

1. An `idempotency_key` column on the `Order` table (Alembic migration).
2. A `version` column on the `StockEntry` table (for optimistic locking).
3. An `INSERT ... ON CONFLICT DO NOTHING` guard on the StockEntry insert path.
4. A retry wrapper on the waiter-side HTTP middleware.

The HANDOFF is to evaluate whether the v1 concurrent-writer surface is the right product-wedge for the next v1 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1/v2 trigger fires:

**For v1 concurrent waiter-write protection** (if approved):
1. Add a `version` column to the `StockEntry` table (Alembic migration).
2. Add an `INSERT ... ON CONFLICT DO NOTHING` guard on the StockEntry insert path.
3. Wrap the waiter-API endpoints in an idempotency-key middleware (read the `Idempotency-Key` header, store in a separate `IdempotencyKey` table with a TTL).
4. Update the cook Telegram bot's message handler to handle the `ConflictOnStockEntry` exception gracefully (the bot retries once with the new version).
5. No new feature file needed; this is an incremental enhancement to the existing append-only `StockEntry` schema.

**For v2 multi-store inventory** (if approved):
1. Add a `tenant_id` column to the `StockEntry` table (Alembic migration).
2. Add a `tenant-aware repository` pattern at `app/stock/tenant_repo.py` that filters by `tenant_id` on every query.
3. Add a `cross-tenant stock transfer` explicit ledger entry at `app/stock/transfer.py`.
4. New feature file at `features/NNN-multi-store-tenant-aware-inventory.md` (NOT this defer artifact).

## Telegram interaction

- **Cook bot**: if a `ConflictOnStockEntry` exception is raised (optimistic-lock conflict), the bot retries once with the new version; if the retry fails, the bot surfaces the error to the cook with a friendly message ("Stock level changed; please re-confirm the order").
- **Waiter web**: the waiter-API retries transparently; the HTML surfaces a non-blocking toast if the retry succeeds ("Updated").
- **Owner**: no direct Telegram interaction; the owner-side daily recap is unchanged.

## Dependencies

- LE31 v1 stack primitives (`StockEntry` schema + `audit_logs` + alembic) — all on the LE31 pin set.
- Database: SQLite (transitive) or Postgres (production). The *optimistic-locking* primitive requires a SQL `UPDATE ... WHERE version = X` semantics; both SQLite and Postgres support this.
- No new external dependency.

## Open questions

1. **Is the v1 concurrent waiter-write surface the right product-wedge today?** LE31 v1 today is single-writer single-restaurant; the surface would add complexity for a non-observed pain.
2. **Is the v2 multi-store inventory surface the right product-wedge today?** LE31 charter is single-restaurant; v2 surface would expand scope; recommend charter-decided before any v2 PR.

## Why this matters

The stockline repo is the strongest direct LE31-stack-shape match for the **`multi-store + atomic + idempotent + optimistic-locking + append-only ledger`** quintuple-primitive in the 71-pass series. The *vocabulary* is the value: when LE31 v1 polish adds concurrent waiter-write protection, the stockline pattern is a ready-made *named primitive*. When LE31 v2 multi-store inventory lands, the stockline pattern is a ready-made *architecture reference*. The 8-day-old repo with first in-window push is the demand-signal, not the adoption-signal.
