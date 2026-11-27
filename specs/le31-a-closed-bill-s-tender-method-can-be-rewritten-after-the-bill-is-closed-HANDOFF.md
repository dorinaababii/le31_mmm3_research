# le31-a-closed-bill-s-tender-method-can-be-rewritten-after-the-bill-is-closed — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/534-le31-a-closed-bill-s-tender-method-can-be-rewritten-after-the-bill-is-closed-and-nothing-records-it-first-party-v1-bill-tender-method-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `534`
- Slug: `le31-a-closed-bill-s-tender-method-can-be-rewritten-after-the-bill-is-closed`
- Contract file: `features/534-le31-a-closed-bill-s-tender-method-can-be-rewritten-after-the-bill-is-closed-and-nothing-records-it-first-party-v1-bill-tender-method-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is one of three filed in the same pass, and they form a family.** All three are the same shape: **a fact on a mutable table that the corpus's own contracts disclaim, and that no feature guards.**

| slice | the fact | the table | the corpus's own words that disclaim it |
|---|---|---|---|
| **534** (this one) | the bill's **tender method** | `bill` | 532: *"**`bill` is otherwise untouched** — `visit_id`, **`payment_method`**, `paid_at`, `closed_by` … are all unchanged"* · 420: *"**Any change to `Bill.payment_method`**"* |
| **535** | the tip's **formula version** | `derived_tip` | 532: *"This slice changes no formula and no **`formula_version`**"* · 457's Open question 4: *"a version string with no referent is exactly feature 448's shape"* |
| **536** | the shift's **opening float** | `shift` | 426's Open question 1: *"**`opening_float` is set when the shift opens and is not re-settable**"* · 391: *"**UNCHANGED by this feature**"* |

**They are pairwise disjoint**: 534 owns `bill.payment_method`, 535 owns `derived_tip.formula_version`, 536 owns `shift.opening_float`. **No two touch the same column. No two touch the same table.** All three add their own append-only event table to `backend/app/models.py` and their own helper. **They may land in one PR or in three — but they must not be merged into one feature, and they must not be widened to cover each other's columns.**

**⚠️ The one thing that can go wrong here is WIDENING 534 INTO 532.** Feature 532 owns the four **money** columns and **explicitly disclaims** `payment_method`. 532's guard refuses a change to *how much*; **534's guard refuses a change to *how it was paid*.** If you find yourself adding `subtotal_items`, `subtotal_tax`, `total_due` or `total_paid` to this slice's event table — **stop. That is 532's, and it is filed.**

**The single sentence this feature exists to make true:** *a closed bill records how it was paid once, and afterwards that fact has a history.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with a 4-seat `Table`, one `AppUser`, one `Visit`, one `OrderItem` and one `Bill` with `payment_method=cash`. `UPDATE bill SET payment_method = 'card'` was **ACCEPTED** — **a cash bill became a card bill, silently.** The full schema census confirmed **10 tables, zero `CHECK` constraints, exactly one `UNIQUE` constraint (`bill.visit_id`)**.

The probe is re-runnable: `/opt/data/le31-daily-2026-11-27-scripts/probe_first_party.py` (probe D).

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path writes a bill today (there is no bills router), so the defect is **latent**, not corrupting data.

**The finding shapes present:** omission (no write-once rule where one is needed) and the **seventh shape** (a covered concept — *the bill's money is protected*, owned by 532 — with an uncovered instance — *the bill's tender method is not*).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily-research job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

- `backend/app/models.py` — **one new append-only table**, `BillTenderMethodChange` (bill id, `field`, `old_value`, `new_value`, `by_user_id`, `at`). **No column is added to `bill`.** Nothing else in the file changes.
- `backend/app/services/bills_service.py` (NEW) — the tender-method-change helper: it either refuses, or writes the event and the change in one transaction. **It does not rewrite the close route's semantics** — feature **415** owns that.
- `backend/tests/test_bill_tender_method_change.py` (NEW) — the regression test.

**Do NOT touch:** `Bill`'s columns, `DerivedTip`, `Visit`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `Shift`, any router, `index.html`, `PROJECT_CHARTER.md`.

**Do NOT add:** a `previous_payment_method` column (it preserves one change and loses the second — feature **523** states this rule), a `CHECK` constraint on `payment_method` (**feature 442** owns it), a `Payment` table or a `shift_id` column (**feature 391** owns it), a split-tender model (**feature 14**), a refund path (**feature 450**), an `alembic` dependency or a `migrations/` directory (**§3.2**).

## Endpoints and contracts added

**None.** This slice adds no route. **The bill-close route does not exist yet** — feature **415** owns it. **This slice adds the helper and the guard beside it, and does not change what any route accepts.** If 415 has landed, the close write must call the helper. **Record which of the two is true in the PR description.**

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the contract file matches the frozen identifiers above; confirm the statuses of features **391**, **415**, **420**, **442**, **450**, **457** and **532**.
2. **The write-path guard is the acceptance criterion** — a schema constraint cannot carry this rule (the database has no notion of a row's history). Build LE31's schema with `SQLModel.metadata.create_all` against a throwaway SQLite file and assert:

   | scenario | expected |
   |---|---|
   | the **close write** creates the bill with its `payment_method` | **ACCEPTED** (the guard must not block the legitimate write) |
   | change `payment_method` on a closed bill, **no** event | **REFUSED**, stored value unchanged |
   | change `payment_method` on a closed bill **with** an event in the same transaction | **ACCEPTED**, event carries old value, new value, actor, time |
   | update or delete an event row | **REFUSED** |
   | change `payment_method` to a value outside the enum | **REFUSED** — feature **442**'s rule, unaffected and not re-implemented here |

   **The probe that produced today's numbers is `probe_first_party.py` in the research-side scripts directory; run it against the pre-change schema FIRST to watch it fail.** Its output: *"UPDATE bill SET payment_method = 'card' -> ACCEPTED"* and *"bill now: payment_method=card"*.
3. **The two-numbers check** — after any accepted change, `bill.payment_method` and the event history's latest `new_value` must agree. **A single number never shows a divergence.**
4. **The negative control** — remove the guard and confirm the regression test **fails**. **A test that passes without the guard proves nothing.** This is the single most important check in this slice.
5. **Regression** — features **391** (the `Payment` table and the derivation), **415** (the close route), **420** (what `total_paid` means), **442** (the enum membership), **450** (refunds), **457** (the tip formula), **532** (the money columns), **435** (the `Bill → order_item` edge), **448** (the bill's identity) and **411** (`Decimal` precision) must all be unaffected. **⚠️ 532's guard and this slice's guard must coexist: 532 refuses a change to the four money columns; this slice refuses a change to the tender method.**
6. **End-to-end** — through the API's terms: close a bill paid in cash, attempt to change `payment_method` without an event and confirm the refusal; then change it *with* an event and confirm the event's old value, new value, actor and time.

## Rollback / feature-removal path

- Remove the event model from `backend/app/models.py`.
- Remove `backend/app/services/bills_service.py`.
- Remove `backend/tests/test_bill_tender_method_change.py`.
- **⚠️ Rolling back requires the same migration work as applying it** — dropping a table cannot be done by `create_all()` either. **Record the prod-migration step in the PR description.**
- **No data loss of existing rows:** the slice adds no column to any existing table. **The event rows it creates are history; dropping the table discards that history — record the count before dropping.**

## What remains safe if removed

- A closed bill's tender method can be rewritten silently again — **which is the defect.** Do not describe the removal as neutral.
- The owner's cash reconciliation can be moved by one column write, with no record — **which is the defect.**

## Adjacent work (recorded, NOT picked)

- **The bill's four money columns being rewritten after the close** — **feature 532**, filed 2026-11-26. **Same table, adjacent columns, and the sibling that explicitly disclaimed this one.**
- **The tip's formula version being rewritten after the tip is computed** — **feature 535**, filed in this same pass. **Same family, different table.**
- **A shift's opening float being rewritten after the shift opens** — **feature 536**, filed in this same pass. **Same family, different table.**
- **An order line's quantity being rewritten after the line exists** — **feature 531**, filed 2026-11-26. **Same family, different table.**
- **A seated visit's party size being rewritten after the party is seated** — **feature 533**, filed 2026-11-26. **Same family, different table.**
- **The bill's `paid_at`** — recorded as *Open questions* 3 in the contract. **It is the payment *instant*; this slice owns the payment *kind*. Not bundled.**
