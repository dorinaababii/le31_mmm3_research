# Feature 181 — `merkle-audit-tamper-evident-root-hash-batching`

**Bucket:** v2 owner-pains architecture-reference (defer, parking-lot)
**Filed:** 2026-09-15 by the LE31 daily-research cron
**Source:** Daily Research 2026-09-15, Pick C
**Gate:** PASS (v2 architecture-reference; defer; parking-lot)

## Goal

Document the **off-chain-batch + on-chain-root-hash-anchor + privacy-preserving-inclusion-proof + role-based-submission-allow-list** primitives formalised in *Merkle Audit: A Merkle Tree-Based Blockchain Framework for Tamper-Evident Audit Logging in Digital Record Systems* (DOI `10.64643/ijirt.208359-459`, 2026-09-11, IJIRT peer-reviewed, by Rashi Vakhare + Sakshi Chavan) as the **v2-hardening vocabulary** for any future LE31 surface that needs to prove `audit_logs` chain integrity to an external stakeholder (tax authority, accountant, second restaurant) without leaking the underlying data.

## Scope

1. **This is a vocabulary-only pick.** No code, no library, no new dependency.
2. **Three transferable primitives** are documented below; each maps to a future LE31 v2 surface:
   - **Off-chain-batching** → batch N `audit_logs` mutations into a Merkle tree, commit only the root hash.
   - **Inclusion proof without DB access** → prove one row is in the log set without disclosing the full log.
   - **Role-based submission allow-list** → restrict log submission to authorized writers, combine public-verifiability with access control.
3. The paper's **measured 99.97% gas-cost saving** (across batch sizes 10–5,000) is the *cost-shape data point* that says the off-chain-batching pattern is **practical for high-throughput logging**, not academic-only.
4. Charter §3.1 explicit-state-transitions compatible (the append-only ledger invariant is preserved; the Merkle tree is a *commitment structure* sitting on top of the existing audit log, not a replacement).
5. Charter §3.2 not triggered (academic-paper license = idea-portability, not code-portability).
6. Charter §3.4 not triggered (no AI integration in the paper or in the proposed LE31 surface).

## Out of scope

1. Any code adoption from the Merkle Audit paper's Ethereum Sepolia prototype. The paper does not publish source code; the primitives are *idea-portable*, not code-portable.
2. Any v1 LE31 surface. The pick is explicitly **defer** because no v1 owner demand exists; the v2 triggers are listed in Open questions.
3. Any AI integration. Charter §3.4 not triggered.
4. Any change to the existing `audit_logs` table schema or the `StockEntry` invariant. The Merkle tree sits **on top of** the existing audit log; the underlying storage does not change.
5. Any change to LE31's choice of ledger substrate. LE31 uses PostgreSQL as the source of truth; the Merkle tree is a *commitment layer* above it, not a replacement.

## Description

**Source paper:** Vakhare, R. & Chavan, S. (2026-09-11). *Merkle Audit: A Merkle Tree-Based Blockchain Framework for Tamper-Evident Audit Logging in Digital Record Systems.* International Journal of Innovative Research in Technology. DOI `10.64643/ijirt.208359-459`. 0 citations at filing time; IJIRT is a peer-reviewed journal.

**Abstract (reconstructed by parent from OpenAlex `abstract_inverted_index`, since the paper is paywalled at IJIRT and the abstract was not available in the raw JSON):**

> *"In digital record-keeping systems, ensuring the integrity and authenticity of audit logs is critical for regulatory compliance, security assurance, and post-incident forensic analysis. Conventional centralized logging architectures remain vulnerable to tampering by insiders with administrative access and constitute single points of failure: an adversary who compromises the log store, or an operator who abuses legitimate access, can retroactively rewrite the historical record without leaving evidence of the change. Blockchain technology offers a compelling countermeasure, since data committed to a well-secured blockchain is computationally infeasible to alter retroactively. However, anchoring every individual log entry on-chain introduces prohibitive latency, storage overhead, and transaction cost, limiting its practicality for high-throughput logging environments such as enterprise transaction systems, hospital record systems, or academic record-keeping platforms. This paper presents MerkleAudit, a hybrid logging framework that combines Merkle tree-based authenticated data structures with blockchain anchoring to address these limitations. MerkleAudit batches log entries off-chain into Merkle trees and commits only the resulting root hash to the blockchain, decoupling log-ingestion throughput from on-chain transaction frequency and substantially improving scalability while preserving tamper-evidence. The framework further supports efficient, privacy-preserving inclusion proofs that allow verification of a single log entry without disclosing the full log set or requiring direct database access, and restricts log submission to an authorized, role-based allow-list, combining the auditability of public verification with the access control of a permissioned system. We implemented and evaluated a prototype of MerkleAudit on the Ethereum Sepolia test network, demonstrating that it can process high volumes of log entries with minimal on-chain storage footprint, rapid proof verification, and reliable detection of tampering, deletion, and forgery attempts. A gas-cost benchmark across batch sizes from 10 to 5,000 entries shows savings of up to 99.97% relative to a naive per-entry logging baseline, while a 25-test adversarial suite and an independent static-analysis pass confirm that no exploitable vulnerabilities were introduced by the batching design. MerkleAudit thus offers a practical, cost-efficient, and privacy-preserving approach to verifiable audit logging for security-critical digital record systems."*

**Three transferable primitives:**

### Primitive 1: Off-chain-batching with root-hash-anchor

The paper's core insight is that you do **not** need to put every log entry on-chain. You batch N log entries into a Merkle tree and commit only the **root hash** to the blockchain. The cost savings scale with N: for N=5,000 entries, the gas cost is **0.03%** of a naive per-entry baseline.

**LE31 analogue:** `audit_logs` is the single source of truth (PostgreSQL table). When LE31 v2 introduces an external-auditor surface (e.g., for a tax filing), the auditor should be able to ask "give me the proof that `audit_logs` row R was committed at time T" — and the answer should be a Merkle inclusion proof derived from a batch-root-hash that was committed to a verification layer at time T, not a direct query against the audit log table.

### Primitive 2: Privacy-preserving inclusion proof

The paper shows how to prove **one specific row is in the log set** without disclosing the full log set or requiring direct database access. The proof is a logarithmic-size Merkle path (sibling hashes from the leaf to the root).

**LE31 analogue:** A tax auditor or accountant should be able to verify "the `audit_logs` entry I am asking about exists in the chain at time T" without needing read access to the LE31 database. This is exactly the question that v2 owner-facing audit-export will need to answer.

### Primitive 3: Role-based submission allow-list

The paper restricts **log submission** to an authorized, role-based allow-list. This combines the **public-verifiability** of the chain (anyone can verify) with the **access control** of a permissioned system (only authorized writers can submit).

**LE31 analogue:** When an accountant or tax-authority auditor becomes a second principal (v2 surface), the audit log submission should remain restricted to LE31-internal writers (the Telegram bot, the htmx owner surface, the nightly batch jobs) — the external auditor is a **reader**, not a writer. The allow-list enforces this without requiring a separate permission system.

## Data model

**No v1 data model change.** This is a v2 architecture-reference.

If a future v2 surface implements these primitives (see Open questions for triggers), the data model addition would be:
- A `merkle_batches` table that records `{batch_id, root_hash, parent_root_hash, batch_start_time, batch_end_time, commit_timestamp, verification_layer_ref}`.
- A `merkle_inclusion_proofs` table (or computed on-demand) that returns the sibling-hash path from any `audit_logs.row_id` to the corresponding `merkle_batches.root_hash`.

The existing `audit_logs` table is **unchanged** — the Merkle tree is a *commitment layer* above it.

## Implementation

**No implementation today.** This is a vocabulary-only defer pick.

If/when a v2 surface triggers (see Open questions), the implementation would be:
1. Add the `merkle_batches` table + migration (Alembic).
2. Implement a nightly batch job that reads the day's `audit_logs` rows, builds a Merkle tree, commits the root hash to a verification layer (could be a private-sidechain, an EU regulatory timestamping service, or a managed cloud WORM storage — owner decision).
3. Implement the inclusion-proof function: given a `row_id`, return the sibling-hash path to the batch root.
4. Implement the role-based submission allow-list: any non-allow-listed writer is rejected at the audit_logs INSERT trigger.
5. Add a v2 surface (e.g., `/audit-proof/<row_id>` for an accountant-facing endpoint) that returns the inclusion proof.

## Telegram interaction

None for v1. The v2 surface (if implemented) would be an accountant/tax-authority-facing endpoint, not a Telegram-bot surface.

## Dependencies

**No v1 dependencies.** This is a vocabulary-only pick.

If/when a v2 surface triggers, the dependencies would be:
1. **A Merkle tree library** (Python: `pymerkle`, `merkletools`, or a hand-rolled SHA-256 implementation — confirm via `le31-conventions` for the LE31 preference).
2. **A verification layer** (owner decision: private-sidechain, EU regulatory timestamping service, managed cloud WORM storage).
3. **The existing LE31 `audit_logs` and `StockEntry` primitives** — no new domain logic.

## Open questions

1. **What v2 surface would justify the engineering effort?** Triggers, in priority order:
   - (a) v2 introduces an **owner-facing audit-export** surface (e.g., a monthly CSV export of `audit_logs` to the owner for offline verification).
   - (b) v2 introduces an **accountant-facing audit-verification** surface (e.g., an accountant can query "was this row committed before tax filing?").
   - (c) v2 introduces a **second stakeholder** (e.g., a tax authority, a regulator, a second restaurant sharing stock data).
   - (d) v2 introduces a **v2-AI surface that consults `audit_logs`** (e.g., an AI assistant that summarizes the day's operations — feature 122's Trace Integrity CAIT becomes the gate).

None of these triggers are present in v1 today. The pick is parked until one fires.

2. **LE31 owner decision: which verification layer?** The paper uses Ethereum Sepolia (public testnet), but the LE31 analogue should use a **permissioned verification layer** because LE31's audit log is single-restaurant and the owner is the only stakeholder (no public verifiability needed). Options:
   - A managed cloud WORM storage (AWS S3 Object Lock, Azure Blob Immutable Storage, Google Cloud Storage Bucket Lock).
   - A private-sidechain (e.g., Hyperledger Fabric, Quorum).
   - An EU regulatory timestamping service (e.g., the EU Commission's qualified timestamping service, if it exists).

   This is an owner decision; the pick is parked until the owner weighs in.

3. **Does the Merkle tree conflict with the existing append-only `StockEntry` invariant?** No — the Merkle tree is *derived* from the audit log; the audit log remains the source of truth; the Merkle tree is a commitment structure that can be reconstructed from the audit log at any time. The two are complementary, not conflicting.

4. **Does the role-based submission allow-list conflict with the existing `audit_logs` writer model?** No — the existing writers (the Telegram bot, the htmx owner surface, the nightly batch jobs) ARE the allow-list; the role-based submission allow-list formalises the existing implicit discipline.

## Why this matters

This pick completes the **v2-hardening story for LE31's audit log** alongside features 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 129 (LEDGER Claim-to-Evidence Trace Graph), 133 (HANSARD Runtime Witnessing), 134 (ECHO Record-Shape), 135 (DreamLedger), 137 (NL-to-Executable-Obligations), 141 (KRINEIA), 167 (provtrail), 168 (asset-ledger), 169 (openshare-ledger). Each of these features contributes a *different* primitive to the audit-trail hardening story:

- **121** = what is committed (the disclosure surface)
- **122** = what is queried (the acceptance surface)
- **129** = explanation-time traceability
- **133** = who acted (runtime witnessing)
- **134** = record-shape (structured vs. unstructured)
- **135** = signal-reliability (consult-before-use)
- **137** = policy compilation (NL rules → typed obligations)
- **141** = invariants under mutation
- **167** = source-provenance for LLM-assisted workflows
- **168** = content-addressed media lineage
- **169** = decentralized replayability
- **181 (this pick)** = **commitment-layer primitives (off-chain-batching + inclusion-proof + role-based-allow-list)**

The 181 pick is the **most concrete** of the v2-hardening cluster: it is the *only* paper in the cluster that includes a **measured performance number** (99.97% gas-cost saving) and an **adversarial-test suite** (25 tests + static-analysis pass) that demonstrates the primitives are **practical for high-throughput logging**, not academic-only. The 181 pick is therefore the *most likely* to be referenced when LE31 v2 actually implements an external-auditor surface.

The pick is **fully reversible** (vocabulary-only artifact) and **does not trigger any v1 work** per `le31-daily-research/SKILL.md` hard rules. It is explicitly **not** a recommendation to start any v2-AI work; the §3.4 no-customer-facing-AI charter provision remains in force, and the 181 pick is **compliant with §3.4** (no AI integration in the paper or the proposed LE31 surface).
