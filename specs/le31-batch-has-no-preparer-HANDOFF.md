# HANDOFF — le31-batch-has-no-preparer

> **Slice contract for the coding agent.** Produced by the 84th LE31 daily-research pass (2026-11-06), Pick B.
>
> **Feature file**: `features/445-le31-batch-has-no-preparer.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite DB, then a `Batch` of 10 tiramisu with `StockEntry(qty_delta=-2, reason='sale', by_user_id=<the waiter>)` and `StockEntry(qty_delta=-2, reason='waste', by_user_id=<the cook>)` — **both ACCEPTED**. The ledger rows carry their actors (`('sale', 2)`, `('waste', 3)`); the **batch row carries none**: its columns are exactly `id, menu_item_id, qty_start, qty_remaining, prepared_at, expires_at, photo_url, notes`). `StockEntry.by_user_id`, `Shift.by_user_id`, `Bill.closed_by` and `Visit.server_id` all exist; **`Batch` has no actor column of any kind.**). All seven checks pass; check 1's **demand** is classed INFERRED, which is why this contract is deliberately **one nullable column** and reversible in one line. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-daily-research-2026-11-06.md`.
>
> **Report**: `/opt/data/le31-daily-research-2026-11-06.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/445-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/446-le31-has-no-schema-evolution-mechanism` FIRST** and confirm the ordering described under *Frozen contract* below. **This slice adds a COLUMN to an existing table — which is exactly the operation `create_all()` cannot perform. 446 is a HARD dependency.**
6. **Add `by_user_id` to `class Batch`** in `backend/app/models.py` — **nullable**, FK to `app_user.id`, **named identically to `StockEntry.by_user_id` and `Shift.by_user_id`**.
7. **Create `backend/app/services/batches.py`** with `create_batch(session, *, menu_item_id, qty_start, prepared_by, prepared_at=None, expires_at=None, notes=None) -> Batch` — the write path the future kitchen flow will call.
8. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_batch_records_who_prepared_it` — it is what proves the column is not decorative.
9. **Record the deferral-chain corrections** — one line each in `features/417-…`, `features/398-…` and `features/429-…`, saying *"the batch's preparer is feature 445."*

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Add a `Recipe`, `Ingredient`, `RecipeItem` or BOM model.** Explicitly out of scope, and **feature 398** explicitly excludes all of it.
- **Implement ingredient-level stock deduction**, or change `StockEntry`'s shape to accommodate it.
- **Change `Batch.qty_remaining`.** Feature **374** owns the derived-not-stored contradiction. **This slice adds a column *beside* it and must not touch it.**
- **Add `OrderItem.batch_id`, or decide which batch a sale hit.** Feature **385** owns the order-line→batch provenance.
- **Make `Batch.expires_at` required, or define what an expiry means.** `expires_at` stays optional. **Recorded in the feature file's *Adjacent work — recorded, NOT picked*.**
- **Change `MenuItem.is_prepared`, or add a column to `MenuItem`.** Feature **398** owns it.
- **Change `StockEntry` in any way.** Feature **417** owns the `StockEntry` actor FK and **explicitly lists `Batch` among what it does not change**. **Do not bundle them and do not modify 417.**
- **Add a `BatchPreparer` join table, or a `shift_id` on `Batch`.** One preparer of record is the recorded position; a multi-preparer model and a shift link are **owner decisions recorded as open questions, not implemented here**.
- **Restrict which roles may prepare a batch.** The slice **records** whoever the acting user is; role policy is **feature 403**.
- **Add a Telegram command.** The feature ships the **record**; the command is a later feature's job (see *Telegram interaction* in the feature file).
- **Introduce Alembic, write a migration, or change `PROJECT_CHARTER.md`.** The charter is the owner's document. **Feature 446 owns the schema-evolution mechanism.**
- **Add a new pip dependency.**

**Disambiguation**: this slice is about **who prepared a batch**. It is **not** about the batch's provenance in a sale (385), the batch's remaining quantity (374), the batch's expiry (372's vocabulary), the item's `is_prepared` flag (398), the ledger's actor FK (417), the order line's allergens (439), the order line's status transitions (379), or the role policy (403).

## Frozen contract

**The one thing this contract exists to make true:** *a batch records who prepared it — the same way every other movement of stock in LE31 records who caused it.*

Concretely, after this slice lands:

1. `Batch` has **exactly one** new column: `by_user_id`, **nullable**, FK to `app_user.id`.
2. The column is **named `by_user_id`**, identically to `StockEntry.by_user_id` and `Shift.by_user_id`.
3. `create_batch(...)` sets it from the acting staff member.
4. `NULL` means **"the preparer is not recorded"** — **never** "the system", and **never** a default.
5. A batch created with a **nonexistent** preparer is **refused** by the foreign key — **not** stored as a dangling integer.
6. A batch created with `prepared_by=None` is **accepted** (not blocked) — seeds and imports must not break.
7. Creating a batch writes **no `StockEntry` row** — the ledger records *movements*, not existence.
8. `prepared_at` keeps its existing behaviour (`default_factory=utcnow`); **this slice does not change it**.
9. The `StockEntry`'s own `by_user_id` is **unchanged** by a batch — the ledger's actor and the batch's preparer are **different facts** and must not be conflated.
10. The preparer is **readable** wherever a batch is returned.

**The prohibition:** *a preparer recorded in `Batch.notes` as free text.* A free-text name is not attribution — it cannot be joined to `app_user`, cannot be filtered on, and can disagree with the real record. If a name is already in `notes`, the feature file's *Open questions* 4 says to document that the typed field is the one that counts.

### The 446 ordering — resolve before writing code

| If | Then |
|---|---|
| **446 has not landed** (today's state) | **445 MUST NOT be deployed to a live database.** A **new column** on an **existing table** is precisely what `create_all()` cannot do — it would be **silently ignored**, and the feature would appear to work in tests and not work in production. **445 may be written and committed, but the commit message MUST state that it cannot be applied to a live database until 446 lands.** |
| **446 has landed** | 445 lands normally. `create_all()` on a differing schema now takes a timestamped backup first and **aborts if the backup fails**. |

**Either way, 445 must not introduce its own migration mechanism, and must not hand-write an `ALTER TABLE`.** That is 446's job.

### The single-preparer question — an owner decision, recorded not guessed

The feature file's *Open questions* 1 asks whether a batch may have **several** preparers. **The recorded position is a single nullable `by_user_id` recording the preparer of record**, because:

- A join table for a scenario that has **not been observed** is over-engineering.
- The alternative — overwriting `by_user_id` with the latest preparer — **destroys evidence** and violates the spirit of charter §4.3.

**The agent may implement the single-column form. The agent may NOT implement a join table, and may NOT implement overwrite-on-second-preparer.** If the owner decides otherwise, that is a new feature, not a change to this one.

## Files to touch

**Create:**

| Path | What |
|---|---|
| `backend/app/services/batches.py` | `create_batch(...)` — the write path helper. |
| `backend/app/services/__init__.py` | **if it does not exist** — `backend/app/services/` is currently absent (`ls backend/app/` returns `bot/`, `routers/` and the module files). Feature 408's *Out of scope* already notes this. |
| `backend/tests/test_batches.py` | The regression tests (the repo's test layout — **check `backend/` for the existing test directory and follow it**; do not invent a second layout). |

**Modify:**

| Path | What |
|---|---|
| `backend/app/models.py` | Add **one line** to `class Batch`: `by_user_id: int \| None = Field(default=None, foreign_key="app_user.id")`. **Change nothing else in this file.** |

**Read but do not modify:**

| Path | Why |
|---|---|
| `features/446-le31-has-no-schema-evolution-mechanism.md` | The hard ordering. |
| `features/417-…` (StockEntry actor FK) | The sibling — and the feature that **explicitly excludes `Batch`**. |
| `features/374-…` (qty_remaining) | The adjacent derivation — **do not change it**. |
| `features/398-…` (`is_prepared`) | The adjacent feature — **do not change it**. |
| `features/385-…` (batch provenance) | The adjacent feature — **do not change it**. |
| `features/429-…` (timestamp convention) | The adjacent feature — **do not change it**. |
| `backend/app/models.py` — `StockEntry`, `Shift`, `Bill`, `Visit` | The four tables that **already** have an actor column. **They are the pattern; do not modify them.** |

## Mandatory LE31 skill list

The external agent **must** load, in this order, before writing code:

1. **`le31-conventions`** — the seven-check gate, the hard invariants, §3.1 (one restaurant, two surfaces; v1 stores counts not identities), §3.2 (fixed stack, no new dependency, `init_db()`-not-Alembic), §4.3 (the append-only ledger pattern), §7 (the quality bar), and the truth invariant.
2. **`le31-v1-feature-pattern`** — the canonical contract shape, the slicing rules, and the *Definition of Done*.
3. **`le31-feature-pipeline`** — where the artefacts land and the commit/push convention.
4. **`le31-handoff-spec`** — the frozen-contract discipline: *do not silently change the slice, scope, or verification path*.
5. **`development`** — the generic code pipeline (specify → plan → tasks → implement → independent review) for the implementation itself.

**Also read** `PROJECT_CHARTER.md` — §3.1 (in scope), §3.2 (out of scope for v1), §4.3 (the append-only ledger pattern), and §7 (the quality bar).

## Mandatory inputs

| Input | Path | Why |
|---|---|---|
| The feature contract | `features/445-le31-batch-has-no-preparer.md` | The scope, the data model, the scenario table, the open questions. |
| The research report | `/opt/data/le31-daily-research-2026-11-06.md` | The gate verdicts, the evidence, the duplicate sweep. |
| The execution probe | `/tmp/le31-daily-2026-11-06/_parent_probe4.py` and `_parent_final.py` | **The parent-run probes that produced the evidence.** They import LE31's own `backend/app/models.py` and run against a throwaway SQLite DB. **Re-runnable.** The venv is at `/tmp/le31-daily-2026-11-06/.probe-venv` (`sqlmodel` 0.0.48 + `sqlalchemy` 2.0.57) — **if `/tmp` has been cleared, recreate it with `uv venv` + `uv pip install "sqlmodel>=0.0.42" "sqlalchemy<2.1"`.** |
| The raw fetches | `/tmp/le31-daily-2026-11-06/` | The third-party READMEs the evidence quotes come from (`readme/FreeOpenSourcePOS__FloCafe.md` and `readme/chamithsilva10__Lazy-Sunday.md` are the triggers). |
| The duplicate-sweep result | the feature file's *Adjacent work* + the report's *Duplicates skipped* | What is **already filed** and must not be re-picked. |

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases (from the feature file's scenario table)

| # | Case | Expected |
|---|---|---|
| 1 | A batch is created by a cook | `by_user_id` = that cook's id |
| 2 | A batch is created with `prepared_by=None` | **accepted**; `by_user_id` is `NULL` — **not** blocked, **not** defaulted to a system user |
| 3 | A batch is created with a **nonexistent** `prepared_by` | **refused by the FK** — no row |
| 4 | A batch is created by a `UserRole.server` | **accepted** — this feature does not restrict roles |
| 5 | A batch is created | **no `StockEntry` row is written** |
| 6 | A batch is created | `prepared_at` behaviour is **unchanged** |
| 7 | The preparer is read back | the id matches what was written |
| 8 | A batch with `by_user_id = NULL` is read back | `NULL`, **distinctly** — not an error, not a default |
| 9 | A `StockEntry` is written against the batch | the `StockEntry`'s own `by_user_id` is **unchanged** — the two actors are different facts |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Create a menu item and **two** users (a cook and a server) **through the real ORM**.
2. Create a batch through `create_batch(...)` as the cook.
3. **Read the batch back** and show `by_user_id` == the cook's id.
4. Write a `StockEntry` against the batch and show that **the ledger's actor and the batch's preparer are two different fields**, and that the ledger's actor is still the server.
5. Create a second batch with `prepared_by=None` and show **`NULL`**, distinctly.
6. Attempt a batch with a nonexistent preparer and show it is **refused** (case 3).

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (the `Batch` model has no `by_user_id` at all), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

LE31's test suite runs on **SQLite**, while production is **Postgres** (charter §4.1). A nullable FK column behaves identically on both. **If the agent adds anything Postgres would enforce differently — a `CHECK`, a `NOT NULL`, a length limit — that is a divergence and must be called out in the commit message.**

## Rollback path

| Aspect | Detail |
|---|---|
| **Revert** | `git revert` the commit. The column is dropped with the model. |
| **Data at risk** | **None.** The column is **nullable** and no existing behaviour depends on it. **Dropping it loses only the preparer attribution for batches created while it existed — and no batch write path exists yet, so in practice: nothing.** |
| **Disable path** | Stop passing `prepared_by`. The column is nullable; existing rows keep their value; new rows get `NULL`. |
| **Migration / rollback cost** | **Zero for the code; NOT zero for the database.** ⚠️ The `ALTER TABLE` needed to add the column to an existing table **cannot be done by `create_all()`** — it needs **feature 446**. **Without 446, the column will not appear on a live database and the feature will silently not work.** |
| **What remains safe if removed** | Everything. No existing behaviour reads or writes the column. |
| **The one irreversible thing** | Nothing at the schema level. **The attribution itself is a fact, and once recorded it should not be edited** — but that is the *preparer's* fact, and the contract makes it immutable by leaving it to the write path. |

## Sign-off gap

**What the agent MUST NOT decide:**

1. **One preparer or several?** The recorded position is **one preparer of record**. A join table or an overwrite behaviour is out of scope.
2. **May a `server` prepare a batch?** The slice **does not restrict roles** — it records whoever the acting user is. In a small restaurant the owner often prepares, and the owner may not be a `cook` in the enum. **An owner decision, recorded not made.**
3. **Should the preparer be immutable once set?** The recommendation is **yes** — a preparer is a historical fact, like a `StockEntry` row. **The agent may implement it as immutable; the agent may NOT make it freely editable.**
4. **Should `Batch.notes` stop being the place for a name?** The recommendation is **yes** — documentation, not code.

**What the agent must report back:**

- The commit SHA and the push confirmation.
- The **failing-then-passing** output of the key regression test.
- The observed acceptance path (steps 1–6 above), with the actual rows shown.
- **A statement of whether feature 446 had landed when this was built**, and what that means for the production database. **This is the single most important line in the report.**
- Any deviation from this contract, stated explicitly rather than absorbed.

## Handoff summary

**One sentence:** *Give a prepared batch the one thing every other table in LE31 already has — a record of the person behind it — in a single nullable column with a foreign key.*

**Three picks of the 84th daily-research pass (2026-11-06):**

| Pick | Slug | Gate | One line |
|---|---|---|---|
| **A** | `le31-order-item-unit-price-is-mutable-in-place-with-no-trace` | **build** | A line's price can be overwritten; the original is unrecoverable and the bill total silently changes. |
| **B** | `le31-batch-has-no-preparer` | **build** | `StockEntry.by_user_id` and `Shift.by_user_id` exist; `Batch` has no actor column, so the preparer of a batch is unknowable. **This contract.** |
| **C** | `le31-has-no-schema-evolution-mechanism` | **build (narrow form)** | `db.py` points at a directory that does not exist, and `create_all()` never alters an existing column. **B is blocked on C.** |

**Feature**: `features/445-le31-batch-has-no-preparer.md`
**Report**: `/opt/data/le31-daily-research-2026-11-06.md`
**Bucket**: v1 · **Gate**: build · **Evidence**: OBSERVED (executed) · **Confidence**: high (gap) / medium (demand)
