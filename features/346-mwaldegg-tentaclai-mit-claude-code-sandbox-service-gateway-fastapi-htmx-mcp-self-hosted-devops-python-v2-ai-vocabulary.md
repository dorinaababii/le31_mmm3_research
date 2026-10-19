# Feature 346 — mwaldegg/tentaclai (v2-AI Claude-Code-sandbox-+-service-gateway-+-FastAPI-+-HTMX-+-MCP-+-self-hosted-+-devops-vocabulary)

> **Bucket**: v2-AI (parking-lot, vocabulary reference)
> **GitHub**: https://github.com/mwaldegg/tentaclai
> **License**: MIT
> **Status (as of 2026-10-19)**: ★0 / ⑂0; 3585 KB modest; pushed 2026-10-18T (in-window; **TODAY**); created 2026-10-18T (**TODAY**); default_branch=main; archived=False
> **Topics (verbatim, 14)**: `ai-agents, automation, claude-code, devops, docker, fastapi, homelab, htmx, infrastructure, mcp, model-context-protocol, sandbox, self-hosted, ssh` = 6/14 LE31-stack-match (Python + FastAPI + HTMX + MCP + model-context-protocol + docker = the 6 LE31 v2-AI backend stack primitives; ai-agents + claude-code + sandbox + self-hosted + devops + homelab + infrastructure + ssh + automation are the 9 v2-AI agent-sandbox + service-gateway primitives)
> **Description (verbatim)**: *Sandbox + service gateway for Claude Code*
> **Cross-section**: features 232 (lpalbou/AbstractGateway, replay-first-architecture), 287-289 (noise01/endoxa + pete-builds/mcp-nixreview + shivamk01here/LedgerLoop, append-only + SMT + CVE/KEV attestation), 327 (musterhq/muster, AI-agent-harness-with-audit-ledger), 332 (vsov/xcheck, cross-agent-audit), 335 (tangwenhai839/create-qingyu, append-only-memory-gateway-with-identity-governance), 338 (agentdrover/haiplane, task-orchestrator-with-acceptance-criteria-+-named-commit), 339 (vggg/barony, git-native-governance-for-AI-coding-agents), 340 (BUGGIEEEEE/worklog, shared-append-only-work-ledger-for-AI-coding-agents), 341 (dashpilot-labs/dashpilot-mcp, MCP-server-for-delivery-aggregator-POS-bridge) = 10-pick v2-AI Claude-Code-sandbox-+-service-gateway-vocabulary cluster of the 80-pass series
> **Decision**: defer (parking-lot, vocabulary reference)
> **Parent research issue**: Research 2026-10-19 — daily (Linear MCP blocked 30th-consecutive-day; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-19.linear-fallback.json`)
> **Slice handoff**: `/opt/data/le31_mmm3_research_work/specs/346-mwaldegg-tentaclai-v2-ai-claude-code-sandbox-service-gateway-fastapi-htmx-mcp-self-hosted-devops-vocabulary-HANDOFF.md`

## Goal

When a future v2-AI LE31 workflow needs to sandbox an AI-coding-agent (e.g. Claude Code) and route its tool calls through a chokepoint service gateway, the system wants the agent to be **isolated in a sandbox** (charter §3.4 non-AI-fallback), the tool calls to be **routed through a chokepoint service gateway** (charter §3.4 chokepoint-governed), and the gateway to be **exposed as an MCP server** (charter §3.4 observable-evidence), but today's LE31 v1 has no AI-coding-agent surface; the v1 has only the waiter web UI + the cook Telegram bot.

## Evidence / JTBD

**Inferred** (vocabulary observation, not observed LE31 user pain). The pain is *possible* in any future v2-AI AI-coding-agent workflow window but is not *directly observed* in any LE31 v1 user flow today.

When a v2-AI workflow needs to sandbox an AI-coding-agent (Pick C), the operator wants the agent to be **isolated in a sandbox** + the tool calls to be **routed through a chokepoint service gateway** + the gateway to be **exposed as an MCP server** + the deployment to be **self-hosted** + the devops tooling to be **operator-friendly** (Docker + SSH + infrastructure + homelab), but struggles because today LE31 v1 has no AI-coding-agent surface.

Confidence: **medium** (1-day-old v2-AI Claude-Code-sandbox with 14 topics = most topic-rich v2-AI agent-sandbox-vocabulary of the 80-pass series = maintainer-discipline signal but no star-inflow yet; the maintainer is shipping real code with a real deployment target).

## Scope

- v2-AI only: applies to a future v2-AI AI-coding-agent workflow window (operator + staff tooling, not customer-facing).
- The transferable vocabulary is the **sandbox + service-gateway + MCP + self-hosted + devops** quintet:
  1. **Sandbox-as-isolated-execution-environment discipline** — the AI-coding-agent is isolated in a sandbox (Docker container, VM, or remote execution environment) so the agent cannot directly access the LE31 v1 system. This is the **sandbox-as-isolated-execution-environment** discipline applied to AI-coding-agent execution (charter §3.4 non-AI-fallback).
  2. **Service-gateway-as-MCP-server discipline** — the AI-coding-agent's tool calls are routed through a chokepoint service gateway exposed as an MCP server. The gateway enforces the chokepoint (charter §3.4) and exposes the tool API as MCP (charter §3.4 observable-evidence).
  3. **Self-hosted-deployment discipline** — the sandbox + service-gateway is deployed self-hosted (on a homelab, a small VM, or a self-managed cluster) rather than on a third-party cloud. This is the **self-hosted-deployment** discipline applied to AI-coding-agent execution (charter §3.4 + §3.7 GDPR-compatible).
  4. **Devops-as-operator-friendly-tooling discipline** — the deployment uses operator-friendly devops tooling (Docker for containerization, SSH for remote access, infrastructure-as-code for reproducibility, homelab for local development). This is the **devops-as-operator-friendly-tooling** discipline applied to AI-coding-agent execution.
  5. **Claude-Code-as-target-agent discipline** — the sandbox is designed specifically for Claude Code (Anthropic's AI-coding-agent). The MCP server adapter speaks the Claude Code protocol (tool calls + tool results + prompt templates). This is the **Claude-Code-as-target-agent** discipline applied to AI-coding-agent execution.
- The Python + FastAPI + HTMX + MCP stack is on-stack (charter §3.1 + §3.2 ✓); the Docker + SSH + infrastructure + homelab stack is on-stack (charter §3.1 + §3.2 + §3.7 ✓); the claude-code-specific adapter is NOT portable to LE31 (LE31 has no AI-coding-agent surface yet); the *sandbox + service-gateway + MCP + self-hosted + devops* quintuple-primitive IS portable to a generic v2-AI AI-agent surface with a §3.4 review.
- No v1 PR today; no v1 build today; no quota-filling.

## Out of scope

- v1 product surface (waiter web UI + cook Telegram bot). LE31 v1 has no AI-coding-agent surface.
- Any customer-facing AI per charter §3.4 (the tentaclai vocabulary is operator-tooling only).
- Any runtime import of tentaclai as a dependency (the tentaclai codebase is the vocabulary reference, not the code dependency).
- Any LE31-specific schema migration or model change (tentaclai is vocabulary-only; the v2-AI surface is greenfield).
- The claude-code-specific adapter is OUT (the tentaclai vocabulary is portable to a generic v2-AI AI-agent surface with a §3.4 review; the claude-code-specific code is NOT adopted).

## Description

The tentaclai vocabulary is the **Claude-Code-sandbox-+-service-gateway** decuple-primitive:

1. **Sandbox-as-isolated-execution-environment discipline** — the AI-coding-agent (Claude Code) is isolated in a sandbox (Docker container, VM, or remote execution environment). The sandbox has its own filesystem, network, and process namespace. The sandbox cannot directly access the LE31 v1 system; all access is routed through the service gateway.
2. **Service-gateway-as-MCP-server discipline** — the service gateway is the chokepoint between the sandbox and the LE31 v1 system. The gateway exposes a controlled set of tools (file read, file write, git commit, shell exec, etc.) as MCP-server tools. The gateway enforces the chokepoint (charter §3.4) and records every tool call in an audit log (charter §3.3 + §3.4 observable-evidence).
3. **Self-hosted-deployment discipline** — the sandbox + service-gateway is deployed self-hosted (on a homelab, a small VM, or a self-managed cluster). No third-party cloud is involved. The deployment is reproducible via infrastructure-as-code (Docker Compose, Ansible, Terraform, etc.).
4. **Devops-as-operator-friendly-tooling discipline** — the deployment uses operator-friendly devops tooling: Docker for containerization, SSH for remote access, infrastructure-as-code for reproducibility, homelab for local development. The operator can spin up the entire stack with a single `docker compose up` command.
5. **Claude-Code-as-target-agent discipline** — the sandbox is designed specifically for Claude Code. The MCP server adapter speaks the Claude Code protocol (tool calls + tool results + prompt templates). The adapter is pluggable so other AI-coding-agents (Codex, Cursor, etc.) can be added.
6. **HTMX-as-operator-UI discipline** — the service gateway exposes an operator-facing UI via HTMX (charter §3.1 on-stack). The operator can see the current sandbox state, the recent tool calls, the audit log, and the operator actions (pause, resume, kill, restart).
7. **FastAPI-as-backend-framework discipline** — the service gateway backend is FastAPI (Python), with Pydantic for request/response validation, SQLAlchemy for ORM, and Alembic for migrations.
8. **MCP-server-as-tool-API discipline** — the service gateway exposes the tool API as an MCP server. AI-coding-agents (Claude Code, Codex, etc.) can discover and consume the tools through the standard MCP protocol.
9. **AI-agent-as-target discipline** — the sandbox is designed to host AI-agents (not just Claude Code). The pluggable adapter design allows other AI-agents to be added with minimal changes.
10. **Audit-log-as-observable-evidence discipline** — every tool call is recorded in an audit log (charter §3.3 + §3.4 observable-evidence). The audit log is append-only and hash-chained so any tampering is detectable.

The Python + FastAPI + HTMX + MCP + docker + self-hosted + devops + claude-code + sandbox + service-gateway stack is the **most topic-rich v2-AI agent-sandbox-vocabulary of the 80-pass series** (14 topics = `ai-agents + automation + claude-code + devops + docker + fastapi + homelab + htmx + infrastructure + mcp + model-context-protocol + sandbox + self-hosted + ssh`).

## Data model

The tentaclai data model is **greenfield** (no v1 file is touched by this slice). The conceptual model is:

```
Sandbox         (id, name, status, docker_container_id, created_at, updated_at)  -- one sandbox per AI-coding-agent session
ToolCall        (id, sandbox_id, tool_name, arguments, result, audit_chain_hash, created_at)  -- append-only per charter §3.3
AuditLog        (id, sandbox_id, action, actor, details, created_at)  -- append-only per charter §3.3
OperatorAction  (id, sandbox_id, action, operator, created_at)  -- append-only per charter §3.3
```

The `audit_chain_hash` on `ToolCall` is the hash of the previous `ToolCall.audit_chain_hash` + the new tool call's contents (Merkle-linked append-only chain).

## Implementation

Not implemented today. When a v2-AI window opens, the implementation will touch:

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

## Telegram interaction

Not implemented today. When a v2-AI window opens, the Telegram interaction will be:

- The cook Telegram bot (LE31 v1) is **unchanged** by this slice (this slice is v2-AI only).
- The v2-AI surface will use the **AI-agent → MCP-server → LE31-API** flow: the AI-coding-agent calls the MCP-server endpoint, the gateway enforces the chokepoint + records the audit log, the gateway returns the result.
- The operator-facing surface (when built) will be a separate Telegram bot for **sandbox-state notifications**: when a sandbox transitions (created, paused, resumed, killed, restarted), the bot sends a notification to the operator; the operator can reply `/pause <sandbox_id>` or `/kill <sandbox_id>` to take action.

## Dependencies

- External: **Docker** (containerization), **MCP-runtime** (Model Context Protocol runtime), **Claude Code** (Anthropic's AI-coding-agent) or another AI-coding-agent that speaks MCP.
- Cross-section: features 232 (lpalbou/AbstractGateway, replay-first-architecture), 287-289 (append-only + SMT + CVE/KEV attestation), 327 (musterhq/muster, AI-agent-harness-with-audit-ledger), 332 (vsov/xcheck, cross-agent-audit), 338 (agentdrover/haiplane, task-orchestrator-with-acceptance-criteria), 339 (vggg/barony, git-native-governance), 340 (BUGGIEEEEE/worklog, shared-append-only-work-ledger) — the *sandbox + service-gateway + MCP + self-hosted + devops + audit-chain* decuple-primitive from feature 346 IS the canonical v2-AI agent-sandbox-+-service-gateway-vocabulary of the 80-pass series; together with the *task-orchestrator-with-acceptance-criteria* triple-primitive from feature 338 + the *git-native-governance* sextuple-primitive from feature 339 + the *shared-append-only-work-ledger* triple-primitive from feature 340, they form the canonical v2-AI AI-coding-agent-execution-sandbox cluster of the 80-pass series.

## Open questions

- Does LE31 v2-AI want to host AI-coding-agents (Claude Code, Codex, Cursor), or only consume MCP-served tools from external AI-coding-agents? (charter §3.4 review needed; the v2-AI surface could be either a host or a consumer.)
- Does the sandbox need to be ephemeral (per-task) or persistent (per-session)? (UX decision; ephemeral sandboxes are simpler to manage; persistent sandboxes preserve state across task boundaries.)
- Does the audit log need to be exportable (e.g. for compliance review), or is in-database storage sufficient? (charter §3.7 GDPR-compatible review needed.)
- Does the operator need real-time notifications (e.g. via Telegram) for sandbox-state transitions? (UX decision.)

## Why this matters

The tentaclai vocabulary is the **canonical v2-AI Claude-Code-sandbox-+-service-gateway-vocabulary reference of the 80-pass series**. The *sandbox + service-gateway + MCP + self-hosted + devops + claude-code* decuple-primitive IS the most topic-rich v2-AI agent-sandbox-vocabulary of the 80-pass series (14 topics; the highest topic-count of any v2-AI pick of the 80-pass series; in-window by BOTH `pushed_at` AND `created_at` on TODAY 2026-10-18 = the freshest in-window pick of the 80-pass series). The *sandbox + service-gateway + MCP + self-hosted + devops* quintuple-primitive IS the §3.4 chokepoint-governed + non-AI-fallback charter invariant applied to the AI-coding-agent-execution-sandbox dimension. When a v2-AI window opens, this vocabulary becomes the canonical reference for any LE31 v2-AI AI-coding-agent-execution-sandbox surface.
