# le31-a-shift-s-opening-float-can-be-rewritten-after-the-shift-opens — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/536-le31-a-shift-s-opening-float-can-be-rewritten-after-the-shift-opens-and-nothing-records-it-first-party-v1-shift-opening-float-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `536`
- Slug: `le31-a-shift-s-opening-float-can-be-rewritten-after-the-shift-opens`
- Contract file: `features/536-le31-a-shift-s-opening-float-can-be-rewritten-after-the-shift-opens-and-nothing-records-it-first-party-v1-shift-opening-float-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is one of three filed in the same pass, and they form a family.** All three are the same shape: **a fact on a mutable table that the corpus's own contracts disclaim, and that no feature guards.**

| slice | the fact | the table | the corpus's own words that disclaim it |
|---|---|---|---|
| **534** | the bill's **tender method** | `bill` | 532: *"**`bill` is otherwise untouched** — `visit_id`, **`payment_method`**, `paid_at`, `closed_by` … are all unchanged"* · 420: *"**Any change to `Bill.payment_method`**"* |
| **535** | the tip's **formula version** | `derived_tip` | 532: *"This slice changes no formula and no **`formula_version`**"* · 457's Open question 4: *"a version string with no referent is exactly feature 448's shape"* |
| **536** (this one) | the shift's **opening float** | `shift` | 426's Open question 1: *"**`opening_float` is set when the shift opens and is not re-settable**"* · 391: *"**UNCHANGED by this feature**"* |

**They are pairwise disjoint**: 534 owns `bill.payment_method`, 535 owns `derived_tip.formula_version`, **536 owns `shift.opening_float`**. **No two touch the same column. No two touch the same table.** All three add their own append-only event table to `backend/app/models.py` and their own helper. **They may land in one PR or in three — but they must not be merged into one feature, and they must not be widened to cover each other's columns.**

**⚠️ THE ONE THING THAT CAN GO WRONG HERE IS RE-OPENING THE CORPUS'S OWN QUESTION INSTEAD OF IMPLEMENTING IT.** Feature **426**'s Open Question 1 already states this slice's rule — *"**`opening_float` is set when the shift opens and is not re-settable at close time. Re-settable floats make the variance untraceable**"* — but scoped it to *"Does the close endpoint take `opening_float`?"*, **which is a question about a request body.** **This slice implements the rule at the column.** **Do not go back and re-decide 426's question; 426 owns the route's request body, this slice owns the stored column's history.**

**⚠️ THE SECOND THING THAT CAN GO WRONG HERE IS BUILDING A SHIFT ROUTER.** This slice adds **no route**. Feature **426** owns `backend/app/routers/shifts.py`, `POST /api/shifts` and `POST /api/shifts/{id}/close`. **If you find yourself writing a router, stop.** This slice is one table, one helper, one test.

**⚠️ THE THIRD THING THAT CAN GO WRONG HERE IS INLINING THE EXPECTED-CASH FORMULA.** Feature **391** owns `expected_cash` and `variance_for_shift`. Feature 426 says it verbatim: *"The endpoint must not contain its own copy of the `expected_cash` formula. … If 391 has not landed, this feature is **blocked on it** — it may **not** inline a private copy of the formula."* **The same rule applies to this slice: read 391's helper, never copy it.**

**The single sentence this feature exists to make true:** *a shift records what was in the till when it opened once, and afterwards that fact has a history.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one `AppUser` and one `Shift` with `opening_float=100.00`. `UPDATE shift SET opening_float = 9999.00` was **ACCEPTED**. The full schema census confirmed **10 tables, zero `CHECK` constraints, exactly one `UNIQUE` constraint (`bill.visit_id`)**.

The probe is re-runnable: `/opt/data/le31-daily-2026-11-27-scripts/probe_second.py` (probe M).

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **MEDIUM for the demand** — the corpus's own Open Question 1 argues the rule's *reason* (*"the manager would be comparing against a number they could have changed after counting"*), which is an **owner-facing harm, not a hypothetical**. **The defect is LATENT**: `Shift` is constructed **zero** times outside its own class declaration, so no shift row exists to corrupt. **This slice is the cheapest in the corpus to implement — one table, one helper, one test — and the most expensive to implement later**, because later there will be rows to migrate and a variance derived against a float nobody can justify.

**The finding shapes present:** omission (no write-once rule where one is needed), the **seventh shape** (a covered concept — *the variance is derived and explained*, owned by 391 and 528 — with an uncovered instance — *the baseline it was derived against can be rewritten*), and a **new variant**: **the corpus already stated the rule in prose and gave it no home.**

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily-research job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

- `backend/app/models.py` — **one new append-only table**, `ShiftFloatChange` (shift id, `field`, `old_value`, `new_value`, `by_user_id`, `at`). **No column is added to `shift`.** Nothing else in the file changes.
- `backend/app/services/shifts_service.py` (NEW) — the float-change helper: it either refuses, or writes the event and the change in one transaction. **It does not create the shift router and does not change the close route's semantics** — feature **426** owns that.
- `backend/tests/test_shift_opening_float_change.py` (NEW) — the regression test.

**Do NOT touch:** `Shift`'s columns, `Bill`, `DerivedTip`, `Visit`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry`, any router, `index.html`, `PROJECT_CHARTER.md`.

**Do NOT add:** a `float_changed_at` column on `shift` (it preserves one change and loses the second — feature **523** states this rule), a `CHECK` constraint on `opening_float` (**feature 404** owns the money columns' *shape*, including `opening_float = round(opening_float, 2)` — do not duplicate it), a `Payment` table or a `shift_id` column (**feature 391**), a shift router (**feature 426**), the expected-cash formula (**feature 391** — never inline a copy), a denomination decomposition (**feature 504**), a cash-movement ledger (**feature 393**), a variance reason column (**feature 528**), a business-date column (**feature 405**), an `alembic` dependency or a `migrations/` directory (**§3.2**).

## Endpoints and contracts added

**None.** This slice adds no route. **The shift lifecycle router does not exist yet** — feature **426** owns creating it. **This slice adds the helper and the guard beside it, and does not change what any route accepts.** If 426 has landed, the open write must call the helper. **Record which of the two is true in the PR description.**

## Telegram interaction

**None.** The charter's criterion for closing a shift is an **HTTP** endpoint (feature 426). **No bot command, no FSM state, no chat surface.**

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the contract file matches the frozen identifiers above; confirm the statuses of features **391**, **393**, **404**, **405**, **426**, **453**, **504**, **513** and **528**.
2. **The write-path guard is the acceptance criterion.** Build LE31's schema with `SQLModel.metadata.create_all` against a throwaway SQLite file and assert:

   | scenario | expected |
   |---|---|
   | the **open write** creates the shift with its `opening_float` | **ACCEPTED** (the guard must not block the legitimate write) |
   | change `opening_float` on an open or closed shift, **no** event | **REFUSED**, stored value unchanged |
   | change `opening_float` **with** an event in the same transaction | **ACCEPTED**, event carries old value, new value, actor, time |
   | update or delete an event row | **REFUSED** |
   | write a value with more than two decimals | **REFUSED** — feature **404**'s rule, unaffected and not re-implemented here |

   **The probe that produced today's numbers is `probe_second.py` in the research-side scripts directory; run it against the pre-change schema FIRST to watch it fail.** Its output: *"UPDATE shift SET opening_float = 9999.00 -> ACCEPTED"* and *"shift now: opening_float=9999.00"*.
3. **The two-numbers check** — after any accepted change, `shift.opening_float` and the event history's latest `new_value` must agree. **A single number never shows a divergence.**
4. **The variance-divergence check** — this is the check that makes the slice mean something. After the close, `shift.variance` and `variance_for_shift(shift)` (feature **391**'s helper) must still agree. **The stored variance does NOT move when the float does — that is the defect.** If 391 has landed, assert that a rewritten float produces a divergence **that the event table explains**. **If 391 has not landed, record that this check is deferred to 391 and do not inline a private copy of the formula to make it run.**
5. **The negative control** — remove the guard and confirm the regression test **fails**. **A test that passes without the guard proves nothing.** This is the single most important check in this slice.
6. **Regression** — features **391** (the derivation), **426** (the router), **504** (the denominations), **513** (the ordering — the count before the expectation), **528** (the variance's reason), **404** (the money columns' shapes), **453** (the timestamp types), **405** (the business date), **393** (the cash-movement ledger) must all be unaffected. **⚠️ 513 protects the count from being fitted to the expectation; this slice protects the baseline from being fitted to the count. The two are complementary and must not be merged.**
7. **End-to-end** — through the API's terms: open a shift with a float of €100, close it with a counted €145, confirm the variance is €45; then attempt to change the float without an event and confirm the refusal; then change it *with* an event and confirm the event's old value, new value, actor and time — **and that the stored variance and the recomputed variance now disagree, and the event table explains why.**

## Rollback / feature-removal path

- Remove the event model from `backend/app/models.py`.
- Remove `backend/app/services/shifts_service.py`.
- Remove `backend/tests/test_shift_opening_float_change.py`.
- **⚠️ Rolling back requires the same migration work as applying it** — dropping a table cannot be done by `create_all()` either. **Record the prod-migration step in the PR description.**
- **No data loss of existing rows:** the slice adds no column to any existing table. **The event rows it creates are history; dropping the table discards that history — record the count before dropping.**

## What remains safe if removed

- A shift's opening float can be rewritten silently again — **which is the defect.** Do not describe the removal as neutral.
- The owner's end-of-day cash count stops being evidence — **which is the defect.**
- Feature 528's reason requirement becomes an explanation of a number whose baseline is unknown — **which is the defect.**

## Adjacent work (recorded, NOT picked)

- **The bill's four money columns being rewritten after the close** — **feature 532**, filed 2026-11-26. **Same family, different table.**
- **A closed bill's tender method being rewritten after the close** — **feature 534**, filed in this same pass. **Same family, different table.**
- **The tip's formula version being rewritten after the tip is computed** — **feature 535**, filed in this same pass. **Same family, different table.**
- **A seated visit's party size being rewritten after the party is seated** — **feature 533**, filed 2026-11-26. **Same family, different table.**
- **The shift's `by_user_id` actor being rewritten** — **recorded here, not picked.** `Shift.by_user_id` is nullable and freely rewritable (the *value* is unguarded; only `NULL` is refused by the `NOT NULL`). **Feature 417 owns the `StockEntry` actor's foreign key** and the corpus's actor convention generally; **the shift's actor's *history* is a separate question and is not bundled here.**
- **A correction path for the tip's amount** — feature 457's open tension. **Not bundled.**
