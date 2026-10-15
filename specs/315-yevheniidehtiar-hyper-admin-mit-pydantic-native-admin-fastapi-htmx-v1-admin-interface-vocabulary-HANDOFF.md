# HANDOFF — Feature 315: `yevheniidehtiar-hyper-admin-mit-pydantic-native-admin-fastapi-htmx-v1-admin-interface-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

> **Note on filename**: the HANDOFF filename uses the full slug per the v1 feature contract shape (see `features/315-…-vocabulary.md`).

## Active feature path

`features/315-yevheniidehtiar-hyper-admin-mit-pydantic-native-admin-fastapi-htmx-v1-admin-interface-vocabulary.md` — defer/parking-lot (Pick B of Daily Research 2026-10-13 carry-over).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface needs a Pydantic-native admin interface for FastAPI + HTMX, *the owner/waiter wants* a ready-made admin-interface that inherits the existing Pydantic schemas + can drop into existing FastAPI routes, *but struggles because* today's FastAPI+HTMX admin-frameworks either require a third-language frontend or hand-rolled CRUD templates, *so that* the admin-interface ships in 1-day of integration work instead of 1-week. |
| 2 | Viability | ✓ | Single-developer v1 surface; no specialist help needed; vocabulary-only artifact; REVERSIBLE (pure observation, zero code today). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + FastAPI ✓ ON-STACK + HTMX ✓ ON-STACK + Pydantic ✓ ON-STACK. The 3/3 LE31-stack-match + the *Pydantic-native* adjective = the strongest in-window 2026 v1 Pydantic-native admin-interface stack-match of the 75-pass series. 5★/2⑂ = 2.4 forks per star = strong fork-to-star ratio = active downstream-fork adoption. Rabbit hole: the *Pydantic-native* adjective is not yet adopted by LE31 v1; the *admin-interface* primitive is a v1 polish surface. Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *FastAPI + HTMX + Pydantic-native* primitives are §3.1 + §3.2 + §3.6-aligned (Python+FastAPI+HTMX+Pydantic + append-only-audit-log + on-premise-deployment + non-AI-fallback). No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (Pydantic-native admin interface on waiter web UI). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + Pydantic schemas + HTMX waiter-web-UI) already implement the *FastAPI + HTMX + Pydantic-native* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (the *Pydantic-native-admin-interface* primitive is a v1 polish surface; v1 charter is waiter-web-UI + cook-Telegram-bot + owner-daily-recap + append-only-StockEntry; the *admin-interface* primitive is not in v1 charter).

## Bucket

**v1** (admin-interface-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description names the *Pydantic-native + admin-interface + FastAPI + HTMX* quadruple-primitive.

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *Pydantic-native-admin-interface* discipline on the waiter web UI lands, the files to touch are:
- `backend/alembic/versions/` — add migration for `AdminUser`, `AdminAuditEntry` tables.
- `backend/admin_user.py` — new file with `AdminAuthenticator` class.
- `backend/admin_audit_logger.py` — new file with `AdminAuditLogger` class.
- `backend/pydantic_admin_ui.py` — new file with `PydanticAdminUI` class.
- `backend/main.py` — add `/api/admin` FastAPI endpoint set.
- `frontend/templates/admin-login.html` — new minimal-HTML/HTMX template with the Pydantic-native admin-interface login form.
- `frontend/templates/admin-dashboard.html` — new minimal-HTML/HTMX template with the Pydantic-native admin-interface dashboard.

## Verification protocol reference

When the first v1 PR that adopts the *Pydantic-native-admin-interface* discipline lands, the verification protocol is:
1. Run `pytest tests/test_admin_user.py` and verify the `AdminAuthenticator` produces a valid admin-user session.
2. Run `pytest tests/integration/test_pydantic_admin_ui.py` and verify the Pydantic-native admin-interface displays the existing v1 Pydantic schemas.
3. Run `uvicorn backend.main:app` and curl `/api/admin/login` to verify the endpoint returns the admin-user session as JSON.
4. Open `frontend/templates/admin-login.html` in a browser and verify the Pydantic-native admin-interface renders as a navigable login form.
5. Inspect the `AdminAuditEntry` table in Postgres and verify every admin-action writes an audit-entry (the §3.1 append-only-ledger invariant).

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *Pydantic-native-admin-interface* discipline lands, the rollback path is:
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
3. Adopt the *Pydantic-native-admin-interface* discipline on the existing v1 minimal-HTML/HTMX waiter-web-UI surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v1 code is shipped.