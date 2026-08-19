# Feature 86 — Salestrics MCP-Native CRM Watch

> **Priority**: P3 (parking-lot) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-19 (Pick C, parking-lot — MCP surface not in v1/v2 scope; only 1 HN point) · **Bucket**: v2-AI control-plane (parking-lot, future-MCP-integration-planning)
> **One-line**: A research-only parking-lot artifact that records the in-window HN Show HN of `Salestrics` (1pt 2026-08-08, "An open MCP server and CRM for AI-native revenue teams", `https://www.salestrics.com/`) as a **peer signal** for the MCP-native small-team pattern. **No code is shipped today**; the artifact is a parking-lot note for future v2-AI MCP integration planning. Re-evaluation trigger: MCP protocol stabilizes at v1.0 OR ≥3 in-window MCP-native small-team SaaS peers surface with public repos.

## Goal

The cross-section signal is **MCP-native + solo-builder + small-team-CRM-shape + AI-native-from-day-one** as a **reference architecture** for any future LE31 v2-AI MCP-server surface. LE31's v2-AI control-plane lane (features 58 operator-ai-action-surface, 62 agents-yaml-ontology-config, 63 second-opinion-verifier-role, 68 cook-assistant-deterministic-gate) sketches what an agent surface *would* look like if shipped. The Salestrics peer validates that the integration fabric (Model Context Protocol, late-2024) is real and growing in the small-team SaaS lane.

The pattern is observed in **`Salestrics`** (HN 1pt 2026-08-08 — "An open MCP server and CRM for AI-native revenue teams", `https://www.salestrics.com/`). The peer is the **first in-window HN Show HN that explicitly positions as MCP-native**, validating that small-team operators are willing to build + ship the integration fabric from day one.

**This is a parking-lot artifact, not a feature contract.** No code is shipped today. The artifact documents the peer signal + the cross-section mapping for future v2-AI MCP integration planning.

## Scope

**In scope (v2-AI control-plane parking-lot, S effort, no code):**

- Record the in-window HN Show HN of `Salestrics` (1pt 2026-08-08) as peer signal for the MCP-native small-team pattern.
- Document the cross-section mapping to LE31 features 58 / 62 / 63 / 68 (v2-AI control-plane lane).
- Document the re-evaluation trigger: revisit when (i) MCP protocol stabilizes at v1.0 (currently in active spec churn), OR (ii) ≥3 in-window MCP-native small-team SaaS peers surface with public repos, OR (iii) the LE31 owner explicitly asks for external-agent integration.

**Out of scope (v2-AI control-plane parking-lot):**

- **Building an MCP-server surface for LE31**. This requires explicit charter approval (charter §3.1 defines the two primary operational surfaces — waiter web UI + cook Telegram bot — and does not include an MCP-server surface).
- Tool registration, auth model, MCP protocol conformance, security review (all required before any MCP surface scope is opened).
- LLM-assisted agent integration for LE31 (already covered by features 58 / 62 / 63 / 68 in the v2-AI control-plane lane; the MCP-server surface is the **integration fabric** that wraps those features, not a replacement).

## Description

**Evidence precondition:** observed (in-window HN Show HN of `Salestrics`, 1pt 2026-08-08, MCP-native small-team CRM). Confidence: **low** for the peer signal (1 HN point = weak validation; no public repo to read; no star count; team size unknown), **high** for the architectural relevance (MCP-native is a real and growing integration fabric in the small-team SaaS lane).

**Cross-validation anchors:**

- Features 58 / 62 / 63 / 68 sit in the v2-AI control-plane lane and sketch what an agent surface *would* look like if shipped.
- The MCP-native small-team pattern (Salestrics) is a reference architecture for **how** to ship such a surface — auth model, tool registration, protocol conformance, security review.
- Anthropic's Model Context Protocol (late-2024) is the integration fabric LE31's eventual bot/agent surface would naturally speak to; Salestrics validates the pattern is real and growing.

**Decision: parking-lot.** The cross-section is real but the peer signal is weak and the scope is significant (MCP-server surface requires explicit charter approval). File as a parking-lot artifact with a clear re-evaluation trigger.

## Data model

No data model changes today. When re-elevated to charter-approved scope, the MCP-server surface would require:

```
McpTool              (id, name, description, input_schema, handler_ref, requires_auth, rate_limit)
McpCall              (id, tool_id, agent_id, called_at, input, output, status, latency_ms)
McpAuth              (id, agent_id, token_hash, scopes, granted_at, revoked_at)
```

Three new tables, append-only `McpCall` (per charter §3.1 stock + state invariants), `McpAuth` revocable (per charter §3.2 privacy: store only data needed for restaurant operations).

## Implementation steps (when re-elevated — NOT planned today)

1. **Verify charter approval** for an MCP-server surface (charter §3.1 explicitly defines two operational surfaces; MCP-server is a third that needs charter sign-off).
2. **Read MCP protocol spec** (Anthropic's MCP v1.0 spec; verify stability before scoping).
3. **Add the three tables** in `backend/app/models/mcp.py` (SQLModel).
4. **Three Alembic migrations** adding the tables.
5. **Add the MCP server** in `backend/app/services/mcp_server.py` (FastAPI route for MCP protocol).
6. **Wire LE31 tools** (`le31.stock.add`, `le31.table.status`, `le31.recap.shift`) — one per v2-AI control-plane feature.
7. **Add the auth layer** (token issuance, scope enforcement, revocation).
8. **Add the rate limiter** (per-tool, per-agent).
9. **Add 10 acceptance tests** in `backend/tests/test_mcp_server.py`.
10. **Commit and push** with message `Add MCP-server surface for LE31 v2-AI control-plane (feature 86)`.

## Telegram interaction

None directly. The MCP-server surface is an integration fabric for external agents (Claude Desktop, Cursor, etc.), not a user-facing Telegram surface. The cook bot's existing surface continues to handle owner/staff interactions.

## Dependencies

- **Explicit charter approval** for the MCP-server surface (charter §3.1).
- MCP protocol stability at v1.0 (currently in active spec churn).
- The existing v2-AI control-plane features (58 / 62 / 63 / 68) — the MCP-server wraps these, it does not replace them.
- Anthropic's MCP SDK for Python (or a community alternative) — would need to be added to the dependency manifest.
- No LE31 schema changes required (the three new tables are additive).

## Open questions

- **Q1: Does the LE31 owner actually want external-agent integration?** The artifact assumes the demand exists; no observed evidence. Re-evaluate when the owner explicitly asks.
- **Q2: Is MCP the right integration fabric, or will a successor protocol win?** Currently MCP is the de facto standard for small-team agent surfaces; if a successor emerges (e.g., Google's Agent2Agent, OpenAI's agent protocol), re-evaluate.
- **Q3: What is the security review scope for an MCP-server surface?** Auth model + token issuance + scope enforcement + rate limiting + audit log (the `McpCall` table is the audit log) are all required; the security review would need to be scoped separately before any MCP-server work begins.
- **Q4: How does the MCP-server surface interact with the existing cook bot's command surface?** Some MCP tools might duplicate cook bot commands; the design must ensure the cook bot remains the primary owner/staff-facing surface.

## Why this matters

MCP-native is a relatively new architectural primitive (Anthropic's Model Context Protocol, late-2024). A solo-founder CRM launching in this window as MCP-native validates that small-team operators are willing to build + ship the integration fabric from day one. The cross-section with LE31's v2-AI control-plane lane is direct: features 58 / 62 / 63 / 68 all sketch a control-plane that an external agent would naturally drive via MCP. The Salestrics peer is useful as a **reference architecture** for how a small-team CRM ships MCP from day one.

**Risk of NOT tracking the MCP-native pattern:** if a future LE31 v2-AI MCP-server surface is scoped without the benefit of observing how small-team SaaS operators are shipping MCP-native today, the surface design could miss important lessons (auth model, tool registration, rate limiting, security review).

**Risk of building without charter approval:** the scope is significant (3 new tables, an MCP server, an auth layer, a rate limiter, 10 acceptance tests, a security review); charter approval is essential before any work begins.

## Status: parking-lot (research-only, no code)

This file is a **parking-lot artifact (no code shipped today)**. The slice boundary is hard: zero source-code changes, zero migrations, zero new dependencies. The artifact lives in this file and the corresponding HANDOFF.md.

The watch should be re-evaluated when: (i) MCP protocol stabilizes at v1.0, OR (ii) ≥3 in-window MCP-native small-team SaaS peers surface with public repos, OR (iii) the LE31 owner explicitly asks for external-agent integration.
