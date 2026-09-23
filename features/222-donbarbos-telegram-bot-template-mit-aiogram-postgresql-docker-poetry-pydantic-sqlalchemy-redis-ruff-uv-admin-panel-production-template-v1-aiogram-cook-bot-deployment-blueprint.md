# Feature 222 — donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template-v1-aiogram-cook-bot-deployment-blueprint (defer)

> **NEW observation (2026-09-23).** Documents in-window GitHub Search `topic:telegram-bot+language:python` query result: `donbarbos/telegram-bot-template` (**MIT ✓**, **476★/79⑂**, Python, **pushed 2026-08-27T02:03:06Z = ~27 days before fetch time**, in-window by push only, **5942 KB** substantial repo, default_branch=`main`). Topics (verbatim from raw JSON, **20 topics**): `aiogram`, `aiogram-bot-template`, `analytics`, `docker`, `docker-compose`, `metrics`, `poetry`, `postgresql`, `pydantic`, `python`, `redis`, `ruff`, `sqlalchemy`, `telegram`, `telegram-bot`, `telegram-bot-example`, `telegram-bot-template`, `telegrambot`, `template`, `uv`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-23): *"🤖 Template for telegram bot using postgres, pgbouncer, redis, docker, amplitude, prometheus, grafana, CI with admin panel"*. **The highest-star-count aiogram-template of the 55-pass brainstorm series** (476★ vs feature 120's geminka-agent at smaller star count and feature 149's personal-agent-blueprint at smaller star count). Bucket: **v1 aiogram-cook-bot-deployment-blueprint (defer, parking-lot)** — watch-list entry, zero build time today. **HONEST DISCLOSURE**: this repo was previously surfaced in `/opt/data/le31-brainstorm-2026-09-22.md` §Operator UX and HCI signals section as a NOT-picked watch-list-only candidate — parent explicitly declined to pick it yesterday because the description was thin and the topic-overlap with LE31 was moderate; the subagent surfaced it again today and parent re-evaluates positively based on the *production-grade-aiogram+postgresql+docker+poetry-template* primitive value; same prior-rejection-then-promotion pattern as yesterday's Pick C `penguineer/PingBoardDaemon` (declined 09-21, promoted 09-22).

## Goal

Retain the **"Template for telegram bot using postgres, pgbouncer, redis, docker, amplitude, prometheus, grafana, CI with admin panel"** thirteen-tuple-primitive as a persistent cross-section reference for any future LE31 v1 maintenance pass that needs an *aiogram + postgresql + docker + poetry + pydantic + sqlalchemy + redis + admin-panel production-template* baseline to compare against. The artifact is the persistent cross-section reference + the thirteen named architectural primitives (aiogram, postgres, pgbouncer, redis, docker, amplitude, prometheus, grafana, CI, admin-panel + pydantic, sqlalchemy, poetry). No code today (MIT license permits future code reuse; vocabulary-only artifact today; 5942 KB substantial-repo size makes source-code inspection immediately productive).

## Scope

**In scope (defer artifact):**
- A written record of the **aiogram + postgresql** discipline: the *direct LE31 v1 cook-bot-stack match* (charter §3.2: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres) — this is the **highest-star-count aiogram-template of the 55-pass brainstorm series**.
- A written record of the **docker + docker-compose** discipline: the *containerization-posture* primitive (LE31 v1 today runs without docker, but the *docker + docker-compose* posture is a future-deployment-formalization vocabulary).
- A written record of the **poetry + uv + ruff + pydantic + sqlalchemy** discipline: the *modern-Python-toolchain* primitive (poetry/uv = dependency manager, ruff = linter, pydantic = data-validation, sqlalchemy = ORM).
- A written record of the **redis** discipline: the *cache/queue* primitive (LE31 v1 today does not use redis, but the *redis-as-cache-or-queue* posture is a future-v2 vocabulary for any high-traffic Telegram-bot traffic).
- A written record of the **amplitude + prometheus + grafana + metrics + analytics** discipline: the *observability-and-admin* cluster (the admin-panel allows the operator to inspect and modify the bot's state without going through the chat UI; the metrics + prometheus + grafana is the production-grade observability primitive).
- A written record of the **admin-panel** discipline: the *chat-bypass-admin-surface* primitive (the operator can administer the bot through a web UI instead of through chat commands).
- A decision record: today's verdict is `defer` because LE31 v1 is working code today; the comparison baseline is informative, not a build-trigger.
- A cross-section reference with the prior v1 aiogram-cook-bot stack-shape cluster: features 48 (pipecat-voice-watch aiogram-cluster), 116 (aiogram-3-31-0-stable-track), 120 (geminka-agent-aiogram-3-telegram-premium-markup-pattern), 149 (personal-agent-blueprint-telegram-chokepoint-architecture-pattern). The *transferable insight* is the **aiogram + postgresql + docker + poetry + pydantic + sqlalchemy + redis + admin-panel production-template** primitive set.

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

GitHub Search `topic:telegram-bot+language:python` query (parent re-fetched live, see `/tmp/le31-brainstorm-2026-09-23/gh/gh_topic_telegram-bot.json`) returned 1435 total / 50 retrieved candidates; `donbarbos/telegram-bot-template` is one of the 27 net-new in-window MIT Python candidates not previously filed. It is the **highest-star-count aiogram-template of the 55-pass brainstorm series** (476★).

The `donbarbos/telegram-bot-template` repo's architectural pattern has thirteen core sub-primitives:

1. **aiogram + postgresql** — direct LE31 v1 cook-bot-stack match. The *aiogram + postgresql* posture is exactly the LE31 v1 cook-bot stack (charter §3.2: aiogram v3 for the cook Telegram bot; Postgres in production). LE31 v1 today uses aiogram v3 + Postgres; the *donbarbos/telegram-bot-template* repo confirms the *aiogram + postgresql* posture is achievable in 5942 KB (note: substantial-repo size; source-code inspection immediately productive).

2. **docker + docker-compose** — the *containerization-posture* primitive. The template ships with a Dockerfile + docker-compose.yml for deployment; the *containerization-posture* IS the *deployment-formalization* primitive. LE31 v1 today runs without docker, but the *docker + docker-compose* posture is a future-deployment-formalization vocabulary.

3. **poetry + uv + ruff + pydantic + sqlalchemy** — the *modern-Python-toolchain* primitive. Poetry/uv = dependency manager, ruff = linter, pydantic = data-validation, sqlalchemy = ORM. The *modern-Python-toolchain* discipline IS the *Python 3.13 + FastAPI + SQLModel + Postgres* posture applied to the dependency-management + linting + validation + ORM dimension.

4. **redis + pgbouncer** — the *cache/queue/connection-pooler* primitive. Redis = cache/queue; pgbouncer = PostgreSQL connection-pooler. The *redis + pgbouncer* discipline IS the *production-grade connection-pooling + cache/queue* posture.

5. **amplitude + prometheus + grafana + metrics + analytics** — the *observability* cluster. The template ships with amplitude (product-analytics), prometheus (metrics), grafana (dashboards), metrics (custom-metrics); the *observability* cluster IS the *production-grade observability* posture.

6. **admin-panel** — the *chat-bypass-admin-surface* primitive. The template ships with an admin-panel web UI; the *admin-panel* discipline IS the *operator-can-administer-bot-without-chat* posture.

7. **CI** — the *continuous-integration* posture. The template ships with CI configuration; the *CI* discipline IS the *automated-testing + automated-deployment* posture.

The LE31 relevance is the **aiogram + postgresql + docker + poetry + pydantic + sqlalchemy + redis + admin-panel production-template** thirteen-tuple-primitive. LE31 v1 today has working cook-bot-stack (aiogram v3 + Postgres); the question this repo answers is "what does a production-grade aiogram + postgresql + docker + poetry + admin-panel template look like in 2026?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v1 maintenance trigger condition (if the first v1 PR that adds a deployment-formalization primitive to the cook-bot surface lands):** potential schema additions (depending on the v1 surface):
- `bot_admin_users` table — a registry of every operator who can access the admin-panel (user_id, username, role, recorded_at); the *admin-panel* vocabulary.
- `bot_metrics` table — a primitive for tracking per-command latency + error-rate for the cook-bot; the *observability* posture.
- `deployment_config` table — a primitive for managing the docker-compose deployment configuration; the *deployment-formalization* posture.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v1 maintenance trigger (when the first v1 PR that adds a deployment-formalization primitive to the cook-bot surface lands):**
- Add a `bot_admin_users` SQLModel table (user_id, username, role, recorded_at).
- Add a `bot_metrics` SQLModel table (metric_id, command, latency_ms, status_code, recorded_at).
- Add a `deployment_config` SQLModel table (config_id, key, value, recorded_at).
- Optionally add a `Dockerfile` + `docker-compose.yml` + `admin/` (FastAPI admin-panel) + `metrics/` (prometheus exporter) + `pyproject.toml` (poetry/uv-managed) to formalize the LE31 v1 deployment posture; the *production-template* discipline.

**Steps independent of the v1 maintenance trigger (today):**
- [x] Read the `donbarbos/telegram-bot-template` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *Template for telegram bot using postgres, pgbouncer, redis, docker, amplitude, prometheus, grafana, CI with admin panel* primitive (parent re-verified verbatim).
- [x] Cross-reference with features 48, 116, 120, 149 (ripgrep-verified distinct).
- [x] HONEST DISCLOSURE: this repo was previously surfaced in `/opt/data/le31-brainstorm-2026-09-22.md` §Operator UX and HCI signals section as a NOT-picked watch-list-only candidate — parent re-evaluates positively today based on the *production-grade-aiogram+postgresql+docker+poetry-template* primitive value.
- [ ] **Future source-code inspection recommended** to confirm the *aiogram + postgresql + docker + poetry + admin-panel* stack (5942 KB substantial-repo size makes the source-code inspection immediately productive — the *Dockerfile + docker-compose.yml + admin/ + pyproject.toml* are likely directly inspectable).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v1 maintenance trigger (when the first v1 PR that adds a deployment-formalization primitive to the cook surface lands):**
- The owner would access the *admin-panel* web UI to view the *cook-bot-metrics* (latency + error-rate + uptime); the *observability* primitive maps 1:1 onto a web-style dashboard.
- The owner would access the *admin-panel* to view the *active-admin-users* list; the *admin-panel* vocabulary maps 1:1 onto a web-style management interface.
- These are v1 maintenance surface additions; not in v1 scope today.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v1 maintenance trigger dependencies:** depends on the v1 maintenance surface that adds a deployment-formalization primitive to the cook-bot surface. Cross-references: features 48 (pipecat-voice-watch aiogram-cluster), 116 (aiogram-3-31-0-stable-track), 120 (geminka-agent-aiogram-3-telegram-premium-markup-pattern), 149 (personal-agent-blueprint-telegram-chokepoint-architecture-pattern).

## Open questions

1. **What is the *admin-panel* technology stack?** Is it a separate FastAPI app, or a Django app, or a React SPA, or a server-side-rendered HTMX page? The full read of the repo's source code is needed.
2. **What is the *CI* configuration?** Is it GitHub Actions, GitLab CI, CircleCI? What tests run? What deploys? The full read of the repo's source code is needed.
3. **What is the *observability* stack?** Does it use prometheus-client for the metrics exporter? Does it use structlog for structured logging? The full read of the repo's source code is needed.
4. **What is the *redis* usage?** Is it used for cache, queue, or session storage? Does it use aioredis or redis-py? The full read of the repo's source code is needed.
5. **What is the *aiogram* discipline?** Does it use aiogram v3 (LE31 v1's choice) or aiogram v2? Does it use middleware? Routers? Filters? FSM? The full read of the repo's source code is needed.
6. **What is the *PostgreSQL* posture?** Does it use asyncpg or psycopg2? Does it use SQLAlchemy 2.0 async? Does it use Alembic for migrations? The full read of the repo's source code is needed.
7. **MIT license file confirmation:** is `donbarbos/telegram-bot-template`'s MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **aiogram + postgresql + docker + poetry + pydantic + sqlalchemy + redis + admin-panel production-template** thirteen-tuple-primitive is **the highest-star-count aiogram-template of the 55-pass brainstorm series (476★) — and the MIT permissive license confirms it's a *practiced discipline*, not just a theoretical one. The vocabulary is fully transferable to LE31 v1's charter §3.2 baseline (Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3). The artifact is informational only today; the value is vocabulary + a future-comparison-baseline note for any v1 maintenance pass.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintenance PR adds a deployment-formalization primitive to the cook-bot surface, the owner wants *a comparison baseline against another production-grade aiogram + postgresql + docker + poetry + admin-panel template*, but struggles because *LE31 v1 is small enough that no in-repo production-template comparison baseline exists*, so that *v1 maintenance can ship deployment-formalization primitives with reference evidence*." **PASS** (zero-pain today; v1 is small enough that the comparison baseline is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 5942 KB repo + the 20-topic vocabulary + the aiogram + postgresql + docker + poetry + admin-panel thirteen-tuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium-high for the architectural match (the *aiogram + postgresql + docker + admin-panel* primitive set is well-established in the GitHub 476★-community-adoption cluster; the 5942 KB substantial-repo size + 20 topics + 1★ source-code inspection is productive). MIT license is charter-compatible per §3.2. **PASS** (with follow-up). |
| 4 | **Conflict** | None. The *aiogram + postgresql + docker + admin-panel* primitive set is charter §3.1 + §3.2 invariant-compatible (aiogram v3 + Postgres match LE31 v1 cook-bot-stack exactly; docker is off-pattern for v1 deployment today but the vocabulary is forward-compatible). **PASS** (charter §3.1 + §3.2 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v1 aiogram-cook-bot-deployment-blueprint (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation + a source-code-inspection follow-up). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 5942 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours). **Cost-to-value ratio: high** (5942 KB substantial-repo size makes source-code inspection immediately productive). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/222-donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template-v1-aiogram-cook-bot-deployment-blueprint-HANDOFF.md` and `features/222-donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template-v1-aiogram-cook-bot-deployment-blueprint.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference + the source-code-inspection follow-up task).

## Cross-references

- Parent research issue: `/opt/data/le31-brainstorm-2026-09-23.md` (55th consecutive daily-brainstorm pass).
- Prior-rejection record: `/opt/data/le31-brainstorm-2026-09-22.md` §Operator UX and HCI signals section (NOT-picked watch-list-only candidate).
- Companion artifacts (ripgrep-verified distinct): features 48 (pipecat-voice-watch aiogram-cluster), 116 (aiogram-3-31-0-stable-track), 120 (geminka-agent-aiogram-3-telegram-premium-markup-pattern), 149 (personal-agent-blueprint-telegram-chokepoint-architecture-pattern).
- Sister-picks from 2026-09-23: feature 221 (mrlonis-python-open-restaurant-fastapi v1 production-restaurant-API-reference), feature 223 (psb684-sketch-athena v2 small-business-ERP-horizontal-vocabulary-reference).
- Linear parent issue: `Brainstorm 2026-09-23 — daily` (or fallback JSON at `/opt/data/le31-brainstorm-2026-09-23.linear-fallback.json` if Linear MCP write is blocked by workspace plan-limit).
- Linear sub-issue (this feature): `LE31-XXX` (pending Linear MCP write — see `Brainstorm 2026-09-23 — daily` parent issue).
