# Feature 338 — agentdrover/haiplane (v2-AI task-orchestrator-with-acceptance-criteria-+-FastAPI-+-HTMX-+-MCP)

> **Bucket**: v2-AI (parking-lot, vocabulary reference)
> **GitHub**: https://github.com/agentdrover/haiplane
> **License**: MIT
> **Status (as of 2026-10-18)**: ★0 / ⑂0; 12840 KB modest; pushed 2026-10-18T06:32:55Z (TODAY); created 2026-08-23T21:48:12Z (~56 days old); default_branch=main; archived=False
> **Topics (verbatim, 10)**: `agentic-workflows, ai-agents, developer-tools, fastapi, htmx, llm, mcp, model-context-protocol, python, task-orchestration` = 5/10 LE31-stack-match = `python + fastapi + htmx + mcp + model-context-protocol` = the strongest in-window 2026-10 v2-AI task-orchestrator-with-acceptance-criteria-and-named-commit FastAPI + HTMX + MCP vocabulary of the 79-pass series
> **Description (verbatim)**: *Task orchestrator for development with AI agents — a task is not ready without acceptance criteria, and not done until the hub can name the commit that shipped it.*
> **Cross-section**: features 316/322 (the-vibey-project/vibey, which uses append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review quad-primitive), 187/188 (traust-security/traust-ledger), 232 (lpalbou/AbstractGateway), 287/288/289 (noise01/endoxa + pete-builds/mcp-nixreview + shivamk01here/LedgerLoop), 327 (musterhq/muster), 332/333/334 (vsov/xcheck + FlashyLabs/flashy-ledger + donaldrichard19-LVD/pattern-mcp)
> **Decision**: defer (parking-lot, vocabulary reference)
> **Parent research issue**: Research 2026-10-18 — daily (Linear MCP blocked; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-18.linear-fallback.json`)
> **Slice handoff**: `/opt/data/le31_mmm3_research_work/specs/338-agentdrover-haiplane-v2-ai-task-orchestrator-with-acceptance-criteria-and-named-commit-fastapi-htmx-mcp-HANDOFF.md`

## Goal

When a future v2-AI LE31 workflow needs to coordinate multiple AI agents on a multi-step restaurant operations task (e.g. weekly inventory reconciliation + supplier ordering + tax-summary drafting), the system wants every agent action to be **bounded by explicit acceptance criteria** and every completed task to be **verifiable by the named commit that shipped it**, but today's LLM agent loops operate without acceptance gates and without commit-level provenance, so that workflow audit trails are incomplete and the owner cannot reconstruct what each agent did or why.

## Evidence / JTBD

**Inferred** (vocabulary observation, not observed LE31 user pain). The pain is *possible* in any future v2-AI workflow window but is not *directly observed* in any LE31 v1 user flow today.

When a v2-AI agent assists the owner/staff with a multi-step workflow, the operator wants every agent action to be **bounded by acceptance criteria** (Pick A: haiplane), **governed by a persona-charter** (Pick B: barony), and **logged in a shared append-only work ledger** (Pick C: worklog), but struggles because today AI agents operate without explicit acceptance gates, without persona-charters, and without cross-session-persistent-context, so that the workflow audit trail is incomplete and the operator cannot reconstruct what the agent did or why.

Confidence: **medium** (the maintainer is shipping real code = the primitives are working in production; the vocabularies are transferable to a Python+FastAPI+Postgres+SQLModel+aiogram v3 stack with a charter §3.4 review).

## Scope

- v2-AI only: applies to a future v2-AI workflow window (operator + staff tooling, not customer-facing).
- The transferable vocabulary is the **task-orchestrator-with-acceptance-criteria-and-named-commit discipline**: every task must have explicit acceptance criteria before the agent can start; every task is not done until the system can name the commit (or StockEntry, or audit log entry) that shipped it.
- The Python + FastAPI + HTMX + MCP stack is portable to LE31 v2-AI with a charter §3.4 review (AI-sandbox-as-auditable-test + non-AI-fallback + observable-evidence).
- No v1 PR today; no v1 build today; no quota-filling.

## Out of scope

- v1 product surface (waiter web UI + cook Telegram bot). LE31 v1 has no AI agent surface.
- Any customer-facing AI per charter §3.4 (the haiplane vocabulary is operator-tooling only).
- Any runtime import of haiplane as a dependency (the haiplane codebase is the vocabulary reference, not the code dependency).
- Any LE31-specific schema migration or model change (haiplane is vocabulary-only; the v2-AI surface is greenfield).

## Description

The haiplane vocabulary is the **task-orchestrator-with-acceptance-criteria-and-named-commit** triple-primitive:

1. **Acceptance-criteria-first task design** — every task in the orchestrator must have explicit acceptance criteria before the AI agent can begin. The orchestrator rejects tasks without acceptance criteria. This is the **acceptance-criteria-as-implicit-state-transition-validator** discipline applied to AI-agent-task-management.
2. **Named-commit-as-completion-evidence** — every task is not done until the hub can name the commit (or the database write, or the audit log entry) that shipped it. The orchestrator refuses to mark a task done without the commit reference. This is the **commit-named-as-completion-evidence** discipline applied to AI-agent-task-management.
3. **MCP-server-as-task-API** — the orchestrator exposes its task API as an MCP server (Model Context Protocol), so AI agents (Claude Code, Codex, etc.) can discover and consume tasks through the standard MCP protocol. This is the **MCP-server-as-tool-API** discipline applied to AI-agent-task-management.

The Python + FastAPI + HTMX + MCP stack is the strongest in-window 2026-10 v2-AI task-orchestrator-with-acceptance-criteria FastAPI + HTMX + MCP primitive of the 79-pass series.

## Data model

No LE31 schema change today. The haiplane vocabulary is operator-tooling infrastructure that would be introduced in a future v2-AI window. The data model for a future haiplane-style v2-AI orchestrator would be:

- `Task` — id, title, description, acceptance_criteria (JSONB), status (open/in_progress/done), assigned_agent_id, completed_commit_sha (nullable), created_at, completed_at
- `AcceptanceCriterion` — id, task_id, criterion_text, verified_by (nullable), verified_at (nullable)
- `TaskCompletionAudit` — id, task_id, commit_sha, evidence_url, verified_by, created_at (append-only per charter §3.3)

All three tables would be append-only per charter §3.3. The `TaskCompletionAudit` is the **charter §3.3 audit-log-immutability** primitive applied to AI-agent-task-completion.

## Implementation steps

Not implemented today (parking-lot). When a v2-AI window opens, the implementation would be:

1. Add a `tasks` SQLModel table with the schema above.
2. Add a FastAPI router under `/v2/ai/tasks` with CRUD endpoints + the MCP-server adapter.
3. Add an HTMX template for the operator-facing task-board UI.
4. Add a Telegram bot command surface for the cook-facing task-update surface (if applicable to a future v2-AI cook workflow).
5. Add a `commit_named_as_completion_evidence` validator that rejects task-completion POSTs without a `commit_sha` reference.
6. Add an integration test that verifies the orchestrator rejects tasks without acceptance criteria + rejects task-completion without a commit reference.

## Telegram interaction

If a future v2-AI cook workflow adopts haiplane vocabulary, the cook Telegram bot would gain:
- `/tasks` — list the cook's open tasks + acceptance criteria
- `/task_done <task_id> <commit_sha>` — mark a task done with the commit reference
- `/task_progress <task_id>` — report task progress

The `/task_done` command enforces the **commit-named-as-completion-evidence** discipline at the cook-side.

## Dependencies

- A future v2-AI window opening (no v1 PR today).
- Charter §3.4 review (AI-sandbox-as-auditable-test + non-AI-fallback + observable-evidence).
- The haiplane codebase is the vocabulary reference; no runtime dependency on the haiplane project itself.
- The MCP-server protocol is the standard Model Context Protocol (Python SDK = `mcp` package on PyPI).

## Open questions

- Is the LE31 v2-AI workflow window opening in 2026-Q4 or later? (parent has no visibility into the charter roadmap).
- Does a future v2-AI cook workflow actually need a task-orchestrator, or is the cook-side simpler than the operator-side? (the haiplane vocabulary is primarily operator-side).
- Does a future v2-AI owner workflow need a task-orchestrator with acceptance-criteria-and-named-commit, or is the existing v1 `audit_logs` append-only ledger sufficient for owner-side audit? (likely yes for any multi-step workflow).
- Should the haiplane vocabulary be combined with the barony vocabulary (Pick B) for persona-charter-governed acceptance-criteria, or should they be adopted independently? (likely independently first, then combined).

## Why this matters

The haiplane vocabulary is the **canonical acceptance-criteria-and-named-commit discipline** of the 79-pass series. It is the strongest v2-AI task-orchestrator primitive that the LE31 project has observed, and the adoption is **fully reversible** (vocabulary-only artifact; no code dependency). When a v2-AI window opens, the haiplane vocabulary becomes the actionable task-orchestrator reference for any LE31 v2-AI workflow that needs to coordinate multiple AI agents on multi-step restaurant operations tasks.

Charter §3.4 alignment is strong: haiplane exposes an MCP-server (chokepoint-governed) + requires acceptance-criteria (human-gate) + requires commit-reference (observable-evidence) + has a non-AI-fallback (the operator can complete tasks manually without an AI agent).

Sister-shape cross-section: features 316/322 (the-vibey-project/vibey, which uses append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review quad-primitive), 187/188 (traust-security/traust-ledger), 232 (lpalbou/AbstractGateway), 287/288/289 (noise01/endoxa + pete-builds/mcp-nixreview + shivamk01here/LedgerLoop), 327 (musterhq/muster), 332/333/334 (vsov/xcheck + FlashyLabs/flashy-ledger + donaldrichard19-LVD/pattern-mcp).

## Trigger condition

Re-evaluate when:
1. A v2-AI workflow window opens in the LE31 charter roadmap.
2. A future v2-AI PR proposes a multi-agent task-orchestrator surface.
3. A future v2-AI PR proposes an MCP-server adapter for the LE31 API.
4. A future v2-AI PR proposes an acceptance-criteria gate for AI-agent-action.
5. A future v2-AI PR proposes a commit-named-as-completion-evidence discipline.

At that point, the haiplane vocabulary becomes actionable for the LE31 v2-AI surface.