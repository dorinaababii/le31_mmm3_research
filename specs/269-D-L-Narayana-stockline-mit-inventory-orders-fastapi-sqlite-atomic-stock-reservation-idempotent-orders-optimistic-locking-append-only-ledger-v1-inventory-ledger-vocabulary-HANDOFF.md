# HANDOFF — Feature 269: `D-L-Narayana-stockline-...-v1-inventory-ledger-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/269-D-L-Narayana-stockline-mit-inventory-orders-fastapi-sqlite-atomic-stock-reservation-idempotent-orders-optimistic-locking-append-only-ledger-v1-inventory-ledger-vocabulary.md` — defer/parking-lot (Pick A of Daily Research 2026-10-09).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes a `multi-store + atomic stock reservation + idempotent orders + optimistic locking + append-only ledger` primitive, the owner wants *evidence that this stack-shape exists in 2026*, but struggles because *LE31 has no documented in-window inventory-ledger-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (atomic stock reservation + idempotent orders + optimistic locking + append-only ledger) without specialist help. The 8-day-old single-maintainer repo makes code adoption not viable, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: FastAPI + Python + SQLite (transitive subset of Postgres). Required data + permissions + infrastructure: Python FastAPI runtime + SQLite/Postgres DB. No AI capability required. Rabbit hole: the Pyodide in-browser demo (LE31 does not have an in-browser surface). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *append-only ledger* is §3.1-aligned. The *idempotent orders* + *optimistic locking* primitives are §3.1-aligned. The `multi-store` vocabulary is off LE31 v1 charter (one restaurant). No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 outcome (operator-side inventory primitive). Maximum time worth spending: 1 hour documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | ~30 min documentation; the LE31 v1 surfaces (StockEntry / reorder-point / shelf-threshold) already implement the discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + 8-day-old repo + Pyodide/SQLite/REST stack mismatch with LE31 aiogram/HTMX/Postgres/StockEntry).

## Bucket

**v1** (inventory-ledger-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description names the 5-primitive set + the tech-stack.

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds concurrent waiter-write protection on the `StockEntry` table):

1. `backend/app/stock/models.py` — add `version: int = 0` column on `StockEntry` (Alembic migration).
2. `backend/alembic/versions/` — add a new Alembic migration: `ALTER TABLE stock_entry ADD COLUMN version INTEGER NOT NULL DEFAULT 0`.
3. `backend/app/stock/repository.py` — add an `INSERT ... ON CONFLICT DO NOTHING` guard on the StockEntry insert path.
4. `backend/app/middleware/idempotency.py` — add an idempotency-key middleware that reads the `Idempotency-Key` header and stores in a new `IdempotencyKey` table with a TTL.
5. `backend/app/bot/cook_dispatcher.py` — handle the new `ConflictOnStockEntry` exception by retrying once with the new version.

**For v2 multi-store inventory** (if approved, NOT this defer):

1. `backend/app/stock/models.py` — add `tenant_id: UUID` column on `StockEntry` (Alembic migration).
2. `backend/app/stock/tenant_repo.py` — NEW: tenant-aware repository pattern that filters by `tenant_id` on every query.
3. `backend/app/stock/transfer.py` — NEW: cross-tenant stock transfer explicit ledger entry.
4. New feature file at `features/NNN-multi-store-tenant-aware-inventory.md` (NOT this defer artifact).

## Verification protocol

1. `git clone https://github.com/D-L-Narayana/stockline` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/D-L-Narayana/stockline/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set).
3. `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN" "https://api.github.com/repos/D-L-Narayana/stockline"` for star count, fork count, license, language, pushed_at, created_at, topics (parent-verified 2026-10-09).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the optimistic-locking + idempotency changes are isolated to the expected files.
5. Per `le31-conventions/SKILL.md`: load `le31-conventions`, `le31-research`, `le31-v1-feature-pattern`, `le31-handoff-spec` before any implementation.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v1 trigger fires and the implementation lands:
- For v1 concurrent waiter-write protection: rollback = `alembic downgrade -1` to drop the `version` column + remove the idempotency middleware.
- For v2 multi-store inventory: rollback = `alembic downgrade -1` to drop the `tenant_id` column + delete `tenant_repo.py` + `transfer.py`.

## Mandatory LE31 skill list

Before any implementation, the coding agent must load:
1. `le31-conventions` — the global LE31 decision layer (charter invariants + feature gate).
2. `le31-research` — the research workflow.
3. `le31-v1-feature-pattern` — v1 feature-pattern enforcement (append-only StockEntry, etc.).
4. `le31-handoff-spec` — the handoff-spec requirements (frozen contract discipline, mandatory skill list, verification protocol).

## Linear sub-issue reference

Sub-issue draft (deferred pending Linear MCP write endpoint recovery): `Research 2026-10-09 / Pick A — v1 inventory-ledger-vocabulary (D-L-Narayana/stockline)`. Parent fallback JSON captures the intended sub-issue at `/opt/data/le31-daily-research-2026-10-09.linear-fallback.json`.
