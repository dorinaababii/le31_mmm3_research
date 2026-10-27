# Feature 388 — `Table` has no status column, so a second seat opens a second `Visit`: the floor's view of the room silently loses a party

> **Pick A of Daily Research 2026-10-27 (89th pass).** **FIRST-PARTY, AND THE DEFECT WAS REPRODUCED BY EXECUTION ON 2026-10-27 — not inferred from reading code.**
>
> The parent ran LE31's real router against a throwaway SQLite DB and issued two identical `POST /api/tables/1/seat` requests. **Both returned HTTP 200. Two open `Visit` rows existed afterwards (`ids [1, 2]`). The derived table status still reported only `"seated"` — so one party became invisible.** Transcript: `/opt/data/le31-verify-2026-10-27/seat_observation.json`; reproduction script: `/opt/data/le31-verify-2026-10-27/observe_seat.py`.
>
> **Root cause:** `Table` has **no `status` column**. `TableStatus` *is* defined in `backend/app/models.py` (line 27) with five states (`free`, `seated`, `ordered`, `billed`, `dirty`) — but it is **never stored on `Table`**. `grep -n "status" backend/app/models.py` returns exactly one hit, and it is `OrderItem.status` on line 151. `backend/app/routers/tables.py` line 50 carries the developer's own note: `# TODO: reject if table is not FREE (need TableStatus column on Table)`.
>
> **This is a specification defect, not only an implementation bug.** `features/01-table-management.md` lists its data model as `Table (id, label, section, seats, x, y)` — **the status column is missing** — while its own Description says *"Tap a **free** table → 'Seat party' → enter `party_size`, `adults`, `children` → confirm."* The implementation faithfully follows the data model, and therefore *cannot* enforce the rule the Description states. LE31's **own cited reference** disagrees with its own feature contract: `research/01-pos-systems.md` line 27 gives the peer model as `Table (id, seats, section, **status**)`, and line 19 gives the peer state machine as `free → seated → ordered → billed → paid → free`.
>
> **Trigger (external, in-window):** `adil-alzhan-dev/kumo-qr-ordering` (created 2026-10-24, in-window) states *"A lost connection never creates a duplicate order: each order carries a key."* — and the Zenodo paper *"A Reliable Event-Reconciliation Framework for Real-Time Restaurant Order and Inventory Synchronization"* (2026-10-23, DOI `10.5281/zenodo.23572532`) prescribes *"**order-state validation**"* as a distinct concern alongside *"duplicate-event detection"*. **Three independent arrivals in three passes** (yesterday's `dc-tech-inc/dotnet-pos-integration` ADR-0001 *"idempotency-in-the-database"*, `kumo-qr-ordering`'s order key, and this paper) name the same hazard: a state-changing endpoint that is retried must not create a second state.
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed), confidence **high** for the defect, **low** for the demand (the *frequency* of a double-tap in production is not evidenced and is not claimed).

## Goal

Make the floor's view of the room **true**: one table, one open party, one `Visit`. When the waiter taps "Seat party" on a table that is already seated, LE31 must **refuse** the transition and say so, instead of silently opening a second `Visit` that no surface displays.

The concrete outcome: **`POST /api/tables/{id}/seat` on a non-free table returns an error (HTTP 409) carrying the existing `visit_id`, and creates no row.**

## Scope

**In scope (v1):**

- **One stored source of truth for table state.** Add `status: TableStatus = TableStatus.free` to `class Table` in `backend/app/models.py`, and make the stored column the **authoritative** value.
- **A guard on the seat transition.** `POST /api/tables/{id}/seat` must check the table's stored status and **refuse** (HTTP 409) when the table is not `free`, returning the existing `visit_id` so the UI can show the party that is already there.
- **The seat transition sets the state.** A successful seat moves the table to `seated`.
- **A release path.** A route or service call that returns a table to `free` when its visit closes — so the table does not become permanently unseatable. (The charter's feature-01 flow ends a visit on billing; feature 02 owns order taking and feature 14/05 own the bill. **This slice supplies the release; it does not re-implement billing.**)
- **One edit to `features/01-table-management.md`** so the contract and the code agree on the data model.
- **A regression test** that fails on today's code and passes on the fixed code.

**Explicitly NOT in scope:**

- The full five-state machine (`ordered`, `billed`, `dirty`) as *transitions*. Only `free → seated` and `seated → free` are implemented. The other three states exist as enum values and are **not** wired.
- Any change to `Visit`, `OrderItem`, `StockEntry`, `Bill`, `DerivedTip`, `Shift`, `Batch` or `MenuItem`.
- Any waiter-UI change beyond what the API response implies (the UI is `index.html`, feature 01's scope; **this slice does not restyle it**).
- Any Telegram bot change.
- **Auth.** `server_id: int = 1,  # TODO: from auth token` (line 39) is a separate, untouched TODO.
- Payment, reservations, delivery, guest QR ordering — all §3.2 non-goals.
- **Reconciling pre-existing duplicate `Visit` rows** in a live database. See Open questions.

## Description

### The defect, as observed in LE31's own code on 2026-10-27

`backend/app/routers/tables.py` today:

```python
@router.post("/{table_id}/seat")
def seat_party(table_id: int, party_size: int, adults: int, children: int = 0,
               server_id: int = 1,  # TODO: from auth token
               session: Session = Depends(get_session)) -> dict:
    """Seat a party at a table → opens a new Visit."""
    table = session.get(Table, table_id)
    if not table:
        raise HTTPException(404, "Table not found")
    if party_size < 1 or adults < 1:
        raise HTTPException(400, "Need at least 1 adult")
    if adults + children < party_size:
        raise HTTPException(400, "adults + children must cover party_size")
    # TODO: reject if table is not FREE (need TableStatus column on Table)
    visit = Visit(table_id=table_id, server_id=server_id, ...)
    session.add(visit)
    session.commit()
```

Every validation present checks the **party size**. **None checks the table.** The `# TODO` at line 50 is the developer's own statement of the gap, including the reason: the column does not exist.

`Table` (models.py line 64) declares `id, label, section, seats, x, y` — and no status.

`TableStatus` (models.py line 27) declares the five states. `_table_status()` (routers/tables.py line 64) *derives* a status from the latest open `Visit`:

```python
def _table_status(table_id: int, session: Session) -> str:
    visit = session.exec(
        select(Visit).where(Visit.table_id == table_id, Visit.closed_at == None)
    ).first()
    if not visit:
        return TableStatus.free.value
    return TableStatus.seated.value  # could be 'ordered' / 'billed' with more checks
```

`.first()` on an unordered result set returns *one* of the open visits. **The second party is not shown, not counted, and not billable** — it exists only as a row.

### The observed run (2026-10-27, parent-run, real router, throwaway DB)

```
-- GET /api/tables (initial: table free) --
   HTTP 200 [{'id': 1, ..., 'status': 'free'}]

-- POST /api/tables/1/seat  (first tap) --
   HTTP 200 {'visit_id': 1, 'table_id': 1}
   open Visits after 1st POST: 1  -> ids [1]

-- POST /api/tables/1/seat  (SAME table, second tap / double-submit) --
   HTTP 200 {'visit_id': 2, 'table_id': 1}
   open Visits after 2nd POST: 2  -> ids [1, 2]

-- GET /api/tables (derived status) --
   HTTP 200 [{'id': 1, ..., 'status': 'seated'}]

   Visits belonging to table 1: 2 -> ids [1, 2]

VERDICT: DEFECT_REPRODUCED
```

**Both requests succeeded.** The API reported two different `visit_id`s for one table. The floor grid shows one yellow tile.

### Why this one is different from the other two open first-party findings

Feature 374 (`Batch.qty_remaining` is a stored number that drifts) and feature 385 (`OrderItem.batch_id` missing) both describe defects in **code that does not exist yet**. LE31's backend is a **318-LOC skeleton with three routes** (`/api/health`, `/`, and the startup hook) plus `routers/tables.py` — every P0 in the charter's acceptance table is specified but unbuilt. Those findings are therefore *specification* gaps, and their fixes require a charter decision and a migration.

**This one is reachable in the shipped code today.** The seat endpoint exists, the `Table` and `Visit` models exist, and the defect is one HTTP request away. Its fix is also **the cheapest of the three**: one column, one guard, one test, one contract edit — no charter decision, no semantics to invent.

### Why an external artifact was the trigger

Three in-window artifacts, three different authors, three different stacks, one agreed hazard:

| Artifact | Date | Stack | Its words |
|---|---|---|---|
| `dc-tech-inc/dotnet-pos-integration` ADR-0001 | 2026-10-22 | C#/.NET + SQL Server | *"idempotency-in-the-database"* — *"There is no 'have I seen this?' read in application code, so there is no check-then-act race."* |
| `adil-alzhan-dev/kumo-qr-ordering` | 2026-10-24 | Next.js/NestJS/PostgreSQL | *"A lost connection never creates a duplicate order: each order carries a key."* |
| Zenodo 10.5281/zenodo.23572532 | 2026-10-23 | React/Node/Express/MySQL/Socket.IO | *"**order-state validation**"*, *"duplicate-event detection"*, *"persistent event tracking"* |

The first is a *ledger-write* rule (feature 382's subject). The second is an *order-submission* rule. **This feature is the third thing: an order-state rule — is this transition legal right now?** That is a different question from "has this event been seen before", and it is a question LE31's seat endpoint does not ask.

## Data model

**Change — `backend/app/models.py`, `class Table` (line 64):**

```python
class Table(SQLModel, table=True):
    __tablename__ = "table_"  # 'table' is a SQL reserved word

    id: int | None = Field(default=None, primary_key=True)
    label: str
    section: str = "main"
    seats: int = 4
    x: int = 0        # for floor map coords
    y: int = 0
    status: TableStatus = TableStatus.free   # <-- ADDED: single source of truth
```

`TableStatus` already exists (line 27) and is already imported by `routers/tables.py` (line 10) — **no new enum, no new import in `models.py`**.

**Change — `features/01-table-management.md`, Data model block:**

```
Table          (id, label, section, seats, x, y, status)  -- x/y for floor map
Visit          (id, table_id, server_id, opened_at, closed_at,
                party_size, adults, children)
```

**No change to `Visit`.** The relationship stays one-table-to-many-visits in the schema — but **one-table-to-one-OPEN-visit as an invariant**, enforced in code, which is the point.

**Note on `TableStatus` as a SQL column:** `TableStatus` is a `str, Enum` (`class TableStatus(str, Enum)`), so SQLModel stores it as a VARCHAR. **Do not** convert it to a native database ENUM — SQLite (dev) and Postgres (prod) must accept the same schema per §3.1, and a native ENUM does not port between them.

**Note on the derived helper:** `_table_status()` must be **rewritten** to read the stored column, not to keep deriving from `Visit`. Two sources of truth that can disagree is the exact failure the pre-mortem names. The derived form may be kept **only** as a consistency assertion in a test, never as the display source.

## Implementation steps

**Order matters: the spec is corrected before the column, and the column before the guard.**

1. **`features/01-table-management.md`** — update the `Table` data-model line to include `status`; add one sentence to the Description stating that seating a non-free table is refused (HTTP 409) with the existing `visit_id`. **Do not restructure the feature, do not renumber it, do not add the other three states as transitions.**
2. **`PROJECT_CHARTER.md`** — **no change is required for this slice.** If you touch the charter, the only permitted edit is a pointer to this feature; the charter's §4 data-model list already describes `Table` generically. **Do not** add a table-state machine to the charter in this slice — that is scope creep.
3. **`backend/app/models.py`** — add `status: TableStatus = TableStatus.free` to `class Table`. **Do not** touch any other class, field or timestamp.
4. **`backend/app/routers/tables.py`** —
   - `seat_party`: after the 404/400 checks, read `table.status`; if it is not `TableStatus.free`, find the open `Visit` for that table and raise `HTTPException(409, ...)` including its id. **Do not** create a `Visit`. On success, set `table.status = TableStatus.seated` **in the same transaction** as the `Visit` insert, then commit once.
   - `_table_status`: return the **stored** `table.status`; stop deriving from `Visit`. **Keep the function** (the UI and the JSON shape depend on the `status` key) — change only its body.
   - **Add the release path.** Where the visit is closed, set the table back to `free`. **Look first** — if no route closes a visit yet (parent-verified: `backend/app/routers/` contains only `__init__.py` and `tables.py`, and `Visit.closed_at` is set nowhere in the shipped code), then **do not invent a billing flow**. In that case: expose a small `POST /api/tables/{id}/release` that closes the open visit and frees the table, and record in the contract that the billing flow will call it. **If you find yourself writing a bill-closing endpoint, stop — that is feature 14/05's job.**
5. **`backend/app/db.py`** — verify `init_db()` creates the altered table via SQLModel `create_all`. **Do not assume.** Per §3.2 v1 uses `init_db()`, not Alembic; `requirements.txt` already pins `alembic>=1.13` but **do not silently introduce Alembic** — follow the stated v1 policy and record the prod-migration step as known debt.
6. **`tests/test_table_seat_guard.py`** — **NEW.** The load-bearing tests (below).
7. **`backend/app/routers/tables.py` line 39** — the `# TODO: from auth token` comment stays. **Out of scope.**

## Telegram interaction if any

**None.** The cook bot (`backend/app/bot/cook_bot.py`) does not seat tables and this slice adds no command.

The only user-visible surface is the waiter web UI's seat action, which will now receive an HTTP 409 instead of a false success. **The UI change itself is feature 01's scope**; this slice changes the API contract it depends on.

## Dependencies

- `features/01-table-management.md` — **the contract this slice corrects and implements.** Its own states list (`free`, `seated`, `ordered`, `billed`, `dirty`) is the vocabulary.
- `features/02-order-taking.md` — every seated visit becomes an order. **This slice does not implement ordering**, but a visit created here is the row feature 02 will hang orders from.
- `features/05-*.md` / `features/14-*.md` — the bill, which is what eventually closes a visit. **Not implemented here.**
- `research/01-pos-systems.md` — **the cited reference that already has the column.** Line 27: `Table (id, seats, section, status)`. Line 19: `free → seated → ordered → billed → paid → free`. This feature closes the gap between LE31's feature contract and LE31's own reference.
- `PROJECT_CHARTER.md` §3.1 — *"Operational transitions are explicit user actions"* — the rule this feature enforces.
- `PROJECT_CHARTER.md` §3.2 — the §3.2 non-goals that keep this slice small (no reservations, no delivery, no online ordering).
- **Feature 382** (`dc-tech-inc/dotnet-pos-integration`) — the *ledger-write* idempotency rule. **Different scope. Do not bundle.** This feature asks *"is this transition legal?"*; feature 382 asks *"has this event been seen?"*.
- **Feature 374** (`Batch.qty_remaining`) and **feature 385** (`OrderItem.batch_id`) — the other two open first-party findings. **All three are open; this one is the cheapest and the only one reachable in shipped code today.**

## Open questions

1. **Should the stored column be the single source of truth, or should the *derived* form be?** This slice says **stored**. The alternative — a partial unique index on `(table_id) WHERE closed_at IS NULL` — is stronger (the database refuses the second row) but is **not portable to SQLite** the way §3.1 requires, and Postgres partial indexes are a different schema object to migrate. **Decided here: stored column + application guard, with the database-level constraint recorded as future work.** Do not implement the partial index in this slice.
2. **What happens to duplicate `Visit` rows that already exist?** A live database could already contain two open visits for one table. **This slice does NOT merge, close or delete them** — that is a data migration with product judgement in it. The guard prevents new duplicates; existing ones are an operational cleanup the owner must confirm. **Decided: out of scope, explicitly named.**
3. **Who calls the release?** If no billing route exists yet, feature 01's flow has no way to free a table. The minimal `POST /api/tables/{id}/release` is provided for that purpose, but **the real bill-closing path belongs to features 05/14**. **Decided: provide the release primitive; do not build the bill.**
4. **Does `free → seated` also need to be atomic with the `Visit` insert?** It should be one transaction. **Decided: yes** — a crash between the two would leave a seated table with no visit, which is the same class of silent inconsistency this feature fixes. Use one `session.commit()`.
5. **Should the 409 body carry the existing `visit_id`?** **Decided: yes.** The waiter needs to know *which* party is already there, and a bare "409" makes the UI's recovery worse, not better. This is the only decision here that changes the API's usefulness to the operator.

## Why this matters

**Because the failure is silent and the consequence is a real party with no bill.**

A double-tap on "Seat party" — on a tablet with a flaky connection, on a phone with a laggy touch handler, by a waiter who does not notice the first tap landed — creates a second `Visit` that **no surface ever displays**. The floor grid shows one yellow tile. The waiter's order screen (feature 02) will list the visit it fetches; the second one is not obviously the one it fetches. **When the bill is closed for that table, one party is seated, eating, and un-billed.** That is not a data-quality issue; it is money and service.

It is also the failure mode an owner cannot self-diagnose. There is no error, no red tile, no "table already seated". The floor looks correct. The problem is only discoverable by reconciling the `visit` table against the bills — and LE31 has no such reconciliation surface, because nothing else in v1 looks at `Visit` either.

**And the cost of waiting is asymmetric in the way that matters.** Today, with one restaurant and one route, the fix is a column and a guard. After the first real bill is closed and the first real order is taken, the *interpretation* of existing rows becomes ambiguous — you no longer know which of two visits was the real party, because both are open and both look valid. **Reconstructing that later requires a manual audit of live service history with no ground truth.** The information that makes the audit possible is the absence of duplicates, and the absence of duplicates is only knowable *before* the duplicates exist.

**Why it is the cheapest of the three open first-party findings.** Feature 374 and feature 385 both need a charter decision (what does "the active batch" mean?) and a migration with semantic consequences. This one needs: **one column, one guard, one release primitive, one test, one line in feature 01's data model.** No new concept, no new vocabulary, no new dependency, no third-party licence question, no traction question — **the subject is LE31's own code, and the defect has been executed and observed.**

**Why the evidence is strong enough to build on, and the demand is not.** The *defect* is OBSERVED — HTTP 200 twice, two `Visit` rows, one yellow tile. The *demand* is LOW-confidence — LE31 has one restaurant and no traffic, so the frequency of a double-tap is unknown. Those are different claims and the contract keeps them apart: the defect is real and reproducible, the urgency is a judgement. The reason to build now is not that operators are complaining (no report of that exists in this window or any prior one); it is that **the fix is cheap, the failure is silent, and the information needed to repair it later will not exist later.**
