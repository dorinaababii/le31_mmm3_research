# HANDOFF — 133-hansard-runtime-witnessing-ledger-architecture

**Status**: defer (watch-list architecture reference, no build today)
**Date**: 2026-08-29
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/133-hansard-runtime-witnessing-ledger-architecture.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no audit-trail viewer surface; charter does not authorise v2 audit-trail work yet)

## Trigger policy

This is a **defer artifact** — a watch-list entry. It does not start
a build. It surfaces the HANSARD paper (arXiv `2608.22512v1`,
2026-08-23, cs.AI) as a dated, in-window architectural reference
for the next time LE31 considers an audit-trail viewer surface for
non-stock entities (visit, bill, shift).

If the trigger condition (LE31 first proposes an audit-trail viewer
surface) is met, the external coding agent should:

1. Load this artifact and the linked arXiv paper.
2. Re-run the LE31 feature gate with the paper in hand.
3. Decide whether graded attribution (multi-actor `StockEntry`
   writes) is in scope for the v2 audit-trail surface.
4. If yes, design a `witness_tokens` schema that names the witnesses
   per row.
5. If no, close this artifact.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/133-hansard-runtime-witnessing-ledger-architecture.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-08-29.md`
- **Raw fetches**: `/tmp/le31-daily-2026-08-29/arxiv-loose-ledger.xml`, `/tmp/le31-daily-2026-08-29/arxiv-loose-provenance.xml`
- **Companion artifacts**: `features/127-zero-shot-self-orchestration-Ledger-Based-Control.md`, `features/121-ledger-commitment-field-tier-minimization.md`, `features/108-telegram-chat-history-fuzzy-search-stockentry-audit.md`, `features/134-echo-auditable-memory-plane-stockentry-audit.md`
- **Charter §3.1 (append-only ledger)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the
  hard invariants (charter §3.1 append-only, §3.4 observable evidence).
- `le31-v1-feature-pattern` — for the canonical contract shape
  (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on arXiv
  paper verification.

The agent must NOT load `le31-feature-pipeline` until the defer
is promoted to build by the LE31 owner.

## Frozen contract

The architectural primitive surfaced by this defer is:

- **Runtime witnessing** — at the moment a `StockEntry` row is
  produced, the system produces a *witness* (a small attestation:
  who authorised the action, what alternatives were considered,
  what the system knew at the time).

LE31 v1 already operationalises a thin version of runtime witnessing
at single-restaurant scale:

- `StockEntry.actor_user_id` — who wrote the row.
- `StockEntry.actor_role` — what role they had.
- Append-only invariant — the witness is preserved.

What LE31 v1 does **not** have:

- **Graded attribution** across multi-actor chains (real
  restaurant operations sometimes involve multiple humans, but
  every `StockEntry` attributes the write to a single actor).

The defer artifact does **not** propose a graded-attribution
schema. It surfaces the *naming* for future documentation purposes
("the `StockEntry` ledger is a *runtime witness*", not just a
record).

## Files to touch (when defer is promoted to build)

None today. When the defer is promoted:

- New SQLModel tables in `/opt/data/le31_mmm3_research_work/backend/`
  (e.g. `witness_tokens`, `audit_records`).
- New alembic migration under
  `/opt/data/le31_mmm3_research_work/backend/migrations/versions/`.
- Documentation updates to charter §3.1 wording.

## Verification protocol

When the defer is promoted to build, the external coding agent must
verify:

1. The defer artifact's frozen contract fields match the new
   schema (e.g. `actor_user_id` remains the witness field).
2. The new schema does not silently bypass the append-only
   invariant (every `witness_tokens` row must reference an
   existing `StockEntry` row by FK).
3. The audit trail is exercisable end-to-end on the configured
   environment (e.g. simulate a multi-actor shift reconciliation,
   confirm the audit records form a coherent timeline).
4. The rollback path (delete `witness_tokens` rows, drop
   `audit_records` table) is documented and reversible.

## Rollback path

If the defer is promoted to build and the implementation proves
unsound:

1. Drop the new tables.
2. Revert the alembic migration.
3. Restore the `StockEntry` schema to the prior state (no
   `witness_tokens` reference).

The defer is fully reversible — no schema change today, so there
is nothing to roll back today.

## Sign-off gap

No build today. The defer artifact does not require sign-off from
the owner; it surfaces a dated, in-window architectural reference
and waits for the next v2 audit-trail surface proposal.

If the owner opens a v2 audit-trail viewer proposal, the external
coding agent must mirror this contract back to the owner before
implementing and stop if it cannot.