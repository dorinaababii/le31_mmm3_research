# HANDOFF — Feature 313: `jklthinking-retinue-mit-self-hosted-ai-worker-coordination-per-task-graphs-device-model-timelines-progress-receipts-source-aware-usage-fastapi-react-sqlite-mcp-multi-agent-systems-telegram-bot-v2-ai-self-hosted-ai-worker-coordination-vocab`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

> **Note on filename**: the HANDOFF filename uses the `vocab` abbreviation (instead of `vocabulary`) to stay under the 256-char filesystem limit; the active feature path uses the full `vocabulary` form per the v1 feature contract shape (see `features/313-...-vocabulary.md`).

## Active feature path

`features/313-jklthinking-retinue-mit-self-hosted-ai-worker-coordination-per-task-graphs-device-model-timelines-progress-receipts-source-aware-usage-fastapi-react-sqlite-mcp-multi-agent-systems-telegram-bot-v2-ai-self-hosted-ai-worker-coordination-vocabulary.md` — defer/parking-lot (Pick C of Daily Brainstorm 2026-10-12).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *self-hosted-AI-worker-coordination + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex primitive*, the owner wants *evidence that this self-hosted-AI-worker-coordination-vocabulary exists in 2026 with the same self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex posture*, but struggles because *LE31 has no documented v2-AI self-hosted-ai-worker-coordination-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex) without specialist help. The 117★/3⑨ (strongest v2-AI self-hosted-ai-worker-coordination-vocabulary topic array of the 75-pass series) with maintainer activity (pushed 2026-10-08 = in-window) makes vocabulary viable, but code adoption is not viable (the 20-topic array is off-§3.1 charter for LE31 v1 today; v2-AI is undefined). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + FastAPI ✓ ON-STACK + React ✓ ON-PATTERN + SQLite ✓ ON-STACK (NB: LE31 v1 uses Postgres in prod but SQLite in dev per charter §3.1) + MCP OFF-STACK + multi-agent-systems OFF-STACK + claude + codex OFF-STACK + feishu OFF-STACK + kanban + task-board + self-hosted ✓ §3.1 + telegram-bot ✓ ON-STACK. Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX. No AI capability required (the self-hosted-AI-worker-coordination primitive is operator-driven; the *multi-agent-systems + claude + codex* posture is the §3.4 *AI-coding-agent-as-deployment-blueprint* invariant). Rabbit hole: the *FastAPI + React + SQLite + MCP + multi-agent-systems + claude + codex + feishu + kanban + task-board* stack is partially off-LE31-v1-stack (LE31 v1 uses aiogram v3 + Postgres, not FastAPI + React + SQLite + MCP + multi-agent-systems + claude + codex + feishu + kanban + task-board; the FastAPI + SQLite + self-hosted sub-stack IS on-§3.1). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex* primitives are §3.1 + §3.2 + §3.3 + §3.4-aligned (self-hosted + on-premise-deployment + append-only-task-ledger + progress-receipts-as-audit-trail + MCP-as-cross-system-tooling + AI-coding-agent-as-deployment-blueprint + non-AI-fallback). The *self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage* posture IS the §3.1 *self-hosted + on-premise-deployment* + §3.3 *append-only-task-ledger + progress-receipts-as-audit-trail* + §3.4 *non-AI-fallback* charter invariant. No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI polish outcome (self-hosted-AI-worker-coordination surface for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + HTMX waiter-web-UI) already implement the *append-only + minimal-HTML/HTMX* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (FastAPI + React + SQLite + MCP + multi-agent-systems + claude + codex + feishu + kanban + task-board off-LE31-stack + no v2-AI self-hosted-AI-worker-coordination surface in v2-AI charter; v2-AI is undefined).

## Bucket

**v2-AI** (self-hosted-ai-worker-coordination-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 20-tuple-primitive set (self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex + feishu + fastapi + react + sqlite + telegram-bot + mcp + model-context-protocol + agent-orchestration + agents + ai-agents + automation + llm + python + task-management) + the tech-stack (Python + FastAPI + React + SQLite + MCP + model-context-protocol + multi-agent-systems + Claude + Codex + Feishu + Kanban + Task-board + Self-hosted + Telegram-bot).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `SelfHostedAIWorkerCoordination`, `AIWorker`, `PerTaskGraph`, `ProgressReceipt` tables.
- `backend/self_hosted_ai_worker_coordination.py` — new file with `SelfHostedAIWorkerCoordinationRuntime` class.
- `backend/main.py` — add `/api/self-hosted-ai-worker-coordination` FastAPI endpoint set.
- `backend/services/per_task_graphs.py` — new file with `PerTaskGraphEngine` class.
- `backend/services/device_model_timelines.py` — new file with `DeviceModelTimelineTracker` class.
- `backend/services/source_aware_usage.py` — new file with `SourceAwareUsageTracker` class.
- `backend/bot/cook_bot.py` — wire the `cook-bot-agent` to the `self_hosted_ai_worker_coordination` surface.
- `backend/mcp_server_self_hosted_ai_worker_coordination.py` — new file with `McpServerForSelfHostedAIWorkerCoordination` FastMCP sub-app.
- `frontend/templates/self-hosted-ai-worker-coordination.html` — new minimal-HTML/HTMX template with the kanban + task-board + task-management UI.
- `tests/test_self_hosted_ai_worker_coordination.py` — new unit test for `SelfHostedAIWorkerCoordinationRuntime`.
- `tests/integration/test_mcp_self_hosted_ai_worker_coordination.py` — new integration test for `McpServerForSelfHostedAIWorkerCoordination`.

## Verification protocol reference

When the first v2-AI PR that adopts the *self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex* discipline lands, the verification protocol is:

1. Run `pytest tests/test_self_hosted_ai_worker_coordination.py` and verify the `SelfHostedAIWorkerCoordinationRuntime` produces a valid self-hosted-AI-worker-coordination for the existing waiter-web-UI + cook-Telegram-bot + owner-daily-recap surfaces.
2. Run `pytest tests/integration/test_mcp_self_hosted_ai_worker_coordination.py` and verify the MCP-server exposes the coord + worker + task-graph + progress-receipt surface correctly.
3. Run `uvicorn backend.main:app` and curl `/api/self-hosted-ai-worker-coordination` to verify the endpoint returns the coord as JSON.
4. Open `frontend/templates/self-hosted-ai-worker-coordination.html` in a browser and verify the self-hosted-AI-worker-coordination renders as a navigable kanban board.
5. Inspect the `ProgressReceipt` table in Postgres and verify every task-step writes a progress-receipt (the §3.3 append-only-ledger invariant).
6. Run the source-aware-usage test (every step tracks which file/URL/MCP-tool it consumed) + the device/model-timeline test (every step tracks which device + which model it used).

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the four tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:

- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-v1-feature-pattern/SKILL.md` — for the v1 feature contract shape and slicing rules (NB: this is v2-AI bucket, but the v1 contract shape still applies for now; v2-AI uses the same slicing rules).
- `skills/le31-research/SKILL.md` — for the research workflow and report shape.
- `skills/le31-feature-pipeline/SKILL.md` — for the feature pipeline (lease to coding agent).
- `skills/le31-handoff-spec/SKILL.md` — for the handoff spec (this file).
- `skills/le31-coding-agent-brief/SKILL.md` — for the paste-in brief.
- `skills/le31-backend/SKILL.md` — for the backend conventions (if applicable).
- `skills/le31-frontend/SKILL.md` — for the frontend conventions (if applicable).
- `skills/le31-data/SKILL.md` — for the data conventions (if applicable).
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

This defer artifact is documentation only. It becomes a build trigger when the **first v2-AI PR that adds a self-hosted-AI-worker-coordination surface to the LE31 single-restaurant Swiss kitchen** lands. At that point:

1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which AI workers (waiter-UI-agent? cook-bot-agent? owner-recap-agent? claude? codex? feishu-bot?), which per-task-graphs (seating? ordering? prep? reconciliation?), which sources (existing `audit_logs` table? existing `cook_bot.py` handlers? existing FastAPI routers?), and which columns on the kanban board (backlog? in-progress? review? done?).
3. Adopt the *self-hosted + per-task-graphs + device/model-timelines + progress-receipts + source-aware-usage + kanban + task-board + multi-agent-systems + claude + codex* discipline on the existing `audit_logs` SQLModel table.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v2-AI code is shipped.
