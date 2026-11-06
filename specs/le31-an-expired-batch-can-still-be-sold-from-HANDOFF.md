# HANDOFF — le31-an-expired-batch-can-still-be-sold-from

> **Slice contract for the coding agent.** Produced by the 99th LE31 daily-brainstorm pass (2026-11-06), Pick A.
>
> **Feature file**: `features/447-le31-an-expired-batch-can-still-be-sold-from.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite DB, then a `Batch` with `expires_at = 2026-11-01` (four days in the past) and a `StockEntry(batch_id=<it>, qty_delta=-1, reason='sale')` — **ACCEPTED**; and an `OrderItem` plus a second linked `StockEntry` against the same expired batch — **ACCEPTED**. Evaluating feature 404's predicate in SQL returned the expired batch as **NOT active**, while the sale against it was still accepted: **expired batches = 1 ; sales accepted against an expired batch = 2**). All seven checks pass; check 1's **demand** is classed INFERRED, which is why this contract is deliberately **one helper, one call site, one error type** and adds no surface. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-brainstorm-2026-11-06.md`.
>
> **Report**: `/opt/data/le31-brainstorm-2026-11-06.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/447-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/404-le31-active-batch-rule-excludes-null-expiry` FIRST** and confirm the ordering described under *Frozen contract* below. **This slice CONSUMES 404's predicate and must not redefine it. 404 is a HARD dependency.**
6. **Read `features/421-le31-stockentry-append-only-linter-rule` and confirm the ordering described under *Frozen contract*.** **421 is about to build the one and only write path every future ledger row will pass, and it explicitly places business rules out of scope — so this rule MUST land first, or in the same PR.**
7. **Create `backend/app/services/stock_service.py`** (if feature 374 has not created it yet) with `is_sellable`, `assert_sellable` and `BatchExpiredError`, exactly as specified in the feature file's *Data model*.
8. **Call `assert_sellable(batch)` at the one place a batch is consumed** — the `StockEntry` sale write.
9. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_sale_from_expired_batch_is_refused`.
10. **Record the refusal vocabulary** — one line in `features/404-…` saying that the *refusal at the write path* is feature 447's.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Change the active-batch predicate.** Feature **404** owns `expires_at IS NULL OR expires_at > now()`. **Do not write a third variant of the rule** and do not "fix" the NULL case — a null-expiry batch **is sellable**.
- **Choose which batch a sale consumes.** Feature **385** owns the batch-selection question and the order-line→batch provenance pointer. **On an expired batch, refuse — do not substitute another batch.**
- **Change the `StockEntry` write path's other rules.** Feature **421** owns the append-only linter rule; feature **441** owns the rule that the batch pointer and the order-line pointer must name the same dish; feature **417** owns the actor FK; feature **426** owns the `ref_order_item_id` FK. **Add one precondition; do not modify theirs.**
- **Refuse writes for `reason` other than `'sale'`.** A `waste` row against an expired batch is **correct** and must be accepted. This is the row that will be got wrong.
- **Auto-mark the batch `sold_out`.** Feature **397** owns the `sold_out` state. **Expired is not sold-out.**
- **Implement FEFO / first-expired-first-out ordering.** Features **153** and **372** own FEFO as a deferred v2 surface.
- **Make `Batch.expires_at` required, or decide what an expiry MEANS.** Feature **404** owns the NULL semantics; feature **03** owns who writes `expires_at`; feature **405** owns the service-day boundary.
- **Add a router, an endpoint, or a Telegram command.** The slice ships the rule and the error type. **Surfaces are a later feature.**
- **Add a table, a column, or any schema change at all.** This slice adds **no** column and **no** table.
- **Introduce Alembic, write a migration, add an `alembic` dependency, an `alembic.ini`, or a `migrations/` directory**, or change `PROJECT_CHARTER.md`.
- **Add a new pip dependency.**

**Disambiguation**: this slice is about **refusing to sell from an expired batch**. It is **not** about the active-batch predicate (404), the batch-selection rule (385), the remaining quantity (374), FEFO (153/372), the `sold_out` state (397), the service day (405), the ledger's actor FK (417), the ledger's linter rule (421), the ledger's back-pointer FK (426), or the pointer-coherence rule (441).

## Frozen contract

**The one thing this contract exists to make true:** *a sale may not consume a batch that has already expired.*

Concretely, after this slice lands:

1. There is **exactly one** helper — `is_sellable(batch, now=None) -> bool` — and one raiser — `assert_sellable(batch, now=None)`.
2. The helper's predicate is **exactly** feature 404's: `expires_at IS NULL OR expires_at > now()`.
3. **A batch with `expires_at IS NULL` IS sellable.** It has not expired.
4. A batch with `expires_at` **strictly in the past** is **not** sellable, and `assert_sellable` raises `BatchExpiredError`.
5. `BatchExpiredError` carries **both** `batch_id` and `expires_at`.
6. The refusal applies **only to `reason='sale'`**. `waste`, `restock` and `initial` writes against an expired batch are **ACCEPTED**.
7. The comparison at `expires_at == now` is **strict**: `>` not `>=`. A batch expires **at** its expiry instant.
8. The `now` used is read **once** and passed down, so a write cannot straddle a boundary and disagree with itself.
9. **A refused write leaves the ledger unchanged** — no partial row, no `StockEntry` written.
10. **The batch is NOT marked `sold_out`** and **NOT mutated** by the refusal.
11. **No schema change** — no column, no table, no constraint.
12. **No new batch is selected** on refusal. The refusal is a refusal.

**The prohibition:** *catching `BatchExpiredError` and falling back to another batch.* That would silently implement feature 385's question inside a slice that was told not to decide it — and it would produce a sale from a batch nobody chose.

### The 404 ordering — resolve before writing code

Feature **404** owns the rule *"a batch with `expires_at IS NULL` is active"*. This slice consumes it.

**404 must land first, or in the same PR.** If 404 has not landed, the helper may still be written — but it **must** be written against 404's predicate, and the PR must state that it depends on 404. **Do not implement 404's NULL decision here** (do not make a null-expiry batch unsellable — that is the opposite of 404's recorded default and a worse failure than today's).

### The 421 ordering — resolve before writing code

Feature **421** owns the `StockEntry` write path and **explicitly places the business rules out of scope**. It is about to build the one and only path every future ledger row will pass.

**This rule must land first, or in the same PR as 421.** If 421 lands first without it, 421 will implement the gap **faithfully** — the path will take the batch id from the request and never ask the expiry question. **That is the upstream-of-filed-work condition, and it is why the ordering is stated here rather than left implicit.**

### The strict-vs-fresh refusal — an owner decision, recorded not guessed

Whether an expiry is a **hard safety deadline** (refuse) or a **freshness estimate** (warn) is an owner decision. **This contract implements the strict reading** — because it is the only reading under which the stored `expires_at` means anything at all — and **records the question rather than hiding it**.

**The agent may implement the strict refusal.** The agent may **not** implement a warn-only mode, a manager override path, or a substitute-batch fallback. **If the owner decides otherwise, that is a new feature, not a change to this one.**

## Files to touch

**Create:**

- `backend/app/services/stock_service.py` — **only if feature 374 has not already created it.** Contains `is_sellable`, `assert_sellable`, `BatchExpiredError`. **If 374's module exists, add to it and do not create a second module.**
- `backend/tests/test_batch_expiry_refusal.py` — the scenario table from the feature file, as eight tests.

**Modify:**

- `backend/app/services/stock_service.py` (or whichever module ends up owning the `StockEntry` sale write) — **one call site.** Add `assert_sellable(batch)` immediately before the `StockEntry` row is written, **for `reason='sale'` only**.
- `features/404-le31-active-batch-rule-excludes-null-expiry-…md` — **one line only**, recording that the *write-path refusal* is feature 447's. **Do not change 404's rule.**

**Read but do not modify:**

- `features/404-le31-active-batch-rule-excludes-null-expiry-…md` — the predicate this slice consumes.
- `features/421-le31-stockentry-append-only-linter-rule-…md` — the write path this slice adds a precondition to.
- `features/441-le31-stockentry-may-name-a-batch-and-an-order-line-for-different-dishes.md` — the coherence rule at the same call site.
- `features/385-le31-order-item-batch-provenance-…md` — the batch-selection question.
- `features/397-le31-sold-out-state-…md` — the `sold_out` state this slice does **not** write.
- `features/374-le31-qty-remaining-derived-not-stored-…md` — the module this slice may share.
- `features/446-le31-has-no-schema-evolution-mechanism.md` — **this slice adds no column, so it is not blocked by 446**; but note the first `create_all()` that runs with a new module present.
- `PROJECT_CHARTER.md` — §3.2 (out of scope for v1), §3.5 (time is UTC), §4.3 (the append-only ledger pattern), §7 (the quality bar).

## Mandatory LE31 skill list

The agent **must** load, in order:

1. `le31-conventions` — §3.2, §4.1, §7, the truth invariant, the seven-check feature gate.
2. `le31-v1-feature-pattern` — the contract shape and the *Definition of Done*.
3. `le31-feature-pipeline` — where the artefacts must land.
4. `le31-handoff-spec` — this file's obligations.
5. `le31-backend` — the service-layer conventions.

**Also read** `PROJECT_CHARTER.md` — §3.2 (out of scope for v1), §3.5 (time is UTC), §4.3 (the append-only ledger pattern), and §7 (the quality bar).

## Mandatory inputs

- The active feature file: `features/447-le31-an-expired-batch-can-still-be-sold-from.md`
- This handoff: `specs/le31-an-expired-batch-can-still-be-sold-from-HANDOFF.md`
- Feature 404's predicate (the exact SQL and the exact Python)
- Feature 421's write-path description
- The charter's §4.3 ledger rules

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases (from the feature file's scenario table)

| # | Batch | Action | Expected |
|---|---|---|---|
| 1 | `expires_at` in the past | sale consumes it | **REFUSED** — `BatchExpiredError` |
| 2 | `expires_at` in the future | sale consumes it | **ACCEPTED** |
| 3 | `expires_at IS NULL` | sale consumes it | **ACCEPTED** (404's default) |
| 4 | `expires_at` in the past | `reason='waste'` | **ACCEPTED** |
| 5 | `expires_at` in the past | `reason='restock'` | **ACCEPTED** |
| 6 | `expires_at` in the past | `reason='initial'` | **ACCEPTED** |
| 7 | `expires_at` exactly == now | sale consumes it | **REFUSED** — `>` is strict |
| 8 | expired batch, sale refused | ledger rows for that batch | **UNCHANGED** — no half-write |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Build a batch with `expires_at` in the past.
2. Attempt a sale that consumes it. **Observe the refusal** — the error, not a silent success.
3. Observe that the ledger for that batch is **unchanged**.
4. Attempt the same sale against a null-expiry batch. **Observe acceptance.**
5. Attempt a `waste` write against the expired batch. **Observe acceptance.**
6. Show the helper's predicate **is** feature 404's, by evaluating both against the same three batches.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (on the unfixed code there is no refusal at all — the sale is simply accepted), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

Use the **existing verification venv** rather than provisioning a new one: `/opt/data/le31-verify-2026-10-27/.venv` (`sqlmodel` 0.0.48, `sqlalchemy` 2.1.6). `python3` on the host has **no `pip` module** (PEP 668); do not try to install into the system interpreter.

## Rollback path

**Fully reversible in one step.** The slice adds **no schema change** — no column, no table, no constraint.

- Remove the `assert_sellable(batch)` call site → the refusal stops applying.
- Delete `is_sellable`, `assert_sellable` and `BatchExpiredError` → the module is back to its previous contents.

**No data is at risk**: no `StockEntry` write path exists outside `models.py`, no batch has ever been created, and no ledger row exists to be rewritten. **The ledger is append-only by charter, and this slice never writes to it except to refuse a write.**

## Sign-off gap

**What the agent MUST NOT decide:**

- whether an expiry is a hard deadline or a freshness estimate (a strict refusal is implemented; the warn mode is **not**);
- whether a manager may override an expiry;
- whether an expired batch should fall back to another batch (**it must not**);
- whether expiry should mark the batch `sold_out` (**it must not**);
- what the service-day boundary is (feature 405's);
- who sets `expires_at` (feature 03's);
- the FEFO ordering (features 153/372's).

**What the agent must report back:**

- the eight scenario results, **one row each, with the observed outcome**;
- the **failing-then-passing** proof for `test_sale_from_expired_batch_is_refused`;
- the exact call site the refusal was added to, and **why that point and not the `OrderItem` write**;
- confirmation that the predicate is **byte-identical** to feature 404's, with both quoted;
- confirmation that **no schema change** was made (a `git diff` on `models.py` must be empty);
- confirmation that features **404** and **421** were read and that the ordering is satisfied or explicitly flagged as pending.

## Handoff summary

**One sentence:** *Make an expired batch unsellable — one helper, one call site, one error type, no schema change, and it must land before the selling path that would otherwise write the wrong row forever.*

**Three picks of the 99th daily-brainstorm pass (2026-11-06):**

| | Pick | Feature | Gate | Evidence |
|---|---|---|---|---|
| A | an expired batch can still be sold from | `features/447-le31-an-expired-batch-can-still-be-sold-from.md` | **build** | OBSERVED (executed) |
| B | a bill has no human-facing identity | `features/448-le31-a-bill-has-no-human-facing-identity.md` | **build** | OBSERVED (executed) |
| C | an order line may carry any price it likes | `features/449-le31-an-order-line-may-carry-any-price-it-likes.md` | **build** | OBSERVED (executed) |

**Feature**: `features/447-le31-an-expired-batch-can-still-be-sold-from.md`
**Report**: `/opt/data/le31-brainstorm-2026-11-06.md`
**Bucket**: v1 · **Gate**: build · **Evidence**: OBSERVED (executed) · **Confidence**: high (gap) / medium (demand)
