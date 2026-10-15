# Feature 315 — `yevheniidehtiar-hyper-admin-mit-pydantic-native-admin-fastapi-htmx-v1-admin-interface-vocabulary` (defer)

> **NEW observation (2026-10-15).** Documents 10-13 daily-research PICK B carry-over (was promised in 2026-10-13 report's INDEX-narrative truth but the actual feature file was never written; today's pass closes the INDEX-vs-on-disk gap). GitHub `yevheniidehtiar/hyper-admin` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **5★/2⑂**, language Python ✓ ON-STACK, **pushed 2026-10-11T20:23:58Z**, **created 2025-08-22T19:51:14Z = ~14-month-old repo with in-window push**, **4464 KB modest**, `default_branch=develop`, archived=`False`). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-15): *"A modern, Pydantic-native admin interface for FastAPI, powered by HTMX."* Topics (verbatim, parent-verified, NO topics listed — description-only metadata). Bucket: **v1 (admin-interface-vocabulary)** — Pick B of Daily Research 2026-10-13 carry-over. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`modern + Pydantic-native + admin-interface + FastAPI + HTMX`** quadruple-primitive as a persistent cross-section reference for the LE31 v1 *Pydantic-native admin-interface* wedge, and document the **FastAPI + HTMX + Pydantic-native = 3/3 LE31-stack-match** validation that an independent maintainer arrived at in 2026 (14-month-old repo). The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`modern + Pydantic-native + admin-interface + FastAPI + HTMX`** quadruple-primitive.
- A written record of the **FastAPI + HTMX + Pydantic-native = 3/3 LE31-stack-match** = the strongest in-window 2026 v1 Pydantic-native admin-interface stack-match of the 75-pass series.
- A written record of the **5★/2⑂ = 2.4 forks per star** = strong fork-to-star ratio = active downstream-fork adoption = consumption-over-popularity signal.
- A written record of the **~14-month-old repo with in-window push** = active 2026 maintainer of the Pydantic-native admin-interface primitive from before LE31 v1's charter date.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of `yevheniidehtiar/hyper-admin` codebase (single-author 5★ v1 polish surface; LE31 v1 has no admin-interface surface today).
- Cross-pollination with the v1 charter §3.4 customer-facing-AI posture (the *Pydantic-native-admin-interface* surface is operator-tooling, not customer-facing).

## Description

GitHub `yevheniidehtiar/hyper-admin` (MIT, 5★/2⑂, Python, pushed 2026-10-11T20:23:58Z, created 2025-08-22T19:51:14Z = ~14-month-old repo with in-window push, 4464 KB modest, default_branch=`develop`, archived=`False`).

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **A modern, Pydantic-native admin interface for FastAPI, powered by HTMX** — the *Pydantic-native-admin-interface primitive* on top of FastAPI + HTMX.
2. **FastAPI + HTMX + Pydantic-native = 3/3 LE31-stack-match** = the strongest in-window 2026 v1 Pydantic-native admin-interface stack-match of the 75-pass series (vs `feldroy/air` = feature 142 = FastAPI+HTMX+ai-write-framework not admin-specific).
3. **NO topics listed (description-only metadata)** = the metadata is description-driven = the owner is focused on the *product* not the *topic-tagging*.
4. **5★/2⑂ = 2.4 forks per star** = strong fork-to-star ratio = active downstream-fork adoption = consumption-over-popularity signal.
5. **~14-month-old repo with in-window push** = active 2026 maintainer of the Pydantic-native admin-interface primitive.

**The 1:1 mapping onto LE31 surface:**

| hyper-admin-primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| modern + Pydantic-native | (LE31 v1 uses Pydantic v2 for validation) | §3.6 ✓ | **Implemented (v1)** — the *Pydantic-native* is implicit in v1's existing Pydantic schemas |
| admin-interface | (LE31 v1 has no admin-interface surface) | n/a | **Not implemented** — v1 polish surface |
| FastAPI | (LE31 v1 uses FastAPI) | §3.1 ✓ | **Implemented (v1)** |
| HTMX | (LE31 v1 uses HTMX) | §3.1 ✓ | **Implemented (v1)** |
| fork-to-star 2.4 | (n/a — measure of adoption not stack-shape) | n/a | Sister-shape |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds an admin-interface surface for the LE31 single-restaurant Swiss kitchen), the implementation would add:

1. A new `AdminUser` SQLModel table (Alembic migration) with columns: `id` (UUID), `username` (str, unique), `password_hash` (str), `is_active` (bool), `role` (str enum: `owner`, `manager`), `created_at`, `updated_at`.
2. A new `AdminAuditEntry` SQLModel table (Alembic migration) with columns: `id` (UUID), `admin_user_id` (UUID FK), `action` (str), `target_table` (str), `target_id` (UUID), `before_state` (JSON), `after_state` (JSON), `created_at` (timezone-aware).
3. An Alembic migration that adds the new tables.
4. A `AdminAuthenticator` service that verifies admin-user credentials.
5. A `PydanticAdminUI` service that renders the Pydantic-native admin-interface as minimal-HTML/HTMX.
6. An `AdminAuditLogger` service that records every admin-action as an `AdminAuditEntry`.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires:

**For v1 Pydantic-native-admin-interface surface** (if approved):
1. Add new `AdminUser` SQLModel table (Alembic migration).
2. Add new `AdminAuditEntry` SQLModel table (Alembic migration).
3. Add Alembic migration for the new tables.
4. Add a `AdminAuthenticator` service that verifies admin-user credentials.
5. Add a `PydanticAdminUI` service that renders the Pydantic-native admin-interface as minimal-HTML/HTMX.
6. Add an `AdminAuditLogger` service that records every admin-action as an `AdminAuditEntry`.
7. Add a `admin-login.html` minimal-HTML/HTMX template with the Pydantic-native admin-interface login form.
8. Add a `admin-dashboard.html` minimal-HTML/HTMX template with the Pydantic-native admin-interface dashboard.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires, the v1 Pydantic-native-admin-interface surface would add **a v1 owner-Telegram-admin primitive** (e.g., the owner Telegram bot subscribes to AdminAuditEntry events and receives formatted audit-summary messages). The owner-Telegram-admin primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 53/66 (offline-first).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; `yevheniidehtiar/hyper-admin` stack is Python + FastAPI + HTMX + Pydantic which is on-§3.1 + §3.6).
- **External**: None.
- **Internal**: §3.1 (Python+FastAPI+HTMX on-§3.1); §3.2 (MIT permissive on-§3.2); §3.4 (no customer-facing AI on-§3.4); §3.6 (Pydantic-as-validation-layer on-§3.6).
- **Trigger dependency**: future v1 PR that adds a Pydantic-native admin interface to the waiter web UI or owner admin screen.

## Open questions

- **Q1**: When (if ever) will LE31 introduce an admin-interface surface? The v1 charter explicitly uses waiter web UI + cook Telegram bot + owner-daily-recap; the admin-interface primitive is a v1 polish surface.
- **Q2**: If the admin-interface surface lands, will it use `yevheniidehtiar/hyper-admin` or `feldroy/air` = feature 142 or hand-rolled? The `yevheniidehtiar/hyper-admin` approach is the *Pydantic-native-admin-interface* primitive; the *hand-rolled* approach is the *start-from-zero* primitive.
- **Q3**: Will the *Pydantic-native* posture align with LE31 v1's existing Pydantic schemas? The *Pydantic-native* posture IS the *inherit-the-existing-Pydantic-schema* invariant applied to the *admin-interface* dimension.
- **Q4**: How will the *admin-interface* posture interact with LE31 v1's existing `audit_logs` schema? The *admin-interface* posture IS the *every-admin-action-is-an-append-only-audit-log-entry* invariant applied to the *admin-user* dimension.

## Why this matters

The **`modern + Pydantic-native + admin-interface + FastAPI + HTMX`** quadruple-primitive is the **strongest direct LE31 v1 Pydantic-native admin-interface stack-match of the 75-pass series** for three reasons:

1. **The 3/3 LE31-stack-match is the canonical FastAPI+HTMX+Pydantic posture**: when LE31 v1 introduces a Pydantic-native admin-interface surface (e.g., a v1 surface that lets the owner manage menu-items + stock + supplier-orders via a Pydantic-native admin screen), the FastAPI+HTMX+Pydantic substrate is the existing v1 stack.
2. **The Pydantic-native adjective is the strongest Pydantic-native framing of any v1-admin-interface candidate of the 75-pass series**: the *Pydantic-native* posture IS the *inherit-the-existing-Pydantic-schema* invariant applied to the *admin-interface* dimension.
3. **The fork-to-star 2.4 = consumption-over-popularity signal**: the maintainer has shipped a 5★/2⑂ Pydantic-native admin-interface from 2025-08-22 = ~14-month-old repo with in-window push = strong adoption of the Pydantic-native admin-interface discipline is real, observable, and growing.

Sister-shape to features 142 (`feldroy/air` = FastAPI+HTMX+ai-write-framework) + 308 (`manwithacat/dazzle` = hypermedia-FastAPI-stack-shape) + 314 (`volfpeter/htmui` = hypermedia-UI-component-vocabulary) + 317 (`nimaxin/adminsite` = Pydantic-native-admin-on-ASGI-vocabulary = 10-15 PICK A). The `yevheniidehtiar/hyper-admin` pattern is the **strongest direct Pydantic-native + FastAPI + HTMX + admin-interface primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that scales owner-screen past 10 tables OR introduces owner-only-auth-scope.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/142-feldroy-air-…md` — FastAPI+HTMX+ai-write-framework (sister-shape)
- `features/308-manwithacat-dazzle-…md` — hypermedia-FastAPI-stack-shape (sister-shape)
- `features/314-volfpeter-htmui-…md` — hypermedia-UI-component-vocabulary (10-13 PICK A carry-over)
- `features/317-nimaxin-adminsite-…md` — Pydantic-native-admin-on-ASGI-vocabulary (10-15 PICK A)

---

**Parent research issue**: [linear: blocked] (parent fallback at `/opt/data/le31-daily-research-2026-10-15.linear-fallback.json`). Original Daily Research issue: 2026-10-13 PICK B carry-over.