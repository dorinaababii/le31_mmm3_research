# 308-manwithacat-dazzle — HANDOFF

> **Slice for the coding agent.** Read this *and* `features/308-manwithacat-dazzle-mit-semantic-substrate-ai-collaborative-software-fastapi-htmx-pydantic-starlette-v1-hypermedia-fastapi-stack-shape-vocabulary.md` before touching any code. Do not paste chat excerpts back into the build.
>
> **Defer artifact (no code today).** This is a parking-lot vocabulary reference. There is no build candidate. The HANDOFF documents what the trigger condition would be and what the slice would look like if the trigger fires.

## Frozen identifiers (do not rename)

- Feature ID: `308`
- Slug: `manwithacat-dazzle-v1-hypermedia-fastapi-stack-shape`
- Contract file: `features/308-manwithacat-dazzle-mit-semantic-substrate-ai-collaborative-software-fastapi-htmx-pydantic-starlette-v1-hypermedia-fastapi-stack-shape-vocabulary.md`
- Bucket: **v1 (hypermedia-FastAPI-stack-shape-vocabulary)** — build verdict `defer`
- Linear parent (intake only — Linear is currently BLOCKED): **intended** `Research 2026-10-12 — daily` (parent fallback at `/opt/data/le31-daily-research-2026-10-12.linear-fallback.json`)
- Linear sub-issue (intake only): **intended** `Research 2026-10-12 / Pick A — v1 hypermedia-FastAPI-stack-shape-vocabulary (manwithacat/dazzle)` with label `Feature`, project `le31 Research` (per `le31-feature-pipeline/SKILL.md` line 33 — `le31 v1` exists as a project; use that, NOT `le31 Research`); state `Triage`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition: **observed** (verified in-window by parent re-parse of `gsearch4.json` raw JSON; the description names the `semantic-substrate + AI-collaborative-software` framing; the topics list `ai-agent + fastapi + htmx + hypermedia + pydantic + saas-platform + starlette` = 4/4 LE31-stack-match).

**Confidence:** **high** for the 4/4 LE31-stack-match (all 4 of LE31's primary stack components appear in the topics verbatim); **medium** for the semantic-substrate match (the description is short; the *semantic-substrate* framing is the value but the implementation is tied to a specific substrate model); **low** for transferability (LE31 v1 has no AI agent; the v2-AI surface is OFF v1 charter; 162020 KB substantial repo is 3rd-largest in-window v1 hypermedia-stack-shape peer of the 74-pass series but could be abandoned; the 4★ is the highest in-window star count of any net-new in-domain non-watchlist of the 74-pass series, but 4★ is still a small community-traction signal).

**Decision: defer (parking-lot, vocabulary reference).** Sister-shape to features 232 + 286 (admin interface) + 35+86+158+222+230+232+260+261 (djust-org/djust — AI-coding-agent orchestrator). No build today; the *semantic-substrate + AI-collaborative-software + 4/4 LE31-stack-match* vocabulary is a persistent cross-section reference for any future v1 polish surface that requires an AI-assisted owner-side workflow.

## Trigger condition (when to un-defer)

This slice un-defers if AND ONLY IF all of the following are true:

1. The first v1 polish PR that introduces an AI-assisted owner-side workflow lands (e.g., a v1 polish that adds an AI-assisted owner-side workflow like "the owner uses the LE31 web UI to query the daily recap; the AI assistant proposes queries; the owner reviews and confirms; the queries are executed against the semantic-substrate").
2. The proposed workflow requires a *semantic-substrate* (a JSON document store that the AI agent can read + propose queries against).
3. The proposed workflow requires a *4/4 LE31-stack-match* (FastAPI + HTMX + Pydantic + Starlette) primitive for the AI-collaborative-software surface.
4. Charter §3.4 *non-AI-fallback + human-gate* invariant can be maintained (the AI agent must be operator-confirmed, not autonomous).

If the trigger condition is met, follow the slice plan below.

## Slice plan (if trigger fires)

### Files to touch

1. **New** `app/db/migrations/2026_XX_XX_add_semantic_substrate.py` (Alembic migration): add the `semantic_substrate` table.
2. **New** `app/db/migrations/2026_XX_XX_add_ai_agent_session.py` (Alembic migration): add the `ai_agent_session` table.
3. **New** `app/db/migrations/2026_XX_XX_add_query_confirmation.py` (Alembic migration): add the `query_confirmation` table.
4. **New** `app/api/semantic_substrate.py`: implement `GET /v1/semantic-substrate/{entity_type}/{entity_id}` + `POST /v1/semantic-substrate/{entity_type}/{entity_id}/update`.
5. **New** `app/api/ai_agent.py`: implement `POST /v1/ai-agent/sessions` + `POST /v1/ai-agent/sessions/{id}/confirm-query` + `GET /v1/ai-agent/sessions/{id}/results`.
6. **New** `app/bot/handlers/ai_agent.py`: implement the `ai_query_confirmation_request` Telegram handler.
7. **Update** `app/templates/owner/dashboard.html`: add the AI-agent panel UI.
8. **Update** `app/db/__init__.py`: register the new SQLModel classes.
9. **Update** `app/main.py`: include the new routers.

### Schema additions (Alembic migrations)

1. `semantic_substrate` table: `id` (UUID PK), `entity_type` (str), `entity_id` (UUID), `attributes` (JSON), `created_at` (DateTime TZ), `updated_at` (DateTime TZ). Index on `(entity_type, entity_id)`.
2. `ai_agent_session` table: `id` (UUID PK), `owner_id` (UUID FK to `User`), `started_at` (DateTime TZ), `ended_at` (DateTime TZ nullable), `proposed_queries` (JSON), `confirmed_queries` (JSON).
3. `query_confirmation` table: `id` (UUID PK), `session_id` (UUID FK to `ai_agent_session`), `proposed_query` (str), `confirmed_by` (str nullable), `confirmed_at` (DateTime TZ nullable), `executed_at` (DateTime TZ nullable), `result_count` (int nullable). Index on `session_id`.

### Verification protocol

Per `le31-daily-research/SKILL.md` + `le31-conventions/SKILL.md` + `le31-v1-feature-pattern/SKILL.md`:

1. Run `pytest app/tests/test_semantic_substrate.py` (new test file). Confirm 100% pass.
2. Run `pytest app/tests/test_ai_agent.py` (new test file). Confirm 100% pass.
3. Manually exercise the end-to-end acceptance path: log in as owner → open the AI-agent panel → propose a query → confirm via Telegram → verify the query is executed against the semantic-substrate.
4. Inspect the `query_confirmation` table to confirm the confirmation is recorded with `confirmed_by = owner_telegram_id` + `confirmed_at = now()`.
5. Inspect the `semantic_substrate` table to confirm the `attributes` JSON is updated correctly.
6. Confirm charter §3.4 invariant is maintained: the AI agent must be operator-confirmed, not autonomous.

### Rollback path

1. Revert the Alembic migrations: `alembic downgrade -1` (3x).
2. Delete the new files: `app/api/semantic_substrate.py` + `app/api/ai_agent.py` + `app/bot/handlers/ai_agent.py`.
3. Revert the `app/main.py` + `app/db/__init__.py` + `app/templates/owner/dashboard.html` updates.
4. Verify: `pytest` passes with no test errors.
5. The semantic-substrate is vocabulary-only; the rollback is safe (no data loss beyond the dropped tables).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job on 2026-10-12).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).
6. `le31-research` (so the agent understands the research methodology that produced this pick).
7. `le31-coding-agent-brief` (so the agent uses the standard brief shape).

## Handoff summary

This is a **defer / parking-lot / vocabulary reference**. No build today. The slice un-defers only when the trigger condition is met. Until then, the artifact is documentation only.

**Sign-off gap:** none. The defer artifact is complete. The trigger condition is explicit. The slice plan is explicit. The verification protocol is explicit. The rollback path is explicit.

---

## Sign-off

- [x] Feature gate verdict is recorded (defer).
- [x] Feature contract (`features/308-...md`) is linked.
- [x] Mandatory LE31 skill list is named.
- [x] Trigger condition is explicit.
- [x] Verification protocol and rollback path are present (for the un-defer scenario).
- [x] Status matches the Linear fallback JSON.
