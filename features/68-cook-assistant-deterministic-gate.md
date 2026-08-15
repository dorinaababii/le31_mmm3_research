# Feature 68 — Cook Assistant Deterministic Gate

> **Priority**: P2 · **Effort**: M (≤1 week) · **Source**: brainstorm 2026-08-15
> (cross-section pick B) · **Bucket**: v2-AI
> **One-line**: A new `AssistantProposal` table (append-only, human-readable, one
> isolated store per consumer — exactly the `4242labs/memento` shape) that the
> v2-AI cook-assistant writes to **before** any `StockEntry` is committed. The
> proposal then runs the same deterministic gate the typed `/86 <item>` path
> enforces; only on gate-pass does the candidate promote into the live
> `StockEntry` ledger with the proposal row preserved for audit.

## Goal

Close the LE31 v2-AI safety gap: today every v2-AI feature (07 demand
forecasting, 17 demand-forecasting ML, 19 menu engineering, 20 waste
prediction, 21 recipe generation, 51 cook-coach parking-lot) that wants to
write a `StockEntry` has to re-invent the gate logic. There is no shared
"AI proposes, gate decides" primitive. Charter §3.3 (the non-AI fallback
rule) requires that AI cannot silently change state — but today the gate
implementation lives inside each v2-AI feature's bot reply handler, and the
audit chain for *rejected* proposals lives nowhere.

A single `AssistantProposal` table (append-only, never mutated, never
deleted) gives every v2-AI feature one place to:
1. write a candidate `StockEntry` row before committing;
2. run the existing deterministic gate (same rules as the typed
   `/86 <item>` path);
3. preserve both the *proposed* and *rejected* decision in the audit
   chain;
4. reference the proposal from the live `StockEntry` row (via a new
   `proposal_id` FK) for full traceability.

Inspired by today's brainstorm: GitHub `topic:append-only` repo
`4242labs/memento` (pushed **2026-08-14T20:34:45Z**, 0★, "Long-term memory
for LLM agents — the model proposes, deterministic gates decide.
Append-only, human-readable, one isolated store per consumer."). The repo
comes from the LLM-agent infrastructure world — completely outside
hospitality — and **directly answers the open question documented in
feature 51's parking-lot contract**: *what is the right shape for the
cook-side AI-coach to commit a `StockEntry` decision?* The answer is exactly
the `memento` shape: **the model proposes, the gate decides, both decisions
are append-only and human-readable, the proposal is never mutated, the live
ledger entry carries a pointer back to the proposal.**

The OpenAlex arXiv 2607.27553 + SAGE EXPRESS pair on "AI and Its Impact on
Creativity and Diversity: An Empirical Study of LLM-Generated Product
Ideas" (2026-07-22 + 2026-07-30) is the academic backdrop for the
"LLM-as-product-ideator" pattern this slice operationalises for the
restaurant surface.

This feature is **independent** — does not require Pick A, Pick C, or any
new feature. Requires the existing `StockEntry` table + the business-rule
gate logic from feature 37.

## Evidence / JTBD

When the v2-AI cook-assistant wants to write a `StockEntry` (e.g. an
AI-generated prep-board forecast that says "ricotta will stock out in 30
minutes" → "86 ricotta now"), the AI wants to record the decision and the
reason, but struggles because the AI cannot silently mutate the
append-only ledger (charter §3.3), so that the assistant first writes a
candidate `AssistantProposal` row, then the deterministic gate runs the same
business rules as the typed `/86 <item>` path, and only if the gate passes
is the candidate promoted into the live `StockEntry` ledger with the
proposal row preserved for audit.

## Scope

**In scope (v2-AI):**
- A new append-only `AssistantProposal` SQLModel table
  `(id, created_at, source, menu_item_id, qty_delta, rationale_proposed,
  status, gate_reason, promoted_stockentry_id)` where:
  - `source` is the assistant identifier (e.g.
    `menu-engineering:demand-forecast`, `cook-coach:voice-proposal`,
    `waste-prediction:prep-shortfall`).
  - `status` is one of `pending`, `promoted`, `rejected` (set once at gate
    resolution; never updated afterwards — the table is append-only).
  - `gate_reason` is the human-readable reason the gate passed or failed
    (set at gate resolution).
  - `promoted_stockentry_id` is the FK to the live `StockEntry` row if the
    gate passed; NULL if the gate failed.
- A new module `backend/app/services/assistant_gate.py` exposing:
  - `propose(source: str, menu_item_id: int, qty_delta: int,
    rationale_proposed: str) -> AssistantProposal` — writes the pending
    proposal, returns the row.
  - `resolve(proposal: AssistantProposal) -> AssistantProposal` — runs the
    deterministic gate, sets `status` + `gate_reason` + (if promoted)
    `promoted_stockentry_id`, returns the resolved row.
  - `gate_for_stockentry(...)` — the actual gate, lifted from feature 37's
    `validate_void_rationale()` and the typed `/86 <item>` handler in the
    cook bot. **No new gate logic** — same rules, same allowlist, same
    money/time invariants.
- A new column on `StockEntry`:
  `proposal_id: int | None = Field(default=None, foreign_key="assistantproposal.id")`
  — NULL for typed `/86` writes; non-NULL for AI-proposed writes. Set once
  at insert time; never updated.
- The existing cook bot's typed `/86 <item> <reason>` command path stays
  unchanged. The new `propose()` + `resolve()` path is for v2-AI features
  only; the typed path remains the non-AI fallback.
- A new bot reply path that v2-AI features call when the gate fails: the
  bot replies to the cook (not the AI) with "I tried to write the 86 but
  the gate failed: <gate_reason>". The reply goes to the cook's Telegram
  chat-id (not to the AI).

**Out of scope (v2-AI):**
- Multi-row proposals (one AI write → many `StockEntry` rows). Out of scope
  for the first slice; defer to v3.
- AI-side retries — if the gate fails, the proposal is rejected and the
  AI does not retry. The cook gets the bot reply and decides whether to
  type the variant manually.
- Approval workflows (a second human must approve AI-proposed writes).
  The deterministic gate IS the approval; if the owner wants a second
  human in the loop, that's a separate feature.
- Cross-restaurant `AssistantProposal` — one isolated store per
  restaurant, exactly as `memento`'s "one isolated store per consumer".

## User flow

**AI proposes; gate passes; StockEntry is written:**

1. The cook-coach (feature 51) generates a candidate: "ricotta will stock
   out at 21:30 based on tonight's covers × avg usage."
2. The cook-coach calls `assistant_gate.propose(source='cook-coach:voice-proposal',
   menu_item_id=ricotta_id, qty_delta=-1, rationale_proposed='forecast stockout
   at 21:30')`. A pending `AssistantProposal` row is written.
3. `assistant_gate.resolve(proposal)` runs the deterministic gate:
   - item exists: ✅
   - prep window valid: ✅
   - owner allowlist (negative delta): ✅ (cook is allowed)
   - business day matches Europe/Paris: ✅
   - EUR/tax invariants preserved: ✅ (no money touched)
4. Gate passes. `status='promoted'`, `gate_reason='all checks passed'`,
   `promoted_stockentry_id=<new StockEntry.id>`. A new `StockEntry` row is
   written with `proposal_id=<AssistantProposal.id>`, `rationale='forecast
   stockout at 21:30'`, `qty_delta=-1`, `source='assistant:cook-coach'`.
5. Cook gets a Telegram reply: "Forecast noted: ricotta 86 at 21:30 (gate
   passed; proposal #1234)."

**AI proposes; gate fails; nothing is written:**

1. The cook-coach generates a candidate: "I think we should 86 the lamb
   because covers are low." Calls `propose(...)`.
2. `resolve(proposal)` runs the gate. Gate fails on one rule: `lamb` was
   already 86ed today via the typed `/86 lamb` path at 18:00, so the
   ledger already has a negative `StockEntry` for `lamb` with a rationale;
   a second negative entry would create a "double 86" that violates the
   business rule that you can only 86 an item once per service.
3. `status='rejected'`, `gate_reason='already 86ed today (StockEntry #567)
   — refusing duplicate'`. **No `StockEntry` row is written.**
4. Cook gets a Telegram reply: "I tried to write the 86 but the gate
   failed: already 86ed today (StockEntry #567) — refusing duplicate."

**Cook types the manual fallback:**

1. Cook replies `/86 lamb we ran out` to the cook bot. The typed path is
   unchanged — it writes a `StockEntry` directly with `proposal_id=NULL`
   and `rationale='we ran out'`.

## Data model

One new table:

```python
# backend/app/models.py (additive)

class AssistantProposal(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    source: str = Field(max_length=80, index=True)  # 'cook-coach:voice-proposal' | 'menu-engineering:demand-forecast' | ...
    menu_item_id: int = Field(foreign_key="menuitem.id", index=True)
    qty_delta: int
    rationale_proposed: str = Field(max_length=500)
    status: str = Field(max_length=20)  # 'pending' | 'promoted' | 'rejected' — set ONCE at gate resolution
    gate_reason: str = Field(max_length=500)
    promoted_stockentry_id: int | None = Field(default=None, foreign_key="stockentry.id", index=True)
```

`AssistantProposal` is append-only (new `assistantproposal_append_only.py`
listener — `status` is set ONCE at gate resolution; `gate_reason` and
`promoted_stockentry_id` are set ONCE at gate resolution; no `UPDATE` or
`DELETE` paths exist).

One new column on `StockEntry`:

```python
# backend/app/models.py (additive)
class StockEntry(SQLModel, table=True):
    ...  # existing fields unchanged
    proposal_id: int | None = Field(default=None, foreign_key="assistantproposal.id", index=True)
```

`StockEntry.proposal_id` is NULL for typed writes; non-NULL for AI-proposed
writes. Set once at insert time; never updated.

No changes to other existing models. Reuses the existing business-rule gate
from feature 37.

## API / bot / UI contract

**Bot (aiogram v3, existing webhook from feature 04):**
- No new bot commands. The typed `/86 <item> <reason>` path stays
  unchanged (the non-AI fallback).
- A new internal handler used by v2-AI features: when an
  `AssistantProposal` is rejected, the bot sends a Telegram reply to the
  cook with the gate reason. The handler is registered as a callback; it
  is not exposed as a `/command`.

**API (FastAPI):**
- No new HTTP routes. The gate is an internal service module.
- Existing routes unchanged.

**Service module:**
- `backend/app/services/assistant_gate.py` — `propose()` and `resolve()`
  functions as described above. Lifts the existing gate logic from
  feature 37's `validate_void_rationale()` and the typed `/86 <item>`
  handler.

## Dependencies

- **No new pip dependencies.** The gate uses existing models, existing
  validators, existing aiogram primitives.
- **Required upstream features**:
  - feature 37 (`void-rationale-ledger-field`) — supplies the
    `rationale` column and the existing gate logic that the new gate
    reuses. Without 37, there is no business-rule gate to lift.
- **Required downstream features**: every future v2-AI feature that wants
  to write a `StockEntry` should call `assistant_gate.propose()` +
  `assistant_gate.resolve()` instead of writing directly. The contract
  documents this requirement.

## Failure / recovery

- **Gate fails** — `AssistantProposal` is written with `status='rejected'`,
  `gate_reason=<reason>`. **No `StockEntry` is written.** Cook gets a
  Telegram reply with the gate reason. The rejected proposal row stays in
  the audit chain.
- **Database error during `propose()`** — the `AssistantProposal` insert
  fails; no `StockEntry` is written; the v2-AI feature gets an exception
  it can retry. The retry will create a *new* proposal row (not a duplicate
  of the failed one).
- **Database error during `resolve()` after a successful `propose()`** —
  the pending proposal row stays in the audit chain with
  `status='pending'`. A reconciliation cron (out of scope for v1) can find
  pending proposals older than N seconds and reject them with
  `gate_reason='stale pending — resolve failed'`. Add to Open Questions
  for v1 follow-up.
- **LLM is unavailable** — the typed `/86 <item> <reason>` path is always
  available (charter §3.3 non-AI fallback). No silent failure.
- **Owner disabled the AI surface** — a new config field
  `AI_PROPOSALS_ENABLED: bool = True` (default True). When False,
  `assistant_gate.propose()` raises a `ProposalsDisabledError`; v2-AI
  features catch and degrade to "AI unavailable, please type `/86 <item>
  <reason>`" reply.

## Definition of done

- [ ] `AssistantProposal` table added; append-only listener extended.
- [ ] `StockEntry.proposal_id` column added (nullable FK, indexed).
- [ ] `backend/app/services/assistant_gate.py` shipped with `propose()`
      and `resolve()` functions.
- [ ] Gate logic verified to be **identical** to the typed `/86 <item>`
      path's gate (regression test: for every rule the typed path
      enforces, the assistant gate enforces the same rule).
- [ ] Bot reply path for rejected proposals shipped (cook gets a Telegram
      message with the gate reason).
- [ ] `AI_PROPOSALS_ENABLED` config field shipped (default True).
- [ ] End-to-end observed: cook-coach proposes a candidate → gate passes
      → `StockEntry` written with `proposal_id=<id>` → cook gets the
      "forecast noted" reply. Cook-coach proposes a second candidate that
      violates the "already 86ed today" rule → gate fails → no `StockEntry`
      written → cook gets the "gate failed" reply.
- [ ] Existing tests still green.
- [ ] Manual acceptance: in a 7-day pilot, the v2-AI cook-coach surface
      proposes ~10 candidates per day, the gate passes ~9, the gate fails
      ~1 (e.g. double-86), and every proposal is preserved in the audit
      chain (zero silent mutations of `StockEntry`).

## Open questions

- Should the v2-AI feature be told why the gate failed, or just that it
  failed? Decision: tell the feature, but not the LLM prompt — the gate
  reason is logged in `AssistantProposal.gate_reason` for the owner to
  read later, but the AI's reply is just "gate failed" without the reason
  (charter §3.3: no PII / no operational data leaves the box).
- Should `AssistantProposal.status` allow re-resolution after a temporary
  DB failure? Decision: no — the table is append-only; a reconciliation
  cron (out of scope for v1) handles stale `pending` rows.
- Should the v2-AI feature have a "preview" endpoint so the cook can see
  the candidate before the gate runs? Decision: no — the deterministic
  gate is fast and the proposal is already logged before the gate runs
  (cook can see it in the audit chain).
- Should the `AssistantProposal` table be per-restaurant or shared?
  Decision: per-restaurant (one isolated store per consumer, exactly as
  `memento`'s pattern).

## Why this matters

LE31's charter §3.3 requires that AI cannot silently change state. Today
every v2-AI feature that wants to write a `StockEntry` has to re-invent the
gate logic; there is no shared primitive. The two in-window real-world peers
that name this exact primitive are:

- `4242labs/memento` (pushed 2026-08-14) — "the model proposes, deterministic
  gates decide. Append-only, human-readable, one isolated store per
  consumer." **Direct inspiration for this slice.**
- `dallascrilley/holdfast` (pushed 2026-08-12, already filed as feature 61
  `holdfast-approval-ledger`) — "an append-only decision ledger with a
  human approval gate: AI can propose, only a person can publish."

Both come from LLM-agent infrastructure / approval-ledger engineering —
completely outside hospitality — and share the same primitive: **the model
proposes, the gate decides, both decisions are append-only and
human-readable, the proposal is never mutated, the live ledger entry carries
a pointer back to the proposal.**

Translated to LE31, this is the missing gate that lets every v2-AI feature
(features 07, 17, 19, 20, 21, 48, 51) safely write to `StockEntry` without
violating charter §3.3. Medium cost (one new table + one new column + one
service module + one bot reply path), high value (this is the primitive
that makes every LE31 v2-AI feature safely AI-driven; without it, every
v2-AI feature has to re-invent the gate).
