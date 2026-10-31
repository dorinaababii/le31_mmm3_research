# Feature 412 — `Sasambatra/orderflow`: atomic multi-item stock reservation, transactional outbox, and an idempotent inbox — vocabulary for a reservation LE31 does not have

> **Pick B of Daily Research 2026-10-31 (93rd pass).** **VOCABULARY ONLY — `defer`.** The artifact is a real, complete, on-stack implementation of three mechanisms LE31's charter *mentions* but does not implement; **LE31 has no reservation concept at all**, so this is recorded for vocabulary, not proposed for build.
>
> `Sasambatra/orderflow` (MIT, ★0/0⑂, **Python**, 157 KB, created 2026-10-30, pushed 2026-10-30 — **in-window by both `created_at` and `pushed_at`**; all fields parent-verified via direct `GET /repos/` at `/tmp/le31-daily-2026-10-31/gh/repos/Sasambatra__orderflow.json`; topics `celery, docker, fastapi, idempotency, inventory-management, portfolio-project, postgresql, redis`).
>
> Its README states, verbatim:
>
> > L25 — *"| Overselling the last unit | Sorted row locks, atomic multi-item reservation, database constraints | [20 buyers / one unit](tests/concurrency/test_races.py) → one `201`, nineteen `409` |"*
> >
> > L15 — *"Two buyers can see the same final unit. A client can retry after losing a successful response. A payment provider can send the same event twice, or report success after a reservation has expired. The broker can fail after the database commits."*
> >
> > L74 — *"Lists use bounded cursor pagination. Prices are integer RUB minor units; order lines preserve product/price snapshots. **Reservations last 15 minutes by default.** All timestamps are timezone-aware UTC."*
> >
> > L63 — *"Routes use `/api/v1`. Write operations require a UUIDv4 `Idempotency-Key`; retry the same operation with the original key. Changed payloads with the same key receive `409`. Replayed responses include `Idempotency-Replayed: true`."*
>
> **Bucket: v1.** MIT ✓ §3.2 strictly-compatible; Python + FastAPI + Postgres **on-stack**. **Vocabulary-only — `defer`.** Evidence class: **INFERRED** (no LE31 owner has asked for reservations; **and LE31's schema has no place to put one**).
>
> **⚠️ Gate check 1 FAILS on two counts, and the second is structural.** First: no reported owner pain. Second, and decisively: **LE31 has no reservation concept at all** — `grep -rni "reserv|hold|release|ttl" backend/app/` returns **exactly two hits**, and **neither is a reservation**: `models.py:65` (the word *"reserved"* in a SQL-reserved-word comment) and `models.py:108` (`Batch.expires_at` — a **shelf-life** timestamp with no owning order, no reserved quantity and no release trigger). `TableStatus` (`models.py:27-32`) has exactly five states — `free, seated, ordered, billed, dirty` — and **no `reserved`**. `StockReason` (`models.py:54-59`) has **no `reserved`/`held`/`released`**. **Adopting a reservation model is a new product concept with a new table, not a feature.**

## Goal

**Record, in LE31's own vocabulary, three mechanisms that a restaurant system needs and that LE31's charter assumes but does not implement** — so that when the owner *does* decide to build a reservation or an event-delivery path, the vocabulary is already settled and the design is not invented from scratch under pressure.

**This feature produces no code and changes no behaviour.** Its deliverable is this document plus the handoff contract beside it. It is a **parking-lot** entry with the vocabulary written down.

**The single sentence this feature exists to make true:** *When LE31 eventually holds stock for an order, the vocabulary for holding, expiring and releasing it is already written down — and the reasons a reservation needs all three are recorded, not guessed.*

## Scope

**In scope (v1):**

- **A written vocabulary** for: an atomic multi-item reservation, a reservation expiry window, a transactional outbox, and an idempotent inbox.
- **The failure modes each mechanism exists to prevent**, recorded verbatim from the artifact and mapped onto LE31's own surfaces.
- **A recorded statement of why each is *not* being built now** — so the next reader does not re-derive it.

**Out of scope (v1):**

- **Any model, column, table, endpoint or bot command.** This feature **adds nothing to `backend/`**. It is a **document**.
- **Any change to `Batch`, `StockEntry`, `OrderItem`, `Table` or `TableStatus`.** Specifically:
  - **`Batch.qty_remaining`** — feature 374 (derive, don't store).
  - **`Batch.expires_at`** — feature 404 (the null-safe active-batch predicate). **A reservation expiry is a different thing from a batch shelf-life**, and the two must never be conflated: `expires_at` says *"this tiramisu goes stale at 14:00"*; a reservation expiry says *"nobody confirmed this order within 15 minutes, so release the hold"*.
  - **The business day** — feature 405.
- **Any change to LE31's committed architecture.** §3.2 commits LE31 to a **single, online, server-authoritative** VPS. The artifact's reservation model is **also** server-authoritative (it is not offline-first), so it does **not** conflict — but a reservation-with-expiry **does** introduce a background job, and **LE31 has no job runner**. Adopting it is a **v1-scope decision for the owner**, not a research finding.
- **Idempotency keys on LE31's write paths.** LE31 has **no** idempotency, dedup or duplicate-guard anywhere — `grep -rni "idempot|dedup|duplicate|nonce|request_id" backend/app/` returns **no hits** (the only `unique=True` in the whole schema is `Bill.visit_id`, `models.py:162`, which is a data constraint, not an action guard). **This is a real first-party gap, but it is a different gap, and it is recorded in *Adjacent evidence* of the parent report — not bundled here.**
- **The artifact's money representation.** It uses **integer RUB minor units**. LE31 uses `Decimal` EUR, and that representation choice is an **unresolved charter conflict** (feature 410). **Do not import the representation.**
- **The artifact's `portfolio-project` nature.** Its README states outright (L131): *"This is a backend portfolio project with one warehouse, RUB, a **mock payment provider** and a database inbox. It does not transfer money, submit bank refunds or send external email/SMS."* **Treat it as a mechanism reference, not a production system.**

## Description

### What the artifact actually demonstrates

`Sasambatra/orderflow` is a small (157 KB) but unusually disciplined transactional-checkout backend. Its README presents a **failure-mode table**, and each row pairs a concrete hazard with a concrete mechanism *and a named test*. Four rows are directly relevant to LE31's charter:

| Hazard (verbatim L15/L25/L28) | Mechanism | Named test |
|---|---|---|
| *"Overselling the last unit"* | *"Sorted row locks, atomic multi-item reservation, database constraints"* | *"20 buyers / one unit → one `201`, nineteen `409`"* |
| *"A client can retry after losing a successful response"* | *"Idempotency-Key … Changed payloads with the same key receive `409`. Replayed responses include `Idempotency-Replayed: true`."* | — |
| *"A payment provider can send the same event twice, or report success after a reservation has expired"* | *"Transactional outbox, leased dispatch, consumer deduplication"* | *"Real Redis outage and recovery"* |
| *"The broker can fail after the database commits"* | *"Transactional outbox"* | *"Real Redis outage and recovery"* |

**The vocabulary that transfers is the *pairing* itself.** The artifact's real contribution is not any one mechanism — it is that **each hazard is stated in the same sentence as its mechanism and its test**. That is a shape LE31's own contracts do not yet have, and it is cheap to copy.

**Three ideas transfer; the rest does not.**

**1. An atomic *multi-item* reservation.** LE31's `OrderItem` rows arrive in **batches** (a party orders three things). The artifact's *"atomic multi-item reservation"* means the whole order either holds all three items or **none** — there is no state in which the kitchen has committed to two of a party's three dishes. **LE31 has no reservation at all**, so this is a *future* concept; the vocabulary worth keeping is *"all-or-nothing across the order, not per line"*.

**2. A reservation expiry window with a named default.** *"Reservations last 15 minutes by default."* LE31's charter is explicitly a **no-silent-transition** system (`le31-conventions`: *"operational transitions are explicit user actions"*), so the interesting part is **not** the 15 minutes — it is that the expiry is **a stated default with a named owner-visible consequence** (a confirmed order arriving after the hold expired). **The number is a placeholder; the *named default* is the transferable part.**

**3. An idempotent inbox.** The broker can deliver twice; the consumer must not act twice. This is the *"consumer deduplication"* half of the outbox pattern, and it is the piece most often forgotten.

**What does not transfer:** the Redis/Celery stack (LE31 runs a single Postgres VPS), the RUB currency, the integer minor units, the warehouse domain, and the mock payment provider.

### Why this is `defer` and not `build`

Three reasons, in order of weight:

1. **There is no owner pain.** No LE31 owner has asked for reservations. The evidence class is **INFERRED**, and `le31-conventions` §*Common Pitfalls* #2 is explicit: *"Treating research novelty as user demand. A paper or release is evidence about possibility, not evidence of restaurant pain."*
2. **LE31's schema cannot hold a reservation.** A reservation needs a *quantity held*, an *owner*, a *window* and a *release trigger*. `Batch` has `qty_start` and `qty_remaining` only (`models.py:105-106`); `StockEntry` has `batch_id`, `qty_delta`, `reason`, `ref_order_item_id`, `by_user_id`, `at` — and **no `reserved_qty`, no `hold_until`**; `TableStatus` has no `reserved` member. **This is a new model, not a feature.**
3. **LE31's whole order path does not exist yet.** The backend has **two** functional HTTP endpoints (`GET /api/tables`, `POST /api/tables/{id}/seat`) and **two** registered bot commands (`/start_today`, `/help`) out of six advertised. `OrderItem` is **never constructed** anywhere in `backend/`. **There is nothing to reserve against.**

**The trigger condition for revisiting this:** the owner decides LE31 must hold stock for an order (a "reserve 2 tiramisu for table 5, confirmed at the table" workflow), **or** the first order router lands and the oversell race becomes reachable. At that point this vocabulary is the starting point, and the decision needs its own gate.

## Data model

**No new table. No new column. No schema change. No code.**

This feature's "data model" section is a **description of what a future reservation model would need**, recorded so the shape is not invented under pressure:

```
A reservation, if LE31 ever builds one, would need at minimum:

  batch_id         -> which prepared batch the quantity is held from
  order_item_id    -> which order line the hold belongs to
  qty              -> how much is held
  held_at          -> when the hold was taken
  expires_at       -> when the hold is released if unconfirmed
  released_at      -> when it was actually released (NULL while held)

None of these exist today. `StockEntry` has `batch_id` and `ref_order_item_id`
already, but no quantity-hold, no window and no release marker -- and a
`StockEntry` is an append-only LEDGER event, not a mutable hold. Reusing it
for a hold would put a mutable fact in the ledger, which is the exact thing
the ledger exists to prevent.
```

**The explicit "do not reuse `StockEntry` for this" note is load-bearing.** `le31-conventions`: *"Stock: every prepared-item quantity change is a new `StockEntry`. Never update or delete ledger events."* A **hold** is a *mutable state*; a `StockEntry` is an *immutable event*. **They are different kinds of thing and the vocabulary must keep them apart** — a hold is released by *writing a new ledger event*, not by mutating the hold row.

## Implementation steps

**There is no implementation.** This is a `defer` — a parking-lot vocabulary artifact. Per `le31-feature-pipeline` §*Hard rules*: *"If the pick fails the gate, do not write a contract; report rejection instead."* **This handoff exists as a record of the rejection, with the vocabulary attached**, and it must state plainly that **a coding agent must not implement it**.

**What a future agent may do with this document:** if and when the owner decides to build a reservation, **read this document and the artifact's README together**, and **re-run the seven-check gate for the actual reservation feature**. The vocabulary below is a starting point, **not an approved design**.

**What a future agent must not do:** implement a reservation from this document alone, attach a `reserved_qty` to `Batch`, reuse `StockEntry` as a hold table, add a job runner, or add an `Idempotency-Key` header to LE31's existing routes. **Each of those is a separate feature with its own gate.**

## Telegram interaction if any

**None.** This feature touches no bot command.

**One observation is recorded because it bears on a *future* decision, not on this one:** LE31's cook bot has **no** handler for `/sold_out` — the command is advertised in the bot's own docstring (`cook_bot.py:11`) and in `/help`'s output (`cook_bot.py:72`), but **it has no handler function and no registration** (`cook_bot.py:82-83` register only `/start_today` and `/help`). So a sold-out or hold workflow has **no bot surface to attach to today**, and **none is proposed here**.

## Dependencies

**Read-only references. This feature depends on nothing to build, because it builds nothing.**

- **The artifact's README** — `/tmp/le31-daily-2026-10-31/gh/readmes/Sasambatra__orderflow.md` (135 lines, fetched by the parent on 2026-10-31; **not** via the delegated subagent, which saved only 3 READMEs).
- **The artifact's direct repo metadata** — `/tmp/le31-daily-2026-10-31/gh/repos/Sasambatra__orderflow.json` (HTTP 200).
- **LE31 first-party state to read but NOT change:**
  - `backend/app/models.py:105-106` — `Batch.qty_start`, `Batch.qty_remaining`
  - `backend/app/models.py:113-126` — `class StockEntry` (the ledger)
  - `backend/app/models.py:27-32` — `class TableStatus` (no `reserved` member)
  - `backend/app/models.py:54-59` — `class StockReason` (no `reserved`/`held`/`released` member)
  - `backend/app/bot/cook_bot.py:9-14, 67-76, 82-83` — the six advertised commands, two registered
- **Sibling features to read but NOT merge:** 374 (`qty_remaining`), 404 (active-batch predicate), 405 (business day), 410 (money-rule reconciliation), and the parent report's *Adjacent evidence* section for the **idempotency gap**, which is **not** bundled here.
- **`le31-conventions`** — the stock invariant and the seven-check gate.
- **`le31-handoff-spec`** — the frozen-contract discipline (used here to *record a rejection*, not to authorise work).

## Open questions

**All owner decisions. None is decided here, and none is decided by this artifact.**

1. **Does LE31 need reservations at all?** This is the **whole question**, and it is unasked. LE31's charter covers **in-service dining** (seat → order → bill), not booking management. **Recorded default: assume no for v1.**
2. **If yes, is the hold on prepared stock, on a menu item, or on a table?** Three different objects, three different models. **Recorded default: undecided — the owner's decision, not a research finding.**
3. **What is the expiry window?** The artifact's 15 minutes is **not** a transferable number — it is a *warehouse* default for an *order basket*, and LE31's flow is a seated party ordering over time. **Recorded default: undecided.** Note that **any** window introduces a background job, and **LE31 has no job runner** — which is itself a larger decision than the window.
4. **What happens to an order confirmed after its hold expired?** The artifact's row is *"report success after a reservation has expired"*. LE31's answer must be chosen deliberately, and **`le31-conventions` §*Common Pitfalls* #3 applies**: *"Calling an automatic transition 'convenient.' Explicit operational state is a deliberate safety principle."* **An auto-releasing hold that nobody asked for is a silent transition.**
5. **Is an outbox needed at all?** LE31 has **no** broker, **no** Celery, **no** Redis, and **no** second service. The outbox exists to make *"the broker can fail after the database commits"* safe — a failure mode LE31 **does not have**, because LE31 does not commit across a broker boundary. **Recorded default: the outbox pattern is not needed until LE31 has an external side effect to make safe.** **Its other use — a reliable local event feed for the cook bot — may be the real need, and that is a separate question.**

## Why this matters

Because **the interesting half of this artifact is the four-line failure table**, and LE31's own contracts do not have that shape. LE31's features describe *what to build*; this artifact's README describes **what breaks and what stops it from breaking** — *"two buyers can see the same final unit"*, *"the broker can fail after the database commits"*, *"report success after a reservation has expired"* — **each paired with a mechanism and a named test in the same breath.**

That pairing is the transferable idea, and it is the one worth copying into LE31's own feature contracts: **a feature that names its hazard in the same sentence as its mechanism is checkable; one that only names the mechanism is not.**

And it is recorded **now**, while it is cheap, because the moment LE31's first order router lands, *"two buyers can see the same final unit"* becomes **LE31's problem**, not an abstraction — and on that day the vocabulary should already be written down rather than invented between a waiter and a customer.
