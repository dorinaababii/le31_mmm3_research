# le31-the-catalogue-s-own-price-can-be-rewritten-with-no-trace — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/523-le31-the-catalogue-s-own-price-can-be-rewritten-with-no-trace-v1-menu-price-history.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `523`
- Slug: `le31-the-catalogue-s-own-price-can-be-rewritten-with-no-trace`
- Contract file: `features/523-le31-the-catalogue-s-own-price-can-be-rewritten-with-no-trace-v1-menu-price-history.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is the scope note that feature 444 wrote and did not take.** Feature **444** (`le31-order-item-unit-price-is-mutable-in-place-with-no-trace`) owns the **order line's** price history and put this in its own *Out of scope* list, verbatim:

> - **The menu price's own history.** The menu is *configuration*; a changed menu price is a catalogue edit, and **the catalogue has no write path today.** This feature records the **line's** price. (The menu-price overwrite is recorded below as an adjacent observation, not a pick.)

And feature **471** recorded the same finding a second time, verbatim:

> - **`UPDATE menu_item.unit_price -> 99.00` was ACCEPTED** — the catalogue's price is a second mutable number with no history. … **The catalogue's own price history is a third thing**, owned by nobody. Recorded, not filed.

**Three things must not be confused with it:**

| rule | column | owner |
|---|---|---|
| what price a **line** may carry (`price_reason`, `comp`, `manager_override`) | `order_item.unit_price` | **feature 449** — filed |
| the **line's** price history | `order_item.unit_price` | **feature 444** — filed |
| the **catalogue's** price history | **`menu_item.unit_price`** | **THIS SLICE** |

**⭐ THE ONE THING THAT MAKES THIS SLICE CHEAP, AND THE ONE THING THAT MAKES IT TRIVIAL:** `OrderItem` already carries its **own** `unit_price`, so a line taken at €2.50 stays at €2.50 when the menu moves to €3.00. **That snapshot behaviour is CORRECT today and feature 444 proved it — do not "fix" it.** **The only missing thing is the memory of what the menu used to charge.** This slice adds the history; it changes no line's price and no bill.

**⚠️ DO NOT IMPLEMENT THIS AS A COLUMN.** A `previous_price` column on `menu_item` preserves **exactly one** change and loses the second. **A history is a table** — the corpus has learned this three times (features 470, 471, 444).

**The single sentence this feature exists to make true:** *the price a dish costs today, and the price it cost when it was sold, are two different facts, and only one of them may be overwritten.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — `UPDATE menu_item SET unit_price = 99.00` was **ACCEPTED silently** against LE31's real schema (`SQLModel.metadata.create_all` on a throwaway SQLite file). Feature 444's own probe on 2026-11-06 recorded the same acceptance; the schema built today has the same ten tables, the same `menu_item` columns and **zero** price-change, audit or history tables.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path changes a menu price today, so the defect is **latent**.

**The finding shapes present:** omission (no history where one is needed) and the "corpus hand-off" shape (a defect named in two features' own scope lists and filed by neither).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

- `backend/app/models.py` — **the new `MenuItemPriceChange` table.** No change to `MenuItem`'s columns.
- `backend/app/services/catalogue_service.py` (NEW) — `set_menu_item_price()` and `list_price_changes()`. **Shared with feature 522 — the two are designed to land together or in either order.**
- `backend/app/routers/menu.py` (NEW or existing) — the price-change route, which must go through the service.
- `backend/tests/test_menu_item_price_history.py` (NEW) — the regression test.

**Do NOT touch:** `OrderItem`, `Bill`, `DerivedTip`, `StockEntry`, `Batch`, `Visit`, `AppUser`, any other table, `index.html`, `PROJECT_CHARTER.md`.

**Do NOT add:** a `previous_price` column on `menu_item`, a `price_reason` on the catalogue (feature **449** owns the line's), any change to the order line's price history (feature **444**), a tax rate (feature **408**), a rounding mode (feature **410**).

## Endpoints and contracts added

One route: the catalogue price change. **It writes the change row and the column in one transaction**, and it is the only way the price may change.

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the contract file matches the frozen identifiers above; confirm features **444**, **449**, **451** and **470**'s status.
2. **The history is the acceptance criterion.** Build LE31's schema with `SQLModel.metadata.create_all` against a throwaway SQLite file and assert:

   | scenario | expected |
   |---|---|
   | menu item created at €11.50, price changed to €13.00 | **both** the column and one change row exist |
   | the change row's `old_price` | **€11.50** |
   | the change row's `new_price` | **€13.00** |
   | the change row's `by_user_id` | **the actor** |
   | a line taken at €11.50, then the price changed to €13.00 | **the line still says €11.50** — the snapshot behaviour must not change |
   | a price change that does not change the price | **no row** (per *Open questions* 5) |

   **The probe that produced today's numbers is `probe_schema.py` in the research-side scripts directory; run it against the pre-change schema FIRST to watch it fail.**
3. **Two rows, one transaction** — assert that a change row and the column update are committed together. **A change row whose column update failed — or the reverse — is worse than neither.** Force the failure and assert nothing is written.
4. **The negative control** — change the price with a **bare `UPDATE`** and confirm the regression test **fails** (no row is written). **A test that passes when the write path is bypassed proves nothing.** This is the single most important check in this slice.
5. **The table, not a column** — assert `menu_item` still has exactly the columns it has today, and that a `menu_item_price_change` table exists.
6. **The Postgres rendering** — assert the DDL renders. **⚠️ Postgres was NOT exercised** (see *Adjacent work*).
7. **Regression** — features **444**, **449**, **435**, **415**, **457**, **420**, **408**, **410**, **411** and **403** must be unaffected.
8. **End-to-end** — through the API's terms: change a price, read the menu (the new price shows), read the history (the old price is there), and read an open order line (it keeps the price it was taken at).

## Rollback / feature-removal path

- Remove the `MenuItemPriceChange` table from `backend/app/models.py`.
- Remove `backend/app/services/catalogue_service.py`'s price functions and the price-change route.
- Remove `backend/tests/test_menu_item_price_history.py`.
- **The table is additive**, so the rollback is a plain drop — **no migration is needed to undo it** (unlike feature **522**'s `ON DELETE` clause).
- **Data loss:** the history rows are lost. **That is the only thing this slice creates, and it is the thing the slice exists to keep.**
- **⚠️ Prices changed before the slice landed have no history and cannot be reconstructed.** Record the count in the PR description; **do not fabricate the missing history.**

## What remains safe if removed

- A menu price can be rewritten with no record of what it was or who changed it — **which is the defect.** Do not describe the removal as neutral.

## Adjacent work (recorded, NOT picked)

- **The catalogue's delete path** — **feature 522**, filed in this same pass.
- **`MenuItem.unit` and `MenuItem.category` are mutable in the same way the price is** — the same guard should cover them, and the implementer should say whether it does rather than the price being special-cased alone. **Recorded in *Open questions* 6; not picked.**
- **The staff role's mutability** — **feature 524**, filed in this same pass.
- **Who may change a price** — feature **403**'s role policy. **This slice records the actor; it does not decide who may act.**
- **A price change while an open visit holds lines at the old price** — see *Open questions* 1. **The default is recorded: no block.**
