# Feature 150 — Mandato MCP digitally-signed-mandate chained-audit cross-section (defer)

> **NEW observation (2026-09-07).** Documents in-window arXiv preprint `arXiv 2608.14074` (2026-08-14, 0 citations, Giovanni Racioppi, type=preprint). Title (verbatim): *"Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails."* Abstract-inverted-index first 30 keys (verbatim): *"AI agents increasingly act on external systems through standardized tool-calling protocols such as the Model Context Protocol (MCP), yet no infrastructure layer constrains their actions to what a principal has..."* **First surface of this paper in the 36-pass brainstorm series** (parent-verified by ripgrep against all features 1–149 + all brainstorm reports 2026-08-04..2026-09-06). Bucket: **v2 owner-pains (architecture-reference, parking-lot defer)** — watch-list entry, zero build time today.

## Goal

Retain the **"digitally signed mandate at the protocol level + cryptographically chained audit trail"** primitive as the **architectural dual** of LE31's charter §3.1 *append-only StockEntry* discipline. The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the Mandato primitive: *AI agent tool-call actions are constrained by a principal-signed mandate recorded at the protocol level (MCP), with the mandate itself forming a node in a cryptographically chained audit trail*.
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-agent surface today (charter §3.4 forbids customer-facing AI; v1 has no AI at all).
- A cross-section reference with the LE31 charter §3.1 *append-only StockEntry* posture — the *transferable insight* is **"the row carries the signed proof of authority that authorised the action"** — applicable to any future LE31 v2 surface that wants to enforce *"this `StockEntry` was authorised by the cook, not by an AI auto-suggestion."*

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any change to the `audit_logs` schema.
- Any change to the cook Telegram bot authorization flow.
- Adoption of MCP, or any agent-tool-calling protocol surface.
- Adoption of any cryptographic-signature primitive in v1.

## Evidence / JTBD

When a future LE31 v2 owner wants to verify *which authorisation enabled a given `StockEntry` row to be written*, the owner wants *a signed proof of authority attached to the row*, but struggles because *the current `audit_logs` records the operator but not the authority*, so that *the owner can answer the authority question without re-litigating the operator's role*.

- **Evidence class**: inferred (no LE31 owner has asked for this surface in 36 passes).
- **Confidence**: medium (mechanism) / low (present urgency).
- **Real observed LE31 JTBD**: none. No owner has asked *"which mandate authorised this `StockEntry`?"* in 36 passes.
- **The value is contingency**, not direct demand: when the question is eventually asked (or when v2 introduces any AI-assisted operator surface), the architectural primitive already exists.

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred only — no observed LE31 v1 pain; no reported v2 demand. |
| 2. Viability | Mechanism is well-defined; LE31 v1 has no AI-agent surface, so viability is conditional on v2. |
| 3. Practicability and confidence | Confidence: medium. Stack: no MCP, no agent surface. No rabbit holes visible today. |
| 4. Conflict | No conflict with charter §3.1 (append-only); charter §3.4 (no customer-facing AI) is the *trigger* for this primitive's relevance, not a conflict. |
| 5. Outcome, appetite, scope | v2 owner-pains (architecture-reference). Appetite: zero today. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value only. |
| 7. Circuit breaker and reversibility | Trivially reversible: this is a written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today.

## Implementation steps

None today. When v2 introduces any AI-assisted operator surface, the *primitive* to surface is **"the row carries the signed proof of authority that authorised the action"** — the audit_logs schema gains a `mandate_hash` column or equivalent, populated by the cook's explicit confirmation (the existing `cook_authorization_at` timestamp is the *implicit* form; the explicit cryptographic primitive is the v2 form).

## Dependencies

- None today.
- Future dependencies (v2 only): a digital-signature library (e.g., `cryptography` stdlib or `secp256k1`); a key-management surface; a mandate-authoring surface. None of these are in v1 scope.

## Open questions

1. **Does LE31 v2 ever introduce an AI-assisted operator surface?** This is the only question that would re-open this pick for a `build` upgrade. The default answer today is *no* (charter §3.4).
2. **Is the *implicit* cook-authorization timestamp sufficient as the v1 primitive?** Today's `cook_authorization_at` field is the implicit form; whether it should be promoted to an explicit *cryptographic* mandate is a v2 owner-facing decision.

## Why this matters

When (if) LE31 ever surfaces an AI-assisted *operator-facing* tool (e.g., an AI-suggested prep adjustment, or an AI-suggested payment tip), the question *"which mandate authorised this action?"* will need an answer. The answer should be **"the row itself carries the signed proof"** — not a separate audit-trail-of-audit-trail. The Mandato paper maps this primitive cleanly. **No build today.**
