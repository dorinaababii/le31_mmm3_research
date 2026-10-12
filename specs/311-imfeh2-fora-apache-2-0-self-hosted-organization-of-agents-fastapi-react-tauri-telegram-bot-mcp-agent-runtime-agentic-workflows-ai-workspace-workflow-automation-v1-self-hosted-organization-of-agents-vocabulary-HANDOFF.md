# HANDOFF — Feature 311: `imfeh2-fora-apache-2-0-self-hosted-organization-of-agents-fastapi-react-tauri-telegram-bot-mcp-agent-runtime-agentic-workflows-ai-workspace-workflow-automation-v1-self-hosted-organization-of-agents-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/311-imfeh2-fora-apache-2-0-self-hosted-organization-of-agents-fastapi-react-tauri-telegram-bot-mcp-agent-runtime-agentic-workflows-ai-workspace-workflow-automation-v1-self-hosted-organization-of-agents-vocabulary.md` — defer/parking-lot (Pick A of Daily Brainstorm 2026-10-12).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes a *run-your-own-organization-of-agents + ai-workspace + agent-runtime + agentic-workflows + workflow-automation primitive*, the owner wants *evidence that this self-hosted-organization-of-agents-vocabulary exists in 2026 with the same self-hosted-organization + ai-workspace + workflow-automation posture*, but struggles because *LE31 has no documented v1 self-hosted-organization-of-agents-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same run-your-own-organization-of-agents + ai-workspace + agent-runtime + agentic-workflows + workflow-automation posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (run-your-own-organization-of-agents + ai-workspace + agent-runtime + agentic-workflows + workflow-automation) without specialist help. The 256★/12⑨ (broadest v1 self-hosted-organization-of-agents-vocabulary topic array of the 75-pass series) with maintainer activity (pushed 2026-10-11 = YESTERDAY) makes vocabulary viable, but code adoption is not viable (the 17-topic array is off-§3.1 charter for LE31 v1 today). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + FastAPI ✓ ON-STACK + React ✓ ON-PATTERN + Rust OFF-STACK + Tauri OFF-STACK + Telegram-bot ✓ ON-STACK + MCP OFF-STACK + LLM OFF-STACK. Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX. No AI capability required (the run-your-own-organization-of-agents primitive is operator-driven; the *agent-runtime + agentic-workflows + workflow-automation* posture is deterministic). Rabbit hole: the *FastAPI + React + Rust + Tauri + MCP + LLM* stack is off-LE31-v1-stack (LE31 v1 uses minimal-HTML/HTMX + Python + FastAPI, not FastAPI + React + Rust + Tauri + MCP + LLM). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *run-your-own-organization-of-agents + ai-workspace + agent-runtime + agentic-workflows + workflow-automation* primitives are §3.1 + §3.4-aligned (operator-orchestrates-the-agents + workflow-automation + MCP-as-cross-system-tooling). The *run-your-own-organization-of-agents + ai-workspace + workflow-automation* posture IS the §3.1 *self-hosted-organization* + §3.4 *MCP-as-cross-system-tooling* charter invariant. No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (self-hosted-organization-of-agents surface for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + HTMX waiter-web-UI) already implement the *append-only + minimal-HTML/HTMX* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (FastAPI + React + Rust + Tauri + MCP + LLM off-LE31-stack + no v1 self-hosted-organization-of-agents surface in v1 charter).

## Bucket

**v1** (self-hosted-organization-of-agents-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 17-tuple-primitive set (run-your-own-organization-of-agents + ai-workspace + agent-runtime + agentic-workflows + workflow-automation + fastapi + react + rust + tauri + telegram-bot + mcp + llm) + the tech-stack (Python + FastAPI + React + Rust + Tauri + Telegram-bot + MCP + LLM).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *run-your-own-organization-of-agents + ai-workspace + agent-runtime + agentic-workflows + workflow-automation* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `SelfHostedAgentOrg`, `SelfHostedAgent`, `WorkflowAutomation`, `SelfHostedAgentEvent` tables.
- `backend/self_hosted_agent_org.py` — new file with `SelfHostedAgentOrg` class.
- `backend/main.py` — add `/api/self-hosted-agent-org` FastAPI endpoint set.
- `backend/services/workflow_automation.py` — new file with `WorkflowAutomationEngine` class.
- `backend/bot/cook_bot.py` — wire the `cook-bot-agent` to the `self_hosted_agent_org` surface.
- `backend/mcp_server_self_hosted_agent_org.py` — new file with `McpServerForSelfHostedAgentOrg` FastMCP sub-app.
- `frontend/templates/self-hosted-agent-org.html` — new minimal-HTML/HTMX template.
- `tests/test_self_hosted_agent_org.py` — new unit test for `SelfHostedAgentOrg`.
- `tests/integration/test_mcp_self_hosted_agent_org.py` — new integration test for `McpServerForSelfHostedAgentOrg`.

## Verification protocol reference

When the first v1 PR that adopts the *run-your-own-organization-of-agents + ai-workspace + agent-runtime + agentic-workflows + workflow-automation* discipline lands, the verification protocol is:

1. Run `pytest tests/test_self_hosted_agent_org.py` and verify the `SelfHostedAgentOrg` produces a valid self-hosted-organization for the existing waiter-web-UI + cook-Telegram-bot + owner-daily-recap surfaces.
2. Run `pytest tests/integration/test_mcp_self_hosted_agent_org.py` and verify the MCP-server exposes the org + agent + workflow surface correctly.
3. Run `uvicorn backend.main:app` and curl `/api/self-hosted-agent-org` to verify the endpoint returns the org as JSON.
4. Open `frontend/templates/self-hosted-agent-org.html` in a browser and verify the self-hosted-organization renders as a navigable tree.
5. Inspect the `SelfHostedAgentEvent` table in Postgres and verify every agent-action is recorded (the §3.3 append-only-ledger invariant).

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *run-your-own-organization-of-agents + ai-workspace + agent-runtime + agentic-workflows + workflow-automation* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the four tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:

- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-v1-feature-pattern/SKILL.md` — for the v1 feature contract shape and slicing rules.
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

This defer artifact is documentation only. It becomes a build trigger when the **first v1 PR that adds a self-hosted-organization-of-agents surface to the LE31 single-restaurant Swiss kitchen** lands. At that point:

1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which existing LE31 surface (waiter-web-UI? cook-Telegram-bot? owner-daily-recap?) becomes the first `self_hosted_agent` in the org.
3. Decide which existing LE31 workflow (seating? ordering? prep? reconciliation?) becomes the first `workflow_automation`.
4. Adopt the *run-your-own-organization-of-agents + ai-workspace + workflow-automation* discipline on the existing waiter-web-UI + cook-Telegram-bot + owner-daily-recap surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v1 code is shipped.
