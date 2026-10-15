# HANDOFF — Feature 317: `nimaxin-adminsite-mit-sqlalchemy-2-0-admin-panel-fastapi-starlette-litestar-asgi-v1-pydantic-native-admin-on-asgi-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

> **Note on filename**: the HANDOFF filename uses the full slug per the v1 feature contract shape (see `features/317-…-vocabulary.md`).

## Active feature path

`features/317-nimaxin-adminsite-mit-sqlalchemy-2-0-admin-panel-fastapi-starlette-litestar-asgi-v1-pydantic-native-admin-on-asgi-vocabulary.md` — defer/parking-lot (Pick A of Daily Research 2026-10-15).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface needs a Pydantic-native admin-interface for FastAPI + SQLAlchemy 2.0 + Starlette + Litestar + ASGI + HTMX, *the owner/waiter wants* a ready-made admin-interface that inherits the existing Pydantic schemas + can drop into existing FastAPI routes + can span ASGI cross-framework, *but struggles because* today's FastAPI+HTMX admin-frameworks either require a third-language frontend (React/Next.js) or hand-rolled CRUD templates, *so that* the admin-interface ships in 1-day of integration work instead of 1-week. |
| 2 | Viability | ✓ | Single-developer v1 surface; no specialist help needed; vocabulary-only artifact; REVERSIBLE (pure observation, zero code today). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + FastAPI ✓ ON-STACK + HTMX ✓ ON-STACK + SQLAlchemy 2.0 ✓ ON-STACK + ASGI ✓ ON-STACK + Starlette ✓ ON-STACK + Litestar ✓ ON-STACK + Pydantic ✓ ON-STACK. The 8/8 LE31-stack-match + 10 topics (admin + admin-dashboard + admin-panel + asgi + fastapi + htmx + litestar + python + sqlalchemy + starlette) = the most topic-rich Pydantic-native-admin-on-ASGI v1 admin-interface candidate of the 76-pass series. 10★ = 3rd-highest in-window 2026 star count of any net-new v1-admin-interface candidate. Rabbit hole: the *SQLAlchemy-2.0-native-discovery + ASGI-cross-framework (Starlette + Litestar)* primitives are not yet adopted by LE31 v1; the *admin-interface* primitive is a v1 polish surface. Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *SQLAlchemy-2.0 + ASGI + Starlette + Litestar + Pydantic-native* primitives are §3.1 + §3.2 + §3.4 + §3.6-aligned (Python+SQLAlchemy+ASGI+Starlette+Litestar+Pydantic + append-only-audit-log + on-premise-deployment + non-AI-fallback). No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (Pydantic-native admin-interface on waiter web UI or owner admin screen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + Pydantic schemas + SQLModel + FastAPI + HTMX waiter-web-UI) already implement the *FastAPI + HTMX + Pydantic + SQLAlchemy* discipline; the *ASGI-cross-framework + Starlette + Litestar* primitives are NEW = the reference is *naming + extending*, not just *naming*. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (the *Pydantic-native-admin-on-ASGI* primitive is a v1 polish surface; v1 charter is waiter-web-UI + cook-Telegram-bot + owner-daily-recap + append-only-StockEntry; the *Pydantic-native-admin-on-ASGI* primitive is not in v1 charter).

## Bucket

**v1** (Pydantic-native-admin-on-ASGI-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the decuple-primitive set (admin-panel + SQLAlchemy 2.0 + FastAPI + Starlette + Litestar + ASGI + Pydantic-native + admin-dashboard + admin-panel + HTMX + Python).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *Pydantic-native-admin-on-ASGI* discipline on the waiter web UI or owner admin screen lands, the files to touch are:
- `backend/alembic/versions/` — add migration for `AdminUser`, `AdminAuditEntry` tables.
- `backend/admin_user.py` — new file with `AdminAuthenticator` class.
- `backend/sqlalchemy2_admin_panel.py` — new file with `SQLAlchemy2AdminPanel` class.
- `backend/pydantic_admin_renderer.py` — new file with `PydanticNativeAdminRenderer` class.
- `backend/admin_audit_logger.py` — new file with `AdminAuditLogger` class.
- `backend/main.py` — add `/api/admin` FastAPI endpoint set.
- `frontend/templates/admin-login.html` — new minimal-HTML/HTMX template with the Pydantic-native admin-interface login form.
- `frontend/templates/admin-dashboard.html` — new minimal-HTML/HTMX template with the Pydantic-native admin-interface dashboard.

## Verification protocol reference

When the first v1 PR that adopts the *Pydantic-native-admin-on-ASGI* discipline lands, the verification protocol is:
1. Run `pytest tests/test_admin_user.py` and verify the `AdminAuthenticator` produces a valid admin-user session.
2. Run `pytest tests/integration/test_pydantic_admin_renderer.py` and verify the Pydantic-native admin-interface displays the existing v1 Pydantic schemas.
3. Run `pytest tests/integration/test_sqlalchemy2_admin_panel.py` and verify the SQLAlchemy-2.0-native-discovery produces a valid admin-panel lookup.
4. Run `uvicorn backend.main:app` and curl `/api/admin/login` to verify the endpoint returns the admin-user session as JSON.
5. Open `frontend/templates/admin-login.html` in a browser and verify the Pydantic-native admin-interface renders as a navigable login form.
6. Inspect the `AdminAuditEntry` table in Postgres and verify every admin-action writes an audit-entry (the §3.1 append-only-ledger invariant).

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *Pydantic-native-admin-on-ASGI* discipline lands, the rollback path is:
1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the two tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.

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

This defer artifact is documentation only. It becomes a build trigger when the **first v1 PR that scales owner-screen past 10 tables OR introduces owner-only-auth-scope** lands. At that point:
1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which admin-user (owner? manager?), which admin-action (add new Pydantic schema? delete existing Pydantic schema?), which admin-page (visible on the admin-dashboard), and which existing v1 surface to inherit the Pydantic schemas from.
3. Adopt the *Pydantic-native-admin-on-ASGI* discipline on the existing v1 minimal-HTML/HTMX waiter-web-UI surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v1 code is shipped.