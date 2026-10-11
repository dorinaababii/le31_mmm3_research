# Feature 302 — `warrant-ai-warrant-apache-2-0-decision-ledger-ai-agents-mandate-evidence-cost-outcome-replay-before-ship-ed25519-merkle-tree-rfc-8785-langgraph-mcp-python-temporal-v2-ai-decision-ledger-vocabulary` (defer)

> **NEW observation (2026-10-11).** Documents in-window GitHub repo `warrant-ai/warrant` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/1⑂**, Python + langgraph + MCP + Temporal + TypeScript, **pushed 2026-10-09T03:26:30Z**, in-window by `pushed_at` only, **created 2026-09-13T..Z**, **1939 KB modest repo**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-11): *"The decision ledger for AI agents. Every action recorded with its mandate, evidence, cost and outcome. Replay real decisions before you ship."* Topics (verbatim, parent-verified, 17 topics): `agent-governance, ai-agents, audit, decision-records, ed25519, governance, javascript, langgraph, llm, mcp, merkle-tree, observability, policy, python, rfc-8785, temporal, typescript` — including **`python` + `mcp` + `ed25519` + `merkle-tree` + `rfc-8785` + `langgraph` + `temporal` + `ai-agents` + `audit` + `decision-records` + `policy` + `governance` + `observability`** = the **strongest v2-AI decision-ledger Python+MCP+ed25519+merkle-tree+RFC-8785+langgraph+temporal+audit match of the 73-pass series**. Bucket: **v2-AI (decision-ledger-vocabulary)** — Pick A of Daily Research 2026-10-11. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`decision-ledger + mandate + evidence + cost + outcome + replay-before-ship + ed25519 + merkle-tree + RFC-8785 + langgraph + MCP + Python + observability + policy + temporal`** 14-dimensional primitive as a persistent cross-section reference for the LE31 v2-AI *decision-attribution with replay-before-ship semantics* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`decision-ledger + mandate + evidence + cost + outcome + replay-before-ship`** sextuple-primitive: every AI-agent action is recorded with its mandate (what the agent was authorised to do), evidence (the inputs that triggered the action), cost (resource cost of executing the action), and outcome (what actually happened). The *replay-before-ship* primitive says: before you ship a model update, replay real agent decisions from the ledger to verify the new model would have produced the same outcome. This is the §3.1 explicit-state-transitions primitive applied to AI-agent decisions with mandate+evidence+cost+outcome as the attribution quadruple + replay-before-ship as the validation primitive.
- A written record of the **`ed25519 + merkle-tree + RFC-8785 + langgraph + MCP + Python + observability + policy + temporal`** stack-shape: ed25519 for signature verification, merkle-tree for content-addressing, RFC-8785 (JSON canonicalization) for deterministic serialization, langgraph for AI-agent graph execution, MCP (Model Context Protocol) for tool invocation, Python on-stack, observability hooks, policy enforcement, temporal workflows for durability. **13 of 17 topics map 1:1 onto the LE31 v2-AI surface vocabulary**; the **Python + MCP + ed25519 + merkle-tree + RFC-8785 + langgraph + temporal** stack-match is the **strongest v2-AI decision-ledger Python+TS+MCP match of the 73-pass series**.
- A written record of the **decision-ledger-vocabulary** operator-surface-shape: every AI-agent action is recorded in an append-only ledger; the ledger is queryable by mandate / evidence / cost / outcome / timestamp; the chain is replayable end-to-end; a policy engine enforces per-action permissions. Sister-shape to feature 187 (traust-security/traust-ledger — append-only disposition ledger) + feature 232 (lpalbou/AbstractGateway — durable AI control plane) + feature 287 (noise01/endoxa — governed beliefs for LLM agents) + feature 288 (pete-builds/mcp-nixreview — MCP-server with CVE/KEV attestation gate) + feature 289 (shivamk01here/LedgerLoop — Python runtime for financial AI agents) + feature 299 (A220man/human-approval-console-ryan-vo — atomic approval receipts) + feature 300 (farooqarahim/glassbox — tamper-evident audit ledger with EU AI Act + MCP) + feature 301 (New1Direction/korg — verifiable cognition for AI agents).
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (1939 KB modest; 0★ with 1 fork); (2) the stack-shape match is the value, not the code (LE31 v1 has no AI agent; the v2-AI surface is OFF v1 charter); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the warrant-ai codebase (0★ with single-maintainer cadence; no observed production usage).
- Cross-pollination with the v2-AI decision-ledger primitive in v1 (LE31 v1 has no AI agent).
- Cross-pollination with the langgraph + MCP + Temporal stack (LE31 v1 uses FastAPI + aiogram, not langgraph or Temporal).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "the decision-ledger for AI agents with mandate + evidence + cost + outcome + replay-before-ship + ed25519 + merkle-tree + RFC-8785 + langgraph + MCP + Python + observability + policy + temporal primitive" (e.g., a v2 surface that introduces an AI-assisted owner-side workflow like "the owner asks the AI assistant to optimise the menu pricing, the AI assistant proposes a draft pricing change, the decision is recorded with mandate + evidence (the demand forecast) + cost (the compute spent) + outcome (the actual revenue change), the ledger is replayable so the owner can verify the new model would have produced the same outcome"), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "decision-ledger + mandate + evidence + cost + outcome + replay-before-ship + ed25519 + merkle-tree + RFC-8785 + langgraph + MCP + Python + observability + policy + temporal" is a real demand signal*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31 + the replay-before-ship primitive + the mandate+evidence+cost+outcome attribution quadruple"*.

- **Evidence class**: observed (the description + 17 topics name the primitives explicitly: `agent-governance, ai-agents, audit, decision-records, ed25519, governance, langgraph, llm, mcp, merkle-tree, observability, policy, python, rfc-8785, temporal`).
- **Confidence**: medium-high for the vocabulary match (the verbatim description names the 5-primitive decision-ledger set + the 14-dimensional stack-shape); low for transferability (LE31 v1 has no AI agent; v2-AI surface is OFF v1 charter).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no AI agent); the value is the *decision-ledger + mandate+evidence+cost+outcome + replay-before-ship + ed25519 + merkle-tree + RFC-8785 + langgraph + MCP + Python + observability + policy + temporal* vocabulary — when the first v2 PR that adds a v2-AI surface lands, the warrant-ai pattern is a ready-made *named primitive*.

## Description

GitHub `warrant-ai/warrant` (Apache-2.0, 0★/1⑂, Python + langgraph + MCP + Temporal + TypeScript, pushed 2026-10-09T03:26:30Z, created 2026-09-13T..Z, 1939 KB modest). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-11): *"The decision ledger for AI agents. Every action recorded with its mandate, evidence, cost and outcome. Replay real decisions before you ship."*

The architectural primitive has five sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **`Decision ledger`** — every AI-agent action is recorded in an append-only ledger (the *ledger* primitive maps 1:1 onto LE31's `audit_logs` schema). The *append-only* discipline is §3.1-aligned.
2. **`Mandate`** — the ledger entry includes the agent's mandate (what the agent was authorised to do at the time of the action). The *mandate* primitive maps 1:1 onto any future v2 surface that needs per-agent authorisation tracking.
3. **`Evidence`** — the ledger entry includes the evidence (the inputs that triggered the action: the demand forecast, the user request, the prior decision, etc.). The *evidence* primitive maps 1:1 onto any future v2 surface that needs decision-traceability.
4. **`Cost`** — the ledger entry includes the resource cost (compute time, API tokens, $ spent). The *cost* primitive maps 1:1 onto any future v2 surface that needs budget-tracking.
5. **`Outcome`** — the ledger entry includes the actual outcome (what the action produced: the new menu price, the predicted revenue change, etc.). The *outcome* primitive maps 1:1 onto any future v2 surface that needs decision-validation.
6. **`Replay-before-ship`** — before shipping a model update, replay real agent decisions from the ledger to verify the new model would have produced the same outcome. The *replay-before-ship* primitive maps 1:1 onto any future v2 surface that needs model-validation-before-deployment.

The cryptographic stack is also significant: **`ed25519`** for signature verification (every ledger entry is signed by the agent's ed25519 key); **`merkle-tree`** for content-addressing (the ledger forms a merkle-tree so any subtree can be verified independently); **`RFC-8785`** (JSON canonicalization) for deterministic serialization (so signatures are reproducible across implementations).

**The 1:1 mapping onto LE31 surface:**

| warrant-ai primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Decision ledger (append-only) | `audit_logs` (append-only atomic) | §3.1 ✓ | **Implemented (v1)** |
| Mandate | (LE31 v1 has no per-agent authorisation tracking) | v2-AI | **Not implemented** — v2-AI surface |
| Evidence | (LE31 v1 has no decision-traceability) | v2-AI | **Not implemented** — v2-AI surface |
| Cost | (LE31 v1 has no budget-tracking) | v2-AI | **Not implemented** — v2-AI surface |
| Outcome | (LE31 v1 has no decision-validation) | v2-AI | **Not implemented** — v2-AI surface |
| Replay-before-ship | (LE31 v1 has no model-validation-before-deployment) | v2-AI | **Not implemented** — v2-AI surface |
| ed25519 signatures | (LE31 v1 has no cryptographic signing) | v2-AI | **Not implemented** — v2-AI surface |
| merkle-tree content-addressing | (LE31 v1 has no merkle-tree) | v2-AI | **Not implemented** — v2-AI surface |
| RFC-8785 JSON canonicalization | (LE31 v1 has no JSON canonicalization) | v2-AI | **Not implemented** — v2-AI surface |
| langgraph agent execution | (LE31 v1 has no AI agent graph execution) | v2-AI | **Not implemented** — v2-AI surface |
| MCP tool invocation | (LE31 v1 has no MCP server) | v2-AI | **Not implemented** — v2-AI surface |
| Temporal workflows | (LE31 v1 has no Temporal) | v2-AI | **Not implemented** — v2-AI surface |
| Python on-stack | Python + FastAPI + SQLModel | §3.1 ✓ | **Implemented (v1)** |
| TypeScript frontend | (LE31 v1 uses HTMX + minimal HTML) | off-stack | **Not implemented** — different frontend |
| JavaScript SDK | (LE31 v1 has no JS SDK) | off-stack | **Not implemented** — different surface |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface that requires decision-ledger with mandate+evidence+cost+outcome+replay-before-ship semantics), the implementation would add:

1. A new `DecisionLedgerEntry` table (Alembic migration) with columns: `id` (UUID), `agent_id` (str), `mandate` (str), `evidence` (JSON), `cost` (JSON), `outcome` (JSON), `decided_at` (timezone-aware datetime), `previous_entry_hash` (str), `this_entry_hash` (str), `ed25519_signature` (str).
2. A `merkle_tree` column on the `DecisionLedgerEntry` table (or a separate `merkle_tree` table) that stores the merkle-root for the subtree containing this entry.
3. A `policy_engine` table (Alembic migration) with columns: `id` (UUID), `agent_id` (str FK), `action` (str), `allowed` (bool), `enforced_at` (timezone-aware datetime).
4. A `langgraph_agent` table (Alembic migration) with columns: `id` (UUID), `name` (str), `description` (str), `graph_definition` (JSON), `created_at`, `updated_at`.
5. A `decision_ledger_search` view over `DecisionLedgerEntry` that exposes `GET /v2/decision-ledger/search?agent=<>&mandate=<>&as_of=<>`.
6. A `decision_ledger_replay` endpoint that walks the chain from a given timestamp to "now" and returns all entries in order.
7. A `decision_ledger_verify` endpoint that walks the chain from genesis to the latest entry and verifies each `ed25519_signature == ed25519(this_entry_hash)` and `this_entry_hash == SHA-256(previous_entry_hash + RFC-8785(entry_payload))`.
8. A `decision_ledger_export` endpoint that exports the chain as a downloadable JSON file.

The HANDOFF is to evaluate whether the v2-AI surface is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires:

**For v2-AI decision-ledger-vocabulary surface** (if approved):

1. Add a new `DecisionLedgerEntry` SQLModel table (Alembic migration).
2. Add a new `policy_engine` SQLModel table (Alembic migration).
3. Add a new `langgraph_agent` SQLModel table (Alembic migration).
4. Add an `INSERT ... ON CONFLICT DO NOTHING` guard on the `DecisionLedgerEntry` insert path.
5. Add a `merkle_tree.py` utility module that computes the merkle-root for a given set of ledger entries.
6. Add a `rfc8785_canonical.py` utility module that JSON-canonicalizes a Python dict per RFC-8785.
7. Add a `ed25519_sign.py` utility module that signs/verifies with ed25519.
8. Add a `GET /v2/decision-ledger/search?agent=<>&mandate=<>&as_of=<>` FastAPI endpoint.
9. Add a `GET /v2/decision-ledger/replay?from=<>&to=<>` FastAPI endpoint.
10. Add a `GET /v2/decision-ledger/verify` FastAPI endpoint that walks the chain from genesis to the latest entry and verifies ed25519 signatures + merkle-tree + RFC-8785 canonicalization.
11. Add a `GET /v2/decision-ledger/export?format=json` FastAPI endpoint.
12. Add a `POST /v2/agents/<agent_id>/decisions/propose` FastAPI endpoint that records a proposed decision.
13. Add a `POST /v2/agents/<agent_id>/decisions/<decision_id>/execute` FastAPI endpoint that records the execution outcome.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires, the v2-AI surface would add **a v2-AI owner-Telegram-notification primitive** (e.g. the owner gets a Telegram notification when an AI-agent decision is proposed + when it is executed + when the outcome is recorded). The notification primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot).

## Dependencies

- Python 3.13 on-stack (LE31 pins Python 3.13).
- FastAPI on-stack (LE31 pins FastAPI).
- Postgres on-stack (LE31 pins Postgres).
- ed25519 (`cryptography` library or `ed25519` package) — NEW transitive dependency for v2-AI surface.
- merkle-tree (`merkletools` or custom implementation) — NEW transitive dependency for v2-AI surface.
- RFC-8785 (`canonicaljson` package) — NEW transitive dependency for v2-AI surface.
- langgraph — NEW transitive dependency for v2-AI surface (off-LE31-stack today).
- MCP server framework — NEW transitive dependency for v2-AI surface (off-LE31-stack today).
- Temporal — NEW transitive dependency for v2-AI surface (off-LE31-stack today).

## Open questions

- **None today.** The defer artifact is documentation only.

## Why this matters

- **Vocabulary persistence**: the **`decision-ledger + mandate + evidence + cost + outcome + replay-before-ship`** sextuple-primitive is a **named primitive** that any future LE31 v2-AI surface can reference without re-deriving the concept. The verbatim description names the 5-primitive set (`decision ledger + mandate + evidence + cost + outcome + replay-before-ship`) + the cryptographic stack (`ed25519 + merkle-tree + RFC-8785`) + the AI-agent framework stack (`langgraph + MCP + Temporal`) + the language pair (`Python + TypeScript`).
- **Stack-shape validation**: the **`Python + MCP + ed25519 + merkle-tree + RFC-8785 + langgraph + Temporal`** stack-shape arrived at independently in 2026 by an Apache-2.0 maintainer with no LE31 charter visibility. This validates that the LE31 v2-AI stack-direction (Python on-stack + AI-agent framework + cryptographic-verifiability surface) is a real 2026 demand signal.
- **Replay-before-ship primitive**: the *replay-before-ship* primitive is the **strongest model-validation-before-deployment vocabulary** of the 73-pass series. The *replay-real-decisions-before-you-ship* framing is a v2-AI model-validation primitive that LE31 v1 has no equivalent of today.
- **Sister-shape to features 187+188+232+287-289+299+300+301**: warrant-ai/warrant is the 9th addition to the persistent v2-AI audit-trail-decision vocabulary cluster (the 73-pass series). The cluster now covers: append-only disposition (traust-ledger) + durable AI control plane (lpalbou/AbstractGateway) + governed beliefs (noise01/endoxa) + MCP CVE-attestation (pete-builds/mcp-nixreview) + Python runtime for financial AI agents (shivamk01here/LedgerLoop) + atomic approval receipts (A220man/human-approval-console-ryan-vo) + EU AI Act + post-quantum (farooqarahim/glassbox) + verifiable cognition (New1Direction/korg) + **decision-ledger with mandate+evidence+cost+outcome+replay-before-ship (warrant-ai/warrant)** = the strongest v2-AI audit-trail-decision vocabulary cluster of the 73-pass series.