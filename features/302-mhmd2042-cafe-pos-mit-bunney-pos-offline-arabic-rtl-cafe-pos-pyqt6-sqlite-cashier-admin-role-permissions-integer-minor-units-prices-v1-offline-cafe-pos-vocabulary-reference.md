# Feature 302 — `mhmd2042-cafe-pos-mit-bunney-pos-offline-arabic-rtl-cafe-pos-pyqt6-sqlite-cashier-admin-role-permissions-integer-minor-units-prices-v1-offline-cafe-pos-vocabulary-reference` (defer)

> **NEW observation (2026-10-10).** Documents in-window GitHub repo `mhmd2042/cafe-pos` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Python + PyQt6 + SQLite, **pushed 2026-10-09T23:42:50Z** AND **created 2026-10-02T01:04:08Z** = IN-WINDOW BY BOTH FIELDS as an 8-day-old repo with fresh push, **363 KB modest repo**, default_branch=`main`, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-10): *"Offline Arabic RTL café POS system built with Python, PyQt6, and SQLite. Features order management, inventory tracking, and sales reporting."* The README reveals the actual product name = **Bunney POS** = *"A local, offline desktop point-of-sale and accounting app for a small café. Python 3, PyQt6 and SQLite, built and distributed for Windows. It needs no internet connection, and keeps everything on the machine it's installed on — no cloud, no API server, no telemetry. The interface is Arabic and right-to-left, since that's who it was built for. Prices are stored as integers in minor units and are tax-inclusive, so what's on the button is what the customer pays."* Topics (verbatim, parent-verified, 8): `arabic, cafe, desktop, pos, pyqt6, python, rtl, sqlite`. Bucket: **v1 (offline-café-POS-vocabulary)** — Pick A of Daily Brainstorm 2026-10-10. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **offline-first + PyQt6 + SQLite-WAL + parameterised-queries + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units-prices + tax-inclusive + finger-sized-touchscreen-controls + no-telemetry + role-based-cost/margin/profit-hiding + SQLite-online-backup-API (a copy taken mid-sale is still a valid database)** undecuple-primitive as a persistent cross-section reference for the LE31 v1 *offline-café-POS* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (8-day-old repo with fresh push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **offline-first + PyQt6 + SQLite-WAL + parameterised-queries + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units-prices + tax-inclusive + finger-sized-touchscreen-controls + no-telemetry + role-based-cost/margin/profit-hiding + SQLite-online-backup-API (a copy taken mid-sale is still a valid database)** undecuple-primitive: the entire café-POS surface is offline-first (no internet, no cloud, no API server, no telemetry); the database is SQLite in WAL mode with parameterised queries throughout; the interface is Arabic and right-to-left; prices are stored as integers in minor units and are tax-inclusive; the controls are finger-sized (sized for a finger, not a mouse); the cashier/admin role permissions are enforced in one place; the cashier does not see cost, margin, or profit figures; backups go through SQLite's online backup API (a copy taken mid-sale is still a valid database). This is the §3.1 explicit-state-transitions primitive applied to the *offline-café-POS + role-permissions + tax-disclosed-at-button + finger-touch* dimension.
- A written record of the **PyQt6 + SQLite + Python** stack-shape: this is **3/3 LE31 non-cloud-POS + single-tenant-RDBMS + Python** stack primitives matched (PyQt6 is the desktop-GUI primitive; SQLite is the single-tenant-RDBMS primitive; Python is the LE31 backend stack primitive). The **offline-first + no-internet + no-telemetry + SQLite-WAL** posture is the §3.5 + §3.1 *operator-can-keep-working-during-network-outage* invariant.
- A written record of the **operator-facing vocabulary** discipline: every control is sized for a finger, not a mouse; the category rail is on the reading side (Arabic RTL); the live cart is on the other; tapping a drink opens a modifier popup for size, milk, sugar, shots, extras, and free-text notes; tapping water just adds it. Sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 53/66 (offline-first) + feature 290 (restaurant-P&L-analytics).
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (8-day-old, first in-window push); (2) the stack-shape match is the value, not the code (LE31 v1 has no offline-POS surface; the v1 charter is web-UI + Telegram-bot, not PyQt6 desktop); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the Bunney POS codebase (8-day-old single-maintainer repo with no observed production usage + PyQt6 desktop is off-LE31-frontend-stack).
- Cross-pollination with the v1 charter §3.5 i18n posture (the v1 charter §3.5 is silent on i18n; Bunney's Arabic-RTL is a sister-shape, not a v1-build trigger).
- Any vendor-relationship with PyQt6 (Riverbank Computing) — LE31 v1 uses minimal-HTML/HTMX, not PyQt6 desktop.

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v1 surface proposes "an offline-first, finger-sized-touchscreen, cashier/admin-role-permissions, integer-minor-units, tax-inclusive, no-telemetry, Arabic-RTL café-POS primitive" (e.g., a v1 surface that introduces an offline-POS mode for the LE31 single-restaurant Swiss kitchen where the waiter/owner needs to keep working during a network outage, the cashier needs to tap finger-sized buttons, the admin needs to manage the menu, prices, inventory, reports, and backups, and the prices need to be stored as integers in minor units and be tax-inclusive so what's on the button is what the customer pays), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry" is a real demand signal*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31"*.

- **Evidence class**: observed (the description + topics + README name the primitives explicitly: `arabic, cafe, desktop, pos, pyqt6, python, rtl, sqlite` + *"offline-first + SQLite-WAL + parameterised-queries + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry + SQLite-online-backup-API"*).
- **Confidence**: medium-high for the vocabulary match (the verbatim description + README name the undecuple-primitive set + the tech-stack + the offline-first posture + the role-permissions posture + the tax-inclusive posture + the finger-sized-touchscreen posture + the no-telemetry posture + the SQLite-online-backup-API posture); low for transferability (LE31 v1 has no offline-POS surface; v1 charter is web-UI + Telegram-bot, not PyQt6 desktop).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no offline-POS surface); the value is the *offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry* vocabulary — when the first v1 PR that adds an offline-POS mode lands, the Bunney-POS pattern is a ready-made *named primitive*.

## Description

GitHub `mhmd2042/cafe-pos` (MIT, 0★/0⑂, Python + PyQt6 + SQLite, pushed 2026-10-09T23:42:50Z, created 2026-10-02T01:04:08Z, 363 KB, default_branch=`main`, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-10): *"Offline Arabic RTL café POS system built with Python, PyQt6, and SQLite. Features order management, inventory tracking, and sales reporting."*

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **Offline-first + no-internet + no-telemetry + no cloud + no API server** — the entire café-POS surface is offline-first; there are no network calls anywhere in the app. The *offline-first* primitive maps 1:1 onto LE31 v1's *operator-can-keep-working-during-network-outage* posture.
2. **SQLite-WAL-mode + parameterised queries throughout** — the database is SQLite in WAL mode (Write-Ahead Logging); every query is parameterised (no SQL injection risk). The *SQLite-WAL + parameterised-queries* primitive maps 1:1 onto LE31 v1's `StockEntry` schema discipline (which is append-only + parameterised).
3. **Arabic-RTL interface** — the entire UI is Arabic and right-to-left, since that's who it was built for. The *Arabic-RTL* posture is the *i18n* primitive applied to the *UI-text* dimension; LE31 v1 is multilingual Swiss kitchen and the v1 charter §3.5 is silent on i18n.
4. **Integer-minor-units-prices + tax-inclusive** — prices are stored as integers in minor units and are tax-inclusive, so what's on the button is what the customer pays. The *integer-minor-units + tax-inclusive* primitive IS the §3.6 money invariant applied to the *tax-disclosed-at-button* dimension.
5. **Finger-sized-touchscreen-controls** — every control is sized for a finger, not a mouse; the category rail is on the reading side (Arabic RTL); the live cart is on the other. The *finger-sized-touchscreen* primitive IS the *operator-UX-vocabulary* discipline applied to the *finger-touch* dimension.
6. **Cashier/admin-role-permissions enforced in one place** — two roles, enforced in one place; a cashier can sell, take payment, and run a shift; an admin additionally manages the menu, prices, inventory, reports, and backups. The *role-permissions* primitive IS the §3.1 *explicit-state-transitions* invariant applied to the *user-role* dimension.
7. **Role-based-cost/margin/profit-hiding** — cost, margin, and profit figures are never rendered on the cashier screen. The *role-based-data-hiding* posture IS the *cashier-doesn't-see-cost-data* discipline applied to the *role-permission* dimension.
8. **SQLite-online-backup-API** — backups go through SQLite's online backup API, so a copy taken mid-sale is still a valid database. The *SQLite-online-backup-API* primitive IS the *no-lost-data-during-backup* discipline applied to the *backup* dimension.
9. **Modifier popup (size, milk, sugar, shots, extras, free-text notes)** — tapping a drink opens a modifier popup for size, milk, sugar, shots, extras, and free-text notes; tapping water just adds it. The *modifier-popup* primitive IS the *menu-item-modifier* discipline applied to the *order* dimension.
10. **Windows-distributed + no internet required for install** — built and distributed for Windows; it needs no internet connection. The *Windows-distributed + no-internet-install* posture IS the *operator-can-install-without-network* discipline.
11. **PyQt6 + SQLite + Python stack** — Python 3 + PyQt6 + SQLite. The *PyQt6 + SQLite + Python* stack-shape IS the *desktop-POS-with-RDBMS* discipline.

**The 1:1 mapping onto LE31 surface:**

| Bunney-POS primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Offline-first + no-internet + no-telemetry | (LE31 v1 is server-side + Postgres + requires network) | §3.5 / §3.1 | **Not implemented** — v1 polish surface |
| SQLite-WAL + parameterised queries | `StockEntry` (append-only + parameterised) | §3.1 ✓ | **Implemented (v1, partial)** |
| Arabic-RTL interface | (LE31 v1 is i18n-silent; v1 charter §3.5) | v1 polish | **Not implemented** — i18n surface |
| Integer-minor-units-prices + tax-inclusive | `MenuItem.price_eur` (Decimal) | §3.6 ✓ | **Implemented (v1, partial)** — the §3.6 invariant is implemented in v1, but Bunney's *integer-minor-units* posture is a sister-shape to the §3.6 *never-use-binary-floats* invariant |
| Finger-sized-touchscreen-controls | (LE31 v1 is web-UI; the v1 charter §3.1 is *phone-first operator surface*) | §3.1 ✓ | **Not implemented** — v1 polish surface |
| Cashier/admin-role-permissions | (LE31 v1 has no role-permissions) | v1 polish | **Not implemented** — v1 polish surface |
| Role-based-cost/margin/profit-hiding | (LE31 v1 has no role-permissions) | v1 polish | **Not implemented** — v1 polish surface |
| SQLite-online-backup-API | (LE31 v1 uses Postgres; Postgres has its own backup API) | §3.1 ✓ | **Not implemented** — different DB |
| Modifier popup (size, milk, sugar, shots, extras) | (LE31 v1 has no modifier system; v1 `MenuItem` has no modifier) | v1 polish | **Not implemented** — v1 polish surface |
| Windows-distributed + no-internet-install | (LE31 v1 is server-side + requires Linux VPS) | §3.1 ✓ | **Not implemented** — different deployment |
| Python + PyQt6 + SQLite | (LE31 v1 is Python + FastAPI + Postgres) | §3.1 ✓ (Python match) | **Not implemented** — different stack |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that introduces an offline-POS mode for the LE31 single-restaurant Swiss kitchen), the implementation would add:

1. A new `OfflineCafePOSRegister` table (Alembic migration) with columns: `id` (UUID), `register_name` (str), `is_active` (bool), `last_heartbeat_at` (timezone-aware datetime), `created_at`, `updated_at`.
2. A new `OfflineCafePOSReceipt` table (Alembic migration) with columns: `id` (UUID), `register_id` (UUID FK), `total_minor_units` (int), `tax_minor_units` (int), `currency` (str, default=`EUR`), `created_at`, `printed_at` (nullable timezone-aware datetime).
3. A new `OfflineCafePOSCashierRole` + `OfflineCafePOSAdminRole` table (Alembic migration) with columns: `id` (UUID), `user_id` (UUID FK), `register_id` (UUID FK), `role` (enum: `cashier`, `admin`), `created_at`.
4. A new `OfflineCafePOSMenu` table (Alembic migration) with columns: `id` (UUID), `name` (str), `category` (str), `price_minor_units` (int), `tax_rate` (Decimal), `currency` (str, default=`EUR`), `is_active` (bool), `created_at`, `updated_at`.
5. A new `OfflineCafePOSMenuModifier` table (Alembic migration) with columns: `id` (UUID), `menu_item_id` (UUID FK), `modifier_type` (enum: `size`, `milk`, `sugar`, `shots`, `extras`, `free_text`), `modifier_name` (str), `price_delta_minor_units` (int, default=0), `created_at`.
6. A new `OfflineCafePOSInventory` table (Alembic migration) with columns: `id` (UUID), `menu_item_id` (UUID FK), `stock_count` (int), `reserved_count` (int, default=0), `last_counted_at` (timezone-aware datetime).
7. A new `OfflineCafePOSShift` table (Alembic migration) with columns: `id` (UUID), `register_id` (UUID FK), `cashier_user_id` (UUID FK), `started_at` (timezone-aware datetime), `ended_at` (nullable timezone-aware datetime), `total_sales_minor_units` (int, default=0), `total_tax_minor_units` (int, default=0).
8. An Alembic migration that adds the new tables.
9. A `OfflineCafePOSBackup` service that uses SQLite's online backup API (or Postgres's pg_dump for LE31's Postgres) to take a backup mid-sale without locking.
10. A role-based middleware that hides cost/margin/profit figures from the cashier screen.
11. A modifier-popup component for the v1 minimal-HTML/HTMX waiter-UI that opens a popup for size, milk, sugar, shots, extras, and free-text notes.

The HANDOFF is to evaluate whether the v1 offline-POS mode is the right product-wedge for the next v1 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires:

**For v1 offline-café-POS-vocabulary surface** (if approved):

1. Add new `OfflineCafePOSRegister` SQLModel table (Alembic migration).
2. Add new `OfflineCafePOSReceipt` SQLModel table (Alembic migration).
3. Add new `OfflineCafePOSCashierRole` + `OfflineCafePOSAdminRole` SQLModel table (Alembic migration).
4. Add new `OfflineCafePOSMenu` SQLModel table (Alembic migration).
5. Add new `OfflineCafePOSMenuModifier` SQLModel table (Alembic migration).
6. Add new `OfflineCafePOSInventory` SQLModel table (Alembic migration).
7. Add new `OfflineCafePOSShift` SQLModel table (Alembic migration).
8. Add Alembic migration for the new tables.
9. Add a `OfflineCafePOSBackup` service that uses Postgres's pg_dump (or SQLite's online backup API for an embedded mode) to take a backup mid-sale without locking.
10. Add role-based middleware that hides cost/margin/profit figures from the cashier screen.
11. Add a `offline-pos-register.html` minimal-HTML/HTMX template with finger-sized-touchscreen-controls + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + Arabic-RTL support (i18n via `accept-language` header + per-request locale).
12. Add a `OfflineCafePOSMenuModifier` UI component for the v1 minimal-HTML/HTMX waiter-UI that opens a popup for size, milk, sugar, shots, extras, and free-text notes.
13. Add a `OfflineCafePOSShift` UI component for shift start/end + total sales + total tax.
14. Add a `OfflineCafePOSInventory` UI component for stock counts + reserved counts.
15. Add a `OfflineCafePOSBackup` CLI command for manual backup (e.g., `python -m backend.app.pos.backup --register-id=<UUID>`).

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires, the v1 offline-café-POS surface would add **a v1 cook-Telegram-notification primitive** (e.g., the cook gets a Telegram notification when an offline-POS receipt is recorded + when a menu item is 86'd due to inventory exhaustion). The notification primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 290 (restaurant-P&L-analytics).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; the Bunney-POS stack is Python + PyQt6 + SQLite which is a sister-shape, not a 1:1 match).
- **External**: None (the offline-POS primitive is local to the LE31 instance; no external API; no telemetry).
- **Internal**: §3.1 (append-only discipline for `audit_logs`); §3.2 (MIT permissive license compatible); §3.5 (offline-first posture); §3.6 (integer-cents EUR discipline).
- **Trigger dependency**: future v1 PR that adds an offline-POS mode for the LE31 single-restaurant Swiss kitchen.

## Open questions

- **Q1**: When (if ever) will LE31 introduce an offline-POS mode? The v1 charter explicitly requires network + Postgres; v1 is server-side + Linux VPS, not Windows + PyQt6 desktop.
- **Q2**: If the offline-POS mode lands, will it use PyQt6 desktop (like Bunney) or minimal-HTML/HTMX web-UI (like LE31 v1)? The PyQt6 desktop approach is a different deployment model (Windows distribution) from LE31 v1's web-UI approach.
- **Q3**: Will the role-permissions primitive be §3.1-compliant? The cashier/admin role-permissions posture is a *role-based-access-control* primitive; LE31 v1's §3.1 *explicit-state-transitions* invariant is the *state-machine* primitive; the role-permissions primitive is a different dimension.
- **Q4**: How will the *integer-minor-units + tax-inclusive* posture interact with LE31 v1's `MenuItem.price_eur` (Decimal)? The v1 schema uses Decimal; the integer-minor-units posture is a sister-shape; a future v1 PR could add a `price_minor_units` column to `MenuItem` for storage while keeping `price_eur` (Decimal) for display.
- **Q5**: How will the *Arabic-RTL + i18n* posture interact with LE31 v1's i18n-silent charter? The v1 charter §3.5 is silent on i18n; a future v1 PR could add i18n support via `accept-language` header + per-request locale.

## Why this matters

The **offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry + SQLite-online-backup-API (a copy taken mid-sale is still a valid database)** undecuple-primitive is the **strongest direct LE31 v1 offline-café-POS-vocabulary reference of the 73-pass series** for three reasons:

1. **The undecuple-primitive vocabulary is the future v1 polish surface primitive**: when LE31 v1 introduces an offline-POS mode for the single-restaurant Swiss kitchen (e.g., a v1 surface that lets the owner keep working during a network outage, the cashier tap finger-sized buttons, the admin manage the menu, prices, inventory, reports, and backups, and the prices be stored as integers in minor units and be tax-inclusive so what's on the button is what the customer pays), the offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry + SQLite-online-backup-API primitive is the gate that satisfies §3.1 + §3.5 + §3.6. The Bunney-POS pattern is a ready-made *named primitive* for this gate.

2. **The PyQt6 + SQLite + Python stack-shape is the strongest of the 73-pass series**: Bunney's stack is Python + PyQt6 + SQLite (the LE31 stack is Python + FastAPI + Postgres; the *Python + SQLite* match is the LE31-stack-match; the *PyQt6* is a sister-shape, not a 1:1 match; the *Postgres* is a different RDBMS but the *append-only + parameterised-queries* discipline is the same).

3. **The 8-day-old repo with fresh push is the demand signal**: the maintainer is iterating fast (8-day-old repo with first in-window push today) without reading the LE31 charter. The demand for the *offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry* primitive is real, observable, and growing.

Sister-shape to features 119 (`Ritchalison/BalanceDesk` — §3.2 BLOCKER NOASSERTION, offline-first reconciliation terminal) + 295 (`23f3000434/CakeShopManagement` — artisanal-bakery-operations POS + Flask + React 19 + Aiven-PostgreSQL) + 297 (`jonalemndi2/ALdia` — open-source-business-engine + AI-agents + invoicing + payments + inventory + checks-and-cash + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country) + 298 (`erhatechnologiesai/point-of-sale-system` — cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt + customer-loyalty + FastAPI + Pydantic + SQLite). The Bunney-POS pattern is the **strongest direct offline-first + PyQt6 + SQLite + Arabic-RTL + cashier/admin-role-permissions + integer-minor-units + tax-inclusive + finger-sized-touchscreen + no-telemetry primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that adds an offline-POS mode for the LE31 single-restaurant Swiss kitchen.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/119-Ritchalison-BalanceDesk-...-offline-reconciliation-terminal.md` — §3.2 BLOCKER NOASSERTION; offline-first reconciliation terminal; sister-shape (the only §3.2-compatible offline-first primitive in features/1..301 is Pick A; the prior cluster is §3.2-blocked)
- `features/295-23f3000434-CakeShopManagement-...-artisanal-bakery-operations-pos.md` — artisanal-bakery-operations POS + Flask + React 19 + Aiven-PostgreSQL; sister-shape (in-domain restaurant-vertical POS)
- `features/297-jonalemndi2-ALdia-...-open-source-business-engine-ai-agents-mcp-tools.md` — open-source-business-engine + AI-agents + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country; sister-shape (offline-first + self-hosted posture)
- `features/298-erhatechnologiesai-point-of-sale-system-...-cloud-pos-touchscreen-cashier-register.md` — cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt + customer-loyalty + FastAPI + Pydantic + SQLite; sister-shape (FastAPI + Pydantic + SQLite stack match)
- `features/290-AlvaroVerona-prime-cost-...-restaurant-p-l-menu-engineering.md` — restaurant-P&L + menu-engineering + demand-forecast + staffing-optimization + monte-carlo; sister-shape (restaurant-P&L primitive)
- `features/53-...offline-first-v1-polish.md` and `features/66-...offline-first-v1-polish.md` — v1 offline-first primitives
- `features/39-...owner-daily-recap-telegram.md` — owner-daily-recap-telegram surface
- `features/16-...supplier-orders-bot.md` — supplier-orders-bot surface
