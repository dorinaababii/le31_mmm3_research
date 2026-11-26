# le31-an-order-line-s-quantity-can-be-rewritten-after-the-line-exists — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/531-le31-an-order-line-s-quantity-can-be-rewritten-after-the-line-exists-first-party-nothing-records-it-v1-order-line-quantity-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `531`
- Slug: `le31-an-order-line-s-quantity-can-be-rewritten-after-the-line-exists`
- Contract file: `features/531-le31-an-order-line-s-quantity-can-be-rewritten-after-the-line-exists-first-party-nothing-records-it-v1-order-line-quantity-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is the feature that features 470 and 471 both asked for.** Two features, on two different days, by two different passes, found this exact defect and both wrote *"recorded, not filed"*:

> **Feature 470**, *Adjacent evidence*: *"**`UPDATE order_item.qty -> 99` was ACCEPTED.** Feature 456 owns the sign and size rule; feature 444 owns the unit price; **neither owns the quantity changing after the line exists.** Recorded, not filed."*

> **Feature 471**, *Adjacent evidence*: *"**`UPDATE order_item.qty -> 99` was ACCEPTED.** … **nobody owns the quantity changing after the line exists.** Recorded, not filed."*

**Four things must not be confused with it, and the corpus says so itself:**

| rule | mechanism | owner |
|---|---|---|
| the **sign and size** of a quantity (no `0`, no `-5`) | a value check at the write site | **feature 456** — filed |
| the **price**'s mutability and history | history table | **feature 444** — filed |
| the **status**' transition log and its actor | append-only transition table | **features 379, 452** — filed |
| the line's **insertion order** | an `added_at` column | **feature 430** — filed |
| **the quantity's timing and history** | **event table + write-path guard** | **THIS SLICE** |

**⚠️ The one thing that can go wrong here is filing a duplicate of 456.** 456 owns *what* a quantity may be. This slice owns *when* it may change. **456's `Out of scope` says the price's mutability is 449's "same table, adjacent column"** — this slice is the quantity's own adjacent column, with a different mechanism (an event, not a check).

**The single sentence this feature exists to make true:** *a quantity is set while the line is `new`; after the line has been fired, the quantity is a fact with a history.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one `MenuItem`, one `Batch`, one `Visit` and one `OrderItem`. `UPDATE order_item SET qty=99` on a **`served`** line was **ACCEPTED**; `UPDATE order_item SET qty=1` on a line whose **bill was already closed and paid** was **ACCEPTED**. The probe compared **two numbers that should agree** and found them diverging: `SUM(order_item.qty * order_item.unit_price)` = **6.50** against `bill.total_due` = **14.30**. `SUM(stock_entry.qty_delta)` stayed at **-2** — **the append-only ledger recorded nothing.**

The probe is re-runnable: `/opt/data/le31-brainstorm-2026-11-26-scripts/probe_lifecycle.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path changes a line's quantity today (there is no orders router), so the defect is **latent**, not corrupting data.

**The finding shapes present:** omission (no quantity-change rule where one is needed), unenforced mechanism (the append-only ledger has no counterpart for the order's own quantity), the **seventh shape** (a covered concept — the quantity's *value* — with an uncovered instance — the quantity's *timing*), and the **corpus hand-off** shape (a defect recorded twice and filed never).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

- `backend/app/models.py` — **one new append-only table**, the order-line quantity-change event (line id, old qty, new qty, `by_user_id`, `at`). **No column is added to `order_item`.** Nothing else in the file changes.
- `backend/app/services/orders_service.py` (NEW) — the quantity-change helper: it either refuses, or it writes the event and the change in one transaction. **It does not invent an orders router** — feature **02** owns that, and the helper is the seam the future router calls.
- `backend/tests/test_order_line_quantity_change.py` (NEW) — the regression test.

**Do NOT touch:** `OrderItem`'s columns, `Bill`, `Visit`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `DerivedTip`, `Shift`, any router, `index.html`, `PROJECT_CHARTER.md`.

**Do NOT add:** a `previous_qty` column (it preserves one change and loses the second — feature **523** states this rule), a `CHECK` on `qty` (feature **456** owns the value's shape), a price-history table (feature **444**), a status-transition log (features **379**, **452**), an `added_at` column (feature **430**), a `StockEntry` row for a quantity change (**a quantity change moves no stock** — feature **452**'s own words).

## Endpoints and contracts added

**None.** This slice adds no route. Today there is no orders router to attach a route to — **the helper is the contract**, and feature **02** will call it. This is the same discipline feature **430** used for its `added_at` helper.

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface. **A quantity change is a fact about the order, not an announcement to the kitchen** — the kitchen is not told, and that is deliberate.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the contract file matches the frozen identifiers above; confirm the statuses of features **379**, **444**, **452**, **456** and **415**.
2. **The write-path guard is the acceptance criterion** — a schema constraint alone cannot carry this rule (the database has no notion of a row's history). Build LE31's schema with `SQLModel.metadata.create_all` against a throwaway SQLite file and assert:

   | scenario | expected |
   |---|---|
   | change the qty on a line with `status=new`, no event | **ACCEPTED** |
   | change the qty on a line with `fired_at` set, **no** event | **REFUSED**, stored qty unchanged |
   | change the qty on a fired line **with** an event in the same transaction | **ACCEPTED**, event carries old qty, new qty, actor, time |
   | update or delete an event row | **REFUSED** |
   | the **close write** sets the money columns | **ACCEPTED** (the guard must not block the legitimate write) |

   **The probe that produced today's numbers is `probe_lifecycle.py` in the research-side scripts directory; run it against the pre-change schema FIRST to watch it fail.** Its output: *"UPDATE order_item SET qty=99 on a SERVED line -> ACCEPTED, qty now 99"* and *"SUM(order_item.qty * unit_price) NOW = 6.50"* against *"bill.total_due = 14.30"*.
3. **The two-numbers check** — after any accepted quantity change, `SUM(order_item.qty * order_item.unit_price)` for the visit and the line's event history must agree on the current quantity. **A single number never shows a divergence.**
4. **The negative control** — remove the guard and confirm the regression test **fails**. **A test that passes without the guard proves nothing.** This is the single most important check in this slice.
5. **Regression** — features **456** (the value's sign and size), **444** (the price's history), **452** and **379** (status and its log), **430** (insertion order), **435** (the `Bill → order_item` edge), **415** (the close write), **421** (the ledger's write path) must all be unaffected. **Note for 452:** a status transition moves no stock, and a quantity change moves no stock either — **no `StockEntry` row is written by this slice.**
6. **End-to-end** — through the API's terms: order a line, fire it, attempt to change its quantity without an event and confirm the refusal; then change it *with* an event and confirm the event's old and new quantities, actor and time.

## Rollback / feature-removal path

- Remove the event model from `backend/app/models.py`.
- Remove `backend/app/services/orders_service.py`.
- Remove `backend/tests/test_order_line_quantity_change.py`.
- **⚠️ Rolling back requires the same migration work as applying it** — dropping a table cannot be done by `create_all()` either. **Record the prod-migration step in the PR description.**
- **No data loss of existing rows:** the slice adds no column to any existing table. **The event rows it creates are history; dropping the table discards that history — record the count before dropping.**

## What remains safe if removed

- A fired line's quantity can be rewritten silently again — **which is the defect.** Do not describe the removal as neutral.
- The bill's stored subtotal and the order's lines can drift apart with no record — **which is the defect.**

## Adjacent work (recorded, NOT picked)

- **The bill's money columns being rewritten after the close** — **feature 532**, filed in this same pass. **Same family, different table, different slice.** The two do not conflict; 532 does not touch `order_item` and this slice does not touch `bill`.
- **A seated visit's party composition being rewritten** — **feature 533**, filed in this same pass. **Same family, different table.**
- **The order-line's price history** — **feature 444**, filed. **Same table, adjacent column.**
- **The quantity's sign and size** — **feature 456**, filed. **Same column, different rule.**
- **`Batch.qty_remaining` vs `SUM(stock_entry.qty_delta)`** — **feature 471**, filed. **A different table and a different question** (a stored column vs a derivation), but the same *shape*.
- **The stock ledger's write path** — **feature 421**. **This slice writes nothing to the ledger.**
- **A question this slice deliberately does not answer** — should a quantity change after the bill closes raise a flag on the bill? See *Open questions* 4 in the contract. **It is recorded, not decided.**
