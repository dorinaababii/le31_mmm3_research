# Feature 544 — A shift can close before it opened: `Shift.closed_at` is unconstrained against `Shift.opened_at`, and the shift's own duration and its variance then disagree

> **Pick C of Daily Brainstorm 2026-11-28 (110th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Shift`, verbatim (lines 181–191):
>
> ```python
> class Shift(SQLModel, table=True):
>     __tablename__ = "shift"
>
>     id: int | None = Field(default=None, primary_key=True)
>     opened_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     closed_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     opening_float: Decimal = Field(max_digits=10, decimal_places=2)
>     counted_cash: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
>     variance: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
>     by_user_id: int = Field(foreign_key="app_user.id")
> ```
>
> **A shift is a working period: it opens at an instant and closes at a later instant. `closed_at` is nullable and unconstrained against `opened_at`.** The schema has **zero `CHECK` constraints** across all ten tables (read back from the created database — see *Evidence*).
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one server and one shift opened `2026-11-27 08:00Z` with an opening float of €100.00, a counted cash of €100.00 and a variance of €0.00):
>
> ```
>   UPDATE shift SET closed_at = '2026-11-26 20:00:00' WHERE id = 1   ->  ACCEPTED
>
>   shift.opened_at = 2026-11-27 08:00:00.000000
>   shift.closed_at = 2026-11-26 20:00:00+00:00      <- TWELVE HOURS BEFORE it opened
> ```
>
> **⭐ TWO NUMBERS THAT MUST AGREE, AND THEY DISAGREE.**
>
> | number | value |
> |---|---|
> | the shift's own duration, `closed_at − opened_at` | **−12.0 hours** |
> | the open-shift count the guard queries | **0** — the shift reads as *closed*, and it is the **only** shift in the table |
>
> **⭐ AND THE STORED VARIANCE STILL READS €0.00.** `variance = counted_cash − opening_float` = `100.00 − 100.00` = **`0.00`**, and it stays **`0.00`** after the backdating. **A shift that ran for minus twelve hours closes with a perfectly clean variance**, and the owner reading the daily report sees a shift that balanced and lasted less than no time at all.
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all **575** feature contracts and **526** HANDOFFs (1,101 files) returns **zero first-party hits** for a rule that a shift's close must not precede its open:
>
> | sweep | hits | what they are |
> |---|---|---|
> | `shift.{0,40}(opened_at\|closed_at).{0,60}(immutab\|rewrit\|mutab)` | 1 | feature **536**'s mention of the shift's timestamps — **about the float's mutability**, not the timestamps' ordering |
> | `shift.{0,60}closed_at.{0,60}(before\|ordering\|constraint)` | 2 | feature **426** and its HANDOFF — **the open-shift guard** (see below) |
> | `closed_at.{0,40}opened_at.{0,60}(before\|shift)` | 4 | feature **426** and its HANDOFF again, plus feature **415**'s and **428**'s **visit**-level notes — **all about `visit`, not `shift`** |
>
> **The two hits that look like owners are not.** Feature **426** (`le31-shift-close-lifecycle`) writes, verbatim, in *Implementation steps* 3:
>
> > *"Implement the open-shift guard as a query for an existing open shift (`closed_at IS NULL`) before inserting a new one; return **409** with a message naming the open shift's id. **The guard is a query, not a database constraint** — feature 404's territory, and adding a partial unique index here would be that feature's territory."*
>
> **That is a guard on how many shifts may be open — not a rule about when a shift may close.** Feature 426's *Open questions* are about the cash-tip term (391), close idempotency, and a shift closed with no payments. **The ordering constraint is in none of them.** And feature 426's own words — *"**The guard is a query, not a database constraint**"* — are the reason this defect is live: **the corpus has already decided, once, that the shift's lifecycle is guarded by queries rather than by the database.** That decision is right for *how many* shifts are open and is **not** a decision about *when* a shift may close.
>
> | rule | mechanism | owner |
> |---|---|---|
> | the **open-shift guard** (one open shift at a time) | a query + HTTP 409 | feature **426** |
> | the shift's **opening float** and its change event | an event table | feature **536** |
> | the **close** route and the variance derivation | a route | feature **426** |
> | the shift's **actor** (`by_user_id`) | a column + FK | feature **417** (the actor convention) |
> | **a shift that closes before it opened** | **a `CHECK` constraint** | **THIS SLICE** |
>
> **⭐ AND THE CONVERSATION WITH 426 IS SPECIFIC AND WORTH STATING.** Executed: with the shift backdated, `SELECT COUNT(*) FROM shift WHERE closed_at IS NULL` returned **0** — so 426's guard saw **no open shift** and permitted a **second** shift to be opened while the backdated one still existed. **The two shifts overlap.** In this probe the second shift was inserted *after* the first was (wrongly) closed, so only one was open at a time; but the sequence *"shift A opened 08:00 → shift A's close is backdated to yesterday → the guard sees no open shift → shift B is opened → shift A is still in the table with its own float, its own counted cash and its own variance"* is exactly the state 426's guard was written to prevent, and the guard cannot see it. **The guard queries `closed_at IS NULL`; a backdated close is a lie that the query cannot detect.**

## Goal

**Make it impossible to store a `Shift` whose `closed_at` precedes its `opened_at`, so that a shift's duration and its variance describe the same period.**

The single sentence this feature exists to make true: *a shift that closed did not close before it began.*

## Scope

- A **`CHECK` constraint on `shift`** that refuses a row whose `closed_at` is non-null and earlier than `opened_at`.
- The constraint in the **portable subset** that behaves identically on SQLite (LE31's dev database, charter §3.1) and Postgres (production).
- One **regression test** that fails on today's schema and passes on the fixed one.
- One **documented note** in `PROJECT_CHARTER.md` §4 recording that a shift's working period is bounded.

## Out of scope

- **The open-shift guard** (one open shift at a time, HTTP 409). Feature **426** owns it and owns its own decision that *"the guard is a query, not a database constraint"*. **This slice does not change the guard, does not change the 409, and does not add a partial unique index** — 426's reasoning about partial indexes not being portable to SQLite is correct and is not reopened here.
- **The shift close route and the variance derivation.** Feature **426** owns `POST /api/shifts/{id}/close` and the `variance = counted_cash − opening_float` computation. **This slice does not add a route, does not compute a variance, and does not change what a variance means.**
- **The shift's opening float and its change event.** Feature **536** owns the float's mutability and the event table. **This slice does not add, remove or alter the float, the counted cash, the variance, or the event table.** 536's *Open questions* 2 (*"should the guard apply to a closed shift as well as an open one?"*) is **not answered here.**
- **The shift's actor.** Feature **417** owns the actor convention (`StockEntry.by_user_id`); `Shift.by_user_id` already exists. **This slice does not touch it.**
- **`Visit.closed_at` vs `Visit.opened_at`.** That is **feature 542** — a different table, a different rule. **Do not bundle.**
- **`Batch.expires_at` vs `Batch.prepared_at`.** That is **feature 543** — a different table, a different rule. **Do not bundle.**
- **Any `CHECK` on the silent-corruption columns.** Feature **404** (the other file of that number) proposes type constraints; feature **413** is about database triggers. **This is a third, separate `CHECK` family** — a *temporal ordering* constraint, not a *type* constraint and not a trigger. **Do not bundle.**

## Description

### The defect

`Shift` is a working period with two business times: `opened_at` and `closed_at`, the latter `NULL` while the shift is open. **The schema does not say the end must come after the start.** A shift whose close precedes its open is not a short shift — it is an impossible one — and it is the one shift fact that every other shift fact is measured against.

### Why it matters more here than on `visit` or `batch`

**The shift carries a money verdict.** `variance` is the number the owner acts on: *"the drawer was €100.00 and we counted €100.00, so the shift balanced."* The variance is derived from `counted_cash` and `opening_float` — **neither of which is a timestamp** — so **the backdating leaves the variance untouched and perfectly clean**. The report says *"the shift balanced"*, and the shift's own timestamps say it ran for minus twelve hours.

And the guard is a **query**, not a constraint. Feature **426** chose that deliberately and its reasoning is sound; the consequence is that **the guard trusts `closed_at` absolutely**. A backdated close does not merely corrupt a duration — it **fools the guard that decides whether another shift may start.**

### The mechanism

A `CHECK` constraint on `shift`:

```sql
CHECK (closed_at IS NULL OR closed_at >= opened_at)
```

**⚠️ THE NULL-SEMANTICS TRAP (feature 91's shape).** A `CHECK` constraint evaluating to `NULL`/`UNKNOWN` **passes** in SQL three-valued logic — it does **not** reject the row. `closed_at IS NULL OR closed_at >= opened_at` writes the NULL case **explicitly true**, rather than relying on `NULL >= opened_at` being `NULL`. **The other way round would silently permit every open shift** — which is every shift, because `closed_at` is nullable and no route writes it today. **Read feature 91 before writing the constraint.**

**⚠️ THE CROSS-ENGINE-TYPE TRAP.** Both columns are `DateTime(timezone=True)` → `DATETIME` on SQLite, `TIMESTAMPTZ` on Postgres. Feature **453** proved by execution that **SQLite silently drops the UTC offset** on these columns. The constraint must therefore use a **plain comparison**, not a `strftime`/`typeof` expression (those are SQLite-only, and feature **453** already proved that a SQLite-only expression is a dev/prod divergence). If the owner wants a SQLite-only type check as well, it goes behind a dialect switch — exactly as feature **404**'s *Open questions* 1 describes.

### The alternative mechanism, and why it is not the one chosen

A **write-path guard** in the close route (refuse a close whose instant precedes the open) would be a nicer error message. It is **not sufficient on its own**:
1. **There is no close route yet.** Feature **426** is about to create one — and until it exists, a write-path rule protects nothing (feature **470**'s vacuity argument).
2. Feature **426**'s own guard is already a query, and the corpus has accepted that the shift's lifecycle is guarded by queries. **This constraint is the database-level backstop for the one fact the queries cannot check.**

**Both mechanisms are compatible.** Recommendation: **the constraint lands first**; if 426's close route adds a guard, it is a **better error message on top of the same rule**, not a substitute.

## Data model

**No new table. No new column. One constraint.**

```python
class Shift(SQLModel, table=True):
    __tablename__ = "shift"
    ...
    __table_args__ = (
        CheckConstraint(
            "closed_at IS NULL OR closed_at >= opened_at",
            name="ck_shift_closed_after_opened",
        ),
    )
```

> **⚠️ `SQLModel` table-arg support.** `SQLModel` 0.0.48 supports `__table_args__` on a `table=True` class. **Verify this in the target environment before relying on it** — the parent's execution environment has `sqlmodel 0.0.48` / `SQLAlchemy 2.1.8`. If `__table_args__` proves not to be honoured in the pinned version, fall back to declaring the constraint via `Column(CheckConstraint(...))` on one of the columns. **Whichever mechanism is used, the regression test must assert the *behaviour*, not the declaration form** — so the test is written against the behaviour and stays valid whichever form is used.

**Effect on the DDL** (read back from the created database after this change):

```sql
CREATE TABLE shift (
    ...
    opened_at DATETIME NOT NULL,
    closed_at DATETIME,
    opening_float NUMERIC(10, 2) NOT NULL,
    counted_cash NUMERIC(10, 2),
    variance NUMERIC(10, 2),
    by_user_id INTEGER NOT NULL,
    ...
    CONSTRAINT ck_shift_closed_after_opened CHECK (closed_at IS NULL OR closed_at >= opened_at)
);
```

**⚠️ THE CONSTRAINT CENSUS IS ALREADY AT ZERO.** The parent's probe read back the created schema: **10 tables, 0 `CHECK` constraints, exactly one `UNIQUE` constraint (`bill.visit_id`)** — the same census feature **470** recorded. **This constraint is the first `CHECK` on `shift`.**

## Implementation steps

1. **Write the regression test FIRST.** It must fail on today's schema and pass on the fixed one:
   - a `Shift` with `opened_at = 2026-11-27 08:00Z` and `closed_at = 2026-11-26 20:00Z` → **REJECTED**;
   - a `Shift` with `opened_at = 2026-11-27 08:00Z` and `closed_at = 2026-11-27 20:00Z` → **ACCEPTED**;
   - a `Shift` with `opened_at = 2026-11-27 08:00Z` and `closed_at = None` → **ACCEPTED** (the open case — **this is the case a badly-written NULL check would reject**);
   - a `Shift` with `opened_at = 2026-11-27 08:00Z` and `closed_at = 2026-11-27 08:00Z` → **ACCEPTED** (the boundary — equal is not before).
2. **Add the `CheckConstraint`** to `class Shift`.
3. **Verify the DDL** by rebuilding the schema and reading `sqlite_master` back — assert the constraint text is present.
4. **Verify the behaviour** by executing the four cases above against the rebuilt schema, not by reading the source.
5. **Add the charter note** — a sentence in `PROJECT_CHARTER.md` §4 recording that a shift's working period is bounded.
6. **Do not touch** `routers/`, `models.py`'s other classes, `index.html`, the float, the counted cash, the variance, or any feature contract.
7. **Run the whole test suite** and confirm the new test is the only new failure before the fix and the only new pass after it.

## Telegram interaction if any

**None.** This slice adds no Telegram surface, no bot command, and no message. It is a schema constraint and a test.

## Dependencies

- **Feature 426** (`le31-shift-close-lifecycle`) — **MUST LAND FIRST, or in the same PR.** 426 creates the close route and the open-shift guard. Before it lands, `closed_at` is never written and the constraint never fires. **After it lands, 426's guard reads `closed_at` absolutely, and this constraint is what makes that reading safe.** Name 426 in the PR description. **No change to 426**, and 426's *Open questions* 1, 2 and 3 (the cash-tip term, close idempotency, an empty shift) are **not answered here**.
- **Feature 536** (`le31-a-shift-s-opening-float-can-be-rewritten-after-the-shift-opens`) — owns the shift's `opening_float` and its change-event table. **This slice does not touch the float.** 536's *Open questions* 2 (*"should the guard apply to a closed shift as well as an open one?"*) is **not answered here** — and the two are compatible: 536's guard decides *whether the float may change*, this constraint decides *whether the shift's span is possible*.
- **Feature 453** (`le31-sqlite-silently-drops-the-utc-offset`) — **read this before writing the constraint.** It is the authority on the SQLite `DATETIME` offset behaviour this constraint sits on top of. **No change to 453.**
- **Feature 470** (`le31-the-append-only-stock-ledger-is-protected-by-a-docstring`) — owns the ledger's *database-level* enforcement and is the corpus's precedent for *"an invariant the database must refuse"*. **Different table, different rule — do not bundle.**
- **Feature 520** (`le31-two-tables-can-sit-on-the-same-floor-map-coordinate`) — the precedent for **adding a constraint to a table that carried zero constraints**, and for **a constraint that must work on SQLite as well as Postgres** (its *Open questions* 1). **Read it before writing the constraint.** **No change to 520.**
- **Features 542 and 543** (`le31-a-visit-can-close-before-it-opened`, `le31-a-batch-can-expire-before-it-was-prepared`) — the **two sibling slices**, on `visit` and `batch`. **Same mechanism, same shape, same charter sentence.** They are designed to land together as one family of temporal-ordering constraints. **Do not merge them** — three tables, three rules, three owners.

## Open questions

1. **Should the constraint be in the database, the write path, or both?** **Recorded default: in the database**, because no close route exists today and a write-path rule alone would be vacuous (feature 470's precedent), and because 426's guard is deliberately a query. A write-path guard, if 426 adds one, is a better error message on top of the same rule.
2. **Should a shift's close be allowed to equal its open?** **Recorded default: yes** — equal is not before. **The regression test must pin this boundary.**
3. **Should the open-shift guard also become a database constraint now?** **Recorded default: no.** Feature **426** decided against it with a correct portability argument (a partial unique index is not expressible in SQLite, LE31's dev database). **That decision is not reopened by this slice**, and this slice's constraint is deliberately a **plain** `CHECK` — no partial index, no dialect-specific form.
4. **Does the same rule apply to `Shift.opened_at` itself being rewritten?** `opened_at` is equally rewritable and no feature owns its mutability. **This slice does not own it** — a different question, recorded here so the next pass files it or discards it deliberately. **It is NOT taken by this slice.**
5. **Should the shift's duration be derived rather than computed from the two timestamps?** A derived duration would be immune to a backdated close in the same way 374's derived `qty_remaining` is. **Recorded default: not in this slice** — that is a charter-shape question about whether a duration is a fact or a computation, and it touches feature 426's variance derivation. **It is recorded here, not decided, and not taken.**
6. **Should an already-stored impossible shift be repaired on migration?** **Recorded default: no.** LE31 v1 uses `init_db()` (charter §3.2) and no code writes `closed_at` today, so there is no production data with an impossible value. **If a repair is ever needed, it is a separate change** — and it must be recorded as one.

## Why this matters

**The shift is the one place where LE31's own numbers are a verdict, and this is the one place where a backdated timestamp leaves the verdict intact.**

A variance of €0.00 means *"the drawer balanced."* That is the sentence the owner takes away. **The backdating cannot touch it**, because the variance is computed from two money columns and not from a single timestamp. So the shift's duration reads **minus twelve hours** while its verdict reads **perfectly clean** — and **the verdict is the part a human acts on.**

Worse, feature **426**'s guard — the one piece of machinery in LE31 that was written specifically to stop two shifts from being open at once — **cannot see it**, because the guard asks *"is there a shift with `closed_at IS NULL`?"* and a backdated close is a perfectly well-formed answer to that question. **The guard is not wrong; the data it was given is.**

**This is the corpus's recurring shape, and this instance has a new edge.** Features **523**, **524**, **531**, **532**, **533**, **534**, **535**, **536**, **537**, **538** and **539** have each found a fact that can be silently *replaced*. **This is the first one about a fact that can be stored as a contradiction** — and the contradiction is invisible in the number the owner reads.

**Cost:** one `CHECK` constraint, one regression test, one charter sentence. **No new table, no new column, no route, no UI change, no migration directory** (charter §3.2 — **do not silently introduce Alembic**). **Rollback:** drop the constraint; no data is lost, because a row that violates it cannot exist once the constraint is in place.

## Evidence

**Parent-run, 2026-11-28.** Full probe: `/opt/data/le31-brainstorm-2026-11-28-scripts/probe_1128.py` and `probe_two_numbers.py`; environment `/opt/data/le31-verify-2026-11-11/.venv` (`sqlmodel 0.0.48`, `SQLAlchemy 2.1.8`).

**Constraint census, read back from the CREATED database:**

```
  10 tables: app_user, batch, bill, derived_tip, menu_item, order_item,
             shift, stock_entry, table_, visit
  CHECK constraints across all ten tables : 0
  UNIQUE constraints                     : bill.visit_id   (the only one)
```

**Probe C — the shift span:**

```
  UPDATE shift SET closed_at = '2026-11-26 20:00:00' WHERE id = 1   ->  ACCEPTED

  shift.opened_at = 2026-11-27 08:00:00.000000
  shift.closed_at = 2026-11-26 20:00:00+00:00

  num1  shift duration (closed_at - opened_at)   = -12.0 hours
  num2  open shifts (closed_at IS NULL)          = 0     (it is the only shift)
  num3  total shifts                             = 1

  the stored money verdict, UNCHANGED by the backdating:
    opening_float = 100.00
    counted_cash  = 100.00
    variance      = 0        <- "the drawer balanced", on a -12 hour shift
```

**The guard's own words** (quoted verbatim from `features/426-…md`, *Implementation steps* 3):

> *"Implement the open-shift guard as a query for an existing open shift (`closed_at IS NULL`) before inserting a new one; return **409** with a message naming the open shift's id. **The guard is a query, not a database constraint** — feature 404's territory, and adding a partial unique index here would be that feature's territory."*

**Corpus sweep, parent-run, over 575 feature contracts + 526 HANDOFFs (1,101 files):**

| sweep | hits | what the hits are |
|---|---|---|
| `shift.{0,40}(opened_at\|closed_at).{0,60}(immutab\|rewrit\|mutab)` | 1 | feature **536** — the **float's** mutability, not the timestamps' ordering |
| `shift.{0,60}closed_at.{0,60}(before\|ordering\|constraint)` | 2 | feature **426** + its HANDOFF — the **open-shift guard**, a rule about *how many* shifts are open |
| `closed_at.{0,40}opened_at.{0,60}(before\|shift)` | 4 | feature **426** + HANDOFF again, plus features **415** and **428** — the latter two are **`visit`**-level notes |

**⚠️ NOT PROVED, AND STATED PLAINLY:** the **Postgres** behaviour of the constraint was **not** executed — `psycopg` is not importable in the verification environment. The Postgres row is proved from the DDL rendering and the dialect's documented `CHECK` semantics, **not** from a live round trip. **Do not report the Postgres behaviour as tested.**
