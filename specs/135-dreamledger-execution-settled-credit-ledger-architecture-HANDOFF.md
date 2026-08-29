# HANDOFF — 135-dreamledger-execution-settled-credit-ledger-architecture

**Status**: defer (watch-list architecture reference, no build today)
**Date**: 2026-08-29
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/135-dreamledger-execution-settled-credit-ledger-architecture.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no signal-source beyond operator input; charter does not authorise v2 work that would expose such a surface)

## Trigger policy

This is a **defer artifact** — a watch-list entry. It does not start a build. It surfaces the DreamLedger paper (arXiv `2608.23863v2`, 2026-08-24, cs.RO) as a dated, in-window architectural reference for the next time LE31 considers a v2 surface that exposes an "AI suggestion", an external signal, or any "next action" that the system could take or recommend.

If the trigger condition (LE31 first proposes a v2 surface that ingests an external signal) is met, the external coding agent should:

1. Load this artifact and the linked arXiv paper.
2. Load the companion feature 134 (ECHO) — the two defer artifacts are companion documents (DreamLedger is about *signal reliability*, ECHO is about *record shape*).
3. Load the companion feature 07 (demand-estimation) — the first candidate signal-source.
4. Re-run the LE31 feature gate with the paper in hand.
5. Define the LE31 "condition" taxonomy (the paper's conditions are `operating-condition × region × horizon`; LE31's are `shift × daypart × menu-section`).
6. Decide whether `ReliabilityLedger` is a new table or a column on existing `audit_logs`.
7. Decide whether the consult-before-use helper is built into the v2 surface or a middleware.
8. Pilot on one signal-source first (do not design for all signal-sources at once).

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/135-dreamledger-execution-settled-credit-ledger-architecture.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-08-29.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-08-29/arxiv_verify/DreamLedger_2608.23863_70c335.json`, `/tmp/le31-brainstorm-2026-08-29/openalex_abstract_W7204222800.json` (198 word entries)
- **Companion artifacts**:
  - `features/134-echo-auditable-memory-plane-stockentry-audit.md` (record-shape primitive)
  - `features/07-demand-estimation.md` (first candidate signal-source)
  - `features/133-hansard-runtime-witnessing-ledger-architecture.md` (runtime witnessing primitive)
- **Charter §3.1 (append-only ledger)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.4 (no customer-facing AI)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 append-only, §3.4 observable evidence).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on arXiv paper verification.

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The architectural primitive surfaced by this defer is:

- **Execution-settled credit ledger** — at the moment a signal is consumed, the system produces a *claim*; attributable outcomes are *settled*; the resulting *credit* gates future consumption. Every reliance event remains *auditable via dependency tickets and replayable logs*.

LE31 v1 has no signal-source beyond operator input, so the credit-rail primitive is a **future v2 surface, not a v1 gap**. The defer artifact does **not** propose a `ReliabilityLedger` schema. It surfaces the *naming* + *empirical claim* for future use.

When the defer is promoted to build, the future `ReliabilityLedger` table would have columns `(signal_kind, condition, outcome, claim_id, settlement_id, recorded_at)` plus a consult-before-use helper.

## Files to touch (when defer is promoted to build)

None today. When the defer is promoted:

- New SQLModel table in `/opt/data/le31_mmm3_research_work/backend/` (e.g. `ReliabilityLedger`).
- New alembic migration under `/opt/data/le31_mmm3_research_work/backend/migrations/versions/`.
- New consult-before-use helper in `/opt/data/le31_mmm3_research_work/backend/` (e.g. `services/reliability.py`).
- New owner-facing "track record" view (if scoped).

## Verification protocol

When the defer is promoted to build, the external coding agent must verify:

1. The defer artifact's frozen contract fields match the new schema (e.g. `claim_id` is a FK to the consumer's claim surface).
2. The new `ReliabilityLedger` does not silently bypass the append-only invariant (every row must reference a known signal-source + a known consumer).
3. The consult-before-use helper is exercisable end-to-end (simulate a low-credit prediction, confirm the gate triggers the additional observation).
4. The empirical claim (62% reduction in burned imagination) is preserved in the LE31 setting (the LE31 single-restaurant scale is much smaller than the paper's robotic-world-model scale; the absolute reduction may be different, but the *direction* should hold).
5. The rollback path (drop `ReliabilityLedger` rows, drop `ReliabilityLedger` table, drop the consult-before-use helper) is documented and reversible.

## Rollback path

If the defer is promoted to build and the implementation proves unsound:

1. Drop the `ReliabilityLedger` table.
2. Revert the alembic migration.
3. Remove the consult-before-use helper from the v2 surface.
4. Restore the v2 surface to the prior state.

The defer is fully reversible — no schema change today, so there is nothing to roll back today.

## Sign-off gap

No build today. The defer artifact does not require sign-off from the owner; it surfaces a dated, in-window architectural reference and waits for the next v2 surface that proposes a signal-source.

If the owner opens a v2 "AI suggestion" surface proposal, the external coding agent must mirror this contract back to the owner before implementing and stop if it cannot.