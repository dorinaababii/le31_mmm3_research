# HANDOFF — Feature 319: `mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-list-open-restaurants-v1-in-domain-fastapi-postgresql-sqlalchemy-sqlmodel-architecture-reference`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

> **Note on filename**: the HANDOFF filename uses the full slug per the v1 feature contract shape (see `features/319-…-architecture-reference.md`).

## Active feature path

`features/319-mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-list-open-restaurants-v1-in-domain-fastapi-postgresql-sqlalchemy-sqlmodel-architecture-reference.md` — defer/parking-lot (Pick C of Daily Research 2026-10-15).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface needs an in-domain FastAPI + PostgreSQL + SQLAlchemy + SQLModel architecture reference for restaurant queries (e.g., "is restaurant X open at time T?"), *the owner/waiter wants* a ready-made in-domain reference that proves the *implementation strategy exists in 2026 with the same FastAPI+PostgreSQL+SQLAlchemy+SQLModel posture*, *but struggles because* LE31 has no documented in-domain FastAPI+PostgreSQL+SQLAlchemy+SQLModel reference that confirms the entire LE31 v1 backend stack is real in 2026, *so that* the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same FastAPI+PostgreSQL+SQLAlchemy+SQLModel posture". |
| 2 | Viability | ✓ | Single-developer v1 surface; no specialist help needed; vocabulary-only artifact; REVERSIBLE (pure observation, zero code today). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + FastAPI ✓ ON-STACK + PostgreSQL ✓ ON-STACK + SQLAlchemy ✓ ON-STACK + SQLModel ✓ ON-STACK. The 5/5 LE31 v1 backend stack primitives matched = the strongest in-window 2026 in-domain FastAPI+PostgreSQL+SQLAlchemy+SQLModel architecture reference of the 76-pass series. The 3.8-year-old repo with in-window push = active 2026 maintainer of the entire LE31 v1 stack from before LE31's charter date. Rabbit hole: the *restaurant-query-as-a-service* primitive is not yet adopted by LE31 v1; the *in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference* primitive is a v1 polish surface. Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *FastAPI + PostgreSQL + SQLAlchemy + SQLModel + in-domain restaurant* quintuple-primitive is §3.1-aligned (Python+FastAPI+Postgres+SQLAlchemy+SQLModel+in-domain-restaurant-vertical = LE31 v1 production stack + restaurant-vertical; the *in-domain restaurant* posture IS the *restaurant-vertical* primitive applied to the *architecture-reference* dimension). No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (in-domain restaurant-query-as-a-service surface). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + SQLModel + FastAPI + Postgres) already implement the *FastAPI+PostgreSQL+SQLAlchemy+SQLModel* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (the *in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference* primitive is a v1 polish surface; v1 charter is waiter-web-UI + cook-Telegram-bot + owner-daily-recap + append-only-StockEntry; the *in-domain-restaurant-query-as-a-service* primitive is not in v1 charter).

## Bucket

**v1** (in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference) — the *vocabulary* is the value, not the code. The verbatim description + topics name the sextuple-primitive set (Demo-API + one-route + datetime + list-of-open-restaurants + FastAPI + PostgreSQL + Python + SQLAlchemy + SQLModel).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that introduces an in-domain restaurant-query-as-a-service surface for the LE31 single-restaurant Swiss kitchen lands, the files to touch are:
- `backend/alembic/versions/` — add migration for `RestaurantQuery`, `RestaurantHours` tables.
- `backend/restaurant_query_service.py` — new file with `RestaurantQueryService` class.
- `backend/restaurant_hours_manager.py` — new file with `RestaurantHoursManager` class.
- `backend/main.py` — add `/api/open-restaurants` FastAPI endpoint.

## Verification protocol reference

When the first v1 PR that introduces the in-domain restaurant-query-as-a-service surface lands, the verification protocol is:
1. Run `pytest tests/test_restaurant_query_service.py` and verify the `RestaurantQueryService` produces a valid open-restaurants list for any datetime input.
2. Run `pytest tests/integration/test_restaurant_hours_manager.py` and verify the `RestaurantHoursManager` manages restaurant open/close hours correctly per day-of-week.
3. Run `uvicorn backend.main:app` and curl `/api/open-restaurants?datetime=2026-10-15T19:00:00` to verify the endpoint returns the open-restaurants list as JSON.
4. Verify the response respects the Europe/Paris timezone (charter §3.6).

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v1 PR that introduces the in-domain restaurant-query-as-a-service surface lands, the rollback path is:
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
- `skills/le31-data/SKILL.md` — for the data conventions (if applicable).
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

This defer artifact is documentation only. It becomes a build trigger when the **first v1 PR that introduces an in-domain restaurant-query-as-a-service surface for the LE31 single-restaurant Swiss kitchen** lands. At that point:
1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which RestaurantQuery (open-restaurants? open-restaurants-by-cuisine? open-restaurants-by-location?), which RestaurantHours (per-restaurant? per-day-of-week? per-special-day?), which Europe/Paris timezone handling, and which existing v1 surface to inherit the SQLModel schemas from.
3. Adopt the *in-domain-FastAPI+PostgreSQL+SQLAlchemy+SQLModel-architecture-reference* discipline on the existing v1 SQLModel + Postgres + SQLAlchemy infrastructure.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v1 code is shipped.