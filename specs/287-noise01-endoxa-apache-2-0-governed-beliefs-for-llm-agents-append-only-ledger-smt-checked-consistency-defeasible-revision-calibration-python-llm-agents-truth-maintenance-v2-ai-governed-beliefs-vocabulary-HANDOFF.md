# HANDOFF — 287-noise01-endoxa-v2-ai-governed-beliefs-vocabulary

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-07
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/287-noise01-endoxa-apache-2-0-governed-beliefs-for-llm-agents-append-only-ledger-smt-checked-consistency-defeasible-revision-calibration-python-llm-agents-truth-maintenance-v2-ai-governed-beliefs-vocabulary.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; 11/11 topic-overlap = highest of 69-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window
v2-AI vocabulary reference (`noise01/endoxa`, Apache-2.0, 0★/0⑂, 811 KB modest,
Python on-stack ✓, 11/11 topic-overlap = 100% = highest single-pick topic-alignment
signal of the 69-pass series) for the next time the LE31 owner opens a v2-AI
belief-surface window.

If the trigger condition (v2-AI belief-surface window opens) is met, the
external coding agent should:

1. Read the active feature file in full.
2. Confirm the `noise01/endoxa` repo is still in-window (pushed within last 7 days
   from the trigger date) and the 11 topics are still the same.
3. Implement the `Belief` + `BeliefRevision` + `SMTConstraint` + `CalibrationLog`
   SQLModel tables as described in the active feature's Data model section.
4. Add the `z3-solver` Python dependency to `pyproject.toml`.
5. Implement the SMT-checked consistency wrapper service.
6. Run the v1 test suite + the new v2-AI belief-surface test suite.
7. Surface any test failures to the owner (LE31 v1 has no LLM agent today;
   the test suite will be green if the `Belief` table is empty, but the
   SMT-checked consistency must be verified against a non-empty belief set).
8. Verify the v1 `audit_logs` SQLModel table is untouched (the v2-AI belief
   ledger is a NEW table, not a migration of the v1 audit log).

If the trigger condition is **not** met, do nothing. The defer
artifact can be safely ignored until the owner opens a v2-AI belief-surface
window.

## Mandatory inputs

- **Active feature**: `features/287-noise01-endoxa-apache-2-0-governed-beliefs-for-llm-agents-append-only-ledger-smt-checked-consistency-defeasible-revision-calibration-python-llm-agents-truth-maintenance-v2-ai-governed-beliefs-vocabulary.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-10-07.md` (pass 69, pick A)
- **Raw fetches**: `/tmp/le31-daily-2026-10-07/gh-q5-append-only-ledger.json` (parent re-fetched the productive g5 query) and `/tmp/le31-daily-2026-10-07/verify/ghverify__parent_noise01_endoxa.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 69-pass series**:
  - **Feature 281 — `siezonsolutions/Seintinel-WasmGate`** (10-06 pick) — v2-AI zero-trust-execution-gate-vocabulary, 7/10 topic-overlap
  - **Feature 282 — `AllStreets/ONEXUS`** (10-06 pick) — v2-AI capability-arbiter-runtime-vocabulary, 7/9 topic-overlap
  - **Feature 283 — `NovasPlace/CSM`** (10-06 pick) — v2-AI persistent-memory-vocabulary, 8/20 topic-overlap
- **Charter §3.1 + §3.3 + §3.4 invariants**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the
  hard invariants (charter §3.1 explicit-state-transition + §3.3 audit-log-immutability + §3.4 AI-sandbox-as-auditable-test).
- `le31-v1-feature-pattern` — for the canonical contract shape.
- `le31-research` — for the source-of-truth discipline on GitHub
  repository verification.
- `development` — for the generic code-change workflow.

The agent must NOT load `le31-feature-pipeline` (this is a defer
artifact, not a build pipeline candidate).

## Frozen contract

The v2-AI vocabulary reference is:

- **Repo**: `noise01/endoxa`
- **License**: Apache-2.0 (permissive; charter §3.2 strictly-compatible)
- **Stars**: 0★/0⑂ at parent-verification time
- **Pushed**: 2026-10-07T05:43:06Z (in-window by `pushed_at` at 2026-10-07)
- **Created**: 2026-08-18T09:40:52Z (out-of-window by `created_at` = ~50 days before window-start)
- **Size**: 811 KB modest
- **Language**: Python ✓ (on-stack)
- **Topics (11)**: `ai-agents + belief-revision + calibration + defeasible-reasoning + knowledge-representation + llm + llm-agents + python + smt + smt-solver + truth-maintenance` (11/11 on the LE31 v2-AI governed-beliefs-vocabulary envelope = 100% topic-overlap = highest single-pick topic-alignment signal of the 69-pass series)
- **Description (verbatim)**: *Governed beliefs for LLM agents: an append-only ledger, SMT-checked consistency, defeasible revision, and calibration instruments.*

The vocabulary primitives are:

- `Belief` (id, content, confidence, created_at, retracted_at, schema_ref)
- `BeliefRevision` (id, belief_id, prior_belief_id, reason, evidence_ref, by_user_id, at)
- `SMTConstraint` (id, schema_name, smt_formula, satisfied_at)
- `CalibrationLog` (id, belief_id, predicted_confidence, actual_outcome, at)

The `Belief` + `BeliefRevision` tables form an **append-only ledger** (never `UPDATE` or `DELETE`).
The current belief set is the set of `Belief` rows with `retracted_at IS NULL` and the highest-confidence `BeliefRevision` per belief.

## Files to touch (when v2-AI belief-surface window opens)

- `/opt/data/le31_mmm3_research_work/backend/app/models/belief.py` — new SQLModel `Belief` + `BeliefRevision` + `SMTConstraint` + `CalibrationLog` tables.
- `/opt/data/le31_mmm3_research_work/backend/app/services/smt_checker.py` — Z3-solver wrapper for SMT-checked consistency verification.
- `/opt/data/le31_mmm3_research_work/backend/app/services/belief_revision.py` — defeasible-revision + calibration-instrument logic.
- `/opt/data/le31_mmm3_research_work/pyproject.toml` — add `z3-solver` dependency.
- (No other files expected to require changes for a vocabulary-only PR.)
- (Do NOT modify the existing v1 `audit_logs` SQLModel table; the v2-AI belief ledger is a NEW table.)

## Verification protocol

When the v2-AI belief-surface window opens:

1. Confirm the `noise01/endoxa` repo is still in-window (pushed within last 7 days
   from the trigger date) via `git ls-remote` or direct GitHub API GET.
2. Run `uv sync` (or `pip install -e .`) to install the new `z3-solver` dependency.
3. Run the v1 test suite — all tests must pass.
4. Run the new v2-AI belief-surface test suite (if any) — the SMT-checked
   consistency test must verify that a non-empty belief set is consistent
   against a knowledge-representation schema.
5. Run the LE31 v1 `audit_logs` test suite — the v1 audit log is untouched
   by the v2-AI belief-surface PR.
6. Surface any test failures to the owner (LE31 v1 has no LLM agent today;
   the test suite will be green if the `Belief` table is empty, but the
   SMT-checked consistency must be verified against a non-empty belief set
   to detect any bugs in the wrapper service).

## Rollback path

If the v2-AI belief-surface PR causes regressions:

1. Revert the SQLModel table additions (drop the `Belief` + `BeliefRevision` + `SMTConstraint` + `CalibrationLog` tables via Alembic downgrade).
2. Revert the `z3-solver` dependency addition in `pyproject.toml`.
3. Revert the SMT-checker + belief-revision service additions.
4. Re-run the v1 test suite.
5. Surface to the owner.

The v2-AI belief-surface PR is fully reversible — no v1 code is touched; the
v2-AI tables are new additions, not migrations of v1 tables.

## Sign-off gap

No build today. The defer artifact does not require sign-off from
the owner; it surfaces a dated, in-window v2-AI vocabulary reference
and waits for the next v2-AI belief-surface window.

If the owner opens a v2-AI belief-surface window, the external coding
agent must mirror this contract back to the owner before implementing
and stop if it cannot.
