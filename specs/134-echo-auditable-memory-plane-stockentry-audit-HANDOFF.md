# HANDOFF — 134-echo-auditable-memory-plane-stockentry-audit

**Status**: defer (watch-list architecture reference, no build today)
**Date**: 2026-08-29
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/134-echo-auditable-memory-plane-stockentry-audit.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no audit-trail viewer surface for non-stock entities; charter does not authorise v2 audit-trail work yet)

## Trigger policy

This is a **defer artifact** — a watch-list entry. It does not start
a build. It surfaces the ECHO paper (arXiv `2608.21755v1`,
2026-08-22, cs.AI) as a dated, in-window architectural reference
for the next time LE31 considers an audit-trail viewer surface
for non-stock entities (visit, bill, shift).

If the trigger condition (LE31 first proposes an audit-trail viewer
surface for non-stock entities) is met, the external coding agent
should:

1. Load this artifact and the linked arXiv paper.
2. Load the companion feature 133 HANSARD (runtime witnessing)
   — the two defer artifacts are companion documents.
3. Load the companion feature 128 SKILL.state (the *opposite* of
   ECHO: replace append-only with structured state for chat
   history).
4. Decide whether the audit-record tables (`VisitAuditRecord`,
   `BillAuditRecord`, `ShiftAuditRecord`) are in scope for the v2
   audit-trail surface.
5. If yes, design the ECHO-style auditable-memory-plane schema
   with `provenance_token` + `witness_token`.
6. If no, close this artifact.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/134-echo-auditable-memory-plane-stockentry-audit.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-08-29.md`
- **Raw fetches**: `/tmp/le31-daily-2026-08-29/arxiv-loose-ledger.xml`
- **Companion artifacts**:
  - `features/133-hansard-runtime-witnessing-ledger-architecture.md` (witness_token primitive)
  - `features/128-skill-state-scalable-long-horizon-agent-skills.md` (opposite: replace append-only with structured state for chat)
  - `features/108-telegram-chat-history-fuzzy-search-stockentry-audit.md` (v2 audit-trail surface architecture)
  - `features/121-ledger-commitment-field-tier-minimization.md` (related: provenance tokens as disclosure minimisation unit)
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

- **Auditable memory plane** — for each non-stock entity (visit,
  bill, shift), produce an *audit record* alongside the entity's
  lifecycle events. Each audit record has:
  - `provenance_token` (SHA-256 hash of entity state at event time)
  - `witness_token` (FK to a `StockEntry` row that is the operational anchor)
  - `actor_user_id` + `actor_role` (same fields as `StockEntry`)
  - `created_at` (timezone-aware UTC)

LE31 v1 already has an append-only posture for `StockEntry` (charter
§3.1) and correctly does NOT extend that posture to chat history
(cf. feature 128 SKILL.state). The ECHO pattern is the *dual* of
feature 128:

- **feature 128 (SKILL.state)**: for chat history, *replace*
  append-only with structured state.
- **feature 134 (ECHO)**: for audit history, *replace* append-only
  conversation history with auditable structured records.

The defer artifact proposes a parallel audit-record schema
(`VisitAuditRecord`, `BillAuditRecord`, `ShiftAuditRecord`) but
does NOT implement it today.

## Files to touch (when defer is promoted to build)

None today. When the defer is promoted:

- New SQLModel tables in `/opt/data/le31_mmm3_research_work/backend/`:
  - `VisitAuditRecord` (id, visit_id, event_type, actor_user_id, actor_role, provenance_token, witness_token, created_at)
  - `BillAuditRecord` (id, bill_id, event_type, actor_user_id, actor_role, provenance_token, witness_token, created_at)
  - `ShiftAuditRecord` (id, shift_id, event_type, actor_user_id, actor_role, provenance_token, witness_token, created_at)
- New alembic migration under
  `/opt/data/le31_mmm3_research_work/backend/migrations/versions/`.
- A new audit-trail viewer endpoint in
  `/opt/data/le31_mmm3_research_work/backend/app/api/`.
- Possibly a new cook-bot audit-trail command in
  `/opt/data/le31_mmm3_research_work/backend/app/bot/`.

## Verification protocol

When the defer is promoted to build, the external coding agent must
verify:

1. The defer artifact's frozen contract fields match the new
   schema (`provenance_token`, `witness_token`, `actor_user_id`,
   `actor_role`).
2. The new tables are append-only (charter §3.1 applies to *all*
   state changes, not just `StockEntry`).
3. The audit records form a coherent timeline when queried (e.g.
   "show me everything that happened at table 5 last Friday").
4. The `witness_token` correctly references an existing
   `StockEntry` row (FK integrity).
5. The rollback path (drop audit-record tables, drop alembic
   migration) is documented and reversible.

## Rollback path

If the defer is promoted to build and the implementation proves
unsound:

1. Drop the audit-record tables.
2. Revert the alembic migration.
3. Restore the `StockEntry` schema to the prior state (no
   `witness_token` FK references).

The defer is fully reversible — no schema change today, so there
is nothing to roll back today.

## Sign-off gap

No build today. The defer artifact does not require sign-off from
the owner; it surfaces a dated, in-window architectural reference
and waits for the next v2 audit-trail surface proposal.

If the owner opens a v2 audit-trail viewer proposal for non-stock
entities, the external coding agent must mirror this contract back
to the owner before implementing and stop if it cannot.