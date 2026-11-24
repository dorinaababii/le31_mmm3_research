# le31-a-menu-item-can-be-deleted-while-its-batches-and-its-order-lines-still-point-at-it — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/522-le31-a-menu-item-can-be-deleted-while-its-batches-and-its-order-lines-still-point-at-it-v1-catalogue-delete-guard.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `522`
- Slug: `le31-a-menu-item-can-be-deleted-while-its-batches-and-its-order-lines-still-point-at-it`
- Contract file: `features/522-le31-a-menu-item-can-be-deleted-while-its-batches-and-its-order-lines-still-point-at-it-v1-catalogue-delete-guard.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is the feature that features 470 and 471 both asked for.** Two features, on two different days, by two different passes, found this exact defect and both wrote *"owned by no feature"* and *"recorded, not filed"*:

> **Feature 470**, *Adjacent evidence*: *"**The catalogue's delete/retire path is owned by no feature** and is recorded as adjacent evidence in the 2026-11-12 report, not filed here."*

> **Feature 471**, *Adjacent evidence*: *"**No feature owns the catalogue's delete/retire path.** Recorded, not filed."*

**Three things must not be confused with it, and the corpus says so itself:**

| rule | mechanism | owner |
|---|---|---|
| retire a dish (a **flag**) | boolean column + read filters | **feature 438** — filed |
| sold out for today | per-day derived record | **feature 397** — filed |
| the catalogue's own **price** history | history table | **feature 523** — THIS PASS |
| **the catalogue's delete path** | **`ON DELETE` clause + write-path guard** | **THIS SLICE** |

**⚠️ The one thing that can go wrong here is deleting the wrong thing.** A dish with history must be **retired**, not deleted. `CASCADE` is **wrong** — it would delete `Batch` rows, and `StockEntry` rows reference `batch.id`, so cascading a batch away cascades the ledger away. **`SET NULL` is impossible** — both columns are `NOT NULL`. **`RESTRICT` is the answer**, and it is the default in both SQLite and Postgres, so stating it makes the rule legible rather than implied.

**The single sentence this feature exists to make true:** *a menu item that has been ordered from is never removed from the catalogue — it is retired, and the history that points at it stays readable.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one `MenuItem`, one `Batch` and one `OrderItem` that both reference it. `DELETE FROM menu_item` was **ACCEPTED**; the batch and the order line **survived** pointing at a row that no longer exists. The probe also enumerated every `ForeignKey` in the schema: **every `ondelete` is `None`** — no `RESTRICT`, no `CASCADE`, no `SET NULL` anywhere in ten tables.

The probe is re-runnable: `/opt/data/le31-brainstorm-2026-11-24-scripts/probe_schema.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path deletes a menu item today, so the defect is **latent**, not corrupting data.

**The finding shapes present:** omission (no delete rule where one is needed), unenforced mechanism (two inbound foreign keys that cannot express what a delete should do), and the "corpus hand-off" shape (a defect recorded twice and filed never).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

- `backend/app/models.py` — **`ondelete="RESTRICT"` on `Batch.menu_item_id` and `OrderItem.menu_item_id`.** Nothing else in the file changes.
- `backend/app/services/catalogue_service.py` (NEW) — `delete_menu_item()` (raises) and `retire_menu_item()`. **Shared with feature 523 — the two are designed to land together or in either order.**
- `backend/app/routers/menu.py` (NEW or existing) — the delete route, refusing with **409**.
- `backend/tests/test_menu_item_delete_guard.py` (NEW) — the regression test.

**Do NOT touch:** `MenuItem`'s other columns, `Batch`, `OrderItem`, `Bill`, `StockEntry`, `Visit`, any other table, any other router, `index.html`, `PROJECT_CHARTER.md`.

**Do NOT add:** a `deleted_at` column (that would be a **third** way to take a dish off the menu — the very thing this slice removes), a `CASCADE` clause, a `SET NULL` clause, a sold-out mechanism (feature **397**), the availability flag (feature **438**), a price-history table (feature **523**).

## Endpoints and contracts added

One route: the catalogue delete. **It refuses when the item has history (409) and says why.** If feature **438** has landed, its retirement route lives in the same module — **point it at this service rather than duplicating the rule.**

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface. Charter §3.1 keeps the Telegram surface to cook and manager; a catalogue delete is a manager action and, if the owner wants it in the bot, that is a separate feature citing this one.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the contract file matches the frozen identifiers above; **confirm feature 446's status** (see the ordering constraint below) and feature **438**'s.
2. **The write-path guard is the acceptance criterion** — the DDL clause alone is not, because SQLite's foreign keys are off in dev (feature **427**). Build LE31's schema with `SQLModel.metadata.create_all` against a throwaway SQLite file and assert:

   | scenario | expected |
   |---|---|
   | delete a menu item **with** a `Batch` | **REFUSED** |
   | delete a menu item **with** an `OrderItem` | **REFUSED** |
   | delete a menu item with **neither** | allowed (per *Open questions* 1) |
   | delete a menu item, then read the `Batch` | **the batch is still there** |
   | delete a menu item, then read the `OrderItem` | **the line is still there** |

   **The probe that produced today's numbers is `probe_schema.py` in the research-side scripts directory; run it against the pre-change schema FIRST to watch it fail.** Its output: *"DELETE FROM menu_item WHERE id=<menu_item> ACCEPTED … batches still pointing at the deleted menu_item : 1 … order_lines still pointing at the deleted item : 1"*.
3. **The DDL clause** — assert `ondelete == "RESTRICT"` on both foreign keys, and assert it renders in the Postgres DDL. **⚠️ Postgres was NOT exercised** (see *Adjacent work*).
4. **The negative control** — remove the guard and confirm the regression test **fails**. **A test that passes without the guard proves nothing.** This is the single most important check in this slice.
5. **Regression** — features **438**, **397**, **427**, **459**, **471** and **470** must be unaffected. **Note for 438:** 438 owns the flag and the filters; this slice owns the absence of a delete path. **A dish with no history may still be retired and still be deleted — both must work.**
6. **End-to-end** — through the API's terms: retire a dish that has been ordered, confirm it disappears from the menu read, then attempt to delete it and confirm the **409** with an operator-readable reason.

## Rollback / feature-removal path

- Remove `ondelete="RESTRICT"` from the two foreign keys in `backend/app/models.py`.
- Remove `backend/app/services/catalogue_service.py` and the delete route.
- Remove `backend/tests/test_menu_item_delete_guard.py`.
- **⚠️ Rolling back requires the same migration work as applying it** — a foreign key's `ON DELETE` clause cannot be removed by `create_all()` either. **Record the prod-migration step in the PR description.**
- **No data loss:** the slice adds no column and no table.
- **⚠️ If a live database already holds orphaned `Batch`/`OrderItem` rows pointing at a deleted `MenuItem`, rolling back does not repair them and the slice did not create them.** Record the count.

## What remains safe if removed

- A menu item with history can be deleted again, orphaning its batches and its order lines — **which is the defect.** Do not describe the removal as neutral.

## Adjacent work (recorded, NOT picked)

- **The catalogue's own price history** — **feature 523**, filed in this same pass. **The two write into the same `catalogue_service.py`; they do not conflict.**
- **The SQLite foreign-key pragma** — feature **427**. When it lands, `RESTRICT` starts firing in dev too. **This slice does not wait for it and does not enable it.**
- **`UPDATE batch.qty_remaining -> 999` was ACCEPTED** — feature **374** removes the column; until then it is writable. Recorded by features 470 and 471.
- **The staff role's mutability** — **feature 524**, filed in this same pass.
- **A dish with no history at all — should it still be deletable?** See *Open questions* 1 in the contract. **The default is recorded; the owner may decide otherwise, and the decision is one line.**
