# Feature 445 — `le31-batch-has-no-preparer`

> **Pick B of Daily Research 2026-11-06 (84th pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Batch` (lines 96–110), verbatim:
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
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite DB, then real inserts):
>
> ```
>   batch of 10 tiramisu created
>   StockEntry(qty_delta=-2, reason='sale',  by_user_id=<the waiter>)  -> ACCEPTED
>   StockEntry(qty_delta=-2, reason='waste', by_user_id=<the cook>)   -> ACCEPTED
>
>   the ledger rows carry their actors:
>     ('sale',  2)     <- the waiter
>     ('waste', 3)     <- the cook
>
>   the batch row carries NONE:
>     columns: id, menu_item_id, qty_start, qty_remaining,
>              prepared_at, expires_at, photo_url, notes
>     can_answer_who_prepared -> false
> ```
>
> **The asymmetry is exact and it is the whole finding:** `StockEntry.by_user_id` exists. `Shift.by_user_id` exists. `Bill.closed_by` exists. `Visit.server_id` exists. **`Batch` has no actor column of any kind.**
>
> **Evidence class: OBSERVED** (every claim below is a reproducible execution against LE31's own schema). **Confidence: high** for the gap; **medium** for the operational pain (see *Evidence* in the gate verdict and *Open questions*).
>
> **Bucket: v1.** **Build verdict: `build`.**

## Goal

Make a prepared batch **attributable to the person who prepared it**, the same way every other movement of stock in LE31 is already attributable to the person who caused it.

One column, one write path, one question answered: **"who made this?"**

## Scope

- Add **one nullable actor column** to `Batch` — the preparer.
- Set it on **the one write path that creates a batch**.
- Make it **readable**: the batch's preparer is returned wherever a batch is returned.
- A **regression test** for each scenario in the table below.

**Nothing else.** This is the smallest feature in the corpus.

## Out of scope (v1)

- **Any recipe, ingredient or BOM model.** No `Recipe` table, no `Ingredient` table, no `qty_per_unit`. Feature **398** explicitly excludes all of it, and this contract does the same.
- **Ingredient-level stock deduction.** Out of scope for the same reason, and out of scope for this feature's size.
- **A change to `Batch.qty_remaining`.** Feature **374** owns the derived-not-stored contradiction.
- **Which batch a sale hit.** Feature **385** owns the order-line→batch provenance.
- **Expiry and shelf-life policy.** `Batch.expires_at` exists and is optional; **this feature does not make it required** and does not decide what an expiry means. Feature 372's vocabulary is adjacent. **Recorded, not picked.**
- **`MenuItem.is_prepared`.** Feature **398** owns it.
- **Any change to `StockEntry`.** Feature **417** owns the `StockEntry` actor FK; this feature changes nothing about the ledger.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### What LE31 already believes

LE31's schema is, on the whole, **good at attribution**. Four of its ten tables carry an actor:

| Table | Actor column | Who it names |
|---|---|---|
| `stock_entry` | `by_user_id` | whoever caused the stock movement |
| `shift` | `by_user_id` | whoever opened the shift |
| `bill` | `closed_by` | whoever closed the bill |
| `visit` | `server_id` | whoever served the table |
| **`batch`** | **— none —** | **nobody** |

**`Batch` is the odd one out, and it is the odd one out in the place where it hurts most.** A batch is *someone's work*: eight tiramisu prepared at 09:00 by a cook. The schema records **the fact of preparation** (`prepared_at`) and **the quantity** (`qty_start`, `qty_remaining`) — and **not the agent**.

### The direction of the asymmetry matters

The obvious reading is *"the ledger is attributed, so we're fine"*. It is the **wrong reading**, because the ledger records what happened **to** the batch, and the batch records what happened **before** it.

Concretely, from the executed probe above: when the cook threw away two tiramisu, **LE31 can name the cook** — the `waste` row has `by_user_id = 3`. But when the question is *"who prepared the batch in the first place?"*, **there is no column to look in**. The schema can answer *"who ruined it"* and cannot answer *"who made it"*.

That is the wrong way round. **A complaint is about what was made**, not about what was thrown away. A food-safety question is about the preparation — the time it was made, the hands that made it, the shift it was made in. All three are asked about **the batch**, and **one of the three (the person) is unanswerable**, while the other two (`prepared_at`, and the shift derivable from `prepared_at`) are recorded.

### Why the plausible wrong answer is the quiet one

> *"The batch has `prepared_at`, so we know when it was made."*

**True** — and it is the answer that hides the gap, because *when* and *who* feel like the same kind of record. They are not. Feature **429** already says this in its own words:

> *"`batch.prepared_at` — records when the batch was **prepared**, which is a business event, not the row's insertion time. A batch row created at 08:00 for a 10:00 prep carries `prepared_at = 10:00`; those are different facts."*

**Feature 429 owns the timestamp convention. It does not own an actor.** The two are adjacent and neither substitutes for the other.

A second quiet answer:

> *"The `notes` field is free text — the cook can write their name in it."*

**This is worse than no answer, not better.** `Batch.notes` is untyped, unindexed and unqueryable; a name written there cannot be joined to `app_user`, cannot be filtered on, and cannot be relied on. **A free-text name is not attribution.** (The same reasoning applies to `photo_url`.)

### The evidence class is important here — and it cuts both ways

**The gap is OBSERVED.** The asymmetry is not an inference; it is a missing column, proved by execution.

**The operational pain is INFERRED.** No owner has said *"I need to know who prepared the tiramisu."* There is no order flow, no kitchen flow, and **no complaint has been recorded**. So the honest reading of the evidence is: **the schema has a hole that the nearest comparable tables do not have, in the one table where the question is most likely to be asked.**

The gate's rule for an assumed pain is *a small experiment, not a full feature*. **This contract IS that small**: one nullable column, one write path, no behaviour change, no new surface, no new dependency, and it is **reversible in one line** (drop the column → zero data loss, because it is nullable and no data depends on it). It is the smallest thing the repository can contain, and it closes a hole **before** the traffic that would expose it.

**The honest counter-argument, stated plainly:** if the owner never asks *"who prepared this?"*, the column is unused. That is a real cost of a small amount of clutter — and it is set against a cost of **permanent unattributability** once batches exist and a question is asked.

## Data model

**One nullable column on `Batch`:**

```python
class Batch(SQLModel, table=True):
    __tablename__ = "batch"

    id: int | None = Field(default=None, primary_key=True)
    menu_item_id: int = Field(foreign_key="menu_item.id")
    qty_start: int
    qty_remaining: int
    prepared_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
    expires_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    photo_url: str | None = None
    notes: str | None = None
    by_user_id: int | None = Field(default=None, foreign_key="app_user.id")   # ← NEW
```

**Design notes:**

- **Named `by_user_id`** — deliberately the **same name as `StockEntry.by_user_id` and `Shift.by_user_id`**, so the three actor columns read identically across the schema. Consistency is what makes the next reader *expect* a `Batch` actor and notice its absence.
- **Nullable** — existing rows (there are none in production, but the dev DB may have some) and any batch created outside a staff context are not blocked. `NULL` means *"the preparer is not recorded"*, **never** *"the preparer is the system"*.
- **Foreign key to `app_user.id`** — so the preparer is always a real staff member. Feature 417's finding applies directly: an actor column without a FK is a **dangling integer** that is accepted, stored, and indistinguishable from a correct value. **LE31's own code already knows how to protect referential integrity** (`StockEntry.batch_id` is caught by the FK — the parent hit exactly that while seeding the probe database) — **this column gets the same protection.**
- **`UserRole.cook` already exists.** The role that prepares a batch is already in the enum. **No new role, no role change.**
- **No new table.** No `BatchPreparer` join table.

**No `StockEntry` row is written when a batch is created.** The ledger records *movements*; a preparation is the batch's own existence. `test_batch_creation_writes_no_ledger_row` enforces it.

**No change to `StockEntry`, `MenuItem`, `OrderItem`, `Bill`, `Visit`, `Shift` or `DerivedTip`.**

## Implementation steps

Dependency-ordered; each task is independently verifiable.

1. **Model change.** Add `by_user_id` to `class Batch` in `backend/app/models.py`, nullable, FK to `app_user.id`. **This step depends on feature 446** for anything beyond `create_all()` — see *Dependencies*.
2. **The one write path.** Wherever a `Batch` is created, set `by_user_id` from the acting staff member. **There is no such write path today** — `backend/app/routers/` contains exactly `__init__.py` and `tables.py`, and there is no kitchen or stock router — so this contract ships **the column, the read path, and the helper the future write path will call**:
   ```python
   # backend/app/services/batches.py
   def create_batch(
       session: Session,
       *,
       menu_item_id: int,
       qty_start: int,
       prepared_by: int | None,
       prepared_at: datetime | None = None,
       expires_at: datetime | None = None,
       notes: str | None = None,
   ) -> Batch:
       """Create a batch and record who prepared it.

       `prepared_by` is the app_user id of the cook. It is nullable so that a
       batch created outside a staff context (a seed, an import) is not blocked —
       but NULL means "not recorded", never "the system".
       """
   ```
3. **The read path.** Include the preparer wherever a batch is returned. If a batch is returned as a response model, add `prepared_by` (the id) and — **only if a join is already in the pattern** — the preparer's display name. **Do not add a join that does not exist.**
4. **Tests.** One test per row of the table below.

### The scenario table (each row is a test)

| Scenario | Expected |
|---|---|
| A batch is created by a cook | `by_user_id` = that cook's id |
| A batch is created with `prepared_by=None` | **accepted**; `by_user_id` is `NULL` — **not** blocked, **not** defaulted to a system user |
| A batch is created with a nonexistent `prepared_by` | **rejected by the FK** — no row |
| A batch is created by a `UserRole.server` | **accepted** — this feature does not restrict roles (see *Open questions*) |
| A batch is created | **no `StockEntry` row is written** |
| A batch is created | `prepared_at` is **unchanged** in behaviour — the column keeps its `default_factory=utcnow` |
| The preparer is read back | the id matches what was written |
| A batch with `by_user_id = NULL` is read back | `NULL`, distinctly — **not** an error, **not** a default |
| **A `StockEntry` is written against the batch** | the `StockEntry`'s own `by_user_id` is **unchanged** — the ledger's actor and the batch's preparer are **different facts** |

## Telegram interaction if any

**None, and this is deliberate.**

The preparer is recorded **at the moment of preparation**, by whoever prepares the batch. LE31's cook surface is the **Telegram bot**. But:

- There is **no kitchen or batch write path today**, so there is **no Telegram command to attach this to**. The feature ships the **record**, and the future write path supplies the actor.
- **The command name is a product decision, not this contract's.** When the cook Telegram bot gains a *"prepared 8 tiramisu"* command, that command sets `by_user_id` to the **authenticated Telegram user** — the same value `StockEntry.by_user_id` uses today. **That is a later feature's job.**

**The read path is a service/API concern**, not a bot concern. The cook bot does not need to be told who prepared a batch; the **owner** needs to be able to look it up.

## Dependencies

- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — HARD dependency.** Adding a column to an existing table is **exactly** the operation `create_all()` cannot perform. Without 446, this column **cannot reach a live database** except by hand — which is the silent-no-op failure 446 exists to prevent. **446 must land first.**
- **Feature 374 (`qty_remaining` derived not stored)** — **adjacent, not a dependency.** 374 changes how `qty_remaining` is computed; this feature adds a column beside it and **must not change 374's derivation**. The two can land in either order once 446 exists; if they land together, `create_all()` handles both (adding a column and leaving `qty_remaining` alone).
- **Feature 417 (`StockEntry` actor FK)** — **adjacent, not a dependency.** 417 adds the FK to the *ledger's* actor and **explicitly lists `Batch` among what it does not change.** This feature adds the FK to the *batch's* actor. **Do not modify 417; do not bundle them.**
- **Feature 398 (`is_prepared` semantics)** — adjacent; explicitly excludes a change to `Batch`. **Do not modify 398.**
- **Feature 429 (timestamp convention)** — adjacent; owns the *timestamp* convention, not an actor. **Do not modify 429.**
- **No new dependency.** No new pip package, no integration, no AI.

## Open questions

1. **One preparer, or several?** A batch may be prepared by more than one person ("Alex and Sam made the tiramisu"). A single column forces a choice between **the preparer** (first one recorded) and **the last preparer** (overwritten — which destroys evidence and violates §4.3's spirit). **The recommendation is a single nullable `by_user_id` recording the preparer of record, with a multi-preparer record as a later, separate decision** — because a join table for a scenario that has not been observed is over-engineering. **This is an owner decision, recorded here, not guessed.**
2. **May a `server` prepare a batch?** LE31's `UserRole` has `server`, `cook`, `manager`. In a small restaurant, **the owner is often the one who prepares** and the owner may not be a `cook` in the enum. **This feature does not restrict the role** — it records whoever the authenticated user is. **Recorded as an owner decision.**
3. **Should the preparer be immutable once set?** The recommendation is **yes** — a preparer is a historical fact, like a `StockEntry` row. Changing it would mean a second preparer, which is *Open question 1*. **Recorded, not decided here.**
4. **Should `Batch.notes` stop being the place for a name?** The recommendation is **yes** — once `by_user_id` exists, a name in `notes` is a duplicate record that can disagree with it. **This is documentation, not code.**
5. **Does the owner actually need this?** This is the honest *evidence* question, and it is the one the gate's rule for an assumed pain turns on. The feature is deliberately tiny and reversible so that the answer does not have to be known in advance — but **if the owner says no, the feature should be closed with the reason recorded, rather than left half-built.**

## Why this matters

**Because LE31's stock ledger answers every question about a batch except the one that starts with "who".**

The batch is the unit of preparation — *"8 pieces of Tiramisu, prepared 09:00 today"*, in LE31's own docstring. It is the thing the kitchen made, the thing the ledger draws down from, and the thing a guest's complaint is about. Every other **movement of stock** in LE31 is attributed to a person: the sale is attributed, the waste is attributed, the shift is attributed, the bill is attributed. **The preparation is not.**

The failure is **silent and permanent** in the same way the stock defects are: there is no error, no constraint, no log line — **there is simply no column to look in**. And unlike the stock ledger, **there is no append-only record to reconstruct it from afterwards**: the batch's `prepared_at` is the only trace, and it is a *time*, not a *person*.

**And it is the cheapest fix in the corpus.** One nullable column with a foreign key, one helper, one read path, no behaviour change, no new surface, **no data at risk** — a batch's existence and quantity are untouched. **Drop the column and the feature is gone with zero residue.** Two to three hours.

The general point is the one LE31's own schema already teaches in four other places: **a record of *what happened* without a record of *who did it* is an audit gap, and this is the one table where it was left open.**

## Adjacent evidence

- **`FreeOpenSourcePOS/FloCafe`** (MIT ✓ §3.2, TypeScript off-stack, ★168/⑂80, pushed 2026-11-05), README verbatim: *"**Granular roles & permissions:** Owner, Manager, Cashier, Server, and **Chef** roles with context-aware access policies."* — **the preparer is a named role in a peer.**
- **`chamithsilva10/Lazy-Sunday`** (TypeScript, `null` licence, created 2026-11-02 and pushed 2026-11-03 — in-window by **both** fields), README verbatim: `| 👨‍🍳 **Kitchen Chef** | \`kitchen\` | \`kitchen123\` | Kitchen Display System (KDS), ticket status bump bar |` — **the preparer is a named account in a peer.**
- **`asimhashmi47/DineSync`** (C#, `null` licence) — *"Paying deducts the ingredients by portion... and a refund puts them back"* and *"Stock is deducted in the same transaction as the payment"* — the transaction-shape vocabulary for the stock write path. **Not picked: it confirms filed work rather than opening a new gap.**
- **`adarsh-yadav1/Dum-Direct`** (Python, `null` licence, in-window by both fields) — *"Only an outlet's manager or an admin may override a promised time."* — the **who-may-override** vocabulary. LE31 is a **one-restaurant** product, so outlet scoping does not transfer; the role-policy shape is adjacent to feature 443 and feature 403. **Recorded, not picked.**

## Adjacent work — recorded, NOT picked

- **`Batch.expires_at` is optional and nothing enforces it.** Executed: a batch with `expires_at = NULL` was accepted. There is no expiry policy in LE31. **Recorded, not picked** — expiry semantics belong with the stock-domain work (feature 372's vocabulary), not with attribution.
- **The batch has no link to the shift it was prepared in.** The shift is derivable from `prepared_at` only by a time heuristic, which is wrong across a midnight service. **Recorded, not picked** — adding `shift_id` would be a second column with its own semantics, and the one-column feature should not grow.
- **The order line has no actor either** (feature 379 owns the status-transition actor). **Recorded, not picked.**
