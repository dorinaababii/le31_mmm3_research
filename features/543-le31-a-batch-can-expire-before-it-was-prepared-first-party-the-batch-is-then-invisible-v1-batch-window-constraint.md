# Feature 543 — A batch can expire before it was prepared: `Batch.expires_at` is unconstrained against `Batch.prepared_at`, and the batch becomes permanently invisible to the active-batch rule

> **Pick B of Daily Brainstorm 2026-11-28 (110th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Batch`, verbatim (lines 96–110):
>
> ```python
> class Batch(SQLModel, table=True):
>     """A concrete prepared quantity of a MenuItem for a specific day.
>
>     E.g. '8 pieces of Tiramisu, prepared 09:00 today'.
>     """
>     __tablename__ = "batch"
>
>     id: int | None = Field(default=None, primary_key=True)
>     menu_item_id: int = Field(foreign_key="menu_item.id")
>     qty_start: int
>     qty_remaining: int
>     prepared_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     expires_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     photo_url: str | None = None
>     notes: str | None = None
> ```
>
> **A batch is a preparation window: it is prepared at an instant and it expires at a later instant. `expires_at` is nullable and unconstrained against `prepared_at`.** The schema has **zero `CHECK` constraints** across all ten tables (read back from the created database — see *Evidence*).
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one menu item, one batch prepared `2026-11-20 09:00Z` and expiring `2026-11-21 09:00Z`, and one server):
>
> ```
>   UPDATE batch SET expires_at = '2026-11-19 09:00:00' WHERE id = 1   ->  ACCEPTED
>
>   batch.prepared_at = 2026-11-20 09:00:00.000000
>   batch.expires_at  = 2026-11-19 09:00:00+00:00     <- ONE DAY BEFORE it was prepared
> ```
>
> **⭐ TWO NUMBERS THAT MUST AGREE, AND THEY DISAGREE.**
>
> | number | value |
> |---|---|
> | the batch's own lifetime, `expires_at − prepared_at` | **−24.0 hours** |
> | the number of batches the active-batch predicate sees | **0** — while the batch still holds **10** units of stock |
>
> **⭐ AND THE CONSEQUENCE IS NOT "AN EXPIRED BATCH" — IT IS "A BATCH THAT WAS NEVER ALIVE".** Feature **404** owns the active-batch predicate — *"a batch is active if `expires_at IS NULL OR expires_at > now()`"* — and feature **447** owns the refusal to sell from an expired batch. Both of those rules read `expires_at` as *"the instant this batch stops being usable"*. **A batch whose `expires_at` precedes its `prepared_at` was never usable at all**, and the two rules cannot tell the difference: the batch simply falls out of every active-batch query **forever**.
>
> Executed: with `expires_at = 2026-11-19 09:00Z` and `prepared_at = 2026-11-20 09:00Z`, the active-batch predicate returned **0** batches while the batch row still carried `qty_remaining = 10`. **Ten prepared tiramisus exist, and no query can find them.**
>
> **⭐ AND THE STOCK IS REAL.** The batch points at a `menu_item_id`, holds `qty_start`/`qty_remaining`, and — under feature **374**'s remedy — its stock is the sum of its `StockEntry` rows. When feature **374** lands, the batch's `qty_remaining` disappears and every read becomes `SUM(stock_entry.qty_delta) WHERE batch_id = X`. **That derivation does not consult `expires_at` at all** — so after 374 lands, the ledger says the batch holds its stock and the active-batch predicate says the batch does not exist. **Two numbers that must agree, disagreeing.**
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all **575** feature contracts and **526** HANDOFFs (1,101 files) returns **zero first-party hits** for a rule that a batch's expiry must not precede its preparation:
>
> | sweep | hits | what they are |
> |---|---|---|
> | `expires.{0,40}(before\|earlier than\|prepared)` | **0** | — |
> | `expires_at.{0,60}(before\|prepared_at\|ordering)` | 1 | feature **453**'s *list of eight `datetime` columns* — a column inventory, not a rule |
> | `batch.{0,50}expires_at.{0,50}(before\|order\|constraint)` | 4 | features **412** and **424** — **both third-party vocabulary references**, plus two HANDOFFs of the same; **zero first-party rules** |
>
> **Every first-party feature that touches `batch.expires_at` owns a *different* rule about it:**
>
> | rule | mechanism | owner |
> |---|---|---|
> | the **active-batch predicate** (`expires_at IS NULL OR expires_at > now()`) | a helper | feature **404** |
> | refusing to sell from an **expired** batch | a write-path precondition | feature **447** |
> | **deriving** `qty_remaining` from the ledger | removing a column | feature **374** |
> | the batch's **preparer** (no actor column exists) | a nullable column | feature **445** |
> | the **order-line → batch** provenance | a pointer + a selection rule | feature **385** |
> | the batch's **dish** coherence with the ledger row | a write-path rule | feature **441** |
> | **a batch that expires before it was prepared** | **a `CHECK` constraint** | **THIS SLICE** |
>
> **Feature 447's own *Out of scope* says, verbatim:** *"**The active-batch predicate itself.** Feature **404** owns the rule … This feature consumes that rule; it does not redefine it."* — 447 **consumes** `expires_at`; it does not say the column may hold an impossible value. **Feature 404's *Open questions* 3 asks *"who sets `expires_at` in practice?"* — it does not ask whether the value may be impossible.**

## Goal

**Make it impossible to store a `Batch` whose `expires_at` precedes its `prepared_at`, so that "active" and "exists" stop being different questions.**

The single sentence this feature exists to make true: *a batch that expires did not expire before it was made.*

## Scope

- A **`CHECK` constraint on `batch`** that refuses a row whose `expires_at` is non-null and earlier than `prepared_at`.
- The constraint in the **portable subset** that behaves identically on SQLite (LE31's dev database, charter §3.1) and Postgres (production).
- One **regression test** that fails on today's schema and passes on the fixed one.
- One **documented note** in `PROJECT_CHARTER.md` §4 recording that a batch's preparation window is bounded.

## Out of scope

- **The active-batch predicate.** Feature **404** owns `"expires_at IS NULL OR expires_at > now()"` and its NULL-safety reasoning. **This slice does not change the predicate, does not change which batches it selects, and does not decide 404's *Open questions* 1 (option A vs option B) or its *Open questions* 2 (what a service day is).**
- **The refusal to sell from an expired batch.** Feature **447** owns that write-path precondition and its *Open questions* 1 (*"is an expiry a hard safety deadline or a freshness estimate?"*). **This slice does not change when a sale is refused** — it only ensures that the value 447 reads was not impossible when it was stored.
- **Deriving `qty_remaining` from the ledger.** Feature **374** owns the column removal and the opening-balance design. **This slice does not remove, rename or derive any column**, and **does not touch `qty_start`**. 374's own *Open questions* 1 (keep `qty_start` or make the `initial` `StockEntry` the sole opening-balance source) is **not answered here**.
- **The batch's preparer.** Feature **445** owns the missing actor column. **This slice does not add an actor column.**
- **Order-line → batch provenance and batch selection.** Feature **385** owns it; feature **441** owns the dish-coherence rule between a ledger row's batch and its order line. **Neither is touched.**
- **The batch's expiry default.** Feature **404**'s *Open questions* 3 (*"who sets `expires_at` in practice?"*) and its option B (a default of end-of-service-day) are **404's**. **This slice adds no default and no writer.**
- **`Visit.closed_at` vs `Visit.opened_at`.** That is **feature 542** — a different table, a different rule. **Do not bundle.**
- **`Shift.closed_at` vs `Shift.opened_at`.** That is **feature 544** — a different table, a different rule. **Do not bundle.**
- **Any `CHECK` on the silent-corruption columns.** Feature **404** (the other file of that number) proposes type constraints; feature **413** is about database triggers. **This is a third, separate `CHECK` family** — a *temporal ordering* constraint, not a *type* constraint and not a trigger. **Do not bundle.**

## Description

### The defect

`Batch` describes a concrete prepared quantity — *'8 pieces of Tiramisu, prepared 09:00 today'* — and carries two business times: `prepared_at` and `expires_at`. **A window whose end precedes its start is not a short window; it is an impossible one.** The schema does not say the end must come after the start, and the schema is the only thing that can say it: feature **404**'s predicate and feature **447**'s refusal are both *readers* of `expires_at`, and neither reader can detect that the value they read was never a possible value.

### The mechanism

A `CHECK` constraint on `batch`:

```sql
CHECK (expires_at IS NULL OR expires_at >= prepared_at)
```

**⚠️ THE NULL-SEMANTICS TRAP (feature 91's shape).** A `CHECK` constraint evaluating to `NULL`/`UNKNOWN` **passes** in SQL three-valued logic — it does **not** reject the row. `expires_at IS NULL OR expires_at >= prepared_at` writes the NULL case **explicitly true**, rather than relying on `NULL >= prepared_at` being `NULL`. **The other way round would silently permit every batch with no expiry** — which is *most* of them, because `expires_at` is nullable and feature **404**'s *Open questions* 3 records that *"no writer"* sets it today. **Read feature 91 before writing the constraint.**

**⚠️ THE CROSS-ENGINE-TYPE TRAP.** Both columns are `DateTime(timezone=True)` → `DATETIME` on SQLite, `TIMESTAMPTZ` on Postgres. Feature **453** proved by execution that **SQLite silently drops the UTC offset** on these columns. The constraint must therefore:
- use a **plain comparison**, not a `strftime`/`typeof` expression (those are SQLite-only, and feature **453** already proved that a SQLite-only expression is a dev/prod divergence);
- be accompanied, if the owner wants belt-and-braces, by a **SQLite-only type check behind a dialect switch** — exactly as feature **404**'s *Open questions* 1 describes for its own constraints.

### Why a `CHECK` and not a write-path guard

The same argument feature **542** makes, applied to the batch:
1. **There is no writer.** Feature **453** records that `expires_at` has no writer; feature **404**'s *Open questions* 3 asks who will set it. **A write-path guard protects a path that does not exist.**
2. Feature **470** established the corpus's precedent: LE31's invariants are upheld **vacuously** until something enforces them, and a rule in the *application* does not constrain a *migration script*, a `psql` shell, or a direct SQL client.
3. Feature **421** made the same argument for the ledger, and feature **520** is the precedent for **adding a constraint to a table that carried zero constraints**.

**Both mechanisms are compatible.** The recommendation: **the constraint lands first**, because it holds when the write path does not exist; a write-path guard, if 404 or the prep flow later adds one, is a *better error message* on top of the same rule.

## Data model

**No new table. No new column. One constraint.**

```python
class Batch(SQLModel, table=True):
    __tablename__ = "batch"
    ...
    __table_args__ = (
        CheckConstraint(
            "expires_at IS NULL OR expires_at >= prepared_at",
            name="ck_batch_expires_after_prepared",
        ),
    )
```

> **⚠️ `SQLModel` table-arg support.** `SQLModel` 0.0.48 supports `__table_args__` on a `table=True` class. **Verify this in the target environment before relying on it** — the parent's execution environment has `sqlmodel 0.0.48` / `SQLAlchemy 2.1.8`. If `__table_args__` proves not to be honoured in the pinned version, fall back to declaring the constraint via `Column(CheckConstraint(...))` on one of the columns. **Whichever mechanism is used, the regression test must assert the *behaviour*, not the declaration form** — so the test is written against the behaviour and stays valid whichever form is used.

**Effect on the DDL** (read back from the created database after this change):

```sql
CREATE TABLE batch (
    ...
    prepared_at DATETIME NOT NULL,
    expires_at DATETIME,
    ...
    CONSTRAINT ck_batch_expires_after_prepared CHECK (expires_at IS NULL OR expires_at >= prepared_at)
);
```

**⚠️ THE CONSTRAINT CENSUS IS ALREADY AT ZERO.** The parent's probe read back the created schema: **10 tables, 0 `CHECK` constraints, exactly one `UNIQUE` constraint (`bill.visit_id`)** — the same census feature **470** recorded. **This constraint is the first `CHECK` on `batch`.**

## Implementation steps

1. **Write the regression test FIRST.** It must fail on today's schema and pass on the fixed one:
   - a `Batch` with `prepared_at = 2026-11-20 09:00Z` and `expires_at = 2026-11-19 09:00Z` → **REJECTED**;
   - a `Batch` with `prepared_at = 2026-11-20 09:00Z` and `expires_at = 2026-11-21 09:00Z` → **ACCEPTED**;
   - a `Batch` with `prepared_at = 2026-11-20 09:00Z` and `expires_at = None` → **ACCEPTED** (the no-expiry case — **this is the case a badly-written NULL check would reject**, and it is the common case today);
   - a `Batch` with `prepared_at = 2026-11-20 09:00Z` and `expires_at = 2026-11-20 09:00Z` → **ACCEPTED** (the boundary — equal is not before).
2. **Add the `CheckConstraint`** to `class Batch`.
3. **Verify the DDL** by rebuilding the schema and reading `sqlite_master` back — assert the constraint text is present.
4. **Verify the behaviour** by executing the four cases above against the rebuilt schema, not by reading the source.
5. **Add the charter note** — a sentence in `PROJECT_CHARTER.md` §4 recording that a batch's preparation window is bounded.
6. **Do not touch** `routers/`, `models.py`'s other classes, `index.html`, `qty_remaining`, or any feature contract.
7. **Run the whole test suite** and confirm the new test is the only new failure before the fix and the only new pass after it.

## Telegram interaction if any

**None.** This slice adds no Telegram surface, no bot command, and no message. It is a schema constraint and a test.

## Dependencies

- **Feature 404** (`le31-active-batch-rule-excludes-null-expiry`) — **the predicate this constraint feeds.** 404's predicate reads `expires_at`; this constraint guarantees the value it reads was possible. **404 must land first, or in the same PR** — **not because 404 would break, but because the constraint's value is realised only once there is a reader that depends on it.** Name 404 in the PR description. **No change to 404.**
- **Feature 447** (`le31-an-expired-batch-can-still-be-sold-from`) — **the consumer of the predicate.** 447's own *Out of scope* says it *"consumes"* 404's rule and *"does not redefine it"*. **This slice does not change 447's refusal.** 447's *Open questions* 1 (*"is an expiry a hard safety deadline or a freshness estimate?"*) is **not answered here** — and this constraint is compatible with either answer, because a *hard deadline* implies the deadline is after the preparation and a *freshness estimate* implies the same.
- **Feature 374** (`le31-qty-remaining-derived-not-stored`) — **the strongest reason this slice exists.** 374 removes `qty_remaining` and replaces every read with `SUM(stock_entry.qty_delta) WHERE batch_id = X` — a derivation that **does not consult `expires_at`**. After 374 lands, the ledger and the active-batch predicate can disagree about the same batch. **374 must land first, or in the same PR** — if 374 lands first without this constraint, the divergence has no guard behind it. **374's *Open questions* 1 (`qty_start` vs the `initial` entry) is not answered here.**
- **Feature 453** (`le31-sqlite-silently-drops-the-utc-offset`) — **read this before writing the constraint.** It is the authority on the SQLite `DATETIME` offset behaviour this constraint sits on top of, and it is where the *"eight `datetime` columns"* list lives — which is the only first-party corpus mention of `expires_at` near a temporal word, and which is a **column inventory, not a rule**. **No change to 453.**
- **Feature 470** (`le31-the-append-only-stock-ledger-is-protected-by-a-docstring`) — owns the ledger's *database-level* enforcement and is the corpus's precedent for *"an invariant the database must refuse"*. **Its *Adjacent evidence* is one of the places this class of defect was recorded.** **Different table, different rule — do not bundle.**
- **Feature 520** (`le31-two-tables-can-sit-on-the-same-floor-map-coordinate`) — the precedent for **adding a constraint to a table that carried zero constraints**, and for **a constraint that must work on SQLite as well as Postgres** (its *Open questions* 1). **Read it before writing the constraint.** **No change to 520.**
- **Feature 542** (`le31-a-visit-can-close-before-it-opened`) — the **sibling slice** on `visit`. Same mechanism, same shape, **different table and different rule**. They are designed to land together. **Do not merge them.**

## Open questions

1. **Should a batch's `expires_at` be allowed to equal its `prepared_at`?** **Recorded default: yes** — equal is not before, and a batch prepared and expiring at the same instant is degenerate but not impossible. **The regression test must pin this boundary.**
2. **Should the constraint be in the database, the write path, or both?** **Recorded default: in the database**, because there is no writer for `expires_at` today and a write-path rule alone would be vacuous (feature 470's precedent). A write-path guard, if one is later added, is a better error message on top of the same rule.
3. **Does the same rule apply to `Batch.prepared_at` itself being rewritten?** `prepared_at` is equally rewritable and no feature owns its mutability. **This slice does not own it** — a different question, recorded here so the next pass files it or discards it deliberately. **It is NOT taken by this slice.**
4. **Does the same rule apply to `StockEntry.at` versus the batch's `prepared_at`?** A ledger row stamped before its batch was prepared is the same class of defect on a different table, and feature **417** owns the ledger's actor and feature **421** owns where the row may be written. **It is recorded here and NOT taken by this slice.**
5. **Should an already-stored impossible batch be repaired on migration?** **Recorded default: this slice does not migrate data.** LE31 v1 uses `init_db()` (charter §3.2), so there is no migration path to hang a repair on; and **today no code writes `expires_at`**, so there is no production data with an impossible value. **If a repair is ever needed, it is a separate change** — and it must be recorded as one.

## Why this matters

**The batch is the unit of prepared stock, and "active" is the question every stock query asks.**

Feature **404**'s predicate is the single definition of what a usable batch is, and feature **447**'s refusal is built on it. Together they are the mechanism by which LE31 decides *there is food to sell*. **A batch whose expiry precedes its preparation is not "expired food" — it is a batch that was never in service**, and the predicate cannot tell those apart: the batch drops out of every active-batch query and stays out, forever.

**Ten prepared portions of tiramisu exist. The ledger says so. No query can find them.** That is not a data-integrity nit; it is **stock that the restaurant owns and cannot see**, and — under feature **374**'s remedy — the derivation that *does* find it (`SUM(stock_entry.qty_delta)`) does not consult `expires_at` at all, so the two disagree permanently and silently.

**Why this one matters more than a routine constraint addition:**

1. **The corpus recorded the class and never the instance.** Features **470**, **471**, **452**, **460**, **520**, **523**, **531**–**539** have each recorded a *"recorded, not filed"* or *"not taken by this slice"* instance of the same family. **This is another one, and it is the first one where the *value* is impossible rather than merely unrecorded** — the others concern a fact that can be silently replaced; this one concerns a fact that can be stored as a contradiction.
2. **It lands with a feature that will make the disagreement worse.** Feature **374** replaces the stored `qty_remaining` with a ledger derivation. **That is a strict improvement to the stock number and it makes this defect materially worse**, because from 374 onward the stock and the batch's visibility are read from two different places and can never agree. **374 must land first, or in the same PR.**
3. **The cost is one line and it is reversible.** One `CHECK` constraint, one regression test, one charter sentence. **No new table, no new column, no route, no UI change, no migration directory** (charter §3.2 — **do not silently introduce Alembic**). **Rollback:** drop the constraint; no data is lost.

## Evidence

**Parent-run, 2026-11-28.** Full probe: `/opt/data/le31-brainstorm-2026-11-28-scripts/probe_1128.py` and `probe_two_numbers.py`; environment `/opt/data/le31-verify-2026-11-11/.venv` (`sqlmodel 0.0.48`, `SQLAlchemy 2.1.8`).

**Constraint census, read back from the CREATED database:**

```
  10 tables: app_user, batch, bill, derived_tip, menu_item, order_item,
             shift, stock_entry, table_, visit
  CHECK constraints across all ten tables : 0
  UNIQUE constraints                     : bill.visit_id   (the only one)
```

**Probe B — the batch window:**

```
  UPDATE batch SET expires_at = '2026-11-19 09:00:00' WHERE id = 1   ->  ACCEPTED

  batch.prepared_at = 2026-11-20 09:00:00.000000
  batch.expires_at  = 2026-11-19 09:00:00+00:00

  num1  batch lifetime (expires_at - prepared_at)          = -24.0 hours
  num2  active batches under 404's predicate
          (expires_at IS NULL OR expires_at > now)          = 0
  num3  the batch's own qty_remaining                       = 10

  -> the batch is invisible to every active-batch query
     while still holding ten units of stock
```

**Feature 447's own words** (quoted verbatim from `features/447-…md`, *Out of scope*):

> *"**The active-batch predicate itself.** Feature **404** owns the rule *"`expires_at IS NULL OR expires_at > now()`"*. **This feature consumes that rule; it does not redefine it.**"*

**Corpus sweep, parent-run, over 575 feature contracts + 526 HANDOFFs (1,101 files):**

| sweep | hits | what the hits are |
|---|---|---|
| `expires.{0,40}(before\|earlier than\|prepared)` | **0** | — |
| `expires_at.{0,60}(before\|prepared_at\|ordering)` | 1 | feature **453**'s *list of eight `datetime` columns* — an inventory, not a rule |
| `batch.{0,50}expires_at.{0,50}(before\|order\|constraint)` | 4 | features **412** and **424** — **third-party vocabulary references** — plus two HANDOFFs of the same. **Zero first-party rules.** |

**Neighbours' own scope statements, quoted verbatim:**

- **404** (*Open questions* 3): *"**Who sets `expires_at` in practice?** … This slice does not add a writer."* — **the writer is 404's question; the value's possibility is this slice's.**
- **447** (*Out of scope*): quoted above — **consumes, does not redefine.**
- **374** (*Out of scope* / *Open questions* 1): owns the column removal and the opening-balance design; *"This feature does not remove, rename or derive any column."*

**⚠️ NOT PROVED, AND STATED PLAINLY:** the **Postgres** behaviour of the constraint was **not** executed — `psycopg` is not importable in the verification environment. The Postgres row is proved from the DDL rendering and the dialect's documented `CHECK` semantics, **not** from a live round trip. **Do not report the Postgres behaviour as tested.**
