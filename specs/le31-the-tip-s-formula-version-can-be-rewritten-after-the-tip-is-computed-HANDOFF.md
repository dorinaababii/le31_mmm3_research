# le31-the-tip-s-formula-version-can-be-rewritten-after-the-tip-is-computed — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/535-le31-the-tip-s-formula-version-can-be-rewritten-after-the-tip-is-computed-and-nothing-records-it-first-party-v1-derived-tip-version-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `535`
- Slug: `le31-the-tip-s-formula-version-can-be-rewritten-after-the-tip-is-computed`
- Contract file: `features/535-le31-the-tip-s-formula-version-can-be-rewritten-after-the-tip-is-computed-and-nothing-records-it-first-party-v1-derived-tip-version-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is one of three filed in the same pass, and they form a family.** All three are the same shape: **a fact on a mutable table that the corpus's own contracts disclaim, and that no feature guards.**

| slice | the fact | the table | the corpus's own words that disclaim it |
|---|---|---|---|
| **534** | the bill's **tender method** | `bill` | 532: *"**`bill` is otherwise untouched** — `visit_id`, **`payment_method`**, `paid_at`, `closed_by` … are all unchanged"* · 420: *"**Any change to `Bill.payment_method`**"* |
| **535** (this one) | the tip's **formula version** | `derived_tip` | 532: *"This slice changes no formula and no **`formula_version`**"* · 457's Open question 4: *"a version string with no referent is exactly feature 448's shape"* |
| **536** | the shift's **opening float** | `shift` | 426's Open question 1: *"**`opening_float` is set when the shift opens and is not re-settable**"* · 391: *"**UNCHANGED by this feature**"* |

**They are pairwise disjoint**: 534 owns `bill.payment_method`, **535 owns `derived_tip.formula_version`**, 536 owns `shift.opening_float`. **No two touch the same column. No two touch the same table.** All three add their own append-only event table to `backend/app/models.py` and their own helper. **They may land in one PR or in three — but they must not be merged into one feature, and they must not be widened to cover each other's columns.**

**⚠️ The one thing that can go wrong here is DUPLICATING THE CONSTANT.** Feature **457**'s Open question 4 records the default this slice implements: *"the implementer must define it in code as the single named constant the derivation uses, and the stored value is that constant's value."* **There must be exactly ONE `DERIVED_TIP_FORMULA_VERSION` in the codebase.** If 457 has landed, use its constant and do not define a second one. **If 457 has not landed, this slice defines it — and 457 must read it when it lands.**

**⚠️ The second thing that can go wrong here is WIDENING 535 INTO 457.** Feature 457 owns the tip's **formula** and the **amount's** enforcement. **This slice owns the version string's *history* and its *referent*.** If you find yourself computing a tip, enforcing the tip's value, or changing the tip's amount — **stop. That is 457's, and it is filed.**

**The single sentence this feature exists to make true:** *a tip records the rule that produced it once, that rule has a name in the code, and that name is a fact with a history.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with a 4-seat `Table`, one `AppUser`, one `Visit`, one `OrderItem`, one `Bill` and one `DerivedTip` with `amount=0.50, formula_version='v1'`. `UPDATE derived_tip SET formula_version = 'v0-legacy'` was **ACCEPTED**, and `UPDATE derived_tip SET amount = -99.00` was **ACCEPTED** in the same probe. The full schema census confirmed **10 tables, zero `CHECK` constraints, exactly one `UNIQUE` constraint (`bill.visit_id`)**.

The probe is re-runnable: `/opt/data/le31-daily-2026-11-27-scripts/probe_first_party.py` (probe E).

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path computes a tip today (there is no bills router), so the defect is **latent**, not corrupting data. **This slice is cheapest now, before there is a single tip row to protect.**

**The finding shapes present:** omission (no write-once rule where one is needed) and the **seventh shape** (a covered concept — *the tip is protected*, owned twice (05, 457) — with an uncovered instance — *the tip's provenance is protected*, owned zero times).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily-research job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

- `backend/app/models.py` — **one new append-only table**, `DerivedTipVersionChange` (bill id, `field`, `old_value`, `new_value`, `by_user_id`, `at`). **No column is added to `derived_tip`, and `derived_tip`'s primary key is NOT changed.** Nothing else in the file changes.
- `backend/app/services/derived_tip_service.py` (NEW) — **the named constant** `DERIVED_TIP_FORMULA_VERSION`, the derivation helper that writes it, and the version-change guard: it either refuses, or writes the event and the change in one transaction. **It does not compute a tip differently from feature 457's rule and must not duplicate that formula.**
- `backend/tests/test_derived_tip_version_change.py` (NEW) — the regression test.

**Do NOT touch:** `DerivedTip`'s columns, `Bill`, `Visit`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `Shift`, any router, `index.html`, `PROJECT_CHARTER.md`.

**Do NOT add:** a `superseded_at` column or a supersession marker on `derived_tip` (**feature 457's *Adjacent evidence* records that a correction path would *"change `DerivedTip`'s primary key"* — that is a v2 shape, not this slice's**), a `CHECK` constraint on `formula_version` (it cannot express a history rule, and **feature 404** owns the constraint family), a second `DERIVED_TIP_FORMULA_VERSION` constant, a tip-amount correction path (**457's open tension**), a `Payment` table (**feature 391**), an `alembic` dependency or a `migrations/` directory (**§3.2**).

## Endpoints and contracts added

**None.** This slice adds no route. **No route computes a tip today** — feature **415** owns the close route. **This slice adds the constant, the helper and the guard; the close route, when it lands, must call the helper.** **Record that in the PR description.**

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the contract file matches the frozen identifiers above; confirm the statuses of features **05**, **404**, **415**, **420**, **432**, **435**, **448**, **450**, **457** and **532**.
2. **The write-path guard is the acceptance criterion.** Build LE31's schema with `SQLModel.metadata.create_all` against a throwaway SQLite file and assert:

   | scenario | expected |
   |---|---|
   | the tip's **computation write** creates the row with `formula_version = DERIVED_TIP_FORMULA_VERSION` | **ACCEPTED** (the guard must not block the legitimate write) |
   | change `formula_version` on an existing tip row, **no** event | **REFUSED**, stored value unchanged |
   | change `formula_version` **with** an event in the same transaction | **ACCEPTED**, event carries old value, new value, actor, time |
   | update or delete an event row | **REFUSED** |
   | a **caller-supplied** `formula_version` at the derivation | **REFUSED** — the code's constant is the only accepted source |
   | the stored `formula_version` and `DERIVED_TIP_FORMULA_VERSION` | **must agree** — the two-numbers check |

   **The probe that produced today's numbers is `probe_first_party.py` in the research-side scripts directory; run it against the pre-change schema FIRST to watch it fail.** Its output: *"UPDATE derived_tip SET amount = -99.00 -> ACCEPTED"* and *"UPDATE derived_tip SET formula_version = 'v0-legacy' -> ACCEPTED"*.
3. **The two-numbers check** — after any accepted change, the tip row's `formula_version` and the event history's latest `new_value` must agree; and the stored value must equal `DERIVED_TIP_FORMULA_VERSION` unless a recorded event says otherwise.
4. **The bump test** — this is the test that makes the column a *referent* rather than a caption: **change the constant to `"v2"` in the code** and confirm that (a) a newly computed tip stores `"v2"`, (b) an existing tip row still stores `"v1"`, and (c) **the stored value and the constant now disagree — and the disagreement is explained by a recorded event, or the row is flagged.** **A tip that silently changes its meaning when the constant is bumped is the failure this slice exists to prevent.**
5. **The negative control** — remove the guard and confirm the regression test **fails**. **A test that passes without the guard proves nothing.** This is the single most important check in this slice.
6. **Regression** — features **05** (the tip rule), **457** (the formula and the amount's enforcement), **532** (the money columns), **420** (what `total_paid` means), **404** (the number's shape), **448** (the bill's identity), **435** (the `Bill → order_item` edge), **450** (refunds) and **14** (split bills) must all be unaffected. **⚠️ 457's amount-enforcement and this slice's version-guard must coexist: 457 says the tip must equal the derivation; this slice says the name of the derivation must not change afterwards.**
7. **End-to-end** — through the API's terms: compute a tip, attempt to change its `formula_version` without an event and confirm the refusal; then change it *with* an event and confirm the event's old value, new value, actor and time.

## Rollback / feature-removal path

- Remove the event model from `backend/app/models.py`.
- Remove `backend/app/services/derived_tip_service.py`.
- Remove `backend/tests/test_derived_tip_version_change.py`.
- **⚠️ If feature 457 has landed, do NOT remove the constant** — 457's derivation depends on it. **Remove only the guard and the event table, and leave `DERIVED_TIP_FORMULA_VERSION` in place.**
- **⚠️ Rolling back requires the same migration work as applying it** — dropping a table cannot be done by `create_all()` either. **Record the prod-migration step in the PR description.**
- **No data loss of existing rows:** the slice adds no column to any existing table and does not change `derived_tip`'s primary key. **The event rows it creates are history; dropping the table discards that history — record the count before dropping.**

## What remains safe if removed

- The tip's provenance can be rewritten silently again — **which is the defect.** Do not describe the removal as neutral.
- A tip row's claim about which rule produced it becomes a caption rather than a fact — **which is the defect.**

## Adjacent work (recorded, NOT picked)

- **The bill's four money columns being rewritten after the close** — **feature 532**, filed 2026-11-26. **Same family, adjacent table, and the sibling that explicitly disclaimed `formula_version` twice.**
- **A closed bill's tender method being rewritten after the close** — **feature 534**, filed in this same pass. **Same family, different table.**
- **A shift's opening float being rewritten after the shift opens** — **feature 536**, filed in this same pass. **Same family, different table.**
- **The tip's amount and the formula itself** — **feature 457**, filed. **Read, not changed.**
- **The bill's human-facing identity** — **feature 448**, filed. **Read, not changed.** 457 named 448's shape as the thing to avoid reproducing; this slice is that shape, on the other half of the row.
- **A correction path for the tip's amount** — **feature 457's *Adjacent evidence*** records it as *"a v2 shape that would change `DerivedTip`'s primary key"*. **Recorded, not resolved here.**
