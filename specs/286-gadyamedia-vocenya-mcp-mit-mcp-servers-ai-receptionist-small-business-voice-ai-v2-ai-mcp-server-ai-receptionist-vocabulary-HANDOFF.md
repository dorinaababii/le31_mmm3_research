# Handoff — Feature 286 — v2-AI MCP-server-for-AI-receptionist-vocabulary (defer)

> **Pick:** `gadyamedia/vocenya-mcp` — v2-AI cross-section reference for **official-MCP-servers-for-Vocenya-the-AI-receptionist-for-small-businesses + registry-entries + Claude-Code-plugin + setup + ai-agents + ai-receptionist + chatgpt + claude + claude-code + claude-code-plugin + cursor + mcp + mcp-server + model-context-protocol + remote-mcp + small-business + streamable-http + vocenya + voice-ai + vscode** primitive.
> **Status:** `defer (parking-lot, vocabulary reference)` — zero build time today; the artifact is vocabulary-only and persists as a future-cast reference for any future LE31 v2-AI surface that adopts the *MCP-server + remote-mcp + streamable-http + ai-receptionist + ai-agents + claude + chatgpt + voice-ai* primitives.
> **Source:** Daily Brainstorm 2026-10-06 (68th consecutive daily-brainstorm pass) → Pick C.
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/286-gadyamedia-vocenya-mcp-mit-mcp-servers-ai-receptionist-small-business-voice-ai-v2-ai-mcp-server-ai-receptionist-vocabulary.md`
> **Raw fetches:** `/tmp/le31-brainstorm-2026-10-06/verify_gadyamedia_vocenya-mcp.json` (parent-verified direct GitHub API GET, raw JSON)

---

## Seven-check gate verdict (LE31 charter §3.1 + §3.2 + §3.4)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✓ justified as a NEW pain | When the LE31 owner wants an external AI-coding-agent (Claude-Code, Codex, OpenCode) to query LE31's `audit_logs` + `StockEntry` + `Visit` + `OrderItem` directly via MCP, the owner wants a *MCP-server + remote-mcp + streamable-http* surface, but struggles because the existing `audit_logs` + `StockEntry` + `Visit` + `OrderItem` table set has *no MCP-server + no remote-mcp + no streamable-http* surface, so the v2-AI surface-extension needs a *MCP-server + remote-mcp + streamable-http + ai-receptionist + ai-agents + claude + chatgpt + voice-ai* discipline. **v2-AI expansion → NEW pain** |
| 2 | Viability | ✓ viable | Non-technical owner CAN understand (the *MCP-server + remote-mcp + streamable-http + ai-receptionist* primitive is operator-readable); CAN recover (the *MCP-server + remote-mcp + streamable-http + audit_logs* discipline is recoverable via Postgres backup); CAN maintain (the *MCP-server + remote-mcp + streamable-http + ai-receptionist* surface is documentation-only at v2-AI; v2-AI surface would require FastAPI + SQLModel + Postgres + FastMCP + MCP-runtime-infrastructure + remote-mcp + streamable-http expertise). **§3.1 owner-readable profile** |
| 3 | Strategic fit | ✓ aligned | Cross-section with feature 234 (narumiruna/gurume MIT Python-CLI-TUI-MCP-server-Japanese-restaurant-tabelog-search-agent-skills-fastmcp-v2-ai-mcp-cli-tui-operator-tooling-vocabulary = *Python-CLI-TUI-MCP-server + Japanese-restaurant-tabelog-search + agent-skills + fastmcp* sextuple-primitive) + 254 (OthmaneBlial/lightclaw MIT supervise-local-Codex-and-Claude-agents-from-Telegram-review-plans-approve-scoped-work-inspect-diffs-and-tests-v2-ai-telegram-bot-agent-supervision-audit-trail-vocabulary = *Telegram-bot-supervises-local-Codex-and-Claude-agents + review-plans + approve-scoped-work + inspect-diffs-and-tests* sextuple-primitive) + today's daily-research Pick B 282 (AllStreets/ONEXUS Apache-2.0 local-first-ai-agent-runtime-capability-arbiter-declared-manifest-earned-trust-immutable-audit-ledger-python-mcp-v2-ai-capability-arbiter-runtime-vocabulary). The *official-MCP-servers-for-AI-receptionist + registry-entries + Claude-Code-plugin + setup + ai-agents + ai-receptionist + chatgpt + claude + claude-code + claude-code-plugin + cursor + mcp + mcp-server + model-context-protocol + remote-mcp + small-business + streamable-http + vocenya + voice-ai + vscode* posture IS the canonical **v2-AI MCP-server-for-AI-receptionist-vocabulary** |
| 4 | Charter conflict | ✓ none hard | §3.1 STRICTLY-COMPATIBLE (Python + minimal-HTML posture; the *MCP-server + remote-mcp + streamable-http + ai-receptionist + small-business* posture IS the §3.1 *single-restaurant + single-owner + on-premise-deployment + cross-system-tooling* invariant applied to the *MCP-server* dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive + 0★/0⑨ community traction start + 32 KB tiny = the *official-MCP-servers + registry-entries + setup* posture IS the §3.2 *minimal-HTML/HTMX + zero-build* invariant applied to the *MCP-registry-entries* dimension); §3.4 RIPGL_REVIEW REQUIRED (the *ai-receptionist* surface is borderline customer-facing if the receptionist answers diner calls; the *claude-code-plugin + setup-as-deployment-blueprint* posture is operator-tooling; the *voice-ai* primitive is borderline customer-facing — explicit §3.4 review needed for any v2-AI surface that exposes the AI-receptionist to diners; the *claude + chatgpt + ai-agents* posture in the topic array is on the topic array but is NOT a v1 customer-facing-AI surface; any future v2-AI surface that exposes *claude + chatgpt + ai-agents* to the owner would require explicit §3.4 review); §3.7 N/A (no privacy primitive change for the operator-side MCP-server surface). **No hard conflict** |
| 5 | Outcome, appetite, scope | ✓ alignable | v2-AI outcome (MCP-server-for-AI-receptionist-vocabulary). Max time worth spending = 0 minutes today (defer artifact); future v2-AI PR = 1-2 weeks for design + 2-3 weeks for *MCP-server + remote-mcp + streamable-http + ai-receptionist + ai-agents* surface + 1 week for verification = 1-2 months total |
| 6 | Cost to operational value | ✓ marginal | Pain frequency = low (LE31 v1 has no v2-AI MCP-server surface today; no owner has asked for v2-AI MCP-server); money vocabulary = minimal; implementation cost = 1-2 months v2-AI PR. **MARGINAL VALUE at v2-AI** |
| 7 | Circuit breaker and reversibility | ✓ reversible | Stop evidence = explicit owner/charter rejection of *MCP-server + remote-mcp + streamable-http + ai-receptionist + ai-agents + claude + chatgpt + voice-ai* adoption; review point = first v2-AI PR that proposes *MCP-server + remote-mcp + streamable-http + ai-receptionist + ai-agents* surface; migration/rollback = trivial (vocabulary-only artifact, zero code shipped); retained data = N/A |

**Final decision: `defer (parking-lot, vocabulary reference)`.**

## Files to touch (future v2-AI PR trigger)

If a future v2-AI PR is triggered by the trigger condition below, the implementation would touch:

| File | Purpose | Notes |
|---|---|---|
| `app/models/mcp_server.py` (NEW) | `McpServer` SQLModel table | `mcp_server_id, mcp_server_name, mcp_server_url, mcp_server_protocol, mcp_server_kind, mcp_server_at` |
| `app/models/mcp_tool_registry.py` (NEW) | `McpToolRegistry` SQLModel table | `registry_id, registry_name, registry_kind, registry_payload_json, registry_at, registry_owner_id` for *registry-entries* discipline |
| `app/models/mcp_tool_call.py` (NEW) | `McpToolCall` SQLModel table | `call_id, call_kind, call_payload_json, call_at, call_owner_id, call_parent_id` for *MCP-server-call* discipline |
| `app/models/mcp_claude_code_plugin.py` (NEW) | `McpClaudeCodePlugin` SQLModel table | `plugin_id, plugin_name, plugin_payload_json, plugin_at, plugin_owner_id` for *Claude-Code-plugin* discipline |
| `app/models/ai_receptionist_session.py` (NEW) | `AiReceptionistSession` SQLModel table | `session_id, session_kind, session_payload_json, session_at, session_owner_id, session_diner_id` for *ai-receptionist* discipline |
| `app/models/voice_ai_call.py` (NEW) | `VoiceAiCall` SQLModel table | `call_id, call_kind, call_audio_url, call_transcript_json, call_at, call_diner_id` for *voice-ai* discipline |
| `app/mcp_server/` (NEW directory) | MCP-server runtime | FastMCP app + MCP-server + remote-mcp + streamable-http runtime |
| `app/mcp_server/server.py` (NEW) | MCP-server entrypoint | FastMCP app + MCP-server + remote-mcp + streamable-http entrypoint |
| `app/mcp_server/tools/audit_logs.py` (NEW) | MCP tool: query audit_logs | `list_audit_logs(event_id, event_kind, event_at)` |
| `app/mcp_server/tools/stock_entries.py` (NEW) | MCP tool: query StockEntry | `list_stock_entries(item_id, entry_kind, entry_at)` |
| `app/mcp_server/tools/visits.py` (NEW) | MCP tool: query Visit | `list_visits(visit_id, visit_kind, visit_at)` |
| `app/mcp_server/tools/order_items.py` (NEW) | MCP tool: query OrderItem | `list_order_items(order_id, item_kind, item_at)` |
| `app/api/mcp_server.py` (NEW) | FastAPI route + endpoint | `/api/mcp-server` (POST register, GET list, GET show) |
| `app/templates/mcp_server.html` (NEW) | minimal-HTML/HTMX template | owner-facing surface for MCP-server with registry-entries + Claude-Code-plugin + setup |
| `migrations/versions/<hash>_add_mcp_server_tables.py` (NEW) | alembic migration | creates `mcp_server + mcp_tool_registry + mcp_tool_call + mcp_claude_code_plugin + ai_receptionist_session + voice_ai_call` tables |
| `tests/test_mcp_server.py` (NEW) | pytest coverage | covers MCP-server + remote-mcp + streamable-http + audit_logs tool + stock_entries tool + visits tool + order_items tool |

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md` + `development` skill, the future v2-AI PR would:
1. Run `pytest tests/test_mcp_server.py -v` to confirm all tests pass.
2. Run `alembic upgrade head` to confirm migrations apply cleanly.
3. Run `python -c "from app.models.mcp_server import McpServer; print(McpServer.__tablename__)"` to confirm SQLModel loads.
4. Manually verify via `curl http://localhost:8000/mcp/list_tools` that the FastMCP app returns the expected tool list (audit_logs + stock_entries + visits + order_items).
5. Manually verify via Claude-Code that the *MCP-server + remote-mcp + streamable-http + ai-receptionist + ai-agents* discipline works end-to-end (load Claude-Code → connect to MCP-server → call `list_audit_logs` → verify response → call `list_stock_entries` → verify response).
6. Run `mypy app/` + `ruff check app/` to confirm static analysis passes.
7. Confirm feature is in `Backlog` status + parent (this brainstorm parent) is in `Done` status in Linear.

## Rollback path

The defer artifact is vocabulary-only, zero code shipped, so no rollback is needed today. If a future v2-AI PR ships and the *MCP-server + remote-mcp + streamable-http + ai-receptionist + ai-agents + claude + chatgpt + voice-ai* discipline is rejected by the owner/charter:
1. Run `alembic downgrade -1` to drop the `mcp_server + mcp_tool_registry + mcp_tool_call + mcp_claude_code_plugin + ai_receptionist_session + voice_ai_call` tables.
2. Delete `app/models/mcp_server.py` + `app/models/mcp_tool_registry.py` + `app/models/mcp_tool_call.py` + `app/models/mcp_claude_code_plugin.py` + `app/models/ai_receptionist_session.py` + `app/models/voice_ai_call.py` + `app/mcp_server/` + `app/api/mcp_server.py` + `app/templates/mcp_server.html` + the alembic migration + the pytest files.
3. Re-run `alembic upgrade head` to confirm clean state.
4. Re-run `pytest -v` to confirm no regressions.

## Mandatory LE31 skill list

The future v2-AI PR author MUST load + apply these skills before any code is written:

| Skill | Why |
|---|---|
| `le31-conventions` | Repository-wide Python + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX conventions |
| `le31-v1-feature-pattern` | Existing v1 feature pattern (table management, cook-channel, stock-ledger) |
| `le31-handoff-spec` | Slice handoff format |
| `le31-coding-agent-brief` | Paste-in prompt generation from this slice contract |
| `systematic-debugging` | 4-phase root cause debugging if any test fails |
| `verify-before-fixing` | Verify diagnostic / CI / delegated subagent before fixing |
| `pre-merge-review` | Independent non-author review before merging |

## Bucket

**v2-AI** (attached to `le31 Research` P-HMM-1 per the verified workspace project list of 2026-10-06; the `le31 v2-AI` project does NOT exist per `le31-feature-pipeline/SKILL.md` line 33; the parent of the sub-issue is `le31 Research` since v2-AI bucket has no dedicated project).

## Trigger condition

First v2-AI PR that adds a `McpServer` SQLModel table + a `McpToolRegistry` + a `McpToolCall` event table + a `le31-mcp-server` FastMCP sub-app + a `/mcp/audit_logs` + `/mcp/stock_entries` + `/mcp/visits` + `/mcp/order_items` FastAPI endpoint set; OR first v2-AI PR that adopts the *official-MCP-servers-for-AI-receptionist + registry-entries + Claude-Code-plugin + setup* discipline on the existing `audit_logs`/`StockEntry`/`Visit`/`OrderItem` SQLModel table set.

## Charter compatibility

§3.1 + §3.2 STRICTLY-COMPATIBLE; §3.4 RIPGL_REVIEW REQUIRED (the *ai-receptionist* surface is borderline customer-facing if the receptionist answers diner calls; the *claude-code-plugin + setup-as-deployment-blueprint* posture is operator-tooling; the *voice-ai* primitive is borderline customer-facing — explicit §3.4 review needed for any v2-AI surface that exposes the AI-receptionist to diners).

## Companion artifacts

- Feature file: `/opt/data/le31_mmm3_research_work/features/286-gadyamedia-vocenya-mcp-mit-mcp-servers-ai-receptionist-small-business-voice-ai-v2-ai-mcp-server-ai-receptionist-vocabulary.md`
- Spec file: `/opt/data/le31_mmm3_research_work/specs/286-gadyamedia-vocenya-mcp-mit-mcp-servers-ai-receptionist-small-business-voice-ai-v2-ai-mcp-server-ai-receptionist-vocabulary-HANDOFF.md`
- Linear sub-issue: BLOCKED (workspace plan-limit error: *"You've exceeded the free issue limit for this workspace"* — **17th consecutive day**; verified today via 1 write-probe with requestId TBD; parent fallback at `/opt/data/le31-brainstorm-2026-10-06.linear-fallback.json`)
- Report: `/opt/data/le31-brainstorm-2026-10-06.md`
- Raw fetches: `/tmp/le31-brainstorm-2026-10-06/verify_gadyamedia_vocenya-mcp.json` (parent-verified direct GitHub API GET, raw JSON)
