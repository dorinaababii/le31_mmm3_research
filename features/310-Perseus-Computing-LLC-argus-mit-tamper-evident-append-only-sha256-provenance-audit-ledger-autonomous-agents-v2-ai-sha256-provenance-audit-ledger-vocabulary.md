# Feature 310 — `Perseus-Computing-LLC-argus-mit-tamper-evident-append-only-sha256-provenance-audit-ledger-autonomous-agents-v2-ai-sha256-provenance-audit-ledger-vocabulary` (defer)

> **NEW observation (2026-10-12).** Documents in-window GitHub repo `Perseus-Computing-LLC/argus` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/1⑂**, Python, **pushed 2026-10-12T01:44:49Z = TODAY**, in-window by `pushed_at` only, **39 KB tiny = 2nd-smallest v2-AI pick of the 74-pass series**). Description (verbatim from GitHub Search API, parent-verified 2026-10-12 via direct re-parse of `gsearch9.json`): *"Tamper-evident append-only SHA-256 provenance and audit ledger for autonomous agents."* Topics (verbatim, parent-verified, 8 topics): **`ai, audit-ledger, autonomous-agents, cryptography, merkle-tree, provenance, rust, sha256`** = **the unique SHA-256 (vs ed25519) v2-AI audit-ledger primitive of the 74-pass series**. Bucket: **v2-AI (SHA-256-provenance-audit-ledger-vocabulary)** — Pick C of Daily Research 2026-10-12. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`tamper-evident + append-only + SHA-256 + provenance + audit-ledger + autonomous-agents`** sextuple-primitive as a persistent cross-section reference for the LE31 v2-AI *SHA-256-provenance-audit-ledger-for-autonomous-agents* wedge, and document the **SHA-256-vs-ed25519-primitive** validation that an independent maintainer arrived at in 2026 without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`tamper-evident + append-only + SHA-256 + provenance + audit-ledger + autonomous-agents`** sextuple-primitive: the *tamper-evident* is the *cryptographic-tamper-evidence* primitive (any modification to a record is detectable via the cryptographic hash); the *append-only* is the *append-only-ledger* primitive (records are never modified once written); the *SHA-256* is the *SHA-256-cryptographic-hash-algorithm* primitive (vs the more common *ed25519* used in sister-shape audit-ledger repos); the *provenance* is the *provenance* primitive (records where the data came from); the *audit-ledger* is the *audit-ledger* primitive (a ledger of audit events); the *autonomous-agents* is the *autonomous-agents* primitive (agents that act without human-in-the-loop). The *SHA-256* primitive is the **unique SHA-256 (vs ed25519) v2-AI audit-ledger primitive of the 74-pass series**; sister-shape `Bastardki11er/tally` + `warrant-ai/warrant` + `farooqarahim/glassbox` + `A220man/human-approval-console-ryan-vo` + `DSHCorrectover/agent-second-fuse` all use *ed25519* (or *Ed25519+ML-DSA-65*); sister-shape `chenhz01/model-origin-ledger` uses SHA-256 but the framing is *model-and-dataset-provenance* not *autonomous-agents*.
- A written record of the **`autonomous-agents`** primitive: the *autonomous-agents* framing is the *AI-agent* framing applied to the *autonomous* agent-class claim. The *autonomous* claim is stronger than the sister-shape *ai-agents* claim because *autonomous* implies the agent acts without human-in-the-loop, while *ai-agents* can include human-gated agents. This is the §3.4 *non-AI-fallback + human-gate* charter invariant applied to the *AI-agent-class* dimension, where the *autonomous* claim is the *agent-without-human-gate* framing.
- A written record of the **`merkle-tree + cryptography + provenance + audit-ledger + ai`** 5-dimensional sub-primitive: the *merkle-tree* is the *merkle-tree* primitive (enables efficient proofs of inclusion); the *cryptography* is the *cryptography* discipline; the *provenance* is the *provenance* primitive; the *audit-ledger* is the *audit-ledger* primitive; the *ai* is the *ai* primitive. Sister-shape to features 187+188+232+287-289+299-304 (the persistent v2-AI audit-trail vocabulary cluster).
- A decision record: today's verdict is `defer` because (1) LE31 v1 has no v2-AI surface requirement; (2) the *SHA-256-provenance-audit-ledger-vocabulary* is the value, not the code (the 39 KB tiny + 0★/1⑂ is the 2nd-smallest v2-AI pick of the 74-pass series, but the *SHA-256-vs-ed25519* primitive difference is the §3.1 *content-addressed-storage* primitive applied with a specific cryptographic-hash-algorithm); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema (the §3.1 *append-only-ledger* primitive is already implemented; the *SHA-256-provenance* extension is OFF the v1 charter).
- Adoption of the Perseus-Computing-LLC/argus codebase (0★/1⑂ with 39 KB tiny; the 0★/1⑂ is a low community-traction signal; the 39 KB tiny size is the 2nd-smallest v2-AI pick of the 74-pass series; the *SHA-256* primitive is the value, not the code-adoption opportunity).
- Cross-pollination with the v2-AI SHA-256-provenance primitive in v1 (LE31 v1 has no v2-AI surface).
- Cross-pollination with the v2-AI autonomous-agents primitive in v1 (LE31 v1 has no AI agent; the *autonomous-agents* framing is OFF the v1 charter).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "the SHA-256-provenance + audit-ledger for autonomous-agents primitive" (e.g., a v2 surface that introduces an AI-assisted owner-side workflow like "the autonomous AI agent proposes a supplier reorder; the proposal is recorded in the SHA-256-provenance + audit-ledger; the operator reviews the audit trail; the operator confirms or rejects the proposal"), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "tamper-evident + append-only + SHA-256 + provenance + audit-ledger + autonomous-agents" is a real demand signal*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same SHA-256 (vs ed25519) + autonomous-agents framing"*.

- **Evidence class**: observed (the description names the 6-primitive set explicitly: `tamper-evident + append-only + SHA-256 + provenance + audit-ledger + autonomous-agents`).
- **Confidence**: medium for the vocabulary match (the verbatim description names the 6-primitive set); low for transferability (LE31 v1 has no v2-AI surface; the 39 KB tiny repo is the 2nd-smallest v2-AI pick of the 74-pass series; the 0★/1⑂ is a low community-traction signal).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no AI agent); the value is the *SHA-256-provenance-audit-ledger-vocabulary* — when the first v2 PR that adds a v2-AI surface with SHA-256-provenance semantics lands, the Perseus-Computing-LLC/argus pattern is a ready-made *named primitive*.

## Description

GitHub `Perseus-Computing-LLC/argus` (MIT, 0★/1⑂, Python, pushed 2026-10-12T01:44:49Z = TODAY, 39 KB tiny). Description (verbatim, parent-verified GitHub Search API re-parse 2026-10-12): *"Tamper-evident append-only SHA-256 provenance and audit ledger for autonomous agents."* Topics (verbatim, parent-verified GitHub Search API, 8 topics): **`ai, audit-ledger, autonomous-agents, cryptography, merkle-tree, provenance, rust, sha256`**.

The architectural primitive has 4 sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **`Tamper-evident + append-only + SHA-256`** — the cryptographic-tamper-evidence surface. The *tamper-evident* means any modification to a record is detectable via the cryptographic hash; the *append-only* means records are never modified once written; the *SHA-256* is the specific cryptographic-hash-algorithm (vs the more common *ed25519* in sister-shape audit-ledger repos). The *SHA-256* primitive is the **unique SHA-256 (vs ed25519) v2-AI audit-ledger primitive of the 74-pass series**.
2. **`Provenance + audit-ledger`** — the audit-trail-vocabulary surface. The *provenance* means records include where the data came from; the *audit-ledger* means a ledger of audit events. The *provenance + audit-ledger* double-primitive maps 1:1 onto any future v2-AI surface that requires a cryptographic-attestation layer.
3. **`Merkle-tree + cryptography`** — the cryptographic-verifiability surface. The *merkle-tree* enables efficient proofs of inclusion; the *cryptography* is the cryptography discipline. The *merkle-tree + cryptography* double-primitive maps 1:1 onto any future v2-AI surface that requires efficient proofs of inclusion + cryptographic-verifiability.
4. **`Autonomous-agents + ai`** — the AI-agent-class surface. The *autonomous-agents* is the *AI-agent* framing applied to the *autonomous* agent-class claim (agent acts without human-in-the-loop); the *ai* is the *ai* discipline. The *autonomous-agents* framing is the **unique autonomous-agents (vs ai-agents) v2-AI audit-ledger primitive of the 74-pass series** (sister-shape repos use *ai-agents* but the *autonomous* claim is a stronger agent-class claim).

**The 1:1 mapping onto LE31 surface:**

| Perseus-Computing-LLC/argus primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Tamper-evident + append-only | `audit_logs` schema (append-only atomic) | §3.1 ✓ | **Implemented (v1, partial)** |
| SHA-256 (vs ed25519) | (LE31 v1 uses UUIDs, not SHA-256; the SHA-256 primitive is a v2 extension) | §3.1 | **Not implemented (v2-AI surface)** |
| Provenance | (LE31 v1 has no provenance; the *provenance* primitive is a v2 extension) | §3.1 + v2-AI | **Not implemented (v2-AI surface)** |
| Audit-ledger | (LE31 v1 has no dedicated audit-ledger; the *audit-ledger* discipline is a v2 extension) | §3.1 + v2-AI | **Not implemented (v2-AI surface)** |
| Merkle-tree | (LE31 v1 has no merkle-tree; the *merkle-tree* discipline is a v2-AI extension) | v2-AI | **Not implemented (v2-AI surface)** |
| Cryptography | (LE31 v1 has no cryptographic-signature; the *cryptography* discipline is a v2-AI extension) | v2-AI | **Not implemented (v2-AI surface)** |
| Autonomous-agents | (LE31 v1 has no AI agent) | §3.4 + v2-AI | **Not implemented (v2-AI surface)** |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface that requires SHA-256-provenance + audit-ledger for autonomous-agents), the implementation would add:

1. A `content_hash` column on the existing `audit_logs` table (Alembic migration) for v2-AI SHA-256 content-addressing (a str column that stores the SHA-256 content hash of the audit-log payload, unique per audit-log row).
2. A `provenance` column on the existing `audit_logs` table (Alembic migration) for v2-AI provenance tracking (a str column that records where the audit-log payload came from, e.g., the agent-id + action-id + upstream-source).
3. A new `AutonomousAgentAudit` table (Alembic migration) with columns: `id` (UUID), `agent_id` (str), `action_id` (str), `proposed_action` (str), `proposed_by` (str agent-id), `content_hash` (str SHA-256), `merkle_root` (str SHA-256 merkle-tree-root), `recorded_at` (timezone-aware datetime), `confirmed_by` (str nullable operator-id), `confirmed_at` (timezone-aware datetime nullable), `rejected_reason` (str nullable).
4. A new `MerkleProof` table (Alembic migration) with columns: `id` (UUID), `audit_id` (UUID FK to `AutonomousAgentAudit`), `proof_path` (JSON list of SHA-256 hashes), `leaf_hash` (str SHA-256), `root_hash` (str SHA-256 merkle-tree-root), `verified_at` (timezone-aware datetime nullable).
5. A `GET /v2/autonomous-agent-audit?agent=<>&action=<>&as_of=<>` search endpoint.
6. A `POST /v2/autonomous-agent-audit/record` FastAPI endpoint that records an autonomous-agent audit (charter §3.1 *explicit-state-transition* primitive applied to autonomous-agent-audit).
7. A `GET /v2/autonomous-agent-audit/{audit_id}/merkle-proof` endpoint that returns the merkle-proof for a given audit (enables efficient proof of inclusion).
8. A `POST /v2/autonomous-agent-audit/{audit_id}/confirm` endpoint that confirms a proposed action (charter §3.4 *human-gate* invariant — autonomous-agents must be confirmed by an operator before action execution).

The HANDOFF is to evaluate whether the v2-AI surface is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

## Telegram interaction

**No new Telegram interaction today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface with SHA-256-provenance + audit-ledger for autonomous-agents), the implementation would add a single Telegram message type:

- `autonomous_agent_audit_request` (sent to the owner): *"Autonomous agent {agent_id} proposes: {proposed_action}. Content hash: {content_hash}. Merkle root: {merkle_root}. Reply /confirm to approve, /reject to discard, /merkle-proof to verify the cryptographic proof."* The owner confirms or rejects via Telegram inline keyboard. The confirmation is logged in the `AutonomousAgentAudit` table with `confirmed_by = owner_telegram_id` + `confirmed_at = now()`.

## Dependencies

- **Existing LE31 v1 primitives** (no change): `audit_logs` schema (append-only atomic) + `StockEntry` schema (append-only atomic). Both are already implemented in LE31 v1.
- **No new dependencies** are required for the defer artifact.
- **Future v2-AI surface** (if trigger fires): would require the `content_hash` column + `provenance` column on `audit_logs` (Alembic migration) + new `AutonomousAgentAudit` table + new `MerkleProof` table + 4 new FastAPI endpoints. The aiogram v3 bot would require 1 new handler type (`autonomous_agent_audit_request`). The Python `hashlib` standard library provides SHA-256 (no new dependency).

## Open questions

- **Will the future v2-AI surface ever need a SHA-256-provenance + audit-ledger for autonomous-agents?** The LE31 v1 `audit_logs` schema is already an append-only ledger. The *SHA-256-provenance + audit-ledger for autonomous-agents* discipline is an extension that adds cryptographic-attestation + provenance-tracking + merkle-tree-efficient-proofs. Sister-shape to features 187+188+232+287-289+299-304 (the persistent v2-AI audit-trail vocabulary cluster) but with the unique *SHA-256 (vs ed25519) + autonomous-agents (vs ai-agents)* framing.
- **Is the SHA-256 primitive meaningfully different from ed25519 for LE31's purposes?** The SHA-256 is a cryptographic-hash-algorithm; the ed25519 is a cryptographic-signature-algorithm. They serve different purposes: SHA-256 produces a content hash; ed25519 produces a signature. Sister-shape repos use ed25519 because ed25519 includes both a hash and a signature; Perseus-Computing-LLC/argus uses SHA-256 because it focuses on content-addressing (not signing). The two primitives are not mutually exclusive (a record can be SHA-256-content-addressed AND ed25519-signed).
- **Is the autonomous-agents framing aligned with LE31's v1 charter?** The LE31 v1 charter has a hard invariant: *"No customer-facing AI. AI may assist owner/staff, with observable evidence and a non-AI fallback."* (charter §3.4). The *autonomous-agents* framing is the *AI-without-human-gate* framing, which would violate the *non-AI-fallback + human-gate* invariant IF the autonomous-agent acts on a customer-facing surface. The v2-AI surface would need to be carefully scoped to *owner/staff-assist only* to maintain the charter invariant.

## Why this matters

The **`tamper-evident + append-only + SHA-256 + provenance + audit-ledger + autonomous-agents`** sextuple-primitive is the **canonical v2-AI SHA-256-provenance-audit-ledger-vocabulary** of the 74-pass series. The *SHA-256* (vs ed25519 in sister-shapes) is the **unique SHA-256 (vs ed25519) v2-AI audit-ledger primitive of the 74-pass series**. The *autonomous-agents* (vs ai-agents in sister-shapes) is the **unique autonomous-agents (vs ai-agents) v2-AI audit-ledger primitive of the 74-pass series**.

When the first v2 PR that adds a v2-AI surface with SHA-256-provenance + audit-ledger for autonomous-agents lands, the Perseus-Computing-LLC/argus pattern is a ready-made *named primitive* for the *SHA-256 (vs ed25519) + autonomous-agents (vs ai-agents) + tamper-evident + provenance + merkle-tree* vocabulary. The defer artifact is a parking-lot reference, not a build candidate.
