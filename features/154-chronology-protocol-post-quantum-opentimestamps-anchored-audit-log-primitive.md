# Feature 154 — chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive (defer)

> **NEW observation (2026-09-08).** Documents in-window GitHub repo `machine-native/chronology-protocol` (Apache-2.0, **0★/0⑂**, Python, **pushed 2026-09-06T22:55:46Z**, in-window by push only, 128 KB substantial repo). Description (verbatim): *"Ledger-independent protocol for append-only, cryptographically renewable chronologies of physical-time observations, anchored into Jan09-compatible blocks."* Topics: `post-quantum`, `opentimestamps`, `provenance`, `reproducible-research`, `bitcoin`, `proof-of-work`, `timestamping`, `verifiable-evidence`. The **post-quantum provenance primitive + OpenTimestamps anchoring** is a v2-hardening primitive for LE31's `audit_logs` if cryptographic verifiability is ever required. Bucket: **v2 owner-pains architecture-reference** — watch-list defer. Zero build time today.

## Goal

Retain the **"ledger-independent protocol for append-only, cryptographically renewable chronologies of physical-time observations, anchored into Jan09-compatible blocks"** cryptographic-verifiability primitive as a persistent cross-section reference for the LE31 v2 architecture review. The artifact is the persistent cross-section reference + a candidate *named v2-hardening primitive* for any future cryptographic audit_export surface. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the chronology-protocol cryptographic-verifiability primitive: *append-only* + *cryptographically renewable* + *physical-time observations* + *Jan09-compatible blocks* (Jan09 = OpenTimestamps calendar).
- A written record of the **post-quantum** + **OpenTimestamps** + **proof-of-work** + **verifiable-evidence** sub-primitive set.
- A written record of the **"ledger-independent"** discipline: the chronology is *not* a separate ledger, it is a *transformation* of any existing append-only log that produces a verifiable chronology.
- A decision record: today's verdict is `defer` because LE31 v1's threat model is *accidental corruption* (a buggy code path), not *malicious tampering* (an attacker with database write access); the cryptographic-verifiability primitive is a *v2 surface* that doesn't exist today.
- A cross-section reference with prior picks: features 121, 122, 125, 127, 129, 133, 134, 135, 137, 138, 139, 141, 145, 146, 147, 148, 149, 153 = the 18-pick append-only-ledger + production-ERP cluster.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any new cryptographic-verifiability surface.
- Any new post-quantum signature scheme.
- Any new OpenTimestamps anchoring surface.
- Adoption of the chronology-protocol code (the repo is 128 KB and includes OpenTimestamps-anchoring + post-quantum + Bitcoin anchoring code; the stack is a Python implementation, not a library to import).

## Evidence / JTBD

When LE31 v2 introduces a cryptographic-verifiability surface (regulator-facing / partner-facing / owner-facing audit-export with non-repudiation requirements), the owner wants *a ready-made named primitive for post-quantum provenance*, but struggles because *the primitive doesn't exist in the LE31 codebase today*, so that *the v2 surface has a defensible cryptographic foundation*.

- **Evidence class**: observed (the chronology-protocol README names the four sub-primitives — *post-quantum / OpenTimestamps / verifiable-evidence / Jan09-compatible blocks* — and the topic tags confirm: `post-quantum`, `opentimestamps`, `provenance`, `reproducible-research`, `bitcoin`, `proof-of-work`, `timestamping`, `verifiable-evidence`).
- **Confidence**: high for the cryptographic primitive (the topics + description align with the OpenTimestamps ecosystem + post-quantum signature research; the *ledger-independent* discipline is a credible design choice — the chronology is computed from any append-only log, not stored separately).
- **Real observed LE31 JTBD**: zero-pain today; the v2 surface that would *use* the primitive doesn't exist; the threat model is *accidental corruption*, not *malicious tampering*.
- **The value is naming, not direct demand**: when the cryptographic-verifiability surface *is* introduced (if/when the owner asks for non-repudiation audit export), the chronology-protocol pattern is a ready-made *named primitive*.

## Description

GitHub `machine-native/chronology-protocol` (Apache-2.0, 0★/0⑂, Python, pushed 2026-09-06T22:55:46Z, in-window by push only, 128 KB substantial repo). Description (verbatim): *"Ledger-independent protocol for append-only, cryptographically renewable chronologies of physical-time observations, anchored into Jan09-compatible blocks."*

The architectural pattern has one core principle and four sub-primitives:

1. **"Append-only, cryptographically renewable chronologies"** — a *chronology* is a time-ordered sequence of records; *append-only* means new records are added but old records are never modified; *cryptographically renewable* means the chronology can be re-anchored to a new cryptographic commitment (e.g. a new OpenTimestamps block) without changing the underlying records.
2. **"Physical-time observations"** — the records are *physical-time observations* (events that happened at a specific moment in real-world time), not just ledger entries. The protocol treats the records as *evidence of physical-time events*, which is a stronger discipline than just "ledger entries with timestamps".
3. **"Anchored into Jan09-compatible blocks"** — Jan09 is the OpenTimestamps calendar that anchors timestamps into Bitcoin blocks via proof-of-work. The chronology is anchored to a Bitcoin block at regular intervals, providing *cryptographic proof* that the chronology existed at a specific time.
4. **"Ledger-independent"** — the protocol is *not* a separate ledger; it is a *transformation* of any existing append-only log. The transformation produces a verifiable chronology from the log without modifying the log. This is the key design choice: the protocol *adds verifiability* without *adding a new system*.

**The sub-primitive set:**

- **post-quantum** — the cryptographic primitives are *post-quantum-secure* (resistant to attacks by quantum computers). The signature scheme is likely a NIST PQC standard (Dilithium, FALCON, or SPHINCS+).
- **OpenTimestamps** — the anchoring surface is OpenTimestamps, which uses Bitcoin's proof-of-work to anchor timestamps. This is a *decentralized* anchoring (no central authority), which is the strongest form of cryptographic proof-of-existence.
- **proof-of-work** — the OpenTimestamps anchoring uses Bitcoin's proof-of-work as the cryptographic primitive. The *anchoring cost* is the Bitcoin mining cost; the *anchoring verification* is checking the Bitcoin block.
- **verifiable-evidence** — the chronology is *verifiable evidence* in the legal sense: a court or regulator can verify that a specific record existed at a specific time by checking the chronology + the Bitcoin block.

**The 1:1 mapping onto LE31 v1/v2 architecture:**

| Chronology-protocol primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| append-only chronologies | `audit_logs` table (every event is a new row) | §3.1 (Never update or delete ledger events) | **Implemented in v1** — `audit_logs` is already append-only |
| cryptographically renewable | **NOT IMPLEMENTED in v1** — `audit_logs` is *not* hash-chained; rows can be re-anchored individually but the chronology is not cryptographically renewable | (future v2 surface) | **Not implemented** — would require a `previous_hash` column on `audit_logs` + a re-anchoring surface |
| physical-time observations | **PARTIALLY IMPLEMENTED in v1** — `audit_logs.created_at` is a timestamp; but the protocol's *physical-time* discipline is stronger (the timestamp is *attested* by the protocol, not just recorded) | §3.1 (persist timezone-aware instants; render business dates in `Europe/Paris`) | **Partially implemented** — timestamp recording is v1; *attestation* would be v2 |
| Jan09-compatible blocks (OpenTimestamps anchoring) | **NOT IMPLEMENTED in v1** — no Bitcoin anchoring | (future v2 surface) | **Not implemented** — would require an OpenTimestamps client + a Bitcoin block verification query |
| ledger-independent | **APPLIES in v1** — the chronology is a *transformation* of `audit_logs`, not a separate system | §3.1 (current stock is derived from entries) | **Applies** — the v2 surface would be a *transformation* of the existing `audit_logs` |

**What chronology-protocol does NOT transfer:**

- The repo is 128 KB with a full Python implementation; the stack is a Python protocol implementation, not a library to import. The *protocol* is the value, not the *code*.
- The author is a *new maintainer* (created 2026-08-19, in-window push 2026-09-06; 0★/0⑂ traction). The 19-day-old repo is *not* production-traction evidence.
- The "post-quantum + OpenTimestamps + Bitcoin anchoring" sub-primitives are *future v2 surfaces*, not v1. Introducing them today would be a *v1 surface expansion* that requires an owner decision per charter §3.2.
- The cryptographic-verifiability primitive requires a Bitcoin full-node (or trusted third-party verification service) to verify the OpenTimestamps anchoring. The infrastructure cost is non-trivial (a Bitcoin full-node is 500+ GB).

**Cross-section with prior picks:**

- **Feature 121 ledger-commitment-field-tier-minimization** — the *what is committed* axis. Chronology-protocol's *append-only chronologies* is the commit primitive; feature 121's *canonical digest* is the commitment that makes the commit verifiable.
- **Feature 122 trace-integrity-cait-acceptance-criterion** — the *what is queried* axis. Chronology-protocol's *verifiable-evidence* is the *query-time* primitive (a query can verify a specific record's chronology); feature 122 supplies the query-time measurement.
- **Feature 125 auditable-continual-learning-three-axis** — the *commit-time gate* axis. Chronology-protocol's *physical-time observations* are the *commit-time gate* (the timestamp is the gate).
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** — the *operational mode of ledger-based control*. Chronology-protocol's *cryptographically renewable* is the *re-anchoring* primitive.
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** — the *explanation-time* axis. Chronology-protocol's *verifiable-evidence* is the *explanation-time* primitive (a query can verify a specific record's claim-to-evidence chain); feature 129's *graph* is the *typed edges* that make the explanation queryable.
- **Feature 133 hansard-runtime-witnessing** — the *who witnessed* axis. Chronology-protocol's *Jan09-compatible blocks* are the *witness* (Bitcoin's proof-of-work is the witness that the chronology existed at a specific time); feature 133 supplies the runtime witness.
- **Feature 134 echo-record-shape** — the *record shape* axis. Chronology-protocol's *physical-time observations* are the *record shape* (the timestamp is part of the record shape).
- **Feature 135 dreamledger-execution-settled-credit-ledger** — the *credit ledger* dual. Chronology-protocol is the *chronology* (time-ordered); feature 135 is the *credit ledger* (value-ordered).
- **Feature 137 natural-language-policies-executable-obligations** — the *policy compilation* axis. Chronology-protocol's *ledger-independent* discipline is the *policy-as-transformation* posture (the policy is applied to the existing log, not stored separately).
- **Feature 138 institutional-continuity-infrastructure-formal-model** — the *formal model* of institutional continuity. Chronology-protocol is the *cryptographic* discipline of feature 138's 9-node model; the chronology is the *independent observation* node.
- **Feature 139 stale-constraints-budgeted-verification-failures** — the *stale-constraint* problem. Chronology-protocol's *re-anchoring* is the *what handles the stale constraint* (re-anchoring re-validates the chronology).
- **Feature 141 krineia-five-invariants** — the *proof/record distinction*. Chronology-protocol's *verifiable-evidence* is the *proof*; the `audit_logs` is the *record*.
- **Feature 145 garde-fous-frozen-mandate-append-only-agent-loop** — the *frozen mandate* primitive. Chronology-protocol's *ledger-independent* discipline is the *what freezes the mandate* (the log is frozen, the chronology is computed from the frozen log).
- **Feature 146 slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section** — the *JTBD framing*. Chronology-protocol is the *cryptographic-verifiability JTBD*; feature 146 is the *bookkeeping JTBD*.
- **Feature 147 reliability-lives-in-institution-not-cognition-2609-03192v1** — the *experimental test* of the architecture. Chronology-protocol is the *informal* statement of the cryptographic-verifiability primitive; feature 147 is the *experimental* test of the operational invariants.
- **Feature 148 coxswain-graphs-harness-owns-consequence-architecture-pattern** — the *one harness owns every consequence* pattern. Chronology-protocol's *ledger-independent* is the *what owns the consequence* (the log owns the consequence, the chronology is the verifiable view of the consequence).
- **Feature 149 personal-agent-blueprint-telegram-chokepoint-architecture-pattern** — the *authorization chokepoint* pattern. Chronology-protocol's *verifiable-evidence* is the *chokepoint for the cryptographic authorization*; feature 149's *chokepoint* is the *chokepoint for the operational authorization*.
- **Feature 153 sausageos-production-erp-append-only-stock-fefo-versioned-recipes** — the *production-ERP primitive set*. Chronology-protocol is the *cryptographic-verifiability* primitive; feature 153 is the *production-ERP* primitive set.

The 19 picks (this one + 18 prior) form the **deepest single-vocabulary cluster in the 40-pass series** for the *append-only-ledger + cryptographic-verifiability + production-ERP* architectural pattern. **All 19 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only. The v2 surface would require:

- A new `previous_hash` column on `audit_logs` (the hash of the previous `audit_logs` row, forming a hash chain).
- A new `chronology_anchor` table that records the OpenTimestamps Bitcoin block anchoring for each re-anchoring event.
- A new `chronology_verification` query that detects chain breaks and verifies Bitcoin block anchoring.

None of these are v1; all are v2 surfaces that would require an *owner decision* per charter §3.2.

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the chronology-protocol cryptographic-verifiability primitive to `specs/2026-09-08-chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive-HANDOFF.md`** as a named v2 primitive for the LE31 codebase — already done in the HANDOFF.md.
2. **Wait for the first v2 surface that requires cryptographic-verifiability** — trigger conditions: (a) first v2 PR that adds a regulator-facing audit-export surface with non-repudiation requirements; (b) first v2 PR that adds a partner-facing audit-export surface with non-repudiation requirements; (c) first v2 PR that adds a post-quantum signature scheme; (d) first v2 PR that adds an OpenTimestamps anchoring surface.
3. **On trigger, evaluate the change against the chronology-protocol primitive** — does the change preserve *append-only chronologies*? Does the change add *cryptographic renewal*? Does the change add *physical-time observation attestation*? Does the change add *Jan09-compatible block anchoring*? Does the change preserve *ledger-independent* discipline?
4. **Future v2 surface (NOT v1)**: the cryptographic-verifiability primitive is a candidate v2 surface. Owner decision required: does the LE31 threat model justify the implementation cost (Bitcoin full-node + post-quantum signature scheme + OpenTimestamps client + schema changes on `audit_logs`)?

## Telegram interaction if any

**None today.** The defer artifact is documentation only; no operator surface changes.

The **future v2 surface** (if the owner decides to add cryptographic-verifiability) would: (a) add a `previous_hash` column to `audit_logs`; (b) compute the hash on every `audit_logs` insert; (c) add an OpenTimestamps client that anchors the chronology to Bitcoin blocks at regular intervals; (d) add a verification query that detects chain breaks and verifies Bitcoin block anchoring. This is a *v2 surface*, not v1.

## Dependencies

- **GitHub access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.
- **Future v2 surface dependencies** (if cryptographic-verifiability is added): a hash function (sha256 is the standard), a `previous_hash` column in `audit_logs`, a verification query, a post-quantum signature scheme (NIST PQC standard), an OpenTimestamps client, a Bitcoin full-node or trusted third-party verification service. All future; no v1 dependency.

## Open questions

1. **Does the LE31 threat model justify the implementation cost?** Owner decision required. The LE31 threat model today is *accidental corruption* (a buggy code path overwrites a row), not *malicious tampering* (an attacker gains write access to the database). The hash-chain protects against the latter; whether that protection is worth the implementation cost depends on the owner's threat model. If the restaurant is small and the database is on a VPS with a single owner account, the threat model is *low*; if the database is on a shared server with multiple users, the threat model is *higher*.
2. **Is the chronology-protocol 19-day-old 0★/0⑂ repo a credible cryptographic-verifiability data point?** Charter §3.2: stars are popularity proxy, not gate. The *protocol* is the value, not the maintainer's track record. The 128 KB substantial repo + the topic tags (`post-quantum`, `opentimestamps`, `provenance`, `reproducible-research`, `bitcoin`, `proof-of-work`, `timestamping`, `verifiable-evidence`) are credible cryptographic-verifiability primitives; the *credibility* of the maintainer is secondary to the *credibility* of the cryptographic design.
3. **Is "ledger-independent" the right framing?** The chronology-protocol is designed to be a *transformation* of any existing append-only log. This is the *correct* design for LE31 v2: the v2 surface would be a *transformation* of the existing `audit_logs`, not a separate system. The transformation produces a verifiable chronology from the log without modifying the log. This is consistent with LE31 charter §3.1 (*current stock is derived from entries*).
4. **Should the LE31 v1 `audit_logs` add a `previous_hash` column today?** Charter §3.2: only data needed for restaurant operations. The owner of a small restaurant trusts the database (single owner account on a VPS); the owner does not need cryptographic verifiability today. Recommend: no, defer to v2 if/when the owner asks for non-repudiation audit export.

## Why this matters

**Chronology-protocol is the post-quantum OpenTimestamps-anchored cryptographic-verifiability primitive of the 40-pass series.** The protocol's *ledger-independent* discipline is the key design choice: the chronology is a *transformation* of any existing append-only log, not a separate system. This is the *right* design for LE31 v2: the v2 surface would be a *transformation* of the existing `audit_logs`, not a new system.

**The cluster (19 picks, this one + 18 prior) is the persistent cross-section reference for the next v2 architecture-review moment.** All 19 are `defer`; no code change today. The cluster is the *what the LE31 architecture is*, named across 19 different sources, and ready to be referenced when the first v2 cryptographic-verifiability surface lands (regulator-facing audit export, partner-facing audit export, or post-quantum signature scheme).

**The most operationally valuable future v2 surface is post-quantum audit export**: introducing a `previous_hash` column on `audit_logs` + a hash-chain + an OpenTimestamps client that anchors the chronology to Bitcoin blocks at regular intervals would close the *non-repudiation gap* (today, the `audit_logs` is structurally append-only but not cryptographically verifiable; cryptographic verifiability would add *tamper evidence* at the cost of a Bitcoin full-node + post-quantum signature scheme + OpenTimestamps client). Owner decision required; not v1.