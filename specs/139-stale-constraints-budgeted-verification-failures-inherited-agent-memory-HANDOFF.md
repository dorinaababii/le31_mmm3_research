# HANDOFF — 139-stale-constraints-budgeted-verification-failures-inherited-agent-memory

**Status**: defer (watch-list architecture reference + empirical evidence, no build today)
**Date**: 2026-08-30
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/139-stale-constraints-budgeted-verification-failures-inherited-agent-memory.md`
**LE31 feature gate verdict**: defer (LE31 v1 doesn't ask operators to verify provenance; the value of this paper today is *evidence that the shape of the appended row matters*, not *implementation*)

## Trigger policy

This is a **defer artifact** — a watch-list entry. It does not start a build. It surfaces the Nakayashiki paper (OpenAlex `W7204257200` / DOI `10.5281/zenodo.22147784`, v3, 2026-08-28, Zenodo) as a dated, in-window empirical-evidence reference for the next time LE31 proposes a v2 surface where the operator (or an LLM assistant) is asked to re-verify a record.

If the trigger condition (LE31 first proposes a v2 surface where the operator must re-verify a `StockEntry`, a `Bill`, a `Visit`, or a `Shift`) is met, the external coding agent should:

1. Load this artifact and the linked paper.
2. Load the companion feature 121 (Field-Tier Minimization), feature 122 (Trace Integrity CAIT), feature 129 (LEDGER Claim-to-Evidence Trace Graphs), feature 137 (NL-to-Executable-Obligations) — this paper is the *operational-budget dual* of those features.
3. Re-run the LE31 feature gate with this paper in hand.
4. **Measure LE31's operator verification budget first**. The paper uses 2 records; LE31's operator budget is unknown. The first step is to measure how many `StockEntry` rows the operator actually reads before deciding.
5. **Identify which `StockEntry` shapes "state a limit on a candidate direction"**. The paper's target-blind rule is *"prefer memories that state a limit on a candidate direction"*. For LE31 v1's `StockEntry` lifecycle, the candidate actions are: reorder, sell, write-off, transfer. Rows that *constrain* one of these actions are the ones the rule would surface.
6. **Decide whether the shape signal is implicit** (the row's amount + item combination implicitly blocks reorder when amount ≤ threshold) **or explicit** (a new `candidates_blocked` field). The implicit form may already exist in v1's row shape.
7. **Pilot on one shape signal first**. Do not add multiple shape signals at once.
8. **Measure the empirical baseline** — the paper documents ~75% stale-consistent decisions; LE31 should measure its own baseline before adding any intervention.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/139-stale-constraints-budgeted-verification-failures-inherited-agent-memory.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-08-30.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-08-30/openalex/abstract_W7204257200.json` (full abstract reconstructed by parent from `abstract_inverted_index`, 600+ word entries)
- **Companion artifacts**:
  - `features/121-ledger-commitment-field-tier-minimization.md` (*what is committed*)
  - `features/122-trace-integrity-cait-acceptance-criterion.md` (*what is queried*)
  - `features/129-ledger-claim-to-evidence-trace-graph-audit.md` (*what edges*)
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

The empirical finding surfaced by this defer is:

- **The verification-budget finding**: when an agent has a verification budget of 2 records and a constraint that has been superseded, **stale-consistent decisions are produced in ~75% of episodes** (77.3% / 74.7% / 74.7% across primary / replication / held-out).
- **The shape-of-row lesson**: the *shape* of the row determines whether the constraint stands out at look-up time. A row that "states a limit on a candidate direction" (e.g., "remaining: ≤ 3 portions", "reorder by: Friday") out-performs a row with no such signal.
- **The target-blind rule**: *"prefer memories that state a limit on a candidate direction"* — recovers **+89.3 points** accuracy without experimenter knowledge of the critical path.

LE31 v1 doesn't ask operators to verify provenance today. The defer artifact does **not** propose a `candidates_blocked` field or any schema change. It surfaces the *empirical baseline* + *shape-of-row lesson* for future use.

When the defer is promoted to build, the future v2 surface would:

- Measure the operator verification budget (likely ≤ 3 rows per decision).
- Identify which `StockEntry` shapes "state a limit on a candidate direction".
- Decide implicit vs explicit shape signal.
- Pilot on one shape signal first.
- Measure the empirical baseline before adding any intervention.

## Files to touch (when defer is promoted to build)

None today. When the defer is promoted:

- `backend/app/models/stockentry.py` — possibly add a `candidates_blocked` text column or a derived view. *Not before the defer is promoted.*
- New module (e.g., `backend/app/services/operator_budget.py`) for measuring the operator verification budget. *Not before the defer is promoted.*
- `features/<NN>-<new-slug>.md` — the build-time feature contract, derived from this defer artifact and the trigger conditions.

## Rollback path

Fully reversible. Filing as a defer artifact does not change any schema, any code, any surface. If the trigger condition is never met, this artifact can be archived without consequence. If the trigger condition is met and the build is rejected, the defer artifact remains in the watch-list for re-evaluation.

## Open questions carried forward

- **What is LE31's operator verification budget?** The paper uses 2 records; LE31's operator budget is unknown. **The first step is to measure it.**
- **Should the shape signal be implicit or explicit?** Implicit may already be present in v1's row shape; explicit adds a schema column.
- **Does the shape signal apply to v1's existing `StockEntry` rows?** v1 already has `amount` + `item` — the implicit shape signal may already be present.
- **What is the cost of being wrong about the shape signal?** The paper claims +89.3 points, not 100 points. The shape signal is a *bias*, not a guarantee.
- **Is "limit on a candidate direction" universal for LE31?** Candidates are: reorder, sell, write-off, transfer. Other candidates?

## Verification protocol reference

When the defer is promoted to build:

1. Re-run `le31-conventions`'s seven-check feature gate with this paper in hand.
2. Measure the operator verification budget (count how many `StockEntry` rows the operator reads before deciding).
3. Identify candidate-direction shapes in v1's existing `StockEntry` rows.
4. Test (RED): perturb a row to remove its candidate-direction shape and verify the operator reads fewer subsequent rows.
5. Test (GREEN): restore the shape and verify the operator reads more subsequent rows.
6. Measure: replicate the paper's experimental design on LE31's `StockEntry` rows to measure LE31's specific baseline (the paper reports ~75% stale-consistent; LE31 may be different).

## Companion artifacts (cross-references)

- Feature 121 (Field-Tier Minimization) — *what is committed*. The paper is the operational-budget dual: feature 121 says the commitment persists; the paper says the commitment *stands out* only if its shape signals a limit.
- Feature 122 (Trace Integrity CAIT) — *what is queried*. The paper is the upstream: feature 122 measures the answer; the paper measures whether the constraint gets read.
- Feature 129 (LEDGER Claim-to-Evidence Trace Graphs) — *what edges*. The paper says typed edges are not enough either; the reader's budget is the binding constraint.
- Feature 137 (NL-to-Executable-Obligations) — *policy compilation*. Even with compiled rules, the operator's verification budget is the binding constraint.

## Why this matters (one-line)

The Nakayashiki paper is the **first empirical evidence in the 31-pass series** that the `audit_logs` shape itself is a design surface, not a passive record — append-only provenance is not enough; the *shape* of the appended row determines whether the constraint stands out at look-up time, and a target-blind rule recovers **+89.3 points** accuracy when the budget is binding.

## AI-assistance disclosure note

The paper's author disclosed AI assistance (Anthropic's Claude + OpenAI's ChatGPT) for design/execution tooling, with the 16 models studied as experimental subjects (not co-authors). Same epistemic posture as the HANSARD / ECHO picks (2026-08-29). The AI assistance is **disclosed in the paper's back matter**, and the data + code are deposited at OSF (project `axsnm`) with frozen analysis outputs. No fabrication concern; this is reproducible research.
