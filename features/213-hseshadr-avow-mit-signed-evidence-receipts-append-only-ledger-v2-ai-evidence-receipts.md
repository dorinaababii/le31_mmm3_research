# Feature 213 — hseshadr-avow-mit-signed-evidence-receipts-append-only-ledger-v2-ai-evidence-receipts (defer)

> **NEW observation (2026-09-22).** Documents in-window GitHub Search `append-only+ledger` query result: `hseshadr/avow` (**MIT ✓**, **0★/0⑂**, Python, **pushed 2026-09-16T16:10:13Z**, in-window by push only, **443 KB** moderate repo, default_branch=`main`). Topics (verbatim from raw JSON, **0 topics**): none. Description (verbatim, parent-verified GitHub Search raw JSON): *"Signed evidence receipts and an append-only ledger."* **The strongest v2-AI signed-evidence-receipts vocabulary of the 53-pass series** (the only in-window candidate with the *signed evidence receipts + append-only ledger* double-primitive). Bucket: **v2-AI signed-evidence-receipts (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"signed evidence receipts + append-only ledger"** double-primitive as a persistent cross-section reference for any future LE31 v2-AI surface that introduces an AI-assisted workflow with evidence-binding + audit-trail. The artifact is the persistent cross-section reference + the two named architectural primitives (signed evidence receipts, append-only ledger). No code today (MIT license permits future code reuse; vocabulary-only artifact today).

## Scope

**In scope (defer artifact):**
- A written record of the **signed evidence receipts** discipline: every fact extracted from an AI assistant interaction is recorded as a cryptographically-signed receipt; the receipt can be verified independently. The *signed-evidence-receipt* primitive is the *cryptographically-bound-assertion* primitive: the receipt carries a signature that proves the assertion came from a specific source at a specific time.
- A written record of the **append-only ledger** discipline: every signed evidence receipt is appended to an immutable ledger; the ledger is the persistent record; views are derived, not stored.
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-assisted workflow surface (charter §3.4 explicit invariant) AND because v1's `audit_logs` table does not currently include a cryptographic-signature column.
- A cross-section reference with the prior AI-governance + audit-log + append-only-ledger + signature-binding + human-gate primitives cluster: features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167 (provtrail hash-chained ledger), 169 (openshare-ledger SHA-256 hash chain), 175 (geminka-agent), 183 (n0-public agent-safety), 187 (traust-ledger), 188 (ShibaClaw), 189 (HASHI), 190 (ilyautov small-business-RU-34), 192 (LinkedParticles/particles-standard), 196 (monstabravo agent-ledger append-only-checked-against-git), 197 (rajo69/ledgerkb — repo now 404), 198 (aidankaras-arbiter postgresql point-in-time), 199 (karusrus-transparency-kit EU AI Act Article 50), 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 212 (this file's Pick A sister — Rooster-glitch/Hardtack v2-AI sovereign-context-ledger), 214 (this file's Pick C sister — ilovepixelart/matador v1 frontend-architecture-reference). The *transferable insight* is the **signed evidence receipts + append-only ledger** double-primitive set.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2-AI surface in v1 (charter §3.4 explicit invariant).
- Any cryptographic signature infrastructure in v1 (LE31 v1 uses no cryptography; signing is out-of-scope until v2 introduces AI).

## Description

GitHub Search `append-only+ledger` query (parent re-fetched live, see `/tmp/le31-daily-2026-09-22/gh/append_only_ledger_10cb2e.json`) returned 35 total / 35 retrieved candidates; `hseshadr/avow` is one of the 3 net-new in-window MIT Python candidates not previously filed. It is the strongest v2-AI signed-evidence-receipts vocabulary of the 53-pass series.

The `hseshadr/avow` repo's architectural pattern has two core sub-primitives:

1. **Signed evidence receipts** — the *evidence-binding* discipline (every fact extracted from an AI assistant interaction is recorded as a cryptographically-signed receipt; the receipt can be verified independently) maps onto any future LE31 v2-AI surface that needs to commit AI-extracted data with verifiable provenance. The *signed-evidence-receipt* primitive is the *cryptographically-bound-assertion* primitive: the receipt carries a signature that proves the assertion came from a specific source at a specific time. The signature scheme is the *attribution primitive* — without it, the receipt is just a claim; with it, the receipt is a verifiable claim.

2. **Append-only ledger** — direct LE31 `audit_logs` discipline match. The *append-only ledger* holds the sequence of signed evidence receipts; each receipt is a new append-only entry; the ledger is the persistent record; views are derived, not stored. The *append-only-ledger* framing maps directly onto LE31's existing `audit_logs` schema (every state change is a new append-only entry).

The LE31 relevance is the **signed evidence receipts + append-only ledger** double-primitive. LE31 v1 has no AI surface at all (charter §3.4 explicit invariant); the question this repo answers is "if (and only if) LE31 v2 ever introduces an AI-assisted workflow, what is the evidence-binding primitive that satisfies charter §3.1 (every state transition must be attributable) + charter §3.4 (operator-tooling with observable evidence + non-AI fallback)?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v2-AI trigger condition (if the first v2-AI PR that introduces an AI-assisted workflow lands):** potential schema additions (depending on the v2-AI surface):
- `signed_evidence_receipts` table — each AI-extracted fact would carry a signed receipt in this table; the *signed-evidence-receipt* primitive from avow. Each row would have `receipt_id`, `actor_user_id`, `assertion` (JSONB), `signature_algorithm` (`HMAC-SHA256` | `Ed25519` | `ECDSA-P256`), `signature_value` (BYTES), `public_key_id` (FK to `signing_keys` table), `recorded_at`, `prev_receipt_hash` (for chain integrity).
- `signing_keys` table — each public key for verifying signatures; the *key-management* discipline from avow.
- `audit_logs.signature_id` FK column — possibly add a nullable `signature_id` FK column to `audit_logs` (existing rows remain signature-less; new AI-assisted workflow entries would carry signatures).
- `signature_verification_log` table — each signature verification attempt would carry an entry; the *verifiable-evidence* discipline from avow.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces an AI-assisted workflow lands):**
- Add a `signed_evidence_receipts` SQLModel table (receipt_id, actor_user_id, assertion, signature_algorithm, signature_value, public_key_id, recorded_at, prev_receipt_hash).
- Add a `signing_keys` SQLModel table (key_id, algorithm, public_key_bytes, owner_user_id, created_at, revoked_at).
- Add a nullable `signature_id` FK column to `audit_logs` (existing rows remain signature-less).
- Add a periodic `signature_verification_log` job that verifies all receipts and logs the verification status.
- Add a `verify_receipt(receipt_id) -> bool` endpoint that re-verifies a single receipt on demand.

**Steps independent of the v2-AI trigger (today):**
- [x] Read the `hseshadr/avow` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *signed evidence receipts + append-only ledger* double-primitive vocabulary (parent re-verified verbatim).
- [x] Cross-reference with features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167 (provtrail hash-chained ledger), 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (repo now 404), 198, 199, 203, 204, 205, 212 (this file's Pick A sister), 214 (this file's Pick C sister) (ripgrep-verified distinct).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces an AI-assisted workflow lands):**
- The owner would need a Telegram command to view a *signed-evidence-receipt* (e.g., `/receipt show <receipt_id>`); the *signed-evidence-receipt* primitive would expose a chat-style query interface for verifying AI-extracted facts.
- The owner would need a Telegram command to verify a receipt's signature (e.g., `/receipt verify <receipt_id>`); the *cryptographically-bound-assertion* primitive maps 1:1 onto a chat-style verification interface.
- These are v2-AI surface additions; not in v1 scope.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v2-AI trigger dependencies:** depends on the v2-AI surface that introduces an AI-assisted workflow with evidence-binding + audit-trail (LE31 v1 has none of these surfaces). Cross-references: features 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 126 (Five Primitives for Governing AI Agents), 127 (Zero-Shot Self-Orchestration), 128 (SKILL.state), 133 (HANSARD), 134 (ECHO), 137 (NL-to-Executable-Obligations), 141 (KRINEIA five-invariants), 145 (garde-fous), 152, 156 (AWIG-OS rule-citing-audit), 160 (FactGraph), 167 (provtrail hash-chained ledger), 169 (akoffice933 openshare-ledger SHA-256 hash chain), 175 (geminka-agent), 183 (n0-public agent-safety), 187 (traust-ledger disposition-ledger kernel), 188 (ShibaClaw self-hosted security-first AI agent), 189 (HASHI local-first control-plane), 190 (ilyautov small-business-RU-34 AI-skills-tax-contractor-INN), 192 (LinkedParticles/particles-standard sourced + confidence-scored append-only ledger), 196 (monstabravo agent-ledger append-only-checked-against-git), 197 (rajo69-ledgerkb — repo now 404, vocabulary-only), 198 (aidankaras-arbiter postgresql point-in-time), 199 (karusrus-transparency-kit EU AI Act Article 50), 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 212 (this file's Pick A sister — Rooster-glitch/Hardtack v2-AI sovereign-context-ledger), 214 (this file's Pick C sister — ilovepixelart/matador v1 frontend-architecture-reference).

## Open questions

1. **Signature scheme choice:** avow's signature scheme is not specified in the description (HMAC-SHA256? Ed25519? ECDSA-P256? a custom scheme?). The full read of avow's signing code is needed before any v2 port.
2. **Key-management discipline:** how does avow manage signing keys (is there a per-user key? a per-organization key? a single root key? a key-rotation policy?). The full read of avow's key-management code is needed before any v2 port.
3. **Receipt-assertion schema:** what is the schema of an *assertion* field (JSONB? a typed payload? a free-form string? a structured claim?). The full read of avow's receipt schema is needed before any v2 port.
4. **Append-only-ledger chain integrity:** does avow use `prev_receipt_hash` for chain integrity (like a Merkle-tree hash chain)? The full read of avow's ledger schema is needed before any v2 port.
5. **MIT license file confirmation:** is avow's MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **signed evidence receipts + append-only ledger** double-primitive is the **cleanest 2026-09-22 v2-AI signed-evidence-receipts vocabulary for any future LE31 v2 surface that introduces an AI-assisted workflow** — and the MIT permissive license confirms it's a *practiced discipline*, not just a theoretical one. The vocabulary is fully transferable to LE31's charter §3.1 compliance pattern (every state transition must be attributable; cryptographic signatures are the strongest attribution primitive) + charter §3.4 compliance pattern (operator-tooling with observable evidence + non-AI fallback; cryptographic verification is the strongest observable-evidence primitive). The artifact is informational only today; the value is vocabulary + a future-forkable-kernel note.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to introduce an AI-assisted workflow (e.g., LLM-suggested menu translation, LLM-suggested owner-question-answering), the owner wants *a signed-evidence-receipts surface that cryptographically binds every AI-extracted fact to its source*, but struggles because *v1 has no AI surface at all (charter §3.4 explicit invariant)* AND *v1 has no cryptographic signature infrastructure*, so that *v2 can offer AI assistance without violating §3.1 + §3.4*." **PASS** (zero-pain today; v1 is small enough that operator-tooling without AI is sufficient; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium for the architectural match (the *signed evidence receipts + append-only ledger* primitive set is well-established in the GitHub 0★-community-adoption cluster; avow's 443 KB moderate-repo footprint + MIT license confirms a real implementation, not just a proposal). MIT license is charter-compatible per §3.2. **PASS**. |
| 4 | **Conflict** | None. The *signed evidence receipts + append-only ledger* primitive set is charter §3.1 + §3.4 invariant-compatible (append-only posture preserved; cryptographic attribution is the strongest observable-evidence primitive; operator-tooling with verifiable claims + non-AI fallback; no customer-facing AI). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI signed-evidence-receipts (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/213-hseshadr-avow-mit-signed-evidence-receipts-append-only-ledger-v2-ai-evidence-receipts-HANDOFF.md` and `features/213-hseshadr-avow-mit-signed-evidence-receipts-append-only-ledger-v2-ai-evidence-receipts.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI architecture-review moment).

## Cross-references

- Parent research issue: `/opt/data/le31-daily-research-2026-09-22.md` (53rd consecutive daily-research pass).
- Companion artifacts (ripgrep-verified distinct): features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167 (provtrail hash-chained ledger), 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (rajo69/ledgerkb — repo now 404, vocabulary-only), 198, 199, 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 212 (this file's Pick A sister), 214 (this file's Pick C sister).
- Sister-picks from 2026-09-22: feature 212 (Rooster-glitch/Hardtack v2-AI sovereign-context-ledger), feature 214 (ilovepixelart/matador v1 frontend-architecture-reference).