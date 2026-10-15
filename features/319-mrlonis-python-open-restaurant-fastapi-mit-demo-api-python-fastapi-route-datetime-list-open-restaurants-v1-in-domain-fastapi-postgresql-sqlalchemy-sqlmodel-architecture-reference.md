# Feature 319 — `mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-list-open-restaurants-v1-in-domain-fastapi-postgresql-sqlalchemy-sqlmodel-architecture-reference` (defer)

> **NEW observation (2026-10-15).** Documents in-window GitHub repo `mrlonis/python-open-restaurant-fastapi` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **2★/1⑂**, language Python ✓ ON-STACK, **pushed 2026-10-09T11:25:37Z (in-window by `pushed_at` only; created 2022-12-07T03:24:31Z = 3.8-year-old repo with in-window push = active 2026 maintainer of the entire LE31 v1 stack from before LE31's charter date)**, **2620 KB modest**, `default_branch=main`, archived=`False`). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-15): *"Demo API, written in Python FastAPI, with one route that takes a datetime string and returns a list of open restaurants, if any."* Topics (verbatim, parent-verified, 5): `fastapi, postgresql, python, sqlalchemy, sqlmodel`. Bucket: **v1 (in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference)** — Pick C of Daily Research 2026-10-15. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`Demo-API-written-in-Python-FastAPI-with-one-route-that-takes-a-datetime-string-and-returns-a-list-of-open-restaurants-if-any + FastAPI + PostgreSQL + Python + SQLAlchemy + SQLModel`** sextuple-primitive as a persistent cross-section reference for the LE31 v1 *in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (3.8-year-old repo) using the **FastAPI + PostgreSQL + Python + SQLAlchemy + SQLModel = 5/5 LE31 v1 backend stack primitives matched** posture = the strongest in-window 2026 in-domain FastAPI+PostgreSQL+SQLAlchemy+SQLModel architecture reference of the 76-pass series. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`Demo-API-written-in-Python-FastAPI-with-one-route-that-takes-a-datetime-string-and-returns-a-list-of-open-restaurants-if-any + FastAPI + PostgreSQL + Python + SQLAlchemy + SQLModel`** sextuple-primitive.
- A written record of the **FastAPI + PostgreSQL + Python + SQLAlchemy + SQLModel = 5/5 LE31 v1 backend stack primitives matched** = the strongest in-window 2026 in-domain FastAPI+PostgreSQL+SQLAlchemy+SQLModel architecture reference of the 76-pass series.
- A written record of the **3.8-year-old repo with in-window push = active 2026 maintainer of the entire LE31 v1 stack from before LE31's charter date** = strong adoption signal.
- A written record of the **in-domain restaurant-vertical primitive** = the *Demo-API-with-one-route-that-takes-a-datetime-string-and-returns-a-list-of-open-restaurants-if-any* posture = the *restaurant-query-as-a-service* discipline.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of `mrlonis/python-open-restaurant-fastapi` codebase (single-author 2★/1⑂ v1 polish surface; LE31 v1 has no restaurant-query-as-a-service surface today).
- Cross-pollination with the v1 charter §3.4 customer-facing-AI posture (the *in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference* surface is operator-tooling, not customer-facing).

## Description

GitHub `mrlonis/python-open-restaurant-fastapi` (MIT, 2★/1⑂, Python, pushed 2026-10-09T11:25:37Z, created 2022-12-07T03:24:31Z = 3.8-year-old repo with in-window push = active 2026 maintainer, 2620 KB modest, default_branch=`main`, archived=`False`).

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **Demo API, written in Python FastAPI, with one route that takes a datetime string and returns a list of open restaurants, if any** — the *restaurant-query-as-a-service primitive* that takes a datetime string + returns a list of open restaurants.
2. **FastAPI** = LE31 v1 uses FastAPI ✓ **ON-STACK**
3. **PostgreSQL** = LE31 v1 uses Postgres in production ✓ **ON-STACK**
5. **SQLAlchemy** = LE31 v1 uses SQLModel (built on top of SQLAlchemy) ✓ **ON-STACK**
6. **SQLModel** = LE31 v1 uses SQLModel ✓ **ON-STACK**
7. **Python** = LE31 v1 uses Python ✓ **ON-STACK**
8. **5/5 LE31 v1 backend stack primitives matched** = the strongest in-window 2026 in-domain FastAPI+PostgreSQL+SQLAlchemy+SQLModel architecture reference of the 76-pass series.
9. **3.8-year-old repo with in-window push = active 2026 maintainer** = strong adoption signal.

**The 1:1 mapping onto LE31 surface:**

| open-restaurant-fastapi-primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Demo API + one route + datetime + returns list of open restaurants | (LE31 v1 has no restaurant-query-as-a-service surface) | n/a | **Not implemented** — v1 polish surface |
| FastAPI | (LE31 v1 uses FastAPI) | §3.1 ✓ | **Implemented (v1)** |
| PostgreSQL | (LE31 v1 uses Postgres in production) | §3.1 ✓ | **Implemented (v1)** |
| SQLAlchemy | (LE31 v1 uses SQLModel which is built on top of SQLAlchemy) | §3.1 ✓ | **Implemented (v1)** |
| SQLModel | (LE31 v1 uses SQLModel) | §3.1 ✓ | **Implemented (v1)** |
| Python | (LE31 v1 uses Python) | §3.1 ✓ | **Implemented (v1)** |
| 3.8-year-old repo with in-window push | (n/a — measure of adoption not stack-shape) | n/a | Sister-shape |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that introduces a restaurant-query-as-a-service surface for the LE31 single-restaurant Swiss kitchen), the implementation would add:

1. A new `RestaurantQuery` SQLModel table (Alembic migration) with columns: `id` (UUID), `restaurant_id` (UUID FK), `query_datetime` (timezone-aware datetime), `result_open` (bool), `result_restaurants` (JSON), `created_at` (timezone-aware).
2. A new `RestaurantHours` SQLModel table (Alembic migration) with columns: `id` (UUID), `restaurant_id` (UUID FK), `open_time` (timezone-aware datetime), `close_time` (timezone-aware datetime), `day_of_week` (int enum: 0-6), `created_at`, `updated_at`.
3. An Alembic migration that adds the new tables.
4. A `RestaurantQueryService` service that takes a datetime string + returns a list of open restaurants.
5. A `RestaurantHoursManager` service that manages restaurant open/close hours per day-of-week.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires:

**For v1 in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference surface** (if approved):
1. Add new `RestaurantQuery` SQLModel table (Alembic migration).
2. Add new `RestaurantHours` SQLModel table (Alembic migration).
3. Add Alembic migration for the new tables.
4. Add a `RestaurantQueryService` service that takes a datetime string + returns a list of open restaurants.
5. Add a `RestaurantHoursManager` service that manages restaurant open/close hours per day-of-week.
6. Add a `/api/open-restaurants` FastAPI endpoint that takes a `datetime` query parameter + returns a JSON list of open restaurants.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires, the v1 in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference surface would add **a v1 cook-Telegram-restaurant-query primitive** (e.g., the cook Telegram bot queries `/api/open-restaurants` and receives formatted restaurant-query messages). The cook-Telegram-restaurant-query primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 53/66 (offline-first).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; `mrlonis/python-open-restaurant-fastapi` stack is Python + FastAPI + PostgreSQL + SQLAlchemy + SQLModel which is 5/5 on-§3.1).
- **External**: None.
- **Internal**: §3.1 (Python+FastAPI+SQLAlchemy+Postgres+SQLModel on-§3.1); §3.2 (MIT permissive on-§3.2); §3.4 (no customer-facing AI on-§3.4).
- **Trigger dependency**: future v1 PR that introduces a restaurant-query-as-a-service surface for the LE31 single-restaurant Swiss kitchen.

## Open questions

- **Q1**: When (if ever) will LE31 introduce a restaurant-query-as-a-service surface? The v1 charter explicitly uses waiter web UI + cook Telegram bot + owner-daily-recap; the restaurant-query-as-a-service primitive is a v1 polish surface.
- **Q2**: If the restaurant-query-as-a-service surface lands, will it use `mrlonis/python-open-restaurant-fastapi` or hand-rolled? The `mrlonis/python-open-restaurant-fastapi` approach is the *Demo-API-with-one-route + datetime + list-of-open-restaurants* primitive; the *hand-rolled* approach is the *start-from-zero* primitive.
- **Q3**: Will the *FastAPI + PostgreSQL + SQLAlchemy + SQLModel* posture align with LE31 v1's existing `audit_logs` schema? The *FastAPI + PostgreSQL + SQLAlchemy + SQLModel* posture IS the *inherit-the-existing-FastAPI+PostgreSQL+SQLAlchemy+SQLModel* invariant applied to the *restaurant-query-as-a-service* dimension.
- **Q4**: How will the *restaurant-query-as-a-service* posture interact with LE31 v1's existing schema? The *restaurant-query-as-a-service* posture IS the *in-domain-restaurant-query-as-a-service* invariant applied to the *datetime + list-of-open-restaurants* dimension.

## Why this matters

The **`Demo-API-written-in-Python-FastAPI-with-one-route-that-takes-a-datetime-string-and-returns-a-list-of-open-restaurants-if-any + FastAPI + PostgreSQL + Python + SQLAlchemy + SQLModel`** sextuple-primitive is the **strongest direct LE31 v1 in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference of the 76-pass series** for three reasons:

1. **The 5/5 LE31 v1 backend stack primitives matched is the canonical in-domain FastAPI+PostgreSQL+SQLAlchemy+SQLModel posture**: when LE31 v1 introduces an in-domain restaurant-query-as-a-service surface (e.g., a v1 surface that lets the cook query a datetime + see which restaurants are open), the FastAPI+PostgreSQL+Python+SQLAlchemy+SQLModel substrate is the existing v1 stack.
2. **The Demo-API + one route + datetime + returns list of open restaurants quintuple-primitive is the unique in-domain restaurant-query-as-a-service discipline of the 76-pass series**: the *restaurant-query-as-a-service* posture IS the *in-domain-restaurant-vertical* discipline applied to the *Demo-API + one route + datetime + list-of-open-restaurants* dimension.
3. **The 3.8-year-old repo with in-window push = active 2026 maintainer of the entire LE31 v1 stack from before LE31's charter date**: the maintainer has shipped a 2★/1⑂ in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference from 2022-12-07 = 3.8-year-old repo with in-window push on 2026-10-09 = strong adoption of the in-domain FastAPI+PostgreSQL+SQLAlchemy+SQLModel discipline is real, observable, and growing.

Sister-shape to features 158 (`ppfenning/coxswain-graphs` = interactive-graph-explorer + FastAPI + HTMX + WebSocket + pydantic + Plotly) + 247 (`graydragon2-mortgage-intelligence-web-public` = MIT + SQLModel + FastAPI + HTMX + multi-tenant SaaS) + 295 (`23f3000434/CakeShopManagement` = artisanal-bakery-operations POS + Flask + React 19 + Aiven-PostgreSQL) + 297 (`jonalemndi2/ALdia` = open-source-business-engine + AI-agents + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country) + 298 (`erhatechnologiesai/point-of-sale-system` = cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt + customer-loyalty + FastAPI + Pydantic + SQLite). The `mrlonis/python-open-restaurant-fastapi` pattern is the **strongest direct in-domain restaurant-query-as-a-service + FastAPI + PostgreSQL + Python + SQLAlchemy + SQLModel primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that introduces a restaurant-query-as-a-service surface for the LE31 single-restaurant Swiss kitchen.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/158-ppfenning-coxswain-graphs-…md` — interactive-graph-explorer + FastAPI + HTMX + WebSocket + pydantic + Plotly (sister-shape)
- `features/247-graydragon2-mortgage-intelligence-web-public-…md` — MIT + SQLModel + FastAPI + HTMX + multi-tenant SaaS (sister-shape)
- `features/295-23f3000434-CakeShopManagement-…md` — artisanal-bakery-operations POS + Flask + React 19 + Aiven-PostgreSQL (sister-shape)
- `features/297-jonalemndi2-ALdia-…md` — open-source-business-engine + AI-agents + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country (sister-shape)
- `features/298-erhatechnologiesai-point-of-sale-system-…md` — cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt + customer-loyalty + FastAPI + Pydantic + SQLite (sister-shape)

---

**Parent research issue**: [linear: blocked] (parent fallback at `/opt/data/le31-daily-research-2026-10-15.linear-fallback.json`).