# HANDOFF — Feature 302: `mhmd2042-cafe-pos-...-v1-offline-cafe-pos-vocabulary-reference`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/302-mhmd2042-cafe-pos-mit-bunney-pos-offline-arabic-rtl-cafe-pos-pyqt6-sqlite-cashier-admin-role-permissions-integer-minor-units-prices-v1-offline-cafe-pos-vocabulary-reference.md` — defer/parking-lot (Pick A of Daily Brainstorm 2026-10-10).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes an *offline-first, finger-sized-touchscreen, cashier/admin-role-permissions, integer-minor-units, tax-inclusive, no-telemetry, Arabic-RTL café-POS primitive*, the owner wants *evidence that this offline-café-POS-vocabulary exists in 2026 with the same stack as LE31*, but struggles because *LE31 has no documented v1 offline-café-POS-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry + SQLite-online-backup-API posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (offline-first + finger-sized-touchscreen + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + no-telemetry + Arabic-RTL) without specialist help. The 0★ with single-maintainer cadence (8-day-old repo, first in-window push) makes code adoption not viable, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: **Python + PyQt6 + SQLite on-stack-sister-shape** (LE31 stack match for Python; PyQt6 is a sister-shape to FastAPI; SQLite is a sister-shape to Postgres). Required data + permissions + infrastructure: Python + PyQt6 + SQLite + WAL mode + parameterised queries. No AI capability required (the offline-café-POS primitive is deterministic). Rabbit hole: the *PyQt6 desktop* posture is off-LE31-frontend-stack (LE31 v1 uses minimal-HTML/HTMX, not PyQt6 desktop). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *offline-first + SQLite-WAL + parameterised-queries + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry + SQLite-online-backup-API* primitives are §3.1 + §3.5 + §3.6-aligned (operator-can-keep-working-during-network-outage + role-permissions + tax-disclosed-at-button). The *cashier/admin-role-permissions* posture IS the §3.1 *explicit-state-transitions* invariant applied to the *user-role* dimension. No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (offline-POS mode for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry`) already implement the discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + 8-day-old repo + PyQt6 desktop off-LE31-frontend-stack + no v1 offline-POS surface in v1 charter).

## Bucket

**v1** (offline-café-POS-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + README name the undecuple-primitive set (offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry + SQLite-online-backup-API) + the tech-stack (Python + PyQt6 + SQLite).

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds an offline-POS mode for the LE31 single-restaurant Swiss kitchen):

1. `backend/app/pos/models.py` — add new `OfflineCafePOSRegister` SQLModel table with columns: `id` (UUID), `register_name` (str), `is_active` (bool), `last_heartbeat_at` (timezone-aware datetime), `created_at`, `updated_at`.
2. `backend/app/pos/models.py` — add new `OfflineCafePOSReceipt` SQLModel table with columns: `id` (UUID), `register_id` (UUID FK), `total_minor_units` (int), `tax_minor_units` (int), `currency` (str, default=`EUR`), `created_at`, `printed_at` (nullable timezone-aware datetime).
3. `backend/app/pos/models.py` — add new `OfflineCafePOSCashierRole` + `OfflineCafePOSAdminRole` SQLModel table with columns: `id` (UUID), `user_id` (UUID FK), `register_id` (UUID FK), `role` (enum: `cashier`, `admin`), `created_at`.
4. `backend/app/pos/models.py` — add new `OfflineCafePOSMenu` SQLModel table with columns: `id` (UUID), `name` (str), `category` (str), `price_minor_units` (int), `tax_rate` (Decimal), `currency` (str, default=`EUR`), `is_active` (bool), `created_at`, `updated_at`.
5. `backend/app/pos/models.py` — add new `OfflineCafePOSMenuModifier` SQLModel table with columns: `id` (UUID), `menu_item_id` (UUID FK), `modifier_type` (enum: `size`, `milk`, `sugar`, `shots`, `extras`, `free_text`), `modifier_name` (str), `price_delta_minor_units` (int, default=0), `created_at`.
6. `backend/app/pos/models.py` — add new `OfflineCafePOSInventory` SQLModel table with columns: `id` (UUID), `menu_item_id` (UUID FK), `stock_count` (int), `reserved_count` (int, default=0), `last_counted_at` (timezone-aware datetime).
7. `backend/app/pos/models.py` — add new `OfflineCafePOSShift` SQLModel table with columns: `id` (UUID), `register_id` (UUID FK), `cashier_user_id` (UUID FK), `started_at` (timezone-aware datetime), `ended_at` (nullable timezone-aware datetime), `total_sales_minor_units` (int, default=0), `total_tax_minor_units` (int, default=0).
8. `backend/alembic/versions/` — add Alembic migration for the new tables.
9. `backend/app/pos/backup.py` — NEW: `OfflineCafePOSBackup` service that uses Postgres's pg_dump (or SQLite's online backup API for an embedded mode) to take a backup mid-sale without locking.
10. `backend/app/pos/middleware.py` — NEW: role-based middleware that hides cost/margin/profit figures from the cashier screen.
11. `backend/app/templates/offline-pos-register.html` — NEW: `offline-pos-register.html` minimal-HTML/HTMX template with finger-sized-touchscreen-controls + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + Arabic-RTL support (i18n via `accept-language` header + per-request locale).
12. `backend/app/pos/ui/menu_modifier_popup.html` — NEW: `OfflineCafePOSMenuModifier` UI component for the v1 minimal-HTML/HTMX waiter-UI that opens a popup for size, milk, sugar, shots, extras, and free-text notes.
13. `backend/app/pos/ui/shift.html` — NEW: `OfflineCafePOSShift` UI component for shift start/end + total sales + total tax.
14. `backend/app/pos/ui/inventory.html` — NEW: `OfflineCafePOSInventory` UI component for stock counts + reserved counts.
15. `backend/app/pos/cli/backup.py` — NEW: `OfflineCafePOSBackup` CLI command for manual backup (e.g., `python -m backend.app.pos.backup --register-id=<UUID>`).

## Verification protocol

1. `git clone https://github.com/mhmd2042/cafe-pos` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/mhmd2042/cafe-pos/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set + offline-first posture + role-permissions posture + tax-inclusive posture + finger-sized-touchscreen posture + no-telemetry posture + SQLite-online-backup-API posture).
3. `curl -sS -H "Authorization: Bearer ***" "https://api.github.com/repos/mhmd2042/cafe-pos"` for star count, fork count, license, language, pushed_at, created_at, topics, description, default_branch, archived (parent-verified 2026-10-10).
4. `curl -sS -H "Authorization: Bearer ***" -H "Accept: application/vnd.github.raw" "https://api.github.com/repos/mhmd2042/cafe-pos/readme"` for the README body (parent-verified 2026-10-10).
5. `grep -cF 'LE31' /tmp/le31-brainstorm-2026-10-10/verify/mhmd2042_cafe-pos.json` (parent-verified 2026-10-10: 0 matches — PASS).
6. `grep -cF 'LE31' /tmp/le31-brainstorm-2026-10-10/verify/mhmd2042_cafe-pos.json /tmp/le31-brainstorm-2026-10-10/verify/AnuragBhandary_Real-Time-Event-Streaming.json /tmp/le31-brainstorm-2026-10-10/verify/drwjkirkpatrick-web_the-pass.json` (parent-verified 2026-10-10: 0 matches — PASS).
7. `grep -lE 'github.com/mhmd2042/cafe-pos|mhmd2042/cafe-pos' features/*.md` (parent-verified 2026-10-10: 0 matches — feature 302 is the only reference; the new feature file itself matches but the contract says it is the first).
8. If the future v1 trigger fires, run the v1 offline-café-POS surface (FUTURE): `pytest backend/tests/pos/test_offline_cafe_pos.py -v` for unit tests; `pytest backend/tests/pos/test_offline_cafe_pos_integration.py -v` for integration tests; `curl -X POST http://localhost:8000/api/offline-pos/register` for smoke test; `curl -X GET http://localhost:8000/api/offline-pos/receipt` for receipt retrieval; `python -m backend.app.pos.backup --register-id=<UUID>` for manual backup; `pytest backend/tests/pos/test_offline_cafe_pos_role_permissions.py -v` for role-permissions tests; `pytest backend/tests/pos/test_offline_cafe_pos_i18n.py -v` for i18n tests.

## Rollback path

No code today. The handbook + HANDOFF can be reverted by `git rm features/302-mhmd2042-cafe-pos-...md specs/302-mhmd2042-cafe-pos-...-HANDOFF.md`.

If the future v1 trigger fires and the implementation is later rejected: `alembic downgrade -1` to drop the new tables; `git rm backend/app/pos/models.py backend/app/pos/backup.py backend/app/pos/middleware.py backend/app/templates/offline-pos-register.html backend/app/pos/ui/menu_modifier_popup.html backend/app/pos/ui/shift.html backend/app/pos/ui/inventory.html backend/app/pos/cli/backup.py backend/alembic/versions/<new_migration>.py`.

## Mandatory LE31 skill list

The coding agent must load the following skills before starting any future implementation of feature 302:

- `le31-conventions` — for the seven-check feature gate and the charter §3.1 + §3.2 + §3.5 + §3.6 invariants
- `le31-backend` — for the FastAPI + SQLModel + Postgres + Alembic stack patterns
- `le31-frontend` — for the minimal-HTML/HTMX waiter-UI patterns
- `le31-data` — for the `StockEntry` + `audit_logs` + `MenuItem` SQLModel table patterns
- `le31-v1-feature-pattern` — for the v1 feature contract template + bucket + cross-section references
- `le31-handoff-spec` — for the slice contract structure (active feature path + seven-check gate verdict + files to touch + verification protocol + rollback path)
- `le31-coding-agent-brief` — for the coding-agent-brief generation pattern (this HANDOFF IS the brief; the agent does not need to re-generate it)

## Why this matters

The **offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry + SQLite-online-backup-API (a copy taken mid-sale is still a valid database)** undecuple-primitive is the **strongest direct LE31 v1 offline-café-POS-vocabulary reference of the 73-pass series** because it is the only in-window 2026-10 Python offline-café-POS-vocabulary candidate that combines all 11 sub-primitives (offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry + SQLite-online-backup-API + role-based-cost/margin/profit-hiding) in a single 8-day-old repo with first in-window push.

Sister-shape to features 119 (Ritchalison/BalanceDesk — §3.2 BLOCKER NOASSERTION; offline-first reconciliation terminal) + 295 (23f3000434/CakeShopManagement — artisanal-bakery-operations POS + Flask + React 19 + Aiven-PostgreSQL) + 297 (jonalemndi2/ALdia — open-source-business-engine + AI-agents + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country) + 298 (erhatechnologiesai/point-of-sale-system — cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt + customer-loyalty + FastAPI + Pydantic + SQLite). The Bunney-POS pattern is the **strongest direct offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that adds an offline-POS mode for the LE31 single-restaurant Swiss kitchen.

**Fully reversible** (vocabulary-only artifact). No code today.
