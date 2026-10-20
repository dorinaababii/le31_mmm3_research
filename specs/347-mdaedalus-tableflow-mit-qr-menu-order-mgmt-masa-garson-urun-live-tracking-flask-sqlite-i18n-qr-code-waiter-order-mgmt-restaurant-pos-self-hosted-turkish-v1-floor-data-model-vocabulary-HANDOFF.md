# HANDOFF — Feature 347: `mdaedalus-tableflow-mit-qr-menu-order-mgmt-masa-garson-urun-live-tracking-flask-sqlite-i18n-qr-code-waiter-order-mgmt-restaurant-pos-self-hosted-turkish-v1-floor-data-model-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/347-mdaedalus-tableflow-mit-qr-menu-order-mgmt-masa-garson-urun-live-tracking-flask-sqlite-i18n-qr-code-waiter-order-mgmt-restaurant-pos-self-hosted-turkish-v1-floor-data-model-vocabulary.md` — defer/parking-lot (Pick A of Daily Brainstorm 2026-10-20).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes a *order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy primitive*, the owner wants *evidence that this floor-data-model-vocabulary exists in 2026 with the same order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy posture AND the 20-topic + restaurant-multilingual-POS + single-deploy + i18n + Turkish + QR-menu + waiter + SQLAlchemy + open-source + minimalist + digital-menu + self-hosted posture*, but struggles because *LE31 has no documented v1 floor-data-model-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy posture AND it's the 20-topic + restaurant-multilingual-POS + single-deploy + i18n + Turkish + QR-menu + waiter + SQLAlchemy + open-source + minimalist + digital-menu + self-hosted vocabulary of the 82-pass series"*. |
| 2 | Viability | ✓ | The owner/staff can understand the floor-data-model vocabulary (order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy) without specialist help. The **20-topic + 0★/0⑂ + Python ✓ ON-STACK + 582 KB modest + GPL-3.0 vocabulary-only + 16-day-old pushed-2026-10-04 repo** makes vocabulary viable, but code adoption is not viable (GPL-3.0 = vocabulary-only per §3.2). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + Flask OFF-STACK (LE31 v1 uses FastAPI) + SQLite OFF-STACK (LE31 v1 uses Postgres) + SQLAlchemy OFF-STACK (LE31 v1 uses SQLModel) + i18n ✓ ON-PATTERN (the §3.5 multi-language posture is portable) + multi-language ✓ ON-PATTERN (the §3.5 multi-language posture is portable; LE31 targets Italian-only today) + QR-code + QR-menu ✓ ON-PATTERN (LE31 v1 has feature 11 customer-qr-menu) + restaurant-management + restaurant-pos + self-hosted ✓ ON-PATTERN (the §3.5 self-hosted posture is portable) + waiter + order-management + pos + menu-system + digital-menu + minimalist + open-source + turkish OFF-PATTERN (LE31 v1 targets Italian-only + HTMX + Postgres + FastAPI, not Turkish + Flask + SQLite + open-source + minimalist). Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX + aiogram v3 + i18n-via-FastAPI-Babel. Rabbit hole: the *GPL-3.0 + Turkish + Flask + SQLite + open-source + minimalist + digital-menu* stack is off-LE31-stack (LE31 v1 is Italian-only + HTMX + Postgres + minimal-HTML/HTMX). Evidence strength: medium-high for vocabulary; high for transferability (the *order-as-sole-persisted-entity + i18n + multi-language + self-hosted + single-deploy* primitive IS portable). |
| 4 | Conflict | ✓ | Does not violate any invariant. The *order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy* primitives are §3.1 + §3.4 + §3.5-aligned (hands-busy phone-first + deterministic kernel + single-binary-install-on-Italian-desktop-laptop). The *order-as-sole-persisted-entity* posture IS the canonical §3.1 *operator-surface-collapses-to-one-ordered-list* invariant. No §3.7 customer-PII violation (the documents are vendor-side; the *Turkish+i18n+multi-language* posture is OFF-§3.5 unless §3.5 Italian-only-decision is made). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 defer outcome (order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy surface for the LE31 v1 floor-data-model). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (planned floor-data-model + i18n + Italian-only-market-scope) may adopt the *order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy* discipline; the reference is *naming*, not new build. The **20-topic + 0★/0⑂ + Python ✓ ON-STACK + 582 KB modest + GPL-3.0 vocabulary-only** makes this the strongest possible vocabulary reference for v1 floor-data-model (the FIRST 20-topic + restaurant-multilingual-POS + single-deploy + i18n + Turkish + QR-menu + waiter + SQLAlchemy + open-source + minimalist + digital-menu + self-hosted vocabulary of the 82-pass brainstorm series). |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable today (GPL-3.0 + Turkish + Flask + SQLite + open-source + minimalist + digital-menu stack off-LE31-v1-stack + no floor-data-model surface in v1 charter). The vocabulary IS portable AND the **20-topic + 0★/0⑂ + Python ✓ ON-STACK + 582 KB modest + GPL-3.0 vocabulary-only** makes this the strongest possible vocabulary reference for v1 floor-data-model.

## Bucket

**v1 (floor-data-model-+-order-as-sole-persisted-entity-+-table/garson/urun-as-lookup-columns-+-live-tracking-as-projection-over-order-state-+-i18n-+-multi-language-+-QR-menu-+-order-management-+-single-deploy-+-self-hosted-+-Turkish-vocabulary)** — the *vocabulary* is the value, not the code. The verbatim description + topics name the 8-tuple-primitive set (order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy + QR-menu + waiter + SQLAlchemy + open-source + minimalist + digital-menu) + the tech-stack (Python ✓ ON-STACK + Flask + SQLite + SQLAlchemy + i18n + multi-language + qr-code + qr-menu + restaurant-management + restaurant-pos + self-hosted + waiter + order-management + pos + menu-system + digital-menu + minimalist + open-source + turkish).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `order` table with `table_id` + `garson_id` + `urun_id` as lookup columns (NOT separate CRUD tables).
- `backend/alembic/versions/` — add migration for `live_tracking` view as a projection over order state.
- `backend/services/order_service.py` — new file with `OrderService` class (charter §3.1 *hands-busy phone-first + operator-surface-collapses-to-one-ordered-list* posture).
- `backend/services/live_tracking_service.py` — new file with `LiveTrackingService` class (charter §3.1 *derived-view-via-join* posture).
- `backend/services/i18n_service.py` — new file with `I18nService` class (charter §3.5 *multi-language + Italian-only-market-scope* posture).
- `backend/main.py` — wire the new sub-apps into the parent uvicorn app.
- `frontend/templates/order-list.html` — new minimal-HTML/HTMX template for the operator-facing-order-list.
- `frontend/templates/live-tracking.html` — new minimal-HTML/HTMX template for the operator-facing-live-tracking.
- `frontend/templates/qr-menu.html` — new minimal-HTML/HTMX template for the customer-QR-menu.
- `frontend/static/i18n-app.js` — new minimal-JS for the i18n + multi-language rendering (charter §3.5 *Italian-only-market-scope* posture).
- `tests/test_order_service.py` — new unit test for `OrderService`.
- `tests/test_live_tracking_service.py` — new unit test for `LiveTrackingService`.
- `tests/test_i18n_service.py` — new unit test for `I18nService`.
- `tests/integration/test_order_to_live_tracking.py` — new integration test for `OrderService` → `LiveTrackingService` (verify the *live-tracking-as-projection-over-order-state* posture).

## Verification protocol reference

See `/opt/data/le31_mmm3_research_work/skills/le31-v1-feature-pattern/SKILL.md` for the canonical v1 verification protocol.

## Rollback path

`git rm features/347-...md specs/347-...-HANDOFF.md` — single-file revert.

## Mandatory LE31 skill list

When the first v1 PR that adopts the *order-as-sole-persisted-entity + table/garson/urun-as-lookup-columns + live-tracking-as-projection-over-order-state + i18n + multi-language + self-hosted + single-deploy* discipline lands, the coding agent must load these skills before starting:

- `le31-conventions` — for the canonical §3.1 + §3.4 + §3.5 charter-invariant review.
- `le31-v1-feature-pattern` — for the canonical v1 feature pattern (HTMX-waiter + aiogram-cook-bot + append-only-StockEntry-ledger + Postgres + FastAPI + SQLModel).
- `le31-backend` — for the canonical FastAPI + SQLModel + Postgres + Alembic + append-only-ledger pattern.
- `le31-frontend` — for the canonical minimal-HTML/HTMX + minimal-JS pattern.
- `le31-handoff-spec` — for the canonical HANDOFF-spec format.
- `le31-coding-agent-brief` — for the canonical paste-in-prompt format.