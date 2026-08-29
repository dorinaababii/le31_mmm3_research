# HANDOFF — 136-memguard-verifier-signals-lifecycle-metadata-stockentry-audit

**Status**: defer (watch-list architecture reference, no build today)
**Date**: 2026-08-29
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/136-memguard-verifier-signals-lifecycle-metadata-stockentry-audit.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no owner-facing history surface for non-stock entities; charter does not authorise v2 audit-trail work yet)

## Trigger policy

This is a **defer artifact** — a watch-list entry. It does not start a build. It surfaces the MemGuard paper (arXiv `2608.21867v1`, 2026-08-22, cs.AI) as a dated, in-window architectural reference for the next time LE31 considers an owner-facing history surface for non-stock entities (`Visit`, `Bill`, `Shift`).

If the trigger condition (LE31 first proposes an owner-facing history surface for non-stock entities) is met, the external coding agent should:

1. Load this artifact and the linked arXiv paper.
2. Load the companion feature 134 (ECHO) — the two defer artifacts are companion documents (MemGuard is about *record lifecycle*, ECHO is about *record shape*).
3. Load the companion feature 108 (telegram-search chat-history fuzzy-search) — adjacent v2 audit-trail surface.
4. Define the LE31 operational verifier signal taxonomy (the paper's signals are multi-criteria LLM-output-derived; LE31's are operational — reconciled? closed? accepted? superseded?).
5. Decide whether `RecordLifecycle` is a new table or columns on existing entity tables.
6. Decide what "superseded_by" means in an append-only setting (charter §3.1 forbids silent rewriting; the lifecycle metadata must record supersession explicitly).
7. Pilot on one entity first (do not design for `Visit + Bill + Shift` at once).

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/136-memguard-verifier-signals-lifecycle-metadata-stockentry-audit.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-08-29.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-08-29/arxiv_verify/MemGuard_2608.21867_bbb2cf.json`, `/tmp/le31-brainstorm-2026-08-29/openalex_abstract_W7204193600.json` (177 word entries)
- **Companion artifacts**:
  - `features/134-echo-auditable-memory-plane-stockentry-audit.md` (record-shape primitive — opposite of MemGuard's record-lifecycle)
  - `features/108-telegram-chat-history-fuzzy-search-stockentry-audit.md` (v2 audit-trail surface architecture)
  - `features/111-arxiv-scroll-append-only-event-log-context-arch.md` (append-only event log + typed namespace)
  - `features/121-ledger-commitment-field-tier-minimization.md` (provenance tokens as disclosure minimisation unit)
- **Charter §3.1 (append-only ledger)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.5 (privacy — counts, not identity)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 append-only, §3.5 counts-not-identity).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on arXiv paper verification.

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The architectural primitive surfaced by this defer is:

- **Verifier signals as persistent lifecycle metadata on records, not a one-shot filter.** Every record carries `admitted_at`, `last_verified_at`, `superseded_by`, `archived_at`, `verifier_signal_json` columns; the verifier signals survive as columns, not as ephemeral filter results.

LE31 v1 has no owner-facing history surface for non-stock entities, so the lifecycle-metadata primitive is a **future v2 surface, not a v1 gap**. The defer artifact does **not** propose a `RecordLifecycle` schema. It surfaces the *naming* + *empirical claim* for future use.

When the defer is promoted to build, the future `RecordLifecycle` table would have columns `(record_kind, record_id, admitted_at, last_verified_at, superseded_by, archived_at, verifier_signal_json)` keyed by `(record_kind, record_id)`.

## Files to touch (when defer is promoted to build)

None today. When the defer is promoted:

- New SQLModel table in `/opt/data/le31_mmm3_research_work/backend/` (e.g. `RecordLifecycle`).
- New alembic migration under `/opt/data/le31_mmm3_research_work/backend/migrations/versions/`.
- New lifecycle-metadata writer in `/opt/data/le31_mmm3_research_work/backend/services/` (writes `RecordLifecycle` rows on every state transition).
- New owner-facing history view (if scoped).

## Verification protocol

When the defer is promoted to build, the external coding agent must verify:

1. The defer artifact's frozen contract fields match the new schema (e.g. `admitted_at` is a non-null timestamp set on every state transition).
2. The `RecordLifecycle` table does not silently bypass the append-only invariant (every `superseded_by` row must reference an existing record).
3. The lifecycle metadata is exercisable end-to-end (simulate a multi-actor shift reconciliation, confirm the lifecycle metadata forms a coherent timeline).
4. Charter §3.5 (privacy — counts, not identity) is satisfied: lifecycle metadata must not include diner-identifying fields.
5. The empirical claim (+7.9 success-rate points on WebArena in the paper's setting) is preserved in the LE31 setting — the absolute improvement may differ, but the *direction* should hold.
6. The rollback path (drop `RecordLifecycle` rows, drop `RecordLifecycle` table, remove the writer) is documented and reversible.

## Rollback path

If the defer is promoted to build and the implementation proves unsound:

1. Drop the `RecordLifecycle` table.
2. Revert the alembic migration.
3. Remove the lifecycle-metadata writer from the entity services.
4. Restore the entity services to the prior state (no `RecordLifecycle` reference).

The defer is fully reversible — no schema change today, so there is nothing to roll back today.

## Sign-off gap

No build today. The defer artifact does not require sign-off from the owner; it surfaces a dated, in-window architectural reference and waits for the next v2 owner-facing history surface proposal.

If the owner opens a v2 owner-facing history surface proposal, the external coding agent must mirror this contract back to the owner before implementing and stop if it cannot.