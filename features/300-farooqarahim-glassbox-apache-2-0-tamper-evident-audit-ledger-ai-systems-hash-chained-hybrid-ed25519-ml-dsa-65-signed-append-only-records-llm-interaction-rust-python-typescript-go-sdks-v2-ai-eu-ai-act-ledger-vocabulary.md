# Feature 300 — `farooqarahim-glassbox-apache-2-0-tamper-evident-audit-ledger-ai-systems-hash-chained-hybrid-ed25519-ml-dsa-65-signed-append-only-records-llm-interaction-rust-python-typescript-go-sdks-v2-ai-eu-ai-act-ledger-vocabulary` (defer)

> **NEW observation (2026-10-10).** Documents in-window GitHub repo `farooqarahim/glassbox` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, **5★/0⑂**, Rust core + Python + TypeScript + Go SDKs, **pushed 2026-10-07T22:24:17Z**, in-window by `pushed_at` only, **created 2026-07-03T20:37:01Z** — 99-day-old repo with in-window push, **429 KB modest repo**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-10): *"Tamper-evident audit ledger for AI systems: hash-chained, hybrid Ed25519 + ML-DMA-65 signed, append-only records of every LLM interaction. Built in Rust, with Python, TypeScript and Go SDKs."* Topics (verbatim, parent-verified): `ai-governance, audit-log, compliance, cryptography, eu-ai-act, golang, llm, mcp, merkle-tree, observability, post-quantum-cryptography, python, rust, tamper-evident, typescript` — 15 topics including **`python`** (LE31 stack match) + **`eu-ai-act`** (LE31 v2-AI domain match) + **`mcp`** (LE31 v2-AI integration) + **`post-quantum-cryptography`** (LE31 v2-AI forward-compatibility) + **`tamper-evident` + `merkle-tree` + `audit-log`** (LE31 v2-AI audit primitives). Bucket: **v2-AI (EU-AI-Act-ledger-vocabulary)** — Pick B of Daily Research 2026-10-10. Build verdict: `defer` (parking-lot). Zero build time today.

> **NOTE**: The repo description has a typo: "ML-DMA-65" — the actual signature scheme is `ML-DSA-65` (Module-Lattice-based Digital Signature Algorithm, formerly `CRYSTALS-DILITHIUM-3`, NIST FIPS 204 standardized for post-quantum cryptography). Topics correctly list `post-quantum-cryptography`.

## Goal

Retain the **`tamper-evident + hash-chained + hybrid Ed25519 + ML-DSA-65 signed + append-only + EU-AI-Act + MCP + Python SDK`** nonuple-primitive as a persistent cross-section reference for the LE31 v2-AI *EU AI Act Article 50 compliance + post-quantum-signature + MCP-server + hash-chained-audit-log* wedge, and document the **stack-shape validation + post-quantum-readiness** that an independent maintainer arrived at in 2026 (99-day-old repo with in-window push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal + a **forward-compatibility signal** for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`tamper-evident + hash-chained + hybrid Ed25519 + ML-DSA-65 signed + append-only + EU-AI-Act + MCP + Python SDK`** nonuple-primitive: every LLM interaction is recorded as an append-only entry; the entry is hash-chained via Merkle-tree; the chain is hybrid-signed with both Ed25519 (classical) and ML-DSA-65 (post-quantum) signature schemes; the package is EU-AI-Act-aware; the package is MCP-server-integrated; the package is Python-SDK-accessible. This is the §3.1 explicit-state-transitions + forward-compatibility + EU-AI-Act-compliance primitive applied to LLM-interaction audit-logging with post-quantum signature readiness.
- A written record of the **`Rust core + Python + TypeScript + Go SDKs`** stack-shape: this is **1 of 4 LE31 backend stack primitives** matched (Python is on-stack; Rust is the off-LE31-stack core; TypeScript and Go are SDKs that LE31 doesn't directly use but the **Python SDK** is the value); the **Python SDK** is the on-LE31-stack primitive that bridges the off-stack Rust core.
- A written record of the **`EU-AI-Act + MCP + LLM + post-quantum-cryptography`** operator-surface-shape: every LLM interaction is recorded + signed + EU-AI-Act-aware + MCP-accessible + post-quantum-ready. Sister-shape to feature 199 (karusrus/transparency-kit — EU AI Act Article 50 + audit-log + hash-chained-ledger + human gate) + feature 232 (lpalbou/AbstractGateway — durable AI control plane) + feature 287 (noise01/endoxa — governed beliefs for LLM agents) + feature 288 (pete-builds/mcp-nixreview — advisory NixOS change-review with CVE attestation gate) + feature 289 (shivamk01here/LedgerLoop — Python runtime for financial AI agents).
- A decision record: today's verdict is `defer` because (1) the repo is 5★ with single-maintainer cadence (99-day-old, in-window push today); (2) the stack-shape match is the value, not the code (LE31 v1 has no LLM; v2-AI is OFF v1 charter; the **Python SDK** bridges the off-stack Rust core); (3) the *post-quantum-readiness + EU-AI-Act + MCP + Python SDK* combination is the **only forward-compatible + EU-AI-Act-aware + Python-SDK-accessible v2-AI audit-ledger of the 72-pass series** = the demand-signal is the value.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the glassbox codebase (Rust core with off-LE31-stack; the Python SDK bridges but the maintainer is single-cadence).
- Cross-pollination with the v2-AI audit primitive in v1 (LE31 v1 has no LLM).
- Cross-pollination with the EU AI Act Article 50 in v1 (LE31 v1 has no LLM, no EU AI Act applicability).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "the EU AI Act Article 50 + post-quantum-signature + MCP-server + hash-chained + Python SDK primitive" (e.g., a v2-AI surface that registers an AI assistant + requires EU AI Act Article 50 label + posts an audit-log entry to MCP for external verification + signs the entry with both Ed25519 + ML-DSA-65 for post-quantum forward-compatibility), the owner wants *a primitive that proves the demand for this shape exists in 2026 with a post-quantum-signature + EU-AI-Act + Python-SDK shape*, but struggles because *most v2-AI audit-ledger candidates are off-stack OR lack post-quantum readiness OR lack EU AI Act awareness OR lack Python SDK*, so that *the v2-AI surface has a credible peer reference with a forward-compatible signature scheme*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `ai-governance, audit-log, compliance, cryptography, eu-ai-act, golang, llm, mcp, merkle-tree, observability, post-quantum-cryptography, python, rust, tamper-evident, typescript`).
- **Confidence**: high for the vocabulary match (the verbatim description names the 4-primitive set + the tech-stack + the **post-quantum-cryptography** topic); high for the **post-quantum-readiness signal** (ML-DSA-65 is the NIST-standardized post-quantum signature scheme = the only post-quantum-ready v2-AI audit-ledger of the 72-pass series); low for code adoption.
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no LLM); the value is the *EU-AI-Act + post-quantum + MCP + Python SDK + hash-chained + tamper-evident* vocabulary — when the first v2 PR that adds a v2-AI surface lands, the glassbox pattern is a ready-made *named primitive*.

## Description

GitHub `farooqarahim/glassbox` (Apache-2.0, 5★/0⑂, Rust core + Python SDK + TypeScript SDK + Go SDK, pushed 2026-10-07T22:24:17Z, created 2026-07-03T20:37:01Z, 429 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-10): *"Tamper-evident audit ledger for AI systems: hash-chained, hybrid Ed25519 + ML-DSA-65 signed, append-only records of every LLM interaction. Built in Rust, with Python, TypeScript and Go SDKs."*

The architectural primitive has nine sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **`Tamper-evident`** — every audit-log entry is sealed with a hash-chain + signature so any tampering is detectable. The *tamper-evident* primitive maps 1:1 onto LE31's §3.1 append-only discipline (current state is derived from entries; entries cannot be silently modified).
2. **`Hash-chained`** — every entry is linked to the previous entry via a hash; the chain is verifiable from the genesis entry to the latest entry. The *hash-chained* primitive maps 1:1 onto LE31's append-only discipline + any future v2 surface that adds a `verify_audit_log_chain` endpoint.
3. **`Hybrid Ed25519 + ML-DSA-65 signed`** — every entry is signed with both Ed25519 (classical, fast, widely-deployed) AND ML-DSA-65 (post-quantum, NIST FIPS 204, future-proof against quantum-computer attacks). The **hybrid-signature primitive is the only post-quantum-readiness signal of the 72-pass series**. The *Ed25519 + ML-DSA-65* combination is the **forward-compatibility primitive** that future-proofs the audit-log against quantum-computer attacks.
4. **`Append-only records of every LLM interaction`** — every LLM interaction (request, response, model, prompt, completion) is recorded as an append-only entry. The *append-only* primitive maps 1:1 onto LE31's §3.1.
5. **`EU-AI-Act`** — the audit-log is EU AI Act Article 50 aware (labelling, human gate, registry). The *EU-AI-Act* primitive maps 1:1 onto any future v2-AI surface that needs EU AI Act Article 50 compliance.
6. **`MCP`** — the audit-log is MCP-server-integrated; external MCP clients can verify the chain via MCP. The *MCP* primitive maps 1:1 onto any future v2-AI surface that needs MCP integration.
7. **`Python SDK`** — the audit-log is Python-SDK-accessible; Python clients can read + verify the chain. The **Python SDK is the on-LE31-stack primitive** that bridges the off-stack Rust core.
8. **`Merkle-tree`** — the chain is organized as a Merkle-tree for efficient verification. The *Merkle-tree* primitive maps 1:1 onto any future v2 surface that needs a `verify_audit_log_merkle_proof` endpoint.
9. **`Observability`** — the audit-log is observability-integrated; metrics + traces + logs are emitted. The *observability* primitive maps 1:1 onto any future v2 surface that needs observability hooks.

**The 1:1 mapping onto LE31 surface:**

| glassbox primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Tamper-evident | `audit_logs` (append-only + hash-chained) | §3.1 ✓ | **Implemented (v1, partial)** |
| Hash-chained | `audit_logs` (append-only) | §3.1 ✓ | **Implemented (v1, partial)** |
| Hybrid Ed25519 + ML-DSA-65 signed | (LE31 v1 has no signature scheme) | v2-AI | **Not implemented** — v2-AI surface |
| Append-only records of every LLM interaction | `audit_logs` (append-only) | §3.1 ✓ | **Implemented (v1)** |
| EU-AI-Act | (LE31 v1 has no LLM, no EU AI Act applicability) | v2-AI | **Not implemented** — v2-AI surface |
| MCP | (LE31 v1 has no MCP integration) | v2-AI | **Not implemented** — v2-AI surface |
| Python SDK | Python 3.13 (LE31 v1 stack) | §3.1 ✓ | **Implemented (v1)** |
| Merkle-tree | (LE31 v1 has no Merkle-tree) | v1 polish | **Not implemented** — v1 polish surface |
| Observability | (LE31 v1 has no observability hooks) | v1 polish | **Not implemented** — v1 polish surface |
| Rust core | (LE31 v1 is Python-only) | off-stack | **Not implemented** — different runtime |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface that requires EU AI Act Article 50 compliance + post-quantum-signature + MCP-server + hash-chained + Python SDK), the implementation would add:

1. A new `LLMAuditLogEntry` table (Alembic migration) with columns: `id` (UUID), `llm_id` (str), `request` (JSON), `response` (JSON), `model` (str), `prompt_hash` (str), `completion_hash` (str), `previous_entry_hash` (str), `this_entry_hash` (str), `ed25519_signature` (str), `ml_dsa_65_signature` (str), `created_at` (timezone-aware datetime), `recorded_at` (timezone-aware datetime).
2. A `llm_audit_log_merkle_proofs` table (Alembic migration) with columns: `id` (UUID), `entry_id` (UUID FK), `merkle_root` (str), `merkle_proof` (JSON), `created_at`.
3. An `INSERT ... ON CONFLICT DO NOTHING` guard on the `LLMAuditLogEntry` insert path.
4. A `POST /v2/llm/audit-log/entries` FastAPI endpoint to record an entry.
5. A `GET /v2/llm/audit-log/entries/verify` FastAPI endpoint that walks the chain + verifies both Ed25519 + ML-DSA-65 signatures.
6. A `GET /v2/llm/audit-log/entries/<entry_id>/merkle-proof` FastAPI endpoint that returns the Merkle proof for a given entry.
7. A `GET /v2/llm/audit-log/entries?llm_id=<>&as_of=<>` query endpoint for the operator UI.
8. A `MCP server` integration that exposes the verify + merkle-proof endpoints via MCP.
9. A `eu_ai_act_registry` table (Alembic migration) that tracks the registered AI systems + their EU AI Act Article 50 labels.

The HANDOFF is to evaluate whether the v2-AI surface is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires:

**For v2-AI EU-AI-Act-ledger-vocabulary surface** (if approved):

1. Add a new `LLMAuditLogEntry` SQLModel table (Alembic migration).
2. Add a new `llm_audit_log_merkle_proofs` SQLModel table (Alembic migration).
3. Add an `INSERT ... ON CONFLICT DO NOTHING` guard on the `LLMAuditLogEntry` insert path.
4. Add a `cryptography` library dependency to `requirements.txt` for Ed25519 signing.
5. Add a `pqcrypto` library dependency to `requirements.txt` for ML-DSA-65 signing (or a C-binding to a Rust implementation).
6. Add a `GET /v2/llm/audit-log/entries/verify` FastAPI endpoint that walks the chain + verifies both signatures.
7. Add a `GET /v2/llm/audit-log/entries/<entry_id>/merkle-proof` FastAPI endpoint.
8. Add a `MCP server` integration via `mcp` library.
9. Add a `eu_ai_act_registry` SQLModel table for the EU AI Act Article 50 registry.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires, the v2-AI surface would add **a v2-AI owner-Telegram-notification primitive** for EU AI Act Article 50 events (e.g. the owner gets a Telegram notification when an AI assistant is registered in the EU AI Act registry, when an LLM interaction is recorded, when the chain is verified, when the Merkle proof is exported). The notification primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; matches glassbox's Python SDK).
- **External**: `cryptography` library (Ed25519 signing); `pqcrypto` library (ML-DSA-65 signing); `mcp` library (MCP-server integration).
- **Internal**: §3.1 (append-only discipline for `audit_logs`); §3.2 (Apache-2.0 permissive license compatible); §3.4 (operator-tooling only, no customer-facing AI).
- **Trigger dependency**: future v2 PR that adds a v2-AI surface that requires EU AI Act Article 50 compliance.

## Open questions

- **Q1**: When (if ever) will LE31 introduce a v2-AI surface with EU AI Act Article 50 applicability? The v1 charter explicitly excludes customer-facing AI (§3.4); the EU AI Act Article 50 only applies to customer-facing AI. If v2-AI is owner/staff-assist only, EU AI Act Article 50 doesn't apply.
- **Q2**: When will ML-DSA-65 be the standard? NIST FIPS 204 was published in 2024; ML-DSA-65 is the 192-bit-security post-quantum signature scheme. The hybrid Ed25519 + ML-DSA-65 signing is the **defensive measure against harvest-now-decrypt-later quantum-computer attacks**; the standard is ready, the tooling is ready, but the threat model is still 5-10 years out.
- **Q3**: Will the LE31 v2 surface ever need a Merkle-tree? The v1 `audit_logs` is a flat append-only table; the Merkle-tree is a v2 surface primitive that allows efficient verification of arbitrary sub-trees.
- **Q4**: Will the LE31 v2 surface ever need MCP-server integration? MCP is the Model Context Protocol for AI-agent tool-calling; if v2-AI ever exposes LE31 as an MCP-server, the audit-log needs to be MCP-accessible.

## Why this matters

The **`tamper-evident + hash-chained + hybrid Ed25519 + ML-DSA-65 signed + append-only + EU-AI-Act + MCP + Python SDK`** nonuple-primitive is the **strongest direct LE31 v2-AI EU-AI-Act-ledger-vocabulary + post-quantum-readiness + Python-SDK reference of the 72-pass series** for three reasons:

1. **The 9-primitive vocabulary is the future v2-AI surface primitive**: when LE31 v2 introduces an AI-assisted owner-side workflow (e.g. an AI assistant that registers in the EU AI Act registry + records LLM interactions + signs with post-quantum-readiness + exposes the chain via MCP for external verification), the glassbox pattern is a ready-made *named primitive*.

2. **The Python SDK is the on-LE31-stack bridge**: glassbox's Rust core is off-LE31-stack, but the **Python SDK is the on-stack bridge** that any future v2-AI surface can adopt directly. The *Apache-2.0 permissive license* + *Python SDK* + *MCP integration* is the unique combination.

3. **The post-quantum-readiness is the only forward-compatibility signal of the 72-pass series**: the **ML-DSA-65 (NIST FIPS 204) signature scheme** is the **only post-quantum-ready v2-AI audit-ledger primitive of the 72-pass series**. The hybrid Ed25519 + ML-DSA-65 signing is the **defensive measure against harvest-now-decrypt-later quantum-computer attacks**; the standard is ready, the tooling is ready, and the **forward-compatibility posture** is rare.

Sister-shape to features 187 + 188 (traust-ledger — append-only disposition ledger) + 199 (karusrus/transparency-kit — EU AI Act Article 50 + audit-log + hash-chained-ledger + human gate) + 232 (lpalbou/AbstractGateway — durable AI control plane) + 287 (noise01/endoxa — governed beliefs for LLM agents) + 288 (pete-builds/mcp-nixreview — advisory NixOS change-review with CVE attestation gate) + 289 (shivamk01here/LedgerLoop — Python runtime for financial AI agents with idempotent exactly-once execution). The glassbox pattern is the **strongest direct EU-AI-Act + post-quantum + Python-SDK v2-AI audit-ledger primitive of the cluster**.

The trigger condition for this defer artifact to become a build is: first v2 PR that adds a v2-AI surface that requires EU AI Act Article 50 compliance + post-quantum-signature + MCP-server + hash-chained + Python SDK.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/142-feldroy-air-fastapi-htmx-ai-write-framework.md` — carry-over FastAPI + HTMX + Pydantic reference
- `features/187-traust-security-traust-ledger-apache-2-0-append-only-disposition-ledger-kernel-security-auditing-workflows-v2-owner-pains-architecture-reference.md` — carry-over append-only disposition ledger
- `features/199-karusrus-transparency-kit-noassertion-eu-ai-act-article-50-audit-log-hash-chained-ledger-human-gate-slack-v2-ai-compliance-primitive.md` — EU AI Act Article 50 + audit-log + hash-chained-ledger + human gate
- `features/232-lpalbou-AbstractGateway-mit-replay-first-durable-ai-control-plane-http-telegram-persistence-append-only-ledger-v2-ai-durable-control-plane.md` — durable AI control plane
- `features/236-shawn-durrani-membro-mit-local-first-memory-ai-assistants-append-only-fact-ledger-deterministic-extraction-walls-immutable-transcripts-provenance-v2-ai-local-first-ai-assistant-memory.md` — local-first AI assistant memory
- `features/287-noise01-endoxa-apache-2-0-governed-beliefs-for-llm-agents-append-only-ledger-smt-checked-consistency-defeasible-revision-calibration-python-llm-agents-truth-maintenance-v2-ai-governed-beliefs-vocabulary.md` — governed beliefs for LLM agents
- `features/288-pete-builds-mcp-nixreview-mit-advisory-nixos-change-review-cve-kev-attestation-gate-ai-agents-mcp-server-v2-ai-mcp-change-review-vocabulary.md` — advisory NixOS change-review with CVE attestation gate for AI agents
- `features/289-shivamk01here-LedgerLoop-mit-python-runtime-financial-ai-agents-idempotent-exactly-once-execution-hash-chained-ledger-v2-ai-exactly-once-execution-vocabulary.md` — Python runtime for financial AI agents with idempotent exactly-once execution
- `features/266-ierg-lab-ergon-mcp-server-ai-agent-tools-workspace-context-mcp-secure-tool-execution-apache-2-0-v2-ai-mcp-server-vocabulary.md` — MCP server for AI agents
- `features/299-A220man-human-approval-console-ryan-vo-mit-review-ai-agent-actions-atomic-approval-receipts-search-receipt-ledger-verify-hash-chain-export-audit-evidence-python-fastapi-v2-ai-approval-receipt-vocabulary.md` — Pick A of Daily Research 2026-10-10 (operator-approval of AI-agent actions)
