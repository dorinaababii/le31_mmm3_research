# HANDOFF — 438-le31-menu-item-has-no-availability-flag

> **Slice contract for the coding agent.** Produced by the 83rd LE31 daily-research pass (2026-11-05), Pick A.
>
> **Feature file**: `features/438-le31-menu-item-has-no-availability-flag.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `MenuItem.model_fields` returned `['category','id','is_prepared','name','photo_url','unit','unit_price']` — **no availability field of any kind**; and two rows, one with a consumed batch and one with no batch at all, carried **identical field values** for every field the model has). All seven checks pass; see the feature file's *Description* and *Why this matters*.

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod, same SQLModel code), §7 (the quality bar: *"Time is UTC"*, *"No magic numbers"*, *"No dead code"*, *"End-to-end before commit"*), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. **Read `features/397-…` FIRST** and confirm the boundary described under *Frozen contract* below. **Do not merge retirement into the sold-out state.**
5. **Add the `is_active` column** to `class MenuItem` in `backend/app/models.py`, with the comment recording the choice and its rationale.
6. **Create `backend/app/services/__init__.py` and `backend/app/services/menu.py`** with the `is_served(item)` helper — **one definition of the rule, imported by every caller.**
7. **Create `backend/app/routers/menu.py`** with `GET /api/menu` (filtered), `POST /api/menu/{item_id}/retire`, and `POST /api/menu/{item_id}/restore`. **Read and restore routes do not write `StockEntry` or `Batch`.**
8. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_sold_out_item_is_still_present` — it is what proves retirement and sold-out did not merge into one field.
9. **Apply the `is_served` filter to the cook's prep-board surface** if that surface exists. **If it does not exist, record that in the PR description rather than creating it.**

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Represent sold-out in this column.** That is **feature 397** — the per-day, derived `sold_out_today` availability state. **This feature owns "is this dish on the menu at all"; 397 owns "is it available today".** The two must be composed by the caller and **never merged into one column.** The test `test_sold_out_item_is_still_present` enforces this.
- **Re-implement 397's derivation inside the helper.** `is_served()` is a pure function of the `MenuItem` row. **If the helper also computed sold-out, it would become a second implementation of 397's rule and the two would drift.** The composition belongs to the caller.
- **Write a `StockEntry` row, or a `Batch` row, on retire or restore.** **A retirement is not a ledger event.** The charter's append-only rule is untouched by this feature. The test `test_retirement_writes_no_ledger_row` enforces this.
- **Delete a `MenuItem` row, or add a delete route.** **The rule is the opposite of deletion** — deletion stays refused while an order references the dish, and that refusal is *why* this column exists.
- **Touch `MenuItem.is_prepared`.** That is **feature 398** — *"the rule with no consumer"*. **This feature does not read it, change it, or give it a consumer.**
- **Touch `MenuItem.category`, or normalise/constrain it.** That is **feature 431**.
- **Touch `MenuItem.unit`.** That is **features 386 / 392 / 407**.
- **Create `backend/app/routers/orders.py`.** There is no orders router today — `backend/app/routers/` holds only `__init__.py` and `tables.py`. **This contract creates a menu router; it does not create the feature that would fill an order.**
- **Write any `OrderItem`, `Bill`, `Visit` or `Shift` row.** Untouched.
- **Introduce Alembic**, or add a foreign key or an index. That is **feature 427** for FKs; charter §3.2 for Alembic.
- **Add a per-day or per-date retirement model.** That is 397's shape. Retirement is a property of the dish until it changes; v1 keeps no history of it.
- **Build a menu-management UI.** The write path is an API; the screen is not in this slice.
- **Change `PROJECT_CHARTER.md`.** The charter is the owner's document.

**Disambiguation**: this slice is about **whether a dish is on the menu at all**. It is **not** about sold-out (397), the quantity derivation (374), whether a dish is prepared (398), its category (431), its unit (386), order taking (02), or the bill (05/415).

## Frozen contract

**The one thing this contract exists to make true:** *a dish that is no longer served must be absent from the menu while its sales history stays intact — and that must not be confused with a dish that is merely sold out today.*

Concretely, after this slice lands:

1. `menu_item` carries exactly one `is_active: bool = True` column. `False` means **retired**.
2. A retired item is **absent** from every menu read that filters on `is_served`.
3. A **sold-out** item is **still present** in the menu read and `is_served()` returns `True` for it — **the two states are distinct and separately testable.**
4. A retired item's **historical `OrderItem` rows still resolve**, because the row was flagged, not deleted.
5. **No `StockEntry` row is written** by retiring or restoring.

**The prohibition:** *representing retirement and sold-out in one field, and writing to the ledger when a dish is retired.*

### The 397/438 boundary — resolve before writing code

| If | Then |
|---|---|
| **397 has not landed** (today's state) | 438 lands alone. `is_served()` is a pure function of `MenuItem.is_active`. The menu read does **not** filter on sold-out. The composition is left to whoever lands 397. |
| **397 has landed first** | The menu read must compose `is_served(item)` **AND** 397's sold-out helper — **calling 397's helper, never re-implementing it.** 438's column stays a separate column. |

**Either way: two columns, never one.** The agent's **first action** is to read `features/397-…` and determine which case applies — and **the commit message must state the resolution.**

### Why the column is a boolean and not a timestamp

`is_active: bool = True`, **not** `retired_at: datetime | None`. A timestamp implies a retirement history that v1 has nowhere to show and no requirement to record, and it would make "retired until 1 March" look implementable when it is not. **A boolean is the smallest representation that makes the distinction, and it is honest about what it does not record.** If the owner later says the menu changes seasonally, **this feature becomes the wrong shape and must be re-specified, not patched.**

### Why `is_active` and not a separate table

A `retired_menu_item(menu_item_id, date)` table would be right *if* retirement were per-day — that is feature 397's shape, and the reason it needs its own table. **Retirement is not per-day; it is a property of the dish until it changes.** A separate table would add a join to every menu read to answer a boolean question.

## Files to touch

| File | Action | Notes |
|---|---|---|
| `backend/app/models.py` | **modify** | Add `is_active: bool = True` to `class MenuItem`, with a comment recording the rationale. **One line.** |
| `backend/app/services/__init__.py` | **create** | `backend/app/services/` **does not exist today.** |
| `backend/app/services/menu.py` | **create** | `is_served(item) -> bool`. **Pure function of the `MenuItem` row** — it must NOT consult `StockEntry` or `Batch`. |
| `backend/app/routers/menu.py` | **create** | `GET /api/menu` (filtered by `is_served`), `POST /api/menu/{item_id}/retire`, `POST /api/menu/{item_id}/restore`. **The write routes must not touch `StockEntry` or `Batch` — put a comment on each saying so.** |
| `backend/tests/test_menu_availability.py` | **create** | The six regression tests listed below. **Confirm the project's test path before assuming this one.** |
| `features/03-kitchen-stock-tracker.md` | **modify** | One line: retirement is not a ledger event; see feature 438. |

**Not touched:** `backend/app/routers/tables.py`, `backend/app/db.py`, `backend/app/cook_bot.py` (or whatever the bot module is called), `index.html`, `PROJECT_CHARTER.md`, every other model.

## Mandatory LE31 skill list

The coding agent **must** load these before writing code. They are in the project repo at `skills/`, and on this VPS they are **not** in the standard `skills_list` index — read them from disk:

- **`le31-conventions`** — `skills/le31-conventions/SKILL.md`. **The fixed stack, the hard invariants, and the seven-check gate.**
- **`le31-v1-feature-pattern`** — `skills/le31-v1-feature-pattern/SKILL.md`. **The contract shape and the Definition of Done.**
- **`development`** → `speckit-specify` / `speckit-plan` / `speckit-tasks` / `speckit-implement`. **Product behaviour changes go through the development pipeline.**
- **`pre-merge-review`** — **product code does not merge on the author's say-so.** An independent reviewer must sign off.

**Also read (not skills, but mandatory context):** `features/397-…` (the boundary), `features/398-…` (`is_prepared`), `features/431-…` (category), `features/374-…` (the quantity derivation), `features/421-…` (the append-only rule), and `PROJECT_CHARTER.md` §3.2 and §4.3.

## Mandatory inputs

| Input | Where | Why |
|---|---|---|
| `PROJECT_CHARTER.md` §3.2 (non-goals), §4.3 (the append-only ledger and the sold-out path) | repo root | **The non-goals list is a hard filter.** Retirement is not on it. The §4.3 sold-out path is what 397 owns. |
| `features/397-…` (sold-out availability) | `features/` | **The boundary.** |
| `features/398-…` (`is_prepared`) | `features/` | The neighbouring boolean on the same table. |
| `features/431-…` (category canonicalisation) | `features/` | The neighbouring field on the same table. |
| `features/374-…` (`qty_remaining` derivation) | `features/` | **Different fact: quantity vs availability.** |
| `features/421-…` (append-only mechanism) | `features/` | **The prohibition on writing the ledger.** |
| The proof script | `/opt/data/le31_proof_picks_2026_11_05.py` | **The parent's execution transcript for this finding.** Run it with `/opt/data/le31-verify-2026-10-27/.venv/bin/python` — that venv has `sqlmodel`/`fastapi`/`pydantic` installed; **the system Python does not have `sqlmodel`.** |
| The research report | `/opt/data/le31-daily-research-2026-11-05.md` | The pass, the evidence, and the rejected alternatives. |

## Verification protocol reference

**Reference**: `skills/le31-research-workflow/SKILL.md` (the curl-only anti-fabrication and signed-delta discipline) and `skills/le31-first-party-defect-proving/SKILL.md` (the execution-proof method). **Read `le31-first-party-defect-proving` — this feature was proven that way and the agent must preserve that property in its own tests.**

**The six required regression tests** (all in `backend/tests/test_menu_availability.py`):

1. `test_retired_item_is_absent_from_menu` — retire a dish, read the menu, assert absent.
2. `test_sold_out_item_is_still_present` — **the boundary test.** A dish with a fully-consumed batch is **still in the menu read** and `is_served()` is `True` for it. **This is the test that proves retirement and sold-out did not merge.**
3. `test_retirement_writes_no_ledger_row` — `StockEntry` count is **unchanged** across a retirement.
4. `test_retired_item_history_still_resolves` — retire a dish that has a historical `OrderItem`; the `OrderItem` still loads and its `menu_item_id` still resolves.
5. `test_restore_brings_the_dish_back` — retire then restore; present again.
6. `test_double_retire_is_refused` — the second retire is refused (409).

**Method — the one that matters:** **write the tests first, watch them fail against the current code, then apply the change and watch them pass.** A test that only ever passed proves nothing, and this feature's entire value is the *distinction*, which is exactly the kind of thing a test that never failed cannot certify.

**End-to-end before commit** (charter §7): run the actual menu read and the actual retire/restore routes against a real database and observe the behaviour change. **Do not declare done from a diff or from green tests alone.**

**Anti-fabrication:** every claim in the PR description must be traceable to a command you ran and its output. **No number, no status code and no test count that you did not observe.**

## Rollback path

**Fully reversible, and deliberately so.**

- **The code rollback:** drop the column, drop `services/menu.py`, drop `routers/menu.py`, drop the test file, revert the one-line note in `features/03-…`. **Nothing today reads a field that does not exist yet, so no existing behaviour can regress.**
- **The data rollback:** `is_active` defaults to `True`, so **every existing `MenuItem` row is active** and the migration is a no-op on existing data. **If the column is dropped, the rows return to their current meaning.**
- **The migration rollback:** LE31 uses `init_db()` (charter §3.2 — **Alembic is a non-goal for v1**), so there is no migration file to revert. **If a migration file is created anyway, that is a scope violation of this contract.**
- **The one irreversible thing:** **if a dish was deleted under the current schema while this feature was in flight, that history is gone.** That loss is exactly what the feature prevents, and it is why the column's value **rises** with time.

**Rollback cost:** minutes. **No data is at risk.**

## Sign-off gap

**What this contract does NOT establish, and the agent must not assume:**

- **That the menu read is the only surface that shows dishes.** The agent must **find** every surface that reads `MenuItem` and apply the filter, or record explicitly which surface it could not find. **A retired dish that still appears somewhere is a failed slice, not a partial success.**
- **That the cook's prep-board surface exists.** It may not. **Record it in the PR description if it does not — do not create it.**
- **That feature 397 will compose correctly.** If 397 lands later, its author must read this contract's *Frozen contract* section. **The composition rule is written down precisely so that this slice cannot be broken by the next one.**
- **That the QR menu (feature 11) honours retirement.** It does not, today. **That is a recorded follow-up, not a defect in this slice.**
- **Any owner decision about seasonal menus.** If the owner says the menu changes seasonally, the shape is wrong and the feature must be re-specified. **The agent is not authorised to make that decision.**

## Handoff summary

One boolean column on `MenuItem`, one service helper, one router with three routes, one filter on each menu surface, six regression tests. **Three to five hours.**

The gap was **proven by execution**, not inferred: LE31's `MenuItem` has **no availability field of any kind**, so a dish that is retired and a dish that merely has no batch today are **the same row with the same field values**. The alternative — deleting the row — destroys the sale history that references it, because `OrderItem` stores `menu_item_id` but snapshots only the *price*, not the *name*.

**The one boundary that must not be crossed:** feature **397** owns *sold-out* (per-day, derived, from the ledger); this feature owns *retired* (stored, until changed). **Two columns, never one** — and `test_sold_out_item_is_still_present` is the test that proves it.

**The one thing that must not happen:** a `StockEntry` row written by a retirement. **The ledger records quantity; this column records whether the dish is on the menu.** They are different facts.
