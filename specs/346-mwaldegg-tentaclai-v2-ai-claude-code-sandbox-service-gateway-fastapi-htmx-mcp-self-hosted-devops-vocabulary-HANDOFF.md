# Slice Handoff — Feature 346 (mwaldegg/tentaclai)

> **Feature ID**: 346
> **Feature path**: `/opt/data/le31_mmm3_research_work/features/346-mwaldegg-tentaclai-mit-claude-code-sandbox-service-gateway-fastapi-htmx-mcp-self-hosted-devops-python-v2-ai-vocabulary.md`
> **Decision**: defer (parking-lot, vocabulary reference)
> **Bucket**: v2-AI

## LE31 feature gate verdict (carried from feature contract)

- **Evidence precondition**: inferred (vocabulary observation, not observed LE31 user pain). Confidence: medium.
- **Seven checks**:
  1. **JTBD**: When a v2-AI workflow needs to sandbox an AI-coding-agent (Pick C), the operator wants the agent to be isolated in a sandbox + the tool calls to be routed through a chokepoint service gateway + the gateway to be exposed as an MCP server + the deployment to be self-hosted + the devops tooling to be operator-friendly.
  2. **Viability**: medium — the *sandbox + service-gateway + MCP + self-hosted + devops* discipline is operator-readable but requires a v2-AI workflow window + charter §3.4 review.
  3. **Practicability and confidence**: Python ✓ ON-STACK + FastAPI ✓ ON-STACK + HTMX ✓ ON-STACK + MCP ✓ ON-STACK + self-hosted ✓ ON-STACK + devops ✓ ON-STACK; confidence: high for the v2-AI surface.
  4. **Conflict**: no hard conflict with any charter invariant. v2-AI bucket pick; the `le31 v2-AI` project does NOT exist in the workspace, so this pick attaches to `le31 Research` P-HMM-1 as parent of the sub-issue.
  5. **Outcome / appetite / scope**: v2-AI outcome; 0 build time today; max 4 weeks if a v2-AI window opens (1 week to specify, 1 week to plan, 2 weeks to build + verify).
  6. **Cost to operational value**: low RICE; not a v1 PR candidate.
  7. **Circuit breaker / reversibility**: fully reversible (vocabulary-only artifact; no code adoption).
- **Decision**: **defer (parking-lot, vocabulary reference)**.

## Files this slice will touch (when implemented)

> Not implemented today. When a v2-AI window opens, the implementation will touch:

- `app/v2/ai/sandbox/__init__.py` — new package
- `app/v2/ai/sandbox/models.py` — `Sandbox` + `ToolCall` (append-only per charter §3.3) + `AuditLog` (append-only) + `OperatorAction` (append-only) SQLModel tables
- `app/v2/ai/sandbox/docker_manager.py` — the Docker container lifecycle manager (create, start, stop, kill, restart)
- `app/v2/ai/sandbox/mcp_server.py` — the MCP server adapter (exposes the tool API as MCP tools)
- `app/v2/ai/sandbox/router.py` — the FastAPI router under `/v2/ai/sandbox` with CRUD endpoints + MCP-server adapter
- `app/v2/ai/sandbox/templates/` — the HTMX templates for the operator-facing sandbox-UI (current state, recent tool calls, audit log, operator actions)
- `app/v2/ai/sandbox/tests/` — verify the sandbox isolation (the agent cannot directly access the LE31 v1 system) + verify the chokepoint (every tool call is routed through the gateway) + verify the audit chain (every tool call is recorded and hash-chained)
- `migrations/` — alembic migration for the new tables
- `docker-compose.yml` — the self-hosted deployment configuration (FastAPI + Postgres + Docker)

> **Greenfield**: no existing v1 files are touched by this slice (LE31 v1 has no AI-coding-agent surface).

## Verification protocol (when implemented)

1. Run `pytest app/v2/ai/sandbox/tests/` and verify all tests pass.
2. Manually create a sandbox via the FastAPI router; verify the Docker container is created and started.
3. Manually run a tool call (e.g. file read) via the MCP-server endpoint; verify the tool call is routed through the gateway (not directly to the LE31 v1 system).
4. Manually run a tool call that exceeds the sandbox's allowed tools; verify the gateway returns HTTP 403 with a descriptive error (chokepoint enforcement).
5. Manually tamper with a `ToolCall.audit_chain_hash`; verify the `verify_audit_chain` function returns False (audit-chain integrity violation).
6. Manually pause/resume/kill/restart a sandbox via the operator UI; verify the Docker container transitions correctly.
7. Verify the HTMX sandbox-UI renders the current state + the recent tool calls + the audit log + the operator actions.
8. Verify the MCP-server endpoint returns the tool list (the MCP-server adapter is correctly wired).

## Rollback path

- `git revert <commit-hash>` to remove the v2-AI AI-coding-agent-execution-sandbox surface.
- `alembic downgrade -1` to drop the new tables.
- `docker compose down` to stop the Docker containers.
- No v1 data is affected (greenfield; no migration of existing v1 data).
- All `ToolCall` rows are append-only per charter §3.3; they remain in the audit trail even after the rollback (the rollback only removes the application code, not the audit data).

## Mandatory LE31 skill list for the external coding agent

Before starting, the external coding agent MUST load these skills:

1. **`le31-conventions`** — the global LE31 decision layer + feature gate + hard invariants.
2. **`le31-v1-feature-pattern`** — the canonical contract shape + slicing rules + definition of done.
3. **`le31-handoff-spec`** — the handoff discipline + frozen contract + verification protocol.
4. **`le31-coding-agent-brief`** — the paste-in prompt template that produces the slice prompt from this HANDOFF.
5. **`le31-research`** — the research workflow + evidence-before-recommendation discipline.
6. **`development`** — the generic code-development pipeline (specify → plan → tasks → implement).

## Trigger policy for the external coding agent

- **DO NOT start** until a v2-AI workflow window opens in the LE31 charter roadmap.
- **DO NOT start** until a future v2-AI PR proposes an AI-coding-agent-execution-sandbox surface, an MCP-server adapter for the LE31 API, a Docker-based sandbox lifecycle manager, or a self-hosted-deployment discipline for an AI-coding-agent.
- **DO NOT start** until the charter §3.4 review has been completed.
- When triggered, mirror back the frozen contract fields (feature ID, decision, bucket, files to touch, verification protocol) before implementing; stop if the mirror-back does not match.

## External-context Linear reference

- Parent research issue: Research 2026-10-19 — daily (Linear MCP BLOCKED 30th consecutive day; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-19.linear-fallback.json` documents the intended parent + 3 sub-issues).
- This feature: Feature 346 — mwaldegg/tentaclai (intended sub-issue in `le31 Research` P-HMM-1).

## Sign-off gap

- External agent has NOT yet been dispatched.
- Charter §3.4 review has NOT yet been completed.
- v2-AI workflow window has NOT yet opened.
- No v1 PR today.
