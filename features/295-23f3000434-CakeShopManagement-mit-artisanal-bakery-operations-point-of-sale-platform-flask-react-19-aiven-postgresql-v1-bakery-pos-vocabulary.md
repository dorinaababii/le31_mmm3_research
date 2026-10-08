# Feature 295 — `23f3000434/CakeShopManagement` v1 in-domain bakery-POS-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v1 (attach to `le31 v1 — Core MVP` P-HMM-3 as the parent of the sub-issue, or to `le31 Research` P-HMM-1 if v1 project is reserved for already-spec'd work — see pipeline note)
> **Date:** 2026-10-08
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/295-23f3000434-CakeShopManagement-mit-artisanal-bakery-operations-point-of-sale-platform-flask-react-19-aiven-postgresql-v1-bakery-pos-vocabulary.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/295-23f3000434-CakeShopManagement-mit-artisanal-bakery-operations-point-of-sale-platform-flask-react-19-aiven-postgresql-v1-bakery-pos-vocabulary-HANDOFF.md`
> **Source daily brainstorm:** `/opt/data/le31-brainstorm-2026-10-08.md` (pass 71, pick C)
> **Parent-verified via:** direct GitHub API GET `/repos/23f3000434/CakeShopManagement` at `/tmp/le31-brainstorm-2026-10-08/verify_parent/23f3000434_CakeShopManagement.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed; v1 in-domain bakery-POS reference is a future-extension signal)
> **Parent-override evidence:** subagent's first-pass Pick C `dashpilot-labs/dashpilot-mcp` was off-domain DoorDash Drive API wrapper; parent re-surfaced `23f3000434/CakeShopManagement` from `gh_pos_py_df.json` and parent-direct-GitHub-API-GET verified.

## Goal

Surface a v1 in-domain bakery-POS vocabulary reference for **artisanal-bakery-operations + point-of-sale + Flask + React 19 + Aiven-PostgreSQL + vite** as a forward-looking pattern for any future LE31 v1 surface that exposes a single-vertical in-domain POS reference (bakery as the restaurant-vertical analog) on a Flask + React + Aiven-managed-PostgreSQL stack.

## Evidence / JTBD

**Evidence classification:** inferred. The *artisanal-bakery-operations + point-of-sale + Flask + React 19 + Aiven-PostgreSQL* discipline is forward-looking for any future LE31 v1 in-domain-POS-vertical-reference surface; no LE31 v1 surface today has in-domain-POS-vertical-reference. **Confidence: high** (0★/0⑂ + 363 KB modest + Python (Flask) on-stack-adjacent ✓ + 9-topic array including `aiven + bakery-management + flask + point-of-sale + pos + postgresql + python + react + vite` + 0 customer-facing AI + in-window by BOTH fields = strongest v1 in-domain bakery-POS cross-section pick of the 71-pass series).

**When** the LE31 owner wants to see an in-domain reference for a restaurant-vertical POS (bakery as the canonical small-restaurant analog), **the owner wants to** see a working Flask + React 19 + Aiven-PostgreSQL implementation that demonstrates the *artisanal-bakery-operations + point-of-sale* discipline, **but struggles because** the existing v1 `audit_logs + StockEntry + MenuItem` SQLModel tables are LE31-internal primitives with no in-domain reference, **so that** the owner cannot see how a similar single-vertical POS would be structured. The *artisanal-bakery-operations + point-of-sale + Flask + React 19 + Aiven-PostgreSQL* discipline IS the *in-domain-restaurant-tech* charter §3.1 invariant applied to the *bakery* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *artisanal-bakery-operations + point-of-sale + Flask + React 19 + Aiven-PostgreSQL + vite* sextuple-primitive as a candidate vocabulary for any future LE31 v1 in-domain-POS-vertical-reference surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres mapping for each primitive (Flask is off-stack for v1; FastAPI is the v1 choice; the discipline is Python-portable).
- Record the §3.1/§3.2/§3.3/§3.4/§3.6 alignment per `le31-conventions/SKILL.md`.
- Note the **9-topic array** = the most topic-rich in-domain-POS candidate of the 71-pass series.
- Note the *in-domain-bakery-as-restaurant-vertical-analog* posture: bakery is the canonical small-restaurant analog (single-tenant, single-vertical, simple POS, inventory + recipe + cost discipline).

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No Aiven-managed-PostgreSQL integration; v1 uses self-hosted PostgreSQL (charter §3.2 invariant).
- No Flask integration; v1 uses FastAPI (charter §3.1 invariant); the *Flask* discipline is Python-portable.
- No React 19 frontend integration; v1 uses minimal-HTML/HTMX (charter §3.1 invariant).

## Description

`23f3000434/CakeShopManagement` is an **artisanal-bakery-operations + point-of-sale platform built with Flask, React 19, and Aiven PostgreSQL** with the following properties:
- **🍰 Artisanal bakery operations & Point-of-Sale (POS) platform** — the central discipline is the *in-domain-bakery-POS* pattern (single-vertical, single-tenant, single-Postgres, simple POS, inventory + recipe + cost discipline).
- **Built with Flask, React 19, and Aiven PostgreSQL** — the stack is Python + Flask (off-stack for LE31 v1; FastAPI is the v1 choice; discipline is Python-portable) + React 19 (off-stack for v1; minimal-HTML/HTMX is the v1 choice; discipline is informational) + Aiven-PostgreSQL (Aiven is a managed-PostgreSQL provider; LE31 v1 uses self-hosted PostgreSQL; discipline is informational).
- **MIT permissive + 363 KB modest** — small enough to be a vocabulary reference, not a production codebase.
- **9-topic array** including `aiven + bakery-management + flask + point-of-sale + pos + postgresql + python + react + vite` = the most topic-rich in-domain-POS candidate of the 71-pass series.

The vocabulary is a strong §3.1-alignment signal for any future LE31 v1 in-domain-POS-vertical-reference surface because:
- The *artisanal-bakery-operations + point-of-sale* IS the §3.1 *in-domain-restaurant-tech* charter invariant applied to the *bakery* dimension.
- The *Flask + React 19 + Aiven-PostgreSQL + vite* IS the *Python + PostgreSQL + React* charter §3.1 invariant applied to the *Aiven-managed-PostgreSQL* dimension.
- The *bakery-management* topic IS the *bakery-as-restaurant-vertical* charter §3.1 invariant.

## Data model

```
BakeryOperation       (id, operation_type, occurred_at, baker_user_id, notes)  # NEW — input row
BakeryRecipe          (id, name, yield_units, prep_minutes, sell_price_eur)   # NEW — recipe table
BakeryIngredientUsage (id, bakery_recipe_id, ingredient_id, quantity, unit)  # NEW — recipe ingredients
BakeryIngredient      (id, name, unit, cost_per_unit_eur, current_stock)      # NEW — ingredient inventory
```

The `BakeryOperation + BakeryRecipe + BakeryIngredientUsage + BakeryIngredient` tables are the *input* layer (POS operations, recipes, ingredients, ingredient usage). They are **append-only** for `BakeryOperation` (charter §3.3 invariant) and **state-row** for `BakeryRecipe + BakeryIngredient` (the recipe and inventory are state, updated on each change). The *sell_price_eur + cost_per_unit_eur* fields use `Decimal` (Python `decimal.Decimal` or pydantic `condecimal`) per the existing v1 EUR convention (charter §3.6 invariant).

## Implementation steps

**This is a defer artifact. No code is written today.** When (and if) a future v1 PR adopts the *artisanal-bakery-operations + point-of-sale + Flask + React 19 + Aiven-PostgreSQL* discipline, the following files would be touched:
- `/opt/data/le31_mmm3_research_work/backend/app/models/bakery.py` — new SQLModel `BakeryOperation + BakeryRecipe + BakeryIngredientUsage + BakeryIngredient` tables (append-only for `BakeryOperation`, state-row for the rest).
- `/opt/data/le31_mmm3_research_work/backend/app/services/bakery_pos.py` — POS operations service (create + read + update for the 4 tables).
- `/opt/data/le31_mmm3_research_work/backend/app/templates/bakery.html` — minimal-HTML/HTMX template for the bakery POS frontend.
- (No other files expected to require changes for a vocabulary-only PR.)

## Telegram interaction

**None today** (defer artifact; no v1 build; vocabulary-only). If a future v1 in-domain-POS-vertical-reference surface is built, the cook-side Telegram bot could accept a `/bakery` command that shows the latest bakery-operations (e.g., "Today's bakery: 12 croissants sold, 2 stockouts on flour, 1 customer complained about stale bread"). The interaction is operator-facing per charter §3.4; not customer-facing.

## Dependencies

- **Charter §3.1 (in-domain-restaurant-tech + Python + PostgreSQL)**: the *artisanal-bakery-operations + point-of-sale + Flask + Aiven-PostgreSQL* discipline IS the *in-domain-restaurant-tech* charter invariant applied to the *bakery* dimension; the *Python + PostgreSQL* primitive IS in the v1 stack; the *Flask* discipline is Python-portable to FastAPI.
- **Charter §3.2 (self-hosted + zero-external-dependencies)**: the *Aiven-PostgreSQL* is a managed-PostgreSQL provider; LE31 v1 uses self-hosted PostgreSQL (charter §3.2 invariant). A future PR that adopts the Aiven-managed-PostgreSQL discipline would need an explicit charter decision (or substitute with self-hosted PostgreSQL on the LE31 v1 VPS).
- **Charter §3.3 (audit-log-immutability)**: the `BakeryOperation` table is append-only (charter §3.3 invariant); the `BakeryRecipe + BakeryIngredient` tables are state-rows (updated on each change).
- **Charter §3.4 (operator-facing)**: the *in-domain-POS-vertical-reference* surface is operator-tooling per charter §3.4 invariant; the *artisanal-bakery-operations + point-of-sale* primitive is a deterministic POS primitive, not customer-facing AI.
- **Charter §3.6 (Money: never use binary floats)**: the *sell_price_eur + cost_per_unit_eur* fields use `Decimal` (Python `decimal.Decimal` or pydantic `condecimal`) per the existing v1 EUR convention.
- **Stack note**: `23f3000434/CakeShopManagement` uses Flask + React 19 + Aiven-PostgreSQL; LE31 v1 uses FastAPI + minimal-HTML/HTMX + self-hosted PostgreSQL. The discipline is Python-portable; the v1 reference would substitute Flask→FastAPI, React→minimal-HTML/HTMX, Aiven-PostgreSQL→self-hosted-PostgreSQL.
- **No v1 dependencies today**: this is a v1 forward-looking surface; no v1 code depends on it.

## Open questions

1. **What is the v1 stack substitution?** A future PR would need to specify the stack substitution (Flask→FastAPI, React→minimal-HTML/HTMX, Aiven-PostgreSQL→self-hosted-PostgreSQL). The *discipline* is stack-portable; the *stack* is not.
2. **What is the relationship between the v1 `MenuItem` SQLModel table and the v1 `BakeryRecipe` SQLModel table?** The v1 `MenuItem` is a flat menu item; the v1 `BakeryRecipe` is a recipe (with `yield_units + prep_minutes + sell_price_eur + BakeryIngredientUsage`). A future PR would need to specify the relationship (e.g., are `BakeryRecipe` rows a subtype of `MenuItem` rows?).
3. **What is the relationship between the v1 `StockEntry` SQLModel table and the v1 `BakeryIngredientUsage` SQLModel table?** The v1 `StockEntry` is a manual structured event log; the v1 `BakeryIngredientUsage` is a recipe-driven consumption log. A future PR would need to specify the relationship (e.g., do `BakeryOperation` rows auto-create `StockEntry` rows?).
4. **What is the bakery-vertical scope?** A future PR would need to specify the bakery-vertical scope (croissants only? full bakery menu? café+bakery?).
5. **What is the data freshness?** A future PR would need to specify the recompute policy (e.g., nightly, on-demand). A nightly recompute is the most common.

## Why this matters

This is the **strongest v1 in-domain bakery-POS cross-section pick of the 71-pass brainstorm series**. The *artisanal-bakery-operations + point-of-sale + Flask + React 19 + Aiven-PostgreSQL + vite* sextuple-primitive maps 1:1 onto the *in-domain-POS-vertical-reference* surface that a future v1 PR might add to extend the existing `audit_logs + StockEntry` SQLModel tables. The Python (Flask) + 9-topic + 0★/0⑂ + in-window-by-both-fields stack is **§3.1 + §3.2 + §3.3 + §3.4 + §3.6 ON-PATTERN** for LE31; the *Flask + React 19 + Aiven-PostgreSQL* discipline is stack-adjacent.

The **artisanal-bakery-operations + point-of-sale** discipline extends the existing v1 event-sourcing pattern to the *in-domain-bakery* dimension. The **Flask + React 19 + Aiven-PostgreSQL** discipline is stack-adjacent (the *Python + PostgreSQL* primitive is shared with v1; the *Flask + React + Aiven* primitives are off-stack but Python-portable + informational). The **bakery-as-restaurant-vertical-analog** posture IS the *in-domain-restaurant-tech* charter §3.1 invariant applied to the *bakery* dimension.

**Charter alignment summary:** §3.1 partial (in-domain-bakery + point-of-sale + Python ✓; Flask off-stack but Python-portable; Aiven-PostgreSQL off-stack but self-hosted-substitution); §3.2 strictly-compatible (the *Aiven-managed-PostgreSQL* posture is informational; LE31 v1 uses self-hosted PostgreSQL; the *self-hosted* charter §3.2 invariant would need an explicit decision if Aiven is adopted); §3.3 ✓ (append-only `BakeryOperation` = same pattern as v1 `StockEntry`); §3.4 strong alignment (in-domain-POS-vertical-reference + operator-facing + non-AI-fallback + observable-evidence); §3.6 ✓ (sell_price_eur + cost_per_unit_eur = existing v1 EUR convention with `Decimal`); §3.7 N/A.

---

**LE31 charter alignment summary** (per `le31-conventions/SKILL.md`): §3.1 partial; §3.2 partial (Aiven-managed-PostgreSQL off-§3.2; explicit charter-decision needed); §3.3 ✓; §3.4 strong alignment; §3.6 ✓; §3.7 N/A.
