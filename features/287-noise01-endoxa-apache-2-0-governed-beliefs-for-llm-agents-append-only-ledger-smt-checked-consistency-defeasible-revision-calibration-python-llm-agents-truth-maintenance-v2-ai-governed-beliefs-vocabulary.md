# Feature 287 — `noise01/endoxa` v2-AI governed-beliefs-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v2-AI (v2-AI project does NOT exist; attach to `le31 Research` P-HMM-1 as the parent of the sub-issue)
> **Date:** 2026-10-07
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/287-noise01-endoxa-apache-2-0-governed-beliefs-for-llm-agents-append-only-ledger-smt-checked-consistency-defeasible-revision-calibration-python-llm-agents-truth-maintenance-v2-ai-governed-beliefs-vocabulary.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/287-noise01-endoxa-apache-2-0-governed-beliefs-for-llm-agents-append-only-ledger-smt-checked-consistency-defeasible-revision-calibration-python-llm-agents-truth-maintenance-v2-ai-governed-beliefs-vocabulary-HANDOFF.md`
> **Source daily research:** `/opt/data/le31-daily-research-2026-10-07.md` (pass 69, pick A)
> **Parent-verified via:** direct GitHub API GET `/repos/noise01/endoxa` at `/tmp/le31-daily-2026-10-07/verify/ghverify__parent_noise01_endoxa.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed)

## Goal

Surface a v2-AI vocabulary reference for **governed beliefs for LLM agents** — an append-only belief ledger, SMT-checked consistency, defeasible revision, and calibration instruments — as a forward-looking pattern for any future LE31 v2-AI control-plane that runs an LLM agent maintaining a set of operational beliefs (e.g., "the menu is updated", "the cook is on shift", "the prepped item has 8 pieces remaining").

## Evidence / JTBD

**Evidence classification:** inferred. The *governed-beliefs + SMT-checked-consistency + truth-maintenance* discipline is forward-looking for any future LE31 v2-AI surface; no LE31 v1 surface today has an LLM agent. **Confidence: medium-high** (0★/0⑂ + 811 KB modest + Python on-stack + 11/11 topic-overlap = strong §3.4-alignment signal + fresh-discovery).

**When** the LE31 v2-AI control-plane wants to run an LLM agent that maintains a set of beliefs, **the owner/waiter/cook wants to** know what the agent believes at any point in time, with a verifiable belief-revision trail, **but struggles because** the existing `audit_logs` SQLModel table is a flat log without SMT-checked consistency or defeasible-revision, **so that** an LLM agent cannot maintain a consistent, revision-tracked belief set with formal-verification guarantees. The *governed-beliefs + append-only-ledger + SMT-checked-consistency* is the *append-only-ledger + formal-consistency-verification* charter §3.1 invariant applied to the *LLM-agent-belief* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *governed-beliefs + append-only-belief-ledger + SMT-checked-consistency + defeasible-revision + calibration-instruments + truth-maintenance* sextuple-primitive as a candidate vocabulary for any future LE31 v2-AI belief-surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres mapping for each primitive.
- Record the §3.1/§3.2/§3.3/§3.4/§3.7 alignment per `le31-conventions/SKILL.md`.
- Record the strongest single-pick topic-alignment signal of the 69-pass series (11/11 = 100% topic-overlap = highest of 69-pass series).

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No LLM agent runtime; v2-AI surface is forward-looking.
- No SMT-solver integration into the existing `audit_logs` SQLModel table.

## Description

`noise01/endoxa` is a Python runtime for *governed beliefs for LLM agents*. The repo provides an append-only belief ledger; every belief is stored as a row in the ledger, and every belief revision (e.g., a new menu item, a stock decrement, a cook shift change) is written as a new ledger row. The ledger is checked for consistency against a satisfiability-modulo-theories (SMT) solver (typically Z3) — every belief set must satisfy a knowledge-representation schema before it is accepted. Beliefs can be revised via *defeasible reasoning* (a belief can be retracted when contradicted by evidence) and *calibration instruments* track the confidence of each belief (a score from 0.0 to 1.0 that is updated as evidence accumulates).

The vocabulary is a strong §3.4-alignment signal for any future LE31 v2-AI belief-surface because:
- The *append-only-belief-ledger* IS the §3.3 *audit-log-immutability* charter invariant applied to the *LLM-agent-belief* dimension.
- The *SMT-checked-consistency + truth-maintenance* IS the §3.4 *AI-sandbox-as-auditable-test* primitive — the SMT solver is the *non-AI-fallback* for belief consistency.
- The *defeasible-revision + calibration* IS the §3.4 *AI-self-correction* primitive applied to the *LLM-agent-belief-update* dimension.

The strongest single-pick topic-alignment signal of the 69-pass series: **11/11 topics on the LE31 v2-AI governed-beliefs-vocabulary envelope** (`ai-agents + belief-revision + calibration + defeasible-reasoning + knowledge-representation + llm + llm-agents + python + smt + smt-solver + truth-maintenance`). This is the highest single-pick topic-overlap score of the 69-pass series (vs feature 281's Seintinel-WasmGate 7/10 = 70% + feature 282's ONEXUS 7/9 = 78% + feature 283's CSM 8/20 = 40%).

## Data model

```
Belief          (id, content, confidence, created_at, retracted_at, schema_ref)
BeliefRevision  (id, belief_id, prior_belief_id, reason, evidence_ref, by_user_id, at)
SMTConstraint   (id, schema_name, smt_formula, satisfied_at)
CalibrationLog  (id, belief_id, predicted_confidence, actual_outcome, at)
```

The `Belief` and `BeliefRevision` tables form an **append-only ledger**. Never `UPDATE` or `DELETE` rows. The current belief set is the set of `Belief` rows with `retracted_at IS NULL` and the highest-confidence `BeliefRevision` per belief.

## Implementation steps

**This is a defer artifact. No code is written today.** When (and if) a future v2-AI PR adopts the *governed-beliefs + SMT-checked-consistency* discipline, the following files would be touched:

- `/opt/data/le31_mmm3_research_work/backend/app/models/belief.py` — new SQLModel `Belief` + `BeliefRevision` + `SMTConstraint` + `CalibrationLog` tables (append-only, §3.1 invariant).
- `/opt/data/le31_mmm3_research_work/backend/app/services/smt_checker.py` — Z3-solver wrapper for SMT-checked consistency verification.
- `/opt/data/le31_mmm3_research_work/backend/app/services/belief_revision.py` — defeasible-revision + calibration-instrument logic.
- `/opt/data/le31_mmm3_research_work/pyproject.toml` — add `z3-solver` dependency.
- (No other files expected to require changes for a vocabulary-only PR.)

## Telegram interaction

**None today** (defer artifact; no v1 build; vocabulary-only). If a future v2-AI belief-surface is built, the cook-side Telegram bot could surface belief-revision events as informational messages (e.g., "Belief updated: tiramisu has 8 pieces remaining").

## Dependencies

- **Charter §3.3 (audit-log-immutability)**: existing `audit_logs` SQLModel table is the v1 precedent; the `Belief` + `BeliefRevision` tables extend the same pattern to the LLM-agent-belief dimension.
- **`z3-solver` package**: Python binding for the Z3 SMT solver; the standard Python SMT-solver binding.
- **No v1 dependencies**: this is a v2-AI surface; no v1 code depends on it.

## Open questions

1. **Who would ever run the offline verifier of a governed-belief ledger with SMT-checked consistency?** LE31 has exactly one stakeholder (the owner) who can just read the beliefs directly. The *governed-beliefs + SMT-checked-consistency* may be over-engineering for a single-tenant single-operator scenario.
2. **What is the schema for the SMT-constraint?** The SMT constraint depends on the operational domain (restaurant, kitchen, stock, etc.); a future PR would need to specify the schema.
3. **What is the calibration-instrument's evidence source?** Calibration is updated as evidence accumulates; the evidence source depends on the LLM agent's actions (e.g., cook's `/sold_out` command, order-close event, etc.).
4. **What is the trade-off between SMT-checked-consistency (formal) and defeasible-revision (non-monotonic)?** SMT-checked-consistency is monotonic (adding beliefs cannot violate a satisfied constraint); defeasible-revision is non-monotonic (retracting a belief may violate a previously-satisfied constraint). The repo must reconcile these two.

## Why this matters

This is the **canonical v2-AI governed-beliefs-vocabulary of the 69-pass series** and the **strongest single-pick topic-alignment signal of the 69-pass series** (11/11 = 100% topic-overlap). The *governed-beliefs + SMT-checked-consistency + truth-maintenance* discipline is the closest vocabulary to a future LE31 v2-AI belief-surface; the *append-only-belief-ledger* extends the v1 `audit_logs` SQLModel table to the LLM-agent-belief dimension; the *defeasible-revision + calibration* extends the v1 `StockEntry` event-sourcing pattern to the LLM-agent-belief-update dimension.

The 11/11 topic-overlap score = 100% means the repo is *exactly* on the LE31 v2-AI governed-beliefs-vocabulary envelope. Future PRs that adopt any of the 6 primitives (governed-beliefs + append-only-ledger + SMT-checked-consistency + defeasible-revision + calibration + truth-maintenance) would inherit the §3.1 + §3.3 + §3.4 charter invariants with no translation needed.

**Charter alignment summary:** §3.1 partial (governed-beliefs + append-only-ledger + SMT-checked-consistency); §3.2 strictly-compatible (Apache-2.0 permissive); §3.3 ✓ (append-only-belief-ledger); §3.4 strong alignment (governed-beliefs + SMT-checked-consistency + truth-maintenance + non-AI-fallback); §3.7 N/A.
