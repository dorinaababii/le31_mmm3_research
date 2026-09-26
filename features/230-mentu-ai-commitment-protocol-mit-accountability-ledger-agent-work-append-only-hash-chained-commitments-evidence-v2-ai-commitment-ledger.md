# Feature 230 — mentu-ai-commitment-protocol-mit-accountability-ledger-agent-work-append-only-hash-chained-commitments-evidence-v2-ai-commitment-ledger (defer)

> **NEW observation (2026-09-26).** Documents in-window GitHub Search `append-only+ledger` query result: `mentu-ai/commitment-protocol` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **10★/4⑂ = highest-star-count in-window candidate of the 57-pass daily-research series**; 10× the star count of feature 187's `traust-security/traust-ledger` 2★; 7× the star count of feature 197's `rajo69/ledgerkb` 7★ HTTP 404 today; parent-direct-GET confirms; subagent missed this candidate), Python, **pushed 2026-09-24T02:48:39Z** (in-window by `pushed_at` only — *2 days before fetch time*), **created 2025-12-31T16:00:00Z** (~9-month-old repo with in-window `pushed_at`; **IN-WINDOW BY PUSH ONLY**; `created_at` is OUT-OF-WINDOW by ~9 months), **108 KB** modest repo, `default_branch=main`, archived=`False`). **8 topics** (verbatim from raw JSON): `accountability`, `agents`, `commitment`, `evidence`, `ledger`, `open-source`, `protocol`, `specification`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-26): *"The Commitment Protocol: an accountability ledger for agent work. Append-only and hash-chained; commitments close against evidence. Specification, agent template, sample ledger and reference verifier."* The **commitment-ledger + hash-chained + commitments-close-against-evidence + accountability + agent-work** quintuple-primitive + the *accountability ledger for agent work* discipline = the **strongest single v2-AI append-only commitment-ledger vocabulary of the 57-pass series**. Bucket: **v2-AI append-only commitment-ledger (parking-lot, future-v2-AI-surface-vocabulary-reference)** — watch-list entry, zero build time today.

## Goal

Retain the **commitment-ledger + hash-chained + commitments-close-against-evidence + accountability + agent-work** quintuple-primitive as a persistent cross-section reference for any future LE31 v2-AI surface that introduces an AI-assisted workflow with (a) **commitments** (the AI makes a promise to do something), (b) **evidence** (the proof that the commitment was honored), and (c) **append-only ledger + hash-chained** (the audit trail that ties the commitment to the evidence). The artifact is the persistent cross-section reference + the 8 named topics + the verbatim description. No code today (MIT license permits future code reuse; vocabulary-only artifact today; 108 KB modest-repo size is comfortably readable).

## Scope

**In scope (defer artifact):**
- A written record of the **commitment-ledger** discipline: the *agent-work-commitment-disposition* primitive (LE31 v1 today has `audit_logs` for state transitions but no notion of an explicit *commitment* that is opened and closed against evidence; the *commitment-ledger* discipline IS the *commit-then-close-against-evidence* posture applied to charter §3.1's *explicit-state-transition* discipline).
- A written record of the **hash-chained** discipline: the *commitment-hash-chain* primitive (each commitment is hash-linked to the previous commitment + the previous commitment's evidence; this is the *append-only-ledger-with-cryptographic-linkage* posture; LE31 v1's `audit_logs` is append-only but does NOT hash-chain — the *hash-chain* addition is a v2-AI vocabulary reference).
- A written record of the **commitments-close-against-evidence** discipline: the *commitment-evidence-tie* primitive (every commitment must be paired with the evidence that proves it was honored; this is the *evidence-tied-commitment* posture; charter §3.4's *observable-evidence* requirement is operationalized by this primitive).
- A written record of the **accountability + agent-work** discipline: the *agent-accountability* primitive (the commitment-ledger is specifically designed for AI agents, not for human operators; the *agent-accountability* discipline IS the *AI-system-observable-evidence* posture per charter §3.4).
- A decision record: today's verdict is `defer` because LE31 v1 has no AI surface at all (charter §3.4 explicit invariant); the cross-section reference is informative, not a v2-AI build-trigger.
- A cross-section reference with the prior v2-AI append-only-ledger + audit-log cluster: features 121 (`ledger-commitment-field-tier-minimization`), 122 (`trace-integrity-cait-acceptance-criterion`), 129 (`ledger-claim-to-evidence-trace-graph-audit`), 160 (`factgraph` Apache-2.0 carry-over), 173 (`consortium-blockchain-audit-sharing-kenfra-fraud-intelligence`), 183 (`n0-public` MIT 0★ carry-over), 187 (`traust-ledger` Apache-2.0 2★/5⑂ carry-over), 197 (`ledgerkb` Apache-2.0 7★ HTTP 404 = 6th consecutive day), 198 (`arbiter` MIT 0★), 199 (`transparency-kit` NOASSERTION 0★), 212 (`Hardtack` MIT 0★ carry-over from 09-22), 219 (`epcore` MIT 0★ carry-over from 09-23), 220 (`commit-replay-bench` Apache-2.0 0★ carry-over from 09-23). The *transferable insight* is the **commitment-ledger + hash-chained + commitments-close-against-evidence + accountability + agent-work** quintuple-primitive.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2 horizontal-expansion surface in v2 (charter §3.1 + §3.2 invariant: v2 surface expansion is the next boundary; this is a vocabulary reference, not a v2 expansion trigger).
- Any v2-AI commitment-ledger implementation in v2 (the artifact is vocabulary-only; the implementation would require explicit owner/charter sign-off).
- Any hash-chain cryptographic primitive in v1 (LE31 v1's `audit_logs` is append-only but does NOT hash-chain; the *hash-chain* vocabulary is a v2-AI future reference).

## Description

The pick is **`mentu-ai/commitment-protocol`** — a Python + MIT + append-only + hash-chained + accountability-ledger for agent work, with commitments that close against evidence. Charter §3.4 NOT triggered because the artifact is operator-tooling-AI (the ledger records AI agent commitments and the evidence they closed against), NOT customer-facing-AI (no restaurant diner interacts with the commitment-ledger; the diner interacts with the operator who uses the AI). The *commitment-ledger* is a tool for the *operator/owner* who supervises the AI; charter §3.4 is satisfied because the AI runs in the *operator-tooling layer* (per charter §3.4 *"AI may assist owner/staff, with observable evidence and a non-AI fallback"*). The artifact is the persistent cross-section reference for the 8 named topics + the verbatim description.

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v2-AI surface that adopts the *commitment-ledger* primitive would extend the LE31 v1 data model with appropriate new tables (e.g., a `commitment` table with `commitment_id, agent_id, opened_at, closed_at, evidence_id, hash_chain_link`; a `commitment_evidence` table with `evidence_id, commitment_id, evidence_type, evidence_payload, evidence_hash, recorded_at`; a `commitment_hash_chain` table with `link_id, prev_link_hash, current_commitments_root_hash, recorded_at`). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v2-AI PR is triggered by the trigger condition below, the implementation would:
1. Read the `mentu-ai/commitment-protocol` README at https://github.com/mentu-ai/commitment-protocol for the *commitment-ledger + hash-chained + commitments-close-against-evidence + accountability + agent-work* quintuple-primitive.
2. Cross-reference with LE31 v1's `audit_logs` schema to identify the *delta* (the *delta* = `mentu-ai/commitment-protocol` introduces commitment-disposition + hash-chain + evidence-tie primitives that LE31 v1's `audit_logs` does not have; LE31 v1's `audit_logs` is append-only but does NOT hash-chain and does NOT have explicit *commitment* records).
3. Apply charter §3.4 *operator-tooling-AI with observable evidence + non-AI fallback* review to the *delta* (any new v2-AI surface requires explicit owner/charter sign-off; the *commitment-ledger* surface is operator-tooling-AI which is charter §3.4-compatible provided the non-AI fallback is preserved — i.e., the operator can view and approve every commitment without using the AI to interpret it).
4. Implement the surface with the LE31 v1 + FastAPI + SQLModel + aiogram stack; the `mentu-ai/commitment-protocol` reference is the *vocabulary* for *commitment-ledger + hash-chained + commitments-close-against-evidence*, NOT for *commitment-ledger replacement*.

## Telegram interaction

Zero new Telegram interaction today. Future v2-AI PR that adopts the *commitment-ledger* primitive would extend the existing aiogram-bot (cook-bot per charter §3.1) with a *commitment-status* command set that allows the operator to query commitment status (e.g., `/commitment status` → list of open commitments; `/commitment close <commitment_id> <evidence>` → close a commitment with evidence). The *commitment-status* discipline is *operator-tooling* (operator queries the commitment status), NOT customer-facing-AI; charter §3.4 is NOT triggered.

## Dependencies

- LE31 charter §3.1 surface-expansion review (for any v2 surface adoption).
- LE31 charter §3.2 surface-expansion review (for any v2-AI surface adoption).
- LE31 charter §3.4 operator-tooling-AI-with-observable-evidence boundary (for any commitment-ledger adoption; the *commitment-ledger* posture is operator-tooling-AI which is charter §3.4-compatible provided the non-AI fallback is preserved).
- LE31 charter §3.2 license-compatible (MIT permissive; future code adoption is possible).
- Features 121 (`ledger-commitment-field-tier-minimization`), 122 (`trace-integrity-cait-acceptance-criterion`), 129 (`ledger-claim-to-evidence-trace-graph-audit`), 160 (`factgraph`), 173 (`consortium-blockchain-audit-sharing-kenya-fraud-intelligence`), 183 (`n0-public`), 187 (`traust-ledger`), 197 (`ledgerkb`), 198 (`arbiter`), 199 (`transparency-kit`), 212 (`Hardtack`), 219 (`epcore`), 220 (`commit-replay-bench`).
- Cross-section reference `mentu-ai/commitment-protocol` at https://github.com/mentu-ai/commitment-protocol (MIT, 10★/4⑂, Python, append-only + hash-chained + commitments-close-against-evidence + accountability + agent-work).

## Open questions

- Will LE31 v2-AI ever introduce a commitment-ledger surface? If yes, `mentu-ai/commitment-protocol` is the vocabulary reference.
- Will LE31 v2-AI ever introduce a hash-chained audit log? If yes, `mentu-ai/commitment-protocol` is the vocabulary reference (note: LE31 v1's `audit_logs` is append-only but does NOT hash-chain; the hash-chain addition is a v2-AI future reference).
- Will LE31 v2-AI ever introduce explicit *commitment* records (vs the current `audit_logs` which records *state transitions* but not *commitments*)? If yes, `mentu-ai/commitment-protocol` is the vocabulary reference.
- Will LE31 v2-AI ever introduce an evidence-tie primitive (every commitment paired with the evidence that proves it was honored)? If yes, `mentu-ai/commitment-protocol` is the vocabulary reference.
- Will LE31 v2-AI ever introduce an agent-accountability primitive (the ledger is specifically designed for AI agents, not for human operators)? If yes, `mentu-ai/commitment-protocol` is the vocabulary reference.
- The 10★/4⑂ is explicitly NOT offered as evidence of *LE31 needing a commitment-ledger*; the 10★/4⑂ is for the *commitment-ledger domain*, not for the *LE31 operational* primitive. The transferable item is the *technique* (commitment + hash-chain + evidence-tie), not the *commitment-ledger* itself.
- **Open question that may kill any future PR**: who would ever run the offline verifier of a commitment-ledger? LE31 has exactly one stakeholder (the owner) who can just ask the AI what it did. The *commitment-ledger* may be over-engineering for a single-tenant single-operator scenario.

## Why this matters

The 8 topics + the verbatim description in `mentu-ai/commitment-protocol` are the **canonical v2-AI commitment-ledger vocabulary** that LE31 v1's `audit_logs` (feature/charter §3.1) and v2-AI's future commitment-tracking surface would inherit. Specifically: (i) **commitment** (the *commitment-disposition* primitive) is the *commit-then-close-against-evidence* posture; (ii) **hash-chained** (the *commitment-hash-chain* primitive) is the *append-only-ledger-with-cryptographic-linkage* posture; (iii) **commitments-close-against-evidence** (the *commitment-evidence-tie* primitive) is the *evidence-tied-commitment* posture per charter §3.4; (iv) **accountability** (the *agent-accountability* primitive) is the *AI-system-observable-evidence* posture; (v) **agent-work** (the *agent-work-discipline* primitive) is the *AI-assisted-operator-work* posture. When v2-AI introduces any of these 5 primitives, `mentu-ai/commitment-protocol` is the vocabulary reference. **HONEST DISCLOSURE**: `mentu-ai/commitment-protocol`'s 10★/4⑂ is for the *commitment-ledger domain*, not for the *LE31 operational* primitive; the 10★/4⑂ is explicitly NOT offered as evidence of LE31's need for the commitment-ledger.