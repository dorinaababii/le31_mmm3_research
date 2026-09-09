# Feature 163 — lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state (defer)

> **NEW observation (2026-09-09).** Documents in-window Figshare preprint **LMCP — The Local Multi-Agent Coordination Protocol** by Jolyon Grace, deposited 2026-09-04 (v1) + updated 2026-09-06 (Figshare ID `33437977`, v1 `W7208739566` + update `W7208724202`). cit=0 (preprint, no peer review yet). Description (verbatim from OpenAlex `abstract_inverted_index`): *"Standardisation in multi-agent systems has focused on two areas: how agents invoke tools or access data (MCP), and how agents discover, negotiate with, and route to one another across domains (A2A and the IETF MACP draft). These approaches assume live, session-based interaction between concurrently running agents. Local Multi-Agent Coordination Protocol (LMCP) is a protocol for coordinating multiple AI agents and human operators working asynchronously on shared mutable resources such as codebases."* **The *"AI agents and human operators working asynchronously on shared mutable resources"* combination is the most directly LE31-shape paper of the 42-pass series** — LE31 is exactly an agent + operator + shared mutable state surface (cook = human operator; waiter = human operator; owner = human operator; future v2-AI agents would be the agent). Bucket: **v2-AI watch-list** — parking-lot defer. Zero build time today.

## Goal

Retain the **"ledger-mediated control plane for asynchronous multi-agent coordination on shared mutable state"** primitive as a persistent cross-section reference for any future v2 surface that introduces an AI agent (charter §3.4 territory). The artifact is the persistent cross-section reference + a candidate *named architectural primitive* for the next v2 owner-facing agent surface. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"ledger-mediated control plane"** primitive: a coordination protocol where every coordination event is recorded as an append-only ledger row, and current state is derived from the ledger. This is the v2-AI architectural dual of LE31's `StockEntry` ledger.
- A written record of the **"AI agents and human operators working asynchronously"** pattern: the LMCP protocol explicitly recognizes that humans are *part of* the multi-agent system, not separate from it. This is the v2-AI architectural dual of LE31's charter §3.1 *"explicit user actions"* invariant.
- A written record of the **"shared mutable resources"** primitive: the LMCP protocol is designed for codebases (a canonical example), but the primitive generalizes to any operator-shared state (the LE31 `StockEntry` table, the LE31 `audit_logs` table, the LE31 `MenuItem` table).
- A decision record: today's verdict is `defer` because **LE31 v1 has no AI agent surface** (charter §3.4: no customer-facing AI; AI may assist owner/staff with observable evidence and a non-AI fallback). LMCP is a future v2 surface, not v1.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema (charter §3.1: append-only).
- Any change to the `audit_logs` schema (charter §3.1: append-only).
- Any new AI agent surface (LE31 v1 has none today; charter §3.4 explicitly rules out customer-facing AI).
- Adoption of the LMCP codebase (the paper is a preprint-only proposal; no production implementation available).
- Cross-pollination with feature 68 cook-assistant-deterministic-gate (different scope: feature 68 is a cook-facing cook-assistant surface; LMCP is a multi-agent coordination protocol).

## Evidence / JTBD

When a future LE31 v2 owner-facing AI agent surface is introduced, the operator wants *a ready-made coordination protocol for human operators + AI agents sharing state*, but struggles because *today's audit trail records only human actions*, so that *the v2 audit trail can record agent + operator actions on equal footing*.

- **Evidence class**: observed (the LMCP preprint explicitly names *"AI agents and human operators working asynchronously on shared mutable resources"* as the design target).
- **Confidence**: high for the design-target match (LE31 is exactly an agent + operator + shared mutable state surface); low for transferability (LMCP is a preprint, no peer review, no production implementation; the protocol is theoretical).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no AI agent surface.
- **The value is naming, not direct demand**: when the first v2 AI agent surface lands, the LMCP *"ledger-mediated control plane"* primitive is a ready-made *named discipline*.

## Description

The LMCP preprint by Jolyon Grace (Figshare ID `33437977`) is a multi-agent coordination protocol that distinguishes itself from MCP (Model Context Protocol — tool/data invocation) and A2A (Agent-to-Agent — peer-to-peer routing) by targeting *asynchronous coordination on shared mutable resources*. The paper's central claim is that *"these approaches [MCP, A2A] assume live, session-based interaction between concurrently running agents"* — and that for human + agent + codebase scenarios (the LE31 analog), session-based interaction is the wrong primitive.

The architectural primitive LMCP proposes has three components:

1. **Ledger-mediated control plane** — every coordination event is recorded as an append-only ledger row. The *current state* is derived from the ledger, never stored as a mutable field. This is the v2-AI architectural dual of LE31's `StockEntry` ledger (every operational transition is a new ledger row).
2. **Asynchronous coordination** — agents and operators do not need to be *concurrently running*. An agent can record an intent in the ledger; an operator can later record an authorization; an agent can later record an execution. The ledger is the coordination substrate.
3. **Shared mutable resources** — the coordination is on *mutable* resources (e.g. a codebase, a database table, a file system). The ledger is the *coordination layer*; the resource is the *work surface*. **For LE31, the resources are `StockEntry`, `audit_logs`, `MenuItem`, `Order`.**

**The 1:1 mapping onto LE31 v1 architecture:**

| LMCP primitive | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| Ledger-mediated control plane | `StockEntry` ledger + `audit_logs` table | §3.1 (every prepared-item quantity change is a new StockEntry; never update or delete ledger) | **Implemented in v1** — append-only by construction |
| Asynchronous coordination | (LE31 v1 commits are synchronous within a single SQL transaction) | §3.1 (every commit is one row, atomic) | **Implemented in v1** *for human actions only*; **future v2** for agent actions |
| Shared mutable resources | `StockEntry`, `audit_logs`, `MenuItem`, `Order` tables | §3.1 (the database tables) | **Implemented in v1** |
| AI agent surface | (LE31 v1 has no AI agent surface) | §3.4 (no customer-facing AI) | **Not implemented** — would require charter §3.4 decision |
| Human operator surface | `audit_logs.actor_user_id` + `audit_logs.actor_role` | §3.1 (every commit has an actor) | **Implemented in v1** |

**Cross-section with prior picks (LE31 cluster of 26 defer picks, this is pick #27 = +1):**

- **Feature 92 ai-agent-decision-ledger-cluster-watch** — the *multi-agent decision-ledger cluster*. LMCP is a *protocol* for multi-agent coordination; the NeuruhAI cluster is a *set of decision-ledgers* for individual agents. **LMCP is the *coordination* discipline; NeuruhAI is the *commit* discipline.**
- **Feature 126 five-primitives-Governing-AI-Agents-at-Runtime** — the *runtime governance* primitives. LMCP is the *coordination protocol*; feature 126 is the *runtime governance discipline*. **LMCP is the *how to coordinate* discipline; feature 126 is the *what to govern* discipline.**
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** — the *ledger-based control* primitive. LMCP is the *multi-agent* version of feature 127's *single-agent* primitive. **Feature 127 is the *one agent + one ledger*; LMCP is the *N agents + one ledger*.**
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** — the *trace graph* primitive. LMCP is the *coordination graph*; feature 129 is the *evidence graph*. **LMCP is the *who-did-what* graph; feature 129 is the *why-was-it-done* graph.**
- **Feature 134 echo-auditable-memory-plane-stockentry-audit** — the *auditable memory plane* primitive. LMCP is the *coordination plane*; feature 134 is the *memory plane*. **LMCP is the *coordination* surface; feature 134 is the *memory* surface.**
- **Feature 137 natural-language-policies-executable-obligations** — the *policy compilation* discipline. LMCP is the *coordination* discipline; feature 137 is the *policy* discipline. **LMCP is the *what-to-do* discipline; feature 137 is the *what-is-allowed* discipline.**
- **Feature 148 coxswain-graphs-harness-owns-consequence-architecture-pattern** — the *one harness owns every consequence* pattern. LMCP is the *multi-agent harness*; feature 148 is the *one-harness discipline*. **LMCP is the *N-harness*; feature 148 is the *1-harness*.**
- **Feature 149 personal-agent-blueprint-telegram-chokepoint-architecture-pattern** — the *authorization chokepoint* pattern. LMCP is the *coordination chokepoint*; feature 149 is the *authorization chokepoint*. **LMCP is the *coordination* chokepoint; feature 149 is the *authorization* chokepoint.**

The 27 picks form the **deepest single-vocabulary cluster in the 42-pass series** for the *append-only-ledger + audit-trail-schema + owner-pains + AI-agent-coordination* architectural pattern. **All 27 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only. LMCP is a future v2 AI agent surface and would require (optionally):
- A new `actor_type` field on `audit_logs` rows to distinguish *human operator* vs *AI agent* (charter §3.4: AI may assist owner/staff, with observable evidence).
- A new `agent_id` field on `audit_logs` rows (for AI agent identity).
- A new *coordination events* table that records agent intents + operator authorizations + agent executions as separate ledger rows (the *asynchronous coordination* primitive).

None of these are v1; all are v2 surfaces that would require an *owner decision* per charter §3.2 (and a charter §3.4 decision if any AI surface is added).

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the LMCP *"ledger-mediated control plane for asynchronous multi-agent coordination"* vocabulary to `specs/2026-09-09-lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state-HANDOFF.md`** as a named architectural primitive for any future v2 AI agent surface — already done in the HANDOFF.md.
2. **Wait for the first v2 surface that introduces an AI agent** — trigger conditions: (a) first v2 PR that adds an `actor_type` field on `audit_logs`; (b) first v2 PR that adds an `agent_id` field on `audit_logs`; (c) first v2 PR that adds a *coordination events* table.
3. **On trigger, evaluate the change against the LMCP *"ledger-mediated control plane"* primitive** — does the change preserve *append-only coordination*? Does the change preserve *asynchronous*? Does the change distinguish *human operator* vs *AI agent*? The primitive is the *what to verify*, not the *what to implement*.

## Telegram interaction if any

**None today.** The defer artifact is documentation only; no operator surface changes.

The **future v2 surface** (if the owner decides to add an AI agent) would: (a) add an `actor_type` field to `audit_logs`; (b) add an `agent_id` field to `audit_logs`; (c) modify the owner recap to expose the agent + operator coordination history. This is a *v2 surface*, not v1.

## Dependencies

- **Figshare access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.
- **Future v2 dependencies** (if LMCP is adopted): schema changes on `audit_logs`; new `actor_type` + `agent_id` fields; new coordination-events table. All future; no v1 dependency.

## Open questions

1. **Is the LMCP preprint a credible production-traction data point?** Charter §3.2: stars are popularity proxy, not gate. The LMCP preprint has 0 citations (preprint-only, no peer review); the author Jolyon Grace is a single researcher. The *protocol design* is the value; the *production traction* is not.
2. **Should the LE31 v1 `audit_logs` gain `actor_type` + `agent_id` fields today?** Charter §3.2: only data needed for restaurant operations. The owner of a small restaurant does not need AI agent tracking today; the v2 surface that needs to expose AI agent coordination needs these fields. Recommend: defer to v2 if/when the owner asks for an AI agent surface.
3. **Does the LMCP overlap with feature 127 ledger-based-control?** Partially: feature 127 is the *single-agent* version of LMCP's *multi-agent* discipline. **Feature 127 is the *one-agent + ledger*; LMCP is the *N-agents + ledger*.**
4. **Does the LMCP overlap with feature 92 ai-agent-decision-ledger-cluster-watch?** Partially: the NeuruhAI cluster is the *commit* discipline; LMCP is the *coordination* discipline. **NeuruhAI is the *what each agent commits*; LMCP is the *how agents coordinate the commits*.**
5. **Does the LMCP overlap with charter §3.4?** Yes: LMCP is an *AI agent* coordination protocol; charter §3.4 explicitly rules out customer-facing AI. LMCP is v2-AI territory; **owner decision required before any LMCP-influenced surface is scoped.**

## Why this matters

**LMCP is the most directly LE31-shape academic paper of the 42-pass series.** The *"AI agents and human operators working asynchronously on shared mutable resources"* combination is the *exact* LE31 pattern (operator = cook/waiter/owner; future agent = v2-AI; shared mutable resources = `StockEntry` + `audit_logs` + `MenuItem` + `Order`). The preprint's central claim — *"session-based interaction is the wrong primitive for human + agent scenarios"* — is the architectural inversion LE31's `StockEntry` ledger already operationalizes for human-only scenarios.

**The cluster (27 picks, this one + 26 prior) is the persistent cross-section reference for the next v2 owner-pains + AI-agent moment.** All 27 are `defer`; no code change today. The cluster is the *what the LE31 v2 owner-pains + AI-agent architecture is*, named across 27 different sources, and ready to be referenced when the first v2 AI agent surface lands.

**The most operationally valuable future v2 surface is owner daily recap with AI agent history**: introducing a Telegram-based daily recap that exposes both human actions (cook prep, waiter orders, owner reconciliation) AND AI agent actions (v2-AI suggestions, v2-AI reconciliations) on equal footing, with the LMCP *"ledger-mediated control plane"* primitive as the architectural substrate. Owner decision required; not v1.