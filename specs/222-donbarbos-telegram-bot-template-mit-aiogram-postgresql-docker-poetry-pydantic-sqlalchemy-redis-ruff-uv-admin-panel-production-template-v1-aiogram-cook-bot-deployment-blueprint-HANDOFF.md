# 222 — donbarbos/telegram-bot-template v1-aiogram-cook-bot-deployment-blueprint HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 deployment-formalization question becomes buildable. **Do not implement today.**
>
> **HONEST DISCLOSURE**: this repo was previously surfaced in `/opt/data/le31-brainstorm-2026-09-22.md` §Operator UX and HCI signals section as a NOT-picked watch-list-only candidate — parent explicitly declined to pick it yesterday because the description was thin and the topic-overlap with LE31 was moderate; the subagent surfaced it again today and parent re-evaluates positively based on the *production-grade-aiogram+postgresql+docker+poetry-template* primitive value, but the cross-section JTBD value is moderate and the prior-rejection is recorded honestly in this report.

## 1. Active feature path

`features/222-donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template-v1-aiogram-cook-bot-deployment-blueprint.md` (defer artifact; **no code today**).

Bucket: **v1 aiogram-cook-bot-deployment-blueprint (aiogram + postgresql + docker + poetry + pydantic + sqlalchemy + redis + admin-panel production-template, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintainer asks *'if v1 introduces a deployment-formalization surface (docker-based-deployment for multi-restaurant franchise rollout, or formal-redis-cache for high-traffic Telegram-bot traffic, or admin-panel for non-chat operator-administration), what is the *aiogram + postgresql + docker + poetry + admin-panel production-template* vocabulary that preserves the existing v1 no-deployment-formalization posture?'*, the maintainer wants *evidence that another independent 2021 Python repo at 5942 KB with 476★/79⑂ + MIT permissive license + 20 topics + in-window-by-pushed-at-only is shipping the *aiogram + postgresql + docker + poetry + admin-panel production-template* primitive as the v1 deployment-formalization discipline*, but struggles because *v1 has no documented deployment-formalization primitive in the charter*, so that *v1 can introduce the deployment-formalization + admin-panel vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no deployment-formalization trigger; the JTBD is primitive vocabulary extension + aiogram + postgresql + docker + admin-panel documentation, not a build-need; **cross-section JTBD value is moderate-to-high** — the highest-star-count aiogram-template of the 55-pass brainstorm series). |
| 2 | **Viability** | Maintainer can read 5942 KB repo description + 20-topic vocabulary + aiogram + postgresql + docker + poetry + admin-panel thirteen-tuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *aiogram + postgresql + docker + admin-panel* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the MIT-permissive code; LE31 v1 has no deployment-formalization surface today). Confidence: medium-high for the *aiogram + postgresql + docker + admin-panel* vocabulary (476★/79⑂ + MIT permissive license + 20 topics including 9 LE31-stack-matched topics + in-window-by-pushed-at-only + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *admin-panel* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the chat-bypass-admin-surface dimension*; the *aiogram + postgresql + docker* discipline IS the *charter §3.2 baseline posture applied to the deployment-formalization dimension*). Stack: FastAPI + SQLModel + aiogram v3 + PostgreSQL = on-pattern for v1 primitives (matches v1 charter §3.2 baseline); docker = off-pattern for v1 deployment today (LE31 v1 has no docker deployment); admin-panel = off-pattern for v1 (LE31 v1 has no admin-panel); redis = off-pattern for v1 (LE31 v1 has no redis); MIT permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v1 maintenance question). |
| 4 | **Conflict** | None. The *aiogram + postgresql + docker + admin-panel* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the chat-bypass-admin-surface dimension* (every admin action is an explicit state transition; no silent transition; the admin-panel preserves the *chat-bypass-admin-surface* primitive by requiring explicit admin actions for every state change). Charter §3.1 alignment (the *admin-panel* discipline IS the *explicit-state-transition* applied to the chat-bypass-admin-surface dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive; docker is off-pattern for v1 today but the vocabulary is forward-compatible); §3.4 not triggered (no AI surface; the admin-panel is operator-tooling, not customer-facing AI). **PASS**. |
| 5 | **Outcome, appetite, scope** | v1 aiogram-cook-bot-deployment-blueprint (production-template); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 5942 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours; 5942 KB substantial-repo size makes inspection immediately productive). **Cost-to-value ratio: high** (5942 KB substantial-repo size; the *aiogram + postgresql + docker + admin-panel* thirteen-tuple + the in-window-by-pushed-at-only signal + the 476★ quality signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/222-donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template-v1-aiogram-cook-bot-deployment-blueprint-HANDOFF.md` and `features/222-donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template-v1-aiogram-cook-bot-deployment-blueprint.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + aiogram + postgresql + docker + admin-panel documentation for the next v1 deployment-formalization review moment; **cross-section JTBD value is moderate-to-high, prior-rejection-then-promotion honest disclosure recorded**).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a deployment-formalization surface to the LE31 v1 cook-bot surface, a docker-based-deployment surface, an admin-panel surface, or a redis-cache surface):

- `Dockerfile` — possibly add (the containerization Dockerfile; depends on the v1 change).
- `docker-compose.yml` — possibly add (the docker-compose deployment configuration; depends on the v1 change).
- `app/admin/` — possibly add (the admin-panel web UI module; depends on the v1 change).
- `app/metrics/` — possibly add (the prometheus metrics exporter; depends on the v1 change).
- `app/models/bot_admin_users.py` — possibly add (the `bot_admin_users` SQLModel table; depends on the v1 change).
- `app/models/bot_metrics.py` — possibly add (the `bot_metrics` SQLModel table; depends on the v1 change).
- `pyproject.toml` — possibly migrate from `requirements.txt` to poetry/uv (LE31 v1 charter §3.2 currently does not pin poetry/uv; the migration is a v1 maintenance question); depends on the v1 change.
- `tests/test_admin_panel.py` + `tests/test_bot_metrics.py` + `tests/test_docker_compose.py` — possibly add (the integration tests for the admin-panel + metrics + docker-compose surfaces; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no deployment-formalization surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/222-donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template-v1-aiogram-cook-bot-deployment-blueprint.md` exists and is read back by the parent.
- [ ] `specs/222-donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template-v1-aiogram-cook-bot-deployment-blueprint-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `donbarbos/telegram-bot-template` description is quoted verbatim (5942 KB repo).
- [ ] The 476★/79⑂ + MIT permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption) + Python + in-window-by-pushed-at-only + 20 topics + description *"🤖 Template for telegram bot using postgres, pgbouncer, redis, docker, amplitude, prometheus, grafana, CI with admin panel"* is documented.
- [ ] The charter §3.1 alignment via *admin-panel = chat-bypass-admin-surface = explicit-state-transition discipline* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (MIT permissive) is documented.
- [ ] The charter §3.4 not-triggered (no AI surface) is documented.
- [ ] The HONEST DISCLOSURE of prior-rejection in `/opt/data/le31-brainstorm-2026-09-22.md` §Operator UX and HCI signals section is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds a deployment-formalization surface to the LE31 v1 cook-bot surface, a docker-based-deployment surface, an admin-panel surface, or a redis-cache surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `donbarbos/telegram-bot-template` *aiogram + postgresql + docker + admin-panel* vocabulary is evaluated against the PR's changes: does the change address the *deployment-formalization* discipline? does the change preserve the *admin-panel* primitive? does the change preserve the *observability* primitive? does the change preserve the *charter §3.1 explicit-state-transition* pattern?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 trigger (if the v1 deployment-formalization surface is adopted):**
- Disable path: feature flag `LE31_DEPLOYMENT_FORMALIZATION_ENABLED = False` (default; gates all `app/admin/` + `app/metrics/` + `Dockerfile` + `docker-compose.yml` deployment); no data loss.
- Delete path: `rm -rf Dockerfile docker-compose.yml` + `rm -rf app/admin/ app/metrics/` + `rm -rf app/models/bot_admin_users.py app/models/bot_metrics.py` + `rm -rf tests/test_admin_panel.py tests/test_bot_metrics.py tests/test_docker_compose.py`; remove any deployment-formalization-specific dependencies (aio-pika, redis, prometheus-client) from `requirements.txt`; no retained data; no safe-failure-mode concern.
- Migration/rollback cost: low (no schema change for `audit_logs` or `StockEntry`; new `bot_admin_users` + `bot_metrics` tables are independent).

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
