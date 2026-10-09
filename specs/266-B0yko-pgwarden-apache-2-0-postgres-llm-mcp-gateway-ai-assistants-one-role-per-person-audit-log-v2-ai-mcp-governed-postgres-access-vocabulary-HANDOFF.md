# Pick A — `B0yko/pgwarden` — v2-AI MCP-governed-Postgres-access-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research/features/266-B0yko-pgwarden-apache-2-0-postgres-llm-mcp-gateway-ai-assistants-one-role-per-person-audit-log-v2-ai-mcp-governed-postgres-access-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2-AI PR that adds a `McpServer` SQLModel table (`server_id, server_name, server_endpoint, server_oauth_client_id, server_oauth_client_secret_hash, recorded_at`).
2. First v2-AI PR that adds a `Persona` SQLModel table (`persona_id, persona_name, persona_postgres_role, persona_oauth_subject, recorded_at`).
3. First v2-AI PR that adds a `ToolInvocation` SQLModel table (`invocation_id, mcp_server_id, persona_id, tool_name, tool_input_hash, tool_output_hash, recorded_at`).
4. First v2-AI PR that adds a `PostgresRole` SQLModel table (`role_id, role_name, role_privileges_json, role_owner_persona_id, recorded_at`).
5. First v2-AI PR that extends the existing `audit_logs` table with `tool_invocation_id` + `mcp_server_id` + `tool_name` + `tool_input` + `tool_output` columns.
6. First v2-AI PR that adds a `/mcp list-servers` / `/mcp invoke <server_id> <tool_name>` / `/mcp audit <invocation_id>` Telegram command set on the cook-bot (operator-tooling only; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**).
7. First v2-AI PR that adds a Hermes Agent MCP-server integration that exposes the existing Postgres database to AI agents via per-principal-least-privilege + database-enforced authorization.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v2-AI surface (owner-AI assistance) wants to expose the existing Postgres database to AI agents, it wants per-principal least-privilege + OAuth 2.1 + OIDC + MCP-gateway + database-enforced authorization, but struggles because the current LE31 has no per-principal-role-discipline + no AI-agent-tool-invocation surface + no MCP-server surface, so that the *MCP-governed-Postgres-access-for-AI-assistants* primitive becomes a future-v2-AI surface-extension recipe."* — PASS (links to features 03 + 121 + 198 + 199 + 232 + 236 + 237 + 257 + 258 + 264; justifies a new pain).
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the *AI-agent-tool-invocation-audit* + *per-principal-least-privilege* outputs. PASS.
3. **Practicability and confidence** — Apache-2.0 permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 not triggered (operator-tooling; no customer-facing AI); §3.7 privacy-aligned (one Postgres role per person = per-principal least-privilege); confidence **high** for vocabulary transferability, **low** for immediate LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling only; §3.1 explicit-state-transitions preserved; §3.2 Apache-2.0 permissive; §3.7 per-person least-privilege. PASS.
5. **Outcome, appetite, and scope** — **v2-AI** outcome (cross-section to features 03+121+198+199+232+236+237+257+258+264). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today (LE31 has no v2-AI surface yet); pain is forecast for v2-AI adoption era. Implementation cost = low-medium (~50-100 lines of SQLModel + MCP-server code; 2-3 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/mcp_server.py` (new) — `McpServer` + `Persona` + `ToolInvocation` + `PostgresRole` SQLModel tables
- `le31/app/services/mcp_server.py` (new) — service layer for `register_mcp_server` + `register_persona` + `record_tool_invocation` + `lookup_postgres_role`
- `le31/app/hermes/hooks/mcp_gateway.py` (new) — Hermes Agent hook integration that exposes the existing Postgres database to AI agents via per-principal-least-privilege + database-enforced authorization
- `le31/app/api/v1/mcp_server.py` (new) — HTTP endpoints: `GET /api/mcp/servers` + `POST /api/mcp/servers/<server_id>/invoke` + `GET /api/mcp/audit/<invocation_id>`
- `le31/app/cook_bot/handlers/mcp_server.py` (new) — Telegram command handlers: `/mcp list-servers` + `/mcp invoke <server_id> <tool_name>` + `/mcp audit <invocation_id>` (operator-tooling only; NOT customer-facing)
- `le31/migrations/versions/<revision>_mcp_server.py` (new) — Alembic migration for the four new tables + the new `audit_logs` columns
- `skills/le31-conventions/SKILL.md` — append the *MCP-gateway + OAuth 2.1 + OIDC + one-Postgres-role-per-person + database-enforced* posture as a §3.1-aligned + §3.7-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the four new tables + revert the new `audit_logs` columns
- **Revert the MCP-server service** (remove the `le31/app/services/mcp_server.py` file + remove the import from `le31/app/services/__init__.py`)
- **Revert the Hermes Agent hook** (remove the `le31/app/hermes/hooks/mcp_gateway.py` file + remove the hook registration from `le31/app/hermes/hooks/__init__.py`)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/mcp_server.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the Telegram command handlers** (remove the `le31/app/cook_bot/handlers/mcp_server.py` file + remove the registration from `le31/app/cook_bot/handlers/__init__.py`)
- **No data loss** if the rollback happens BEFORE any `ToolInvocation` row is written
- **Full data retention** if the rollback happens AFTER rows are written (the four tables are dropped but the `ToolInvocation` rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked] (workspace plan-limit error — 14th consecutive day; verified today via `save_issue` write-probe with requestId `a449f6e6bc89bb71`; parent fallback at `/opt/data/le31-daily-research-2026-10-03.linear-fallback.json`)
