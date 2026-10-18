# Slice Handoff — Feature 338 (agentdrover/haiplane)

> **Feature ID**: 338
> **Feature path**: `/opt/data/le31_mmm3_research_work/features/338-agentdrover-haiplane-mit-task-orchestrator-ai-agents-acceptance-criteria-named-commit-fastapi-htmx-mcp-python-v2-ai-task-orchestrator-with-acceptance-criteria-and-named-commit-fastapi-htmx-mcp-vocabulary.md`
> **Decision**: defer (parking-lot, vocabulary reference)
> **Bucket**: v2-AI

## LE31 feature gate verdict (carried from feature contract)

- **Evidence precondition**: inferred (vocabulary observation, not observed LE31 user pain). Confidence: medium.
- **Seven checks**:
  1. **JTBD**: When a v2-AI agent assists the owner/staff with a multi-step workflow, the operator wants every agent action bounded by acceptance criteria + verifiable by the named commit that shipped it.
  2. **Viability**: medium — non-technical owner/staff would need help to interpret git-native-governance / task-orchestrator artifacts.
  3. **Practicability and confidence**: medium — Python+FastAPI+HTMX+MCP on-stack; rabbit hole = charter §3.4 review before any v1 PR.
  4. **Conflict**: no hard conflict with any charter invariant.
  5. **Outcome / appetite / scope**: v2-AI outcome; 0 build time today; max 4 weeks per pick if a v2-AI window opens.
  6. **Cost to operational value**: low RICE; not a v1 PR candidate.
  7. **Circuit breaker / reversibility**: fully reversible (vocabulary-only artifact; no code adoption).
- **Decision**: **defer (parking-lot, vocabulary reference)**.

## Files this slice will touch (when implemented)

> Not implemented today. When a v2-AI window opens, the implementation will touch:

- `app/v2/ai/tasks/__init__.py` — new package
- `app/v2/ai/tasks/models.py` — `Task` + `AcceptanceCriterion` + `TaskCompletionAudit` SQLModel tables (append-only `TaskCompletionAudit` per charter §3.3)
- `app/v2/ai/tasks/router.py` — FastAPI router under `/v2/ai/tasks` with CRUD endpoints + MCP-server adapter
- `app/v2/ai/tasks/templates/` — HTMX templates for the operator-facing task-board UI
- `app/v2/ai/tasks/hooks/` — `commit_named_as_completion_evidence` validator
- `app/v2/ai/tasks/tests/` — verify the orchestrator rejects tasks without acceptance criteria + rejects task-completion without a commit reference
- `migrations/` — alembic migration for the new tables

> **Greenfield**: no existing v1 files are touched by this slice (LE31 v1 has no AI-agent surface).

## Verification protocol (when implemented)

1. Run `pytest app/v2/ai/tasks/tests/` and verify all tests pass.
2. Manually create a task via the FastAPI router with no acceptance criteria; verify the router returns HTTP 400 with a descriptive error.
3. Manually create a task with acceptance criteria + mark it done without a `commit_sha`; verify the router returns HTTP 400 with a descriptive error.
4. Manually create a task with acceptance criteria + mark it done with a valid `commit_sha`; verify the task transitions to `done` + the `TaskCompletionAudit` row is created (append-only).
5. Verify the HTMX task-board UI renders the task list + the MCP-server endpoint returns the task list.
6. Verify the integration with the v2-AI surface (if the v2-AI surface is already implemented).

## Rollback path

- `git revert <commit-hash>` to remove the v2-AI task-orchestrator surface.
- `alembic downgrade -1` to drop the new tables.
- No v1 data is affected (greenfield; no migration of existing v1 data).
- All `TaskCompletionAudit` rows are append-only per charter §3.3; they remain in the audit trail even after the rollback (the rollback only removes the application code, not the audit data).

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
- **DO NOT start** until a future v2-AI PR proposes a multi-agent task-orchestrator surface, an MCP-server adapter for the LE31 API, an acceptance-criteria gate for AI-agent-action, or a commit-named-as-completion-evidence discipline.
- **DO NOT start** until the charter §3.4 AI-sandbox-as-auditable-test review has been completed.
- When triggered, mirror back the frozen contract fields (feature ID, decision, bucket, files to touch, verification protocol) before implementing; stop if the mirror-back does not match.

## External-context Linear reference

- Parent research issue: Research 2026-10-18 — daily (Linear MCP BLOCKED 29th consecutive day; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-18.linear-fallback.json` documents the intended parent + 3 sub-issues).
- This feature: Feature 338 — agentdrover/haiplane (intended sub-issue in `le31 Research` P-HMM-1).

## Sign-off gap

- External agent has NOT yet been dispatched.
- Charter §3.4 review has NOT yet been completed.
- v2-AI workflow window has NOT yet opened.
- No v1 PR today.

## Cross-references

- Feature contract: `/opt/data/le31_mmm3_research_work/features/338-...md`
- Source artifact: `/opt/data/le31-daily-research-2026-10-18.md` (pick A)
- Sister-shapes: features 316/322 (the-vibey-project/vibey), 187/188 (traust-security/traust-ledger), 232 (lpalbou/AbstractGateway), 287/288/289 (noise01/endoxa + pete-builds/mcp-nixreview + shivamk01here/LedgerLoop), 327 (musterhq/muster), 332/333/334 (vsov/xcheck + FlashyLabs/flashy-ledger + donaldrichard19-LVD/pattern-mcp).