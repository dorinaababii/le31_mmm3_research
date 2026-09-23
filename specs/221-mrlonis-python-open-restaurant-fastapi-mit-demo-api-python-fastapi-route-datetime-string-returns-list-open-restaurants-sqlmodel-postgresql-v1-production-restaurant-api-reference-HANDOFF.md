# 221 — mrlonis/python-open-restaurant-fastapi v1-production-restaurant-api-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 opening-hours surface question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/221-mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-string-returns-list-open-restaurants-sqlmodel-postgresql-v1-production-restaurant-api-reference.md` (defer artifact; **no code today**).

Bucket: **v1 production-restaurant-API reference (FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintainer asks *'if v1 introduces an opening-hours surface (guest-facing "is the restaurant open right now?" query, or staff-facing "what are today's hours?" query, or owner-facing "what were last week's open-hours?" analytics query), what is the *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* vocabulary that preserves the existing v1 no-opening-hours-surface posture?'*, the maintainer wants *evidence that another independent 2022 Python repo at 2813 KB with 2★/1⑂ + MIT permissive license + 5 topics + in-window-by-pushed-at-only is shipping the *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* primitive as the v1 production-restaurant-API discipline*, but struggles because *v1 has no documented opening-hours primitive in the charter*, so that *v1 can introduce the opening-hours + restaurant-hours-lookup vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no opening-hours surface trigger; the JTBD is primitive vocabulary extension + FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup documentation, not a build-need; **cross-section JTBD value is medium-high** — the only candidate of the 55-pass series that pins `sqlmodel` as a topic). |
| 2 | **Viability** | Maintainer can read 2813 KB repo description + 5-topic vocabulary + FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup quadruple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the MIT-permissive code; LE31 v1 has no opening-hours surface today). Confidence: medium-high for the *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* vocabulary (2★/1⑂ + MIT permissive license + 5 topics including the rare `sqlmodel` topic + in-window-by-pushed-at-only + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *restaurant-hours-lookup* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the datetime-windowed-availability-query dimension*; the *FastAPI + SQLModel + PostgreSQL* stack matches LE31 v1's stack exactly). Stack: FastAPI + SQLModel + PostgreSQL backend = on-pattern for v1 primitives (matches v1 charter §3.2 baseline); opening-hours surface = off-pattern for v1 (LE31 v1 has no opening-hours surface); restaurant-hours-lookup = off-pattern for v1 (LE31 v1 has no restaurant-hours-lookup surface); MIT permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v1 maintenance question). |
| 4 | **Conflict** | None. The *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the datetime-windowed-availability-query dimension* (the *restaurant-hours-lookup* route is read-only; no state change). Charter §3.1 alignment (the *datetime-windowed-availability-query* is a read-only route; no state change); §3.2 STRICTLY-COMPATIBLE (MIT permissive); §3.4 not triggered (no AI surface; the route is a deterministic SQL query). **PASS**. |
| 5 | **Outcome, appetite, scope** | v1 production-restaurant-API reference (FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2813 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours; 2813 KB substantial-repo size makes inspection immediately productive). **Cost-to-value ratio: high** (2813 KB substantial-repo size; the *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* quadruple + the in-window-by-pushed-at-only signal + the rare `sqlmodel` topic need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/221-mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-string-returns-list-open-restaurants-sqlmodel-postgresql-v1-production-restaurant-api-reference-HANDOFF.md` and `features/221-mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-string-returns-list-open-restaurants-sqlmodel-postgresql-v1-production-restaurant-api-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup documentation for the next v1 opening-hours review moment; **cross-section JTBD value is medium-high — the only of the 55-pass brainstorm series that pins `sqlmodel` as a topic**).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds an opening-hours surface to the LE31 v1 operator surface, a restaurant-hours-lookup surface, or a FastAPI + SQLModel + PostgreSQL production-template surface):

- `app/api/v1/restaurants.py` — possibly add (the restaurant-hours-lookup FastAPI route module; depends on the v1 change).
- `app/api/v1/restaurants/open.py` — possibly add (the `/api/v1/restaurants/open` route handler; depends on the v1 change).
- `app/models/restaurant_hours.py` — possibly add (the `restaurant_hours` SQLModel table; depends on the v1 change).
- `app/models/availability_query_log.py` — possibly add (the `availability_query_log` SQLModel table; depends on the v1 change).
- `tests/test_restaurants_open.py` + `tests/test_restaurant_hours.py` + `tests/test_availability_query_log.py` — possibly add (the integration tests for the opening-hours + restaurant-hours-lookup + availability-query-log surfaces; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no opening-hours surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/221-mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-string-returns-list-open-restaurants-sqlmodel-postgresql-v1-production-restaurant-api-reference.md` exists and is read back by the parent.
- [ ] `specs/221-mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-string-returns-list-open-restaurants-sqlmodel-postgresql-v1-production-restaurant-api-reference-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `mrlonis/python-open-restaurant-fastapi` description is quoted verbatim (2813 KB repo).
- [ ] The 2★/1⑂ + MIT permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption) + Python + in-window-by-pushed-at-only + 5 topics including the rare `sqlmodel` topic + description *"Demo API, written in Python FastAPI, with one route that takes a datetime string and returns a list of open restaurants, if any."* is documented.
- [ ] The charter §3.1 alignment via *datetime-windowed-availability-query = read-only route; no state change* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (MIT permissive) is documented.
- [ ] The charter §3.4 not-triggered (no AI surface) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds an opening-hours surface to the LE31 v1 operator surface, a restaurant-hours-lookup surface, or a FastAPI + SQLModel + PostgreSQL production-template surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `mrlonis/python-open-restaurant-fastapi` *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* vocabulary is evaluated against the PR's changes: does the change address the *opening-hours* discipline? does the change preserve the *restaurant-hours-lookup* primitive? does the change preserve the *FastAPI + SQLModel + PostgreSQL* stack? does the change preserve the *charter §3.1 explicit-state-transition* pattern?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 trigger (if the v1 opening-hours surface is adopted):**
- Disable path: feature flag `LE31_OPENING_HOURS_ENABLED = False` (default; gates all `app/api/v1/restaurants/open.py` routes); no data loss.
- Delete path: `rm -rf app/api/v1/restaurants/open.py` + `rm -rf app/models/restaurant_hours.py` + `rm -rf app/models/availability_query_log.py` + `rm -rf tests/test_restaurants_open.py` + `rm -rf tests/test_restaurant_hours.py` + `rm -rf tests/test_availability_query_log.py`; remove any opening-hours-specific dependencies from `requirements.txt`; no retained data; no safe-failure-mode concern.
- Migration/rollback cost: low (no schema change for `audit_logs` or `StockEntry`; new `restaurant_hours` table is independent).

## 6. Mandatory LE31 skill list (per `le31-feature-pipeline/SKILL.md` step 5)

The following skills MUST be loaded by the coding agent before any v1 trigger fires:

- `le31-conventions` — for the seven-check feature gate + charter §3.1 + §3.2 + §3.4 invariants.
- `le31-verification-protocol` — for the verification protocol + the "done means observed, not asserted" principle.
- `le31-feature-pattern` — for the existing v1 feature pattern (FastAPI + SQLModel + aiogram v3 + Postgres; first-class prepared-item stock via append-only `StockEntry` ledger).
- `le31-handoff-spec` — for the slice contract format (this file is an example).
- `le31-coding-agent-brief` — for the paste-in prompt that the coding agent will use to start work.

The following skills MAY be loaded depending on the trigger:

- `le31-research` — if the v1 trigger requires additional cross-section vocabulary.
- `le31-v1-feature-pattern` — if the v1 trigger requires extending the v1 feature pattern.
- `le31-frontend` / `le31-backend` — if the v1 trigger requires frontend or backend changes.
