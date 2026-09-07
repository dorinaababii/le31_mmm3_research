# Feature 152 — LATTICE governance-first authorized-autonomous-AI architecture cross-section (defer)

> **NEW observation (2026-09-07).** Documents in-window peer-reviewed article `doi:10.3389/frai.2026.1800407` (2026-08-14, **3 citations**, Elias Calboreanu, type=article, primary location: *Frontiers in Artificial Intelligence*, peer-reviewed). Title (verbatim): *"LATTICE: a governance-first architecture for authorized autonomous AI operations."* **First surface of this paper in the 36-pass brainstorm series** (parent-verified by ripgrep against all features 1–149 + all brainstorm reports 2026-08-04..2026-09-06). Bucket: **v2 owner-pains (architecture-reference, parking-lot defer)** — watch-list entry, zero build time today. **The peer-reviewed venue distinguishes this from the in-window Zenodo / arXiv preprints** (features 92 / 134 / 137 / 141 / 150 / 151 are all preprints).

## Goal

Retain the **"governance-first"** architectural primitive as the **transferable insight** for any future LE31 v2 owner-facing audit surface where the *governance contract* is the primary surface and *operational events* are constrained by it. The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the LATTICE primitive: *the governance layer is the primary architectural surface, and AI operations are constrained by the governance contract rather than the AI surface being primary with governance bolted on*.
- A decision record: today's verdict is `defer` because LE31 v1 has no governance-first surface today (the existing `audit_logs` is *operational-first* with explicit-state-disciplines).
- A cross-section reference with features 121 / 122 / 137 (the existing rules-as-code / verification-harness cluster) — the *transferable insight* is the *architectural inversion*: LE31 v1 is *operational-first with governance constraints*; LATTICE argues *governance-first with operational events constrained*. The inversion is *transferable*: any future v2 owner-facing surface where the *governance contract* (e.g., "this shift's reconciliation rules") is the *primary authoring surface* could adopt the inversion.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Adoption of any *governance-first* authoring surface in v1.
- Adoption of any *authorized-autonomous-AI* surface in v1 (charter §3.4).

## Evidence / JTBD

When a future LE31 v2 owner wants to author *shift-specific reconciliation rules* as a *primary authoring surface* (rather than author them implicitly via operational event types), the owner wants *a governance-first surface where the rules are the primary artefact and the operational events are derived from them*, but struggles because *v1 has no such surface and the operational-first posture is structurally entrenched*, so that *v2 can offer a shift-specific governance authoring surface without re-architecting v1*.

- **Evidence class**: inferred (no LE31 owner has asked for a governance-first authoring surface in 36 passes).
- **Confidence**: medium (mechanism) / low (present urgency).
- **Real observed LE31 JTBD**: none directly. The 3-citation count is a *peer-reviewed credibility signal*, not an LE31 demand.
- **The value is contingency**, not direct demand: when (if) LE31 v2 introduces an owner-facing reconciliation-rules authoring surface, the architectural primitive already exists.

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred only — no observed LE31 v1 pain; v2 surface doesn't exist. |
| 2. Viability | Mechanism is well-defined (governance contract → operational events); viability is conditional on a v2 owner-facing authoring surface. |
| 3. Practicability and confidence | Confidence: medium-high (peer-reviewed venue, 3 citations in ~24 days). Stack: no impact on v1 (which is operational-first). |
| 4. Conflict | No conflict with charter §3.1 (operational-first posture is preserved); no conflict with §3.4 (LATTICE is *authorized-autonomous-AI*, not customer-facing-AI — the boundary is the explicit authorization layer). |
| 5. Outcome, appetite, scope | v2 owner-pains (architecture-reference). Appetite: zero today. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value: medium (governance-first is a v2 authoring pattern, useful for any future rules-as-code surface). |
| 7. Circuit breaker and reversibility | Trivially reversible: written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today. Peer-reviewed venue is a *credibility signal* but not a `build` upgrade trigger.

## Implementation steps

None today. When v2 introduces any governance-first authoring surface (e.g., an owner-facing shift-reconciliation-rules editor), the *primitive* to surface is **"the governance contract is the primary authoring artefact, and operational events are derived from it"** — the v2 owner-facing surface would let the owner author *rules*, and the system would emit *operational events* (e.g., `StockEntry` rows) as derived effects of the rules. This is the architectural *inverse* of v1's operational-first posture; both are valid patterns for different surfaces.

## Dependencies

- None today.
- Future dependencies (v2 only): a governance-rule authoring surface (UI + storage); a rules-to-events derivation engine; a verification layer to confirm operational events satisfy governance rules. None of these are in v1 scope.

## Open questions

1. **Does LE31 v2 ever introduce an owner-facing reconciliation-rules authoring surface?** Today: no signal. The default answer is *no* unless owner-facing reconciliation pain surfaces.
2. **Is the *governance-first* inversion better than the *operational-first* posture for any specific v2 surface?** The honest answer is *probably not for v1* — v1's operational-first posture is structurally aligned with the cook's confirmation-as-event model. The inversion is a *v2 question*, not a v1 question.

## Why this matters

Peer-reviewed venue (*Frontiers in AI*, article type, DOI registered) is a *rare credibility signal* in the in-window cross-section pool — most of the in-window papers on the append-only / AI-agent-ledger axis are Zenodo or arXiv preprints (features 92 / 134 / 137 / 138 / 141 / 150 / 151 are all preprints). The peer-review process applied to LATTICE distinguishes its *governance-first* claim from the preprint cluster. For LE31 v1, the implication is *none*. For LE31 v2, the implication is *the governance-first primitive is mapped, and the architectural inversion is available as a v2 surface pattern*. **No build today.**
