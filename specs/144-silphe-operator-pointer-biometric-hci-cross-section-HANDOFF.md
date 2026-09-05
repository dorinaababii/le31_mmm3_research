# HANDOFF — 144-silphe-operator-pointer-biometric-hci-cross-section

**Status**: defer (parking-lot, watch-list, operator-UX research-note, no build today)
**Date**: 2026-09-05
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/144-silphe-operator-pointer-biometric-hci-cross-section.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no operator-identity-at-the-workstation surface today; the value of silphe today is *vocabulary*, not *implementation*).

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the silphe repo (GitHub `martymcenroe/silphe`, 3★/0 forks, Apache-2.0, Python, pushed 2026-09-01T00:18:06Z, in-window by push only) as a dated, in-window **architectural-vocabulary reference** for the next time LE31 proposes a v2 owner-facing audit-trail surface that needs to verify *which operator was at the workstation when a `StockEntry` row was written* without violating charter §3.2 (privacy: counts not identity).

If the trigger condition (LE31 first proposes a v2 owner-facing audit-trail surface that needs operator-identity-at-the-workstation verification — most likely a v2 owner-facing reconciliation surface, a v2 surface that wants to verify *"the same person who closed last night's shift also opened tonight's shift"*, or a v2 surface that introduces a second stakeholder like a reviewer or auditor) is met, the external coding agent should:

1. Load this artifact and the parent brainstorm report (`/opt/data/le31-brainstorm-2026-09-05.md`).
2. Load the silphe repo (parent-fetched 2026-09-05; do NOT trust any prose summary of the library — re-read the README directly from the GitHub repository before adopting).
3. Load the companion features 130 / 131 / 134 / 135 / 141 (ripgrep-verified distinct) — silphe is the *operator-identity primitive* that complements the *record-architecture primitives* in those features.
4. Re-run the LE31 feature gate with the silphe primitive in hand.
5. **Decide whether the new v2 surface needs operator-identity verification**. Use the matrix in the parent feature 144 (`Description` section) as the starting checklist.
6. **For v2 owner-facing audit-trail surfaces**: explicitly check whether the existing `actor_user_id` + `actor_role` provenance satisfies the same JTBD more cheaply. The silphe primitive's value emerges only when the operator is *not* explicitly logged in (e.g., a shared terminal).
7. **For v2 surfaces with a second stakeholder**: explicitly check whether the operator signature is needed for the *second-stakeholder* read path (e.g., the auditor asking *"who was at the workstation when this `StockEntry` row was written?"*).
8. **Pilot on one surface first**. Do not try to instrument every operator action with silphe at once.
9. **Document the per-surface decision** in the surface's feature contract.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/144-silphe-operator-pointer-biometric-hci-cross-section.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-09-05.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-09-05/gh_topic_hci.json` (silphe repo at index position verified by parent).
- **Silphe repo**: GitHub `martymcenroe/silphe` (parent-fetched 2026-09-05; description field re-verified by parent against raw JSON).
- **Companion artifacts**:
  - `features/130-dhh-kitchen-accessible-operator-ux-visual-replayable.md` (DHH-restaurant paper — *operator-accessibility*)
  - `features/131-puntovivo-fiscal-native-local-first-pos-cross-section.md` (PuntoVivo — *statutory fiscal identity*)
  - `features/134-echo-auditable-memory-plane-stockentry-audit.md` (ECHO — *record shape*)
  - `features/135-dreamledger-execution-settled-credit-ledger-architecture.md` (DreamLedger — *credit ledger dual*)
  - `features/141-krineia-five-invariants-append-only-audit-proof.md` (KRINEIA — *proof/record distinction + trust-root separation*)
- **Charter §3.1 (mobile-responsive waiter UI)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.2 (privacy: counts not identity)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 append-only, §3.2 privacy, §3.4 observable evidence).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repository verification (re-read the README directly from the repo, never trust prose summaries).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The vocabulary surfaced by this defer is:

- **Local-only pointer-movement biometric quantifier**: the silphe library generates a signature from the operator's pointer-movement data on the workstation; the signature *changes with the operator* and is computed *locally*, never sent off-device.
- **Operator-identity primitive**: the signature is a privacy-friendly operator-identity primitive — the owner can verify *"the same person who closed last night's shift also opened tonight's shift"* by comparing signatures, without storing PII.
- **Trust-root separation invariant contribution**: the signature is the *trust root* for the operator's actions; the operator's workstation is the *signing identity*; the audit_logs read path is the *verifying identity*.

LE31 v1 doesn't have a v2 surface that needs this primitive today. The defer artifact does **not** propose a `silphe` integration or an `operator_signature` column. It surfaces the *primitive* for future use.

## Rollback path

This is a documentation-only artifact. There is no code to roll back. If the LE31 owner decides the primitive is not worth carrying, the file can be deleted with no operational impact.

## Verification protocol reference

For the LE31 seven-check feature gate, see `skills/le31-conventions/SKILL.md` §"Feature gate". For GitHub repository verification, see `skills/le31-research/SKILL.md` (always re-read the README directly from the repository, never trust prose summaries — the 2026-08-28 subagent fabrication incident is the reference failure mode).