# Feature 301 — `New1Direction-korg-mit-verifiable-cognition-ai-agents-tamper-evident-replayable-ledger-what-agent-did-why-korg-ledger-spec-rust-v2-ai-verifiable-cognition-vocabulary` (defer)

> **NEW observation (2026-10-10).** Documents in-window GitHub repo `New1Direction/korg` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **4★/0⑂**, Rust, **pushed 2026-10-05T20:54:03Z**, in-window by `pushed_at` only, **created 2026-05-21T02:40:52Z** — 142-day-old repo with in-window push, **43401 KB substantial repo**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-10): *"Verifiable cognition for AI agents — a tamper-evident, replayable ledger of what an agent did and why (korg-ledger spec)."* Topics (verbatim, parent-verified): `agents, ai, audit, autonomous, deterministic, korg-core, ledger, llm, mcp, runtime, rust, tamper-evident, verifiable` — 13 topics including **`korg-core` + `korg-ledger`** (LE31 v2-AI spec match — *named spec primitive*) + **`deterministic` + `verifiable` + `tamper-evident`** (LE31 v2-AI audit primitives) + **`mcp` + `runtime`** (LE31 v2-AI integration primitives). Bucket: **v2-AI (verifiable-cognition-vocabulary)** — Pick C of Daily Research 2026-10-10. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`verifiable cognition + tamper-evident + replayable + ledger of what an agent did and why (korg-ledger spec)`** quintuple-primitive as a persistent cross-section reference for the LE31 v2-AI *deterministic-replay + tamper-evident + what-did-the-agent-do-and-why + named-spec (korg-ledger spec)* wedge, and document the **stack-shape validation + named-spec framing + deterministic-replay discipline** that an independent maintainer arrived at in 2026 (142-day-old repo with in-window push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal + a **named-spec primitive** for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`verifiable cognition + tamper-evident + replayable + ledger of what an agent did and why (korg-ledger spec)`** quintuple-primitive: every AI-agent action is recorded as a tamper-evident entry; the entry is replayable from a deterministic starting state; the chain is organized as a ledger; the ledger answers the *what-did-the-agent-do-and-why* question; the whole thing is a *named spec* (korg-ledger spec). This is the §3.1 explicit-state-transitions + deterministic-replay + named-spec primitive applied to AI-agent action audit-logging.
- A written record of the **`Rust + korg-core + korg-ledger spec + mcp + runtime`** stack-shape: this is **0 of 4 LE31 backend stack primitives** matched (Rust is off-LE31-stack; the **korg-ledger spec** is a *specification*, not a code dependency = portable to Python); the *spec framing* bridges the off-stack Rust core.
- A written record of the **`deterministic + verifiable + tamper-evident + autonomous-agents`** operator-surface-shape: every AI-agent action is deterministic + verifiable + tamper-evident. Sister-shape to feature 232 (lpalbou/AbstractGateway — durable AI control plane with replay-first architecture) + feature 287 (noise01/endoxa — governed beliefs for LLM agents with append-only ledger + SMT-checked consistency) + feature 289 (shivamk01here/LedgerLoop — Python runtime for financial AI agents with idempotent exactly-once execution).
- A decision record: today's verdict is `defer` because (1) the repo is 4★ with single-maintainer cadence (142-day-old, in-window push today); (2) the stack-shape match is the value, not the code (LE31 v1 has no AI agent; v2-AI is OFF v1 charter; the **korg-ledger spec** is portable to any future v2-AI surface); (3) the *deterministic-replay + what-did-the-agent-do-and-why + named-spec (korg-ledger spec)* combination is the **strongest deterministic-replay vocabulary of the 72-pass series** = the demand-signal is the value.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the korg codebase (Rust off-stack; the korg-ledger spec is portable but the maintainer is single-cadence).
- Cross-pollination with the v2-AI verifiable-cognition primitive in v1 (LE31 v1 has no AI agent).
- Cross-pollination with the korg-core runtime in v1 (LE31 v1 is aiogram + FastAPI, not korg-core).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "the deterministic-replay + tamper-evident + what-did-the-agent-do-and-why + named-spec (korg-ledger spec) primitive" (e.g., a v2-AI surface that asks "what did the AI assistant do between 14:00 and 16:00 yesterday?" and the owner wants a deterministic replay of the agent's actions + the reasoning behind each action), the owner wants *a primitive that proves the demand for this shape exists in 2026 with a deterministic-replay + named-spec framing*, but struggles because *most v2-AI audit-ledger candidates lack deterministic-replay semantics OR lack a named-spec framing*, so that *the v2-AI surface has a credible peer reference with a named spec (korg-ledger spec) that any future v2 surface can reference*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `agents, ai, audit, autonomous, deterministic, korg-core, ledger, llm, mcp, runtime, rust, tamper-evident, verifiable`).
- **Confidence**: high for the vocabulary match (the verbatim description names the 4-primitive set + the tech-stack + the **korg-ledger spec** named-spec primitive); high for the **deterministic-replay signal** (the *deterministic* + *replayable* + *what-did-the-agent-do-and-why* framing is the strongest deterministic-replay vocabulary of the 72-pass series); low for code adoption.
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no AI agent); the value is the *deterministic-replay + what-did-the-agent-do-and-why + korg-ledger-spec* vocabulary — when the first v2 PR that adds a v2-AI surface lands, the korg pattern is a ready-made *named spec primitive*.

## Description

GitHub `New1Direction/korg` (MIT, 4★/0⑂, Rust, pushed 2026-10-05T20:54:03Z, created 2026-05-21T02:40:52Z, 43401 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-10): *"Verifiable cognition for AI agents — a tamper-evident, replayable ledger of what an agent did and why (korg-ledger spec)."*

The architectural primitive has five sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **`Verifiable cognition`** — the AI-agent's cognition (decisions, reasoning, action selection) is verifiable from the audit-log. The *verifiable-cognition* primitive maps 1:1 onto any future v2-AI surface that needs to answer "why did the AI assistant do X?" from the audit-log alone.
2. **`Tamper-evident`** — every audit-log entry is sealed with a hash-chain so any tampering is detectable. The *tamper-evident* primitive maps 1:1 onto LE31's §3.1 append-only discipline.
3. **`Replayable`** — every AI-agent action is replayable from a deterministic starting state. The *replayable* primitive maps 1:1 onto any future v2-AI surface that needs a `replay_agent_actions(agent_id, start_time, end_time)` endpoint that reconstructs the agent's state-transition sequence.
4. **`Ledger of what an agent did and why`** — every audit-log entry answers the *what-did-the-agent-do-and-why* question. The *what-and-why* primitive maps 1:1 onto any future v2-AI surface that needs an operator-facing *audit-explainer* primitive.
5. **`Korg-ledger spec`** — the audit-log format is specified by a named spec (korg-ledger spec). The **korg-ledger spec is the *named-spec primitive*** that future v2 surface can reference. The *named-spec* framing is the **only named-spec audit-ledger of the 72-pass series**.

**The 1:1 mapping onto LE31 surface:**

| korg primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Verifiable cognition | (LE31 v1 has no AI agent) | v2-AI | **Not implemented** — v2-AI surface |
| Tamper-evident | `audit_logs` (append-only + hash-chained) | §3.1 ✓ | **Implemented (v1, partial)** |
| Replayable | (LE31 v1 has no replay primitive) | v1 polish | **Not implemented** — v1 polish surface |
| Ledger of what an agent did and why | `audit_logs` (append-only) | §3.1 ✓ | **Implemented (v1, partial)** |
| Korg-ledger spec | (LE31 v1 has no named spec) | v2-AI | **Not implemented** — v2-AI surface |
| Deterministic | (LE31 v1 has no deterministic-replay discipline) | v1 polish | **Not implemented** — v1 polish surface |
| Autonomous-agents | (LE31 v1 has no AI agent) | v2-AI | **Not implemented** — v2-AI surface |
| MCP | (LE31 v1 has no MCP integration) | v2-AI | **Not implemented** — v2-AI surface |
| Rust core | (LE31 v1 is Python-only) | off-stack | **Not implemented** — different runtime |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface that requires deterministic-replay + tamper-evident + what-did-the-agent-do-and-why + named-spec), the implementation would add:

1. A new `AgentAction` table (Alembic migration) with columns: `id` (UUID), `agent_id` (str), `action` (str), `reasoning` (str), `proposed_payload` (JSON), `actual_payload` (JSON), `deterministic_state_hash` (str), `previous_action_hash` (str), `this_action_hash` (str), `created_at` (timezone-aware datetime), `recorded_at` (timezone-aware datetime).
2. A `korg_ledger_spec_compliance` table (Alembic migration) that tracks the spec compliance per action.
3. An `INSERT ... ON CONFLICT DO NOTHING` guard on the `AgentAction` insert path.
4. A `POST /v2/agents/<agent_id>/actions` FastAPI endpoint to record an action.
5. A `GET /v2/agents/<agent_id>/actions/replay?start=<>&end=<>` FastAPI endpoint that deterministically replays the agent's actions from a starting state.
6. A `GET /v2/agents/<agent_id>/actions/explain?action_id=<>` FastAPI endpoint that explains *what-did-the-agent-do-and-why* for a given action.
7. A `GET /v2/audit-log/spec-compliance` FastAPI endpoint that reports the korg-ledger-spec compliance.
8. A `MCP server` integration that exposes the replay + explain endpoints via MCP.

The HANDOFF is to evaluate whether the v2-AI surface is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires:

**For v2-AI verifiable-cognition-vocabulary surface** (if approved):

1. Add a new `AgentAction` SQLModel table (Alembic migration).
2. Add a new `korg_ledger_spec_compliance` SQLModel table (Alembic migration).
3. Add an `INSERT ... ON CONFLICT DO NOTHING` guard on the `AgentAction` insert path.
4. Add a `pydantic` library dependency for the deterministic-state-hash computation.
5. Add a `GET /v2/agents/<agent_id>/actions/replay?start=<>&end=<>` FastAPI endpoint.
6. Add a `GET /v2/agents/<agent_id>/actions/explain?action_id=<>` FastAPI endpoint.
7. Add a `GET /v2/audit-log/spec-compliance` FastAPI endpoint.
8. Add a `MCP server` integration via `mcp` library.
9. Document the `korg-ledger spec` adoption in `PROJECT_CHARTER.md` as a v2-AI surface primitive.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires, the v2-AI surface would add **a v2-AI owner-Telegram-notification primitive** for agent-action events (e.g. the owner gets a Telegram notification when an AI agent proposes an action, when the action is recorded, when the replay is requested, when the explain is requested). The notification primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; the korg-ledger spec is a spec, not a code dependency).
- **External**: `pydantic` library (deterministic-state-hash computation); `mcp` library (MCP-server integration); the korg-ledger spec (specification only).
- **Internal**: §3.1 (append-only discipline for `audit_logs`); §3.2 (MIT permissive license compatible); §3.4 (operator-tooling only, no customer-facing AI).
- **Trigger dependency**: future v2 PR that adds a v2-AI surface that requires deterministic-replay + named-spec (korg-ledger spec).

## Open questions

- **Q1**: When (if ever) will LE31 introduce a v2-AI surface with deterministic-replay semantics? The v1 charter explicitly excludes customer-facing AI (§3.4); v2-AI is OFF v1 charter but the §3.4 owner/staff-assist allowance leaves the door open for v2.
- **Q2**: Will the LE31 v2 surface adopt the korg-ledger spec? The korg-ledger spec is a *named spec*; adopting it is a charter decision. The benefit is a *named spec* reference for any future v2-AI audit-log.
- **Q3**: Will the LE31 v2 surface ever need a *what-did-the-agent-do-and-why* explainer? The v1 `audit_logs` is a state-transition log; the *what-and-why* explainer is a richer primitive that requires the AI agent to record its reasoning alongside the action.
- **Q4**: How will the *replayable* primitive interact with the v1 `audit_logs` schema? The v1 schema is append-only + hash-chained; the *replayable* primitive requires a *deterministic starting state* which is OFF v1 charter (the v1 state machine is too simple to need deterministic-replay).

## Why this matters

The **`verifiable cognition + tamper-evident + replayable + ledger of what an agent did and why (korg-ledger spec)`** quintuple-primitive is the **strongest direct LE31 v2-AI verifiable-cognition-vocabulary + deterministic-replay + named-spec reference of the 72-pass series** for three reasons:

1. **The 5-primitive vocabulary is the future v2-AI surface primitive**: when LE31 v2 introduces an AI-assisted owner-side workflow (e.g. an AI assistant that proposes a draft menu item, the owner wants to know *why* the AI proposed that item, and the owner wants to *replay* the AI's reasoning from a deterministic starting state), the korg pattern is a ready-made *named spec primitive*.

2. **The named-spec framing is the only named-spec audit-ledger of the 72-pass series**: the **korg-ledger spec** is a *named spec* that any future v2 surface can reference. The *named-spec* framing is the **only named-spec audit-ledger of the 72-pass series**; other v2-AI audit-ledgers (PICK A + PICK B) describe patterns but don't have a named spec.

3. **The deterministic-replay + what-did-the-agent-do-and-why framing is the strongest deterministic-replay vocabulary of the 72-pass series**: the *replayable* + *what-did-the-agent-do-and-why* framing is the **strongest deterministic-replay vocabulary of the 72-pass series**; other v2-AI audit-ledgers (PICK A + PICK B) describe audit-log patterns but don't emphasize deterministic-replay.

Sister-shape to features 232 (lpalbou/AbstractGateway — durable AI control plane with replay-first architecture) + 287 (noise01/endoxa — governed beliefs for LLM agents with append-only ledger + SMT-checked consistency) + 288 (pete-builds/mcp-nixreview — advisory NixOS change-review with CVE attestation gate) + 289 (shivamk01here/LedgerLoop — Python runtime for financial AI agents with idempotent exactly-once execution). The korg pattern is the **strongest direct deterministic-replay + named-spec v2-AI audit-ledger primitive of the cluster**.

The trigger condition for this defer artifact to become a build is: first v2 PR that adds a v2-AI surface that requires deterministic-replay + tamper-evident + what-did-the-agent-do-and-why + named-spec (korg-ledger spec).

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/142-feldroy-air-fastapi-htmx-ai-write-framework.md` — carry-over FastAPI + HTMX + Pydantic reference
- `features/187-traust-security-traust-ledger-apache-2-0-append-only-disposition-ledger-kernel-security-auditing-workflows-v2-owner-pains-architecture-reference.md` — carry-over append-only disposition ledger
- `features/199-karusrus-transparency-kit-noassertion-eu-ai-act-article-50-audit-log-hash-chained-ledger-human-gate-slack-v2-ai-compliance-primitive.md` — EU AI Act Article 50 + audit-log + hash-chained-ledger + human gate
- `features/232-lpalbou-AbstractGateway-mit-replay-first-durable-ai-control-plane-http-telegram-persistence-append-only-ledger-v2-ai-durable-control-plane.md` — durable AI control plane (sister-shape: replay-first architecture)
- `features/236-shawn-durrani-membro-mit-local-first-memory-ai-assistants-append-only-fact-ledger-deterministic-extraction-walls-immutable-transcripts-provenance-v2-ai-local-first-ai-assistant-memory.md` — local-first AI assistant memory
- `features/266-ierg-lab-ergon-mcp-server-ai-agent-tools-workspace-context-mcp-secure-tool-execution-apache-2-0-v2-ai-mcp-server-vocabulary.md` — MCP server for AI agents
- `features/287-noise01-endoxa-apache-2-0-governed-beliefs-for-llm-agents-append-only-ledger-smt-checked-consistency-defeasible-revision-calibration-python-llm-agents-truth-maintenance-v2-ai-governed-beliefs-vocabulary.md` — governed beliefs for LLM agents (sister-shape: append-only ledger + SMT-checked consistency)
- `features/288-pete-builds-mcp-nixreview-mit-advisory-nixos-change-review-cve-kev-attestation-gate-ai-agents-mcp-server-v2-ai-mcp-change-review-vocabulary.md` — advisory NixOS change-review with CVE attestation gate for AI agents
- `features/289-shivamk01here-LedgerLoop-mit-python-runtime-financial-ai-agents-idempotent-exactly-once-execution-hash-chained-ledger-v2-ai-exactly-once-execution-vocabulary.md` — Python runtime for financial AI agents with idempotent exactly-once execution
- `features/299-A220man-human-approval-console-ryan-vo-mit-review-ai-agent-actions-atomic-approval-receipts-search-receipt-ledger-verify-hash-chain-export-audit-evidence-python-fastapi-v2-ai-approval-receipt-vocabulary.md` — Pick A of Daily Research 2026-10-10 (operator-approval of AI-agent actions)
- `features/300-farooqarahim-glassbox-apache-2-0-tamper-evident-audit-ledger-ai-systems-hash-chained-hybrid-ed25519-ml-dsa-65-signed-append-only-records-llm-interaction-rust-python-typescript-go-sdks-v2-ai-eu-ai-act-ledger-vocabulary.md` — Pick B of Daily Research 2026-10-10 (EU-AI-Act + post-quantum + Python SDK v2-AI audit-ledger)
