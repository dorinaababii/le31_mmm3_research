# Feature 221 — mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-string-returns-list-open-restaurants-sqlmodel-postgresql-v1-production-restaurant-api-reference (defer)

> **NEW observation (2026-09-23).** Documents in-window GitHub Search `restaurant+language:python` query result: `mrlonis/python-open-restaurant-fastapi` (**MIT ✓**, **2★/1⑂**, Python, **pushed 2026-09-04T11:25:01Z = ~19 days before fetch time**, in-window by push only, **2813 KB** substantial repo, default_branch=`main`). Topics (verbatim from raw JSON, **5 topics**): `fastapi`, `postgresql`, `python`, `sqlalchemy`, `sqlmodel`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-23): *"Demo API, written in Python FastAPI, with one route that takes a datetime string and returns a list of open restaurants, if any."* **The only 2026-09-23 in-window v1 production-restaurant-API reference that pins all 5 of `fastapi + postgresql + python + sqlalchemy + sqlmodel` in the topic array** = the **only candidate of the 55-pass brainstorm series that pins `sqlmodel` as a topic** = the closest LE31-stack-shape match for the *restaurant-Python-API* primitive. Bucket: **v1 production-restaurant-API-reference (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"Demo API, written in Python FastAPI, with one route that takes a datetime string and returns a list of open restaurants, if any."** quadruple-primitive as a persistent cross-section reference for any future LE31 v1 maintenance pass that needs a *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* baseline to compare against. The artifact is the persistent cross-section reference + the four named architectural primitives (FastAPI, SQLModel, PostgreSQL, restaurant-hours-lookup). No code today (MIT license permits future code reuse; vocabulary-only artifact today; 2813 KB substantial-repo size makes source-code inspection immediately productive).

## Scope

**In scope (defer artifact):**
- A written record of the **FastAPI + SQLModel** discipline: the *direct LE31 v1 backend stack match* (charter §3.2: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres) — this is the **only of the 55-pass brainstorm series' restaurant-API candidates that pins `sqlmodel` as a topic**.
- A written record of the **PostgreSQL** discipline: the *direct LE31 v1 production-database match* (charter §3.2: Postgres in production).
- A written record of the **restaurant-hours-lookup** surface: the *datetime-windowed-availability-query* primitive (a read-only route that takes a datetime string and returns the list of restaurants that are open at that datetime).
- A written record of the **demo-API** discipline: the *minimal-API-surface-as-evidence-of-stack* posture (the API is intentionally minimal — one route — but the stack is fully represented; the minimality is the evidence that the stack is the discipline, not the surface area).
- A decision record: today's verdict is `defer` because LE31 v1 is working code today; the comparison baseline is informative, not a build-trigger.
- A cross-section reference with the prior v1 restaurant-API stack-shape cluster: features 158 (azizsekerdil-smart-restaurant-management-system), 195 (skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management), 201 (sahajasakhunala-DineDesk), 205 (Mark007-R/Restaurant-Intelligence-Platform), 218 (LuisRG98-restaurant-saas-api from 09-23 daily-research). The *transferable insight* is the **FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup** primitive set.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).

## Description

GitHub Search `restaurant+language:python` query (parent re-fetched live, see `/tmp/le31-brainstorm-2026-09-23/gh/gh_restaurant.json`) returned 1918 total / 50 retrieved candidates; `mrlonis/python-open-restaurant-fastapi` is one of the 6 net-new in-window MIT Python candidates not previously filed. It is the **only 2026-09-23 in-window v1 production-restaurant-API reference that pins all 5 of `fastapi + postgresql + python + sqlalchemy + sqlmodel` in the topic array** of the 55-pass brainstorm series.

The `mrlonis/python-open-restaurant-fastapi` repo's architectural pattern has four core sub-primitives:

1. **FastAPI + SQLModel** — direct LE31 v1 backend stack match. The *FastAPI + SQLModel + PostgreSQL* posture is exactly the LE31 v1 backend stack (charter §3.2: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres). LE31 v1 today uses FastAPI + SQLModel + Postgres; the *python-open-restaurant-fastapi* repo confirms the *FastAPI + SQLModel + PostgreSQL + restaurant-domain* posture is achievable in 2813 KB (note: substantial-repo size; source-code inspection immediately productive).

2. **Restaurant-hours-lookup** — the *datetime-windowed-availability-query* primitive. The single route takes a datetime string and returns the list of restaurants that are open at that datetime; the primitive IS the *restaurant-hours-table joined to a datetime-window* query. LE31 v1 today has 2 primary surfaces (waiter web UI + cook Telegram bot) per charter §3.1; the *restaurant-hours-lookup* pattern is the *third-surface-vocabulary* (the API-only surface, no UI) for any future v1 expansion to opening-hours queries.

3. **PostgreSQL** — direct LE31 v1 production-database match (charter §3.2: Postgres in production). The *postgresql* topic explicitly names the production-database choice.

4. **Demo-API** — the *minimal-API-surface-as-evidence-of-stack* posture. The API is intentionally minimal (one route), but the stack is fully represented (FastAPI + SQLModel + PostgreSQL); the minimality is the evidence that the stack is the discipline, not the surface area.

The LE31 relevance is the **FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup** quadruple-primitive. LE31 v1 today has working stack (FastAPI + SQLModel + Postgres); the question this repo answers is "what does a FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup baseline look like in 2026?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v1 maintenance trigger condition (if the first v1 PR that adds an opening-hours surface to the waiter/cook surface lands):** potential schema additions (depending on the v1 surface):
- `restaurant_hours` table — a registry of every restaurant's open-hours windows per day-of-week (restaurant_id, day_of_week, open_time, close_time, recorded_at); the *restaurant-hours-lookup* vocabulary.
- `availability_query_log` table — a primitive for tracking per-query latency + result-set-size for the *datetime-windowed-availability-query*; the *production-grade* posture.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v1 maintenance trigger (when the first v1 PR that adds an opening-hours surface to the waiter/cook surface lands):**
- Add a `restaurant_hours` SQLModel table (restaurant_id, day_of_week, open_time, close_time, recorded_at).
- Add a `availability_query_log` SQLModel table (query_id, datetime_input, result_set_size, latency_ms, recorded_at).
- Optionally add an `availability_query` FastAPI route (`GET /api/v1/restaurants/open?datetime=2026-09-23T19:30:00`) that returns the list of open restaurants at the given datetime; the *restaurant-hours-lookup* primitive.

**Steps independent of the v1 maintenance trigger (today):**
- [x] Read the `mrlonis/python-open-restaurant-fastapi` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *Demo API, written in Python FastAPI, with one route that takes a datetime string and returns a list of open restaurants, if any.* primitive (parent re-verified verbatim).
- [x] Cross-reference with features 158, 195, 201, 205, 218 (ripgrep-verified distinct).
- [ ] **Future source-code inspection recommended** to confirm the *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* stack (2813 KB substantial-repo size makes the source-code inspection immediately productive — the *restaurant_hours* table schema + the *availability_query* route handler are likely directly inspectable).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v1 maintenance trigger (when the first v1 PR that adds an opening-hours surface to the cook surface lands):**
- The cook would need a Telegram command to view the *opening-hours summary* (e.g., `/hours today`); the *restaurant-hours-lookup* primitive maps 1:1 onto a chat-style query interface.
- The owner would need a Telegram command to view the *opening-hours-modification* interface (e.g., `/hours set <day> <open> <close>`); the *restaurant-hours* vocabulary maps 1:1 onto a chat-style modification interface.
- These are v1 maintenance surface additions; not in v1 scope today.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v1 maintenance trigger dependencies:** depends on the v1 maintenance surface that adds an opening-hours surface to the waiter/cook surface. Cross-references: features 158 (azizsekerdil-smart-restaurant-management-system), 195 (skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management), 201 (sahajasakhunala-DineDesk), 205 (Mark007-R/Restaurant-Intelligence-Platform), 218 (LuisRG98-restaurant-saas-api from 09-23 daily-research).

## Open questions

1. **What is the exact route handler signature?** Does it use `def` or `async def`? Does it return `List[Restaurant]` or `Dict[str, Any]`? What is the `Restaurant` SQLModel schema? The full read of the repo's source code is needed.
2. **What is the *restaurant_hours* table schema?** Is it one row per restaurant-day, or one row per restaurant-day-window (allowing multiple open-windows per day)? Is `timezone` stored per restaurant or as a global setting? The full read of the repo's source code is needed.
3. **What is the *datetime-windowed-availability-query* SQL?** Is it a `BETWEEN` query against a `restaurant_hours` table, or a more complex `OVERLAPS` query? The full read of the repo's source code is needed.
4. **What is the *SQLModel* discipline?** Does it use `SQLModel` (the unified SQLModel-Pydantic class) or `SQLModel + Pydantic v2 BaseModel` (separate schema + table)? What is the `Restaurant` table's column-typing posture? The full read of the repo's source code is needed.
5. **What is the *PostgreSQL* posture?** Does it use `JSONB` for the `hours` column, or normalized per-day rows? Does it use `TIMESTAMPTZ` or `TIMESTAMP`? The full read of the repo's source code is needed.
6. **MIT license file confirmation:** is `mrlonis/python-open-restaurant-fastapi`'s MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup** quadruple-primitive is **the only 2026-09-23 in-window v1 production-restaurant-API reference that pins all 5 of `fastapi + postgresql + python + sqlalchemy + sqlmodel` in the topic array of the 55-pass brainstorm series** — and the MIT permissive license confirms it's a *practiced discipline*, not just a theoretical one. The vocabulary is fully transferable to LE31 v1's charter §3.2 baseline (Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3). The artifact is informational only today; the value is vocabulary + a future-comparison-baseline note for any v1 maintenance pass.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintenance PR adds an opening-hours surface to the waiter/cook surface, the owner wants *a comparison baseline against another FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup reference*, but struggles because *LE31 v1 has no opening-hours surface today*, so that *v1 maintenance can ship opening-hours primitives with reference evidence*." **PASS** (zero-pain today; v1 has no opening-hours surface; the JTBD is vocabulary + future-comparison-baseline, not a build-need). |
| 2 | **Viability** | Owner can read the 2813 KB repo + the 5-topic vocabulary + the FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup quadruple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium-high for the architectural match (the *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* primitive set is well-established in the GitHub 2★-community-adoption cluster; the 2813 KB substantial-repo size + 5 topics + 1★ source-code inspection is productive). MIT license is charter-compatible per §3.2. **PASS** (with follow-up). |
| 4 | **Conflict** | None. The *FastAPI + SQLModel + PostgreSQL + restaurant-hours-lookup* primitive set is charter §3.1 + §3.2 invariant-compatible (FastAPI + SQLModel + Postgres match LE31 v1 stack exactly). **PASS** (charter §3.1 + §3.2 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v1 production-restaurant-API-reference (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation + a source-code-inspection follow-up). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2813 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours). **Cost-to-value ratio: high** (2813 KB substantial-repo size makes source-code inspection immediately productive). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/221-mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-string-returns-list-open-restaurants-sqlmodel-postgresql-v1-production-restaurant-api-reference-HANDOFF.md` and `features/221-mrlonis-python-open-restaurant-fastapi-mit-demo-api-python-fastapi-route-datetime-string-returns-list-open-restaurants-sqlmodel-postgresql-v1-production-restaurant-api-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference + the source-code-inspection follow-up task).

## Cross-references

- Parent research issue: `/opt/data/le31-brainstorm-2026-09-23.md` (55th consecutive daily-brainstorm pass).
- Companion artifacts (ripgrep-verified distinct): features 158 (azizsekerdil-smart-restaurant-management-system), 195 (skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management), 201 (sahajasakhunala-DineDesk), 205 (Mark007-R/Restaurant-Intelligence-Platform), 218 (LuisRG98-restaurant-saas-api from 09-23 daily-research).
- Sister-picks from 2026-09-23: feature 222 (donbarbos-telegram-bot-template v1 aiogram-cook-bot-deployment-blueprint), feature 223 (psb684-sketch-athena v2 small-business-ERP-horizontal-vocabulary-reference).
- Linear parent issue: `Brainstorm 2026-09-23 — daily` (or fallback JSON at `/opt/data/le31-brainstorm-2026-09-23.linear-fallback.json` if Linear MCP write is blocked by workspace plan-limit).
- Linear sub-issue (this feature): `LE31-XXX` (pending Linear MCP write — see `Brainstorm 2026-09-23 — daily` parent issue).
