# HANDOFF — 141-krineia-five-invariants-append-only-audit-proof

**Status**: defer (parking-lot, watch-list, architecture-reference, no build today)
**Date**: 2026-09-04
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/141-krineia-five-invariants-append-only-audit-proof.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no v2 surface that needs the five-invariant vocabulary today; LE31 v1 meets all five KRINEIA invariants vacuously or structurally by charter §3.1 + §3.4 + Postgres transactional constraints. The value of KRINEIA today is *vocabulary*, not *implementation*.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the KRINEIA paper (OpenAlex `W7203539524` / `W7203537535`, Zenodo `10.5281/zenodo.21957892` / `10.5281/zenodo.21957891`, *Append-Only as Proof: A Formal Account of Governance Sovereignty in AI Audit Systems* by Reuben Bowlby, 2026-08-15) as a dated, in-window **architectural-vocabulary reference** for the next time LE31 proposes a v2 surface that needs to ask *which of the five KRINEIA invariants does this surface need to preserve?*

If the trigger condition (LE31 first proposes a v2 surface that needs the five-invariant vocabulary — most likely a v2 owner-facing audit-trail surface, a v2-AI surface that consults `audit_logs`, or a v2 surface that introduces a second stakeholder like a reviewer or auditor) is met, the external coding agent should:

1. Load this artifact and the parent brainstorm report (`/opt/data/le31-brainstorm-2026-09-04.md`).
2. Load the KRINEIA paper (parent-fetched 2026-09-04; `abstract_inverted_index` reconstructed from raw JSON, do NOT trust any prose summary of the paper).
3. Load the companion features 121 / 122 / 129 / 133 / 134 / 135 / 136 / 137 / 138 (ripgrep-verified distinct) — KRINEIA is the *envelope* around all of them.
5. Re-run the LE31 feature gate with the KRINEIA five-invariant vocabulary in hand.
6. **Decide which of the five invariants the new v2 surface needs to preserve**. Use the matrix in the parent feature 141 (`Description` section) as the starting checklist.
7. **For v2-AI surfaces**: explicitly check `no reward-path self-reference`. If the proposed v2-AI surface consults `audit_logs` while generating a recommendation, this invariant must be checked before the surface is approved.
8. **For v2 owner-facing audit-trail surfaces**: explicitly check `external analysis only`. The owner-as-auditor read path must be distinguishable from the owner-as-operator read path.
9. **For v2 surfaces with a second stakeholder**: explicitly check `trust-root separation`. The trust root that signs rows must not be the same identity as the trust root that reads them.
10. **Pilot on one surface first**. Do not try to satisfy all five invariants on every v2 surface at once.
11. **Document the per-invariant verdict** in the surface's feature contract.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/141-krineia-five-invariants-append-only-audit-proof.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-09-04.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-09-04/openalex/append-only-AND---audit-OR-ledger--.json` (KRINEIA papers at `W7203539524` and `W7203537535`).
- **KRINEIA paper**: Zenodo `10.5281/zenodo.21957892` / OpenAlex `W7203539524` (parent-fetched 2026-09-04; `abstract_inverted_index` reconstructed by parent).
- **Companion artifacts**:
  - `features/121-ledger-commitment-field-tier-minimization.md` (Field-Tier Minimization — *what is committed*)
  - `features/122-trace-integrity-cait-acceptance-criterion.md` (Trace Integrity CAIT — *what is queried*)
  - `features/129-ledger-claim-to-evidence-trace-graph-audit.md` (LEDGER Trace Graph — *what edges*)
  - `features/133-hansard-runtime-witnessing-ledger-architecture.md` (HANSARD — *who witnessed*)
  - `features/134-echo-auditable-memory-plane-stockentry-audit.md` (ECHO — *record shape*)
  - `features/135-dreamledger-execution-settled-credit-ledger-architecture.md` (DreamLedger — credit ledger dual)
  - `features/136-memguard-verifier-signals-lifecycle-metadata-stockentry-audit.md` (MemGuard — verifier signals)
  - `features/137-natural-language-policies-executable-obligations-verification-harness.md` (NL-to-Executable-Obligations — policy compilation)
  - `features/138-institutional-continuity-infrastructure-formal-model.md` (ICI — nine-node model)
- **Charter §3.1 (append-only ledger)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.4 (no customer-facing AI)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 append-only, §3.4 observable evidence, §3.4.4 the non-technical owner).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on academic paper verification (reconstruct `abstract_inverted_index` from raw JSON, never trust prose summaries).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The vocabulary surfaced by this defer is:

- **Proof/record distinction**: a row is a record if it can be edited to document a different claim; a row is a proof if any change is detectable from outside.
- **Five KRINEIA invariants** (named acronym: keep — reward-path self-reference — inspect — external — audit; or whatever the LE31 owner prefers — the paper uses KRINEIA but the acronym etymology is not stated):
  1. **append-only** — no row is updated or deleted; corrections are new rows.
  2. **no reward-path self-reference** — an AI agent that scores its own reward cannot read the log it generates to score itself.
  3. **minimal operators** — the set of roles that can write rows is the smallest set that satisfies the operational requirement.
  4. **external analysis only** — the analyst of the log is not the producer; reading-as-auditor is distinct from reading-as-operator.
  5. **trust-root separation** — the trust root that signs rows is not the same identity as the trust root that reads them.

LE31 v1 doesn't have a v2 surface that needs this vocabulary today. The defer artifact does **not** propose a `KRINEIA` check function or a `proof/record` flag. It surfaces the *vocabulary* for future use.

## Rollback path

This is a documentation-only artifact. There is no code to roll back. If the LE31 owner decides the vocabulary is not worth carrying, the file can be deleted with no operational impact.

## Verification protocol reference

For the LE31 seven-check feature gate, see `skills/le31-conventions/SKILL.md` §"Feature gate". For academic paper verification, see `skills/le31-research/SKILL.md` (always reconstruct `abstract_inverted_index` from raw JSON, never trust prose summaries — the 2026-08-28 subagent fabrication incident is the reference failure mode).