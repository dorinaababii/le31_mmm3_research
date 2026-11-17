# Feature 490 — `v2-reservation-engine-with-database-enforced-table-allocation`

> **Pick B of Daily Research 2026-11-17.** **Bucket: v2 (new reservation domain).** **Verdict: `defer` — parking-lot architecture reference.**
>
> **Source artifact:** `David-Cabeza/OpenCovers` — Apache-2.0, ★2 / ⑂0, TypeScript/Hono/PostgreSQL/React, created 2026-11-09, pushed 2026-11-16. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-17/repos/09_David-Cabeza_OpenCovers.json`; README: `/tmp/le31-daily-2026-11-17/readme/09_David-Cabeza_OpenCovers.md`; source URL: https://github.com/David-Cabeza/OpenCovers.
>
> **Why this pick:** the source makes the no-double-booking rule a **database invariant**, and combines it with idempotency keys, monotonic versions, an overbooking ceiling, and the rule that a reservation cannot be seated without a table. That is a compact, explicit reservation-engine vocabulary.
>
> **Project constraint:** the workspace has only `le31 v1 — Core MVP`, `le31 Workflow`, and `le31 Research`. The matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's reservation-engine mechanisms as the reference design for a future LE31 v2 reservations surface:

1. overlapping table allocations are rejected by PostgreSQL, not by application locking;
2. every reservation write carries an idempotency key and a monotonic version;
3. a reservation cannot be seated without a table;
4. overbooking is an explicit per-venue ceiling, default zero;
5. privacy-preserving erasure keeps hashes rather than personal values.

No reservation surface or schema is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the five-mechanism summary.
- The explicit boundary with LE31 v1's two-surface charter and existing feature 402 (reservation domain out of v1).
- A future-project attachment decision: `le31 Research`, because no v2 project exists.

**Out of scope (defer artifact):**

- No reservation, booking, waitlist, venue, floor-plan, host, or table-allocation table.
- No PostgreSQL exclusion constraint in LE31.
- No waitlist, walk-in triage, visual floor plan, email confirmation, signed webhook, MCP server, or venue API-key administration.
- No adoption of the TypeScript/Hono/React/Better Auth stack.
- No v1 scope expansion.

## Description

OpenCovers' README states the mechanisms directly:

- *"Any platform or AI agent reads availability, creates a booking, modifies it, or cancels it through the same contract — and the no-double-booking rule is enforced by the database, not by application code."*
- *"Every write carries an idempotency key and a monotonic version."*
- *"A GiST exclusion constraint in PostgreSQL rejects overlapping table allocations. It holds for any number of concurrent writers — no application-level locking."*
- *"An explicit overbooking ceiling per venue (default 0, enforced under a per-venue lock) ... and a rule that a reservation cannot be seated without a table."*
- *"Tombstones keep the hashes, never the personal values."*

The transferable idea is the **placement of the invariant**. LE31's own feature 402 records that action guards should live below the UI. OpenCovers demonstrates the same principle for allocation: the check lives in the database's concurrency semantics, so every writer gets the same answer.

The two mechanisms that are not merely conceptual are:

- **idempotency key + monotonic version** on every write; and
- **seatability requires a table**, which makes the state transition from reservation to seated explicit rather than inferred.

## Data model

No schema change. The future reference shape, explicitly **not proposed today**, is:

```text
Reservation (future reference)
  id, venue_id, starts_at, ends_at, table_ids[], party_size,
  idempotency_key, version, status, seated_table_id
```

A PostgreSQL exclusion constraint over the allocated table/time interval would express non-overlap. LE31's SQLite development environment cannot enforce the same constraint shape, so a future implementation would need a cross-database answer rather than a direct copy.

## Implementation

None in this feature. When reservations are promoted into a scoped v2 feature:

1. Decide the cross-database strategy for allocation non-overlap.
2. Define the idempotency-key namespace and version semantics.
3. Make seating require a table allocation.
4. Make overbooking an explicit, visible ceiling with default zero.
5. Define erasure semantics that retain hashes, not personal values.
6. Keep reservation state transitions separate from LE31's `StockEntry` and bill ledger.

## Telegram interaction

None. A host assistant or reservation bot would be a new surface and is not authorized by this reference.

## Dependencies

- Existing feature 402 — reservations are out of v1; storage-layer guard vocabulary.
- Existing feature 414 — table capacity and over-capacity seating behavior in LE31's current model.
- Existing feature 388 — table status and free/seated semantics, if that feature remains in the corpus.
- Existing features 382/400 — idempotency-key vocabulary.
- PostgreSQL in production; SQLite in development is an unresolved cross-database constraint.

## Open questions

1. Is reservations a real v2 product need, or only a reference worth retaining?
2. If yes, is reservation a new domain or an extension of `Visit`?
3. How will allocation non-overlap be enforced in SQLite development and PostgreSQL production without divergent behavior?
4. Does idempotency use the same namespace as LE31's stock/bill writes or a separate reservation namespace?
5. Is overbooking ever permitted, and who may raise the ceiling?
6. What data must be erased when a guest is deleted, and which hashes must remain?

## Why this matters

OpenCovers is recent, permissive, and unusually explicit about where the invariant lives. It gives LE31 a reference for a domain that currently has only an out-of-scope note.

The correct disposition is nevertheless **defer**: the reservation domain is absent from LE31 v1, no operator has asked for it, and a database constraint that only works in Postgres would create the same dev/prod divergence already recorded in feature 413. Filing it now preserves the mechanism without pretending the demand exists.
