# le31-the-bill-s-money-columns-can-be-rewritten-after-the-bill-is-closed-and-paid — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/532-le31-the-bill-s-money-columns-can-be-rewritten-after-the-bill-is-closed-and-paid-first-party-the-tip-never-moves-v1-bill-money-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `532`
- Slug: `le31-the-bill-s-money-columns-can-be-rewritten-after-the-bill-is-closed-and-paid`
- Contract file: `features/532-le31-the-bill-s-money-columns-can-be-rewritten-after-the-bill-is-closed-and-paid-first-party-the-tip-never-moves-v1-bill-money-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is the one thing feature 450 pointed at and deliberately left alone.** Feature 450's own prose is the single corpus mention of the defect:

> **Feature 450**: *"the ledger is append-only and audited; the money side is not. LE31's own `StockEntry` docstring says 'Never UPDATE or DELETE rows'; `Bill.total_paid` says nothing and means the opposite: **a single mutable number that can be set to anything**, including a negative one."*

And then, in 450's *Goal*: *"**`Bill.total_paid` stays exactly as it is** — but it becomes the sum of payment rows."*

**450 fixed the *refund* problem. It did not, and by its own words did not, own the *mutability*.** A corpus-wide sweep over all 564 feature contracts and 517 HANDOFFs finds **exactly one** mention of the bill's money columns being mutable or traced — **that sentence.** This slice is the contract that sentence asked for.

**Five things must not be confused with it, and the corpus says so itself:**

| rule | mechanism | owner |
|---|---|---|
| the **tip formula** and its enforcement | formula + `formula_version` | **features 05, 457** — filed |
| the **bill-close route** and the `subtotal_items` derivation | router + `Decimal` sum | **feature 415** — filed |
| the **`Bill → order_item` edge** | the membership relation | **feature 435** — filed |
| the **`total_paid` meaning** (tendered vs received) | a definition | **feature 420** — filed |
| the **refund** and the payment row | payment rows + a cap | **feature 450** — filed |
| **the bill's money being written once** | **event table + write-path guard** | **THIS SLICE** |

**⚠️ The one thing that can go wrong here is BLOCKING FEATURE 450.** 450 makes `total_paid` a sum over payment rows so a refund can be capped against a payment. **This slice's guard must be written so that 450's rows are the mechanism for a legitimate post-close money movement, not a violation of it.** **A refund is not an overwrite.** See *Open questions* 4 in the contract — **this is the single most important question in the slice.**

**The single sentence this feature exists to make true:** *a closed bill's money is written once; a later change to it is a recorded event, never a silent overwrite.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one `MenuItem`, one `Batch`, one `Visit`, one `OrderItem` and one `Bill`. `UPDATE bill SET subtotal_items=0.01, total_due=0.01` was **ACCEPTED** against a visit whose lines total **€13.00**; `UPDATE bill SET total_paid=100.00` was **ACCEPTED** after payment. The probe compared **two numbers that should agree** and found them diverging: the stored `derived_tip.amount` = **€0.00** against the tip the bill's own `total_paid` implies = **€85.70**. **Both rows are on the same bill, and nothing raised an error.**

The probe is re-runnable: `/opt/data/le31-brainstorm-2026-11-26-scripts/probe_round2.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no bills router exists today, so the defect is **latent**, not corrupting data.

**The finding shapes present:** omission (no write-once rule where one is needed), the **sixth shape** (a formula whose *input's* semantics are undefined — the tip is derived from four columns, none of which may not change afterwards), the **seventh shape** (a covered concept — the bill's money as a fact — with an uncovered instance — its mutability), and the **eighth shape** (a duplicated derivation across two moments: the tip was computed once and the inputs moved afterwards).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

- `backend/app/models.py` — **one new append-only table**, the bill-money correction event (bill id, field name, old value, new value, `by_user_id`, `at`). **No column is added to `bill`.** Nothing else in the file changes.
- `backend/app/services/bills_service.py` (NEW) — the bill-money write helper: it either refuses, or it writes the event and the change in one transaction. **It does not invent a bills router** — feature **415** owns that, and the helper is the seam 415's route calls.
- `backend/tests/test_bill_money_change_event.py` (NEW) — the regression test.

**Do NOT touch:** `Bill`'s columns, `DerivedTip`, `Visit`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `Shift`, any router, `index.html`, `PROJECT_CHARTER.md`.

**Do NOT add:** a `previous_total_paid` column (it preserves one overwrite and loses the second — feature **523** states this rule), a refund mechanism (feature **450**), a payment table (feature **450**), a `CHECK` on the money columns' shape (feature **404**), a currency column (feature **409**), a tax rate (feature **408**), a split-bill model (feature **14**), a bill number (feature **448**).

## Endpoints and contracts added

**None.** This slice adds no route. Today there is no bills router — **the helper is the contract**, and feature **415** will call it. This is the same discipline feature **430** used for its `added_at` helper and feature **415** used for its close write.

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface. **A manager approval workflow is a real requirement and is deliberately NOT designed here** — see *Open questions* 3.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the contract file matches the frozen identifiers above; **confirm the statuses of features 415, 435, 450 and 457** — 415 and 450 are the two that constrain this slice.
2. **The write-path guard is the acceptance criterion** — a schema constraint cannot carry this rule (the database has no notion of a row's history). Build LE31's schema with `SQLModel.metadata.create_all` against a throwaway SQLite file and assert:

   | scenario | expected |
   |---|---|
   | the **close write** sets the four money columns on a new bill | **ACCEPTED** (the guard must not block the legitimate write) |
   | change `total_paid` on a **closed** bill, **no** event | **REFUSED**, stored value unchanged |
   | change `total_paid` on a closed bill **with** an event in the same transaction | **ACCEPTED**, event carries field, old value, new value, actor, time |
   | change `total_paid` on an **open** bill | **ACCEPTED**, no event needed |
   | update or delete an event row | **REFUSED** |

   **The probe that produced today's numbers is `probe_round2.py` in the research-side scripts directory; run it against the pre-change schema FIRST to watch it fail.** Its output: *"UPDATE bill SET total_paid=100.00 -> ACCEPTED"* and *"derived_tip.amount (stored) = 0.00"* against *"recomputed tip = 85.70"*.
3. **The two-numbers check** — after any accepted change, the tip implied by the bill's money and the `DerivedTip` row stored against it **must agree** — or the difference must be exactly accounted for by a recorded event. **A single number never shows a divergence.**
4. **The negative control** — remove the guard and confirm the regression test **fails**. **A test that passes without the guard proves nothing.** This is the single most important check in this slice.
5. **Regression** — features **415** (the close write), **435** (the edge), **450** (refunds and payments), **457** (the tip's formula), **448** (the bill's number), **420** (`total_paid`'s meaning), **404** (money column shape), **411** (the `Decimal` guarantee), **408** (the tax rate), **14** (split bills), **391** (`Shift` and the `Shift ↔ Bill` edge) must all be unaffected. **⚠️ Feature 450 is the one that must not be broken by this slice** — if 450 has landed, the guard must permit 450's payment rows.
6. **End-to-end** — through the API's terms: close a bill, then attempt to change `total_paid` without an event and confirm the refusal; then change it *with* an event and confirm the event's old value, new value, actor and time.

## Rollback / feature-removal path

- Remove the event model from `backend/app/models.py`.
- Remove `backend/app/services/bills_service.py`.
- Remove `backend/tests/test_bill_money_change_event.py`.
- **⚠️ Rolling back requires the same migration work as applying it** — dropping a table cannot be done by `create_all()` either. **Record the prod-migration step in the PR description.**
- **No data loss of existing rows:** the slice adds no column to any existing table. **The event rows it creates are history; dropping the table discards that history — record the count before dropping.**

## What remains safe if removed

- A closed, paid bill's money can be replaced silently again — **which is the defect.** Do not describe the removal as neutral.
- The recorded tip and the bill's own money can contradict each other with no record of why — **which is the defect.**

## Adjacent work (recorded, NOT picked)

- **The order line's quantity being rewritten after the line exists** — **feature 531**, filed in this same pass. **Same family, different table.** The two do not conflict: 531 does not touch `bill` and this slice does not touch `order_item`.
- **A seated visit's party composition being rewritten** — **feature 533**, filed in this same pass. **Same family, different table.**
- **The refund and the payment row** — **feature 450**, filed. **This slice must not block it.**
- **The tip's formula and `formula_version`** — **features 05, 457**, filed. **Unaffected; read, not changed.**
- **`Bill → order_item` and the derivation of `subtotal_items`** — **features 435, 415**, filed.
- **The manager-approval workflow for a money correction** — **feature 403**'s territory (manager PIN for voids, discounts and refunds). **Recorded, not picked.**
- **A question this slice deliberately does not answer** — does a refund count as a "change to a closed bill's money"? See *Open questions* 4 in the contract. **It is recorded, not decided — and it must be settled before 450 lands.**
