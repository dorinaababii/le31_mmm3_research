# Feature 303 — `Bastardki11er-tally-mit-double-entry-ledger-postgresql-as-arbiter-append-only-idempotency-reconciliation-fastapi-postgres-hypothesis-v1-double-entry-ledger-vocabulary` (defer)

> **NEW observation (2026-10-11).** Documents in-window GitHub repo `Bastardki11er/tally` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Python + FastAPI + Postgres + Hypothesis, **pushed 2026-10-11T01:22:08Z = TODAY**, in-window by `pushed_at` only, **created 2026-09-XX**, **387 KB modest repo**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-11): *"Double-entry ledger API where PostgreSQL itself guarantees the books balance: deferred constraint triggers, append-only history, idempotency, holds, reversals, reconciliation. FastAPI + Postgres + Hypothesis."* Topics (verbatim, parent-verified, 8 topics): `database-design, double-entry, fastapi, fintech, hypothesis, ledger, postgresql, python` — including **`fastapi` + `python` + `postgresql`** (LE31 backend stack match) + **`double-entry` + `ledger`** (LE31 v1 double-entry-ledger domain match) + **`hypothesis`** (LE31 v1 property-based-testing discipline). Bucket: **v1 (double-entry-ledger-vocabulary)** — Pick B of Daily Research 2026-10-11. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`PostgreSQL-as-arbiter + deferred-constraint-triggers + append-only-history + idempotency + holds + reversals + reconciliation + FastAPI + Postgres + Python + Hypothesis`** decuple-primitive as a persistent cross-section reference for the LE31 v1 *PostgreSQL-itself-guarantees-the-books-balance + Hypothesis-property-tests* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (TODAY PUSH of a freshly-published repo) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`PostgreSQL-as-arbiter + deferred-constraint-triggers`** double-primitive: the books balance is **guaranteed by PostgreSQL itself** via deferred constraint triggers (the constraint that the books balance is checked at COMMIT time, not at INSERT time, so partial transactions can complete without violating the constraint; the database itself is the source of truth for ledger consistency, not the application code). This is the §3.1 explicit-state-transitions primitive applied to ledger writes with PostgreSQL-itself as the arbiter. The **PostgreSQL-itself-guarantees-the-books-balance** pattern is the **strongest v1 PostgreSQL-as-arbiter double-entry-ledger pattern of the 73-pass series**.
- A written record of the **`append-only-history + idempotency + holds + reversals + reconciliation`** quintuple-primitive: the ledger history is append-only (no UPDATE or DELETE on ledger rows); writes are idempotent (a duplicate write does not create a duplicate row); holds can be placed on ledger entries (a hold reserves a balance for a future transaction); reversals are first-class (a reversal is a new ledger entry that negates a prior entry, never an UPDATE on the original); reconciliation is a first-class operation (the system can verify that the books balance at any point in time). This is the §3.1 + §3.3 *append-only + no-implicit-state-transition + audit-log-immutability* charter invariant applied to the *double-entry-ledger* dimension.
- A written record of the **`FastAPI + Postgres + Python + Hypothesis`** stack-shape: FastAPI on-stack, Postgres on-stack, Python on-stack, Hypothesis for property-based testing. **4 of 4 LE31 backend stack primitives** matched (FastAPI + Postgres + Python + Hypothesis is the LE31-stack-match primitive). The **Hypothesis** primitive is the **§3.2 property-based-testing discipline** applied to ledger-write correctness (vs application-side logic tests).
- A written record of the **PostgreSQL-itself-as-arbiter** operator-surface-shape: the operator can rely on PostgreSQL to reject any transaction that would leave the books unbalanced; the operator does not need to trust the application code. Sister-shape to feature 259 (CtrlAltDevelop/ledger-service — double-entry ledger over HTTP with atomic + idempotent + append-only + transactional-outbox) + feature 232 (lpalbou/AbstractGateway — durable AI control plane) + feature 287-289 (v2-AI audit-trail vocabulary cluster) + feature 187 + 188 (traust-ledger — append-only disposition) + feature 296 (AlvaroVerona/prime-cost — restaurant P&L analytics) + feature 270 (cesaremcasa/manager-architecture — auditable calculations).
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (387 KB modest; TODAY PUSH); (2) the stack-shape match is the value, not the code (LE31 v1 has no double-entry ledger; the surface is OFF v1 charter today); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the Bastardki11er codebase (0★ with single-maintainer cadence; TODAY PUSH = freshly-published; no observed production usage).
- Cross-pollination with the PostgreSQL-itself-as-arbiter pattern in v1 (LE31 v1 has no double-entry ledger).
- Cross-pollination with the Hypothesis property-based-testing pattern in v1 (LE31 v1 uses pytest fixtures + assertions, not Hypothesis).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v1 ledger surface proposes "the double-entry ledger where PostgreSQL itself guarantees the books balance via deferred constraint triggers + append-only history + idempotency + holds + reversals + reconciliation + Hypothesis property tests primitive" (e.g., a v1 surface that adds a *cash-till-ledger* or *payment-tip-reconciliation-ledger* or *expense-ledger* to LE31 v1's existing StockEntry + audit_logs, with PostgreSQL-itself-as-arbiter for ledger consistency), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "PostgreSQL-itself-as-arbiter + deferred-constraint-triggers + double-entry + append-only + idempotency + holds + reversals + reconciliation + Hypothesis" is a real demand signal*, so that *the v1 ledger surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31 + the PostgreSQL-itself-as-arbiter pattern + the Hypothesis-property-tests discipline"*.

- **Evidence class**: observed (the description + 8 topics name the primitives explicitly: `database-design, double-entry, fastapi, fintech, hypothesis, ledger, postgresql, python`).
- **Confidence**: high for the vocabulary match (the verbatim description names the 10-primitive decuple set + the FastAPI + Postgres + Python + Hypothesis stack); medium for transferability (LE31 v1 has no double-entry ledger today; the surface is OFF v1 charter but is a future v1 polish candidate).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has StockEntry + audit_logs but no double-entry money ledger); the value is the *PostgreSQL-itself-as-arbiter + deferred-constraint-triggers + append-only-history + idempotency + holds + reversals + reconciliation + Hypothesis-property-tests* vocabulary — when the first v1 PR that adds a cash-till-ledger or payment-tip-reconciliation-ledger lands, the Bastardki11er pattern is a ready-made *named primitive*.

## Description

GitHub `Bastardki11er/tally` (MIT, 0★/0⑂, Python + FastAPI + Postgres + Hypothesis, pushed 2026-10-11T01:22:08Z = TODAY, created 2026-09-XX, 387 KB modest). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-11): *"Double-entry ledger API where PostgreSQL itself guarantees the books balance: deferred constraint triggers, append-only history, idempotency, holds, reversals, reconciliation. FastAPI + Postgres + Hypothesis."*

The architectural primitive has nine sub-primitives that map 1:1 onto the LE31 v1 ledger surface:

1. **`PostgreSQL itself guarantees the books balance`** — the books balance is enforced by PostgreSQL itself via deferred constraint triggers (the constraint is checked at COMMIT time, not at INSERT time). The *PostgreSQL-itself-as-arbiter* primitive is the **strongest v1 PostgreSQL-as-arbiter double-entry-ledger pattern of the 73-pass series**.
2. **`Deferred constraint triggers`** — the constraint that the books balance is implemented as a deferred constraint trigger (CREATE CONSTRAINT TRIGGER ... DEFERRABLE INITIALLY DEFERRED). The *deferred* discipline means partial transactions can complete without violating the constraint, and the constraint is only checked at COMMIT time. This maps 1:1 onto the *atomic-transaction* primitive applied to ledger-write operations.
3. **`Append-only history`** — the ledger history is append-only (no UPDATE or DELETE on ledger rows). The *append-only* primitive is §3.1-aligned (current stock is derived from entries; ledger entries are never updated or deleted).
4. **`Idempotency`** — writes are idempotent (a duplicate write does not create a duplicate row; the API uses idempotency keys). The *idempotency* primitive maps 1:1 onto any future v1 ledger-write surface (e.g., a retry-safe payment-tip-reconciliation write).
5. **`Holds`** — holds can be placed on ledger entries (a hold reserves a balance for a future transaction; the hold is recorded as a ledger entry with a `hold` flag). The *holds* primitive maps 1:1 onto any future v1 cash-till surface (e.g., a held-payment that has not yet cleared).
6. **`Reversals`** — reversals are first-class (a reversal is a new ledger entry that negates a prior entry, never an UPDATE on the original). The *reversals* primitive maps 1:1 onto any future v1 ledger-correction surface (e.g., a wrong-tip-reversal or a mis-keyed-amount-reversal).
7. **`Reconciliation`** — reconciliation is a first-class operation (the system can verify that the books balance at any point in time). The *reconciliation* primitive maps 1:1 onto any future v1 end-of-day-recap surface.
8. **`FastAPI + Postgres + Python`** — the stack is FastAPI on-stack, Postgres on-stack, Python on-stack. **3 of 4 LE31 backend stack primitives** matched (LE31 also pins SQLModel which is built on SQLAlchemy + Pydantic — FastAPI + Postgres + Python is the direct stack-match).
9. **`Hypothesis property tests`** — the test discipline is Hypothesis (property-based testing, not example-based testing). The *Hypothesis* primitive is the **§3.2 property-based-testing discipline** applied to ledger-write correctness (e.g., a property that verifies that the books always balance after any sequence of writes).

**The 1:1 mapping onto LE31 surface:**

| Bastardki11er primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| PostgreSQL itself guarantees the books balance | (LE31 v1 has no double-entry ledger) | v1 polish | **Not implemented** — v1 polish surface |
| Deferred constraint triggers | (LE31 v1 has no deferred triggers) | v1 polish | **Not implemented** — v1 polish surface |
| Append-only history | `audit_logs` (append-only atomic) | §3.1 ✓ | **Implemented (v1)** |
| Idempotency | (LE31 v1 has no idempotency keys for ledger writes) | v1 polish | **Not implemented** — v1 polish surface |
| Holds | (LE31 v1 has no holds) | v1 polish | **Not implemented** — v1 polish surface |
| Reversals | (LE31 v1 has no reversals) | v1 polish | **Not implemented** — v1 polish surface |
| Reconciliation | (LE31 v1 has no reconciliation endpoint) | v1 polish | **Not implemented** — v1 polish surface |
| FastAPI + Postgres + Python | Python + FastAPI + SQLModel + Postgres | §3.1 ✓ | **Implemented (v1)** |
| Hypothesis property tests | (LE31 v1 uses pytest fixtures, not Hypothesis) | v1 polish | **Not implemented** — v1 polish surface |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that introduces a cash-till-ledger or payment-tip-reconciliation-ledger with PostgreSQL-itself-as-arbiter semantics), the implementation would add:

1. A new `LedgerEntry` table (Alembic migration) with columns: `id` (UUID), `account_id` (str FK), `debit` (Decimal with EUR-cents precision per §3.6), `credit` (Decimal with EUR-cents precision per §3.6), `memo` (str), `idempotency_key` (str UNIQUE), `hold_id` (UUID FK nullable), `reversal_of_id` (UUID FK nullable), `decided_at` (timezone-aware datetime per §3.5).
2. A deferred constraint trigger that verifies `SUM(debit) == SUM(credit)` per `account_id` at COMMIT time (CREATE CONSTRAINT TRIGGER ... DEFERRABLE INITIALLY DEFERRED).
3. A `hold` column on the `LedgerEntry` table that is true when the entry is a hold (the hold reserves a balance for a future transaction).
4. A `Hold` table (Alembic migration) with columns: `id` (UUID), `amount` (Decimal with EUR-cents precision per §3.6), `released_at` (timezone-aware datetime nullable), `released_to_ledger_entry_id` (UUID FK nullable).
5. A `Reconciliation` table (Alembic migration) with columns: `id` (UUID), `reconciled_at` (timezone-aware datetime), `balanced` (bool), `discrepancy` (Decimal with EUR-cents precision per §3.6).
6. A `GET /v1/ledger/entries?account=<>&as_of=<>&hold=<>` search endpoint.
8. A `GET /v1/ledger/verify?account=<>&as_of=<>` reconciliation endpoint.
9. A `POST /v1/ledger/holds` FastAPI endpoint that places a hold.
10. A `POST /v1/ledger/holds/<hold_id>/release` FastAPI endpoint that releases a hold.

The HANDOFF is to evaluate whether the v1 ledger surface is the right product-wedge for the next v1 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires:

**For v1 double-entry-ledger-vocabulary surface** (if approved):

1. Add a new `LedgerEntry` SQLModel table (Alembic migration).
2. Add a new `Hold` SQLModel table (Alembic migration).
3. Add a new `Reconciliation` SQLModel table (Alembic migration).
4. Add a deferred constraint trigger that verifies `SUM(debit) == SUM(credit)` per `account_id` at COMMIT time.
6. Add a `GET /v1/ledger/entries?account=<>&as_of=<>&hold=<>` FastAPI endpoint.
8. Add a `GET /v1/ledger/verify?account=<>&as_of=<>` reconciliation endpoint.
9. Add a `POST /v1/ledger/holds` FastAPI endpoint.
10. Add a `POST /v1/ledger/holds/<hold_id>/release` FastAPI endpoint.
11. Add a `POST /v1/ledger/entries/<entry_id>/reverse` FastAPI endpoint that records a reversal.
12. Add Hypothesis property tests in `backend/tests/property/test_ledger.py` that verify the books-always-balance property after any sequence of writes.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires, the v1 surface would add **a v1 owner-Telegram-recap primitive** (e.g. the owner gets a Telegram end-of-day-recap with the day's ledger totals + reconciliation status). The recap primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram).

## Dependencies

- Python 3.13 on-stack (LE31 pins Python 3.13).
- FastAPI on-stack (LE31 pins FastAPI).
- Postgres on-stack (LE31 pins Postgres).
- SQLModel on-stack (LE31 pins SQLModel).
- Hypothesis — NEW transitive dependency for v1 polish surface (property-based testing).
- `decimal` stdlib (LE31 already uses Decimal per §3.6).

## Open questions

- **None today.** The defer artifact is documentation only.

## Why this matters

- **Vocabulary persistence**: the **`PostgreSQL-as-arbiter + deferred-constraint-triggers + append-only-history + idempotency + holds + reversals + reconciliation + Hypothesis-property-tests`** decuple-primitive is a **named primitive** that any future LE31 v1 ledger surface can reference without re-deriving the concept. The verbatim description names the 9-primitive set + the FastAPI + Postgres + Python + Hypothesis stack.
- **Stack-shape validation**: the **`FastAPI + Postgres + Python + Hypothesis`** stack-shape arrived at independently in 2026 by an MIT maintainer with no LE31 charter visibility (TODAY PUSH of a freshly-published repo). This validates that the LE31 v1 ledger stack-direction (FastAPI + Postgres + Python + property-based tests) is a real 2026 demand signal.
- **PostgreSQL-itself-as-arbiter pattern**: the *PostgreSQL-itself-guarantees-the-books-balance* pattern is the **strongest v1 PostgreSQL-as-arbiter double-entry-ledger pattern of the 73-pass series**. The *deferred-constraint-triggers* primitive is the **strongest v1 atomic-transaction-via-database-constraint pattern of the 73-pass series**.
- **Sister-shape to features 259 + 232 + 287-289 + 187 + 188 + 221 + 270 + 296**: Bastardki11er/tally is the 9th addition to the persistent v1 ledger vocabulary cluster. The cluster now covers: CtrlAltDevelop/ledger-service (double-entry + atomic + idempotent + append-only + transactional-outbox) + lpalbou/AbstractGateway (durable AI control plane) + noise01/endoxa (governed beliefs for LLM agents) + pete-builds/mcp-nixreview (MCP-server with CVE/KEV attestation) + shivamk01here/LedgerLoop (Python runtime for financial AI agents) + traust-ledger (append-only disposition) + mrlonis/python-open-restaurant-fastapi (in-domain 100% LE31-stack-match) + cesaremcasa/manager-architecture (auditable calculations + tenant isolation) + AlvaroVerona/prime-cost (restaurant P&L analytics) + **PostgreSQL-itself-as-arbiter + deferred-constraint-triggers + Hypothesis-property-tests (Bastardki11er/tally)** = the strongest v1 ledger-vocabulary cluster of the 73-pass series.