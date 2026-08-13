# Feature 61 — Holdfast Approval Ledger

> **Priority**: P2 · **Effort**: M (≤1 week) · **Source**: brainstorm
> 2026-08-13 (cross-section pick A) · **Bucket**: **v2-AI control-plane**
> (same bucket as feature 58).
> **One-line**: an append-only `DecisionLedger` with a two-row
> proposal/decision shape — the same pattern LE31 already uses for
> `StockEntry`, applied to AI actions — so every AI proposal and
> every owner decision is a separate, tamper-evident row.

## Goal

Feature 58 (`operator-ai-action-surface`) ships the **control plane**:
`attempt()`, `approve()`, `reject()`, `permission_table_get()`,
`fallback_path_for()`. It writes one `AIActionAttempt` row per
attempt. That is the *outcome* of an AI action, not the
proposal/decision dance itself.

LE31's charter already promises an evidence-grade append-only chain
for `StockEntry` and `AuditLog`. The same shape should hold for
**the AI's proposal and the owner's decision**, so that:

- The owner's daily-recap Telegram (`feature 39`) can quote the
  proposal row id and the decision row id side by side.
- The evidence-review surface (`feature 55`) can trace
  *"what was the AI's reasoning"* to a row, not to free text.
- A future charter revision introducing multi-model orchestration
  (parking-lot feature 63) can plug into the same ledger.

`holdfast-approval-ledger` ships the **shape**: two rows per AI
action event — the proposal (`DecisionRow(kind='ai_proposal', …)`)
and the decision (`DecisionRow(kind='owner_decision', …)`, status
`approved | rejected | fallback`). Both rows are append-only and
participate in the **same hash chain** that feature 49
(`postledger-tamper-evident-hash`) extends.

## Scope

**In scope (v2-AI control-plane companion):**

- New SQLModel table `backend/app/models/decision_ledger.py`:
  `DecisionRow(id, kind, attempt_id, evidence_id, payload, rationale,
   actor_kind, actor_id, prev_hash, row_hash, created_at)`. One new
  Alembic migration.
- New helper `backend/app/services/decision_ledger.py`:
  `propose(...)`, `decide(...)`, `chain_for(attempt_id)`, and
  `audit_dump(attempt_id)`. Pure stdlib + SQLModel; the hash chain
  reuses the same `prev_hash → row_hash` scheme as feature 49.
- `backend/app/services/ai_control_plane.py` (from feature 58):
  `attempt()` now writes one `DecisionRow(kind='ai_proposal', …)`
  before any model call. `approve()` and `reject()` write a second
  `DecisionRow(kind='owner_decision', …)`. `fallback_path_for()`
  writes a third row with `kind='fallback_dispatch'`. Net: ≥2 rows
  per AI action; ≥1 row per deterministic fallback. Total ≤ ~80
  lines added to `ai_control_plane.py`.
- `backend/app/bot/cook_bot.py`: extend `/approve <id>` and
  `/reject <id>` to surface the proposal row id alongside the
  decision row id, and accept the new `/decisions` command that
  lists the last 10 decisions with both rows. ≤ ~30 lines added.
- `backend/tests/test_decision_ledger.py`: 5 fixtures (propose,
  decide, hash-chain integrity, append-only invariant, evidence
  round-trip).
- `backend/scripts/verify_decision_chain.py`: read-only CLI that
  walks the chain for a given attempt id and prints the two rows
  in human-readable form. Mirrors `verify_evidence_chain.py` from
  feature 55.
- `backend/README.md`: note the new table, the new bot command,
  and the relationship to `feature 58`.

**Out of scope (v2-AI control-plane v1):**

- The AI itself. No model call inside this slice. The control
  plane's `attempt(...)` calls `propose(...)` before the model
  call and `decide(...)` after the owner reply; this slice
  implements the *ledger shape*, not the *dispatcher* (the
  dispatcher is feature 58).
- Multi-model orchestration (feature 63, parking-lot). When feature
  63 ships, it will read from this ledger.
- Owner-facing write to the YAML ontology (feature 62). The
  ledger is code-driven only at v1; owner edits come in feature 62.
- Telemetry dashboard. Same as feature 55 — the audit table is
  queryable; the v3 dashboard is a separate pick.

## Description

`dallascrilley/holdfast` (pushed **2026-08-12**, MIT, TypeScript,
★0) ships the same two-row *proposal / human approval* shape that
LE31 needs. The shape is described in plain English by the
project's tagline: *"an append-only decision ledger with a human
approval gate: AI can propose, only a person can publish."*

`chiga0/marshal-harness` (pushed 2026-08-13, Go, ★1) corroborates
with *"Evidence-gated orchestration for coding agents: frozen
tasks, independent verification, digest-bound review,
draft-only publication"* — different stack, same shape.

LE31's contribution is to bind this shape to the existing
audit-grade chain (features 30, 47, 49, 50) so that an owner-side
review can replay *both* the AI's reasoning and the owner's
decision at any past date with the same hash integrity as
`StockEntry`.

## Data model

```sql
CREATE TABLE decision_row (
    id              BIGSERIAL PRIMARY KEY,
    kind            TEXT NOT NULL,           -- ai_proposal|owner_decision|fallback_dispatch
    attempt_id      BIGINT NOT NULL REFERENCES ai_action_attempt(id),
    evidence_id     BIGINT,                  -- optional EvidenceLink row id (feature 55)
    payload         JSONB NOT NULL,          -- the proposal JSON, or the decision JSON
    rationale       TEXT,                    -- owner rationale (for kind=owner_decision)
    actor_kind      TEXT NOT NULL,           -- 'ai' | 'owner' | 'system'
    actor_id        INTEGER,
    prev_hash       BYTEA NOT NULL,          -- chain: row_hash of the previous decision_row
    row_hash        BYTEA NOT NULL,          -- sha256 of (prev_hash || row-json)
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX decision_row_attempt_kind_idx ON decision_row (attempt_id, kind);
CREATE INDEX decision_row_created_at_idx   ON decision_row (created_at);
```

APPEND-ONLY at the API layer: never UPDATE or DELETE a `decision_row`
row once written. Hash chain mirror of feature 49.

A single AI action attempt looks like:

```
DecisionRow #101 (kind=ai_proposal,     actor_kind=ai)
DecisionRow #102 (kind=owner_decision,  actor_kind=owner, status=approved)
                          ── chain links via prev_hash/row_hash ──
```

## Implementation steps

1. Add `backend/app/models/decision_ledger.py` with the `DecisionRow`
   SQLModel.
2. Add Alembic migration `XXXX_add_decision_ledger.py`.
3. Add `backend/app/services/decision_ledger.py` — `propose()`,
   `decide()`, `chain_for()`, `audit_dump()`. Reuse the
   `prev_hash → row_hash` from feature 49's helper, do not
   reimplement.
4. Extend `backend/app/services/ai_control_plane.py`:
   - `attempt(...)` wraps the first DB insert in
     `decision_ledger.propose(...)` before the model call.
   - `approve(...)` and `reject(...)` wrap their DB updates in
     `decision_ledger.decide(...)` after the AuditLog row.
   - `fallback_path_for(...)` wraps the manual-path write in
     `decision_ledger.propose(..., kind='fallback_dispatch')`.
5. Extend `backend/app/bot/cook_bot.py`: add `/decisions` handler,
   and extend `/approve <id>` and `/reject <id>` to return both
   row ids in the reply card.
6. Add `backend/tests/test_decision_ledger.py` (5 fixtures).
7. Add `backend/scripts/verify_decision_chain.py`.
8. Add `backend/README.md` section.

## Telegram interaction if any

- `/decisions` — owner-only. Returns last 10 `DecisionRow` entries
  with the attempt id, the kind, the actor kind, and a one-line
  rationale (if present). New command, no overlap with feature 55
  or 58.
- `/approve <attempt_id>` (extended from feature 58) — reply card
  now reports both the attempt id and the new `decision_row` id
  so the owner can recall it via `/decisions` later.
- `/reject <attempt_id> reason=<text>` (extended from feature 58)
  — same as above.
- No new owner-only deterministic fallback command — feature 58's
  `/<action> manual` already routes through the fallback path,
  which now writes one `DecisionRow` automatically.

## Dependencies

- **Feature 30** (`append-only-audit-redirect`) — every new row
  still emits an `AuditLog` entry; this slice reuses the helper.
- **Feature 49** (`postledger-tamper-evident-hash`) — the
  `prev_hash → row_hash` chain is reused. No new hashing.
- **Feature 55** (`evidence-review-surface`) — the new
  `evidence_id` column on `decision_row` is an `EvidenceLink.id`
  reference (feature 55), the same shape used by feature 58's
  `evidence_link_ids` JSON array.
- **Feature 58** (`operator-ai-action-surface`) — the dispatcher
  and the `AIActionAttempt` table are inputs to this slice, not
  produced by it.
- **Feature 47** (`decision-rationale-mixin`) — the new
  `rationale` column on `decision_row` is the same column type as
  feature 47's `DecisionRationale.rationale` (TEXT, append-only).

No new pip dependencies. No new external service. No model call.
One new SQLModel table. One new Alembic migration.

## Open questions

- Should the `decision_row` rationales be visible in the daily
  recap Telegram, or owner-only? Recommendation: owner-only at
  v1, opt-in later.
- When the owner runs `/<action> manual`, should the new
  `kind='fallback_dispatch'` row be written before or after the
  manual entry's AuditLog? Recommendation: before, so the
  chronological order matches a natural reading.
- Should the `verify_decision_chain.py` CLI be the only
  external reader of the chain, or should the existing
  `verify_evidence_chain.py` (feature 55) be extended to walk
  it? Recommendation: separate CLI, but a v3 could merge them.

## Why this matters

LE31's v2-AI control plane (feature 58) is incomplete without a
**decision ledger**. Without it, the audit row `AIActionAttempt`
records the outcome; the proposal and decision are *implied*
between the call sites. With it, the proposal and the decision
are *both* rows, both immutable, both replayable, both inside
the same hash chain that protects `StockEntry`.

`holdfast` exists *today* (2026-08-12) in MIT-licensed TypeScript.
LE31 ships the equivalent in Python with one new SQLModel table,
≤80 lines of code in `ai_control_plane.py`, and reuses every
append-only primitive that already ships for stock. The risk
profile is bounded by the existing v2-AI control-plane slice.

This is a **build, M effort, ≤1 week** pick. The slice boundary
is hard: no model call, no dispatcher logic beyond reading/
writing two rows, no schema change to `AIActionAttempt`.

## Evidence (recorded)

- **Cross-section anchor 1**: `dallascrilley/holdfast` (pushed
  2026-08-12, MIT, TypeScript, ★0) — *"append-only decision
  ledger with a human approval gate: AI can propose, only a
  person can publish"*. Read at
  `/tmp/le31-brainstorm-2026-08-13/gh_topic_append_only.json`.
- **Cross-section anchor 2**: `chiga0/marshal-harness` (pushed
  2026-08-13, Go, ★1) — *"Evidence-gated orchestration for
  coding agents"*. Same shape, different stack.
- **In-repo anchor**: feature 58's `AIActionAttempt` table is
  the parent row this slice references; feature 49's hash helper
  is the chain mechanism this slice reuses.
- **Literature anchor**: OpenAlex `Designing Agentic AI
  Experiences` (DOI 10.1201/9781003738374, 2026-07-28).
