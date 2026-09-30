# Feature 255 — `t0mer-Wazy-apache-2-0-self-hosted-telegram-bot-and-fastapi-rest-api-checks-waze-travel-times-routes-scheduled-checks-v1-self-hosted-telegram-bot-fastapi-rest-api-aiogram-deployment-blueprint-vocabulary` (defer)

> **NEW observation (2026-09-30).** Documents in-window GitHub Search `topic:telegram-bot language:python pushed:>2026-09-01` query result: `t0mer/Wazy` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, **19★/4⑂**, Python, **pushed 2026-09-30T02:08:27Z = TODAY** (in-window by `pushed_at` = strong fresh-discovery signal of the 62-pass brainstorm series), **created 2022-10-25T07:29:20Z** (~4 years before window-start = OUT-OF-WINDOW by `created_at` = in-window by push only), **repo size = 81 KB** (parent-verified via raw GitHub API JSON = tiny repo = deployment-blueprint-not-the-application discipline), `default_branch=main`, `archived=false`). Topics (verbatim, parent-verified GitHub API direct-GET 2026-09-30, **12 topics**): `bot + fastapi + telegram + telegram-bot + traffic + waze + commute + docker + python + route-planning + self-hosted + travel-time` (**3/12 topics on the literal LE31 v1 stack: `fastapi + python + telegram-bot` = on-LE31-stack-vocabulary-envelope**). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-30): *"Self-hosted Telegram bot and FastAPI REST API that checks Waze travel times for your routes, with scheduled checks and Docker"*. The **self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python** quintuple-primitive = the **canonical v1 aiogram-deployment-blueprint vocabulary** of the 62-pass brainstorm series. Net-new observation 2026-09-30 (ripgrep-confirmed unique vs features 1–253). Bucket: **v1 self-hosted-Telegram-bot + FastAPI-REST-API + aiogram-deployment-blueprint cross-section vocabulary** (parking-lot, future-v1-surface-vocabulary-reference).

## Goal

Retain the **self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python** quintuple-primitive as a persistent cross-section reference for any future LE31 v1 surface that introduces (a) **self-hosted-Telegram-bot** (the Telegram-bot runs entirely on the owner's hardware with no operator = no Telegram-Bot-hosting dependency = charter §3.1 *on-premise + Postgres single-instance* posture preserved), (b) **FastAPI-REST-API** (the bot exposes a REST API alongside the Telegram-bot surface = the *FastAPI-as-shared-API-layer* primitive applied to the *Telegram-bot-deployment* dimension), (c) **Docker** (the bot is shipped as a Docker image for easy deployment = the *Docker-as-deployment-primitive* discipline), (e) **scheduled-checks** (the bot runs scheduled checks in the background via FastAPI background-tasks or APScheduler = the *scheduled-check-primitive* applied to the *background-task* dimension), and (f) **Python** (the canonical LE31 v1 language = charter §3.1 *Python 3.13 + FastAPI + SQLModel* stack). Today's verdict is **`defer (parking-lot)`** because LE31 v1 already has the cook-Telegram-bot running on aiogram v3 + FastAPI webhook + Postgres + Docker compose (per `le31-arch-patterns/SKILL.md` + `le31-backend/SKILL.md`); the *self-hosted + Docker + FastAPI + Telegram-bot + scheduled-checks* primitive set is the **canonical vocabulary for any future v1 owner-self-hosted-deployment surface** (e.g., the *owner-self-hosted-deployment-instructions* primitive applied to the *on-premise-deployment* dimension).

## Scope

**In scope (defer artifact):**
- A written record of the **self-hosted-Telegram-bot** discipline: the *Telegram-bot-runs-on-owner-hardware-no-operator* primitive applied to the *Telegram-bot-deployment* dimension (LE31 v1's cook-bot already uses this discipline per charter §3.1).
- A written record of the **FastAPI-REST-API** discipline: the *bot-exposes-REST-API-alongside-Telegram-bot-surface* primitive applied to the *shared-API-layer* dimension (LE31 v1's cook-bot uses the FastAPI webhook + REST endpoints; this pick confirms the *FastAPI-REST-API + Telegram-bot* discipline is the canonical deployment blueprint).
- A written record of the **Docker** discipline: the *bot-shipped-as-Docker-image-for-easy-deployment* primitive applied to the *deployment* dimension (LE31 v1's cook-bot is shipped as a Docker container per `le31-backend/SKILL.md`; this pick confirms the *Docker* discipline is canonical).
- A written record of the **scheduled-checks** discipline: the *bot-runs-scheduled-checks-in-background-via-FastAPI-background-tasks-or-APScheduler* primitive applied to the *background-task* dimension.
- A written record of the **Python** discipline: charter §3.1 explicit *Python 3.13* stack.
- A decision record: today's verdict is `defer` because LE31 v1 already has the cook-Telegram-bot running on this exact primitive set; the cross-section reference is informative, not a v1 build-trigger.
- A cross-section reference with the prior v1 self-hosted-Telegram-bot + FastAPI-REST-API + aiogram-deployment-blueprint cluster: features 02, 03, 09, 22, 116, 158, 170, 173, 176, 195, 200, 205, 223, 224, 225, 239, 240, 248, 251. The *transferable insight* is the **self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python** quintuple-primitive.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any v2-AI surface in v1 (charter §3.4 explicit invariant).
- Any v1 aiogram-cook-bot-deployment surface change (LE31 v1's cook-bot is already deployed with this exact primitive set; the artifact is vocabulary-only, not a deployment-change).

## Description

The pick is **`t0mer/Wazy`** — a Python + Apache-2.0 + self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python vocabulary artifact. **Charter §3.1 + §3.2 STRICTLY-COMPATIBLE** (Apache-2.0 permissive + 19★/4⑂ community traction + 81 KB tiny-deployment-blueprint + 2022-10-25 created + 2026-09-30 fresh-push-TODAY = sustained-active-developer signal = **3/12 topics on the literal LE31 v1 stack** = on-LE31-stack-vocabulary-envelope). The artifact is the persistent cross-section reference for the verbatim description + the 5 named primitives + the 12 topics.

**Why the *in-window by `pushed_at` only + TODAY-fresh-push + 81 KB tiny* matters**: the `pushed_at=2026-09-30T02:08:27Z = TODAY` = strong fresh-discovery signal; the `created_at=2022-10-25T07:29:20Z` = ~4 years before window-start = OUT-OF-WINDOW by `created_at` = in-window by push only; the 81 KB tiny-repo size + 19×/4⑂ community traction + 12 topics = the *smallest-repo + deployment-blueprint-not-the-application* pick of the 62-pass brainstorm series. The 81 KB size signals *deployment-blueprint-not-the-application* discipline — the *value* is the *primitive set* (self-hosted + Docker + FastAPI + Telegram-bot + scheduled-checks), not the *application* (Waze travel time checking). The artifact is the persistent cross-section reference for the **self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python** quintuple-primitive, not just for the verbatim description.

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v1 surface that adopts the *self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python* primitive would extend the LE31 v1 data model with appropriate new tables (e.g., a `ScheduledCheck` SQLModel table with `scheduled_check_id, check_name, check_type, check_interval_seconds, last_run_at, next_run_at, created_at`; a `DeploymentBlueprint` SQLModel table with `deployment_blueprint_id, blueprint_name, blueprint_docker_image, blueprint_docker_compose_path, blueprint_owner_instructions, created_at`). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v1 PR is triggered by the trigger condition below, the implementation would:
1. Read the `t0mer/Wazy` README at https://github.com/t0mer/Wazy for the *self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python* quintuple-primitive.
2. Cross-reference with LE31 v1's existing cook-bot Docker-compose deployment to identify the *delta* (the *delta* = `t0mer/Wazy` introduces *self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks* discipline that LE31 v1's cook-bot already implements per `le31-backend/SKILL.md`; the *delta* is mostly zero, but the *deployment-blueprint-as-documentation* discipline = the *owner-self-hosted-deployment-instructions* primitive applied to the *on-premise-deployment* dimension).
3. Apply charter §3.1 *Python 3.13 + FastAPI + SQLModel + Postgres + aiogram v3 + on-premise* posture review to the *delta* (LE31 v1's existing cook-bot already satisfies charter §3.1; the artifact is a *deployment-blueprint-vocabulary-reference*, not a charter-3.3-required decision).
4. Document the deployment blueprint in `features/255-*.md` + `specs/255-*-HANDOFF.md`; the `t0mer/Wazy` reference is the *vocabulary* for *self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python*, NOT for *cook-bot replacement*.

## Telegram interaction

This is a vocabulary reference — no Telegram interaction changes today. The future v1 surface that adopts this vocabulary would not add a new Telegram-bot-command surface (the deployment-blueprint is a deployment-primitive, not a bot-command-primitive). The existing cook-Telegram-bot surface (charter §3.1) is not affected; the artifact documents the *deployment-blueprint* that the cook-bot is already deployed with.

## Dependencies

- Read-only reference to `t0mer/Wazy` at https://github.com/t0mer/Wazy (no installation, no import).
- Future v1 surface that adopts the vocabulary would require: FastAPI (already in LE31 v1 stack), aiogram v3 (already in LE31 v1 stack), SQLModel (already in LE31 v1 stack), Postgres (already in LE31 v1 stack), Docker (already in LE31 v1 deployment per `le31-backend/SKILL.md`), Docker-compose (already in LE31 v1 deployment per `le31-backend/SKILL.md`), APScheduler or FastAPI-background-tasks (likely needed for scheduled-checks primitive; charter §3.1 known-conflict note on background-tasks).
- No new infrastructure today.

## Open questions

1. **Does the v1 surface adopt the deployment-blueprint-as-documentation discipline?** LE31 v1's cook-bot is already deployed with this exact primitive set; the artifact is informative, not a deployment-change.
2. **What is the APScheduler-vs-FastAPI-background-tasks tradeoff?** This pick uses APScheduler (likely); LE31 v1's cook-bot uses FastAPI-background-tasks per `le31-backend/SKILL.md`. The *APScheduler-vs-FastAPI-background-tasks* tradeoff is a future v1 design decision.
3. **What is the Docker-compose-vs-Docker-Swarm-vs-Kubernetes tradeoff?** This pick uses Docker-compose (likely); LE31 v1's cook-bot uses Docker-compose per `le31-backend/SKILL.md`. The *Docker-compose-vs-Docker-Swarm-vs-Kubernetes* tradeoff is a future v1 deployment-scale decision.
4. **What is the on-premise-vs-cloud tradeoff?** This pick uses on-premise (self-hosted); LE31 v1's charter §3.1 *on-premise + Postgres single-instance* posture preserves on-premise as the default. The *on-premise-vs-cloud* tradeoff is a future charter-§3.1 design decision.

## Why this matters

The **self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python** quintuple-primitive is the **canonical v1 aiogram-deployment-blueprint vocabulary** of the 62-pass brainstorm series. The 81 KB tiny-repo size signals *deployment-blueprint-not-the-application*; the TODAY fresh-push + 12 topics + 19★/4⑂ community traction = the *3/12-topics-on-literal-LE31-v1-stack* pick of the 62-pass brainstorm series (the on-LE31-stack-vocabulary-envelope is strong). The *self-hosted + Docker + FastAPI + Telegram-bot + scheduled-checks* discipline = the **canonical charter §3.1 alignment** (Python 3.13 + FastAPI + Postgres + aiogram v3 + on-premise posture preserved). The Apache-2.0 license makes this the **STRICTLY-ADOPTABLE v1 aiogram-deployment-blueprint primitive** (charter §3.2 STRICTLY-COMPATIBLE). The brainstorm value is the **self-hosted-Telegram-bot + FastAPI-REST-API + Docker + scheduled-checks + Python** quintuple for any future v1 owner-self-hosted-deployment surface. **Trigger for re-evaluation**: first v1 PR that proposes an owner-self-hosted-deployment-instructions surface; OR first v1 PR that proposes a deployment-blueprint-as-documentation discipline; OR first v1 PR that proposes an APScheduler-vs-FastAPI-background-tasks migration.