# HANDOFF — Feature 305: `footprintjs-hcifootprint-mit-typed-traversable-skill-graph-llm-can-plan-over-hci-frontend-sibling-mcp-server-agentic-apps-v1-hci-typed-skill-graph-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/305-footprintjs-hcifootprint-mit-typed-traversable-skill-graph-llm-can-plan-over-hci-frontend-sibling-mcp-server-agentic-apps-v1-hci-typed-skill-graph-vocabulary.md` — defer/parking-lot (Pick A of Daily Brainstorm 2026-10-11).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes a *typed-traversable-skill-graph-an-LLM-can-plan-over + frontend-sibling-of + MCP-server + agentic-apps + skill-graph + hci primitive*, the owner wants *evidence that this HCI-typed-skill-graph-vocabulary exists in 2026 with the same HCI-research-grounded + LLM-can-plan-over posture*, but struggles because *LE31 has no documented v1 HCI-typed-skill-graph-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same typed-traversable-skill-graph + frontend-sibling-of + MCP-server + agentic-apps + skill-graph + hci posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (typed-traversable-skill-graph + frontend-sibling-of + MCP-server + agentic-apps + skill-graph + hci) without specialist help. The 10★/1⑨ (highest-star brainstorm pick of the 74-pass series) with maintainer activity (pushed 2026-10-10 = in-window by push only) makes vocabulary viable, but code adoption is not viable (TypeScript off-§3.1 stack for LE31 v1 today). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: TypeScript off-§3.1 stack for LE31 v1 today but the *typed-traversable-skill-graph + frontend-sibling-of + MCP-server-as-cross-system-tooling + agentic-apps + skill-graph + hci* vocabulary IS stack-agnostic and IS portable to Python. Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX. No AI capability required (the typed-skill-graph primitive is deterministic). Rabbit hole: the *TypeScript + Node.js + MCP-server + agentic-apps* stack is off-LE31-stack (LE31 v1 uses minimal-HTML/HTMX + Python + FastAPI, not TypeScript + Node.js + MCP-server + agentic-apps). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *typed-traversable-skill-graph + frontend-sibling-of + MCP-server + agentic-apps + skill-graph + hci* primitives are §3.1 + §3.4-aligned (operator-can-keep-working-during-network-outage + observable-evidence + MCP-as-cross-system-tooling). The *typed-traversable-skill-graph + frontend-sibling-of* posture IS the §3.1 *web-UI-as-frontend-sibling-of-LLM-context* charter §3.4 invariant applied to the *web-UI-telemetry* dimension. No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (typed-skill-graph surface for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + HTMX waiter-web-UI) already implement the *append-only + minimal-HTML/HTMX* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (TypeScript + Node.js off-LE31-stack + no v1 typed-skill-graph surface in v1 charter).

## Bucket

**v1** (HCI-typed-skill-graph-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the octuple-primitive set (typed-traversable-skill-graph + frontend-sibling-of + MCP-server + agentic-apps + skill-graph + hci) + the tech-stack (TypeScript + Node.js + MCP-server + agentic-apps).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *typed-traversable-skill-graph + frontend-sibling-of + MCP-server + agentic-apps + skill-graph + hci* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `SkillGraphNode`, `SkillGraphEdge`, `WebUIInteractionSurface` tables.
- `backend/skill_graph.py` — new file with `SkillGraphBuilder` class.
- `backend/main.py` — add `/api/web-ui-skill-graph` FastAPI endpoint.
- `frontend/templates/web-ui-skill-graph.html` — new minimal-HTML/HTMX template.
- `backend/mcp_server_skill_graph.py` — new file with `McpServerForSkillGraph` FastMCP sub-app.
- `backend/web_ui_interaction_logger.py` — new file with `WebUIInteractionSurfaceLogger`.
- `tests/test_skill_graph.py` — new unit test for `SkillGraphBuilder`.
- `tests/integration/test_mcp_skill_graph.py` — new integration test for `McpServerForSkillGraph`.

## Verification protocol reference

When the first v1 PR that adopts the *typed-traversable-skill-graph + frontend-sibling-of + MCP-server + agentic-apps + skill-graph + hci* discipline lands, the verification protocol is:

1. Run `pytest tests/test_skill_graph.py` and verify the `SkillGraphBuilder` produces a valid typed-skill-graph for a known `index.html`.
2. Run `pytest tests/integration/test_mcp_skill_graph.py` and verify the MCP-server exposes the skill graph correctly.
3. Run `uvicorn backend.main:app` and curl `/api/web-ui-skill-graph` to verify the endpoint returns the skill graph as JSON.
4. Open `frontend/templates/web-ui-skill-graph.html` in a browser and verify the skill graph renders as a navigable tree.
5. Inspect the `WebUIInteractionSurface` table in Postgres and verify every interaction is recorded.

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *typed-traversable-skill-graph + frontend-sibling-of + MCP-server + agentic-apps + skill-graph + hci* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the three tables.
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

First v1 PR that adds a `typed_skill_graph` SQLModel table + a `WebUIInteractionSurface` event table + a `/api/web-ui-skill-graph` FastAPI endpoint + a `web-ui-skill-graph.html` minimal-HTML/HTMX template with typed-traversable-skill-graph + frontend-sibling-of + MCP-server-as-cross-system-tooling metrics; OR first v1 PR that adopts the *typed-traversable-skill-graph-an-LLM-can-plan-over + frontend-sibling-of* discipline on the existing waiter-web-UI telemetry surface.

## Adjacent evidence

- [../features/256-jblattgerste-sus-analysis-toolkit-...-v1-hci-usability-evaluation-vocabulary-reference.md](../features/256-jblattgerste-sus-analysis-toolkit-...-v1-hci-usability-evaluation-vocabulary-reference.md) — sister-shape for HCI-research-grounded-telemetry.
- [../features/268-escarletdesign-ux-laws-auditor-...-v1-hci-usability-audit-vocabulary.md](../features/268-escarletdesign-ux-laws-auditor-...-v1-hci-usability-audit-vocabulary.md) — sister-shape for HCI-research-grounded-audit.
- [../features/285-uniovi-hci-pywib-...-v1-hci-usability-evaluation-vocabulary.md](../features/285-uniovi-hci-pywib-...-v1-hci-usability-evaluation-vocabulary.md) — sister-shape for HCI-research-grounded-web-page-telemetry.

## Notes

- The 10★/1⑨ (highest-star brainstorm pick of the 74-pass series) makes this a high-confidence vocabulary candidate.
- The TypeScript + Node.js stack is off-§3.1 for LE31 v1 today but the vocabulary is stack-agnostic and portable to Python.
- The MCP-server-as-cross-system-tooling posture is consistent with the v2-AI MCP-as-cross-system-tooling posture (Pick B + Pick C + features 232 + 287-289 + 299-302).
- The agentic-apps posture is borderline §3.4 if extended to customer-facing flows; the typed-traversable-skill-graph surface is operator-tooling + observable-evidence per charter §3.4 invariant.