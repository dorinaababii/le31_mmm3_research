# HANDOFF — 138-institutional-continuity-infrastructure-formal-model

**Status**: defer (watch-list architecture reference, no build today)
**Date**: 2026-08-30
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/138-institutional-continuity-infrastructure-formal-model.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no v2 surface that asks "is institutional continuity maintained?"; charter §3.1 already enforces append-only at the operational layer; ICI is the formal envelope for a future v2 surface)

## Trigger policy

This is a **defer artifact** — a watch-list entry. It does not start a build. It surfaces the ICI paper (OpenAlex `W7204524067` / DOI `10.5281/zenodo.22135314`, 2026-08-28, Zenodo) as a dated, in-window architectural reference for the next time LE31 considers a v2 surface that needs to verify "institutional continuity" not just "operational correctness".

If the trigger condition (LE31 first proposes a v2 surface that asks "is this chain still connected to the institutional meaning from which authority was claimed?") is met, the external coding agent should:

1. Load this artifact and the linked ICI paper.
2. Load the companion feature 129 (LEDGER Claim-to-Evidence Trace Graphs), feature 133 (HANSARD Runtime Witnessing), feature 134 (ECHO Auditable Memory Plane), feature 121 (Field-Tier Minimization), feature 122 (Trace Integrity CAIT), feature 137 (NL-to-Executable-Obligations) — the ICI envelope is the *vocabulary* layer that names what those features implement.
3. Re-run the LE31 feature gate with the ICI paper in hand.
4. **Enumerate the joins** the surface needs. For LE31's `StockEntry` lifecycle, the natural joins are: `source (order event) → exact_action (StockEntry row) → consequence (derived current stock) → reconciliation (end-of-shift closing)`.
5. **Define the per-join predicates**. The ICI paper's `non-compensatory join-status algebra` says each predicate must be independently testable. Define each predicate explicitly.
6. **Define the three authority planes** the surface needs. For LE31: *institutional* (charter §3), *runtime* (the Python process), *observational* (the nightly close or owner's manual review).
7. **Decide what "broken join" means** for the surface. ICI says broken joins cannot be compensated; LE31 must decide whether a broken join blocks the action or is logged as a `correction`.
8. **Pilot on one join first**. Do not design the full nine-node envelope for all joins at once.
9. **Skip the exhaustive conformance checker** (the paper's 5,764,801-status-vector checker is a research artefact, not a v1 or v2 LE31 feature).

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/138-institutional-continuity-infrastructure-formal-model.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-08-30.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-08-30/openalex/abstract_W7204524067.json` (full abstract reconstructed by parent from `abstract_inverted_index`)
- **Companion artifacts**:
  - `features/121-ledger-commitment-field-tier-minimization.md` (*what is committed*)
  - `features/122-trace-integrity-cait-acceptance-criterion.md` (*what is queried*)
  - `features/129-ledger-claim-to-evidence-trace-graph-audit.md` (*what edges*)
  - `features/133-hansard-runtime-witnessing-ledger-architecture.md` (*who witnessed*)
  - `features/134-echo-auditable-memory-plane-stockentry-audit.md` (*record shape*)
  - `features/137-natural-language-policies-executable-obligations-verification-harness.md` (*policy compilation*)
- **Charter §3.1 (append-only ledger)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.4 (no customer-facing AI)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 append-only, §3.4 observable evidence).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on arXiv/OpenAlex/Zenodo verification.

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The architectural primitive surfaced by this defer is:

- **Institutional Continuity Infrastructure (ICI)** — a typed nine-node continuity model with eight independently testable joins, three non-interchangeable authority planes, a non-compensatory join-status algebra, exact-action binding, independent consequence coverage, and append-only correction. The central result: *"institutional continuity is not established by correctness at any single link"*.

LE31 v1 has no v2 surface that needs this primitive today. The defer artifact does **not** propose a `ContinuityCheck` table or a per-join predicate table. It surfaces the *naming* + *vocabulary* for future use.

When the defer is promoted to build, the future v2 surface would:

- Enumerate the joins it needs.
- Define a per-join predicate for each join.
- Implement the three authority planes.
- Decide what "broken join" means for the surface.
- Pilot on one join first.

## Files to touch (when defer is promoted to build)

None today. When the defer is promoted:

- `backend/app/models/audit_logs.py` — possibly add a `join_evaluations` related table or a per-join predicate column on `audit_logs`. *Not before the defer is promoted.*
- New module (e.g., `backend/app/services/continuity_check.py`) for the per-join predicate evaluator. *Not before the defer is promoted.*
- `features/<NN>-<new-slug>.md` — the build-time feature contract, derived from this defer artifact and the trigger conditions.

## Rollback path

Fully reversible. Filing as a defer artifact does not change any schema, any code, any surface. If the trigger condition is never met, this artifact can be archived without consequence. If the trigger condition is met and the build is rejected, the defer artifact remains in the watch-list for re-evaluation.

## Open questions carried forward

- **Which joins does LE31 v2 actually need?** The ICI paper enumerates all nine nodes; LE31's `StockEntry` lifecycle has at most 4–5 of those joins naturally.
- **What does "broken join" mean for LE31?** Block action, raise warning, or silently log?
- **Who runs the conformance checker?** The paper's exhaustive 5,764,801-vector checker is a research artefact, not a LE31 feature. Minimum viable equivalent is per-join predicates at reconciliation time.
- **How does ICI interact with feature 137's policy-as-input posture?** If LE31 ever allows owner-authored rules, each rule creates new joins. ICI is the natural verification envelope.

## Verification protocol reference

When the defer is promoted to build:

1. Re-run `le31-conventions`'s seven-check feature gate with the ICI paper in hand.
2. Enumerate the joins the new surface needs.
3. Implement per-join predicates.
4. Test: for each join, perturb the upstream and verify the predicate fails (RED).
5. Test: for each join, restore the upstream and verify the predicate passes (GREEN).
6. Test: for each join, perturb a non-adjacent join and verify the predicate still passes (proves non-compensatory algebra).
7. Test: at the surface level, exercise the v2 surface with all 8 joins passing and observe correct behavior.

## Companion artifacts (cross-references)

- Feature 121 (Field-Tier Minimization) — *what is committed*.
- Feature 122 (Trace Integrity CAIT) — *what is queried*.
- Feature 129 (LEDGER Claim-to-Evidence Trace Graphs) — *what edges*.
- Feature 133 (HANSARD Runtime Witnessing) — *who witnessed*.
- Feature 134 (ECHO Auditable Memory Plane) — *record shape*.
- Feature 137 (NL-to-Executable-Obligations) — *policy compilation*.

## Why this matters (one-line)

The ICI paper is the **formal envelope** that names what features 121, 122, 129, 133, 134, 137 implement in LE31-adjacent vocabulary; the central result — *"institutional continuity is not established by correctness at any single link"* — is the formalised version of charter §3.1's append-only posture, and the v2 surface that asks the continuity question will need this vocabulary when it is proposed.
