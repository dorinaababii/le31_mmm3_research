# Feature 138 — Institutional Continuity Infrastructure (ICI) formal model (defer)

> **NEW observation (2026-08-30).** Documents in-window OpenAlex paper `W7204524067` / DOI `10.5281/zenodo.22135314` *Institutional Continuity Infrastructure: A Formal Model from Governing Meaning to Provable Machine Consequence* (Zenodo, 2026-08-28) from the 2026-08-30 daily-brainstorm pass. The paper defines a typed nine-node continuity model with eight independently testable joins spanning source, admitted meaning, warranted control, runtime authority, exact action, consequence, independent observation, reconciliation, and examination. It formalises three non-interchangeable authority planes, a non-compensatory join-status algebra, exact-action binding, independent consequence coverage, and **append-only correction**. A bounded executable conformance checker exhaustively evaluates all **5,764,801 possible eight-join status vectors** and uses mutation discrimination to test implementation conformance. Bucket: **v2 owner-pains (architecture reference)** — watch-list defer. Zero build time today.

## Goal

Retain the **nine-node continuity model + eight independently testable joins + non-compensatory join-status algebra** as the architectural-vocabulary reference for the first LE31 v2 surface that asks *"is institutional continuity maintained?"* — i.e., for the v2 surface that needs to reason about whether a chain of LE31 actions still connects to the institutional meaning from which authority was claimed.

The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the ICI model: nine nodes, eight joins, three authority planes, append-only correction.
- A decision record: today's verdict is `defer` because LE31 v1 has no v2 surface that asks "is institutional continuity maintained?" — the v1 answer is "yes, by charter §3.1 append-only".
- A reference for the next time LE31 proposes a v2 surface that wants to verify *institutional continuity* not just *operational correctness*.
- The central result of the paper: *"institutional continuity is not established by correctness at any single link"* — formalised version of LE31's append-only posture.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any change to the `audit_logs` schema.
- Any user-facing "institutional continuity" surface (no owner-facing query today).
- The 5,764,801-status-vector exhaustive conformance checker — it would be an order of magnitude of work to instantiate against LE31's state transitions and is not a v1 or v2 LE31 feature.

## Description

OpenAlex `W7204524067` / Zenodo `10.5281/zenodo.22135314` — *Institutional Continuity Infrastructure (ICI)* — defines a **typed nine-node continuity model** that formalises what it means for a machine consequence to remain continuously connected to the institutional meaning from which authority is claimed. The model's nine nodes are:

1. **Source** — the originating institutional record.
2. **Admitted meaning** — what the source is interpreted to mean.
3. **Warranted control** — who is authorised to act on it.
4. **Runtime authority** — the runtime that actually acts.
5. **Exact action** — the specific action taken.
6. **Consequence** — the recorded outcome.
7. **Independent observation** — an external record of the consequence.
8. **Reconciliation** — the cross-check between consequence and observation.
9. **Examination** — the join-by-join mechanism to detect and record any change.

The model defines **eight independently testable joins** between consecutive nodes, **three non-interchangeable authority planes** (institutional, runtime, observational), and a **non-compensatory join-status algebra** — meaning that a broken join cannot be "fixed" by strengthening an adjacent join; each join must independently satisfy its predicate. The model also specifies **exact-action binding** (the exact bytes of the action are committed), **independent consequence coverage** (the consequence is observed by something other than the actor), and **append-only correction** (corrections are recorded as new entries, not edits).

The bounded executable conformance checker exhaustively evaluates all 5,764,801 possible eight-join status vectors and uses mutation discrimination to test implementation conformance to the specified aggregation algebra. Six propositions are stated with proof sketches. The central result is deliberately bounded:

> *"Institutional continuity is not established by correctness at any single link. It requires an unbroken, independently examinable witness path across every mandatory join under explicit materiality, configuration, and disposition assumptions, plus a join-by-join mechanism to detect and record any change. Without that path, an organisation cannot recover its institutional reasoning from the record it kept, regardless of how perfect the audit log looks in isolation."*

**Cross-section with LE31 charter §3.1** (append-only posture):
- LE31's `StockEntry` ledger + `audit_logs` give the **source → exact-action → consequence → reconciliation** chain for the operational lifecycle of every prepared-item quantity change.
- The ICI nine-node model is *strictly additive* over the existing `audit_logs` shape — it does not require any schema change to v1; it requires the v2 surface that asks "is institutional continuity maintained?" to *enumerate which joins it needs to verify*, and to verify them independently rather than via compensating controls.
- The ICI central result is the formalised version of charter §3.1's append-only posture: a "perfect audit log" is necessary but not sufficient; what matters is the join-by-join witness path that lets a reviewer recover the chain.

**Cross-section with prior picks**:
- **Feature 121 Field-Tier Minimization** (2026-08-27) — *"what is committed is canonical even if later reclassified"*. ICI is the *formal envelope* around feature 121's principle: feature 121 says the commitment persists; ICI says the joins across the commitment must be independently testable.
- **Feature 122 Trace Integrity CAIT** (2026-08-27) — *"what is queried is the right answer"*. ICI is the *upstream* of feature 122's measurement: feature 122 measures the answer; ICI verifies the joins that *produced* the answer.
- **Feature 129 LEDGER Claim-to-Evidence Trace Graphs** (2026-08-28) — *"what's the typed edge from a derived figure back to the rows that produced it?"*. ICI is the *vocabulary layer* of feature 129: feature 129 names the edges; ICI names the nodes and the join predicates.
- **Feature 133 HANSARD Runtime Witnessing** (2026-08-29) and **Feature 134 ECHO Auditable Memory Plane** (2026-08-29) — HANSARD = runtime witnessing; ECHO = record-shape primitive. ICI = the formal envelope that names why both are necessary.

LE31 v1 currently has no v2 surface that asks "is institutional continuity maintained?" — the answer for v1 is "yes, by charter §3.1 append-only". The value of ICI today is *vocabulary*, not *implementation*. The paper provides LE31 with the terms (`nine-node`, `eight joins`, `three authority planes`, `non-compensatory join-status algebra`, `append-only correction`) to use when the next v2 surface is proposed.

## Data model

No schema change today. The defer artifact documents that the future ICI-instantiation would have:

- The existing `StockEntry` and `audit_logs` tables remain the source of truth for `source`, `exact-action`, and `consequence`.
- The future v2 surface that asks "is institutional continuity maintained?" would *enumerate the joins* it needs (e.g., `warranted_control → runtime_authority`, `consequence → independent_observation`) and implement *per-join predicates*.
- The `non-compensatory join-status algebra` is a design constraint: a broken join cannot be fixed by strengthening an adjacent join. Each join must satisfy its predicate independently.

## Implementation steps

None today (defer). When LE31 first proposes a v2 surface that asks "is institutional continuity maintained?":

1. **Re-run the LE31 feature gate** with the ICI paper in hand.
2. **Enumerate the joins** the surface needs. For LE31's `StockEntry` lifecycle, the joins are likely: `source (order event) → exact_action (StockEntry row) → consequence (derived current stock) → reconciliation (end-of-shift closing)`.
3. **Define the per-join predicates**. The ICI paper's `non-compensatory join-status algebra` says each predicate must be independently testable. The predicate for `source → exact_action` might be "the order event ID exists and is the most recent un-superseded event for this prepared-item"; the predicate for `exact_action → consequence` might be "the current derived stock equals the sum of all `StockEntry` rows for this prepared-item since the last reconciliation".
4. **Define the three authority planes** the surface needs. For LE31, the planes are likely: *institutional* (charter §3 mandates), *runtime* (the Python process), *observational* (the nightly close or owner's manual review).
5. **Decide what "broken join" means for the surface**. ICI says broken joins cannot be compensated; LE31 must decide whether a broken join blocks the action or is logged as a `correction`.
6. **Pilot on one join first**. Do not design the full nine-node envelope for all joins at once.

## Dependencies

- Charter §3.1 (append-only posture) — ICI is strictly additive over `audit_logs`.
- Charter §3.4 (no customer-facing AI) — ICI surfaces are owner/staff, not diner.
- Feature 121 Field-Tier Minimization — companion: *what is committed* (feature 121) + *what is queried* (feature 122) + *what is joined* (this feature, ICI).
- Feature 122 Trace Integrity CAIT — companion: CAIT measures the answer; ICI verifies the joins.
- Feature 129 LEDGER Claim-to-Evidence Trace Graphs — companion: LEDGER names the edges; ICI names the nodes and the join predicates.
- Feature 133 HANSARD Runtime Witnessing — companion: HANSARD = runtime witnessing; ICI = formal envelope.
- Feature 134 ECHO Auditable Memory Plane — companion: ECHO = record shape; ICI = join verification.
- Feature 137 NL-to-Executable-Obligations — surface where ICI joins would be most natural: the policy → typed-rule → deterministic-obligation pipeline needs join-by-join verification.

## Open questions

- **Which joins does LE31 v2 actually need?** The ICI paper enumerates all nine nodes and all eight joins. LE31's `StockEntry` lifecycle has at most 4–5 of those joins naturally; the others are speculative. The "smallest ICI surface that helps" is an open question.
- **What does "broken join" mean?** ICI says broken joins cannot be compensated; LE31 must decide whether a broken join blocks the action, raises a warning, or is silently logged.
- **Who runs the conformance checker?** The paper's exhaustive 5,764,801-vector checker is a research artefact, not a v1 or v2 LE31 feature. The minimum viable LE31 equivalent is per-join predicates run at reconciliation time, not an exhaustive state-space search.
- **How does ICI interact with feature 137's policy-as-input posture?** If LE31 ever allows owner-authored rules (feature 137), each rule creates new joins (admitted meaning → warranted control → exact action). ICI is the natural verification envelope for those new joins.

## Why this matters

The paper provides LE31 with three things it does not currently have: (i) **architectural vocabulary** for "institutional continuity" as a measurable primitive; (ii) **a non-compensatory algebra** that formalises why "perfect audit log" is not enough; (iii) **a dated reference** for the next time LE31 proposes a v2 surface that asks "is this chain still connected to the institutional meaning from which authority was claimed?". The cost of *not* filing this today is the risk that the first v2 surface that asks the continuity question reinvents the vocabulary from scratch, or shorts the question entirely. Filed now so the v2 boundary has the vocabulary ready when the surface is proposed.

**Fully reversible.** Filing as a defer artifact does not commit to any schema change or any v2 work.
