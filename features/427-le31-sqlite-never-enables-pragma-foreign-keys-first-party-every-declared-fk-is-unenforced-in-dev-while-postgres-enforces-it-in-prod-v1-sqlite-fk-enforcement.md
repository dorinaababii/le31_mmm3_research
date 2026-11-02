# Feature 427 — SQLite never enables `PRAGMA foreign_keys`, so every foreign key LE31 declares is UNENFORCED in dev while Postgres enforces it in prod

> **Pick B of Daily Brainstorm 2026-11-02 (95th pass).** **FIRST-PARTY — the defect is in LE31's own code, and it is proven by EXECUTION, not by reading.**
>
> `backend/app/db.py` (the whole file, 29 lines):
>
> ```
> 12: engine = create_engine(
> 13:     settings.database_url,
> 14:     echo=False,
> 15:     # Required for SQLite (no-op for Postgres)
> 16:     connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {},
> 17: )
> ```
>
> **There is no `PRAGMA foreign_keys` anywhere in LE31's backend.** The parent
> proved the consequence against a real SQLite database built from LE31's own
> `models.py` (`_exec_proof_2026_11_02.py`):
>
> ```
> --- PROOF 3: does SQLite enforce the FKs LE31 *does* declare? ---
>        PRAGMA foreign_keys = 0  (SQLite default is 0/OFF)
> PASS PROOF 3   SQLite FK enforcement pragma is OFF by default   PRAGMA foreign_keys=0 -> declared FKs are NOT enforced on this connection
> PASS PROOF 3b  with pragma ON, a dangling batch_id is REJECTED  rejected: IntegrityError
>
> --- PROOF 5: LE31's engine does NOT enable PRAGMA foreign_keys ---
>        backend/app/db.py mentions 'foreign_keys': False
> PASS PROOF 5   LE31's own engine does NOT enable SQLite FK enforcement db.py has no 'foreign_keys' pragma -> every declared FK is unenforced in dev
> ```
>
> **The constraint exists and the mechanism is switched off.** With the pragma
> ON, the *same* insert that SQLite happily stores is rejected with an
> `IntegrityError`. LE31 declares eight foreign keys. In dev, **none of them
> is enforced.**
>
> Bucket: **v1 (dev/prod referential-integrity parity — the fifth first-party defect of the brainstorm series)** — Pick B of Daily Brainstorm 2026-11-02. Build verdict: **`build`** (first-party fix: one SQLite `connect` event listener + one regression test).

## Goal

Make LE31's **declared** foreign keys **actually enforced** on the database LE31
develops and tests against — so that a row the development database accepts is
a row the production database also accepts.

**The single sentence this feature exists to make true:** *the database LE31
tests against enforces the same rules the database LE31 runs against.*

Two concrete outcomes:

1. **`PRAGMA foreign_keys = ON` on every SQLite connection** the application
   opens. The eight foreign keys LE31 already declares — `batch_id`,
   `by_user_id` (once feature 417 lands), `menu_item_id`, `visit_id`,
   `table_id`, `server_id`, `closed_by`, `bill_id` — become **enforced**.
2. **The dev/prod divergence is written down**, so the next field added to
   LE31's schema does not assume that "declared" means "enforced".

## Scope

**In scope (v1):**
- Add a SQLAlchemy `connect` event listener on the engine that executes
  `PRAGMA foreign_keys = ON` for SQLite connections only.
- One regression test that proves a dangling foreign key is **rejected** on the
  SQLite connection LE31's own `get_session()` hands out.
- One documented note in `backend/README.md` (or the equivalent) recording that
  SQLite requires the pragma **per connection**, and that the pragma is a
  **no-op on Postgres** (which enables foreign keys by default).
- One row in `INDEX.md`'s "Active feature pipeline" table.

## Out of scope

- **Adding any foreign key.** The schema already declares eight. This feature
  changes **the mechanism**, not the schema. Adding a *new* foreign key is a
  separate feature — in particular **feature 426** (`le31-stockentry-ref-order-item-id-foreign-key`), which adds the ninth, and **feature 417**, which adds the actor FK to `StockEntry.by_user_id`. **⏱️ ORDERING: this feature (427) lands FIRST, or in the same PR — features 417 and 426 are inert without it.** Their contracts name this ordering explicitly.
- **Any change to `backend/app/models.py`.** No column, no constraint, no
  table. This is an engine-level change.
- **Enabling `CHECK` constraints or `STRICT` tables.** That is **feature 404**
  (`le31-sqlite-tables-not-strict`). **Do not bundle** — different mechanism,
  different failure mode.
- **`ON DELETE` / `ON UPDATE` cascade semantics.** This feature enables
  enforcement of the constraints **as declared**. It does not decide what
  should happen on delete. (`ON DELETE` appears in **2** feature contracts in
  the corpus; this is not one of them.)
- **Alembic.** §3.2's stated v1 policy is `init_db()`.
- **Any change to `Batch`, `StockEntry`, `Visit`, `OrderItem`, `Bill`,
  `DerivedTip`, `Shift`, `MenuItem`, `AppUser` or `Table`.**
- **Making SQLite the production database.** §3.1 says *"SQLite for dev, Postgres for prod."* This feature closes the *behavioural* gap between them; it does not change the deployment decision.
- **WAL mode, busy timeout, or any other SQLite pragma.** Not this feature's business.

## Description

### The defect, as observed by execution on 2026-11-02

Parent-verified against a real SQLite database built from LE31's own `models.py`.
Re-runnable: `_exec_proof_2026_11_02.py`.

| Probe | Result |
|---|---|
| `PRAGMA foreign_keys` on a stock SQLite connection | **`0`** — SQLite's default is OFF |
| `backend/app/db.py` mentions `foreign_keys` | **`False`** — the pragma is never enabled |
| `INSERT INTO stock_entry (batch_id=777777, …)` with the pragma **OFF** | **ACCEPTED** — a row pointing at a batch that does not exist |
| The *same* insert with `PRAGMA foreign_keys=ON` | **REJECTED** — `IntegrityError` |

### What LE31 declares, and what it therefore does not enforce

Read from `backend/app/models.py` by AST on 2026-11-02. **These are the
constraints that are declared. With the pragma off, none of them fires.**

| Table | Column | References |
|---|---|---|
| `batch` | `menu_item_id` | `menu_item.id` |
| `stock_entry` | `batch_id` | `batch.id` |
| `visit` | `table_id` | `table_.id` |
| `visit` | `server_id` | `app_user.id` |
| `order_item` | `visit_id` | `visit.id` |
| `order_item` | `menu_item_id` | `menu_item.id` |
| `bill` | `visit_id` | `visit.id` (unique) |
| `bill` | `closed_by` | `app_user.id` |
| `derived_tip` | `bill_id` | `bill.id` (primary key) |
| `shift` | `by_user_id` | `app_user.id` |

**Ten declared foreign keys. Zero enforced on the development database.**

### Why this is worse than it looks, and better at the same time

**Worse:** the development database is the one the team tests against. Every
manual test in the charter — *"order a tiramisu → stock goes 8 → 7 → ledger has
one entry"* — runs on a database that accepts rows Postgres would reject. So a
constraint that *looks* implemented is **never exercised in dev**, and the
first time it matters is in production, on a real bill.

**Better:** this is the cheapest defect in the series to fix. It is **one
event listener** and **no schema change at all**. And it is the **prerequisite**
for two other filed features — feature 417 (the actor foreign key) and feature
426 (the order-line foreign key) — both of which are **inert** without it.

### The asymmetry, stated precisely

| | SQLite (dev) | Postgres (prod) |
|---|---|---|
| Foreign keys declared in the schema? | yes | yes |
| Foreign keys **enforced** by the database? | **NO** (pragma off) | **yes** (on by default) |
| A dangling reference is | **stored silently** | **rejected** |

**Consequence:** a bug that writes a dangling reference **passes every
development test and fails in production.** This is the same *class* of defect
as feature 411 (money precision: *"declared but not enforced — `Decimal("12.345")`
is silently coerced"*), but it sits on the **referential-integrity** axis, and
it has not been filed.

### The external instrument: an in-window third-party vocabulary

`Raktim94/nodedr-restaurant-pos` (AGPL-3.0 → §3.2 strictly-incompatible →
**vocabulary only**; NestJS/Prisma/PostgreSQL **off-stack**; ★279, created
2026-08-03, pushed 2026-11-02 = in-window by push only; 28,111 B README read
in full). Its README records, verbatim:

> *"**Postgres/Prisma**"* and *"Full rationale for every choice — including why NestJS over the plain-Express pattern its sister project uses, and **why Postgres over the originally-specced SQLite** — is in [`ARCHITECTURE.md`](./ARCHITECTURE.md)."*

and its roadmap explicitly lists, verbatim:

> *"**What is not built yet?** Native payment-gateway checkout, direct accounting-software and delivery-platform connectors, weighing-scale and label printers, **a SQLite edition** and native installers. The [roadmap](./ROADMAP.md) is explicit about what is done and what is not."*

**The transferable item is the vocabulary of naming the dialect the schema is
written against, and treating the other dialect's behaviour as a distinct
thing to reason about rather than an assumption.** LE31's charter says
*"SQLite for dev, Postgres for prod. Same SQLModel code for both."* — and the
two dialects do **not** behave the same on this axis. No code is adopted from an
AGPL-3.0, off-stack project; the **shape** is the transfer.

## Data model

**No schema change.** This is the whole point: the constraints already exist.

```python
# backend/app/db.py — the engine definition (lines 7-17), before

from sqlmodel import SQLModel, Session, create_engine

from .config import settings

# `echo=False` keeps logs clean; flip to True to see every SQL statement.
engine = create_engine(
    settings.database_url,
    echo=False,
    # Required for SQLite (no-op for Postgres)
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {},
)
```

```python
# backend/app/db.py — the engine definition, after

from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import event

from .config import settings

engine = create_engine(
    settings.database_url,
    echo=False,
    # Required for SQLite (no-op for Postgres)
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {},
)


@event.listens_for(engine, "connect")
def _enable_sqlite_foreign_keys(dbapi_connection, connection_record):
    """Turn on SQLite's foreign-key enforcement. OFF by default since SQLite 3.6.

    SQLite does NOT enable foreign-key enforcement unless this pragma is set on
    EVERY connection. Postgres enforces foreign keys by default, so without this
    the dev database accepts rows the production database rejects.

    `PRAGMA foreign_keys` is a no-op on Postgres, but the listener is scoped to
    SQLite connections so the behaviour is identical on both engines.
    """
    if settings.database_url.startswith("sqlite"):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
```

### The pragma, per dialect

| Dialect | Default | Effect of the pragma |
|---|---|---|
| SQLite | **OFF** (since 3.6, per connection) | turns constraint checking on |
| Postgres | **ON** | no-op — the listener does not run for Postgres connections |

**Note on the listener's guard.** The check is on `settings.database_url`
(the configured URL), not on the connection object, because SQLAlchemy's
`connect` event fires for every dialect and the safest form is to test the
configured engine up front. If the URL is swapped at runtime, the guard must
move with it.

## Implementation steps

1. **Add the listener** to `backend/app/db.py` as shown above. Import
   `event` from `sqlalchemy`. **One import, one function, one registration.**
2. **Verify the pragma is on.** From a session created by LE31's own
   `get_session()`, run `PRAGMA foreign_keys` and assert it returns `1`
   (not `0`).
3. **Add the regression tests:**
   - `test_sqlite_enforces_foreign_keys` — insert a `StockEntry` naming a
     nonexistent `batch_id`; assert the write is **rejected** with an
     `IntegrityError`.
   - `test_declared_foreign_keys_are_present` — assert that, for the tables
     that declare them, `PRAGMA foreign_key_list(<table>)` lists the expected
     columns. This makes the assertion **specific** (the *declared* set) rather
     than a generic "some FK exists" check, which would pass vacuously.
   - `test_null_foreign_key_is_still_allowed` — insert a `StockEntry` with
     `ref_order_item_id=None` (once feature 426 lands) and assert it is
     **accepted**. A foreign key must not turn a nullable column into a
     required one.
4. **Document the dialect difference** in `backend/README.md`: *"SQLite requires
   `PRAGMA foreign_keys=ON` per connection; Postgres enforces foreign keys by
   default. LE31's dev engine enables it in `backend/app/db.py`."* One or two
   sentences.
5. **Check the existing test-suite fixtures.** If any existing test or fixture
   relies on writing a dangling reference, it will now fail — **that is the
   point**, and each such failure must be inspected, not blanket-fixed. Record
   every one that surfaces; a fixture that was writing a dangling reference was
   itself carrying an undeclared assumption.
6. **Add one row** to `INDEX.md`'s "Active feature pipeline" table.
7. **Run the LE31 test suite** and confirm no regressions.

## Telegram interaction if any

**None.** This is an engine-level configuration change. No Telegram command,
no FSM state, no message changes.

The operator-visible consequence is **negative and desirable**: the database
now refuses rows it previously accepted. Since no write path exists for the
ledger yet (verified by execution: zero `StockEntry(` construction sites), and
`backend/app/routers/` holds only `__init__.py` and `tables.py`, **there is no
live flow to break today.**

## Dependencies

- **Feature 417 (`le31-stockentry-actor-foreign-key`)** — **downstream beneficiary.** Its foreign key to `StockEntry.by_user_id` is **declared but unenforced** until this feature lands. Its contract states the same ordering; the two must agree.
- **Feature 426 (`le31-stockentry-ref-order-item-id-foreign-key`)** — **downstream beneficiary.** Same: inert without the pragma. **Its contract names this feature explicitly as the "must land first" dependency.**
- **Feature 404 (`le31-sqlite-tables-not-strict`)** — **adjacent, not blocking.** It adds `CHECK` constraints and `STRICT` tables; those are a *different* mechanism, and `CHECK` constraints in SQLite are honoured independently of the foreign-key pragma. **Do not bundle.** Its own deferral note about `ref_order_item_id` must still be amended (by feature 426, step 4) — that amendment is independent of this feature.
- **Feature 411 (`le31-money-precision-guard`)** — **sibling pattern.** The same *declared-but-not-enforced* shape on the money axis. **Not a dependency** — but the two should be read together, and the PR descriptions should cross-reference so a future pass does not file the same shape twice.
- **Feature 421 (`le31-stockentry-append-only-linter-rule`)** — **adjacent mechanism.** A linter rule (app layer) and a database constraint (data layer) are different instruments. 421 owns the linter; this feature owns the constraint. **Do not implement 421's rule here.**
- **`sqlalchemy`** — already a transitive dependency via `sqlmodel`. **No new dependency.** The `event` module ships with SQLAlchemy.

## Open questions

1. **Should the pragma be enabled in `init_db()` as well, or only on the event listener?** The event listener covers every connection the application opens, including `init_db()`'s. **Recorded default: the listener alone.** `init_db()` uses the same engine, so the listener fires for it too. A belt-and-braces `PRAGMA` inside `init_db()` would be redundant — and would create a second place to forget to update.
2. **What about `PRAGMA foreign_keys` and `legacy_alter_table` / table rebuilds?** SQLite's documented quirk: `PRAGMA foreign_keys` is a **no-op inside a transaction**, and altering a table with foreign keys enabled requires care. **Recorded default: defer.** LE31 uses `init_db()` (no migrations) per §3.2, so no table is rebuilt today. **When Alembic arrives (post-v1), this must be revisited** — it is recorded here as known debt.
3. **Should the pragma be configurable?** **Recorded default: no.** A configuration flag that can switch off the enforcement the feature exists to enable is a footgun; if a test needs to bypass it, it can open its own connection.
4. **Does this change what feature 404's `CHECK`-constraint work must do?** SQLite honours `CHECK` constraints independently of the foreign-key pragma, so **no** — but this is recorded so the two features' implementers do not assume a dependency that does not exist.

## Sources

- **LE31's own code** — `backend/app/db.py` (all 29 lines), read on 2026-11-02.
- **LE31's own code** — `backend/app/models.py`, `class StockEntry` and the FK inventory extracted by AST, read on 2026-11-02.
- **LE31's charter** — `PROJECT_CHARTER.md` §3.1 (*"SQLite for dev, Postgres for prod. Same SQLModel code for both."*), §4.1 (the stack table), §3.2 (the Alembic non-goal).
- **Execution proof** — `_exec_proof_2026_11_02.py`, run 2026-11-02 against a throwaway SQLite database built from LE31's own `models.py`. Probe 3 (`PRAGMA foreign_keys = 0`), Probe 3b (with the pragma ON the dangling insert raises `IntegrityError`), Probe 5 (`db.py` contains no `foreign_keys`).
- **Third-party instrument (vocabulary only)** — `Raktim94/nodedr-restaurant-pos`, GitHub API `/repos/` GET on 2026-11-02, HTTP 200: ★279, AGPL-3.0, NestJS/TypeScript **off-stack**, created 2026-08-03, pushed 2026-11-02 = **in-window by push only** (created 3 months before the 2026-10-03 window start — **not a fresh discovery**), 28,111 B README read in full. **AGPL-3.0 → §3.2 strictly-incompatible → no code is adopted; the shape is the transfer.**
- **Corpus evidence** — `grep -rilE 'pragma' features/*.md` → **4 files** (404, 417, 423, 424); none of them enables foreign-key enforcement. `grep -riE 'foreign key.{0,60}enforc|enforc.{0,60}foreign key' features/*.md` → **1 file** (417), and 417's own DDL block shows the FK *declared*, not enforced.

## Why this matters

**Because "declared" and "enforced" are different words, and LE31 has been
writing the first one in a schema while the database only ever honoured the
second.**

This is the cheapest fix in the series and the **prerequisite for two others**,
which is exactly why it belongs at the front of the queue rather than the back:

- **One event listener.** No schema change, no migration, no new dependency.
- **It makes features 417 and 426 real.** Both add foreign keys. Without the
  pragma they add *decorations*.
- **It closes the dev/prod gap on the axis where a silent difference is
  most expensive.** Money precision (feature 411) differs by *coercion*;
  referential integrity differs by *acceptance*. A dangling ledger row
  accepted in dev and rejected in prod is the definition of a bug that ships.

And there is a second-order reason to file it today rather than later:
**the moment `backend/app/routers/` gains a stock-writing router, this stops
being a configuration nicety and becomes the difference between a development
database and a production database having the same rules.** The write path is
the natural next piece of work — the ledger has **zero** construction sites
today — so this feature is cheap precisely *now* and expensive after.

**Finally, it is the same shape as the money-precision defect, which is
precisely why it was filed.** Feature 411 asked *"what does 'Decimal' mean
here, and is that meaning enforced?"* This feature asks the same question
about a foreign key: **you have written the constraint down; who is
responsible for making the database obey it?** The answer, today, is nobody.

## Adjacent evidence

| # | Item | Relationship |
|---|---|---|
| 1 | **Feature 417** — `StockEntry.by_user_id` FK | **Downstream beneficiary.** Inert without the pragma. |
| 2 | **Feature 426** — `StockEntry.ref_order_item_id` FK | **Downstream beneficiary.** Inert without the pragma. |
| 3 | **Feature 404** — SQLite not `STRICT` | **Adjacent mechanism, different axis.** `CHECK` constraints are honoured independently of the pragma. **Not a dependency; do not bundle.** |
| 4 | **Feature 411** — money precision declared not enforced | **Sibling pattern.** Same *class* of defect, different axis. Read together. |
| 5 | **Feature 421** — the charter's §7 linter rule | **Adjacent mechanism.** App-layer lint vs data-layer constraint. |
| 6 | **Feature 374** — `qty_remaining` derived | **Adjacent.** The ledger's derivation; unaffected by the pragma. |
| 7 | **Feature 421 / 423 / 424** — the only other contracts mentioning `pragma` | **Recorded-not-picked.** None of them enables FK enforcement. |
