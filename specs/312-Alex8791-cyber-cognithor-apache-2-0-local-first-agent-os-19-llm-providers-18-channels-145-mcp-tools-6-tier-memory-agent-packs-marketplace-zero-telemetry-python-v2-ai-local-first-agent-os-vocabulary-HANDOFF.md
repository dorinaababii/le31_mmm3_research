# HANDOFF — Feature 312: `Alex8791-cyber-cognithor-apache-2-0-local-first-agent-os-19-llm-providers-18-channels-145-mcp-tools-6-tier-memory-agent-packs-marketplace-zero-telemetry-python-v2-ai-local-first-agent-os-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/312-Alex8791-cyber-cognithor-apache-2-0-local-first-agent-os-19-llm-providers-18-channels-145-mcp-tools-6-tier-memory-agent-packs-marketplace-zero-telemetry-python-v2-ai-local-first-agent-os-vocabulary.md` — defer/parking-lot (Pick B of Daily Brainstorm 2026-10-12).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *local-first-agent-OS + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace + zero-telemetry + gdpr-compliant primitive*, the owner wants *evidence that this local-first-agent-OS-vocabulary exists in 2026 with the same local-first + zero-telemetry + gdpr-compliant + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace posture*, but struggles because *LE31 has no documented v2-AI local-first-agent-OS-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same local-first + zero-telemetry + gdpr-compliant + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (local-first + zero-telemetry + gdpr-compliant + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace) without specialist help. The 158★/25⑨ (strongest v2-AI local-first-agent-OS-vocabulary topic array of the 75-pass series) with maintainer activity (pushed 2026-10-05 = in-window) makes vocabulary viable, but code adoption is not viable (the 20-topic array is off-§3.1 charter for LE31 v1 today; v2-AI is undefined). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + 19-LLM-providers OFF-STACK + 18-channels (Telegram-bot ✓ + Discord-bot OFF) + 145-MCP-tools OFF-STACK + 6-tier-memory OFF-STACK + Agent-Packs-marketplace OFF-STACK + zero-telemetry ✓ §3.7 + gdpr-compliant ✓ §3.7. Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX. No AI capability required (the local-first-agent-OS primitive is operator-driven; the *19-LLM-providers + 145-MCP-tools + 6-tier-memory* posture is the §3.4 *MCP-as-cross-system-tooling + multi-LLM-pluggable* invariant). Rabbit hole: the *19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace* stack is off-LE31-v1-stack (LE31 v1 uses aiogram v3 + Postgres, not 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *local-first + zero-telemetry + gdpr-compliant + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace* primitives are §3.1 + §3.2 + §3.3 + §3.4 + §3.7-aligned (self-hosted + on-premise-deployment + append-only-knowledge-ledger + MCP-as-cross-system-tooling + privacy-first). The *local-first + zero-telemetry + gdpr-compliant* posture IS the §3.1 *self-hosted + on-premise-deployment* + §3.7 *privacy-first* + §3.4 *non-AI-fallback* charter invariant. No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI polish outcome (local-first-agent-OS surface for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + HTMX waiter-web-UI) already implement the *append-only + minimal-HTML/HTMX* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace off-LE31-stack + no v2-AI local-first-agent-OS surface in v2-AI charter; v2-AI is undefined).

## Bucket

**v2-AI** (local-first-agent-OS-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 20-tuple-primitive set (local-first + zero-telemetry + gdpr-compliant + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace + knowledge-graph + knowledge-vault + knowledge-synthesis + hierarchical-retrieval + document-analysis) + the tech-stack (Python + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *local-first + zero-telemetry + gdpr-compliant + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `LocalFirstAgentOS`, `LocalFirstAgent`, `AgentPack`, `LocalFirstAgentEvent`, `KnowledgeNode` tables.
- `backend/local_first_agent_os.py` — new file with `LocalFirstAgentOSRuntime` class.
- `backend/main.py` — add `/api/local-first-agent-os` FastAPI endpoint set.
- `backend/services/agent_pack_marketplace.py` — new file with `AgentPackMarketplace` class.
- `backend/services/six_tier_memory.py` — new file with `SixTierMemory` class.
- `backend/services/knowledge_layer.py` — new file with `KnowledgeLayer` class.
- `backend/bot/cook_bot.py` — wire the `cook-bot-agent` to the `local_first_agent_os` surface.
- `backend/mcp_server_local_first_agent_os.py` — new file with `McpServerForLocalFirstAgentOS` FastMCP sub-app.
- `frontend/templates/local-first-agent-os.html` — new minimal-HTML/HTMX template.
- `tests/test_local_first_agent_os.py` — new unit test for `LocalFirstAgentOSRuntime`.
- `tests/integration/test_mcp_local_first_agent_os.py` — new integration test for `McpServerForLocalFirstAgentOS`.

## Verification protocol reference

When the first v2-AI PR that adopts the *local-first + zero-telemetry + gdpr-compliant + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace* discipline lands, the verification protocol is:

1. Run `pytest tests/test_local_first_agent_os.py` and verify the `LocalFirstAgentOSRuntime` produces a valid local-first-agent-OS for the existing waiter-web-UI + cook-Telegram-bot + owner-daily-recap surfaces.
2. Run `pytest tests/integration/test_mcp_local_first_agent_os.py` and verify the MCP-server exposes the OS + agent + agent-pack + knowledge-layer surface correctly.
3. Run `uvicorn backend.main:app` and curl `/api/local-first-agent-os` to verify the endpoint returns the OS as JSON.
4. Open `frontend/templates/local-first-agent-os.html` in a browser and verify the local-first-agent-OS renders as a navigable tree.
5. Inspect the `LocalFirstAgentEvent` + `KnowledgeNode` tables in Postgres and verify every event + every knowledge-node is recorded (the §3.3 append-only-ledger invariant).
6. Run the zero-telemetry test (no network egress) + the gdpr-compliant test (no PII collection beyond what LE31 charter §3.7 allows).

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *local-first + zero-telemetry + gdpr-compliant + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the five tables.
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

This defer artifact is documentation only. It becomes a build trigger when the **first v2-AI PR that adds a local-first-agent-OS surface to the LE31 single-restaurant Swiss kitchen** lands. At that point:

1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which 18 channels (Telegram-bot + Discord-bot + ?), which 19 LLM providers (Anthropic + OpenAI + Gemini + Ollama + ?), which 145 MCP tools (the §3.4 *MCP-as-cross-system-tooling* surface is open-ended), which 6 memory tiers (working + episodic + semantic + procedural + ?), and which Agent-Packs are pre-built for the LE31 single-restaurant.
3. Adopt the *local-first + zero-telemetry + gdpr-compliant + 19-LLM-providers + 18-channels + 145-MCP-tools + 6-tier-memory + Agent-Packs-marketplace* discipline on the existing `audit_logs` SQLModel table.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v2-AI code is shipped.
