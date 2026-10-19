# HANDOFF — Feature 345: `alissonlittig-vitrine-erp-mit-desktop-pdv-erp-multiloja-python-sqlite-customtkinter-multistore-retail-portfolio-v2-owner-pains-multistore-desktop-POS-ERP-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/345-alissonlittig-vitrine-erp-mit-desktop-pdv-erp-multiloja-python-sqlite-customtkinter-multistore-retail-portfolio-v2-owner-pains-multistore-desktop-POS-ERP-vocabulary.md` — defer/parking-lot (Pick B of Daily Brainstorm 2026-10-19).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2 owner-pains surface proposes a *multi-shop / multi-store-data-model + desktop-install-able-operator-binary + portfolio-posture primitive*, the owner wants *evidence that this multi-shop-data-model-vocabulary exists in 2026 with the same multi-store-PDV-ERP + portfolio-posture + Python + SQLite + CustomTkinter posture*, but struggles because *LE31 has no documented v2 owner-pains multi-shop-data-model-vocabulary reference*, so that *the v2 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same multi-store-data-model + portfolio-posture + single-binary-installer + Italian-desktop-laptop-install-able posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (multi-store-POS + ERP + portfolio-posture + Python + SQLite + CustomTkinter + desktop-app) without specialist help. The 2★/0⑨ with maintainer activity (created 2026-09-24 + pushed 2026-09-24 = IN-WINDOW BY BOTH FIELDS, ~25-day-old repo, same-instant push, 2025 KB modest) makes vocabulary viable, but code adoption is not viable (LE31 v2 has no multi-shop / multi-store surface today; v2 is single-shop + online + Postgres + minimal-HTML/HTMX). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + SQLite OFF-STACK (LE31 v2 is Postgres, not SQLite) + CustomTkinter OFF-STACK (LE31 v2 is minimal-HTML/HTMX, not desktop-CustomTkinter) + Desktop-app OFF-STACK (LE31 v2 is online + browser, not desktop-app) + multi-store-retail OFF-PATTERN (LE31 v2 is single-shop today; multi-shop is a v2 expansion wedge) + portfolio ✓ ON-PATTERN (go-to-market stance only). Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX; multi-shop-data-model requires explicit §3.5 review. Rabbit hole: the *CustomTkinter + SQLite + Desktop-app + multi-store* stack is off-LE31-stack (LE31 v2 is single-shop + online + Postgres + minimal-HTML/HTMX). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *multi-store-data-model + portfolio-posture + single-binary-installer + Italian-desktop-laptop-install-able* primitives are §3.5-aligned (multi-shop-data-model + Italian-desktop-laptop-install-able). The *per-shop-ledger + multi-shop-rollup* posture IS the §3.1 *explicit-state-transitions* + §3.5 *multi-shop-rollup* charter invariant. No §3.4 customer-facing AI. No data rule violation (charter §3.7 N/A for the multi-shop-PDV-ERP surface today). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2 owner-pains defer outcome (multi-shop-data-model + single-binary-installer + multi-shop-rollup surface for the LE31 v2 owner-pains). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v2 owner-pains surfaces (planned operator-pain-surfaces + AI-assisted) may adopt the *multi-shop-data-model + portfolio-posture + single-binary-installer + Italian-desktop-laptop-install-able* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable today (CustomTkinter + SQLite + Desktop-app stack off-LE31-v2-stack + no multi-shop-data-model surface in v2 charter). The vocabulary IS portable.

## Bucket

**v2 owner-pains** (multi-shop / multi-store-data-model + desktop-install-able-operator-binary + portfolio-posture-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 7-tuple-primitive set (multi-store-POS + ERP + portfolio-posture + Python + SQLite + CustomTkinter + desktop-app + multi-store-retail) + the tech-stack (Python + SQLite + CustomTkinter + ERP + portfolio + POS + desktop-app + multi-store-retail).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v2 PR that adopts the *multi-shop / multi-store-data-model + portfolio-posture + single-binary-installer + Italian-desktop-laptop-install-able* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `Shop`, `Customer` (with `shop_id`), `Product` (with `shop_id`), `Sale` (with `shop_id`), `SaleItem` tables.
- `backend/services/shop.py` — new file with `Shop` model + `ShopService` class (multi-shop-data-model; the §3.5 invariant).
- `backend/services/customer_shop.py` — new file with `CustomerShopService` class (per-shop-customer; the §3.1 invariant).
- `backend/services/product_shop.py` — new file with `ProductShopService` class (per-shop-SKU; the §3.1 invariant).
- `backend/services/sale_shop.py` — new file with `SaleShopService` class (per-shop-sale + multi-shop-rollup query; the §3.1 + §3.5 invariant).
- `backend/services/italian_desktop_installer.py` — new file with `ItalianDesktopInstaller` script (single-binary-installer; the §3.5 Italian-desktop-laptop-install-able posture).
- `frontend/templates/shop-list.html` — new minimal-HTML/HTMX template for the operator-facing-multi-shop-list.
- `frontend/templates/shop-detail.html` — new minimal-HTML/HTMX template for the operator-facing-per-shop-detail.
- `frontend/templates/multi-shop-rollup.html` — new minimal-HTML/HTMX template for the operator-facing-multi-shop-rollup.
- `backend/main.py` — wire the new sub-apps into the parent uvicorn app.
- `tests/test_shop.py` — new unit test for `ShopService`.
- `tests/test_customer_shop.py` — new unit test for `CustomerShopService`.
- `tests/test_product_shop.py` — new unit test for `ProductShopService`.
- `tests/test_sale_shop.py` — new unit test for `SaleShopService`.
- `tests/integration/test_multi_shop_rollup.py` — new integration test for the multi-shop-rollup query.

## Verification protocol reference

When the first v2 PR that adopts the *multi-shop / multi-store-data-model + portfolio-posture + single-binary-installer + Italian-desktop-laptop-install-able* discipline lands, the verification protocol is:

1. Run `pytest tests/test_shop.py` and verify the `ShopService` produces a valid shop-model for multi-shop-onboarding.
2. Run `pytest tests/test_customer_shop.py` and verify the `CustomerShopService` produces a valid per-shop-customer-model.
3. Run `pytest tests/test_product_shop.py` and verify the `ProductShopService` produces a valid per-shop-SKU-model.
4. Run `pytest tests/test_sale_shop.py` and verify the `SaleShopService` produces a valid per-shop-sale-model.
5. Run `pytest tests/integration/test_multi_shop_rollup.py` and verify the multi-shop-rollup query computes *per-shop-revenue + across-shop-rollup* correctly.
6. Run `python backend/services/italian_desktop_installer.py` and verify the single-binary-installer produces a runnable `.exe` for Italian-desktop-laptop.
7. Open `frontend/templates/shop-list.html` in a browser and verify the operator-facing-multi-shop-list renders the shops as a navigable table.
8. Open `frontend/templates/multi-shop-rollup.html` in a browser and verify the operator-facing-multi-shop-rollup renders the rollup correctly.
9. Inspect the `Shop` + `Customer` + `Product` + `Sale` + `SaleItem` tables in Postgres and verify the `shop_id` foreign-keys are correct (the §3.1 + §3.5 multi-shop-data-model invariant).

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v2 PR that adopts the *multi-shop / multi-store-data-model + portfolio-posture + single-binary-installer + Italian-desktop-laptop-install-able* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the five tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.
5. Remove the `italian_desktop_installer.py` script from the build pipeline.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:

- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-v1-feature-pattern/SKILL.md` — for the v1 feature contract shape and slicing rules.
- `skills/le31-research/SKILL.md` — for the research workflow and report shape.
- `skills/le31-feature-pipeline/SKILL.md` — for the feature pipeline (lease to coding agent).
- `skills/le31-handoff-spec/SKILL.md` — for the handoff spec (this file).
- `skills/le31-coding-agent-brief/SKILL.md` — for the paste-in brief.
- `skills/le31-backend/SKILL.md` — for the backend conventions (if applicable).
- `skills/le31-frontend/SKILL.md` — for the frontend conventions (if applicable).
- `skills/le31-data/SKILL.md` — for the data conventions (if applicable).
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

This defer artifact is documentation only. It becomes a build trigger when the **first v2 PR that adds a multi-shop / multi-store-data-model surface to the LE31 v2 owner-pains** lands. At that point:

1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which multi-shop-data-model schema (per-shop-customer + per-shop-SKU + per-shop-sale + multi-shop-rollup vs single-customer + cross-shop-SKU + per-shop-sale + multi-shop-rollup) becomes the canonical.
3. Decide which multi-shop-rollup query (per-shop-revenue + across-shop-rollup vs per-shop-revenue + per-shop-profit + across-shop-rollup) becomes the canonical.
4. Apply charter §3.5 review to the *single-binary-installer + Italian-desktop-laptop-install-able* posture before any v2 PR.
5. Adopt the *multi-shop-data-model + portfolio-posture + single-binary-installer + Italian-desktop-laptop-install-able* discipline on the chosen surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v2 code is shipped.
