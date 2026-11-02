# Feature 426 — `StockEntry.ref_order_item_id` has no foreign key: the ledger accepts a reference to an order line that does not exist

> **Pick A of Daily Brainstorm 2026-11-02 (95th pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proven by EXECUTION, not by reading.**
>
> `backend/app/models.py`, `class StockEntry` (line 113):
>
> ```
> 121:    batch_id: int = Field(foreign_key="batch.id", index=True)   ← FK ✓
> 124:    ref_order_item_id: int | None = None                      ← NO FK
> 125:    by_user_id: int | None = None                             ← NO FK  (feature 417 owns this one)
> ```
>
> **The parent proved the consequence against a real SQLite database built from LE31's own `models.py`** (`_exec_proof_2026_11_02.py`, run with the existing verification venv `/opt/data/le31-verify-2026-10-27/.venv`):
>
> ```
> --- PROOF 1: StockEntry.ref_order_item_id has NO foreign key ---
> PASS PROOF 1a  StockEntry with ref_order_item_id=999999 is ACCEPTED  dangling reference STORED (row id=1)
> PASS PROOF 1b  and the referenced OrderItem DOES NOT EXIST           order_item 999999 -> ABSENT (dangling)
>        ledger rows for batch 1: 1 (derivation unaffected — corruption absorbed)
> ```
>
> **And the corruption is ABSORBED, not raised.** LE31's own ledger derivation —
> `SUM(qty_delta) WHERE batch_id = X` — returned normally, because a dangling
> *reference* is not a malformed *value*. The row is well-formed; it is simply
> **pointing at nothing**.
>
> Bucket: **v1 (ledger referential integrity — the fourth first-party defect of the brainstorm series)** — Pick A of Daily Brainstorm 2026-11-02. Build verdict: **`build`** (first-party fix: one nullable foreign key column + one deferral-chain correction + one regression test).

## Goal

Make LE31's append-only stock ledger **refuse a reference to an order line that does not exist** — the same thing it already does for the batch it consumed.

**The single sentence this feature exists to make true:** *the ledger's back-pointer to the order line is exactly as trustworthy as its forward-pointer to the batch.*

Two concrete outcomes:

1. **`StockEntry.ref_order_item_id` carries a foreign key to `order_item.id`.** A write naming a nonexistent order line is rejected by the database, not stored.
2. **The deferral chain that currently has a hole is repaired.** Feature 404 states, verbatim: *"note that `StockEntry.ref_order_item_id` has no FK at all, which is **feature 385's** subject, not this one."* But feature 385's Goal is *"one nullable foreign key on `OrderItem`"* — the **forward** pointer — and it never adds a foreign key to `ref_order_item_id`. So the chain is **404 → 385 → (nothing)**, and the back-pointer is owned by no feature at all. This feature closes the chain.

## Scope

**In scope (v1):**
- Change `StockEntry.ref_order_item_id` from `int | None = None` to `int | None = Field(default=None, foreign_key="order_item.id")`.
- Keep the column **nullable**: `NULL` means *"this ledger row is not caused by an order line"* — which is exactly right for `reason='initial'` (morning prep), `reason='restock'` and `reason='waste'`. Only the `sale` reason should ever name an order line. **This feature makes the column honest; it does not make it mandatory.**
- One regression test: a `StockEntry` with `ref_order_item_id` naming a nonexistent order item is **rejected**; a `StockEntry` with `ref_order_item_id=NULL` and `reason='initial'` is **accepted**.
- A **deferral-chain correction** recorded in feature 404's own text (a one-line amendment) so the next pass does not re-derive this and re-file it.
- One row in `INDEX.md`'s "Active feature pipeline" table.

## Out of scope

- **Any change to `StockEntry.by_user_id`.** That is **feature 417** (`le31-stockentry-actor-foreign-key`), which adds the FK to the actor field. **This feature does not touch it and must not be bundled with it** — two different columns, two different defects, two different failure modes.
- **Adding `OrderItem.batch_id`.** That is **feature 385** (batch provenance — the *forward* pointer). This feature adds the *backward* pointer's constraint. **The two are complementary: 385 makes the order name the batch; 426 makes the ledger's back-reference provably valid.** Neither implies the other.
- **Any `StockEntry` write path, selling endpoint, inventory router, `/sold_out` command, or Telegram alert.** None of those exist yet (`backend/app/routers/` holds only `__init__.py` and `tables.py`; `backend/app/services/` does not exist). The parent verified by execution that `StockEntry(` is constructed **zero** times outside its own class declaration — so the defect is **latent, not yet corrupting data**. This feature changes the **schema shape**, not runtime behaviour of a selling flow that does not yet exist.
- **Enabling `PRAGMA foreign_keys` on SQLite.** That is **feature 427** (`le31-sqlite-never-enables-pragma-foreign-keys`). **⚠️ ORDERING: feature 427 must land FIRST, or in the same PR.** As long as the pragma is off, the foreign key this feature adds is **declared but unenforced** — exactly the state the schema is in today for its other eight foreign keys. Adding a tenth unenforced foreign key is not a fix. (See *Dependencies*.)
- **Any change to `OrderItem`, `Visit`, `Bill`, `DerivedTip`, `Shift`, `Batch` or `MenuItem`.**
- **Any retro-fitting of historical rows.** There are none — no `StockEntry` write path exists yet.
- **A migration.** §3.2's stated v1 policy is `init_db()`.
- **The `qty_remaining` derivation.** Feature 374.
- **The `sold_out` inverse operation.** Feature 419.

## Description

### The defect, as observed by execution on 2026-11-02

Parent-verified against a real SQLite database built from LE31's own `models.py`
(`SQLModel.metadata.create_all(engine)` against a throwaway file). Re-runnable:
`_exec_proof_2026_11_02.py`.

| Probe | Result |
|---|---|
| `StockEntry(ref_order_item_id=999999, reason='sale')` — order item 999999 does not exist | **ACCEPTED and STORED** (row id 1) |
| The referenced `OrderItem` | **ABSENT** — the row is a dangling reference |
| LE31's own derivation `SUM(qty_delta) WHERE batch_id = X` | **returns normally** — the corruption is absorbed |
| Contrast: `StockEntry(by_user_id=888888)` — nonexistent user | also accepted today (feature 417 owns that one) |
| Contrast: `StockEntry(batch_id=777777)` with `PRAGMA foreign_keys=ON` | **REJECTED** — `IntegrityError` — proving the mechanism works when it is switched on |

### Why this is not cosmetic

The charter's P0 acceptance criterion is:

> *"Manual test: order a tiramisu → stock goes 8 → 7 → ledger has one entry."* — `PROJECT_CHARTER.md` §2, P0 row.

and the ledger's whole design rests on §4.3:

> ```
> EVERY change to batch stock is a new StockEntry row. Never UPDATE or DELETE.
> batch.qty_remaining = SUM(stock_entry.qty_delta WHERE batch_id = X)
> ```

The ledger is the one table that **can never be corrected**. It has no `UPDATE`
path, no `DELETE` path, and no `void` concept. That makes its *write-time*
validation the **only** validation it will ever get.

A dangling `ref_order_item_id` is the specific corruption this design cannot
later detect:

- The ledger's derivation (`SUM(qty_delta)`) is **unaffected** — a wrong
  *reference* is not a wrong *value*. So the stock number stays plausible.
- There is no reconciliation pass that could find it. The ledger is not
  cross-checked against `order_item` anywhere, because there is no such code.
- Once written, the row is **permanent**. The only repair is a manual row
  deletion — which the charter's append-only rule forbids.

So the failure mode is the exact one the skill's audit instrument calls a
**corruption sink**: the system's own derivations return a *plausible business
number* rather than an error, and there is no ground truth to audit against.

### Why this is not feature 417, and not feature 385

The three features touch three **different** edges of the same triangle, and
the corpus's own deferral notes have blurred them:

| Feature | Edge | Direction |
|---|---|---|
| **417** | `StockEntry.by_user_id` → `app_user.id` | ledger → **actor** |
| **385** | `OrderItem.batch_id` → `batch.id` | order → **batch** (new forward pointer) |
| **426** (this) | `StockEntry.ref_order_item_id` → `order_item.id` | ledger → **order line** |

Feature 417's title says `by_user_id` is *"the only **actor** field without a
foreign key"* — which is **literally true**: `ref_order_item_id` is a
**reference** field, not an actor field. Feature 417's own DDL block proves the
distinction — it shows `ref_order_item_id INTEGER,` with **no** `FOREIGN KEY`
line, and `FOREIGN KEY(by_user_id) REFERENCES app_user (id)   -- ← the whole change`.

Feature 404's note defers `ref_order_item_id` to feature 385, but feature 385's
Goal is *"one nullable foreign key on `OrderItem`"* — it adds the forward
pointer and **never** constrains the back-pointer. **The deferral chain has a
hole, and that hole is this feature.**

### The external instrument: an in-window third-party vocabulary

`Raktim94/nodedr-restaurant-pos` (AGPL-3.0 → §3.2 strictly-incompatible →
**vocabulary only**; NestJS/Prisma/PostgreSQL **off-stack**; ★279, created
2026-08-03, pushed 2026-11-02 = in-window by push only; 28,111 B README read in
full). Its README records, verbatim:

> *"**Postgres/Prisma**"* and *"Full rationale for every choice — including why NestJS over the plain-Express pattern its sister project uses, and **why Postgres over the originally-specced SQLite** — is in [`ARCHITECTURE.md`](./ARCHITECTURE.md)."*

and its roadmap explicitly lists, verbatim:

> *"**What is not built yet?** Native payment-gateway checkout, direct accounting-software and delivery-platform connectors, weighing-scale and label printers, **a SQLite edition** and native installers. The [roadmap](./ROADMAP.md) is explicit about what is done and what is not."*

**The transferable item is the discipline of writing down which dialect the
schema is written against, and accepting that the other dialect behaves
differently.** LE31's charter says *"SQLite for dev, Postgres for prod. Same
SQLModel code for both."* — but the two dialects differ in exactly the
mechanism this feature relies on (feature 427). No code is adopted from an
AGPL-3.0, off-stack project; the **shape** is the transfer.

## Data model

One column changes. Its type, nullability and index are unchanged.

```python
# backend/app/models.py — class StockEntry (line 113)

class StockEntry(SQLModel, table=True):
    """Append-only ledger. Never UPDATE or DELETE rows.

    Current stock for a batch = SUM(qty_delta) WHERE batch_id = X.
    """
    __tablename__ = "stock_entry"

    id: int | None = Field(default=None, primary_key=True)
    batch_id: int = Field(foreign_key="batch.id", index=True)
    qty_delta: int              # positive = added, negative = consumed
    reason: StockReason
    ref_order_item_id: int | None = Field(default=None, foreign_key="order_item.id")  # ← CHANGED
    by_user_id: int | None = None   # ← feature 417 owns this column; unchanged here
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

### The constraint, as it should read in the DDL

```sql
CREATE TABLE stock_entry (
    id INTEGER NOT NULL,
    batch_id INTEGER NOT NULL,
    qty_delta INTEGER NOT NULL,
    reason VARCHAR(8) NOT NULL,
    ref_order_item_id INTEGER,
    by_user_id INTEGER,
    at DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY(batch_id) REFERENCES batch (id),
    FOREIGN KEY(ref_order_item_id) REFERENCES order_item (id)   -- ← ADDED
);
```

**⏱️ Note the ordering constraint.** This DDL only *bites* once feature 427 has
enabled `PRAGMA foreign_keys` on the SQLite connection. Until then the
constraint is declared and unenforced — the same state as LE31's eight other
foreign keys. **Feature 427 lands first, or in the same PR.**

### Why the column stays nullable

| `reason` | `ref_order_item_id` | Why |
|---|---|---|
| `initial` (morning prep) | `NULL` | prep is not caused by an order line |
| `restock` | `NULL` | restock is not caused by an order line |
| `waste` | `NULL` | waste is not caused by an order line |
| `sold_out` | `NULL` | withdrawn stock, not a sale |
| `sale` | **the order line id** | **the only reason that has one** |

**Making it NOT NULL would be wrong** — it would force prep and waste rows to
carry a fake order id. The nullable form is the honest one; the foreign key is
what makes the non-null case trustworthy.

## Implementation steps

1. **Change the column.** In `backend/app/models.py`, `class StockEntry`:
   `ref_order_item_id: int | None = None` →
   `ref_order_item_id: int | None = Field(default=None, foreign_key="order_item.id")`.
   **One line.**
2. **Confirm the DDL.** With feature 427 landed (pragma on), run
   `sqlite3 backend/restaurant.db ".schema stock_entry"` and confirm
   `FOREIGN KEY(ref_order_item_id) REFERENCES order_item (id)` is present.
3. **Add the regression test** (the naming convention follows the repo's
   existing `backend/tests/` layout if present, else create it):
   - `test_stockentry_rejects_dangling_order_ref` — insert a `StockEntry` with
     `ref_order_item_id=999999` (no such order item); assert the write is
     **rejected** (`IntegrityError`), and that no row was created.
   - `test_stockentry_accepts_null_order_ref_for_prep` — insert a `StockEntry`
     with `reason='initial'` and `ref_order_item_id=None`; assert it is
     **accepted**.
   - `test_stockentry_accepts_valid_order_ref` — insert a `StockEntry` with
     `reason='sale'` and `ref_order_item_id=<a real order item id>`; assert it
     is **accepted**.
4. **Amend feature 404's deferral note.** Feature 404 currently says
   `ref_order_item_id` "is feature 385's subject". That is not correct, and the
   next pass would otherwise re-derive this and file a duplicate. Amend the
   sentence in `features/404-...md` to point at **this** feature (426), and
   leave 404's own scope untouched. **A one-line amendment, not a rewrite.**
5. **Record the sibling relationships in the contract's own text** (done above)
   so that feature 427's ordering requirement is visible from both ends.
6. **Add one row** to `INDEX.md`'s "Active feature pipeline" table.
7. **Run the LE31 test suite** and confirm no regressions.

## Telegram interaction if any

**None.** This is a schema-shape change with no runtime behaviour. The
Telegram surface (cook bot) is unaffected: no command, no FSM state, no
message changes.

The single operator-visible consequence is **negative**: a ledger write naming
a nonexistent order line will now **fail loudly at the database** instead of
being stored and silently believed. Since no `StockEntry` write path exists
yet (verified by execution: zero construction sites), **there is no operator
flow to update today** — the change is safe to land before the selling flow
does.

## Dependencies

- **⭐ Feature 427 (`le31-sqlite-never-enables-pragma-foreign-keys`) — MUST LAND FIRST, OR IN THE SAME PR.** Without `PRAGMA foreign_keys = ON`, the foreign key added here is **declared and unenforced**, so the defect is not actually fixed — it is merely *documented* in the schema. This ordering is the same class of rule as the 95th pass's "upstream-of-filed-work" rule: **a filed feature that would implement the defect faithfully must be named and ordered explicitly.** Name it in the PR description.
- **Feature 417 (`le31-stockentry-actor-foreign-key`)** — the sibling column. **Must NOT be bundled**: different column, different defect, different failure mode. If both land in the same PR, they must be **separate commits** with separate tests.
- **Feature 385 (`le31-order-item-batch-provenance`)** — adds `OrderItem.batch_id`. Complementary, not blocking. 385's regression test ("the batch named on the order line is the batch the ledger entry hit") **becomes meaningful only once this feature lands** — before that, the ledger's back-pointer is unconstrained and the test could be satisfied by a dangling row.
- **Feature 421 (`le31-stockentry-append-only-linter-rule`)** — the charter's own §7 linter rule. Not blocking, but **adjacent**: once this feature adds a foreign key to the ledger, the linter rule (421) gains a second thing to check. **Do not implement 421's rule inside this feature.**
- **Feature 404 (`le31-sqlite-tables-not-strict`)** — adds `CHECK` constraints and `STRICT` tables. Not blocking; **do not bundle**. Its deferral note about `ref_order_item_id` must be amended (step 4), but its own scope is untouched.
- **Feature 421's charter basis — `PROJECT_CHARTER.md` §7.** The charter's quality bar already names a linter rule for `StockEntry` writes; this feature adds a *database* constraint, which is a different mechanism from the linter rule 421 owns. **Both are wanted; they are not the same mechanism.**

## Open questions

1. **Should `ref_order_item_id` become NOT NULL for `reason='sale'` rows specifically?** A `CHECK` constraint of the form
   `CHECK (reason <> 'sale' OR ref_order_item_id IS NOT NULL)` would enforce the
   pairing the table above describes. **Recorded default: defer.** It is a
   separate mechanism from the foreign key, it needs the `CHECK`-constraint
   work feature 404 owns, and the foreign key alone already removes the
   dangerous case (a *dangling* reference). **Not decided here.**
2. **What should happen to a sale whose order line was legitimately deleted?** The charter's append-only rule applies to the *ledger*, not to `OrderItem`, and §3.2 has no "void an order line" concept. **Recorded default: `OrderItem` rows are not deleted in v1**, so the question is theoretical today. If voiding is ever added, it needs `ON DELETE` semantics on this foreign key — which is **not** decided here. (Note: `ON DELETE` appears in **2** feature contracts in the corpus; this is not one of them.)
3. **Should the foreign key be indexed?** `batch_id` carries `index=True`; `ref_order_item_id` currently does not. A nullable FK on a lookup path (find the ledger rows for an order line) may want one. **Recorded default: no index** — the lookup direction that matters (`batch_id` → ledger rows) is already indexed, and there is no read path yet to justify the second index.

## Sources

- **LE31's own code** — `backend/app/models.py`, `class StockEntry` (line 113), read on 2026-11-02.
- **LE31's own code** — `backend/app/db.py` (the `create_engine` call), read on 2026-11-02.
- **LE31's charter** — `PROJECT_CHARTER.md` §2 (P0 acceptance criterion), §4.3 (the append-only ledger pattern), §7 (the quality bar).
- **Execution proof** — `_exec_proof_2026_11_02.py`, run 2026-11-02 against a throwaway SQLite database built from LE31's own `models.py` with `SQLModel.metadata.create_all`. Probe 1a/1b (the dangling reference is accepted and stored; the referenced order item is absent; the ledger's derivation is unaffected), Probe 2 (the `by_user_id` contrast), Probe 3/3b (the pragma is off by default; with it on the constraint bites), Probe 6 (zero `StockEntry(` construction sites today).
- **Third-party instrument (vocabulary only)** — `Raktim94/nodedr-restaurant-pos`, GitHub API `/repos/` GET on 2026-11-02, HTTP 200: ★279, AGPL-3.0, NestJS/TypeScript **off-stack**, created 2026-08-03, pushed 2026-11-02 = **in-window by push only** (created 3 months before the 2026-10-03 window start — **not a fresh discovery**), 28,111 B README read in full. **AGPL-3.0 → §3.2 strictly-incompatible → no code is adopted; the shape is the transfer.**
- **Corpus evidence** — features 385, 404, 417 read in full on 2026-11-02; `grep -l "ref_order_item_id" features/*.md` → **14 files**, none of which adds a foreign key to that column.

## Why this matters

**Because it is the last unconstrained edge in the one table LE31 can never correct.**

Every other first-party defect in this series has been about a rule that *could* be stated. This one is about a rule that **is not stated at all**, on a table the charter describes as the product's killer feature:

> *"**The killer feature** — and the reason we are building this rather than forking an existing POS — is **first-class finite stock of prepared/cooked items**."* — `PROJECT_CHARTER.md` §1

A ledger that can point at nothing, in a table with no `UPDATE` and no `DELETE`
path, in a system whose P0 acceptance criterion is *"the ledger has one entry"*
— that is the shape of a defect that surfaces to the owner as a stock number
that is wrong by one tiramisu, with **no ground truth to audit against**.

And the fix is **one line**. The asymmetry is stark: the P0 criterion is
testable in a manual test, the fix is a single `Field(...)` argument, and the
regression test is three assertions. **Cheap now, before the first ledger write.
Expensive after — because by then the row is permanent, the ledger is
append-only, and the only repair is a manual deletion the charter forbids.**

**Finally, this feature closes a hole in a deferral chain, and that hole is
itself the finding.** Feature 404 deferred `ref_order_item_id` to feature 385;
feature 385 does not do it; nobody did it. **The corpus's own cross-references
were load-bearing and one link was missing.** That is exactly what a
corpus-wide grep cannot detect and a row-by-row audit can — and it is the
reason this pass audited the charter's P0/P1 rows individually rather than
trusting the (zero-hit) concept sweep.

## Adjacent evidence

| # | Item | Relationship |
|---|---|---|
| 1 | **Feature 417** — `StockEntry.by_user_id` FK | **Sibling column.** `by_user_id` is an *actor* field; `ref_order_item_id` is a *reference* field. 417's title is literally true and does not cover this. **Do not bundle.** |
| 2 | **Feature 385** — `OrderItem.batch_id` | **Sibling edge.** Adds the forward pointer; never constrains the back-pointer. 385's regression test becomes meaningful only once this lands. |
| 3 | **Feature 404** — SQLite not `STRICT` | **Deferred this to 385, wrongly.** Its note must be amended here (step 4). Its own scope — `CHECK` constraints and `STRICT` tables — is untouched. |
| 4 | **Feature 427** — `PRAGMA foreign_keys` | **⭐ Must land first, or in the same PR.** Without it, this foreign key is declared and unenforced. |
| 5 | **Feature 421** — the charter's §7 linter rule | **Adjacent mechanism.** A linter rule and a database constraint are different instruments; 421 owns the linter. |
| 6 | **Feature 374** — `qty_remaining` derived | **Adjacent.** The ledger's derivation. Untouched here. |
| 7 | **Feature 419** — `/sold_out` inverse operation | **Adjacent.** Also writes ledger rows; also has a `NULL` back-pointer legitimately. |
| 8 | **Feature 385, 404, 417, 421** — all four mention `ref_order_item_id` | **Recorded-not-picked.** The corpus knows the column exists; it does not know it is unconstrained. |
