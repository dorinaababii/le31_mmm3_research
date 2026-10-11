# Feature 307 — `felipesauer-mnema-apache-2-0-signed-append-only-ai-coding-agents-decision-records-adr-tamper-evident-mcp-server-claude-code-codex-copilot-opencode-vscode-cursor-guardrails-audit-trail-v2-ai-vocab` (defer)

> **NEW observation (2026-10-11).** Documents in-window GitHub repo `felipesauer/mnema` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, **4★/0⑂**, **22954 KB substantial = 2nd-largest in-window v2-AI append-only-decision-record of the 74-pass series**, TypeScript off-§3.1 stack for LE31 v1 today but the **signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint** vocabulary IS stack-agnostic and IS portable to Python, **pushed 2026-10-11T05:45:12Z = TODAY** AND **created 2026-05-06T17:57:50Z** = ~5-month-old repo with today's push, default_branch=`main`, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-11): *"Signed, append-only decision records for AI coding agents: an MCP server and CLI that open Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, VS Code and Cursor sessions with your team's decisions, hold the edits a rule governs, and let anyone verify the record offline. Tamper-evident, in git."* Topics (verbatim, parent-verified, 20): `adr, agent-memory, ai-agents, ai-governance, append-only, architecture-decision-records, audit-trail, claude-code, claude-code-plugin, codex, coding-agents, cursor, gemini-cli, github-copilot, guardrails, mcp, mcp-server, opencode, tamper-evident, vscode`. Bucket: **v2-AI (signed-append-only-AI-coding-agents-decision-records-vocabulary)** — Pick C of Daily Brainstorm 2026-10-11. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **signed-append-only-decision-records-for-AI-coding-agents + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint + agent-memory + ai-governance + coding-agents + ai-agents** 20-tuple-primitive as a persistent cross-section reference for the LE31 v2-AI *signed-append-only-decision-records-for-AI-coding-agents* wedge, and document the **signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint** discipline that an independent maintainer arrived at in 2026 (~5-month-old repo with today's push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **signed-append-only-decision-records-for-AI-coding-agents + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint** 20-tuple-primitive: every AI-coding-agent decision is recorded in a signed-append-only ledger; edits that a rule governs are held; anyone can verify the record offline. This is the §3.1 explicit-state-transitions + §3.3 *append-only-ledger-as-immutable-audit-trail + cryptographic-signature-as-audit-evidence* + §3.4 *MCP-as-cross-system-tooling + deterministic-rule + non-AI-fallback* invariant applied to the *AI-coding-agent-decision* dimension.
- A written record of the **Apache-2.0 + 4★/0⑂ + 22954 KB substantial + 20-topic array + TypeScript off-§3.1 stack but portable + pushed 2026-10-11T05:45:12Z = TODAY** stack-shape: this is the **strongest v2-AI signed-append-only-AI-coding-agents-decision-records-vocabulary candidate of the 74-pass brainstorm series**.
- A written record of the **operator-facing vocabulary** discipline: every AI-coding-agent decision is recorded in a signed-append-only ledger; the ledger is tamper-evident; the ledger is in git; the ledger is verifiable offline; edits that a rule governs are held; the ledger is exposed via MCP-server. Sister-shape to features 197 (rajo69/ledgerkb) + 245 (EvezArt/evez-event-spine) + 271 (znbsf/agent-case-graph) + 284 (S0tman/irp-capture) + 286 (gadyamedia/vocenya-mcp) + 300 (farooqarahim/glassbox) — the *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* posture IS the canonical v2-AI signed-append-only-AI-coding-agents-decision-records-vocabulary applied to the *AI-coding-agent-decision* dimension.
- A decision record: today's verdict is `defer` because (1) the v2-AI roadmap is not yet active (LE31 v1 is the current focus); (2) the stack-shape match is the value, not the code (LE31 v1 has no AI-coding-agent-decision surface; the v1 charter is HTMX + Postgres, not TypeScript + MCP-server + claude-code/codex/copilot/opencode/vscode/cursor); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the mnema codebase (TypeScript + ~5-month-old repo with today's push + Apache-2.0 permissive + 4★/0⑨).
- Cross-pollination with the v2-AI roadmap §3.3 *append-only-ledger-as-immutable-audit-trail + cryptographic-signature-as-audit-evidence* + §3.4 *MCP-as-cross-system-tooling + deterministic-rule + non-AI-fallback* posture (the *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails* discipline IS the §3.3 + §3.4 invariant).
- Any vendor-relationship with TypeScript / Node.js / MCP-server / claude-code / codex / copilot / opencode / vscode / cursor (LE31 v1 uses Python + FastAPI + Postgres, not TypeScript + Node.js + MCP-server + claude-code/codex/copilot/opencode/vscode/cursor).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v2-AI code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "a signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint primitive" (e.g., a v2-AI surface that introduces a signed-append-only-decision-record for the LE31 single-restaurant Swiss kitchen where the owner wants every AI-coding-agent decision to be recorded in a signed-append-only ledger, with tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "signed-append-only-decision-records-for-AI-coding-agents + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint" is a real demand signal*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same signed-append-only-decision-record posture + the ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint posture"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `adr, agent-memory, ai-agents, ai-governance, append-only, architecture-decision-records, audit-trail, claude-code, claude-code-plugin, codex, coding-agents, cursor, gemini-cli, github-copilot, guardrails, mcp, mcp-server, opencode, tamper-evident, vscode` + *"Signed, append-only decision records for AI coding agents: an MCP server and CLI that open Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, VS Code and Cursor sessions with your team's decisions, hold the edits a rule governs, and let anyone verify the record offline. Tamper-evident, in git."*).
- **Confidence**: medium-high for the vocabulary match (the verbatim description + topics name the 20-tuple-primitive set + the signed-append-only-decision-records posture + the ADR posture + the tamper-evident posture + the audit-trail posture + the MCP-server posture + the guardrails posture + the claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint posture + the in-git posture); low for transferability (LE31 v1 has no AI-coding-agent-decision surface; v1 charter is HTMX + Postgres, not TypeScript + MCP-server + claude-code/codex/copilot/opencode/vscode/cursor).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no AI-coding-agent-decision surface; v2-AI roadmap is not yet active); the value is the *signed-append-only-decision-records-for-AI-coding-agents + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* vocabulary — when the first v2-AI PR that adds a signed-append-only-decision-record surface lands, the mnema pattern is a ready-made *named primitive*.

## Description

GitHub `felipesauer/mnema` (Apache-2.0, 4★/0⑂, TypeScript, pushed 2026-10-11T05:45:12Z, created 2026-05-06T17:57:50Z, 22954 KB, default_branch=`main`, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-11): *"Signed, append-only decision records for AI coding agents: an MCP server and CLI that open Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, VS Code and Cursor sessions with your team's decisions, hold the edits a rule governs, and let anyone verify the record offline. Tamper-evident, in git."*

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **Signed-append-only-decision-records-for-AI-coding-agents** — every AI-coding-agent decision is recorded in a signed-append-only ledger. The *signed-append-only-decision-record* primitive maps 1:1 onto any future v2-AI surface that needs a signed-append-only-decision-record for the LE31 single-restaurant Swiss kitchen.
2. **ADR (Architecture Decision Records)** — decisions are recorded as ADRs. The *ADR* posture IS the §3.1 *explicit-state-transitions* charter invariant applied to the *AI-decision* dimension.
3. **Tamper-evident** — the ledger is tamper-evident. The *tamper-evident* posture IS the §3.3 *cryptographic-signature-as-audit-evidence* charter invariant applied to the *AI-decision* dimension.
4. **Audit-trail** — the ledger is an audit trail. The *audit-trail* posture IS the §3.3 *append-only-ledger-as-immutable-audit-trail* charter invariant applied to the *AI-decision* dimension.
5. **MCP-server** — the ledger is exposed via MCP-server. The *MCP-server* posture IS the §3.4 *MCP-as-cross-system-tooling* charter invariant applied to the *AI-decision* dimension.
6. **Guardrails** — edits that a rule governs are held. The *guardrails* posture IS the §3.4 *deterministic-rule + non-AI-fallback* charter invariant applied to the *AI-decision* dimension.
7. **Claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint** — the ledger is integrated with Claude Code, Codex, Copilot CLI, OpenCode, VS Code and Cursor. The *claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* posture IS the §3.4 *cross-system-tooling* charter invariant applied to the *AI-coding-agent* dimension.
8. **In-git** — the ledger is in git. The *in-git* posture IS the §3.1 *version-controlled-audit-trail* charter invariant applied to the *AI-decision* dimension.
9. **Verify-the-record-offline** — anyone can verify the record offline. The *verify-the-record-offline* posture IS the §3.4 *observable-evidence* charter invariant applied to the *AI-decision* dimension.
10. **Agent-memory** — the ledger is agent-memory. The *agent-memory* posture IS the §3.4 *agent-memory* charter invariant applied to the *AI-decision* dimension.
11. **AI-governance** — the ledger is AI-governance. The *AI-governance* posture IS the §3.4 *AI-governance* charter invariant applied to the *AI-decision* dimension.
12. **Coding-agents** — the ledger is for coding-agents. The *coding-agents* posture IS the §3.4 *coding-agents* charter invariant applied to the *AI-decision* dimension.
13. **AI-agents** — the ledger is for AI-agents. The *AI-agents* posture IS the §3.4 *AI-agents* charter invariant applied to the *AI-decision* dimension.
14. **Gemini-cli** — the ledger is integrated with Gemini CLI. The *gemini-cli* posture IS the §3.4 *cross-system-tooling* charter invariant applied to the *AI-coding-agent* dimension.
15. **Github-copilot** — the ledger is integrated with GitHub Copilot. The *github-copilot* posture IS the §3.4 *cross-system-tooling* charter invariant applied to the *AI-coding-agent* dimension.
16. **Opencode** — the ledger is integrated with OpenCode. The *opencode* posture IS the §3.4 *cross-system-tooling* charter invariant applied to the *AI-coding-agent* dimension.
17. **Claude-code-plugin** — the ledger is exposed as a Claude Code plugin. The *claude-code-plugin* posture IS the §3.4 *cross-system-tooling* charter invariant applied to the *AI-coding-agent* dimension.
18. **Claude-code** — the ledger is integrated with Claude Code. The *claude-code* posture IS the §3.4 *cross-system-tooling* charter invariant applied to the *AI-coding-agent* dimension.
19. **Cursor** — the ledger is integrated with Cursor. The *cursor* posture IS the §3.4 *cross-system-tooling* charter invariant applied to the *AI-coding-agent* dimension.
20. **VSCode** — the ledger is integrated with VS Code. The *vscode* posture IS the §3.4 *cross-system-tooling* charter invariant applied to the *AI-coding-agent* dimension.

**The 1:1 mapping onto LE31 surface:**

| mnema primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Signed-append-only-decision-records-for-AI-coding-agents | (LE31 v1 has no signed-append-only-decision-record surface) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| ADR (Architecture Decision Records) | (LE31 v1 has no ADR surface) | §3.1 ✓ | **Not implemented** — v2-AI polish surface |
| Tamper-evident | (LE31 v1 has no tamper-evident surface) | §3.3 ✓ | **Not implemented** — v2-AI polish surface |
| Audit-trail | `audit_logs` (append-only) | §3.3 ✓ | **Implemented (v1, partial)** — the *append-only* discipline is implemented in v1, but the *tamper-evident + audit-trail* posture is a sister-shape |
| MCP-server | (LE31 v1 has no MCP-server) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| Guardrails | (LE31 v1 has no guardrails surface) | §3.4 ✓ | **Not implemented** — v2-AI polish surface |
| Claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint | (LE31 v1 has no AI-coding-agent surface) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| In-git | (LE31 v1 has no in-git ledger surface) | §3.1 ✓ | **Not implemented** — v2-AI polish surface |
| Verify-the-record-offline | (LE31 v1 has no offline-verification surface) | §3.4 ✓ | **Not implemented** — v2-AI polish surface |
| Agent-memory | (LE31 v1 has no agent-memory surface) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| AI-governance | (LE31 v1 has no AI-governance surface) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| Coding-agents | (LE31 v1 has no coding-agents surface) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| AI-agents | (LE31 v1 has no AI-agents surface) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| Gemini-cli | (LE31 v1 has no Gemini CLI) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| Github-copilot | (LE31 v1 has no GitHub Copilot) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| Opencode | (LE31 v1 has no OpenCode) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| Claude-code-plugin | (LE31 v1 has no Claude Code plugin) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| Claude-code | (LE31 v1 has no Claude Code) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| Cursor | (LE31 v1 has no Cursor) | v2-AI polish | **Not implemented** — v2-AI polish surface |
| VSCode | (LE31 v1 has no VS Code) | v2-AI polish | **Not implemented** — v2-AI polish surface |

## Data model

```
MnemaDecisionRecord  (id, agent_id, decision_type, decision_payload_json,
                     signature, public_key, hash_chain_prev, hash_chain_self,
                     verified_at_utc, verified_by, in_git_commit_sha)
MnemaRule            (id, name, rule_code, enforcement_type, active, hold_edits)
MnemaGuardrailHit   (id, decision_record_id, rule_id, hit_at_utc, action_taken,
                     hold_status)
MnemaMcpServer       (id, decision_record_id, mcp_tool_name, mcp_payload_json,
                     timestamp_utc)
```

## Implementation steps

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* discipline lands, the implementation steps are:

1. Add the four tables above as a migration under `backend/alembic/versions/`.
2. Add a `MnemaDecisionRecordBuilder` class that creates a signed-append-only-decision-record for every AI-coding-agent decision.
3. Add a `MnemaRuleEngine` that holds edits that a rule governs.
4. Add a `MnemaGuardrail` that enforces deterministic rules.
5. Add a `MnemaHashChain` that links every decision record to the previous one via a cryptographic hash.
6. Add a `/api/mnema-decision-records` FastAPI endpoint that returns the decision-records ledger.
7. Add a `mnema-decision-records.html` minimal-HTML/HTMX template that renders the ledger as a navigable tree.
8. Add a `McpServerForMnemaDecisionRecords` FastMCP sub-app that exposes the ledger via MCP-server for cross-tool consumption.
9. Add a unit test that verifies the signed-append-only-decision-record discipline is correctly enforced.
10. Add an integration test that verifies the MCP-server exposes the ledger correctly.

## Telegram interaction if any

None today. The defer artifact is documentation only. When the first v2-AI PR that adopts the *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* discipline lands, the Telegram interaction is the cook Telegram bot receiving a notification when a new decision record is created (e.g., *"A new mnema decision record was created: agent=claude-code, decision=add-table-T5, hash_chain_self=abc123"*) and the owner daily-recap consuming the ledger as an audit trail (e.g., *"Today, 12 new mnema decision records were created; 3 records were rejected by the guardrails"*).

## Dependencies

- [02-order-taking.md](02-order-taking.md) — every waiter-web-UI interaction triggers an order; the mnema-decision-record tracks the order-taking primitive.
- [../research/01-pos-systems.md](../research/01-pos-systems.md) — TastyIgniter's AI-coding-agent-decision model as a reference.
- [../features/197-rajo69-ledgerkb-...-v2-owner-pains.md](../features/197-rajo69-ledgerkb-...-v2-owner-pains.md) — sister-shape for evidence-bearing-assertions + append-only-ledger.
- [../features/245-EvezArt-evez-event-spine-...-append-only-hash-linked-event-log-...-v2-owner-pains.md](../features/245-EvezArt-evez-event-spine-...-append-only-hash-linked-event-log-...-v2-owner-pains.md) — sister-shape for append-only-hash-linked-event-log.
- [../features/271-znbsf-agent-case-graph-...-v2-owner-pains-audit-architecture-reference.md](../features/271-znbsf-agent-case-graph-...-v2-owner-pains-audit-architecture-reference.md) — sister-shape for evidence-first-append-only-case-ledger.
- [../features/284-S0tman-irp-capture-...-v2-owner-pains-decision-rationale-ledger-vocabulary.md](../features/284-S0tman-irp-capture-...-v2-owner-pains-decision-rationale-ledger-vocabulary.md) — sister-shape for append-only-ledger-that-records-why-decisions-were-made.
- [../features/286-gadyamedia-vocenya-mcp-...-v2-ai-mcp-server-ai-receptionist-vocabulary.md](../features/286-gadyamedia-vocenya-mcp-...-v2-ai-mcp-server-ai-receptionist-vocabulary.md) — sister-shape for mcp-servers-ai-receptionist-small-business.
- [../features/300-farooqarahim-glassbox-...-v2-ai-eu-ai-act-ledger-vocabulary.md](../features/300-farooqarahim-glassbox-...-v2-ai-eu-ai-act-ledger-vocabulary.md) — sister-shape for tamper-evident-audit-ledger-ai-systems.

## Open questions

- Does the signed-append-only-decision-record vocabulary need to support multi-party signing (e.g., cook + owner + supplier) or is single-party signing sufficient?
- Does the tamper-evident posture require a specific cryptographic-signature scheme (e.g., Ed25519, RSA-4096, ML-DSA-65) or is it signature-scheme-agnostic?
- Does the in-git posture require a specific git-hosting platform (e.g., GitHub, GitLab, Bitbucket) or is it git-hosting-platform-agnostic?
- Does the claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint posture require all 7 integrations or is a subset acceptable?

## Why this matters

LE31 v1 today has *waiter web UI + cook Telegram bot + owner daily-recap* but has *no signed-append-only-decision-records-for-AI-coding-agents surface* (no ADR; no tamper-evident; no MCP-server; no AI-coding-agent). The *signed-append-only-decision-records-for-AI-coding-agents + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* discipline IS the canonical v2-AI signed-append-only-AI-coding-agents-decision-records-vocabulary that would let a future v2-AI PR add a *signed-append-only-decision-records-for-AI-coding-agents* surface that records every AI-coding-agent decision in a signed-append-only ledger, holds edits that a rule governs, and lets anyone verify the record offline. The Apache-2.0 + 20-topic + 22954 KB substantial + pushed 2026-10-11T05:45:12Z = TODAY stack is **§3.1 + §3.2 + §3.3 + §3.4 ON-PATTERN** for LE31; the *signed-append-only-decision-records-for-AI-coding-agents + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* discipline IS stack-agnostic and IS the §3.3 *append-only-ledger-as-immutable-audit-trail + cryptographic-signature-as-audit-evidence* + §3.4 *MCP-as-cross-system-tooling + deterministic-rule + non-AI-fallback* charter invariant applied to the *AI-coding-agent-decision* dimension; the cross-section vocabulary is informative, not a v2-AI-build trigger.