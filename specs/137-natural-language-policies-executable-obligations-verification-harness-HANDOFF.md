# HANDOFF — 137-natural-language-policies-executable-obligations-verification-harness

**Status**: defer (watch-list architecture reference, no build today)
**Date**: 2026-08-29
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/137-natural-language-policies-executable-obligations-verification-harness.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no owner-authored-rules surface; charter §3.1 *rules-as-code* posture is the inverse of the paper's *policy-as-input* posture; owner decision required before any rule-authoring surface is scoped)

**Charter tension**: the paper's *policy-as-input* posture is the **inverse of LE31 charter §3.1's *rules-as-code* posture**. The defer artifact surfaces this tension explicitly so that any future v2 surface that wants owner-authored rules must resolve it before scoping.

## Trigger policy

This is a **defer artifact** — a watch-list entry. It does not start a build. It surfaces the AgentGuardUtil / NL-to-Executable-Obligations paper (arXiv `2608.23282v1`, 2026-08-24, cs.SE) as a dated, in-window architectural reference for the next time LE31 considers a v2 surface that allows the owner to author operational rules without involving an engineer.

If the trigger condition (LE31 first proposes a v2 surface that allows owner-authored rules) is met, the external coding agent should:

1. Load this artifact and the linked arXiv paper.
2. **Re-confirm charter §3.1** ("operational transitions are explicit user actions") with the owner before any rule-authoring surface is scoped.
3. **Resolve the *policy-as-input* vs *rules-as-code* tension.** Either (i) the rule-authoring surface is restricted to a *non-operational* subset (e.g., display-only rules, not state-transition rules), or (ii) the charter is amended to allow operator-authored state-transition rules with explicit deterministic obligation-engine checks.
4. Load the companion feature 121 (commitment-before-minimization) and feature 122 (CAIT) — the transitive difference is that this paper specifies the *policy-compilation step*.
5. Load the companion feature 133 (HANSARD runtime-witnessing) — HANSARD is about *who acted*, this paper is about *what rules the actor's action must satisfy*.
6. Define the LE31 rule taxonomy (the paper's rules are in-car driving-domain; LE31's natural rules are visibility / allergen / payment-method).
7. Decide the policy-compilation surface (single-shot per-rule vs continuous).
8. Pilot on one rule class first (do not design for all rule classes at once).

If the trigger condition is **not** met, or the charter-§3.1 tension is **not** resolved, do nothing.

## Mandatory inputs

- **Active feature**: `features/137-natural-language-policies-executable-obligations-verification-harness.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-08-29.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-08-29/arxiv_verify/NL-to-Executable-Obligations_2608.23282_6ba217.json`, `/tmp/le31-brainstorm-2026-08-29/openalex_abstract_W7204190262.json` (130 word entries)
- **Companion artifacts**:
  - `features/121-ledger-commitment-field-tier-minimization.md` (commitment-before-minimization — *what is committed*)
  - `features/122-trace-integrity-cait-acceptance-criterion.md` (CAIT — *what is queried*)
  - `features/133-hansard-runtime-witnessing-ledger-architecture.md` (HANSARD — *who acted*)
  - `features/137-natural-language-policies-executable-obligations-verification-harness.md` (this paper — *what rules the actor's action must satisfy*)
- **Charter §3.1 (explicit state transitions)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.4 (no customer-facing AI; non-AI fallback)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 explicit state transitions, §3.4 observable evidence + non-AI fallback).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on arXiv paper verification.

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner. The agent must NOT scope a rule-authoring surface without first resolving the charter-§3.1 tension with the owner.

## Frozen contract

The architectural primitive surfaced by this defer is:

- **Runtime policy compiler + deterministic obligation engine.** A natural-language policy is compiled into typed machine-checkable rules; a deterministic obligation engine interprets the rules against live state and emits remedial calls with computed arguments.

LE31 v1 has no owner-authored-rules surface (every rule is hard-coded in the data model today). The defer artifact does **not** propose a `PolicyRule` schema. It surfaces the *naming* + *the charter-§3.1 tension* for future use.

When the defer is promoted to build (after the charter-§3.1 tension is resolved), the future `PolicyRule` table would have columns `(rule_id, natural_language, typed_obligation_json, executable_form_json, applies_to_entity, recorded_at)` plus a deterministic obligation engine.

## Files to touch (when defer is promoted to build)

None today. When the defer is promoted:

- **Owner decision required first** (charter-§3.1 tension resolution).
- New SQLModel table in `/opt/data/le31_mmm3_research_work/backend/` (e.g. `PolicyRule`).
- New alembic migration under `/opt/data/le31_mmm3_research_work/backend/migrations/versions/`.
- New policy-compiler service in `/opt/data/le31_mmm3_research_work/backend/services/` (compiles natural-language → typed obligations).
- New deterministic obligation engine in `/opt/data/le31_mmm3_research_work/backend/services/` (interprets typed obligations against live state).
- New owner-facing rule-authoring surface (if scoped).

## Verification protocol

When the defer is promoted to build (after the charter-§3.1 tension is resolved), the external coding agent must verify:

1. The defer artifact's frozen contract fields match the new schema (e.g. `natural_language` is the owner-authored source; `typed_obligation_json` is the compiler output).
2. The `PolicyRule` table does not silently bypass the append-only invariant (every rule edit must create a new `PolicyRule` row, not update an existing one).
3. Charter §3.4 (no customer-facing AI; non-AI fallback) is satisfied: any LLM-critic layer must have a deterministic non-AI fallback.
4. The deterministic obligation engine is exercisable end-to-end (compile a test rule, observe the typed obligation, run the engine, observe the remedial call).
5. The policy-compiler rejects ambiguous rules deterministically (no silent failure).
6. The rollback path (drop `PolicyRule` rows, drop `PolicyRule` table, remove the policy-compiler + obligation engine) is documented and reversible.

## Rollback path

If the defer is promoted to build and the implementation proves unsound:

1. Drop the `PolicyRule` table.
2. Revert the alembic migration.
3. Remove the policy-compiler + deterministic obligation engine from the backend.
4. Restore the rule-as-code data model to the prior state.

The defer is fully reversible — no schema change today, so there is nothing to roll back today.

## Sign-off gap

**No build today. The defer artifact requires explicit owner sign-off before any rule-authoring surface is scoped** — the charter-§3.1 tension is the central honesty note and must be resolved before implementation begins.

If the owner opens a v2 rule-authoring surface proposal, the external coding agent must mirror this contract back to the owner **including the charter-§3.1 tension** before implementing and stop if it cannot.