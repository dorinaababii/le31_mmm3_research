# Feature 151 — Offline Attestation Record sovereign-offline tamper-evident audit cross-section (defer)

> **NEW observation (2026-09-07).** Documents in-window Zenodo preprint `doi:10.5281/zenodo.22143718` (2026-08-28, **12 citations**, Micky Irons, type=preprint, Zenodo/CERN, OA status `green`). Title (verbatim): *"The Offline Attestation Record: A Tamper-Evident Provenance Mechanism for Sovereign, Offline Enterprise AI."* **First surface of this paper in the 36-pass brainstorm series** (parent-verified by ripgrep against all features 1–149 + all brainstorm reports 2026-08-04..2026-09-06). Bucket: **v2 owner-pains (architecture-reference, parking-lot defer)** — watch-list entry, zero build time today. **The 12-citation count is the highest of any net-new in-window paper in the 36-pass series** (parent-verified — next-closest net-new in-window papers cited 0–4 times).

## Goal

Retain the **"offline-first tamper-evident provenance"** primitive as the **v2-hardening pattern** for any future LE31 v2 owner-facing audit-trail surface. The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the Offline Attestation Record primitive: *sovereign/offline tamper-evident provenance for AI operations, with no third-party attestation service dependency*.
- A decision record: today's verdict is `defer` because LE31 v1 already enforces offline operation (Postgres on-premises, no cloud dependency) — the *sovereign* framing is **redundant** for v1 but the *attestation-record* pattern is the v2-hardening step.
- A cross-section reference with features 92 / 134 / 137 / 141 (the existing append-only / AI-agent-ledger cluster) — the *transferable insight* is that LE31's existing `audit_logs` discipline is already structurally aligned with the offline-attestation-record pattern; the v2 hardening is *cryptographic*, not architectural.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Adoption of any cryptographic-attestation primitive in v1.
- Adoption of any third-party attestation service in v2 (the *sovereign/offline* framing rules out cloud-dependent attestation services).

## Evidence / JTBD

When a future LE31 v2 owner wants *cryptographically verifiable audit trails without depending on a third-party attestation service*, the owner wants *a tamper-evident provenance record generated and verified on the same on-premises infrastructure that produced the original `audit_logs` rows*, but struggles because *the v1 `audit_logs` discipline is logical-append-only, not cryptographic-tamper-evident*, so that *the v2 owner can answer "was this `audit_logs` row altered since it was written?" with a cryptographic proof*.

- **Evidence class**: inferred (no LE31 owner has asked for cryptographic-verifiability in 36 passes; the 12-citation count is a cross-section signal, not an LE31 demand).
- **Confidence**: medium (mechanism is well-defined; v2 surface doesn't exist today).
- **Real observed LE31 JTBD**: none directly. Charter §3.1 *append-only StockEntry* is the *logical* primitive; the *cryptographic* primitive is the v2 step.
- **The value is contingency**, not direct demand: when (if) LE31 v2 introduces an owner-facing audit-trail surface with cryptographic-verifiability requirements, the architectural primitive already exists.

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred only — no observed LE31 v1 pain; v2 surface doesn't exist. |
| 2. Viability | Mechanism is well-defined (offline, sovereign, tamper-evident); no on-premises cryptographic-attestation service exists in LE31 today. |
| 3. Practicability and confidence | Confidence: medium. Stack: Python stdlib `hashlib` covers SHA-256; `cryptography` covers signatures; on-premises key-management is the only v2-dependency. |
| 4. Conflict | No conflict with charter §3.1 (the primitive is *additive* to append-only); no conflict with §3.2 (no third-party attestation service). |
| 5. Outcome, appetite, scope | v2 owner-pains (architecture-reference). Appetite: zero today. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value: high (cryptographic-verifiability is a regulator-facing primitive, useful for any future audit-export surface). |
| 7. Circuit breaker and reversibility | Trivially reversible: written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today. The 12-citation count is a *cross-section credibility signal* but not a `build` upgrade trigger.

## Implementation steps

None today. When v2 introduces any cryptographic-verifiability requirement, the *primitive* to surface is **"tamper-evident provenance generated and verified on the same on-premises infrastructure"** — the `audit_logs` schema gains a `row_hash` column (SHA-256 of the canonicalised row) and the table gains a *hash-chain* column (each row's hash includes the previous row's hash). Both fields are computable from existing data via a one-shot migration; the runtime cost is one SHA-256 per row write.

## Dependencies

- None today.
- Future dependencies (v2 only): Python `hashlib` (stdlib, no install); optional `cryptography` package for ECDSA signatures (already in the LE31 transitive dependency graph via `pyjwt`); on-premises key-management surface (a sealed config file or env var is sufficient for v2).

## Open questions

1. **Does LE31 v2 ever introduce cryptographic-verifiability?** Today: no signal. The default is *no* unless regulator-facing or partner-facing audit requirements surface.
2. **Is the v2 primitive SHA-256 hash-chain (cheap, sufficient) or ECDSA signed-hash-chain (heavier, regulator-recognised)?** The hash-chain alone proves tamper-evident; the signature additionally proves non-repudiation. The v2 decision depends on whether the audit trail needs to defend against *operator-level tampering* (hash-chain is sufficient) or *owner-level tampering* (signature is required).

## Why this matters

The 12-citation count is a *credibility signal*: 12 distinct citing works chose to cite this preprint within ~10 days of release (2026-08-28 → 2026-09-07). That's an unusually high citation velocity for an in-window preprint and indicates the *sovereign/offline* framing has cross-discipline resonance. For LE31 v1, the implication is *none* (v1 is already offline-first). For LE31 v2, the implication is *the architectural primitive is mapped, and the implementation is one hash-chain migration away*. **No build today.**
