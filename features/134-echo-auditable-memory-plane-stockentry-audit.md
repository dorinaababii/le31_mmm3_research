# Feature 134 — ECHO auditable-memory-plane StockEntry audit (defer)

## Goal

Surface arXiv `2608.21755v1` ECHO (2026-08-22, cs.AI) as a dated,
in-window architectural reference for any future LE31 v2 audit-trail
surface for non-stock entities — specifically, the **"auditable
memory plane"** framing as an alternative audit primitive for
owner-facing history that does *not* corrupt the append-only
`StockEntry` ledger by re-introducing chat-history anti-patterns
(cf. feature 128).

## Scope

**In scope (defer artifact):**
- A written record of the paper's mechanism (cognitively-inspired
  auditable memory plane for long-horizon agents with checkable
  provenance).
- A decision record: today's verdict is `defer` because LE31 v1 has
  no audit-trail viewer surface and the charter does not authorise
  v2 audit-trail work yet.
- A reference for the next time LE31 considers an audit-trail
  surface for non-stock entities (visit, bill, shift).

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any user-facing audit-trail viewer surface.
- Any owner-facing auditable-memory-plane tooling.
- Implementation of the paper's cognitive-inspiration primitives
  (they are no-ops at LE31's scale).

## Description

arXiv `2608.21755v1` ECHO — "A Cognitively Inspired, Auditable
Memory Plane for Long-Horizon Agents" — proposes an *auditable
memory plane* as an alternative to append-only conversation
history for long-horizon agents. The pattern is:

- Long-horizon agents that maintain context by continually appending
  to conversation history suffer *context poisoning* and unbounded
  growth.
- The paper proposes replacing the append-only conversation history
  with a **structured memory plane** where each record has
  *checkable provenance* — a small attestation that the record can
  be traced to a specific event, action, or observation.
- The *auditable* + *checkable provenance* framing is the durable
  takeaway.

LE31 v1 already has an append-only posture for `StockEntry` (charter
§3.1) and *correctly* does not extend that posture to chat history
(cf. feature 128 SKILL.state, which argues against the naive
extension). The ECHO paper's auditable-memory-plane framing is the
*dual* of feature 128:

- **feature 128 (SKILL.state)**: for chat history, *replace*
  append-only with structured state (because chat history is not a
  state ledger).
- **feature 134 (ECHO)**: for audit history, *replace* append-only
  conversation history with auditable structured records (because
  audit history needs more than a log — it needs checkable
  provenance).

For LE31 v2 audit-trail surfaces (e.g. "show me everything that
happened at table 5 last Friday"), the ECHO pattern suggests:

1. Do not log chat history as a substitute for `StockEntry`. The
   `StockEntry` ledger is the operational truth; chat is dialogue.
2. For each non-stock entity (visit, bill, shift), produce an
   *audit record* alongside the entity's lifecycle events.
3. Each audit record has a checkable provenance token (e.g. hash
   + witness reference per feature 133 HANSARD).
4. The audit records form an *auditable memory plane* parallel to
   the operational ledger, not a replacement for it.

The paper's cognitive-inspiration primitives (memory consolidation,
forgetting, retrieval) are out of scope for LE31 — restaurant
operations are short-horizon (one service per day) and do not need
memory consolidation.

## Data model

No schema change. The defer artifact documents that the v2
audit-trail surface, when it ships, should follow the ECHO pattern:

```
StockEntry          (existing)        — operational truth
VisitAuditRecord    (v2, future)      — auditable audit record per visit
BillAuditRecord     (v2, future)      — auditable audit record per bill
ShiftAuditRecord    (v2, future)      — auditable audit record per shift
```

Each `*AuditRecord` has:

- `id` (UUID)
- `entity_id` (FK to the audited entity)
- `entity_type` (enum: visit | bill | shift)
- `event_type` (enum: created | updated | closed | reconciled)
- `actor_user_id` (FK to actor — same field as `StockEntry.actor_user_id`)
- `actor_role` (enum: cook | manager | waiter)
- `provenance_token` (SHA-256 hash of entity state at event time)
- `witness_token` (optional FK to a `StockEntry` row that is the
  operational anchor for this audit record)
- `created_at` (timezone-aware UTC)

The `provenance_token` is the *checkable provenance* primitive; the
`witness_token` is the *runtime witnessing* primitive from feature
133 HANSARD.

## Implementation steps

None today (defer). When LE31 first considers an audit-trail
viewer surface for non-stock entities:

1. Load this artifact and the linked arXiv paper.
2. Load feature 133 HANSARD (runtime witnessing) — the two
   defer artifacts are companion documents.
3. Load feature 128 SKILL.state (the *opposite* of ECHO: replace
   append-only with structured state for chat history).
4. Decide whether the audit-record tables above are in scope for
   the v2 audit-trail surface.
5. If yes, design the ECHO-style auditable-memory-plane schema
   with `provenance_token` + `witness_token`.
6. If no, close this artifact.

## Telegram interaction if any

None. This is an architectural reference, not a user-facing feature.

## Dependencies

- LE31 charter §3.1 (append-only ledger invariant) — the audit
  records are *parallel* to the `StockEntry` ledger, not a
  replacement for it.
- LE31 charter §3.4 (observable evidence) — the audit records
  exist to make §3.4 queryable for non-stock entities.
- `features/128-skill-state-scalable-long-horizon-agent-skills.md`
  — companion observation: SKILL.state argues against append-only
  for chat history; ECHO argues for auditable for audit history.
  The two are complements, not contradictions.
- `features/133-hansard-runtime-witnessing-ledger-architecture.md`
  — companion observation: HANSARD supplies the
  `witness_token` primitive; ECHO supplies the `provenance_token`
  primitive. Together they form the auditable-memory-plane
  primitive.
- `features/108-telegram-chat-history-fuzzy-search-stockentry-audit.md`
  — companion observation for v2 audit-trail surface architecture.
- `features/121-ledger-commitment-field-tier-minimization.md` —
  related: provenance tokens can be the unit of disclosure
  minimisation.

## Open questions

- Does the v2 audit-trail surface need `provenance_token` (hash)
  or is a soft reference (FK to `StockEntry`) sufficient?
- Should the `witness_token` reference the *latest* `StockEntry`
  at event time, or the *specific* `StockEntry` that caused the
  event? The semantics differ: latest is cheaper, specific is
  more precise.
- Should `*AuditRecord` rows be themselves append-only (parallel
  to `StockEntry`) or updatable (correct for typical audit logs)?
  Paper is silent; LE31's charter §3.1 would suggest append-only.

## Why this matters

The ECHO paper is the second-strongest in-window arXiv signal of
the LE31 daily-research 30-pass series, complementary to feature
133 HANSARD. Together they supply two named primitives —
*checkable provenance* (ECHO) and *runtime witnessing* (HANSARD)
— that operationalise the *audit-trail* surface that LE31 v1
intentionally does not yet ship. Filing both defer artifacts today
costs near-zero and creates dated, in-window academic reference for
the next time LE31 considers an audit-trail viewer surface. The
papers are not features; they are a *vocabulary* for a future
feature.