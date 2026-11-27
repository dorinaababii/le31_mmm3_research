# le31-an-order-line-s-dish-can-be-swapped-after-the-line-exists — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/537-le31-an-order-line-s-dish-can-be-swapped-after-the-line-exists-first-party-nothing-records-it-v1-order-line-dish-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `537`
- Slug: `le31-an-order-line-s-dish-can-be-swapped-after-the-line-exists`
- Contract file: `features/537-le31-an-order-line-s-dish-can-be-swapped-after-the-line-exists-first-party-nothing-records-it-v1-order-line-dish-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is the missing half of feature 441's guarantee.** 441 owns the rule *"a `StockEntry` may not name a batch and an order line for **different dishes**"* — and it obtains the line's dish by **reading `order_item.menu_item_id` through the order line**, at the moment the ledger row is written.

**A value that can be rewritten after the rule has run makes the rule defeatable after the fact.** The ledger is append-only by charter, so the wrong row is **permanent**.

> **Feature 441**, verbatim: *"**COHERENCE:** `batch.menu_item_id == order_item.menu_item_id`"*, and *"the cross-item rule reads `menu_item_id` **through** the order line"*.

**Five things must not be confused with it, and the corpus says so itself:**

| rule | mechanism | owner |
|---|---|---|
| the **sign and size** of a quantity | a value check at the write site | **feature 456** |
| the **quantity**'s timing and history | event table + write-path guard | **feature 531** |
| the **price**'s mutability and history | history table | **feature 444** |
| the **catalogue's** price history | history table | **feature 523** |
| the **status** transition log and its actor | append-only transition table | **features 379, 452** |
| a ledger row's batch and line must name the **same dish** | a write-path coherence rule | **feature 441** — **read-side, at write time** |
| **the line's dish changing after the line exists** | **event table + write-path guard** | **THIS SLICE** |

**⚠️ The one thing that can go wrong here is filing a duplicate of 441.** 441 owns *the rule*. This slice owns *the value the rule reads*. **Fixing 441 without this feature produces a guarantee over a number that can move; fixing this without 441 produces a record of a change to a value nothing checks.**

**The single sentence this feature exists to make true:** *a line's dish is set when the line is created; after that it is a fact with a history, and the line's price is the price of the dish it names.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with two dishes (Schnitzel €14.00, Margherita €9.00), one batch of Schnitzel, one visit, one served order line at qty 2, one `StockEntry(-2, reason='sale')` and one paid bill.

`UPDATE order_item SET menu_item_id = <margherita>` on the **served** line was **ACCEPTED**. The probe then read back **three numbers that must agree**, and all three disagreed:

| what | value after the rewrite | should say |
|---|---|---|
| `order_item.menu_item_id` | **2** (Margherita) | 1 (Schnitzel) |
| `order_item.unit_price` | **14.00** | 9.00 — the price of the dish it now names |
| `SUM(stock_entry.qty_delta)` for the batch | **-2** | -2 — two **Schnitzel**, while the line says Margherita |

The re-runnable probe is `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path changes a line's dish today (there is no orders router), so the defect is **latent**, not corrupting data.

**The finding shapes present:** omission (no dish-change rule where one is needed), the **seventh shape** (a covered concept — a ledger row's dish coherence, feature 441 — with an uncovered instance — the line's dish itself), **upstream-of-filed-work** (421 and 441 are about to build the write path this defect hides behind), and the **duplicated-derivation** family inverted: three numbers that must agree and do not.

## Mandatory LE31 skill list (load these first)

1. `skills/le31-conventions/SKILL.md` — the seven-check gate, the naming conventions and the table conventions.
2. `skills/le31-backend/SKILL.md` — the backend layout, the SQLModel conventions and the write-path rules.
3. `skills/le31-data/SKILL.md` — the data-model conventions, the actor convention and the decimal rules.
4. `skills/le31-handoff-spec/SKILL.md` — this document's shape, for reference.
5. `skills/le31-v1-feature-pattern/SKILL.md` — the v1 feature pattern this contract follows.
6. `skills/le31-coding-agent-brief/SKILL.md` — **produces the paste-in prompt automatically from this contract. Do not paste chat excerpts into a prompt.**

## Files the slice touches

- **`backend/app/models.py`** — **ADD** `class OrderItemDishChange` (`__tablename__ = "order_item_dish_change"`). **DO NOT** modify `OrderItem`, `MenuItem`, `Batch`, `StockEntry`, `Visit`, `Bill`, `Shift` or `DerivedTip`.
- **A new helper** — `backend/app/services/order_line_service.py` (or the package feature **441** / **421** creates; **if `backend/app/services/` does not exist, create it and say so in the PR**). One function: `change_order_line_dish(session, order_item_id, to_menu_item_id, actor_id)`.
  - **DO NOT** put the helper in `routers/` — it is not a route. Feature 441's own *Out of scope* draws that line.
  - **DO NOT** add the ledger coherence rule (441's), the single `StockEntry` write path (421's), a quantity event (531's) or a price-history table (444's / 523's).
- **Tests** — the regression tests listed in the contract's *Verification protocol*, including the **negative control**.

**NOT touched:** `index.html` (feature **08**'s scope; a thirteen-way collision zone — features 465/466/467/474/475/476/484/487/489/509/511/516 and this corpus's other UI owners), `backend/app/bot/cook_bot.py`, `backend/app/routers/tables.py`, `PROJECT_CHARTER.md`, and every file outside `backend/app/models.py` and the new helper.

## Endpoints and contracts added

**None.** This slice adds **no route**, **no request shape** and **no response shape**. It adds a table, a helper and a rule.

**The refusal is part of the contract even though there is no route:** a dish change on a line that is not `ItemStatus.new` raises a legible error naming the current dish, the requested dish and the line's status. **The error must be legible, because a surface that cannot express it will swallow it** — that is feature **486**'s problem, not this slice's.

## Telegram interaction

**None.** No Telegram surface is added or changed. The **cook bot** (`backend/app/bot/cook_bot.py`) is untouched — a dish change is a waiter's correction.

## Verification protocol (end-to-end acceptance path)

**Re-run the probe first.** `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py`. **Before the fix it prints `ACCEPTED`.** After the fix, the same probe must show the fired-line dish change **refused**.

**The negative control is load-bearing.** A test that asserts "the dish change is refused" **must fail** when the guard is removed — comment out the refusal and watch the test go red. **A test that passes both with and without the guard proves nothing.**

The assertions, in order:

1. `UPDATE order_item SET menu_item_id` on a **served** line is **refused**; the line's `menu_item_id` and `unit_price` are unchanged; **zero** `OrderItemDishChange` rows exist.
2. `change_order_line_dish(..., status='new')` is **accepted**; exactly **one** change row exists with `from_menu_item_id`, `to_menu_item_id`, `from_unit_price`, `to_unit_price`, `by_user_id` and `at` correct; `line.menu_item_id` **and** `line.unit_price` both moved.
3. A **second** change on the same line produces a **second** row — **the case a `previous_*` column would have lost.**
4. A change on a **`cancelled`** line is **refused**.
5. The consistency assertion holds for every change row: `line.menu_item_id == latest_change.to_menu_item_id` and `line.unit_price == latest_change.to_unit_price`.
6. A dish change on a `new` line writes **no** `StockEntry` row and does **not** touch `batch.qty_remaining`.
7. `grep -rn "menu_item_id = " backend/` returns the creation path and the helper, **and nothing else**.

**⚠️ Postgres was NOT exercised** — `psycopg` is not importable in the verification venvs on this VPS (sqlmodel 0.0.48 / SQLAlchemy 2.1.6). **Every Postgres claim in the contract is proved from the DDL rendering and dialect behaviour, not a live round trip.** The write-path rule is enforced in the application helper and therefore behaves identically on both databases — feature **441** made the same choice for the same reason.

**⚠️ The demand is UNEVIDENCED.** No code path changes a line's dish today. The defect is **latent**. The contract says so in its *Evidence class* line and in *Why this matters*.

## Rollback / feature-removal path

1. Drop `OrderItemDishChange` (`DROP TABLE order_item_dish_change;`).
2. Delete the helper file, or reduce it to a single function that always refuses.
3. Remove the `OrderItemDishChange` import and class from `backend/app/models.py`.
4. Remove the tests.

**The rollback is safe because the slice is additive.** It adds a table and a helper and **changes no existing column** — so removing it cannot leave a half-migrated database. **The one caveat: if a dish change was ever recorded and then the feature is rolled back, the recorded changes are lost and the lines' current dishes are unrecoverable.** That is why the table is append-only and why the rollback step says to check for rows before dropping.

## What remains safe if removed

- **Every existing behaviour is unchanged.** No route, no request shape and no response shape is touched, so no client can notice the removal.
- **`order_item.menu_item_id` remains exactly as it is** — the same bare foreign key, with the same defect. **The defect returns with the feature; the slice only ever made it impossible to exercise.**
- **Feature 441's coherence rule keeps working at write time.** This slice does not own it and does not change it.
- **Features 444, 456, 531, 379, 452 are unaffected** — a different column, a different rule, a different event table.

## Adjacent work (recorded, NOT picked)

- **`order_item.course`** — the line's course (`appetizer / main / dessert`) is **equally rewritable** after the line exists, and it is **not** covered by the sweep either (`order_item.{0,30}course.{0,40}(update|mutable|rewrite|change)` → **0 files**). **It is a different question — a course is a routing hint for the kitchen, not an identity — and it is recorded in the contract's *Open questions* 5. It is NOT taken by this slice.**
- **`order_item.notes`** — likewise rewritable, **0** corpus hits, **not taken**.
- **`order_item.fired_at` / `ready_at` / `served_at`** — likewise rewritable, **0** corpus hits, **not taken**. **Feature **452** owns *status versus timestamps* — the comparison — and feature **379** owns the transition log; the timestamps' own mutability is a separate question, recorded here.**
- **`visit.table_id`** — filed by this same pass as **feature 538**.
- **`visit.server_id`** — filed by this same pass as **feature 539**.
- **`bill.closed_by`** — the bill's closer can be rewritten, **0** corpus hits for the mutation. **Feature **443** owns the comparison between it and `visit.server_id`; its own mutability is a separate question, recorded here, not taken.**
- **`stock_entry.ref_order_item_id`** — rewritable, **0** corpus hits for the mutation — **but feature **470**'s database trigger refuses **all** `UPDATE` and `DELETE` on `stock_entry`, so it is covered by a filed feature. **Not taken.**
- **`menu_item.photo_url`, `menu_item.is_prepared`, `batch.photo_url`, `batch.notes`, `batch.qty_start`** — all rewritable, **0** corpus hits for the mutation. **Recorded here so the next pass files them or discards them deliberately. None is taken.**
