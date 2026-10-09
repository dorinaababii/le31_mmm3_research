# HANDOFF — 298-erhatechnologiesai-point-of-sale-system-v1-small-shop-pos-vocabulary

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-09
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/298-erhatechnologiesai-point-of-sale-system-mit-cloud-point-of-sale-pos-touchscreen-cashier-register-mock-payments-automated-receipt-generation-customer-loyalty-rewards-v1-small-shop-pos-vocabulary-reference.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; strongest v1 small-shop-POS-on-stack touchscreen-cashier-register cross-section pick of the 72-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window v1 small-shop-POS touchscreen-cashier-register vocabulary reference (`erhatechnologiesai/point-of-sale-system`, MIT, 0★/0⑨, 22 KB tiny, Python ✓ on-stack (FastAPI + Pydantic + SQLite = exact LE31-stack-adjacent), 10 topics, IN-WINDOW BY BOTH FIELDS, 10/10 LE31 v1 small-shop-POS-vocabulary envelope = 100% topic-overlap) for the next time the LE31 owner opens a v1 small-shop-POS touchscreen-cashier-register surface window.

If the trigger condition (v1 small-shop-POS touchscreen-cashier-register surface window opens) is met, the external coding agent should:

1. Read the active feature file in full.
2. Confirm the `erhatechnologiesai/point-of-sale-system` repo is still in-window (pushed within last 7 days from the trigger date) and the description is still the same.
3. Set up minimal-HTML/HTMX `pos-register.html` template for the touchscreen cashier register UI.
4. Implement the `PosRegister + PosReceipt + PosCustomerLoyalty + PosLoyaltyEarnEvent` SQLModel tables as described in the active feature's Data model section.
5. Implement the `POS` FastAPI endpoints (`/api/pos/register`, `/api/pos/receipt`, `/api/pos/loyalty`).
6. Implement the automated-receipt-generation discipline (every transaction auto-generates a receipt HTML).
7. Implement the customer-loyalty-rewards discipline (every purchase earns loyalty points) per charter §3.7 *counts-not-identity* discipline.
8. Implement the mock-payments discipline (no real money in test environment per charter §3.4).
9. Adapt the `point-of-sale-system`'s SQLite choice to LE31 v1's Postgres invariant.
10. Adapt the `point-of-sale-system`'s Pydantic schema to LE31 v1's existing Pydantic schema.
11. Run the v1 test suite + the new v1 small-shop-POS test suite.
12. Surface any test failures to the owner (LE31 v1 has no POS-register today; the test suite will be green if `PosRegister + PosReceipt + PosCustomerLoyalty + PosLoyaltyEarnEvent` are empty, but the touchscreen-cashier-register + mock-payments + automated-receipt-generation + customer-loyalty-rewards disciplines must be verified against the v1 stack).
13. Verify the v1 `audit_logs + StockEntry + MenuItem` SQLModel tables are untouched (the v1 `PosRegister + PosReceipt + PosCustomerLoyalty + PosLoyaltyEarnEvent` tables are NEW, not a migration of v1 `audit_logs`).
14. Charter §3.4 NOT TRIGGERED — the *POS + cashier-register + receipt-generator + customer-loyalty-rewards* surface is operator-tooling + customer-data-collection, not customer-facing-AI; the *mock-payments* posture IS the *non-real-money-test-environment* charter §3.4 invariant applied to the *payment* dimension.

If the trigger condition is **not** met, do nothing. The defer artifact can be safely ignored until the owner opens a v1 small-shop-POS touchscreen-cashier-register surface window.

## Mandatory inputs

- **Active feature**: `features/298-erhatechnologiesai-point-of-sale-system-mit-cloud-point-of-sale-pos-touchscreen-cashier-register-mock-payments-automated-receipt-generation-customer-loyalty-rewards-v1-small-shop-pos-vocabulary-reference.md`
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-10-09.md` (pass 72, pick C)
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-09/verify_erhatechnologiesai_point-of-sale-system.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 72-pass series**:
  - **Feature 295 — `23f3000434/CakeShopManagement`** — v1 in-domain bakery-POS
  - **Feature 265 — `violentzone/CarzinomaxERP`** — v1 small-business-AI-ERP-vocabulary
  - **Feature 195 — `skaslam1407/Restaurant-and-Cloud-Kitchen-Operations-Management`** — v1 frappe-erpnext-cloud-kitchen
  - **Feature 176 — `Sholu021/KitchenIQ`** — v1 fastapi-postgresql-restaurant-erp-fefo-ai-copilot
  - **Feature 218 — `LuisRG98/restaurant-saas-api`** — v1 production-restaurant-api-reference
  - **Feature 276 — `Mu7ammad01/Snacki-ndb`** — v1 restaurant-pwa-fastapi-vocabulary
  - **Feature 239 — `Hearthplug/mosaic-erp`** — v1 small-shop-POS-inventory-ERP-vocabulary
  - **Adjacent-evidence today (not picked)** — `mdaedalus/tableflow` (GPL-3.0 §3.2 BLOCKS v1; off-stack-but-vocabulary-only) + `Robahy/foxshop` (PyQt5 desktop not in charter §3.1 stack) + `ALPHAMAN-0/burgerCodeEmployes` (no tips surface in v1) + `shakhruz/mila-companion` (off-domain already filed as adjacent evidence)

## Verification protocol

Per `le31-conventions/SKILL.md` verification protocol:
- All SQLModel tables must use `Decimal` for `subtotal_eur + tax_eur + total_eur` fields (charter §3.6)
- All datetime fields must be timezone-aware (Europe/Paris per charter §3.6)
- All POS-receipt events must write to `audit_logs` via the standard LE31 audit-pipeline (charter §3.1 + §3.3)
- All on-stack dependencies (FastAPI, Pydantic) per charter §3.1 stack constraint
- All off-stack dependencies (HTMLReceiptGenerator, Mock-payment-gateway, SQLite) require explicit charter review

## Rollback path

The pick is a parking-lot vocabulary reference. If the trigger condition is met and the implementation does not work, the implementation can be rolled back by:
1. Dropping the `PosRegister + PosReceipt + PosCustomerLoyalty + PosLoyaltyEarnEvent` SQLModel tables (no data loss expected; vocabulary-only references do not have production data)
2. Removing the `pos-register.html` minimal-HTML/HTMX template
3. Disabling the `POS` FastAPI endpoints (`/api/pos/register`, `/api/pos/receipt`, `/api/pos/loyalty`)
4. Removing the mock-payment-gateway integration

The rollback is fully reversible; no v1 data is touched.

## Mandatory LE31 skill list

The coding agent MUST load before starting any implementation:
- `le31-conventions` — for the standard v1 conventions (audit_logs, money discipline, Paris timezone)
- `le31-v1-feature-pattern` — for the standard v1 feature pattern (SQLModel tables + FastAPI endpoints + minimal-HTML/HTMX templates + Telegram interaction if any)
- `le31-handoff-spec` — for the slice handoff format (this document)
- `le31-coding-agent-brief` — for the paste-in prompt format (this slice contract is the paste-in prompt)

This is a **defer artifact**; the coding agent does NOT need to start implementation today. The trigger condition (v1 small-shop-POS touchscreen-cashier-register surface window opens) is not met. The artifact is preserved on file for future surfacing.
