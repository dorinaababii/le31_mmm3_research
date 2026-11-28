# Feature 542 — A visit can close before it opened: `Visit.closed_at` is unconstrained against `Visit.opened_at`, and the floor map then reads `free` with the guest sitting at the table

> **Pick A of Daily Brainstorm 2026-11-28 (110th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Visit`, verbatim (lines 129–139):
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
> **`closed_at` is a bare nullable timestamp with no ordering constraint against `opened_at`.** The schema has **zero `CHECK` constraints** across all ten tables (read back from the created database — see *Evidence*). A `Visit` is a span of time; a span whose end precedes its start is not a shorter visit, it is an impossible one.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one table, one server, one menu item, one open visit opened `2026-11-27 12:00Z`, one order line and one paid bill with `paid_at = 2026-11-27 13:00Z`):
>
> ```
>   UPDATE visit SET closed_at = '2026-11-24 09:00:00' WHERE id = 1   ->  ACCEPTED
>
>   visit.opened_at   = 2026-11-27 12:00:00
>   visit.closed_at   = 2026-11-24 09:00:00        <- three days BEFORE it opened
>   bill.paid_at      = 2026-11-27 13:00:00        <- the guest HAS PAID
> ```
>
> **⭐ TWO NUMBERS THAT MUST AGREE, AND THEY DISAGREE.**
>
> | number | value |
> |---|---|
> | the visit's own duration, `closed_at − opened_at` | **−4,500 minutes** (−75 hours) |
> | the bill's payment instant minus the visit's close | **+4,560 minutes** (+76 hours) |
>
> The bill says the guest paid **76 hours after** the visit closed. The visit says the guest was there for **−75 hours**. Both numbers are read from the same two rows. **A negative duration is not a short visit — it is a visit that cannot exist**, and the schema accepts it silently.
>
> **⭐ AND LE31'S OWN SHIPPED CODE ANSWERS WRONG.** `_table_status()` (`backend/app/routers/tables.py:64–71`, read verbatim in *Evidence*) derives a table's status from:
>
> ```python
> select(Visit).where(Visit.table_id == table_id, Visit.closed_at == None).first()
> ```
>
> After the rewrite the query finds **no open visit** on that table, so `_table_status` returns **`TableStatus.free.value` → `"free"`** — **while the guest is physically sitting at it, and their bill is already paid.** Executed: the open-visit count for that table went from 1 to **0**, and the floor map reads `free`.
>
> **This is not a theoretical inconsistency.** `seat_party` (`tables.py:33–61`) creates a **new** `Visit` for the table with **no guard**: line 50 is a literal `# TODO: reject if table is not FREE (need TableStatus column on Table)`. So the sequence *"a visit's close is backdated → the table reads free → the next party is seated at the same table → the original visit and the new visit both exist on the same table"* is **reachable through the shipped router**, and the first visit's order lines are still attached to it.
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all **575** feature contracts and **526** HANDOFFs (1,101 files) returns **zero** hits for a rule that a visit's close must not precede its open:
>
> | sweep | hits | what they are |
> |---|---|---|
> | `closed_at.{0,40}opened_at.{0,40}(before\|order\|constraint)` | **0** | — |
> | `visit.{0,40}closed_at.{0,60}(before\|after\|order)` | 3 | feature **452**'s *recording*; feature **415**'s open question 1; feature **428**'s *ordering* note — **all three are prose, none is a rule** |
> | `dwell.{0,40}(negative\|before\|ordering)` | 1 | feature **428**, on the *population* rule — not the ordering |
>
> **⭐ THE CORPUS ALREADY RECORDED THIS AND FILED IT NEVER.** Feature **452** wrote, verbatim, in its *Adjacent evidence*:
>
> > *"`Visit.closed_at` is unconstrained against `opened_at` — executed: a visit can close three days **before** it opened. Feature **428** owns the *population* rule for open visits; feature **415** owns *writing* `closed_at`. **Neither owns the ordering constraint. Recorded, not picked** — a visit's duration is a different fact from a line's state."*
>
> **That is the sixth instrument's shape exactly: a feature that found a defect, did not own it, and said so.** The corpus named the right neighbours (415 writes `closed_at`, 428 aggregates it) and both of those neighbours **disclaim** the ordering — 415's *Out of scope* is about the `Table` status column, and 428's *Out of scope* says *"**Writing `Visit.closed_at`. That is feature 415**"*. **Neither one owns the constraint between the two columns.**
>
> | rule | mechanism | owner |
> |---|---|---|
> | **writing** `Visit.closed_at` (the close write) | a route | feature **415** |
> | the **population** for the dwell average | an aggregate helper | feature **428** |
> | the **table's** status | a derived helper + a `Table.status` column | feature **388** |
> | the visit's **table** changing after seating | an event table | feature **538** |
> | the visit's **server** changing after seating | an event table | feature **539** |
> | the visit's **composition** (`party_size`/`adults`/`children`) changing | an event table | feature **533** |
> | **a close that precedes the open** | **a `CHECK` constraint** | **THIS SLICE** |

## Goal

**Make it impossible to store a `Visit` whose `closed_at` precedes its `opened_at`, and make the floor-map read agree with the visit's own timeline.**

The single sentence this feature exists to make true: *a visit that has closed did not close before it began.*

## Scope

- A **`CHECK` constraint on `visit`** that refuses a row whose `closed_at` is non-null and earlier than `opened_at`.
- The constraint expressed in the **portable subset** that behaves identically on SQLite (LE31's dev database, charter §3.1) and Postgres (production).
- One **regression test** that fails on today's schema and passes on the fixed one.
- One **documented note** in `PROJECT_CHARTER.md` §4 (or the nearest section) recording that a visit's span is bounded.

## Out of scope

- **Writing `Visit.closed_at`.** That is **feature 415** (`le31-bill-closes-visit-edge`), which is about to create the close write and the `Bill`/`DerivedTip`/`Visit.closed_at` transaction. **This slice does not add a route, does not create a bills router, and does not change when a visit closes.** **⚠️ ORDERING: feature 415 must land FIRST, or in the same PR** — before it lands, `closed_at` is never written and the constraint has nothing to constrain. See *Dependencies*.
- **The dwell KPI and its population.** Feature **428** owns `avg dwell` and the open-visit aggregate rule. **This slice does not change the aggregation**, does not change which visits are counted, and does not decide feature 415's Open question 1 (*"should `closed_at` be the payment instant or the moment the waiter taps close?"*). **That question is unaffected by this constraint** — whichever endpoint is chosen, it will be *after* `opened_at`, and the constraint only refuses a close that is *before* it.
- **The `Table.status` column and the seat guard.** Feature **388** owns the stored status and `POST /api/tables/{id}/release`. The `# TODO: reject if table is not FREE` comment at `tables.py:50` is **388's** to resolve. **This slice does not add a status column, does not add a release endpoint, and does not change `seat_party`'s guard.**
- **Any correction or reopening of an existing visit.** Feature **415**'s Open question 6 asks *"should a closed visit be immutable?"* — **this slice does not answer it** and does not open a correction path. A constraint that refuses to *create* an impossible visit is not a prohibition on correcting one.
- **`OrderItem`'s timestamps** (`fired_at`, `ready_at`, `served_at`). Feature **452** owns their ordering; the same class of defect on the line is **452's**, not this slice's.
- **`Batch.expires_at` vs `Batch.prepared_at`.** That is **feature 543** — a different table, a different rule, a different mechanism. **Do not bundle.**
- **`Shift.closed_at` vs `Shift.opened_at`.** That is **feature 544** — a different table, a different rule, a different mechanism. **Do not bundle.**

## Description

### The defect

`Visit` is a span of time. `opened_at` is its start; `closed_at` is its end, `NULL` while the visit is open. **The schema does not say the end must come after the start, and the schema is the only thing that can say it** — no route currently writes `closed_at`, so a write-path rule would protect nothing today.

### The mechanism

A `CHECK` constraint on `visit`:

```sql
CHECK (closed_at IS NULL OR closed_at >= opened_at)
```

**⚠️ THE NULL-SEMANTICS TRAP (feature 91's shape).** A `CHECK` constraint that evaluates to `NULL` (or `UNKNOWN`) **passes** in SQL three-valued logic — it does **not** reject the row. `closed_at IS NULL OR closed_at >= opened_at` is written so that the `IS NULL` branch is **explicitly true** for an open visit, rather than relying on `NULL >= opened_at` being `NULL`. **A check written the other way round would silently permit every open visit.** This is exactly the trap feature **91** exists for; read it before writing the constraint.

**⚠️ THE CROSS-ENGINE-TYPE TRAP.** `opened_at` and `closed_at` are `DateTime(timezone=True)` → `DATETIME` on SQLite, `TIMESTAMPTZ` on Postgres. Feature **453** proved by execution that **SQLite silently drops the UTC offset** on these columns. So:
- On **SQLite**, the comparison is a naive string/datetime comparison of two values written in the same convention — fine as long as every writer uses UTC (charter §3.5).
- On **Postgres**, `TIMESTAMPTZ` comparison is absolute and correct.
- **The constraint must not depend on a `strftime`/`typeof` expression**, because those are SQLite-only and feature **453** already proved that a SQLite-only expression is a dev/prod divergence.

**Recommendation:** the portable expression is the plain comparison `closed_at >= opened_at`, plus — if the owner wants belt-and-braces — an additional SQLite `CHECK (typeof(closed_at) IS NULL OR typeof(closed_at) = 'datetime')` in the SQLite-only path. **The portable core is the ordering comparison; the type check is SQLite-specific and must be behind a dialect switch, exactly as feature 404's *Open questions* 1 describes.**

### The alternative mechanism, and why it is not the one chosen

A **write-path guard** (refuse a close whose instant precedes the open) is also possible, and feature **415** is the natural place for it. It is **not** sufficient on its own, for two reasons that the corpus has already paid for:
1. Feature **470** established that LE31's invariants are currently upheld **vacuously** — there is no write path for `closed_at` at all, so a write-path rule protects nothing until the path exists, and the path may be written by anything (a script, a future route, a direct SQL client).
2. Feature **421** made the same argument for the ledger: a lint rule protects the *application*, not the *database*.

**Both mechanisms are compatible.** The recommendation is: **the constraint lands first**, because it is the only thing that holds when the write path does not exist; and the write-path guard, if 415 adds one, is a *better error message* on top of the same rule. **They must not be merged** — they are two mechanisms and two layers.

## Data model

**No new table. No new column. One constraint.**

```python
class Visit(SQLModel, table=True):
    __tablename__ = "visit"
    ...
    __table_args__ = (
        CheckConstraint(
            "closed_at IS NULL OR closed_at >= opened_at",
            name="ck_visit_closed_after_opened",
        ),
    )
```

> **⚠️ `SQLModel` table-arg support.** `SQLModel` 0.0.48 supports `__table_args__` on a `table=True` class. **Verify this in the target environment before relying on it** — the parent's execution environment has `sqlmodel 0.0.48` / `SQLAlchemy 2.1.8`. If `__table_args__` proves not to be honoured in the pinned version, fall back to declaring the constraint via `sa_column`/`Column(CheckConstraint(...))` on one of the columns, or via `__table_args__` as a tuple. **Whichever mechanism is used, the regression test must assert the *behaviour*, not the declaration form** — so the test is written against the behaviour and stays valid whichever form is used.

**Effect on the DDL** (read back from the created database after this change):

```sql
CREATE TABLE visit (
    ...
    opened_at DATETIME NOT NULL,
    closed_at DATETIME,
    ...
    CONSTRAINT ck_visit_closed_after_opened CHECK (closed_at IS NULL OR closed_at >= opened_at)
);
```

**⚠️ THE CONSTRAINT CENSUS ALREADY AT ZERO.** The parent's probe read back the created schema and found: **10 tables, 0 `CHECK` constraints, and exactly one `UNIQUE` constraint (`bill.visit_id`)** — the same census feature **470** recorded. **This constraint is the first `CHECK` on `visit`.** Feature **404** proposes `CHECK` constraints on the silent-corruption columns, and feature **413** is about database triggers. **This is a third, separate `CHECK` family** — a *temporal ordering* constraint, not a *type* constraint (404) and not a *trigger* (413). **It must not be bundled with either.**

## Implementation steps

1. **Write the regression test FIRST.** It must fail on today's schema and pass on the fixed one:
   - a `Visit` with `opened_at = 2026-11-27 12:00Z` and `closed_at = 2026-11-24 09:00Z` → **REJECTED**;
   - a `Visit` with `opened_at = 2026-11-27 12:00Z` and `closed_at = 2026-11-27 13:00Z` → **ACCEPTED**;
   - a `Visit` with `opened_at = 2026-11-27 12:00Z` and `closed_at = None` → **ACCEPTED** (the open case — **this is the case a badly-written NULL check would reject**);
   - a `Visit` with `opened_at = 2026-11-27 12:00Z` and `closed_at = 2026-11-27 12:00Z` → **ACCEPTED** (the boundary — equal is not before).
2. **Add the `CheckConstraint`** to `class Visit`.
3. **Verify the DDL** by rebuilding the schema and reading `sqlite_master` back — assert the constraint text is present.
4. **Verify the behaviour** by executing the four cases above against the rebuilt schema, not by reading the source.
5. **Add the charter note** — a sentence in `PROJECT_CHARTER.md` recording that a visit's span is bounded: *a visit that has closed did not close before it began.* Point at the constraint, not at a route.
6. **Do not touch** `routers/tables.py`, `models.py`'s other classes, `index.html`, or any feature contract.
7. **Run the whole test suite** and confirm the new test is the only new failure before the fix and the only new pass after it.

## Telegram interaction if any

**None.** This slice adds no Telegram surface, no bot command, and no message. It is a schema constraint and a test.

## Dependencies

- **Feature 415** (`le31-bill-closes-visit-edge`) — **MUST LAND FIRST, or in the same PR.** 415 creates the `closed_at` write. Before it lands, `closed_at` is `NULL` for every visit and the constraint never fires — which is **correct** but means the constraint's value is realised only once 415 exists. **Name 415 in the PR description.** This is the **upstream-of-filed-work** condition in its clearest form: **415 would otherwise implement the close write with no guard behind it, faithfully.**
- **Feature 428** (`le31-avg-dwell-silently-excludes-still-open-visits`) — depends on this constraint being *possible*, not on it landing. 428's `avg dwell` will now be non-negative. **No change to 428.** 428's *Open questions* 3 (*"should a visit still open after N hours be flagged as abandoned?"*) is **unaffected and not answered here**.
- **Feature 452** (`le31-an-order-line-can-be-served-and-still-say-it-is-new`) — **the sibling defect on `order_item`.** 452 owns the line's `status`↔timestamp rule. **Its `Adjacent evidence` is where this defect was recorded.** This slice is the **visit-level** half; 452 is the **line-level** half. **Do not merge them** — different tables, different rules, different owners. **A note in 452 pointing at 542 is acceptable and is recorded here.**
- **Feature 453** (`le31-sqlite-silently-drops-the-utc-offset`) — **read this before writing the constraint.** It is the authority on the SQLite `DATETIME` offset behaviour this constraint sits on top of. **No change to 453.**
- **Feature 470** (`le31-the-append-only-stock-ledger-is-protected-by-a-docstring`) — owns the ledger's *database-level* enforcement (a trigger + a privilege statement) and is the precedent for "an invariant the database must refuse". **Its *Adjacent evidence* is one of the places this class of defect was recorded.** **Different table, different rule — do not bundle.**
- **Feature 520** (`le31-two-tables-can-sit-on-the-same-floor-map-coordinate`) — the precedent for **a `UniqueConstraint` added to a table that carried zero constraints**, and the precedent for **a constraint that has to be expressed so it works on SQLite** (its *Open questions* 1 discusses exactly this). **Read it before writing the constraint.** **No change to 520.**
- **Feature 388** (`le31-table-state-machine`) — owns `Table.status` and the seat guard. **The `free` reading this feature's evidence shows is 388's defect, not this slice's** — this slice's defect is the *impossible span*, and 388's is the *derived status*. **The two are adjacent and must not be merged.**

## Open questions

1. **Should a visit be allowed to be reopened (a correction)?** Feature **415**'s Open question 6 asks the same thing. **Recorded default: this slice answers only the negative span** — a constraint that refuses to *create* an impossible visit is not a prohibition on correcting one. **415's question is not answered here.**
2. **Should the constraint live in the database, in the write path, or in both?** **Recorded default: in the database**, because no write path for `closed_at` exists today and a write-path rule alone would be vacuous (feature 470's precedent). If 415 adds a write-path guard, it is a **better error message** on top of the same rule, not a substitute.
3. **What should the error look like when the constraint fires?** **Recorded default: the database's own constraint-violation error**, wrapped by the route layer into LE31's existing error shape. **The exact message is not decided here.**
4. **Does the same rule apply to `opened_at` and `closed_at` being *equal*?** **Recorded default: equal is allowed** — a visit that closes at the instant it opened is a zero-length visit, which is degenerate but not impossible. **This is the boundary case and the regression test must pin it.**
5. **Does the same rule apply to `visit.opened_at` itself being rewritten?** `opened_at` is equally rewritable, and features **538**/**539**/**533** each own a *different* column of the same table and each explicitly disclaim the others. **This slice does not own `opened_at`'s mutability** — that is a different question, and it is recorded here so the next pass files it or discards it deliberately. **It is NOT taken by this slice.**
6. **Should the constraint be expressed with an explicit `IS NOT NULL` on both sides rather than `IS NULL OR ...`?** **Recorded default: `closed_at IS NULL OR closed_at >= opened_at`** — the `IS NULL` branch must be *explicitly true*, because a `NULL` comparison evaluates to `UNKNOWN` and `UNKNOWN` passes a `CHECK`. **A check written the other way round silently permits every open visit.**

## Why this matters

**The floor map is the operator's whole view of the room, and it is derived from this column.**

`_table_status()` answers *"is anyone sitting here?"* by asking *"is there a visit on this table with `closed_at IS NULL`?"*. That is a **complete and correct** implementation of the question — provided the visits in the table have a coherent timeline. The schema does not require that, so the answer can be wrong, and it is wrong **silently**: no error, no log line, no exception. The floor map says `free`. The waiter seats a second party at that table. The first party is still there, and their bill is already paid.

This is the shape the corpus has been fixing for a dozen passes — **a fact that is owned by nobody** — but this instance is sharper than most, for two reasons worth stating:

1. **The corpus recorded it and filed it never.** Feature **452** found it, named the right neighbours, and wrote *"Recorded, not picked."* It has been sitting in the corpus since 2026-11-14. A finding that is recorded twice and filed never is a finding that will be rediscovered forever — this is the argument feature **531** made when it closed the quantity case. **This contract is the door, closed.**
2. **It is not latent in the way most of these are.** The corpus's usual caveat is *"no code path changes this today, so the defect is latent, not corrupting data."* That caveat **does not apply here.** `seat_party` runs **today**, on **today's** router, and it creates a `Visit` with **no guard at all** (line 50 is a `TODO` comment). The only thing that stops the bad state today is that **nothing writes `closed_at` yet** — and feature **415** is about to start writing it. **So the precondition for this defect is a filed feature that is about to land.**

**Cost:** one `CHECK` constraint, one regression test, one charter sentence. **No new table, no new column, no route, no UI change, no migration directory** (charter §3.2: LE31 v1 uses `init_db()`, not Alembic — **do not silently introduce Alembic**). **Rollback:** drop the constraint; no data is lost, because a row that violates it cannot exist once the constraint is in place.

## Evidence

**Parent-run, 2026-11-28.** Full probe: `/opt/data/le31-brainstorm-2026-11-28-scripts/probe_1128.py` and `probe_two_numbers.py`; environment `/opt/data/le31-verify-2026-11-11/.venv` (`sqlmodel 0.0.48`, `SQLAlchemy 2.1.8`).

**Constraint census, read back from the CREATED database:**

```
  10 tables: app_user, batch, bill, derived_tip, menu_item, order_item,
             shift, stock_entry, table_, visit
  CHECK constraints across all ten tables : 0
  UNIQUE constraints                     : bill.visit_id   (the only one)
```

**Probe A — the visit span:**

```
  UPDATE visit SET closed_at = '2026-11-24 09:00:00' WHERE id = 1   ->  ACCEPTED

  visit.opened_at   = 2026-11-27 12:00:00.000000
  visit.closed_at   = 2026-11-24 09:00:00+00:00
  bill.paid_at      = 2026-11-27 13:00:00.000000

  num1  visit duration (closed_at - opened_at)      = -4500.0 minutes
  num2  bill.paid_at - visit.closed_at              = +4560.0 minutes
  both numbers disagree                             = True

  _table_status()'s query, open visits on that table:
        before the rewrite : 1
        after  the rewrite : 0        -> the floor map reads "free"
```

**The shipped read, quoted verbatim** (`backend/app/routers/tables.py:64–71`):

```python
def _table_status(table_id: int, session: Session) -> str:
    """Derive a table's current status from the latest open Visit."""
    visit = session.exec(
        select(Visit).where(Visit.table_id == table_id, Visit.closed_at == None)
    ).first()
    if not visit:
        return TableStatus.free.value
    return TableStatus.seated.value  # could be 'ordered' / 'billed' with more checks
```

**And the unguarded seat write** (`backend/app/routers/tables.py:50`, quoted verbatim):

```python
    # TODO: reject if table is not FREE (need TableStatus column on Table)
```

**Corpus sweep, parent-run, over 575 feature contracts + 526 HANDOFFs (1,101 files):**

| sweep | hits | what the hits are |
|---|---|---|
| `closed_at.{0,40}opened_at.{0,40}(before\|order\|constraint)` | **0** | — |
| `visit.{0,40}closed_at.{0,60}(before\|after\|order)` | 3 | 452's recording; 415's open question 1; 428's ordering note — **prose, not rules** |
| `dwell.{0,40}(negative\|before\|ordering)` | 1 | 428 — the population rule, not the ordering |

**Feature 452's own words** (quoted verbatim from `features/452-…md`, line 316):

> *"`Visit.closed_at` is unconstrained against `opened_at` — executed: a visit can close three days **before** it opened. Feature **428** owns the *population* rule for open visits; feature **415** owns *writing* `closed_at`. **Neither owns the ordering constraint. Recorded, not picked** — a visit's duration is a different fact from a line's state."*

**Neighbours' own disclaimers, quoted verbatim:**

- **415** (`features/415-…md`, *Out of scope*): *"**`Table` status, double-seating, and `POST /api/tables/{id}/release`.** Feature **388** owns those. This feature writes `Visit.closed_at`; it does **not** add a status column to `Table`, does not prevent double-seating, and does not add a release endpoint."* — **the write, not the ordering.**
- **428** (`features/428-…md`, *Out of scope*): *"**Writing `Visit.closed_at`.** That is **feature 415**"* — **the write, not the ordering.**
- **388** (`features/388-…md`): owns the `Table.status` column and the double-seating guard — **not the visit's span.**

**⚠️ NOT PROVED, AND STATED PLAINLY:** the **Postgres** behaviour of the constraint was **not** executed — `psycopg` is not importable in the verification environment. The Postgres row is proved from the DDL rendering and the dialect's documented `CHECK` semantics, **not** from a live round trip. **Do not report the Postgres behaviour as tested.**
