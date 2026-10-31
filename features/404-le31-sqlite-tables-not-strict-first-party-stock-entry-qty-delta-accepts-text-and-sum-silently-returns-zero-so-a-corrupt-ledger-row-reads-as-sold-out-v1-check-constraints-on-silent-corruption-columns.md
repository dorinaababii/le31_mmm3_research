# Feature 404 — LE31's SQLite tables are not `STRICT`, so the stock ledger's own derivation silently returns the wrong number

> **Pick C of Daily Brainstorm 2026-10-29 (91st pass).** **FIRST-PARTY, and verified by EXECUTION against LE31's own schema.**
>
> `backend/app/db.py` creates the tables with `SQLModel.metadata.create_all(engine)`, and the DDL that actually lands in SQLite is **not `STRICT`**. SQLite's type affinity is **not** a type constraint, and the parent proved the consequence on a throwaway database built from LE31's **own** `models.py`:
>
> ```
> after poisoning UPDATE: qty_delta='not-a-number' typeof=text
> ORM re-read: qty_delta='not-a-number' type=str
> after UPDATE: total_paid=4.675 typeof=real
> ORM SUM(qty_delta) over the poisoned row: 0.0
> ```
>
> **The last line is the finding.** LE31's current stock is defined as `SUM(stock_entry.qty_delta)` (charter §4.3, feature 03). When that column holds a non-numeric value, SQLite **coerces it to 0** — so the derivation returns **0.0**, silently, instead of raising. A poisoned ledger row reads as *"the batch sold out"*, not as *"the batch's quantity is corrupt."*
>
> The money case is sharper. Charter §3.6 states: *"**Money is `Decimal`, never `float`.**"* The column is declared `NUMERIC(10, 2)`; the parent wrote `total_paid = 4.675` — a value with **no exact decimal representation** — and SQLite stored it as a binary **REAL**. The `Decimal` guarantee is a **Python-side** guarantee the storage layer does not enforce.
>
> **External instrument** — `devstroop/ros` (MIT), for a *different* rule from the one used for Pick A: *"**`STRICT` tables only.** A column's declared type means something."* and *"`native check` validates every migration against real SQLite at build time — **a non-STRICT table or a broken foreign key fails the check, not production**."*
>
> **Bucket: v1** — charter §3.6 is a money rule, and money is P1 (end-of-shift reconciliation) and P0 (the bill). **Build verdict: `build`.** Evidence class: **OBSERVED** (executed).

## Goal

Make the **database** enforce the types LE31's schema already claims — so that a corrupt quantity or a float in a money column **fails at write time**, instead of being silently absorbed by the ledger's own derivations.

Concretely:

1. **A `CHECK` constraint on every column whose corruption is silent.** In particular `stock_entry.qty_delta` and the money columns.
2. **One place** where the constraints live, so they are auditable without reading every model.
3. **A stated rule** for what LE31's `Decimal` money guarantee means at the storage layer — and an honest statement of where it currently holds and where it does not.

**The single sentence this feature exists to make true:** *a declared type that the database does not enforce is documentation, not a guarantee.*

## Scope

**In scope (v1):**

- **`CHECK` constraints on the columns where corruption is currently silent** — `stock_entry.qty_delta` first, then the money columns (`bill.total_paid`, `bill.total_due`, `bill.subtotal_items`, `bill.subtotal_tax`, `shift.opening_float`, `shift.counted_cash`, `shift.variance`, `derived_tip.amount`, and the `unit_price` columns).
- **A `CHECK` that forbids a float-shaped money value**: the stored value must equal its own 2-decimal rounding (`total_paid = round(total_paid, 2)`), which rejects `4.675` while accepting `4.67`.
- **A documented statement** of where LE31's `Decimal` guarantee is enforced (Python/ORM) and where it is not (the database), recorded in the feature that owns money (feature 05) and in charter §3.6.
- **A regression test** that asserts a non-integer `qty_delta` and a 3-decimal money value are **rejected** by the database.

**Out of scope (v1):**

- **`STRICT` tables.** `STRICT` is a **SQLite 3.37+** feature; LE31's production target is **Postgres**, where the equivalent is `NUMERIC` precision plus explicit `CHECK` constraints. The transferable item is the **discipline**, and the stack-agnostic implementation is **`CHECK` constraints**, which work on **both** engines. **Turning on `STRICT` is a v2 decision** and is recorded, not taken.
- **Every column.** Constraints go where corruption is **silent**. A `VARCHAR` column that accepts a longer string is a different (and much less dangerous) problem.
- **Changing how money is represented** — integer minor units, as `devstroop/ros` uses. That is a **v2 decision about LE31's `Decimal` money** and it would rewrite every money column. **Explicitly not this feature.**
- **Changing the timestamps to epoch milliseconds** (`ros`'s third rule). Same reason: a representation change, not a constraint.
- **Alembic / migrations.** §3.2's v1 policy is `init_db()`. Follow it and record the prod-migration step as known debt.
- **A `CHECK` on every foreign key.** `ros` also validates foreign keys at build time. LE31's FKs are **declared** — but note that **`StockEntry.ref_order_item_id` has no FK at all**, which is **feature 385's** subject, not this one.
- **Any change to `Batch.qty_remaining`.** That is **feature 374**. **This feature's constraint makes the *column type* true; it does not make the *value* right.** The two are independent and must not be merged.

## Description

### The defect, as observed on 2026-10-29

**Shape (a) — contradiction.** §3.6 says money is `Decimal`, never float. The storage layer accepts and stores a float, **demonstrated**.

**Shape (b) — omission.** Not one declared type is enforced by the database. `grep -rn 'Constraint' backend/` returns **no output** — there is no `CHECK`, no `UniqueConstraint` beyond primary keys, and no `STRICT`.

**Shape (c) — missing inverse edge.** `StockEntry.qty_delta` is **written** by the ORM and **read** by the derivation, and there is **no constraint edge** connecting the two. The database does not know what `qty_delta` must satisfy, so it cannot reject a value that breaks the derivation.

**Shape (d) — undefined term.** "**`Decimal`**" and "**exact**" are used in §3.6 as if the schema guaranteed them. It does not. The guarantee is real **only for writes that go through the ORM's `Decimal` coercion** — and there is exactly one such path today, which is why the defect has never surfaced.

### Why `SUM` returning 0.0 is worse than an exception

An exception is a **good** failure: loud, attributable, and it stops the write. This is not that.

```
qty_delta = 'not-a-number'   (typeof = text)
SUM(qty_delta)  ->  0.0
```

SQLite's aggregate silently coerces the non-numeric value to **0**. So the ledger's own definition of current stock — `SUM(stock_entry.qty_delta) WHERE batch_id = X` (charter §4.3) — reports a batch with a corrupt row as having **less** stock, and a batch whose *only* row is corrupt as having **zero** stock.

**Zero is not a neutral value here.** Zero means **sold out**. So a single corrupt row produces a **plausible, business-meaningful wrong answer**: the cook sees the tiramisu as gone, the menu hides it, the waiter is told it is unavailable — and **nothing anywhere says the number is wrong.** There is no ground truth to audit against, because the ledger's own derivation is the ground truth.

### The money case, and where LE31's `Decimal` guarantee actually holds

`Bill.total_paid` is `Decimal(10, 2)` in Python and `NUMERIC(10, 2)` in SQLite. The parent wrote `total_paid = 4.675`; SQLite stored it as a **binary REAL** — a value with no exact decimal representation. Read back through the ORM it becomes `Decimal('4.675')`, which **looks** exact and **is not** the number that was stored.

**The guarantee is real but narrow.** It holds for writes that pass through the ORM's `Decimal` coercion. It does **not** hold for:

- a `sqlite3` shell session or a maintenance script;
- a future **Alembic** migration that writes data (§3.2 already records Alembic as a known debt);
- any future bulk-import or backfill path;
- a second application instance pointing at the same database file.

**None of these exist today.** That is why this is a **latent** defect, and why the constraint is worth adding **before** those paths exist rather than after.

### The mechanism, from the artifact

`devstroop/ros` states two things, and both are transferable:

> *"**`STRICT` tables only.** A column's declared type means something."*
> *"`native check` validates every migration against real SQLite at build time — **a non-STRICT table or a broken foreign key fails the check, not production**."*

The second sentence is the more important one, and it is a **process** rule rather than a schema rule: **the guarantee is checked before production, not discovered in it.** LE31's equivalent — a schema check that runs as part of `init_db()` or a test — is what this feature delivers.

**The vocabulary transfers; the code-shape is not adopted.** `ros` is Zig on a bespoke Native SDK, its schema is 43 `STRICT` SQLite tables with epoch-millisecond integers, and its build tool is not LE31's. **No `ros` code is adopted.** What is adopted is the *rule* — *a declared type that the database does not enforce is documentation, not a guarantee* — expressed in the stack-agnostic form (`CHECK` constraints), which works on both SQLite and Postgres.

## Data model

**No new table. No new column. No column type changed.**

**Changed — `CHECK` constraints, expressed in the model so they are created with the table:**

```
stock_entry
  qty_delta INTEGER NOT NULL
    CHECK (typeof(qty_delta) = 'integer')

bill
  subtotal_items NUMERIC(10,2) NOT NULL  CHECK (subtotal_items = round(subtotal_items, 2))
  subtotal_tax   NUMERIC(10,2) NOT NULL  CHECK (subtotal_tax   = round(subtotal_tax,   2))
  total_due      NUMERIC(10,2) NOT NULL  CHECK (total_due      = round(total_due,      2))
  total_paid     NUMERIC(10,2) NOT NULL  CHECK (total_paid     = round(total_paid,     2))

derived_tip
  amount NUMERIC(10,2) NOT NULL  CHECK (amount = round(amount, 2))

shift
  opening_float NUMERIC(10,2) NOT NULL  CHECK (opening_float = round(opening_float, 2))
  counted_cash  NUMERIC(10,2) NULL      CHECK (counted_cash  IS NULL OR counted_cash  = round(counted_cash,  2))
  variance      NUMERIC(10,2) NULL      CHECK (variance      IS NULL OR variance      = round(variance,      2))

menu_item / order_item
  unit_price NUMERIC(10,2) NOT NULL     CHECK (unit_price = round(unit_price, 2))
```

**Notes on the constraint forms — these are chosen deliberately:**

- **`typeof(x) = 'integer'`** is SQLite-specific. It is the right check for SQLite (LE31's dev engine) because it tests the **storage class**, not the value. On **Postgres** the equivalent is `CHECK (qty_delta = trunc(qty_delta))` plus the column's own integer type. **The constraint must be written so that it is valid on both engines, or it must be written per-engine** — this is an **open question**, recorded below.
- **`x = round(x, 2)`** is the money check. It rejects `4.675` (because `round(4.675, 2) = 4.68 ≠ 4.675`) and accepts `4.67`. **It works identically on SQLite and Postgres** and is therefore the more portable of the two.
- **The `IS NULL OR` guard** on nullable money columns is required: `NULL = round(NULL, 2)` is NULL, and a `CHECK` passes on NULL — so the guard is belt-and-braces and **makes the intent explicit** rather than relying on SQL's CHECK semantics.

**A `STRICT` alternative, recorded not taken:**

```
-- SQLite 3.37+ only. NOT portable to Postgres.
CREATE TABLE stock_entry (...) STRICT;
```

## Implementation steps

1. **Decide the engine strategy.** Write the constraints **per-engine** (SQLite + Postgres variants) or restrict v1 to the **portable** subset (`x = round(x, 2)` for money; `x = trunc(x)` for integers) and defer the SQLite-only `typeof()` check to a Postgres-specific build. **The portable subset is the recommended v1 scope** — it covers the money case, which is the one §3.6 names.
2. **Add the constraints to the models.** `backend/app/models.py` — each affected `Field(...)` gains a `sa_column=Column(..., CheckConstraint(...))`, or the table gains `__table_args__`. **The constraint must be visible in the model file**, not in a separate SQL script, so that a reader of the model sees what the database enforces.
3. **Add the check to `init_db()`.** `backend/app/db.py`'s `init_db()` should **verify** the constraints exist after `create_all` — a cheap `PRAGMA table_info` / `PRAGMA index_list` inspection — and **raise** if a constraint is missing. This is `ros`'s *"a non-STRICT table fails the check, not production"* rule, expressed in the smallest way LE31 can.
4. **Add the regression test.** Two cases, both asserting the **database** rejects the write:
   - `stock_entry.qty_delta = 'not-a-number'` → the write raises `IntegrityError`;
   - `bill.total_paid = 4.675` → the write raises `IntegrityError`.
   And one positive case: `qty_delta = -1` and `total_paid = 4.67` **both succeed**. A constraint test that does not also prove the valid write still works is a constraint that could be trivially wrong (e.g. a constraint on the wrong column, or a NOT NULL that rejects everything).
5. **Assert the derivation is now safe.** The test should also insert the valid rows and confirm `SUM(qty_delta)` returns the expected total — i.e. that the constraint has not changed the *happy path*.
6. **Record where the `Decimal` guarantee holds.** One paragraph in `features/05-payment-tip-reconciliation.md` and one line in charter §3.6: *money is `Decimal` in the ORM **and** constrained to 2 decimal places in the database; writes that bypass the ORM are rejected by the constraint, provided they go through the database.* **The last clause is the honest part** — a write that bypasses the database entirely is not covered, and the paragraph should say so.
7. **Run the schema check as part of the test suite.** The `init_db()` verification from step 3 becomes a test, so the guarantee is checked **before** production rather than discovered in it.

## Telegram interaction if any

**None.** This feature adds no command, changes no command, and changes nothing the cook or the owner sees.

**What changes observably**: a write that would have been silently absorbed is now **rejected**. In practice, today, **nothing** changes — because the only write path is the ORM, and the ORM's `Decimal` coercion already produces valid values. The change is **latent-defence**, not visible behaviour.

**One thing to state plainly, because it could surprise**: rejecting a write is a **new failure mode**. If a future write path constructs a `Decimal` with more than two decimal places (a computed `Decimal('4.675')` from a division, say), the write will now **fail** where it previously succeeded and stored a float. **That is the intended behaviour** — but it must be a **deliberate** change, and step 6's paragraph should say that the constraint is a **rejection**, not a rounding.

## Dependencies

- **No new package.** `sqlalchemy` exposes `CheckConstraint` already; `sqlmodel` passes through `sa_column`.
- **Must not be merged with feature 374** (`Batch.qty_remaining`). This feature's constraint makes the **column type** true; 374 is about the **value** (derive, don't store). **A reviewer must be able to check each on its own.**
- **Related, not blocking:** feature 382 (`StockEntry` idempotency and shortfall — it constrains `qty_delta` at the *application* level with `min(OnHand, qty)`; a `CHECK` here is a *storage* level backstop and **does not** decide that open owner question), feature 391 (`Payment` table and shift-money edge — **the money columns this feature constrains will be re-specified by 391**; the constraints should be added to 391's `Payment` table when it lands, and 391's shape is the reference), feature 385 (`StockEntry.ref_order_item_id` has no FK — a different kind of unconstrained column).
- **No dependency on the Linear write endpoint** (blocked on this workspace — see the HANDOFF's sign-off gap).

## Open questions

1. **One constraint language for two engines, or two?** SQLite's `typeof()` and Postgres's `trunc()` differ. The **portable** subset (`x = round(x, 2)`, `x = trunc(x)`) covers both cases in one expression and is the recommended v1 scope. **Owner/engine-owner to confirm** whether LE31 wants the SQLite-only stronger check behind a dialect switch.
2. **Does the constraint reject or round?** A `CHECK` **rejects**. A future computed `Decimal` with more than two places will now fail where it used to be stored as a float. Is a **reject** the right policy, or should the write path round first and the constraint only guard the storage layer? **The two are different contracts** — the contract must say which.
3. **Should `qty_delta` be constrained to be non-negative?** No — feature 382's open question is exactly whether an oversell records a negative quantity or a separate shortfall, and LE31 has **not** decided. A `CHECK (qty_delta >= 0)` would **pre-empt that owner decision**. **Explicitly not added.**
4. **Which columns are worth constraining at all?** The feature proposes a list. Is `photo_url` / `notes` worth a length constraint? **Out of scope by the "silent corruption" rule**, but the *boundary* is the owner's to draw.
5. **`STRICT` tables — when?** If LE31 ever wants them, the enabler is **SQLite 3.37+** in the dev environment and an equivalent discipline on Postgres. **Recorded, not scheduled.**
6. **Does the constraint need to survive a `ALTER`?** §3.2's `init_db()` policy means schema changes are create-only, so a constraint added later means a **table rebuild** on Postgres. **Known debt**, recorded here so it is not a surprise at migration time.

## Why this matters

**Because LE31's money rule is currently a Python convention rather than a database guarantee, and money is the domain where a wrong number is a real loss.** The charter is explicit — *"Money is `Decimal`, never `float`"* — and the enforcement is explicit too: `Decimal(10, 2)` on every money field. It is very easy to read that as a guarantee. **It is not.** The guarantee holds for writes that pass through the ORM, and the parent's own probe wrote a float into a money column **through the database** and it was stored.

**And the stock case is the one that should worry an owner.** `SUM(qty_delta)` returning **0.0** for a corrupt row does not crash and does not look wrong — it looks like **sold out**. LE31's P0 criterion is *"order a tiramisu → stock goes 8 → 7"*, and the derivation that produces that number is the same one that would silently return a wrong one. **The ledger is the source of truth; a source of truth that can return a plausible wrong answer without complaining is not a source of truth.**

**The asymmetry, stated as the argument for `build` over `defer`:** today there is **exactly one** write path and it is correct. The constraint therefore costs **nothing** today and protects **everything** tomorrow — it is added while the paths that need it do not yet exist, which is the cheapest possible moment. The reverse order is the expensive one: a bulk import, a backfill, a migration, a second instance — **any** of which bypasses the ORM — and then the first float is stored and no one is looking, because the code that reads it is correct.

**And this is the third instance of one new shape, in the same pass.** Pick A found a **written rule** whose mechanism **cannot carry it** (a flat `list[int]` against "role-based"). Pick B found a **written rule** that **fails on NULL** (a nullable column against `> now()`). Pick C found a **written rule** the **database does not enforce** (a `Decimal` guarantee against a non-`STRICT` table). **The unifying shape is: a written rule and an unenforced mechanism.** That is a better question to carry into the next pass than any single field — and the honest limit of the claim is that **three instances in one pass is a reason to check for more, not a reason to believe there are only three.**

**Finally, the method, one more time, because it is the transferable finding of the whole series.** Six consecutive passes, six first-party defects, **all six found in the code corpus and none in the paper families.** Today's external input was three GitHub READMEs; the finding was four greps, a `sqlite3` probe against LE31's own models, and **twenty minutes**. Ninety citations had not found the first one. **A `grep` and a `sqlite3` did.**
