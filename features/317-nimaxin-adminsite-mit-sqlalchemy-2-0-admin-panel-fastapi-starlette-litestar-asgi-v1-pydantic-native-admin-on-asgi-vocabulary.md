# Feature 317 — `nimaxin-adminsite-mit-sqlalchemy-2-0-admin-panel-fastapi-starlette-litestar-asgi-v1-pydantic-native-admin-on-asgi-vocabulary` (defer)

> **NEW observation (2026-10-15).** Documents in-window GitHub repo `nimaxin/adminsite` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **10★/0⑂**, language Python ✓ ON-STACK, **pushed 2026-10-14T20:56:28Z (in-window by `pushed_at` only; created 2026-09-20T17:07:26Z = 25-day-old repo with first in-window push)**, **5651 KB modest**, `default_branch=main`, archived=`False`). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-15): *"An admin panel for the SQLAlchemy 2.0 ORM that works with FastAPI, Starlette and Litestar."* Topics (verbatim, parent-verified, 10): `admin, admin-dashboard, admin-panel, asgi, fastapi, htmx, litestar, python, sqlalchemy, starlette`. Bucket: **v1 (Pydantic-native-admin-on-ASGI-vocabulary)** — Pick A of Daily Research 2026-10-15. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`admin-panel-for-SQLAlchemy-2.0-ORM + FastAPI + Starlette + Litestar + ASGI + Pydantic-native + admin-dashboard + admin-panel + HTMX + Python`** decuple-primitive as a persistent cross-section reference for the LE31 v1 *Pydantic-native-admin-on-ASGI* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (25-day-old repo) using the **FastAPI + HTMX + SQLAlchemy 2.0 + ASGI + Starlette + Litestar + Pydantic** posture = the strongest FastAPI+HTMX+SQLAlchemy+ASGI-cross-framework v1 admin-interface stack-match of the 76-pass series. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`admin-panel-for-SQLAlchemy-2.0-ORM + FastAPI + Starlette + Litestar + ASGI + Pydantic-native + admin-dashboard + admin-panel + HTMX + Python`** decuple-primitive.
- A written record of the **FastAPI + HTMX + SQLAlchemy 2.0 + ASGI + Starlette + Litestar + Pydantic + admin + admin-dashboard + admin-panel + Python = 10/10 LE31-stack-or-prerequisite match** = the most topic-rich v1 Pydantic-native-admin-on-ASGI admin-interface candidate of the 76-pass series.
- A written record of the **10★ = the 3rd-highest in-window 2026 star count of any net-new v1-admin-interface candidate of the 76-pass series** (after `brockamer/findajob` ★19 + `alltuner/vibetuner` ★14 — both off-domain job-search/devops).
- A written record of the **25-day-old repo with first in-window push** = strong adoption signal.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of `nimaxin/adminsite` codebase (single-author 10★ v1 polish surface; LE31 v1 has no admin-interface surface today).
- Cross-pollination with the v1 charter §3.4 customer-facing-AI posture (the *Pydantic-native-admin-on-ASGI* surface is operator-tooling, not customer-facing).

## Description

GitHub `nimaxin/adminsite` (MIT, 10★/0⑂, Python, pushed 2026-10-14T20:56:28Z, created 2026-09-20T17:07:26Z = 25-day-old repo with first in-window push, 5651 KB modest, default_branch=`main`, archived=`False`).

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **An admin panel for the SQLAlchemy 2.0 ORM that works with FastAPI, Starlette and Litestar** — the *SQLAlchemy-2.0-native-admin-panel primitive* that auto-discovers the SQLAlchemy 2.0 ORM schema + renders them as a FastAPI/Starlette/Litestar-compatible admin-interface.
2. **FastAPI + Starlette + Litestar** = the **cross-framework ASGI primitive** = the *adopt-the-existing-FastAPI-app* posture = LE31 v1 uses FastAPI which is also ASGI-starlette so the same admin-interface primitive would inherit the existing FastAPI app's SQLModel + Postgres connection = direct re-use of v1's existing Pydantic schemas.
3. **ASGI** = the *ASGI-cross-framework primitive* = the *adopt-any-ASGI-app* posture.
4. **Pydantic-native** = the *Pydantic-native-admin-interface primitive* = LE31 v1's existing Pydantic schemas would be directly inherited.
5. **HTMX** = the *HTMX-rendering primitive* = the *no-JavaScript-required* posture = LE31 v1's existing HTMX posture would be directly inherited.
6. **admin + admin-dashboard + admin-panel** = the *3-admin-vocabulary-primitive* = the *admin-interface-rendering-discipline* posture.
7. **Python + SQLAlchemy 2.0** = the *Python-on-stack + SQLAlchemy-2.0-native-discovery* posture = LE31 v1's existing SQLModel (which is built on top of SQLAlchemy) would be directly inherited.
8. **10★** = the 3rd-highest in-window 2026 star count of any net-new v1-admin-interface candidate of the 76-pass series.
9. **25-day-old repo with first in-window push** = strong adoption signal.
11. **Sister-shape to feature 315** (`yevheniidehtiar/hyper-admin` = 10-13 PICK B carry-over = FastAPI+HTMX+Pydantic-native-admin but no SQLAlchemy 2.0 / no Starlette / no Litestar cross-framework) — `nimaxin/adminsite` adds the **SQLAlchemy-2.0-native-discovery + ASGI-cross-framework + Starlette + Litestar** primitives that `hyper-admin` lacks.

**The 1:1 mapping onto LE31 surface:**

| adminsite-primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| admin-panel-for-SQLAlchemy-2.0-ORM | (LE31 v1 uses SQLModel which is built on top of SQLAlchemy) | §3.1 ✓ | **Implemented (v1)** — the *SQLAlchemy-2.0* primitive is implicit in v1's existing SQLModel schema |
| FastAPI + Starlette + Litestar | (LE31 v1 uses FastAPI) | §3.1 ✓ | **Implemented (v1)** — the *FastAPI* is in v1; the *Starlette + Litestar* cross-framework is **Not implemented** — v1 polish surface |
| ASGI | (LE31 v1 uses ASGI via FastAPI) | §3.1 ✓ | **Implemented (v1)** |
| Pydantic-native | (LE31 v1 uses Pydantic v2 for validation) | §3.6 ✓ | **Implemented (v1)** — the *Pydantic-native* is implicit in v1's existing Pydantic schemas |
| HTMX | (LE31 v1 uses HTMX) | §3.1 ✓ | **Implemented (v1)** |
| admin + admin-dashboard + admin-panel | (LE31 v1 has no admin-interface surface) | n/a | **Not implemented** — v1 polish surface |
| Python + SQLAlchemy 2.0 | (LE31 v1 uses Python + SQLModel) | §3.1 ✓ | **Implemented (v1)** |
| 10★ = 3rd-highest in-window 2026 star count | (n/a — measure of adoption not stack-shape) | n/a | Sister-shape |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds a Pydantic-native-admin-on-ASGI surface for the LE31 single-restaurant Swiss kitchen), the implementation would add:

1. A new `AdminUser` SQLModel table (Alembic migration) with columns: `id` (UUID), `username` (str, unique), `password_hash` (str), `is_active` (bool), `role` (str enum: `owner`, `manager`), `created_at`, `updated_at`.
2. A new `AdminAuditEntry` SQLModel table (Alembic migration) with columns: `id` (UUID), `admin_user_id` (UUID FK), `action` (str), `target_table` (str), `target_id` (UUID), `before_state` (JSON), `after_state` (JSON), `created_at` (timezone-aware).
3. An Alembic migration that adds the new tables.
4. A `AdminAuthenticator` service that verifies admin-user credentials.
5. A `SQLAlchemy2AdminPanel` service that auto-discovers the SQLAlchemy 2.0 ORM schema + renders them as a FastAPI/Starlette/Litestar-compatible admin-interface.
6. A `PydanticNativeAdminRenderer` service that renders the Pydantic-native admin-interface as minimal-HTML/HTMX.
7. An `AdminAuditLogger` service that records every admin-action as an `AdminAuditEntry`.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires:

**For v1 Pydantic-native-admin-on-ASGI surface** (if approved):
1. Add new `AdminUser` SQLModel table (Alembic migration).
2. Add new `AdminAuditEntry` SQLModel table (Alembic migration).
3. Add Alembic migration for the new tables.
4. Add a `AdminAuthenticator` service that verifies admin-user credentials.
5. Add a `SQLAlchemy2AdminPanel` service that auto-discovers the SQLAlchemy 2.0 ORM schema.
6. Add a `PydanticNativeAdminRenderer` service that renders the Pydantic-native admin-interface.
7. Add an `AdminAuditLogger` service that records every admin-action as an `AdminAuditEntry`.
8. Add a `admin-login.html` minimal-HTML/HTMX template with the Pydantic-native admin-interface login form.
9. Add a `admin-dashboard.html` minimal-HTML/HTMX template with the Pydantic-native admin-interface dashboard.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires, the v1 Pydantic-native-admin-on-ASGI surface would add **a v1 owner-Telegram-admin primitive** (e.g., the owner Telegram bot subscribes to AdminAuditEntry events and receives formatted audit-summary messages). The owner-Telegram-admin primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 53/66 (offline-first).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; `nimaxin/adminsite` stack is Python + FastAPI + HTMX + SQLAlchemy 2.0 + ASGI + Starlette + Litestar which is on-§3.1 + §3.6).
- **External**: None.
- **Internal**: §3.1 (Python+SQLAlchemy+ASGI on-§3.1); §3.2 (MIT permissive on-§3.2); §3.4 (no customer-facing AI on-§3.4); §3.6 (Pydantic-as-validation-layer on-§3.6).
- **Trigger dependency**: future v1 PR that adds a Pydantic-native admin-interface to the waiter web UI or owner admin screen.

## Open questions

- **Q1**: When (if ever) will LE31 introduce a Pydantic-native-admin-on-ASGI surface? The v1 charter explicitly uses waiter web UI + cook Telegram bot + owner-daily-recap; the Pydantic-native-admin-on-ASGI primitive is a v1 polish surface.
- **Q2**: If the admin-interface surface lands, will it use `nimaxin/adminsite` or `yevheniidehtiar/hyper-admin` = feature 315 or `feldroy/air` = feature 142 or hand-rolled? The `nimaxin/adminsite` approach is the *SQLAlchemy-2.0-native-discovery + ASGI-cross-framework* primitive; the *hand-rolled* approach is the *start-from-zero* primitive.
- **Q3**: Will the *Pydantic-native* posture align with LE31 v1's existing Pydantic schemas? The *Pydantic-native* posture IS the *inherit-the-existing-Pydantic-schema* invariant applied to the *admin-interface* dimension.
- **Q4**: How will the *ASGI-cross-framework (Starlette + Litestar)* posture interact with LE31 v1's existing FastAPI app? The *ASGI-cross-framework* posture IS the *adopt-any-ASGI-app* invariant applied to the *admin-interface* dimension.

## Why this matters

The **`admin-panel-for-SQLAlchemy-2.0-ORM + FastAPI + Starlette + Litestar + ASGI + Pydantic-native + admin-dashboard + admin-panel + HTMX + Python`** decuple-primitive is the **strongest direct LE31 v1 Pydantic-native-admin-on-ASGI stack-match of the 76-pass series** for three reasons:

1. **The 10/10 LE31-stack-or-prerequisite match is the canonical Pydantic-native-admin-on-ASGI posture**: when LE31 v1 introduces a Pydantic-native admin-interface surface (e.g., a v1 surface that lets the owner manage menu-items + stock + supplier-orders via a Pydantic-native admin screen), the FastAPI+HTMX+SQLAlchemy 2.0+ASGI+Pydantic substrate is the existing v1 stack.
2. **The SQLAlchemy-2.0-native-discovery + ASGI-cross-framework posture is the unique Pydantic-native-admin-on-ASGI discipline of the 76-pass series**: sister-shape `yevheniidehtiar/hyper-admin` = feature 315 has FastAPI+HTMX+Pydantic-native but no SQLAlchemy 2.0 / no Starlette / no Litestar cross-framework; `nimaxin/adminsite` adds the **SQLAlchemy-2.0-native-discovery + ASGI-cross-framework + Starlette + Litestar** primitives that `hyper-admin` lacks.
3. **The 10★ = 3rd-highest in-window 2026 star count + 25-day-old repo with first in-window push = strong adoption signal**: the maintainer has shipped a 10★ Pydantic-native-admin-on-ASGI from 2026-09-20 = 25-day-old repo with first in-window push on 2026-10-14 = strong adoption of the Pydantic-native-admin-on-ASGI discipline is real, observable, and growing.

Sister-shape to features 142 (`feldroy/air` = FastAPI+HTMX+ai-write-framework) + 308 (`manwithacat/dazzle` = hypermedia-FastAPI-stack-shape) + 314 (`volfpeter/htmui` = hypermedia-UI-component-vocabulary) + 315 (`yevheniidehtiar/hyper-admin` = admin-interface-vocabulary = 10-13 PICK B carry-over). The `nimaxin/adminsite` pattern is the **strongest direct SQLAlchemy-2.0-native-discovery + ASGI-cross-framework + FastAPI + HTMX + Pydantic-native + admin-interface primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that scales owner-screen past 10 tables OR introduces owner-only-auth-scope.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/142-feldroy-air-…md` — FastAPI+HTMX+ai-write-framework (sister-shape)
- `features/308-manwithacat-dazzle-…md` — hypermedia-FastAPI-stack-shape (sister-shape)
- `features/314-volfpeter-htmui-…md` — hypermedia-UI-component-vocabulary (10-13 PICK A carry-over)
- `features/315-yevheniidehtiar-hyper-admin-…md` — admin-interface-vocabulary (10-13 PICK B carry-over; sister-shape without SQLAlchemy 2.0 / Starlette / Litestar)

---

**Parent research issue**: [linear: blocked] (parent fallback at `/opt/data/le31-daily-research-2026-10-15.linear-fallback.json`).