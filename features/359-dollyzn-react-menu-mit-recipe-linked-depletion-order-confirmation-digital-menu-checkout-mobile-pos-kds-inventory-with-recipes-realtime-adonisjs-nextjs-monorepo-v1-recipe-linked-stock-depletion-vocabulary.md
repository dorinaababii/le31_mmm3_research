# Feature 359 — `dollyzn-react-menu-mit-recipe-linked-depletion-order-confirmation-digital-menu-checkout-mobile-pos-kds-inventory-with-recipes-realtime-adonisjs-nextjs-monorepo-v1-recipe-linked-stock-depletion-vocabulary` (experiment)

> **Pick A of Daily Brainstorm 2026-10-22 (pass 83).** Documents in-window GitHub repo `dollyzn/react-menu` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**), **★0/⑂0**, **TypeScript OFF-STACK** (AdonisJS + Next.js monorepo) but the *data-shape* is entirely portable to LE31's Python 3.13 / FastAPI / SQLModel / Postgres / aiogram v3 charter, **created 2026-10-21 — one day before this pass — and pushed 2026-10-22 (today)**, in-window by **both** `created_at` and `pushed_at`. 17 topics including `digital-menu + food-ordering + inventory-management + kitchen-display-system + point-of-sale + restaurant + pix + redis + postgresql`. Bucket: **v1**. Verdict: **`experiment`**.

## Goal

Make stock depletion a **consequence of the sale LE31 already records**, rather than a separate chore the owner performs. When a ticket line is confirmed, the line is simultaneously a quantity sold and a set of recipe components to decrement. The floor operator sees one fact — "we sold the last flat white" — not a sale plus an inventory task.

## Scope

**In scope:**

- A `RecipeComponent` entity: `(menu_item, ingredient, qty_per_unit)`.
- A `Depletion` record written when an order line is confirmed: the *immutable* record of which components were decremented, by how much, and why (the triggering line).
- Recipe resolution **at the point of sale**, inside the existing order-confirmation transaction.
- A floor-facing signal when a component crosses its reorder threshold — derived, not hand-entered.
- An `experiment` scope boundary: **one prep station, a handful of recipes, and a daily reconciliation check** that the derived depletion matches what the owner would have written by hand. If they diverge, the experiment has told us something worth knowing.

**Out of scope:**

- Purchase orders, supplier contracts, three-way match, or any procurement flow.
- Multi-branch or multi-tenant stock.
- Cost accounting, recipe *pricing*, or margin analysis.
- Wastage / void / comped-ticket handling beyond refusing to deplete on a voided line. (Named here because getting it wrong is the obvious failure mode, not because it is in scope.)

## Evidence / JTBD

**Gate check 1 (JTBD) passes.** The job: *when the owner sells the last of a prepped item mid-service, they want to know it without a separate inventory round, but currently must notice and record it by hand, so the stock ledger drifts from the truth by the end of service.* This is a real floor job that LE31's owner already does manually today, and LE31 already owns the append-only `StockEntry` ledger that would receive these writes.

- **Evidence class**: **observed intent**, not shipped behaviour. The repo was **created 2026-10-21**, one day before this pass, at ★0/⑂0. It advertises *"inventory with recipes"*; there is no evidence that recipe-linked depletion works, is deployed, or is used. **Traction is zero and is recorded as zero.** The transferable item is the *data shape*, not the code.
- **Confidence**: **medium** that the recipe-linked-inventory idea is the real differentiator in this repo (it is explicitly named in both the description and the topic list); **low** for implementation quality, which cannot be assessed on a 1-day-old ★0 repo.
- **Honest counter-consideration**: the same idea appears in `hamidkhan069731-blip/restaurant-erp-system` (created 2026-10-17) with a fuller shape — recipe-level inventory costing, three-way procurement match, shift reconciliation — but that repo's licence is **`null`, a §3.2 blocker, and is therefore vocabulary-only**. `dollyzn/react-menu` is the MIT-licensed carrier of the idea, which is why it is the pick and not the richer repo.

## Description

`dollyzn/react-menu` positions itself as a full restaurant ordering monorepo: customer menu with Pix/card checkout, mobile POS, kitchen display, realtime orders, and inventory. The AdonisJS backend and Next.js frontend are off-stack. What is *not* off-stack is the event ordering: **confirm order → decrement components → emit realtime update to KDS**, all inside one transaction boundary, with Redis for fan-out.

LE31 already has the two halves separately — a `StockEntry` append-only ledger, and a cook-side Telegram channel. What it does not have is the *link*: the sale is not currently an input to stock. Idea 359 is that link, and it is the smallest change that makes the existing ledger trustworthy without anyone remembering to write to it.

## Data model

New:

- `RecipeComponent(id, menu_item_id, ingredient_id, qty_per_unit)` — a menu item decomposes into N components.
- `Depletion(id, order_line_id, component_id, qty, created_at, trigger)` — **append-only**, written once, never updated (§3.3). `trigger` records the sale that caused it, so a depletion can always be traced back to a line.

Existing, unchanged: `MenuItem`, `StockEntry` (a depletion may also be recorded as a `StockEntry` for continuity with the existing ledger; the `trigger` field is what distinguishes the two).

The important property: **stock level is derived by folding `Depletion` records**, never stored as a mutable counter. A recipe correction therefore never silently rewrites history — it writes a reversing record.

## Implementation steps

1. Add `RecipeComponent` + migration. Seed 10–15 recipes for **one** prep station (the simplest station in a real kitchen, typically a prep/juice station where component counting is obvious).
2. Add `Depletion` as an append-only table with `order_line_id` FK.
3. Hook order-confirmation: resolve recipe, write `Depletion` rows in the same transaction.
4. Void handling: a voided line writes a reversing `Depletion`, never deletes.
5. Derived reorder signal on the existing owner view.
6. **Daily reconciliation report**: derived depletion vs. the owner's manual count, side by side, for 14 days.

## Telegram interaction

One notification, at threshold crossing only: *"Flat white: last 2 portions of the 20 remaining."* No AI, no LLM, no suggestion. Deterministic arithmetic on existing records — this is a §3.7-safe surface.

## Dependencies

- **`StockEntry` ledger** (exists).
- **Order line entity with a confirmed state** (exists in v1 core).
- **Blocker to acknowledge honestly**: if a menu item has no recipe, order confirmation must still succeed — a missing recipe is not a reason to block a sale. Recipes are opt-in per item, and the reconciliation report measures the coverage gap rather than pretending it does not exist.

## Open questions

1. **How much drift is acceptable?** The 14-day reconciliation has no pass threshold yet. If the owner's manual count diverges by more than a portion or two per item, the idea has told us the floor does not want it.
2. **Does the cook or the owner own the recipe?** Recipes are a prep-station artefact; LE31's two roles do not obviously split this. Genuinely unmade.
3. **Unit normalisation.** "2 portions" of an ingredient is not the same across recipes. Needs a units table before more than one station is onboarded.
4. **Void rate.** High void rates would make `Depletion` noise. Not measured.

## Why this matters

This is the first pick in several passes that touches the **correctness** of an existing LE31 ledger rather than adding a surface. Every prior append-only-ledger pick has been about auditability of *actions*. This one is about stock being *right by construction*. If the 14-day reconciliation shows drift below the threshold, LE31's stock number becomes trustworthy without a daily chore — which is the difference between a ledger the owner maintains and a ledger that maintains itself.

---

**Gate verdict: `experiment`.** Passes check 1 (JTBD is a real, currently-manual floor job), passes check 2 (MIT, §3.2 strictly-compatible), passes check 3 (buildable on the existing v1 stack). **The risk is not technical, it is evidentiary**: ★0 traction, 1 day old, no evidence the idea works anywhere. That is why this is an `experiment` with a built-in falsification test (the 14-day reconciliation) rather than a `build`. Fully reversible: no migration is destructive, `Depletion` is append-only, and the only cost of being wrong is one new table and a derived report. v1 bucket. Attached to `le31 Research` P-HMM-1 in the fallback payload only — **not attached in Linear** (write endpoint blocked, 34th consecutive day).