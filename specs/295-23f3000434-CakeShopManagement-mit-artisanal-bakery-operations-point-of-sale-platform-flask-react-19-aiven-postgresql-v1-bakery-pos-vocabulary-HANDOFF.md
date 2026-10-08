# HANDOFF — 295-23f3000434-CakeShopManagement-v1-bakery-pos-vocabulary

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-08
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/295-23f3000434-CakeShopManagement-mit-artisanal-bakery-operations-point-of-sale-platform-flask-react-19-aiven-postgresql-v1-bakery-pos-vocabulary.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; strongest v1 in-domain bakery-POS cross-section pick of the 71-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window v1 in-domain bakery-POS vocabulary reference (`23f3000434/CakeShopManagement`, MIT, 0★/0⑂, 363 KB modest, Python (Flask), 9-topic array, in-window by BOTH fields) for the next time the LE31 owner opens a v1 in-domain-POS-vertical-reference surface window.

If the trigger condition (v1 in-domain-POS-vertical-reference surface window opens) is met, the external coding agent should:

1. Read the active feature file in full.
2. Confirm the `23f3000434/CakeShopManagement` repo is still in-window (pushed within last 7 days from the trigger date) and the description is still the same.
3. Implement the `BakeryOperation + BakeryRecipe + BakeryIngredientUsage + BakeryIngredient` SQLModel tables as described in the active feature's Data model section.
4. Implement the bakery-POS service (POS operations service: create + read + update for the 4 tables).
5. Implement the stack-substitution mapping (Flask→FastAPI, React 19→minimal-HTML/HTMX, Aiven-PostgreSQL→self-hosted-PostgreSQL on the LE31 v1 VPS).
6. Add a minimal-HTML/HTMX template `bakery.html` for the bakery-POS frontend.
7. Run the v1 test suite + the new v1 in-domain-bakery-POS test suite.
8. Surface any test failures to the owner (LE31 v1 has no in-domain-bakery-POS today; the test suite will be green if `BakeryOperation + BakeryRecipe + BakeryIngredient` are empty, but the stack-substitution must be verified against the v1 stack).
9. Verify the v1 `audit_logs + StockEntry + MenuItem` SQLModel tables are untouched (the v1 `BakeryOperation + BakeryRecipe + BakeryIngredient` tables are NEW, not a migration of v1 `audit_logs`).
10. Verify the *sell_price_eur + cost_per_unit_eur* fields use `Decimal` per charter §3.6.

If the trigger condition is **not** met, do nothing. The defer artifact can be safely ignored until the owner opens a v1 in-domain-POS-vertical-reference surface window.

## Mandatory inputs

- **Active feature**: `features/295-23f3000434-CakeShopManagement-mit-artisanal-bakery-operations-point-of-sale-platform-flask-react-19-aiven-postgresql-v1-bakery-pos-vocabulary.md`
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-10-08.md` (pass 71, pick C)
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-08/gh_pos_py_df.json` (parent re-fetched the productive query) and `/tmp/le31-brainstorm-2026-10-08/verify_parent/23f3000434_CakeShopManagement.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 71-pass series**:
  - **Feature 293 — `quueli/shift-report-bot`** — v1 operator-text-to-structured-records
  - **Feature 294 — `quueli/yookassa-polling-payments`** — v1 payment-polling-without-webhook
  - **Feature 165 — `Ladle/restaurant-prep-forecasting`** — v1 food-cost-leak-detection
  - **Feature 173 — `Sholu021/KitchenIQ`** — v1 fastapi-postgresql-restaurant-erp-fefo-ai-copilot
  - **Feature 195 — `skaslam1407/Restaurant-and-Cloud-Kitchen-Operations-Management`** — v1 frappe-erpnext-cloud-kitchen
  - **Feature 201 — `sahajasakhunala/DineDesk`** — v1 full-stack-restaurant-normalized-postgresql
  - **Feature 218 — `LuisRG98/restaurant-saas-api`** — v1 production-restaurant-api-reference
  - **Feature 276 — `Mu7ammad01/Snacki-ndb`** — v1 restaurant-pwa-fastapi-vocabulary
  - **Feature 290 — `AlvaroVerona/prime-cost`** — v1 restaurant-P&L-analytics (carry-over from 2026-10-07)

## Mandatory LE31 skill list

The external coding agent **MUST** load these skills before implementing:
- `le31-conventions` — charter invariants and the seven-check feature gate
- `le31-v1-feature-pattern` — v1 feature contract shape, slicing rules, and DoD
- `le31-handoff-spec` — frozen contract discipline and verification protocol
- `development` — generic coding pipeline (specify → plan → tasks → implement)
- `speckit-specify` — feature spec writer
- `speckit-plan` — implementation plan writer
- `speckit-tasks` — dependency-ordered task list writer

The external coding agent **MUST NOT**:
- Add Flask or React to the v1 stack without an explicit charter decision (v1 uses FastAPI + minimal-HTML/HTMX; the discipline is Python-portable).
- Add Aiven-managed-PostgreSQL to the v1 stack without an explicit charter decision (v1 uses self-hosted PostgreSQL per charter §3.2).
- Update or delete any `BakeryOperation` rows (append-only §3.3 invariant).
- Send `BakeryOperation` events to diners (operator-facing §3.4 invariant).
- Use binary floats for `sell_price_eur + cost_per_unit_eur` (use `Decimal` per charter §3.6).

## Frozen contract

The active feature file is the frozen contract. Do not silently change the slice, scope, or verification path. If new evidence requires a contract change, surface it to the user and patch the package before re-sending.

## Verification protocol

The external coding agent verifies:
1. Its read of the contract matches the recorded contract fields (`Goal`, `Evidence`, `Scope`, `Description`, `Data model`, `Implementation steps`, `Telegram interaction`, `Dependencies`, `Open questions`, `Why this matters`).
2. The slice does not require another skill, model, or migration outside the package.
3. The end-to-end acceptance path is executable in the configured environment.
4. The rollback or feature-removal path is present and reversible.

End-to-end acceptance path (when triggered):
- Baker creates a new `BakeryRecipe` for "Sourdough Croissant" with `yield_units=12, prep_minutes=180, sell_price_eur=2.50`
- Baker adds 3 `BakeryIngredientUsage` rows (flour, butter, salt)
- Baker creates a `BakeryOperation` row with `operation_type=bake, notes=12 croissants baked`
- The kitchen-display shows the in-progress recipe + the 3 ingredients
- The owner-daily-recap shows the day's bakery operations + the ingredient cost
- The stack-substitution test verifies the v1 stack (FastAPI + minimal-HTML/HTMX + self-hosted-PostgreSQL) works with the substituted tables

## Rollback path

- Delete the `BakeryOperation + BakeryRecipe + BakeryIngredientUsage + BakeryIngredient` SQLModel tables (drop + alembic downgrade).
- Delete the `bakery.py + bakery_pos.py` service files.
- Delete the `bakery.html` template.
- The v1 `audit_logs + StockEntry + MenuItem` SQLModel tables are untouched (NEW tables, not a migration).
- No data is lost (the `BakeryOperation + BakeryRecipe + BakeryIngredient` tables are NEW; deleting the tables loses the cached bakery-POS data but not the source `audit_logs + StockEntry`).

## Sign-off gap

This is a defer artifact. The trigger condition is **the next time the LE31 owner opens a v1 in-domain-POS-vertical-reference surface window** (estimated Q1 2027 based on the v1 roadmap; no current commitment).

The external coding agent must mirror back the frozen contract before implementing and stop if it cannot.

---

**LE31 charter alignment summary** (per `le31-conventions/SKILL.md`): §3.1 partial; §3.2 partial (Aiven-managed-PostgreSQL off-§3.2; explicit charter-decision needed); §3.3 ✓; §3.4 strong alignment; §3.6 ✓; §3.7 N/A.
