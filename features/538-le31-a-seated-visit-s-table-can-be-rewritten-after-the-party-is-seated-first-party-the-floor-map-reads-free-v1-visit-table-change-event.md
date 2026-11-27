# Feature 538 — A seated visit's table can be rewritten, and the table it left reads free while its order is still outstanding

> **Pick B of Daily Brainstorm 2026-11-27 (109th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema AND against LE31's own shipped `_table_status()` helper.**
>
> `backend/app/models.py`, `class Visit`, verbatim (lines 126–139):
>
> ```python
> class Visit(SQLModel, table=True):
>     __tablename__ = "visit"
>
>     id: int | None = Field(default=None, primary_key=True)
>     table_id: int = Field(foreign_key="table_.id")
>     server_id: int = Field(foreign_key="app_user.id")
>     opened_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     closed_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     party_size: int
>     adults: int
>     children: int = 0
> ```
>
> **`table_id` is a bare foreign key with no constraint, no history, and no write-path rule.** A seated visit's table is a fact — *this party is at table T1* — and nothing stops that fact from being rewritten.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with two tables — T1 with `seats=4` and T2 with `seats=2` — one server, one open visit at T1 with `party_size=2`, one served order line, one paid bill):
>
> ```
>   UPDATE visit SET table_id = <T2> WHERE id = 1        ->  ACCEPTED
>
>   open visits on T1 (closed_at IS NULL)  =  0
>   open visits on T2 (closed_at IS NULL)  =  1
>   the party's order lines are still on visit 1 (which now points at T2)
>   order lines on that visit             =  1
> ```
>
> **⭐ AND THE SHIPPED CODE READS EXACTLY THAT QUERY.** `backend/app/routers/tables.py`, lines 64–71, verbatim:
>
> ```python
> def _table_status(table_id: int, session: Session) -> str:
>     """Derive a table's current status from the latest open Visit."""
>     visit = session.exec(
>         select(Visit).where(Visit.table_id == table_id, Visit.closed_at == None)
>     ).first()
>     if not visit:
>         return TableStatus.free.value
>     return TableStatus.seated.value  # could be 'ordered' / 'billed' with more checks
> ```
>
> **⭐ TWO NUMBERS THAT SHOULD AGREE, DISAGREEING.** After the rewrite, **T1 has zero open visits** — so `_table_status(T1)` returns **`free`** — while **T1's party is still seated there**, with an order line on the visit and a paid bill attached to it. **The floor map says T1 is free. The guest is sitting at T1.** And because the visit now points at T2, **T2 reports `seated` for a party that is not there** — so a second party can be seated at T2 while the first party's order still lives on T2's visit row.
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all **570** feature contracts and **525** HANDOFFs (1,093 files) returns **zero hits** for a rule about the visit's *table* changing after the party is seated:
>
> | sweep | files | hits |
> |---|---|---|
> | `visit.{0,50}table_id.{0,60}(update\|rewrite\|mutab\|reassign\|mov(e\|ed))` | 0 | 0 |
> | `(move\|moving\|reassign\w*).{0,40}(the )?(party\|visit\|table)` — *scoped to a table-move rule* | 0 | 0 |
> | `table.{0,40}(assignment\|membership).{0,50}(change\|mutable\|rewrite\|fixed)` | 0 | 0 |
>
> **27** corpus files mention `visit.table_id` — the column is well discussed. **Not one of them is about the column changing.** The nearest neighbours each own a *different* half:
>
> | rule | mechanism | owner |
> |---|---|---|
> | **a second seat on an occupied table opens a second visit** | a stored `Table.status` column + an API guard | **feature 388** |
> | `party_size` vs `Table.seats` — does the party fit | a comparison at the seat | **feature 414** |
> | `party_size` vs `adults + children` — is the composition coherent | a comparison at the seat | **feature 423** |
> | the peak-party-count question | — | **feature 416**, `defer`red, **and it stays deferred** |
> | `Table.seats`' lower bound | a value check | **feature 501** |
> | the visit's **composition** (`party_size`, `adults`, `children`) after seating | an event table + a write-path guard | **feature 533** |
> | **the visit's table after seating** | **event table + write-path guard** | **THIS SLICE** |
>
> **⭐ AND 388 IS UPSTREAM-OF-FILED-WORK, IN BOTH DIRECTIONS.** Feature **388**'s own text says: *"**Note on the derived helper:** `_table_status()` must be **rewritten** to read the stored column, not to keep deriving from `Visit`. Two sources of truth that can disagree is the exact failure the pre-mortem names."* **This slice is the third half of that sentence.** 388 replaces the *derived* status with a *stored* one — which removes the derivation's fragility, and **leaves the stored `table.status` to disagree with the stored `visit.table_id`**, because nothing owns the relationship between them either. **If this slice has not landed, 388 will implement a stored status column that a later `visit.table_id` rewrite silently desynchronises** — and 388's own pre-mortem is about exactly that failure.
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed against LE31's real schema and against its own shipped `_table_status()`). Confidence: **high** for the defect, **low** for the demand (no operator has reported a moved table; no code path changes `table_id` today — there is no route that moves a seated party).
>
> The re-runnable probe is `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py`.

## Goal

Make a seated visit's **table** mean one thing: **the table this party is at, recorded when the party is seated, and afterwards a fact with a history.**

The concrete outcome: **the table of a visit that has been seated cannot be rewritten silently**, and where the domain genuinely requires it (the party is moved to another table — a real event in a busy restaurant), that move is **a recorded event** carrying the old table, the new table, the actor and the time, and **the two tables' states are moved with it in the same transaction**.

The single sentence this feature exists to make true: *a party is seated at a table; the table it is at is a fact with a history; and the floor map and the order always agree about which table that is.*

## Scope

- **One new table** — `VisitTableChange` — recording `visit_id`, `from_table_id`, `to_table_id`, `by_user_id`, `at`.
- **One write-path rule**: the table of a seated visit may be changed only through a helper, and only when the destination table is **free** — the same guard feature **388** applies to the seat path, expressed for the move path.
- **A refusal** when the destination table is not free, naming both tables and the destination's state.
- **An atomic state move**: the source table's state and the destination table's state are updated **in the same transaction** as the visit's `table_id`, so the floor map and the order never disagree even momentarily.
- **A regression test** that asserts a move to an occupied table is refused, that a permitted move writes exactly one change row with the old table, the new table, the actor and the time, and that **both** tables' states are consistent afterwards.

**The move is recorded in an event table, not by a `previous_table_id` column.** A column preserves one move and loses the second; feature **523** established that argument for the catalogue's price (*"a `previous_price` column preserves one change and loses the second"*), and the same argument applies here.

## Out of scope

- **The visit's composition** (`party_size`, `adults`, `children`). Feature **533** owns it and its own *Out of scope* says *"The capacity comparison — **feature 414**, filed. The composition comparison — **feature 423**, filed."* **This slice does not touch those columns and does not add a composition event.**
- **The visit's server.** Feature **451** owns the role rule at the write path; feature **443** owns the bill's closer against the visit's server. **This slice does not change `server_id`.**
- **`Table.status` — the stored column itself.** Feature **388** owns it, and this slice **must not add it, must not rename it, and must not change its enum.** Where this slice needs to move a table's state, it goes through **388's** stored column and **388's** guard; this slice does not re-implement either.
- **The `_table_status()` rewrite.** Feature **388** owns it. **This slice does not rewrite that function** — it adds the rule that keeps the stored value honest.
- **The capacity comparison** (`party_size` vs `Table.seats`). Feature **414** owns it, at the seat.
- **`Table.seats`' lower bound.** Feature **501** owns it.
- **The peak-party-count question.** Feature **416** owns it, it is `defer`red, **and it stays deferred.** This slice does not decide how many people may join a table and does not touch that question.
- **A second seat on an occupied table.** Feature **388** owns it.
- **The bill-close path.** Feature **415** owns it. The tip derivation — features **05** / **415**.
- **Any change to `OrderItem`, `MenuItem`, `Batch`, `StockEntry`, `Bill`, `Shift` or `DerivedTip`.**
- **A floor-plan, menu or waiter-UI change.** `index.html` is feature **08**'s scope and a thirteen-way collision zone. **The floor map's rendering of a moved party is a surface question, and the surfaces are not this slice's.**
- **Alembic**, except as noted in *Dependencies* for feature **446**.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The defect, as executed

The schema declares `table_id` as a bare foreign key. There is no `UniqueConstraint`, no `CheckConstraint`, no `ondelete` clause, and **no write path exists** that could enforce anything about it. The visit therefore names a table, and nothing stops that name from changing.

The executed probe seeded a coherent world and then made one change:

```
  table_  T1  label='T1'  seats=4  x=1  y=2
  table_  T2  label='T2'  seats=2  x=9  y=9
  app_user  server
  visit(id=1, table_id=T1, server_id=<server>, party_size=2, adults=2, children=0, closed_at=NULL)
  order_item(id=1, visit_id=1, menu_item_id=1, qty=2, unit_price=14.00, status='served')
  bill(id=1, visit_id=1, subtotal_items=28.00, total_due=33.60, total_paid=33.60, payment_method='cash')

  UPDATE visit SET table_id = T2 WHERE id = 1;        ->  ACCEPTED
```

and then read back the two numbers that must agree — the number of **open visits** per table, which is exactly what the shipped `_table_status()` counts:

| what | value after the rewrite | what it should say |
|---|---|---|
| open visits on **T1** (`closed_at IS NULL`) | **0** | **1** — the party is still at T1 |
| open visits on **T2** (`closed_at IS NULL`) | **1** | **0** — nobody is at T2 |
| order lines on the visit | **1** | 1 — the order travelled with the visit |
| `visit.party_size` | **2** | 2 |

**And the shipped helper's answer, computed by the same query it uses:**

```
  _table_status(T1)  ->  'free'      <-- the guest is sitting at T1
  _table_status(T2)  ->  'seated'    <-- nobody is at T2
```

### Why this is not a cosmetic row edit

Three concrete consequences follow from the rewrite, and **each is a behaviour of LE31's shipped code**, not a hypothetical:

1. **T1 reads `free` on the floor map** while a party is sitting at it with an order outstanding. The waiter sees an available table and may seat a second party there — **feature 388's exact failure**, arriving by a different route than the one 388 closes.
2. **T2 reads `seated`** for a party that is not there, so the floor map shows a false occupancy. Every KPI derived from "open visits per table" is now wrong.
3. **The order lines moved with the visit, not with the table.** The lines are on `visit_id = 1`, and the visit now says T2 — so the kitchen's ticket for T1's order is now attributed to T2. **A dish prepared for T1 is served at T2.**

### Why the rule is "a seated visit's table is a fact"

The charter's P0 row 42 is *"Waiter can seat a party at any free table and capture `party_size`, `adults`, `children`."* **The seat is the moment the table is chosen**, and it is the moment the table stops being free. A table is not a property of the *visit* that may be edited — it is the *place* the party occupies, and a party occupies one place at a time.

**The domain does have a real move event**: in a busy restaurant a party is moved from T1 to T2 because T1's neighbours are having a noisy conversation. **That event is real, and the contract does not forbid it** — it makes it a **recorded, guarded** event rather than a silent column edit. The rule is not *"the table may never change"*; it is *"when the table changes, it changes with a record and with the floor map moved in the same breath."*

### Why the destination guard is 388's, reused

A move to a table that is **occupied** is the same mistake as a seat at an occupied table: two parties, one table. Feature **388** owns that refusal for the seat path and states the shape of its refusal: *"read `table.status`; if it is not `TableStatus.free`, find the open `Visit` for that table and raise `HTTPException(409, ...)` including its id."*

**This slice reuses that rule and does not re-implement it.** The implementer of 388 must not add a move guard and the implementer of this slice must not add a seat guard. **They are the same refusal at two different entry points**, and the corpus's rule is that a second entry point must reach the same helper.

### Why the state move must be atomic

The move changes three things at once: the visit's `table_id`, the source table's status and the destination table's status. **If those are three writes and one of them fails, the floor map and the order disagree** — which is the very defect this feature exists to remove, reproduced one level down.

The move must therefore be **one transaction**: the visit's `table_id` and both tables' statuses are written together, and a failure rolls all three back. **The implementer must not write a helper that commits between them.**

### Why an event table and not a guard alone

A guard that refuses a move to an occupied table is necessary but not sufficient:

1. A move to a **free** table is legitimate and **must be possible** — the domain has the event.
2. When it happens it must be **visible afterwards**: which table the party was at, which it is at now, who moved them and when.
3. The rule must survive the **read side**: a reader that asks *"where is this party?"* must be able to see that the party was moved, and when.

A `previous_table_id` column satisfies (1)–(2) once and fails on the second move: it preserves one move and loses the second. Feature **523** already made this argument for the catalogue's price; the same argument applies here.

### The actor

The actor is a **staff** member (`app_user`), never a guest — consistent with charter §3.1 (v1 stores counts, not guest identities) and with the corpus's actor convention as recorded in feature **417**'s schema note: *"every actor field carries a foreign key."* `by_user_id` is **nullable** with a foreign key, the same form features **379** and **417** specify.

## Data model

```python
# backend/app/models.py — ADD, do not modify any existing class

class VisitTableChange(SQLModel, table=True):
    """A seated visit was moved from one table to another. Append-only."""
    __tablename__ = "visit_table_change"

    id: int | None = Field(default=None, primary_key=True)
    visit_id: int = Field(foreign_key="visit.id", index=True)
    from_table_id: int = Field(foreign_key="table_.id")
    to_table_id: int = Field(foreign_key="table_.id")
    by_user_id: int | None = Field(default=None, foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

Notes the implementer must honour:

- The class name and table name follow the corpus's convention: **`visit_table_change`**, in the pluralised snake style of `stock_entry` and `order_item`.
- `by_user_id` is **nullable** with a foreign key — the corpus's actor convention, applied a fourth time (features **379**, **417** and this slice).
- **Do not add a `UniqueConstraint`** on `(visit_id, …)`. A party may be moved more than once; a constraint would forbid the second move.
- **Do not add a column for the tables' statuses.** The statuses live on `table_.status` — feature **388**'s column — and this slice reads and writes it **through 388's rule**, never duplicates it.

**Migration path.** `PROJECT_CHARTER.md` §3.2 says v1 uses `init_db()` rather than Alembic, and `create_all()` **cannot alter an existing table** — but this slice **adds** a table and **changes no existing column**, so `create_all()` is sufficient for a fresh database. **If the deployment has an existing database, feature **446** owns the migration path and this slice must not invent one.** If feature **388** has already added `table_.status`, that column's own migration is 388's and 446's business — **this slice adds nothing to that table.**

## Implementation

1. **`backend/app/models.py`** — add `class VisitTableChange` exactly as specified above. **Do not touch `Visit`, `Table`, `AppUser`, `OrderItem`, `Bill`, `Batch`, `StockEntry`, `Shift` or `DerivedTip`.**
2. **The move helper** — one function, `move_visit_to_table(session, visit_id, to_table_id, actor_id)`, which:
   - loads the visit and the destination table;
   - **refuses** when the destination is not free, raising a legible error naming both tables and the destination's state (**388's rule, reached through 388's helper — not re-implemented here**);
   - writes **one** `VisitTableChange` row;
   - sets `visit.table_id = to_table_id` **and** updates the source table's status and the destination table's status;
   - commits **once**.
3. **The helper is the only writer of `visit.table_id` after the visit is created.** A grep for `table_id =` under `backend/` must return the seat path and this helper, and nothing else. **Record the grep output in the PR description** — a rule with two writers is not a rule.
4. **Regression tests** — at minimum:
   - a move to an **occupied** table is **refused**; the visit is unchanged; **zero** `VisitTableChange` rows exist;
   - a move to a **free** table is **accepted**, writes exactly **one** change row with the old table, the new table, the actor and the time, and leaves **both** tables in the right state;
   - a **second** move produces a **second** row — the case a `previous_table_id` column would have lost;
   - a move to a table that **does not exist** is refused.
5. **The consistency assertion** — a test that, for every `VisitTableChange`, asserts the visit's current `table_id` equals the **latest** change's `to_table_id`, and that no open visit exists on a table whose status is `free` (and vice versa) — **the shipped `_table_status()`'s question, asked of the stored column.** This is a **test**, not a second source of truth.

**The implementer must not guess at step 2's package location.** LE31 has **no `services/` package** today (`backend/app/` holds `models.py`, `main.py`, `routers/`, `bot/`). Feature **441** says it *"supplies the rule and the helper"* and feature **421** supplies *"the single write path"*; whichever lands first **creates** the package. **If `backend/app/services/` does not exist when you start, create it — and say so in the PR.** Do not put the helper in `routers/`: it is not a route.

## Telegram interaction

**None.** The waiter UI is `index.html`, feature **08**'s scope and a thirteen-way collision zone. This slice changes **no** surface.

The refusal is raised at the write path and reaches whichever surface eventually calls the helper — and **the helper's error must be legible**, because a surface that cannot express the refusal will swallow it. That is feature **486**'s problem, not this slice's, and it is recorded in *Dependencies*.

The **cook bot** (`backend/app/bot/cook_bot.py`) is untouched. A table move is a floor-floor event; the cook's flow is feature **469**'s and feature **380**'s territory.

## Dependencies

- **Feature 388 (the table state machine and the stored `Table.status`) — ⭐ UPSTREAM-OF-FILED-WORK, IN BOTH DIRECTIONS.** 388 owns the stored column, the seat guard and the `_table_status()` rewrite. **This slice must not add the column, must not add the guard and must not rewrite the helper.** 388's own text is the reason: *"Two sources of truth that can disagree is the exact failure the pre-mortem names."* **388 replaces the derived status with a stored one — and leaves the stored status to disagree with the stored `visit.table_id`, because nothing owns the relationship between them.** **The two must be designed together, and this slice states the rule the stored column needs.**
- **Feature 414 (`party_size` vs `Table.seats`) — adjacent, not blocking.** 414 owns the capacity comparison **at the seat**. **A move to a table that cannot hold the party is a different question from a seat at a table that cannot hold the party** — and the contract records that question in *Open questions* rather than deciding it.
- **Feature 423 (`party_size` vs `adults + children`) — untouched.** A different comparison, at the same moment.
- **Feature 533 (the visit's composition change event) — adjacent, same table, same shape, may land in either order.** 533 owns `party_size`/`adults`/`children`. **This slice owns `table_id`.** **The two must not share an event table and must not be merged** — a composition change and a table change are different events, exactly as feature 444's own *Out of scope* states for its sibling event.
- **Feature 416 (the peak-party-count question) — `defer`, and it STAYS deferred.** This slice does not decide how many people may join.
- **Feature 501 (`Table.seats`' lower bound) — untouched.**
- **Feature 427 (the SQLite FK pragma) — adjacent.** The pragma is off by default in SQLite (`PRAGMA foreign_keys = 0` — proved by execution), so this table's foreign keys are enforced in Postgres and not in SQLite. **The write-path rule does not depend on them**, and the implementer must not write a test that passes only because SQLite ignores a foreign key.
- **Feature 446 (the migration path) — needed only if the deployment already has a database.** This slice **adds** a table and changes no existing column, so `create_all()` suffices for a fresh database. **If an existing database must be migrated, 446 owns the mechanism and this slice must not invent one.**
- **Feature 474 (the shipped waiter's per-table order state) — adjacent, and a warning rather than a dependency.** 474 owns the *UI's* copy of the per-table order state. **This slice changes no surface**, but 474's UI holds one visit for the whole restaurant (features **474** and **467**), so a surface that reads a moved visit must re-read the table. **Recorded here so the next pass does not file it twice.**

## Open questions

1. **May a party be moved to a table that is too small for it?** Feature **414** compares `party_size` to `seats` **at the seat**. **A move re-opens the same question at a different moment.** **Recorded default: the destination guard re-checks capacity as well as occupancy — because the move is a seat in all but name — and this is recorded as a decision to escalate, not as a settled rule.** **The implementer must not guess.** If the owner decides the move may be refused on capacity, feature **414**'s comparison is reused, not re-implemented.
2. **Does a move close the old visit and open a new one?** The alternative model is that a move is *two* visits, with the second closing the first. **Recorded default: one visit, one change row** — the visit is the party's stay, not the party's seat. **The implementer must not build a close-and-reopen flow.**
3. **What happens to a table's `dirty` state on a move?** The five states are `free`, `seated`, `ordered`, `billed`, `dirty`. A move off a table that was `ordered` leaves the source table dirty (it was used). **Recorded default: the source table becomes `dirty` if it was `ordered` or `billed`, and `free` if it was only `seated`.** **Recorded and escalated — this is 388's vocabulary and the owner decides.**
4. **Is the actor required?** `by_user_id` is nullable, matching the corpus's convention. **Recorded default: nullable — a move made by an unauthenticated path is still a move, and a missing actor is visible as a missing actor.**
5. **Does the same rule apply to `visit.server_id`?** The visit's server is equally rewritable after seating, and feature **451** owns the *role* rule at the write path while saying nothing about the column changing afterwards. **That is a different question, and it is recorded here so the next pass files it or discards it deliberately. It is NOT taken by this slice.**

## Why this matters

**The floor map is how a waiter finds the party.** `_table_status()` is the shipped function that answers *"is this table free?"* and the waiter reads its answer. **A rewrite of one column makes that answer wrong** — and wrong in the direction that causes a second party to be seated at a table that is occupied. **The failure is not a wrong number in a report; it is two guests at one table.**

**It is the same shape as six defects the corpus has already filed** — features **531** (the quantity), **532** (the bill's money), **533** (the party's composition), **534** (the tender method), **535** (the tip's formula version) and **536** (the shift's opening float) — and the corpus sweep returned **zero** hits for the visit's *table*. **Six sibling facts have a rule; the seventh does not.** Feature **533** is the exact sibling: it owns *"the party size and its composition are recorded when the party is seated, and afterwards they are facts with a history"*. **This slice owns the third fact in that sentence — the table the party is at.**

**It closes a gap feature 388 itself names.** 388's pre-mortem is *"two sources of truth that can disagree"*. 388 removes one source (the derivation). **This slice removes the remaining disagreement — between the stored status and the stored pointer.** Neither alone is sufficient, and 388's own text does not claim to be.

**The demand is INFERRED and the contract says so.** No operator has reported a moved table, because no route moves a seated party — `backend/app/routers/` holds only `__init__.py` and `tables.py`. **The defect is latent, not corrupting data.** That is exactly the moment to add the rule: before the first write path exists. **The evidence for the defect is OBSERVED — executed, re-runnable, with the numbers in this contract — and the evidence for the priority is INFERRED.** Those are different claims and the gate asks for both.

## Adjacent evidence

- **Feature 388** (`le31-table-state-machine-first-party-table-has-no-status-column-so-a-second-seat-opens-a-second-visit-…`) — *"**Note on the derived helper:** `_table_status()` must be **rewritten** to read the stored column, not to keep deriving from `Visit`. Two sources of truth that can disagree is the exact failure the pre-mortem names."*
- **The shipped `_table_status()`** (`backend/app/routers/tables.py:64–71`) — read verbatim in this contract; **the probe ran the same query it runs.**
- **Feature 414** (`le31-table-capacity-…`) — *"The two fields already exist and already point at each other in the data model. `Visit.table_id` → `table_.id` is a real foreign key. **The missing piece is a rule, not a column**."* **That sentence is this feature's shape: the pointer exists; the rule does not.**
- **Feature 423** (`le31-party-composition-…`) — *"**Any change to `party_size` vs `Table.seats`.** That is **feature 414** … This feature is about the party's own composition. **The two are independent and both may land.**"*
- **Feature 533** (`le31-a-seated-visit-s-party-size-can-be-rewritten-after-the-party-is-seated-…`) — the sibling contract, same table, same shape, different column. Its *Out of scope* names *"the table-state machine — **feature 388**, filed"* — **and says nothing about the visit's table changing.**
- **Feature 501** (`le31-a-table-with-zero-seats-can-never-be-seated-…`) — *"Nothing in LE31 distinguishes 'a table nobody can seat' from 'a table that is merely empty'."*
- **Feature 474** (`le31-the-shipped-waiter-screen-holds-one-visit-for-the-whole-restaurant-…`) — the UI's copy of the per-table order state.
- **Charter P0 row 42** — *"Waiter can seat a party at any free table and capture `party_size`, `adults`, `children`."*
- **Feature 427** — the SQLite FK pragma, proved by execution (`PRAGMA foreign_keys = 0`), which is why this slice's rule lives at the write path.

## Verification protocol

**Re-run the probe.** `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py` builds LE31's real schema on a throwaway SQLite file and executes the rewrite. **Its output, before the fix, is `ACCEPTED` and `open visits on T1 = 0`.** After the fix, the same probe must show the rewrite **refused**, and the shipped `_table_status()`'s own query must show **1** open visit on the table the party is at.

**The negative control is load-bearing.** A test that asserts "the move is refused" **must fail** when the guard is removed — assert that by commenting out the refusal and watching the test go red. **A test that passes both with and without the guard proves nothing.**

**The assertions, in order:**

1. `UPDATE visit SET table_id` on a seated visit is **refused**; the visit's `table_id` is unchanged; **zero** `VisitTableChange` rows exist.
2. `move_visit_to_table(..., to_table_id=<free table>)` is **accepted**; exactly **one** change row exists with `from_table_id`, `to_table_id`, `by_user_id` and `at` correct; the visit's `table_id` moved; **both** tables' statuses are correct afterwards.
3. A move to an **occupied** table is **refused**; the visit is unchanged.
4. A **second** move produces a **second** row (the case a `previous_table_id` column loses).
5. The consistency assertion holds: `visit.table_id == latest_change.to_table_id`, and **no** open visit sits on a table whose status is `free`.
6. A move writes **no** `StockEntry`, **no** `Bill` and **no** `OrderItem` row — a move relocates the party, it does not re-ring or re-bill anything.
7. `grep -rn "table_id = " backend/` returns the seat path and the move helper, **and nothing else**.

**A note on the numbers in this contract.** Every number quoted here was produced by execution against LE31's real schema on 2026-11-27, by the parent, with the probe in the `scripts/` directory named above, and the `_table_status()` answer was obtained by running **the shipped function's own query**. **They are not transcribed from a subagent's prose.** Where a claim is not proved by execution — Postgres behaviour, the UI's reaction, the operational demand — this contract says so explicitly, in the *Evidence class* line, in the *Open questions*, and in *Why this matters*.
