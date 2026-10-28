# Feature 394 — LE31 has no guarded state transitions and no database constraints: a retried write can create a second state

> **Pick A of Daily Research 2026-10-28 (90th pass).** **FIRST-PARTY.** The gap was established by **grep against LE31's own `backend/`**, not inferred from reading prose.
>
> **The three greps (parent-run, 2026-10-28):**
> - `grep -rn "CHECK\|check_constraint\|Constraint" backend/` → **NO OUTPUT**. LE31 declares **zero** database constraints.
> - `grep -n "status" backend/app/models.py` → **EXACTLY ONE hit**: `OrderItem.status` (line 151). Feature 379 already established that **there is no write site for it at all** (`grep -rn 'ItemStatus\.\|\.status = \|status=' --include=*.py backend/` → exactly one hit, and it is the *declaration*).
> - `grep -rn -i "reserved\|available\|on_hand\|on hand" backend/app/` → **NO OUTPUT**. `grep -rn -i "cursor\|replay\|offset\|sequence" backend/app/` → **NO OUTPUT**.
>
> **Trigger (external, in-window):** `hemeshwar09/StockGuard` — **licence `null` → §3.2 STRICTLY-INCOMPATIBLE (the *vocabulary-shape* is transferable, the *code-shape* is NOT adopted)**, **★0/⑂0 — no traction evidence in either direction**, **55 KB**, **Python ✓ + FastAPI ✓ + PostgreSQL ✓ = LE31's exact stack**, created **2026-10-21T07:39:33Z AND pushed 2026-10-21T08:17:55Z = IN-WINDOW BY BOTH FIELDS**, 0 topics, `default_branch=main`, `archived=false`, `fork=false`, 0 open issues. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-28 (`/tmp/le31-daily-2026-10-28/gh/pv/hemeshwar09__StockGuard.json`), **not from search-result numbers**. Description (verbatim): *"Inventory reservation and order service that never oversells under concurrent checkout. FastAPI, PostgreSQL, idempotent payments, TTL-based stock holds, Dockerized."*
>
> **The README was read** (parent, 2026-10-28, `/tmp/le31-daily-2026-10-28/gh/readmes/hemeshwar09__StockGuard.md`). Three claims are recorded below, verbatim: *"Every state change is `UPDATE ... WHERE status = 'ACTIVE'`, so exactly one transition wins"*; *"`CHECK (reserved <= stock)`, `CHECK (stock >= 0)` constraints: the DB refuses to commit an oversold state"*; and the deliberately-broken control strategy *"`naive` — Read, check, write an absolute value — **Intentionally broken** (lost update). Exists so the load test can show what overselling looks like."*
>
> Bucket: **v1**. Verdict: **`defer`** — vocabulary + **one unmade charter question**. **Not `build`, and the reason is the substance of this feature, not a scheduling excuse.**

## Goal

Record in LE31's vocabulary the primitive LE31 currently lacks — **a state transition that is guarded by the condition it depends on**, so that a retried or concurrent write cannot produce a second state — and **name the one business question that must be answered before it can be built**.

The concrete outcome: **one document stating (a) the guarded-transition primitive and (b) the open question about whether a derived stock balance may be negative** — with the two in-window artifacts that disagree about (b) cited side by side.

## Scope

**In scope (v1, defer):**

- **One document** recording the guarded-transition primitive with the verbatim `StockGuard` quotes, the source URL, and the LE31-side vocabulary each one names.
- **One document section** recording LE31's verified current state — the three greps above, quoted, with their outputs.
- **One explicitly-framed open question** — *"may a derived stock balance be negative?"* — with both in-window positions quoted side by side and **neither adopted**.
- **An explicit statement of the dependency** on feature 388 (the `Table` state machine, filed 2026-10-27) and feature 379 (transition attribution): this feature does **not** own the table status column and does **not** own the actor attribution.
- **An explicit statement of what this feature is NOT** — namely, that it is **not** a second copy of feature 388.

**Explicitly NOT in scope:**

- **Any `CHECK` constraint written today.** The sign of the constraint is undetermined (see Open questions). Writing one now would make the decision by accident.
- **Any change to `backend/app/models.py`, `backend/app/routers/tables.py`, or any other file in `backend/`.** This feature changes **zero lines of application code.**
- **Any change to `OrderItem.status` semantics.** The `ItemStatus` enum values and their order are feature 379's and feature 388's business.
- **Any `Table.status` column.** That is **feature 388** (2026-10-27), filed yesterday. See the non-duplication proof below.
- **Any idempotency-key mechanism.** Feature 382 (stock-deduction idempotency) owns the *ledger-write* idempotency rule; this feature is about the *transition guard* shape.
- **Any reservation / hold mechanism.** Feature 269 (`stockline`) already covers the atomic-reservation vocabulary, and feature 382 covers the business half of the shortfall question. **The reservation half is explicitly not re-picked.**
- **Any change to the FastAPI / SQLAlchemy / SQLModel / Postgres pins.**
- **Any adoption of `StockGuard`'s code.** Licence `null` — §3.2 strictly-incompatible. The transferable item is a **sentence and a constraint shape**, not a module.

## Description

### What `StockGuard` actually is

A **FastAPI + PostgreSQL + SQLAlchemy (async)** inventory-reservation and order service, containerised, 55 KB, zero stars, zero issues, created and pushed inside a single day on 2026-10-21. It resolves the classic e-commerce race — *"N buyers, M < N units, and nobody may buy a unit that isn't there"* — by claiming stock with **one conditional `UPDATE`**, so that *"check and write are one atomic step"*.

**There is no traction claim here and none is made.** ★0, 0 open issues, no topics, a same-day repository.

### The three claims worth taking

**Claim 1 — the guarded transition (the reason this pick exists).**

> *"Cancel / expire / pay can't double-release — **Every state change is `UPDATE ... WHERE status = 'ACTIVE'`, so exactly one transition wins**"*

Read precisely, this is a **single-statement conditional write**: the state change and its precondition live in **one** SQL statement, so there is no window between *"check the status"* and *"write the new status"* in which a second writer can slip in. The consequence is stronger than "we check first": it is *"**exactly one** transition wins"* — the losers affect **zero rows** and can be told so.

**This is precisely the primitive LE31 does not have**, and the gap is structural rather than incidental. LE31's only status column is `OrderItem.status`, and feature 379 established there is **no write site for it at all** — so there is currently nothing to guard. But features **03, 09, 15, 17, 30 and 45** all plan to move items through `ItemStatus`, and the first of them to write `status = ItemStatus.served` will be writing an **unguarded** transition, because LE31 has no shared helper that makes a guarded write the path of least resistance, and no database constraint as a backstop.

**Claim 2 — the constraint as a backstop.**

> *"**Safety net if app code is wrong** — `CHECK (reserved <= stock)`, `CHECK (stock >= 0)` constraints: the DB refuses to commit an oversold state"*

The two-layer structure is the transferable part: the *application* guards the transition, and the *database* refuses to commit a state the application should never have produced. **LE31 has neither layer.** `grep -rn "CHECK\|check_constraint\|Constraint" backend/` returns nothing.

**Claim 3 — the deliberately-broken control (recorded, not the reason for the pick).**

> *"`naive` — Read, check, write an absolute value — **Intentionally broken** (lost update). Exists so the load test can show what overselling looks like. Never use in production"*

A **production-shaped service that ships an intentionally broken strategy so a load test can demonstrate the failure it prevents** is a genuinely valuable testing practice, and LE31 has no equivalent. Recorded as a testing-vocabulary item, **not** as part of this feature's scope.

### ⭐ Why this is `defer` and not `build` — the unmade question

**The constraint's sign is undetermined, and two in-window artifacts disagree.**

| Artifact | Position on a negative derived balance | Quote |
|---|---|---|
| `hemeshwar09/StockGuard` | **The database refuses to commit it.** | *"`CHECK (stock >= 0)` constraints: the DB refuses to commit an oversold state"* |
| `fortikday/pantry-signal` (Pick B, same window) | **It is allowed, and flagged.** | *"**On hand:** received grams minus recorded recipe usage and logged waste. This is an estimate and **can become negative when records are incomplete**."* |

Both are competent, in-window, MIT-or-open, Python, restaurant-domain artifacts. **One makes the database refuse; the other lets the number go negative and marks it as an estimate.** These are not two implementations of one policy — they are **two different policies**, and they disagree about what the owner should see.

LE31 has **never chosen**. Feature 382 records the *business* half of the shortfall question; the *storage* half — whether a negative derived balance is representable at all, and whether the database is the right place to enforce it — **is still open and is not answerable from the existing feature tree.**

**Adopting either sign silently would smuggle a business decision into a technical change**, which is exactly what `le31-conventions` forbids: *"When sources conflict, stop and expose the exact conflict. Do not silently pick the newest-looking or easiest rule."*

### Why this is not a duplicate of feature 388

Feature 388 (`le31-table-state-machine-first-party-…`, filed 2026-10-27) is the **table** state machine: `Table` has no `status` column, so a second seat opens a second `Visit`. Its fix is **a column plus a guard in the seat route**.

This feature is a **different** thing: the **guarded-write primitive itself**, plus the **database-constraint layer**, plus the **negative-balance question**. The proofs:

- `grep -ril "guarded transition\|conditional update\|exactly one transition\|where status" features/` → **NO OUTPUT across all 423 pre-existing feature files**. Nothing in LE31's tree names this primitive.
- `grep -rn "CHECK\|check_constraint\|Constraint" backend/` → **NO OUTPUT**. The constraint layer is absent from the implementation, not merely from the prose.
- Feature 388's own scope is explicitly the `Table` entity and the seat route; it does not name `OrderItem.status`, does not name a database constraint, and does not ask the negative-balance question.

**Adjacency, recorded, not bundled:** feature 388's guard would be the *first* consumer of this primitive if it were built, and feature 379's transition log would be the *first* consumer of its attribution half. **This feature does not pre-empt either.**

### A genuine duplicate, explicitly NOT re-picked

**Feature 269** (`D-L-Narayana-stockline`, 2026-10-09) already records the **reservation** vocabulary verbatim: *"Atomic stock reservation, idempotent orders, optimistic locking, append-only ledger."* Its Goal section explicitly states that the idempotency and optimistic-locking primitives are *"OFF LE31 v1 today"* and apply *"to any future v1 polish that adds concurrent waiter-write protection."*

**The reservation half of `StockGuard` is therefore NOT picked.** What remains genuinely new after feature 269 is exactly: **the guarded conditional transition**, **the database-constraint backstop**, and **the deliberately-broken control strategy**. The report's candidate list contains 55 repos; this is the only new shape among them that feature 269 does not already cover.

## Data model

**No data model change. This feature changes zero lines of `backend/app/models.py`.**

For reference, the *shape* it is recording — explicitly **not** proposed as an implementation today:

```
GuardedTransition(table, pk, status_column, expected_from_state)
  -- a write is expressed as:
  --   UPDATE <table> SET <status_column> = :new
  --   WHERE id = :id AND <status_column> = :expected_from_state
  -- and is considered to have WON if and only if it affected exactly one row.
  -- Zero rows affected == the transition was not legal at the time of the write.
```

The two questions that are **deliberately unanswered** by this feature:

1. **Which entity does the first guarded transition apply to?** `OrderItem` (feature 379's subject) or `Table` (feature 388's subject)? — *feature 379 and 388 own this; this feature does not decide.*
2. **Does a `CHECK` constraint exist, and with which sign?** — *the unmade question above. **Not decided here.***

## Implementation

**No implementation steps. This feature is a `defer` vocabulary artifact.**

What a future implementer would need, and what this feature deliberately does **not** specify, is recorded so the shape is not lost:

- **One shared write helper** that expresses a transition as a single conditional statement and reports *"won"* vs *"lost"*, with **no caller able to bypass it** (feature 379 already requires *"one single write path"*; this primitive is how that path is made safe).
- **A database constraint** — **once the sign is decided.**
- **A regression test** that issues the same transition twice concurrently and asserts that **exactly one** succeeded and **zero** extra rows exist.
- **A transition attempt must be visible** to the surface that made it, so a lost transition is a *refusal the user sees*, not a silent no-op. (This is the same principle as feature 388's HTTP 409 carrying the existing `visit_id`.)

**None of the above is in this feature's scope today**, because all of it depends on the sign question being answered first.

## Telegram interaction

**None. No bot, no command, no surface change.**

Rationale, recorded so it is not re-litigated: the cook Telegram bot is LE31's staff-facing surface for **kitchen work** (fire, ready, serve). A *refused* transition is an **error path** on an existing waiter-UI or bot action — it does not introduce a new interaction. When the first guarded transition is built, its refusal **must** be visible on whichever surface made the attempt (the waiter web UI for table/order actions, the cook bot for kitchen actions), but **this feature adds no Telegram surface of its own**.

## Dependencies

- **Feature 388** (`le31-table-state-machine-first-party-…`, 2026-10-27) — the table state machine. **Read first.** Its seat guard would be the first consumer of the guarded-transition primitive, and its contract must not be re-litigated here.
- **Feature 379** (`le31-order-item-transition-actor-attribution-first-party-…`) — the transition attribution log. It establishes that **no write site for `OrderItem.status` exists today**; this feature's *"cheap now"* argument depends on that fact remaining true.
- **Feature 382** (`dc-tech-inc/dotnet-pos-integration`, 2026-10-26) — stock-deduction idempotency and the shortfall rule. Owns the **business** half of the negative-balance question.
- **Feature 269** (`D-L-Narayana-stockline`, 2026-10-09) — the reservation vocabulary. **Already owns the reservation half; not re-picked.**
- **Feature 374** (`le31-qty-remaining-derived-not-stored-…`) — `qty_remaining` stored-vs-derived. Owns the *"should the number be stored?"* half of the stock-model question.
- **Charter §3.3** (stock is derived from entries), **§3.1** (operational transitions are explicit user actions), **§3.5** (do not silently send, serve, close, or reconcile), **§3.2** (fixed stack; licences).
- **`skills/le31-conventions/SKILL.md`** — the seven-check feature gate and the *"when sources conflict, stop and expose the exact conflict"* rule that produced this `defer`.

## Open questions

1. **⭐ THE UNMADE QUESTION — may a derived stock balance be negative?**
   - **Option A (StockGuard):** *the database refuses to commit it.* A `CHECK (stock >= 0)` constraint makes an oversold state unrepresentable. Consequence: a bug that would produce a negative balance instead **fails loudly** — but it also means the system **cannot represent** an honest "we are short" state, and a legitimate shortfall (feature 382's case) must therefore be modelled **somewhere other than the balance**.
   - **Option B (pantry-signal):** *it is allowed, and flagged.* The derived balance may go negative when records are incomplete, and the system **marks it as an estimate** rather than refusing it. Consequence: the owner sees the true arithmetic, and the UI carries the burden of communicating *"this number is not trustworthy right now."*
   - **Neither is LE31's.** This is an **owner/charter decision**, and it is **not** answerable from the existing feature tree. **Until it is made, no `CHECK` constraint should be written** — because whichever sign a contributor happens to pick first becomes the de-facto policy.
2. **Which entity gets the first guarded transition** — `OrderItem` or `Table`? Features 379 and 388 own this; this feature does not decide.
3. **Is the database the right enforcement layer at all**, or should the guarantee live purely in the application helper? (`StockGuard` does both; LE31's charter has no position.)
4. **What does a *lost* transition look like to the surface that attempted it** — a refusal with the current state, a silent no-op, or a retry? (Feature 388's HTTP-409-with-`visit_id` is the precedent; consistency across surfaces is not yet stated.)
5. **Does the deliberately-broken-control-strategy practice belong in LE31's test vocabulary?** Recorded, not decided.

## Why this matters

**Because LE31's safety claims are currently enforced only by the discipline of whoever writes the next line of code — and there is no backstop under that discipline.**

Every LE31 invariant that concerns *state* (§3.1's *"operational transitions are explicit user actions"*, §3.3's *"current stock is derived from entries"*) is currently upheld by application code alone. There is **no database constraint anywhere in LE31** and **no guarded write anywhere in LE31**. The seat-endpoint defect found and **reproduced by execution** on 2026-10-27 (feature 388) is the visible instance of that; it is not the only possible instance, it is merely the one that happened to be reachable in the shipped code.

The cost profile is unusually favourable and unusually time-sensitive:

- **Cheap now:** one helper, one constraint, one regression test.
- **Expensive after:** the first unguarded transition writes a fact that cannot be un-written. `StockEntry` is append-only by charter, so a wrongly-recorded sale is **permanent and auditable** — the ledger will look perfectly well-formed (both foreign keys non-null, both pointing at real rows) while being **wrong**. Recovering from that requires a historical audit with **no ground truth** to audit against, which is precisely the failure mode of feature 374's `qty_remaining` and feature 385's `OrderItem.batch_id`.

**And the decision that gates it is cheap to make and expensive to defer.** A five-minute conversation with the owner settles the sign. Until then, the risk is not that LE31 writes the wrong constraint — it is that **somebody writes one without noticing there was a question**, and the codebase inherits a policy nobody chose.

## Evidence

- **Evidence class:** **OBSERVED** for the state of LE31's code (three greps, quoted above, run by the parent against `backend/` on 2026-10-28). **Reported** for the shape (one in-window external artifact, ★0, no traction).
- **Confidence:** **high** for the gap's existence; **low** for the demand (no operator has reported being harmed by it — and nothing could, because no unguarded write site exists yet).
- **Raw artefacts:** `/tmp/le31-daily-2026-10-28/gh/pv/hemeshwar09__StockGuard.json`, `/tmp/le31-daily-2026-10-28/gh/readmes/hemeshwar09__StockGuard.md`.
- **Report:** `/opt/data/le31-daily-research-2026-10-28.md`.
- **Parent verification scripts:** `/opt/data/le31-verify-2026-10-28/rederive.py`, `rank.py`.
