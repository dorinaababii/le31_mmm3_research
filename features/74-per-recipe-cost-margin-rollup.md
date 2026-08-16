# Feature 74 — Per-Recipe Cost + Margin Rollup from StockEntry

> **Priority**: P3 (parking-lot) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-16 (Pick B, **parking-lot**) · **Bucket**: new (v2 owner-pains candidate)
> **One-line**: A research-only **parking-lot** artifact that records the in-window GitHub repo `ifrederico/forkluck` (pushed 2026-08-16T04:37:15Z, AGPL, 0★, "Open-source recipe costing, labor, and sales workbench for working kitchens") — a Django + Next.js kitchen-costing workbench whose pattern (recipe costing from ingredient deltas) maps directly onto LE31's existing `StockEntry` ledger. **No code today; parked until feature 43 (prep-checkoff adherence) ships to provide per-prep-task timing data for the labor-cost dimension and feature 21 (recipe generation) ships to provide the Recipe-to-IngredientBatch map.**

## Goal

The kitchen-costing workbench pattern —rolling up the actual ingredient cost of each menu item from receipt-side `StockEntry` deltas, divided by expected yield, surfaced as theoretical cost alongside menu price — is **the missing piece between feature 19 (`menu-engineering`, price-only) and feature 21 (`recipe-generation`, AI dish-from-leftovers)**. The owner pain "what does this dish actually cost to plate, and which dishes have the best margin?" is unanswered in LE31 today.

The slice ships **zero code**; the slice ships **one parking-lot artifact** that future v2 passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 owner wants to decide which dishes to keep on the menu and which to retire, the owner wants to see the theoretical plate cost of each menu item alongside the menu price, but the existing `StockEntry` ledger is not exposed as a per-recipe cost rollup, so that the owner can see margin per dish in under 30 seconds without leaving the kitchen.

**Why this is a fresh cross-section signal today**: `ifrederico/forkluck` (AGPL, Python Django + Next.js, 0★, "Open-source recipe costing, labor, and sales workbench for working kitchens") was pushed 2026-08-16T04:37:15Z — created 2026-08-11, in-window. The repo confirms the JTBD pull exists in the broader ecosystem (a kitchen-workbench pattern that the AGPL author's first-push did not yet validate with stars but did validate with the very specific description). Combined with `Hamuda55/restaurant-ops-dashboard` (no license, Python Streamlit, 0★, 548 bytes README-only, "Restaurant operations analytics dashboard (Streamlit) on real, anonymised Square POS data - peak hours, revenue by day-part, menu performance"), the two repos form an **owner-side analytics pattern** that LE31 has the raw data to compute but no surface to render.

**Why parking-lot**: AGPL is viral copyleft — LE31 would not import code, only the pattern. The 0★ first-push repo carries no observed pain. The labor dimension is dropped (no time-tracking data); parking-lot until feature 43 (`telegram-prep-checkoff-adherence`) generates per-prep-task timing data that can roll up into labor cost. The Recipe-to-IngredientBatch map that the rollup needs does not exist (feature 21 has not shipped).

## Scope

**In scope (parking-lot, S effort, ≤1 day, defer — no observed pain):**
- One source-file edit: this `features/74-per-recipe-cost-margin-rollup.md` artifact (the parking-lot record).
- The corresponding HANDOFF.md under `specs/`.
- The corresponding row in `INDEX.md` "Active feature pipeline" table.

**Out of scope (deferred to a future v2 scope when feature 43 + feature 21 ship):**
- A new `/cost <menu_item>` cook-bot command. The parking-lot artifact records the pattern; it does NOT spawn a new LE31 implementation.
- A new owner no-account page for margin rollup. Same.
- A `ifrederico/forkluck` codebase fork or adaptation. AGPL is viral copyleft; LE31 would not import code, only the pattern. `ifrederico/forkluck` is Django + Next.js (not LE31's FastAPI + SQLModel + aiogram + Postgres). Pattern transfers, not code.
- A new pip dependency. None.

## Description

**Evidence precondition:** inferred (owner-KPI pattern from two 0★ repos, no observed pain). Confidence: **low** for the JTBD shape (the pattern is well-established in the broader ecosystem), **zero** for the LE31-specific pain (no observed pain, no HN/OpenAlex validating peer, no AGPL-acceptable peer).

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: Owner needs plate-cost per dish — plausible but not observed at the LE31 owner level. Cross-section pattern from kitchen-workbench ecosystem.
2. **Viability**: Once features 43 + 21 ship, the rollup is a build-time concern. **High** in that future state; **undefined** today.
3. **Practicability and confidence**: Features 43 + 21 prerequisites not yet shipped. **Low** confidence today.
4. **Conflict**: No invariant conflict. The rollup is a read-only query against existing `StockEntry` receipt rows.
5. **Outcome, appetite, scope**: v2 owner-pains. M effort if the prerequisites ship.
6. **Cost to operational value**: Low value today (prerequisites not yet shipped). High value once features 43 + 21 land.
7. **Circuit breaker**: Delete this file + the corresponding `INDEX.md` row + the Linear sub-issue. No other code changes to revert.

**Decision: parking-lot.** Re-evaluate when feature 43 + feature 21 ship to production.

## Data model

No data model changes. The slice is a pure parking-lot artifact. **Future scope** (if the feature un-parked): add a `RecipeIngredientBatch` SQLModel table mapping menu items to ingredient batches with `unit_cost` + `expected_yield` columns. The rollup query sums `abs(delta) * unit_cost / expected_yield` over all `StockEntry` receipt rows for each batch.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline" table with date 2026-08-16, pick `per-recipe-cost-margin-rollup`, feature path `features/74-per-recipe-cost-margin-rollup.md`, Linear sub-issue ID (TBD), status "Parking-lot (no observed pain; prerequisites not yet shipped)".
2. **Re-check** on a future daily-research pass once feature 43 ships to production and feature 21 ships a Recipe-to-IngredientBatch map. If the in-window GitHub `restaurant created:>2026-07-17 language:python` cluster continues to ship same-week kitchen-costing repos, the parking-lot re-activates.

## Telegram interaction

None. The slice is a research artifact; no user-facing Telegram surface changes.

## Dependencies

- The `/opt/data/INDEX.md` file — must be writable.
- Feature 43 (`telegram-prep-checkoff-adherence`) must ship to production to provide per-prep-task timing data for the labor-cost dimension.
- Feature 21 (`recipe-generation`) must ship to provide the Recipe-to-IngredientBatch map.
- The `MenuItem.unit_cost` column (introduced by feature 19) must be populated for all menu items.

No new pip dependencies today. No new system dependencies. No new external services.

## Open questions

- **Q1: Will `ifrederico/forkluck` gain stars? Currently 0★.** Re-check on a future pass. If the repo accumulates star velocity, the JTBD pull is validated.
- **Q2: Will feature 43 ship to production first?** Without feature 43, the labor-cost dimension is missing. The parking-lot is parked behind feature 43.
- **Q3: Will feature 21 ship a Recipe-to-IngredientBatch map?** Without feature 21, the rollup has no data to work with. The parking-lot is parked behind feature 21.
- **Q4: Will a non-AGPL peer emerge?** Currently `ifrederico/forkluck` is the only in-window kitchen-costing repo and is AGPL. If a non-AGPL peer emerges, the parking-lot's evidence precondition can be upgraded from "inferred" to "observed".

## Why this matters

The owner pain "which dishes have the best margin?" is a **real LE31 owner problem** (small restaurants often retire high-cost low-margin dishes that have low popularity). The pattern is mature in the broader ecosystem (workbench + cost-rollup is a standard restaurant-tech component). **The blocker is not pattern novelty; the blocker is observed pain + prerequisite availability.**

**Risk of NOT tracking**: the cost-rollup problem will surface after the owner reviews a quarterly margin report. If the parking-lot is not already in place when that happens, the build will be rushed. The watch exists to ensure the pattern is already-evaluated when the trigger condition arrives.

**Risk of over-tracking**: features 43 + 21 are not yet shipped. The parking-lot artifact is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the feature under "parking-lot until feature 43 + feature 21 ship to production." Re-evaluate when both prerequisites land.

## Status: parking-lot

This file is a **parking-lot artifact (no build)**. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. No code change today. The research-side subagent (Pass 17, 2026-08-16) records the pick as **parking-lot — no observed pain; prerequisites not yet shipped**.

## Cross-validation anchors

- **`ifrederico/forkluck`** (in-window, 2026-08-16T04:37:15Z push, AGPL, 0★, Django + Next.js) — kitchen costing workbench. Pattern transfer only.
- **`Hamuda55/restaurant-ops-dashboard`** (in-window, 2026-08-13T07:58:05Z push, no license, 0★, 548 bytes README-only, Streamlit) — analytics dashboard. Same-license / same-cluster signal.
- **Feature 19 (`menu-engineering`)** — price-only menu engineering. Pick fills the cost-side gap.
- **Feature 21 (`recipe-generation`)** — AI dish-from-leftovers. Pick needs feature 21's Recipe-to-IngredientBatch map.
- **Feature 43 (`telegram-prep-checkoff-adherence`)** — prep-task timing. Pick needs feature 43's per-prep-task timing for the labor-cost dimension.
- **Feature 39 (`owner-daily-recap-telegram`)** — owner daily recap. Pick is a drill-in extension of feature 39.
- **No HN / OpenAlex validating peer** — the GitHub `restaurant created:>2026-07-17 language:python` cluster is the only in-window signal. No HN thread, no OpenAlex paper, no ProductHunt item validates the LE31-specific pain.
