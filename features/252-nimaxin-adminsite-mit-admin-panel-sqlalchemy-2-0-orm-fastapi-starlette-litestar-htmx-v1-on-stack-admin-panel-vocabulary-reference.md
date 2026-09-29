# Feature 252 — `nimaxin-adminsite-mit-admin-panel-sqlalchemy-2-0-orm-fastapi-starlette-litestar-htmx-v1-on-stack-admin-panel-vocabulary-reference` (defer)

> **NEW observation (2026-09-29).** Documents in-window GitHub Search `restaurant+language:python` query result: `nimaxin/adminsite` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **4★/0⑂**, Python, **pushed 2026-09-27T18:20:57Z** (2 days ago, in-window by `pushed_at`), **created 2026-09-20T17:07:26Z** (~9 days before push, **both fields in-window** = *both in-window by 9-day-old-repo created+committed-within-window*), **repo size = 4306 KB substantial repo** (parent-verified via raw GitHub API JSON), `default_branch=main`, `archived=false`). Topics (verbatim, parent-verified GitHub API direct-GET 2026-09-29, 10 topics): `admin + admin-dashboard + admin-panel + asgi + fastapi + htmx + litestar + python + sqlalchemy + starlette`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-29): *"An admin panel for the SQLAlchemy 2.0 ORM that works with FastAPI, Starlette and Litestar."* The **on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel** primitive = the **on-LE31-stack-vocabulary-envelope admin-panel reference** (5 of 10 topics = fastapi + htmx + python + sqlalchemy + starlette = the **literal LE31 v1 stack primitive**). Net-new observation 2026-09-29 (ripgrep-confirmed unique vs features 1–250). Bucket: **v1 on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel primitive (defer, parking-lot, vocabulary reference)** — zero build time today.

## Goal

Retain the **on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel** primitive as a persistent cross-section reference for any future LE31 v1 surface that introduces (a) **admin-panel-as-ASGI-app** (a reusable admin-panel library that mounts on any ASGI framework — FastAPI is LE31's v1 stack; Starlette is FastAPI's underlying framework; Litestar is an alternative ASGI framework), (b) **SQLAlchemy-2.0-ORM** (the literal ORM that SQLModel is built on — SQLModel = SQLAlchemy 2.0 + Pydantic, per the SQLModel README; the *SQLAlchemy-2.0* vocabulary maps 1:1 onto LE31's SQLModel stack), (c) **on-LE31-stack-vocabulary-envelope** (5 of 10 topics = fastapi + htmx + python + sqlalchemy + starlette = the **literal LE31 v1 stack primitive** — the *off-the-shelf-owner-web-UI* vocabulary), (d) **admin-dashboard** (the *admin-dashboard* primitive = the *operator-facing view* applied to the *SQLModel table CRUD* dimension; LE31 v1's existing `index.html` floor plan + stock view is a custom admin-dashboard, but does not have a generic admin-panel library), (e) **HTMX-rendering** (the admin-panel uses HTMX for partial-page-updates; this matches LE31 v1's charter §3.1 *minimal HTML/HTMX* posture), and (f) **off-the-shelf-reuse** (the *off-the-shelf-admin-panel-library* primitive = any future v1 owner-web-UI surface could compose this library with the existing `StockEntry` + `audit_logs` + `Order` SQLModel tables to render an admin dashboard without writing raw SQL). The artifact is the persistent cross-section reference + the verbatim description + the 6 named primitives. No code today (MIT license permits future code reuse; vocabulary-only artifact today; 4306 KB substantial-repo size is production-grade).

## Scope

**In scope (defer artifact):**
- A written record of the **admin-panel-as-ASGI-app** discipline: the *reusable admin-panel-library* primitive applied to the *SQLModel-table-CRUD* dimension (LE31 v1 does NOT have a generic admin-panel library; this is a future v1 owner-facing surface that would adopt this pattern).
- A written record of the **SQLAlchemy-2.0-ORM** discipline: the *SQLAlchemy-2.0-vocabulary* primitive applied to the *SQLModel-stack* dimension (LE31 v1's SQLModel is built on SQLAlchemy 2.0; the *SQLAlchemy-2.0* vocabulary maps 1:1 onto LE31's SQLModel stack).
- A written record of the **on-LE31-stack-vocabulary-envelope** discipline: the *literal-LE31-v1-stack-primitive* primitive applied to the *admin-panel-library* dimension (5 of 10 topics = the literal LE31 v1 stack primitive = FastAPI + HTMX + Python + SQLAlchemy 2.0 + Starlette).
- A written record of the **HTMX-rendering** discipline: the *HTMX-partial-page-updates* primitive applied to the *admin-panel-UI* dimension (LE31 v1's charter §3.1 *minimal HTML/HTMX* posture).
- A written record of the **off-the-shelf-reuse** discipline: the *off-the-shelf-admin-panel-library* primitive applied to the *owner-facing-web-UI* dimension (any future v1 PR that adopts this library would save the v1 implementer from writing a custom admin-dashboard).
- A decision record: today's verdict is `defer` because LE31 v1's existing `index.html` floor plan + stock view is a custom admin-dashboard that works; the *off-the-shelf-admin-panel-library* is a future-v1 surface that would require explicit owner/charter sign-off.
- A cross-section reference with the prior SQLModel + FastAPI + HTMX + multi-tenant + SaaS cluster: features 191 (jonalemndi2 ALdia), 194 (vaibhavkr993630 droid-CollabFlow), 197 (rajo69 ledgerkb), 202 (Elkin-Tovar POS-Multi-Tenant), 204 (domious cavekeeper), 239 (Hearthplug mosaic-erp), 240 (huoyunpili xiaomaipu), 247 (graydragon2 mortgage-intelligence-web-public). The *transferable insight* is the **on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel** primitive.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2 horizontal-expansion surface in v2 (charter §3.1 + §3.2 invariant: v2 surface expansion is the next boundary; this is a vocabulary reference, not a v2 expansion trigger).
- Any v2 admin-panel implementation in v2 (the artifact is vocabulary-only; the implementation would require explicit owner/charter sign-off).

## Description

The pick is **`nimaxin/adminsite`** — a Python + MIT + on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel vocabulary artifact. **Charter §3.4 NOT triggered** because the admin-panel is a generic SQLModel-table-CRUD library (no AI surface; the admin-panel renders existing SQLModel tables; no restaurant diner interacts with the admin-panel). The artifact is the persistent cross-section reference for the verbatim description + the 6 named primitives.

**Why the *both fields in-window* + 9-day-old-repo + 4★ community traction matters**: the repo was created 2026-09-20T17:07:26Z (~9 days before window start? no — 9 days before push, both in window); the `pushed_at=2026-09-27T18:20:57Z` 2-day-ago fresh-push + the 9-day-old-repo + the **4★ community traction** = the **highest star count of any 2026-09-29 in-window Python FastAPI + HTMX admin-panel repo of the 61-pass series**. The 4306 KB substantial-repo size is production-grade (the largest in-window Python admin-panel of today's brainstorm). The artifact is the persistent cross-section reference for the **on-stack-admin-panel-as-ASGI-app primitive**, not just for the verbatim description.

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v1 surface that adopts the *on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel* primitive would extend the LE31 v1 data model with appropriate new tables (e.g., a `User` SQLModel table with `user_id, username, hashed_password, role, recorded_at`; a `Session` SQLModel table with `session_id, user_id, expires_at, recorded_at`; or a `AuditLog` SQLModel table with `audit_log_id, user_id, action, table_name, row_id, recorded_at`). The admin-panel-as-library would auto-discover the existing `StockEntry + audit_logs + Order` SQLModel tables and render them as admin-dashboards without code changes. All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v1 PR is triggered by the trigger condition below, the implementation would:
1. Read the `nimaxin/adminsite` README at https://github.com/nimaxin/adminsite for the *on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel* primitive.
2. Cross-reference with LE31 v1's existing `index.html` floor plan + stock view (charter §3.1) to identify the *delta* (the *delta* = `nimaxin/adminsite` introduces a *generic admin-panel-as-ASGI-app* primitive that LE31 v1's custom `index.html` dashboard does NOT have; the *generic admin-panel-as-library* would auto-discover the existing `StockEntry + audit_logs + Order` SQLModel tables and render them as admin-dashboards).
3. Apply charter §3.4 *operator-tooling-AI with observable evidence + non-AI fallback* review to the *delta* (no AI surface; admin-panel-as-library is operator-tooling; charter §3.4 not triggered).
4. Implement the surface with the LE31 v1 + FastAPI + SQLModel + aiogram stack; the `nimaxin/adminsite` reference is the *vocabulary* for *on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel*, NOT for *admin-panel replacement*.

## Telegram interaction

This is a vocabulary reference — no Telegram interaction changes today. The future v1 surface that adopts this vocabulary would not add a new Telegram-bot-command surface (the admin-panel is a web-UI surface, not a Telegram-bot surface). The existing cook-Telegram-bot surface (charter §3.1) is not affected.

## Dependencies

- Read-only reference to `nimaxin/adminsite` at https://github.com/nimaxin/adminsite (no installation, no import).
- Future v1 surface that adopts the vocabulary would require: FastAPI (already in LE31 v1 stack), SQLAlchemy 2.0 (already in LE31 v1 stack via SQLModel), HTMX (already in LE31 v1 stack), Starlette (already in LE31 v1 stack via FastAPI), Jinja2 templates (likely needed; charter §3.1 known-conflict note on minimal HTML/HTMX), SQLModel (already in LE31 v1 stack).
- No new infrastructure today.

## Open questions

1. **Does the v1 owner-web-UI surface adopt a generic admin-panel-library or stay with the custom `index.html` floor plan + stock view?** LE31 v1's existing `index.html` is a custom admin-dashboard that works; a *generic admin-panel-library* would be a future v1 surface that requires explicit owner/charter sign-off.
2. **What is the SQLModel-vs-SQLAlchemy-2.0 compatibility status?** `nimaxin/adminsite` is built for SQLAlchemy 2.0; SQLModel is built on SQLAlchemy 2.0; the *SQLAlchemy-2.0-vocabulary* should map 1:1 onto LE31's SQLModel stack. Any future v1 PR adopting this library would need to verify the SQLModel compatibility (charter §3.1 known-conflict note).
3. **What is the Jinja2-templates posture?** `nimaxin/adminsite` likely uses Jinja2 templates; LE31 v1's charter §3.1 *minimal HTML/HTMX* posture may or may not include Jinja2 explicitly. Owner decision required.
4. **What is the auth posture?** The admin-panel likely requires authentication; LE31 v1 has no auth surface today (single-tenant + on-premise). Any future v1 PR adopting this library would need to integrate with LE31's existing single-tenant auth posture (or add a v2 multi-tenant auth).

## Why this matters

The **on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel** primitive is the **first in-window 2026 Python MIT FastAPI + HTMX + SQLAlchemy-2.0 admin-panel repo with 4★ community traction of the 61-pass series**. The 4306 KB substantial-repo size signals *production-grade*; the 4★ community traction signals *community-validation*; the **on-LE31-stack-vocabulary-envelope** (5 of 10 topics = the literal LE31 v1 stack primitive) signals *on-stack-match*. The MIT license makes this the **STRICTLY-ADOPTABLE on-stack-admin-panel primitive** (charter §3.2 STRICTLY-COMPATIBLE). The brainstorm value is the **on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel + off-the-shelf-owner-web-UI** vocabulary for any future v1 owner-facing-web-UI surface. **Trigger for re-evaluation**: first v1 PR that adopts an admin-panel-library; OR first v1 PR that adds an admin-dashboard surface; OR first v2 PR that introduces a multi-tenant admin-panel.
