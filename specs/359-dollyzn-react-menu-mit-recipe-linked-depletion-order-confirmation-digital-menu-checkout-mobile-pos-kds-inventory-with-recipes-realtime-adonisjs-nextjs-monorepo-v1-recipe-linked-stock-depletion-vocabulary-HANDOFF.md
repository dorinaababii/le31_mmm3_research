# HANDOFF — Feature 359 · Recipe-linked depletion (experiment, v1)

**Date:** 2026-10-22 · **Feature:** `features/359-dollyzn-react-menu-...-v1-recipe-linked-stock-depletion-vocabulary.md`
**Source:** [`dollyzn/react-menu`](https://github.com/dollyzn/react-menu) — MIT ✓ §3.2 · ★0/⑂0 · TypeScript off-stack · created 2026-10-21, pushed 2026-10-22
**Linear:** not attached — write endpoint blocked (34th day), `requestId a4e6a0548d28d2de`

## Why this slice is next

It is the only pick today that makes an **existing** LE31 ledger correct-by-construction instead of adding a surface. The falsification test is built into the slice, so it is cheap to run and cheap to abandon.

## Upstream references

| Ref | Detail |
|---|---|
| Repo | https://github.com/dollyzn/react-menu |
| Licence | MIT (verified via `GET /repos/dollyzn/react-menu`, 2026-10-22) |
| Description | *"Open-source digital menu and ordering system for restaurants: customer menu with Pix/card checkout, mobile POS, kitchen display (KDS), inventory with recipes and realtime orders. AdonisJS + Next.js monorepo."* |
| Topics | 17, incl. `inventory-management`, `point-of-sale`, `kitchen-display-system`, `pix`, `redis`, `postgresql` |
| In-window | **both** `created_at` (2026-10-21) and `pushed_at` (2026-10-22) |
| Sibling, richer but blocked | [`hamidkhan069731-blip/restaurant-erp-system`](https://github.com/hamidkhan069731-blip/restaurant-erp-system) — recipe-level costing + three-way procurement + shift reconciliation, created 2026-10-17, **licence `null` → §3.2 blocked, vocabulary-only, not adopted** |

**Adoption posture: vocabulary only.** The AdonisJS/Next.js codebase is off-stack and is not adopted. The transferable item is the event ordering — *confirm order → decrement components → emit update, in one transaction*.

## Slice

1. `RecipeComponent(id, menu_item_id, ingredient_id, qty_per_unit)` + migration. Seed **one** prep station.
2. `Depletion(id, order_line_id, component_id, qty, created_at, trigger)` — append-only (§3.3).
3. Order-confirmation hook: resolve recipe, write `Depletion` rows in the same transaction.
4. Void → **reversing** `Depletion`, never a delete.
5. Derived reorder signal on the owner view.
6. **14-day reconciliation:** derived depletion vs. owner's manual count.

## Acceptance

- An order for an item with a recipe decrements components within the confirm transaction.
- An order for an item **without** a recipe still succeeds (missing recipe must never block a sale).
- Voiding a line leaves both the original and the reversing `Depletion`; history is never rewritten.
- The 14-day report shows derived vs. manual per item, with the coverage gap (items lacking recipes) stated explicitly rather than hidden.

## Risks

| Risk | Severity | Mitigation |
|---|---|---|
| ★0 traction, 1-day-old repo — the pattern is unproven anywhere | **high** | The 14-day reconciliation is the test. No destructive migration; a new table and a report are all that ship. |
| Owner disagrees with recipe-derived counts | high | This is the measurement, not a failure — divergence is the finding. |
| Unclear whether cook or owner owns the recipe | medium | Open question 2. Seed with the owner's recipes first; do not block. |
| Unit normalisation across recipes | medium | Open question 3. One station only until a units table exists. |
| Void rate makes `Depletion` noisy | low | Reversing records keep the ledger true regardless; noise is a UI concern. |

## Reversibility

**Fully reversible.** One additive migration, two append-only tables, one derived report. Undo = drop the table. No existing entity is altered. Stock level is *derived* by folding, so there is no stored counter to corrupt.

## Rollback trigger

Run the 14-day reconciliation. If drift exceeds ~1–2 portions per tracked item consistently, **stop and record why** — the floor does not want recipe-derived depletion. Do not quietly keep iterating.