# HANDOFF — Feature 303: `Bastardki11er-tally-mit-double-entry-ledger-postgresql-as-arbiter-append-only-idempotency-reconciliation-fastapi-postgres-hypothesis-v1-double-entry-ledger-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/303-Bastardki11er-tally-mit-double-entry-ledger-postgresql-as-arbiter-append-only-idempotency-reconciliation-fastapi-postgres-hypothesis-v1-double-entry-ledger-vocabulary.md` — defer/parking-lot (Pick B of Daily Research 2026-10-11).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 ledger surface proposes a *PostgreSQL-itself-guarantees-the-books-balance + deferred-constraint-triggers + append-only-history + idempotency + holds + reversals + reconciliation + Hypothesis-property-tests* primitive, the owner wants *evidence that this double-entry-ledger-vocabulary exists in 2026 with a PostgreSQL-as-arbiter + property-based-tests discipline*, but struggles because *LE31 has no documented v1 double-entry-ledger-vocabulary reference*, so that *the v1 ledger surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31 + the PostgreSQL-itself-as-arbiter pattern + the Hypothesis-property-tests discipline"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (PostgreSQL-itself-as-arbiter + deferred-constraint-triggers + double-entry + append-only + idempotency + holds + reversals + reconciliation) without specialist help. The 0★/0⑂ with TODAY PUSH (single-maintainer cadence; freshly-published) makes code adoption risky, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: **FastAPI + Postgres + Python on-stack** (LE31 stack match). The **Hypothesis** primitive is the §3.2 *property-based-testing* discipline applied to ledger-write correctness. Required data + permissions + infrastructure: Python FastAPI runtime + Postgres + property-based-testing framework. No AI capability required. Rabbit hole: the deferred-constraint-trigger pattern is a Postgres-specific feature that requires Alembic migration to set up the trigger. Evidence strength: high for vocabulary + stack-match + active-maintenance-signal (TODAY PUSH); medium for code adoption (freshly-published). |
| 4 | Conflict | ✓ | Does not violate any invariant. The *append-only-history* primitive is §3.1-aligned (current stock is derived from entries; ledger entries are never updated or deleted). The *PostgreSQL-itself-as-arbiter* primitive is the §3.1 explicit-state-transitions primitive applied to ledger writes with PostgreSQL-itself as the arbiter. No §3.4 customer-facing AI (the ledger is operator-tooling). No data rule violation. The *Hypothesis property tests* discipline is the §3.2 *property-based-testing* charter principle applied to ledger-write correctness. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 outcome (PostgreSQL-itself-as-arbiter double-entry-ledger for cash-till / payment-tip / expense). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry`) already implement the *append-only* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is freshly-published with single-maintainer cadence (0★/0⑂ + TODAY PUSH) and the PostgreSQL-itself-as-arbiter pattern is a future v1 polish surface, not a v1 charter surface.

## Bucket

**v1** (double-entry-ledger-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description names the 10-primitive decuple set (`PostgreSQL-as-arbiter + deferred-constraint-triggers + append-only-history + idempotency + holds + reversals + reconciliation + FastAPI + Postgres + Hypothesis`) + the FastAPI + Postgres + Python + Hypothesis stack.

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds a cash-till-ledger or payment-tip-reconciliation-ledger with PostgreSQL-itself-as-arbiter semantics):

1. `backend/app/ledger/models.py` — add new `LedgerEntry` SQLModel table with columns: `id` (UUID), `account_id` (str FK), `debit` (Decimal with EUR-cents precision per §3.6), `credit` (Decimal with EUR-cents precision per §3.6), `memo` (str), `idempotency_key` (str UNIQUE), `hold_id` (UUID FK nullable), `reversal_of_id` (UUID FK nullable), `decided_at` (timezone-aware datetime per §3.5).
2. `backend/app/ledger/models.py` — add new `Hold` SQLModel table with columns: `id` (UUID), `amount` (Decimal with EUR-cents precision per §3.6), `released_at` (timezone-aware datetime nullable), `released_to_ledger_entry_id` (UUID FK nullable).
3. `backend/app/ledger/models.py` — add new `Reconciliation` SQLModel table with columns: `id` (UUID), `reconciled_at` (timezone-aware datetime), `balanced` (bool), `discrepancy` (Decimal with EUR-cents precision per §3.6).
4. `backend/alembic/versions/` — add Alembic migration for the new tables + the deferred constraint trigger (CREATE CONSTRAINT TRIGGER ... DEFERRABLE INITIALLY DEFERRED).
5. `backend/app/ledger/repository.py` — add an idempotent-write helper that uses the `idempotency_key` UNIQUE constraint to dedupe writes.
6. `backend/app/ledger/holds.py` — NEW: hold placement + release helpers.
7. `backend/app/ledger/reversals.py` — NEW: reversal helpers that create a new ledger entry instead of updating the original.
8. `backend/app/ledger/reconciliation.py` — NEW: reconciliation helper that verifies `SUM(debit) == SUM(credit)` per `account_id` at a given timestamp.
9. `backend/app/api/v1/ledger/entries.py` — NEW: `GET /v1/ledger/entries?account=<>&as_of=<>&hold=<>` search endpoint.
10. `backend/app/api/v1/ledger/verify.py` — NEW: `GET /v1/ledger/verify?account=<>&as_of=<>` reconciliation endpoint.
11. `backend/app/api/v1/ledger/holds.py` — NEW: `POST /v1/ledger/holds` and `POST /v1/ledger/holds/<hold_id>/release` endpoints.
12. `backend/app/api/v1/ledger/reverse.py` — NEW: `POST /v1/ledger/entries/<entry_id>/reverse` endpoint.
13. `backend/tests/property/test_ledger.py` — NEW: Hypothesis property tests that verify the books-always-balance property after any sequence of writes.

## Verification protocol

1. `git clone https://github.com/Bastardki11er/tally` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/Bastardki11er/tally/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set).
3. `curl -sS -H "Authorization: Bearer ***" "https://api.github.com/repos/Bastardki11er/tally"` for star count, fork count, license, language, pushed_at, created_at, topics, description (parent-verified 2026-10-11).
4. Per `le31-conventions/SKILL.md`: load `le31-conventions`, `le31-research`, `le31-v1-feature-pattern`, `le31-handoff-spec` before any implementation.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v1 trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop the new tables + remove the deferred constraint trigger + remove the new API endpoints.
- No data loss if the rollback happens BEFORE any ledger row is written.
- Full data retention if the rollback happens AFTER rows are written (the new tables are dropped but the original `audit_logs` rows are preserved per the *append-only* invariant).

## Mandatory LE31 skill list

Before any implementation, the coding agent must load:
1. `le31-conventions` — the global LE31 decision layer (charter invariants + feature gate).
2. `le31-research` — the research workflow.
3. `le31-v1-feature-pattern` — v1 feature-pattern enforcement (append-only StockEntry, etc.).
4. `le31-handoff-spec` — the handoff-spec requirements (frozen contract discipline, mandatory skill list, verification protocol).
5. `le31-feature-pipeline` — the feature-pipeline workflow (parent research issue, sub-issue creation, handoff file).

## Linear sub-issue reference

Sub-issue draft (deferred pending Linear MCP write endpoint recovery): `Research 2026-10-11 / Pick B — v1 double-entry-ledger-vocabulary (Bastardki11er/tally)`. Parent fallback JSON captures the intended sub-issue at `/opt/data/le31-daily-research-2026-10-11.linear-fallback.json`. Sub-issue project = `le31 Research` (P-HMM-1) per `le31-feature-pipeline/SKILL.md` line 33 since `le31 v2-AI` does not exist.

## Parent research issue

[linear: blocked — workspace plan-limit error 21st consecutive day; parent fallback at `/opt/data/le31-daily-research-2026-10-11.linear-fallback.json`]