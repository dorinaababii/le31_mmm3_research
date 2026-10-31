# HANDOFF — 401-bzubairy-home-kitchen-pos

**Status**: defer (v1 vocabulary + one decision, no build today)
**Date**: 2026-10-29
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/401-bzubairy-home-kitchen-pos-mit-typescript-supabase-vercel-phone-first-small-food-business-orders-recipes-per-menu-item-stock-history-low-stock-counts-pending-orders-v1-pending-order-reservation-vocabulary.md`
**LE31 feature gate verdict**: **defer** — vocabulary-only; no code is adopted. The gap is OBSERVED (parent-verified against `backend/app/models.py`); the demand is not.

## Trigger policy

This is a **defer artifact** — a vocabulary record plus **one named decision**. It does **not** start a build.

It surfaces `bzubairy/home-kitchen-pos` (MIT, TypeScript + Supabase, in-window by both `created_at` and `pushed_at`) as the **third artifact in three consecutive daily-research passes** to name the same missing quantity, and records the decision it forces:

> **Is "committed" a stored number or a derivation?**

Under charter §3.3 the answer **must** be *a derivation* — and that is the point of the record, because **the artifact itself stores a balance**. LE31's rule and the artifact's implementation point in opposite directions; **only the rule transfers**.

**Trigger conditions** — if ANY of these is met, the external coding agent should:

1. Load this artifact, the linked feature file, and the raw README (`/tmp/le31-daily-2026-10-29/parent/bzubairy__home-kitchen-pos__README.md`).
2. Load the companion features **374** (`qty_remaining` stored-vs-derived — owns the stored-number decision), **382** (stock-deduction idempotency — owns the write path), **385** (batch provenance — owns the recipe→ingredient mapping) and **397** (menu availability — a *different* concept from *committed*).
3. Load **feature 400** (the same window's idempotency-key / reversal vocabulary) and **feature 402** (the same window's permission rule).
4. Decide, in writing: **when the ingredient deduction is written** (order entry / fire / prepare / serve) and **which `OrderItem.status` states count as committed**.
5. Implement the derivation in the **owning** feature — **374** for the stored-vs-derived question, **385** for the recipe mapping — **not** in a new feature.
6. If no decision can be made, close this artifact and leave the ledger as-is.

**If the trigger condition is NOT met, do nothing.** In particular: **do not** add a `reserved` column, **do not** add a `committed` column, and **do not** add a `StockReason.reserve` member — the whole point of the defer is that these are decisions, not defaults.

**Disambiguation**: this artifact is about the **pending-order reservation quantity** and its derivation. It is **not** about the idempotency key or the reversal event (**feature 400**) and **not** about permission enforcement (**feature 402**). Three separate artifacts, one window, three different concepts — do not merge them.

## Mandatory inputs

- **Active feature**: `features/401-bzubairy-home-kitchen-pos-…-v1-pending-order-reservation-vocabulary.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-10-29.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-29/`
  - `parent/bzubairy__home-kitchen-pos__repo.json` — direct `GET /repos/`
  - `parent/bzubairy__home-kitchen-pos__README.md` — README, 10,826 B
  - `parent/bzubairy__home-kitchen-pos__tree.json` — file tree, 123 files
- **LE31 source of truth**: `backend/app/models.py`
  - `Batch.qty_remaining: int` (line 106) — a single stored number
  - `StockEntry` (lines 113–126) — no reserved/committed concept; `at: datetime` is a wall-clock timestamp
  - `StockReason` (lines 54–60) — no `reserve`/`release` member
  - `MenuItem.is_prepared: bool = True` (line 92) — the prepared/unprepared split
  - `ItemStatus` (lines 35–40) — `new`, `preparing`, `ready`, `served`, `cancelled`
- **Charter §3.3** (append-only stock ledger; current stock is derived from entries) — `PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — the seven-check feature gate and the hard invariants (charter §3.3 append-only, §3.2 two fixed surfaces).
- `le31-v1-feature-pattern` — the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — the source-of-truth discipline on the artifact's README quotes.
- `le31-handoff-spec` — the frozen-contract discipline.

The agent must **NOT** load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The recorded derivation, stated so it can be implemented later without re-deriving it:

```
on_hand(batch)   = SUM(StockEntry.qty_delta WHERE batch_id = B)     -- per §3.3, derived
committed(batch) = Σ over open OrderItems of qty(recipe explosion)  -- derived, not stored
available(batch) = on_hand(batch) − committed(batch)                -- derived, not stored
```

The vocabulary:

- **Committed** — the quantity that open (not-yet-served, not-yet-cancelled) `OrderItem`s will consume, computed by exploding their recipes to ingredients. **A relation between an order and stock, not a quantity on a row.**
- **Available** — on-hand minus committed. **A derived quantity, never a column.**
- **Recipe explosion** — a menu-item sale becomes N ingredient-level `StockEntry` rows, one per ingredient, each sharing the same `ref_order_item_id`. **This is what makes the derivation computable at all.**

**Anti-goals, stated so they are not drifted into:**

- **No `reserved` column and no `committed` column.** Both would be stored balances, which **§3.3 forbids**.
- **No adoption of the artifact's storage model.** *"stock history for every ingredient"* alongside a current balance is a stored-balance model and **conflicts with §3.3**. The rule is more §3.3-compatible than the artifact's implementation — that asymmetry is the reason this is a vocabulary record.
- **No `StockReason.reserve`/`release` member without an explicit decision.** The release question belongs with the reversal question in **feature 400**.
- **No reservation model.** Not in scope, not adjacent, not a sub-question.

## Files to touch (when the defer is promoted to build)

**None today.** When promoted, the changes belong to the **owning** features:

- `backend/app/models.py` — **only** if the owner decides to remove `Batch.qty_remaining`; that decision belongs to **feature 374**, not here.
- The recipe→ingredient mapping and the explosion logic — belongs to features **03**, **15** and **385**.
- The derivation query (a view, or a service-layer function) — belongs to **feature 374**.
- A new alembic migration under `backend/migrations/versions/` **only** if a column is removed — **note the charter's known unresolved migration-strategy inconsistency; surface it, do not settle it by accident.**

## Verification protocol

When promoted, the external coding agent must verify:

1. **The frozen contract fields match the recorded derivation** — `on_hand`, `committed`, `available`, and the recipe explosion.
2. **"Committed" is computed, not stored.** Assert that no column in `backend/app/models.py` holds a reserved/committed quantity.
3. **The derivation is correct at the boundaries.** With N on hand and M committed: available = N − M; and when M > N (over-committed), the derivation **must not silently clamp** — it must surface the shortfall. **Over-commitment is a real case and is the reason the sign of a shortfall rule was left undecided on 2026-10-28.**
4. **Cancelling an open order releases its commitment**, and the release is recorded **as a new ledger entry**, not by editing the original.
5. **The end-to-end acceptance path is executable**: open two orders → the available figure drops by both → cancel one → the figure returns by exactly one → the ledger contains the compensating entry.
6. **The rollback path is present and reversible**: re-add the derived column or disable the derivation; the ledger rows remain valid, and any committed balance is **not** written back into the ledger.

## Rollback path

- Today: **nothing to roll back** — this defer writes **no** code, **no** schema, and **no** data.
- When promoted: revert the migration; remove the derivation from the read path. **Never** persist a derived value back into the ledger to make a rollback easier — that is the §3.3 violation this whole artifact exists to prevent.
- **Ledger rows are never edited or deleted to roll back** (charter §3.3). A mistaken write is compensated by a **new compensating `StockEntry`**.

## Sign-off gap

No build today. This defer artifact does **not** require owner sign-off; it surfaces a dated, in-window reference and one open decision.

**The open decisions DO require owner sign-off before implementation** — specifically:
1. **When the ingredient deduction is written** (order entry / fire / prepare / serve). This determines the meaning of "committed" and is the harder question.
2. **Which `OrderItem.status` states count as committed** — `new`/`preparing` vs. `new` only.

The external coding agent must mirror this contract back to the owner before implementing and **stop if it cannot**.
