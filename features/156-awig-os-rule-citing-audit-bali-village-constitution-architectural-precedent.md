# Feature 156 — AWIG-OS rule-citing-audit Bali-village-constitution architectural precedent (defer)

> **NEW observation (2026-09-08).** Documents in-window GitHub repo `kfkchau/AWIG-OS` (**GPL-3.0, 0★/0⑂, Python, pushed 2026-09-08T03:56:50Z**, in-window by push only, 0.8 KB description). Description (verbatim): *"An operating system where every act is a recorded decision citing the rule that allowed it, refusals recorded the same way, and the whole system rebuilds from its record. Named for Bali's awig-awig village constitutions. GPLv3. Pre-alpha; keys are stand-ins."* Topics: `ai-governance, ai-safety, append-only, audit-log, awig-awig, constitution, event-sourcing, governance, gplv3, open-governance-standard, operating-system, python, rule-engine, subak`. **The most novel cross-section signal of the 41-pass brainstorm series. First surface of this repo in the 41-pass series** (parent-verified by ripgrep against all features 1–155 + all brainstorm reports 2026-08-04..2026-09-08). Bucket: **v2 owner-pains (architecture-reference, parking-lot defer)** — watch-list entry, zero build time today.

## Goal

Retain the **"every act cites the rule that allowed it; refusals recorded the same way; the whole system rebuilds from its record"** primitive as a persistent cross-section reference for any future LE31 v2 surface that adds a *rule-citing-audit* field to the `audit logs` table. The artifact is the persistent architectural vocabulary + the Bali `awig-awig` / `subak` named-pattern cultural precedent (Balinese village constitutions + subak irrigation councils as a *named* analogy for rule-citing-audit AI governance). No code today.

## Scope

**In scope (defer artifact):**
- A written record of the AWIG-OS primitive: *every act cites the rule that allowed it; refusals are recorded the same way; the system rebuilds from its record*. The *rule citation as a first-class element of the audit log entry* is the step-beyond features 137 / 138 / 141 / 152.
- A written record of the Bali `awig-awig` / `subak` named-pattern cultural precedent: Balinese village constitutions + subak irrigation councils as an analogy for AI governance (the GitHub repo's author uses this as a metaphor).
- A cross-section reference with the append-only-ledger + rules-as-code cluster: features 121 (Field-Tier Minimization, *what is committed*) / 122 (Trace Integrity CAIT, *what is queried*) / 125 (Auditable Continual Learning) / 137 (NL-to-Executable-Obligations, *policy compilation*) / 138 (ICI nine-node continuity) / 141 (KRINEIA five-invariants) / 145 (garde-fous frozen-mandate) / 152 (LATTICE governance-first) — the *transferable insight* is the **rule-citation-as-first-class-element-of-the-audit-log-entry**.
- A decision record: today's verdict is `defer` because LE31 v1 has no rule-citing-audit surface today (charter §3.1 append-only is satisfied by the `audit_logs` + `StockEntry` writes, but the **rule citation as a first-class field** would require a `rule_id` column on `audit_logs`, which is a v2 surface).

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Adoption of any *rule-citing-audit* surface in v1.
- Adoption of any *open-governance-standard* authoring surface in v1 (charter §3.1 tension).
- Adoption of the AWIG-OS code (the repo is GPL-3.0, which fails §3.2 for v1 import; cross-section reference value only).

## Evidence / JTBD

When a future LE31 v2 owner wants to author *shift-specific rules* as a *primary surface* (rather than author them implicitly via operational event types), the owner wants *a rule-citing-audit log where every `audit_logs` row carries the rule that authorised the action*, but struggles because *v1 has no such surface and the append-only posture is structurally entrenched*, so that *v2 can offer a rule-citing-audit surface without re-architecting v1*.

- **Evidence class**: inferred (no LE31 owner has asked for a rule-citing-audit surface in 41 passes).
- **Confidence**: medium (mechanism) / low (present urgency).
- **Real observed LE31 JTBD**: none directly. The 0★ count is a *novelty signal*, not an LE31 demand.
- **The value is vocabulary + contingency**: when (if) LE31 v2 introduces a rule-citing-audit surface, the AWIG-OS primitive is already mapped, and the Bali cultural precedent is already named.

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred only — no observed LE31 v1 pain; v2 surface doesn't exist. |
| 2. Viability | Mechanism is well-defined (rule_id column on audit_logs); viability is conditional on a v2 owner-facing authoring surface. |
| 3. Practicability and confidence | Confidence: medium for the architectural match (the rule-citation primitive is one-shot more specific than features 137/138/141/152). Stack: no impact on v1 (charter §3.1 is preserved). |
| 4. Conflict | No conflict with charter §3.1 (append-only posture is preserved); no conflict with §3.4 (AWIG-OS is *every-act-cites-the-rule*, not customer-facing-AI — the rule citation is the *authorization*, not the *AI action*). |
| 5. Outcome, appetite, scope | v2 owner-pains (architecture-reference). Appetite: zero today. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value: medium (rule-citing-audit is a v2 authoring pattern, useful for any future rules-as-code surface). |
| 7. Circuit breaker and reversibility | Trivially reversible: written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today. The Bali cultural precedent is a vocabulary addition, not a `build` upgrade trigger.

## Implementation steps

None today. When v2 introduces any rule-citing-audit surface (e.g., an owner-facing shift-reconciliation-rules editor + a `rule_id` column on `audit_logs`), the *primitive* to surface is **"every act cites the rule that allowed it; refusals recorded the same way; the whole system rebuilds from its record"** — and the *cultural precedent* to surface is **the Bali `awig-awig` / `subak` named-pattern** (village constitutions + irrigation councils as a *named* analogy for rule-citing-audit AI governance). The v2 owner-facing surface would let the owner author *rules*, and the system would emit *rule-citing audit log entries* as derived effects of the rules. This is a *refinement* of v1's append-only posture; it does not require re-architecting v1.

## Dependencies

- None today.
- Future dependencies (v2 only): a rule-authoring surface (UI + storage); a `rule_id` column on `audit_logs`; a rule-citation enforcement layer. None of these are in v1 scope.

## Open questions

1. **Does LE31 v2 ever introduce a rule-citing-audit surface?** Today: no signal. The default answer is *no* unless owner-facing rule-authoring pain surfaces.
2. **Is the *every-act-cites-the-rule* discipline better than the *implicit-rule-via-event-type* discipline for any specific v2 surface?** The honest answer is *probably not for v1* — v1's append-only posture is structurally aligned with the cook's confirmation-as-event model. The discipline is a *v2 question*, not a v1 question.
3. **Is the Bali `awig-awig` / `subak` cultural metaphor a useful named-pattern for v2 owner-facing documentation?** The cultural precedent is a *novelty signal*, not a *demand signal*. Owner decision required before any v2 surface references the Bali metaphor in user-facing UI text.

## Why this matters

The Bali `awig-awig` / `subak` named-pattern vocabulary is the *highest-novelty cultural-architectural-precedent* of any in-window cross-section signal in 2026 (Balinese *subak* irrigation councils are governed by *awig-awig* = village constitutions written down; the GitHub repo uses this as a metaphor for AI governance). For LE31 v1, the implication is *none*. For LE31 v2, the implication is *the rule-citing-audit primitive is mapped, and the Bali cultural precedent is available as a v2 documentation vocabulary*. **No build today.**

## Cross-section (vs the prior 35-pick cluster)

- Feature 137 (NL-to-Executable-Obligations, policy compilation) — *upstream* of AWIG-OS (rules are compiled before they are cited).
- Feature 138 (ICI nine-node continuity) — *peer* (same architectural-vocabulary layer).
- Feature 141 (KRINEIA five-invariants) — *peer* (same architectural-vocabulary layer).
- Feature 152 (LATTICE governance-first) — *peer* (same architectural-vocabulary layer; governance-first inversion is the *closest* peer).
- Feature 150 (Mandato protocol-level digitally-signed mandates) — *peer* (the signed mandate is the *rule citation* that authorizes the action).
- Feature 154 (chronology-protocol post-quantum OpenTimestamps anchoring) — *downstream* (the cryptographic anchoring is a *hardening step* applied to the rule-citing audit log).

The *transferable insight* is **the rule-citation-as-first-class-element-of-the-audit-log-entry** — a step further than features 137/138/141/152 because it adds the **rule citation as a first-class field**, not as a separately-managed upstream step.