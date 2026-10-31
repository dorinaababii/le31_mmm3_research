# HANDOFF — 412-sasambatra-orderflow-reservation-and-outbox-vocabulary

**Status**: **defer** (v1, parking-lot vocabulary reference — **NOT a build**)
**Date**: 2026-10-31
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/412-sasambatra-orderflow-mit-python-fastapi-postgresql-redis-celery-atomic-multi-item-reservation-sorted-row-locks-transactional-outbox-idempotent-inbox-15-minute-reservation-window-v1-reservation-and-outbox-vocabulary.md`
**LE31 feature gate verdict**: **defer** — gate check 1 (JTBD) **FAILS**. Evidence class **INFERRED**. **This contract records a rejection. It does not authorise work.**

## Trigger policy

**This is a `defer`. A coding agent must NOT implement this.**

Per `le31-feature-pipeline` §*Hard rules*: *"If the pick fails the gate, do not write a contract; report rejection instead."* **This document exists because the rejection still needs its vocabulary attached** — so that the next pass does not re-derive it, and so that the moment the owner decides to build a reservation, the starting point is written down rather than invented under pressure.

**This contract may be opened by an agent in exactly one circumstance:** the owner has **since** decided that LE31 must hold stock for an order, or the first order router has landed and the oversell race is reachable. **In that case** the agent must:

1. **Re-run the seven-check gate** for the *actual* reservation feature. **This document does not substitute for that gate** — the gate may still reject, because the owner decision changes the evidence, not the verdict automatically.
2. Read the feature file and the artifact's README together.
3. **Treat the vocabulary below as a starting point, not an approved design.**

**Until then, this document is a record.** Implementing it as written — a reservation table, a hold mechanism, an outbox, a job runner — would be **scope creep against a rejected proposal**.

## Frozen contract

**The one thing this contract records:** *When LE31 eventually holds stock for an order, the vocabulary for holding, expiring and releasing it is already written down — and the reasons a reservation needs all three are recorded, not guessed.*

**The vocabulary, and the hazard each part answers** (all quotes verbatim from the artifact's README, 135 lines, `/tmp/le31-daily-2026-10-31/gh/readmes/Sasambatra__orderflow.md`):

| Hazard (L15 / L25 / L28) | Mechanism (L25 / L63 / L74) |
|---|---|
| *"Two buyers can see the same final unit."* | *"Sorted row locks, atomic multi-item reservation, database constraints"* → *"20 buyers / one unit → one `201`, nineteen `409`"* |
| *"A client can retry after losing a successful response."* | *"Write operations require a UUIDv4 `Idempotency-Key`; retry the same operation with the original key. Changed payloads with the same key receive `409`. Replayed responses include `Idempotency-Replayed: true`."* |
| *"A payment provider can send the same event twice, or report success after a reservation has expired."* | *"Transactional outbox, leased dispatch, consumer deduplication"* |
| *"The broker can fail after the database commits."* | *"Transactional outbox"* |

**The three ideas that transfer:**

1. **Atomicity across the order, not per line.** *"atomic multi-item reservation"* — the whole order holds all three items or none. **There is no state in which the kitchen has committed to two of a party's three dishes.**
2. **A named expiry default.** *"Reservations last 15 minutes by default."* **The transferable part is not the 15 minutes** — it is that the window is **a stated default with a named consequence** (a confirmed order arriving after the hold expired). **The number is a placeholder.**
3. **An idempotent inbox.** *"consumer deduplication"* — the broker may deliver twice; the consumer must not act twice. **This is the half of the outbox pattern that is most often forgotten.**

**What does NOT transfer:** the Redis/Celery stack (LE31 runs a single Postgres VPS); RUB; **integer minor units** (LE31 uses `Decimal` EUR, and that choice is an unresolved charter conflict — feature 410); the warehouse domain; the mock payment provider (L131: *"a backend portfolio project with one warehouse, RUB, a **mock payment provider** and a database inbox"*).

**The `StockEntry` rule that must not be broken by any future implementation:** a **hold** is a *mutable state*; a `StockEntry` is an *immutable event*. `le31-conventions`: *"every prepared-item quantity change is a new `StockEntry`. Never update or delete ledger events."* **A hold is released by writing a new ledger event, not by mutating the hold row.** Reusing `StockEntry` as a hold table would put a mutable fact inside the ledger.

## Files to touch

**None.** This feature adds nothing to the repository.

| File | Change |
|---|---|
| `features/412-…md` | **NEW** (this pass). The vocabulary record. |
| `specs/412-…-HANDOFF.md` | **NEW** (this pass). This document. |
| `backend/**` | **NO CHANGE.** No model, no column, no endpoint, no bot command. |

**Any change to `backend/` from this slice is a defect.**

## Mandatory LE31 skill list

An agent **reading** this contract (under the trigger condition above) must load:

- `le31-conventions` — the stock invariant and the seven-check gate.
- `le31-v1-feature-pattern` — the canonical contract shape and the slicing rules.
- `le31-handoff-spec` — the frozen-contract discipline.
- `development` — the generic code pipeline, **if and only if** the gate is re-run and passes.

An agent **not** acting on the trigger condition needs **none** of these; this document is a record.

## Mandatory inputs

- **Active feature**: `features/412-sasambatra-orderflow-mit-python-fastapi-postgresql-redis-celery-…-v1-reservation-and-outbox-vocabulary.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-10-31.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-31/`
  - `gh/repos/Sasambatra__orderflow.json` — direct `GET /repos/` (HTTP 200)
  - `gh/readmes/Sasambatra__orderflow.md` — README, 135 lines, raw text (fetched by the **parent**, not the delegated subagent)
- **LE31 source of truth** (read-only):
  - `backend/app/models.py:105-106` — `Batch.qty_start`, `Batch.qty_remaining`
  - `backend/app/models.py:113-126` — `class StockEntry` (the ledger; **never constructed anywhere**)
  - `backend/app/models.py:27-32` — `class TableStatus` — `free, seated, ordered, billed, dirty`; **no `reserved`**
  - `backend/app/models.py:54-59` — `class StockReason` — **no `reserved`/`held`/`released`**
  - `backend/app/bot/cook_bot.py:11, 72, 82-83` — `/sold_out` advertised, **unregistered**
  - `grep -rni "reserv|hold|release|ttl" backend/app/` → **two hits**, neither a reservation: `models.py:65` (the word *"reserved"* in a SQL comment) and `models.py:108` (`Batch.expires_at` — **shelf-life**, no owning order, no release trigger)
- **Sibling features to read but NOT merge:** 374 (`qty_remaining`), 404 (active-batch predicate — **a reservation expiry is not a batch shelf-life**), 405 (business day), 410 (money-rule reconciliation).
- **NOT bundled here:** the **idempotency gap**, recorded in the parent report's *Adjacent evidence*. It is a real first-party gap and it is a **separate** gap.

## Verification protocol reference

**There is no verification protocol, because there is nothing to verify.** No code, no schema, no behaviour.

**The only check an agent may perform** is a read-only confirmation that the recorded first-party state is still true:

```bash
grep -rni "reserv|hold|release|ttl" backend/app/     # expect: 2 hits, neither a reservation
grep -rn "StockEntry" backend/app/                     # expect: declaration only, no construction site
grep -n "reserved" backend/app/models.py              # expect: no TableStatus/StockReason member
```

**If any of those has changed** — a reservation model now exists, or the ledger is now written — **this document is stale and must be re-derived**, not acted on.

## Rollback path

**Nothing to roll back.** No code, no schema, no data.

**What remains safe if the document is deleted:** every LE31 behaviour. **The vocabulary is the only thing it holds.**

**Trigger condition for revisiting:** the owner decides LE31 must hold stock for an order, **or** the first order router lands and the oversell race becomes reachable. **At that point, re-run the gate** — the trigger changes the *evidence*, not the verdict.

## Sign-off gap

**Every question in this slice is an unmade owner decision, and this artifact made none of them:**

1. **Does LE31 need reservations at all?** **The whole question, unasked.** Recorded default: assume **no** for v1 — LE31's charter covers in-service dining (seat → order → bill), not booking management.
2. **What is being reserved** — prepared stock, a menu item, or a table? **Three different objects, three different models.** Recorded default: undecided.
3. **The expiry window.** The artifact's 15 minutes is a **warehouse** default for an order basket; LE31's flow is a seated party ordering over time. Recorded default: undecided. **Note that any window introduces a background job, and LE31 has no job runner — a larger decision than the window.**
4. **What happens to an order confirmed after its hold expired?** `le31-conventions` common pitfall 3 applies: *"Calling an automatic transition 'convenient.' Explicit operational state is a deliberate safety principle."* An auto-releasing hold nobody asked for **is** a silent transition.
5. **Is an outbox needed at all?** LE31 has no broker, no Celery, no Redis and no second service, so *"the broker can fail after the database commits"* is **not LE31's failure mode today**. Recorded default: **not needed until LE31 has an external side effect to make safe.** Its other use — a reliable local event feed for the cook bot — **may be the real need, and that is a separate question.**

**The agent must not widen any of these.** If the trigger fires, each needs its own decision and its own gate.

## Handoff summary

`Sasambatra/orderflow` (MIT, Python, in-window by both dates) is a compact, unusually disciplined transactional-checkout backend whose README pairs **each failure mode with its mechanism and a named test in the same breath**: *"Overselling the last unit → Sorted row locks, atomic multi-item reservation, database constraints → 20 buyers / one unit → one `201`, nineteen `409`"*; *"The broker can fail after the database commits → Transactional outbox → Real Redis outage and recovery."*

**That pairing is the transferable idea**, and it is a shape LE31's own feature contracts do not yet have: a feature that names its hazard in the same sentence as its mechanism is checkable; one that only names the mechanism is not.

**It is recorded and not adopted** because LE31 **has no reservation concept at all** — `TableStatus` has no `reserved` member, `StockReason` has no `reserved`/`held`/`released` member, `StockEntry` has no `reserved_qty` and no `hold_until` — and because **there is nothing to reserve against**: `OrderItem` and `StockEntry` are never constructed anywhere in `backend/`, the HTTP surface is two endpoints, and the bot registers two of six advertised commands.

**The vocabulary is worth having on the shelf**, because the day LE31's first order router lands, *"two buyers can see the same final unit"* stops being an abstraction and becomes **LE31's problem** — and on that day the vocabulary should already be written down rather than invented between a waiter and a customer.
