# Feature 429 — `backend/app/models.py` states *"All tables have created_at; only mutable ones get updated_at"* — and **not one table has either column**

> **Pick A of Daily Brainstorm 2026-11-03 (97th pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proven by EXECUTION, not by reading.**
>
> `backend/app/models.py`, the module docstring, lines 6-11, verbatim:
>
> ```
> 6: Conventions:
> 7: - IDs are auto-incrementing integers (SERIAL on Postgres, INTEGER on SQLite).
> 8: - Timestamps use UTC.
> 9: - Money uses Decimal (never float) — exact arithmetic.
> 10: - All tables have created_at; only mutable ones get updated_at.
> 11: """
> ```
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then `sqlalchemy.inspect`):
>
> ```
>   tables_total              10
>   tables_with_created_at    []          <-- ZERO
>   tables_with_updated_at    []          <-- ZERO
>   convention_fully_honoured false
> ```
>
> **The convention is stated universally and violated by every table in the database.** Four tables — `app_user`, `derived_tip`, `menu_item`, `table_` — carry **no timestamp column of any kind**: no `created_at`, no `updated_at`, no `at`, no `opened_at`, no `prepared_at`, nothing.
>
> **Why this is not a style note.** Line 10 is in the **docstring of the file that defines LE31's schema** — it is the first thing any coding agent reads before writing a model, a migration, or a router. An agent told to "implement the schema as described" will read line 10, believe it, and either add a `created_at` to tables that already have one, or assume the column exists and write a query against it. **LE31's schema documentation is currently a trap.**

## Goal

**Make `backend/app/models.py`'s own stated convention true, or delete the claim.**

Two acceptable end-states, and the implementer picks one and records it in the commit message:

- **(a) Honour it.** Add `created_at: datetime` to every table that lacks one, and `updated_at: datetime | None` to the mutable ones (`menu_item`, `batch`, `visit`, `order_item`, `bill`, `table_`, `shift`).
- **(b) Correct it.** If the owner prefers not to add nine columns to a v1 schema, **amend line 10 of the docstring** to state the convention the schema actually follows, so that the file stops lying to its reader.

**Either end-state is a fix. Leaving the contradiction in place is not.**

## Scope

- The **ten** tables in `backend/app/models.py`: `table_`, `app_user`, `menu_item`, `batch`, `stock_entry`, `visit`, `order_item`, `bill`, `derived_tip`, `shift`.
- The module docstring's `Conventions:` block, line 10.
- The `created_at` / `updated_at` **column definitions** and their `default_factory=utcnow` wiring — consistent with the file's existing convention at line 8 (*"Timestamps use UTC"*) and with the `utcnow()` helper already defined at line 21.
- A **migration** for existing databases. Per charter §3.2, v1 uses **`init_db()`**, **not** Alembic (*"Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod)"*). `alembic>=1.13` is already in `requirements.txt` — **do not silently introduce it.** The prod-migration step is recorded as known debt.

## Out of scope (v1)

- **Any audit-trail or "who changed what" feature.** This contract adds a timestamp; it does not build a change log. That is feature 129 / the `audit log` family.
- **Populating `created_at` for rows that already exist.** Existing rows get the column's default (the migration instant) — LE31 has no historical insertion times to backfill, and inventing them would be worse than having none. **This is a real limitation and is stated here rather than hidden.**
- **Adding `created_at` to `derived_tip`** *only if* it is created in the same transaction as its `bill` — see the Open question.
- **Any business-date column.** The *service day* is a different concept and is **feature 405**.
- **Any change to `Batch.expires_at`, `Visit.closed_at`, `Bill.paid_at`, `Shift.closed_at`** or any other existing timestamp. This contract does not touch them.
- **The `order_item` insertion-time question.** That is **feature 430** — a separate contract, because it has a different business consequence and a different owner.
- **`MenuItem.category` normalisation.** That is **feature 431**.

## Description

### What the schema actually is

The ten tables, their columns and their foreign keys, as parsed from `models.py` in-process (not by grepping the working tree):

| Table | Columns | FKs |
|---|---|---|
| `app_user` | `id, name, pin_hash, role` | — |
| `batch` | `id, menu_item_id, qty_start, qty_remaining, prepared_at, expires_at, photo_url, notes` | `menu_item` |
| `bill` | `id, visit_id, subtotal_items, subtotal_tax, total_due, total_paid, payment_method, paid_at, closed_by` | `visit`, `app_user` |
| `derived_tip` | `bill_id, amount, formula_version` | `bill` |
| `menu_item` | `id, name, category, unit_price, unit, is_prepared, photo_url` | — |
| `order_item` | `id, visit_id, menu_item_id, qty, unit_price, course, status, notes, fired_at, ready_at, served_at` | `visit`, `menu_item` |
| `shift` | `id, opened_at, closed_at, opening_float, counted_cash, variance, by_user_id` | `app_user` |
| `stock_entry` | `id, batch_id, qty_delta, reason, ref_order_item_id, by_user_id, at` | `batch` |
| `table_` | `id, label, section, seats, x, y` | — |
| `visit` | `id, table_id, server_id, opened_at, closed_at, party_size, adults, children` | `table_`, `app_user` |

**`created_at` appears in none of them. `updated_at` appears in none of them.**

The `Conventions:` block at line 10 is therefore false on **ten of ten** tables.

### The three timestamps that *do* exist are not `created_at`

It is worth being exact about why the schema is not already covered:

- `stock_entry.at` — records when the ledger row was written. `stock_entry` is **append-only**, so its write time *is* its creation time. This table needs no `created_at` under any reading of the convention.
- `batch.prepared_at` — records when the batch was **prepared**, which is a business event, not the row's insertion time. A batch row created at 08:00 for a 10:00 prep carries `prepared_at = 10:00`; those are different facts.
- `bill.paid_at`, `visit.opened_at`, `shift.opened_at` — business-event timestamps, each with its own meaning and each **set at a different moment from the row's insertion**.

So six of the ten tables (`app_user`, `menu_item`, `table_`, `derived_tip`, and — by the strict reading — `order_item` and `visit`/`bill` for their *creation* moment) have **no** field that records when the row came into existence.

### Why this matters more than it looks

Three concrete consequences, each of which will bite an implementer:

1. **The docstring is a specification, and it is false.** LE31's charter §7 demands *"End-to-end before commit. Don't commit a feature that 'compiles but doesn't work in the UI'."* The same section demands *"No dead code."* A false convention in the file's own header is neither dead code nor live code — it is **a lie the reader pays for.**
2. **Ordering becomes implicit.** With no insertion timestamp, the only ordering available on most tables is the autoincrement `id`. That is a **surrogate key**, not a business fact; it is not guaranteed monotonic across a Postgres sequence reset, a restore from backup, or a bulk data migration. `table_`, `app_user` and `menu_item` have **no** ordering column of any kind.
3. **Audit and debugging lose their ground truth.** *"When was this menu item added? When did this table row change? When was this user created?"* are questions LE31's schema currently **cannot answer** — and they are answerable today for `stock_entry` and only today because `stock_entry.at` happens to do double duty.

### The third-party instrument

`Ifazawezk/dukkan` (MIT ✓ §3.2, ★1/⑂0 — no traction evidence, FastAPI + SQLAlchemy 2 + SQLite/Postgres, created **and** pushed 2026-11-01, **in-window by both fields**, 1,719 KB, all fields parent-verified via direct `GET /repos/`) states, verbatim:

> *"**Exact money.** Amounts are stored as whole dirhams (1 QAR = 100 dirhams) and are `Decimal` in Python, so no floating point touches a price."*

and, in its layout table, a dedicated `backend/app/models` directory whose rows carry their own timestamps. Its `stock_movements` table is *"insert only"* with a `created_at`-style write time distinct from the movement's business time — the same distinction LE31's `stock_entry.at` makes and the rest of LE31's schema does not.

The transferable idea is narrow and worth stating precisely: **a row's creation time and a row's business-event time are different facts, and a schema that only keeps the second has lost the first.** LE31 already believes this for `stock_entry` (which has `at`) and for `batch` (which has `prepared_at` and `expires_at` — two business times and no creation time). The claim at line 10 says LE31 believes it everywhere. It does not.

## Data model

### Option (a) — honour the convention (additive, recommended)

Add to **every table that lacks them**:

```python
created_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
updated_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
```

- `created_at` — **all ten tables**, `default_factory=utcnow`, `DateTime(timezone=True)`, matching the existing `prepared_at` / `opened_at` / `at` wiring exactly.
- `updated_at` — **the mutable ones only**, nullable, default `None`: `menu_item`, `batch`, `visit`, `order_item`, `bill`, `table_`, `shift`. Immutable and append-only tables (`app_user` — arguably mutable, see Open question; `stock_entry` — **append-only by charter §4.3, never UPDATE**; `derived_tip` — one row per bill, written once) get `created_at` only.
- `stock_entry` keeps `at` as its business write-time and gains `created_at` as its row-insertion time — the two are set in the same statement, so they will be equal in practice, which is **fine and honest**: the point is that the convention is now true of every table, including the one that already had a timestamp.

### Option (b) — correct the convention (docstring only)

Amend line 10 to state what is true, e.g.:

```
- Tables carry a creation timestamp where one is meaningful. Append-only
  stock_entry uses `at`; business events use their own columns
  (`prepared_at`, `opened_at`, `paid_at`). Not every table has a creation time.
```

**Acceptable, and much cheaper.** It is listed first in the Goal because it is the honest minimum: **the file must stop lying.** If the owner picks (b), this contract is a one-line docstring change plus a note in the commit message, and it is **done**.

### Explicitly NOT part of the data model

- **No `updated_at` on `stock_entry`.** Charter §4.3: *"EVERY change to batch stock is a new StockEntry row. Never UPDATE or DELETE."* An `updated_at` on an append-only table is a contradiction waiting to happen.
- **No backfill of historical values.** See *Out of scope*.
- **No `business_date` / `service_date` column.** That is **feature 405**.

## Implementation steps

1. **Decide (a) or (b)** and record the choice in the commit message. Do not do both.
2. If **(a)**: add `created_at` (and `updated_at` where mutable) to each of the ten classes in `backend/app/models.py`, using the existing `utcnow` helper and the existing `Column(DateTime(timezone=True))` pattern. **Match the file's style exactly** — the timestamp columns on `batch`, `visit`, `bill`, `shift` and `stock_entry` are the template.
3. If **(a)**: extend the `init_db()` path (`backend/app/db.py`) per charter §3.2's stated v1 policy — **no Alembic**. For an existing dev database, drop and re-create (v1 data is not precious); record the prod-migration step as **known debt** in the commit message.
4. If **(b)**: amend the `Conventions:` block. Nothing else changes.
5. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test must assert the *convention*, not the implementation:
   - `test_every_table_has_created_at` — for each of the ten `__tablename__`s, the inspected column list contains `created_at`.
   - `test_no_table_has_unexpected_updated_at` — `stock_entry` does **not** have `updated_at`.
   - `test_docstring_convention_matches_schema` — **parse the module docstring** and assert that if it claims "All tables have created_at", then every table does. **This test is what stops the contradiction from coming back**, and it is the one that makes this contract worth more than a data migration.
6. **If (a)**, verify `created_at` is populated on insert without the caller passing it, and that it is **UTC** (`tzinfo` is not `None`).

## Telegram interaction if any

**None.** This is a schema and docstring change. No bot command, no waiter surface, no kitchen surface.

## Dependencies

- **Charter §7** — *"No magic numbers"*, *"End-to-end before commit"*, *"No dead code"*.
- **Charter §4.1** — SQLite (dev) / Postgres (prod), same SQLModel code for both.
- **Charter §3.2** — `init_db()` for v1; **no Alembic**; no new dependency.
- **`le31-conventions`** — the seven-check feature gate and the hard invariants.
- **`le31-v1-feature-pattern`** — the contract shape and the *Definition of Done* (the **actual path** must be exercised, not merely a passing test).
- **`le31-handoff-spec`** — the frozen-contract discipline.

**Nearest siblings — read these so this slice does not open them:**

- **`features/430-…-v1-order-item-insertion-time.md`** — the `order_item` insertion-time contract. **It is the closest sibling in the whole corpus** and it touches the same table. If 430 adds an insertion timestamp to `order_item`, then **430 satisfies this convention for `order_item` and 429 must not add a second one.** Ordering: **429 first** (the convention and the test), **430 second** (the business-meaningful column), or 430's column *is* 429's `created_at` on `order_item` — see the Open question.
- **`features/405-…-v1-service-day-boundary-and-business-date.md`** — owns the **business** date. Do **not** add a `business_date`.
- **`features/421-…-v1-ledger-append-only-mechanism.md`** — the append-only linter rule. `stock_entry`'s append-only status is **its** subject; 429 must not weaken it and must not add `updated_at` to that table.
- **`features/427-…-v1-sqlite-fk-enforcement.md`** and **`features/426-…`** — schema-level work on the same file. They do not own timestamps.

## Open questions

1. **`derived_tip` — is it created in the same transaction as its `bill`?** If yes, `created_at` on `derived_tip` is redundant with `bill.paid_at` and the implementer may prefer to leave `derived_tip` without it and amend the docstring to name the exception. **Default recorded: add it anyway** — one column, and the convention stays true without an exception clause.
2. **`app_user` — is a user row mutable?** `role` and `pin_hash` are mutable in principle, `name` in practice. **Default recorded: give `app_user` both `created_at` and `updated_at`.** If the owner says users are append-only, drop `updated_at` and name the exception in the docstring.
3. **Does the owner want (a) or (b)?** This is an **owner decision, not an implementation detail** — (a) costs nine to seventeen columns and a migration; (b) costs one line. **Both are correct; they are not equivalent in cost, and the owner should choose.**
4. **What should `created_at` be for rows that already exist?** **Default recorded: the migration instant.** No historical insertion times exist and none can be reconstructed. If the owner has an old dev database with meaningful row order, the `id` is a better proxy for *those* rows than a migration timestamp — **record which was used**.

## Why this matters

**⭐ LE31's schema documentation is currently a trap, and it is the first thing an implementer reads.**

The `Conventions:` block in `backend/app/models.py` is not a comment in the margin — it is **the contract's own header**, sitting directly above the code it describes, in the file that defines every table LE31 has. Line 10 says *"All tables have created_at"*. Every table below it does not. An agent asked to *"implement the schema as described"* and pointed at this file will draw a false conclusion, and an agent that trusts a file's docstring more than its code — which is the correct default — will be misled here.

**The fix is cheap and the ambiguity is not.** Nine columns and a `default_factory`, or one line of docstring. Both make the file true. Neither is a large refactor, neither touches a business rule, neither risks a migration, and **the version that ships a regression test** (`test_docstring_convention_matches_schema`) means the contradiction cannot silently return.

**⭐ And the deeper habit this contract encodes is worth naming.** LE31's schema has, from the start, treated **business-event time** and **row-creation time** as different things — `batch.prepared_at` and `batch.expires_at` are two business times; `stock_entry.at` is a write time. The line-10 convention was an attempt to generalise that habit into a rule, and the rule was never carried through. **A stated convention that the code does not follow is worse than no convention at all**, because it converts a fact a reader could have checked into a fact a reader will assume. Making the convention true — or deleting it — is the same kind of honesty LE31 already demands of its data in the ledger: *the record should be exactly what it claims to be, and no more.*

## Adjacent evidence

**Third-party instrument — `Ifazawezk/dukkan`** (MIT ✓ §3.2 STRICTLY-COMPATIBLE, ★1/⑂0 — **no traction evidence in either direction**, 1,719 KB, **Python ✓ ON-STACK** (FastAPI + SQLAlchemy 2 + Pydantic v2), created 2026-11-01 **AND** pushed 2026-11-01 = **IN-WINDOW BY BOTH FIELDS**, `default_branch=main`, `archived=false`, `fork=false`; all fields **parent-verified via direct `GET /repos/`**; README read in full, 14,693 bytes).

Its README, verbatim:

> *"**Exact money.** Amounts are stored as whole dirham (1 QAR = 100 dirhams) and are `Decimal` in Python, so no floating point touches a price."*

> *"Every sale also stores its local business date, so a sale at 1 am Doha time lands on the right day whatever the server's time zone."*

**Le31-side gap this names (proven by EXECUTION):** `tables_with_created_at` = `[]` over all ten tables; `tables_with_NO_timestamp_at_all` = `["app_user", "derived_tip", "menu_item", "table_"]`; `convention_fully_honoured` = `false`. The distinction between **the time a sale happened** (`bill.paid_at`) and **the time the row was written** (`bill.created_at`) is exactly the distinction `created_at` is for, and `bill` currently keeps only the first.

**Recorded, not picked (each verified by a corpus-wide grep, not by memory):**

| Rule from the source | LE31 analogue | Disposition |
|---|---|---|
| *"Every change to stock is a row in a ledger … `record_movement` … in the same transaction"* | the append-only ledger | **Feature 421** (linter rule) + feature 374 (derivation) — **filed** |
| *"On PostgreSQL the stock row is locked with `FOR UPDATE`"* | concurrency on the sale path | **COVERED (7)** — features 171, 242, 269, 392, 394 |
| *"`verify_ledger` recomputes every balance from the ledger and reports any mismatch"* | a ledger self-check | **COVERED (6)** — features 303, 368, 410, 414, 49- |
| *"An order discount is split across lines with the largest remainder method"* | money split rules | **COVERED** — feature 14 (split bills) |
| *"Every sale also stores its local business date"* | the service-day boundary | **Feature 405** — **filed** |
| *"Refunds that add up … a return pays back the line's share of what the customer actually paid"* | returns/refunds | **COVERED (4)** — features 18-, 304, 400, 404 |
| *"Two views of returns (a cash view … a product view)"* | cash vs accrual reporting | **NOT COVERED** — **recorded here, deliberately not picked**; it is a *reporting* concept, and the reporting features (06, 08) are briefs, not contracts |
| *"Cash drawer sessions with end of day counts"* — on dukkan's **unbuilt** roadmap | the shift close | **Feature 426** (today's research cron) — **filed** |

**Boundary — what this feature does NOT own:** the *service day* (405), the *ledger append-only rule* (421), the *`order_item` insertion time* (430), the *`menu_item.category` normalisation* (431), the *ledger derivation* (374), the *tip semantics* (420), the *shift close* (426), the *SQLite FK enforcement* (427).

**Fully reversible.** Under option (a) the columns are additive and default to the insert instant; under option (b) nothing changes but a sentence.
