# Feature 58 — Operator AI Action Surface

> **Priority**: P2 · **Effort**: M (≤1 week) · **Source**: brainstorm
> 2026-08-12 (cross-section pick A) · **Bucket**: **v2-AI** (new bucket —
> justified below).
> **One-line**: a permission-gated, evidence-traced *AI action surface*
> for the LE31 owner behind charter invariant *"AI may assist owner/
> staff, with observable evidence and a non-AI fallback"*, anchored by
> the just-pushed `sirquy/bestie` (153★, 2026-08-12).

## Bucket justification (new: v2-AI control-plane)

This is **v2-AI** (not v2 plain, not v1) because:

- Charter invariant "AI may assist owner/staff, with observable evidence
  and a non-AI fallback" is the *central* design constraint — not an
  ancillary one. A control plane for AI is its own bucket.
- v1 (features 01-08) is intentionally non-AI per charter. v2 (features
  09-18) is operator-pain polish on the existing product.
  v2-AI (features 19-22 in the research file) is *LLM-summarised*
  features (menu engineering, waste prediction, recipe generation,
  sentiment). This pick is **not** an LLM-summarised feature; it is a
  control-plane for *any* operator-facing AI surface (LLM or not).
- A new bucket name *v2-AI control-plane* is therefore the cleanest
  home. If a future pick duplicates it, this name holds.

## Goal

LE31 currently has no AI surface. v2-AI features (19-22) plan to add
LLM-summarised outputs. The charter says every AI action must (a) have
observable evidence and (b) have a non-AI fallback. Without a *control
plane* these two requirements are ad-hoc per feature.

`operator-ai-action-surface` ships that control plane **once**, as a
reusable piece:

- A single, well-typed Python module — `backend/app/services/
  ai_control_plane.py` — that **never** invokes an LLM itself; it only
  *dispatches* user-approved actions and writes them as append-only
  ledger events.
- One owner-only Telegram command, `/ai-actions`, that lists the last
  N AI action attempts with their evidence card and the owner decision
  (approve / edit / reject).
- A permission table — `backend/app/config.py::AI_PERMISSIONS = {...}`
  — that defaults to `*` (deny everything) and ships with one
  pre-approved permission per v2-AI feature as it lands.

The control plane does not own or weigh in on what the AI *does*;
that's each v2-AI feature's job. It owns:

1. The **permission table** (which actions are even allowed to
   surface to the owner for approval).
2. The **evidence card** (which `StockEntry`/`VoidRationale`/`AuditLog`
   rows back the AI's claim).
3. The **append-only audit row** (one new `AIActionAttempt` row per
   attempt; never updated, never deleted).
4. The **non-AI fallback path** (every action has a `/<action> manual`
   alias that runs the same effect with no model).

## Scope

**In scope (v2-AI control-plane, M effort):**

- `backend/app/services/ai_control_plane.py` (NEW) — `attempt()`,
  `approve()`, `reject()`, `permission_table_get()`,
  `fallback_path_for()`. Pure stdlib + SQLModel; no provider call.
- `backend/app/models/ai_action.py` (NEW, SQLModel) — `AIActionAttempt`
  (id, action_name, evidence_link_ids, status,
  proposed_payload, owner_decision_at, owner_id, created_at). ONE new
  table; one Alembic migration.
- `backend/app/bot/cook_bot.py` — register `/ai-actions`, `/approve
  <attempt_id>`, `/reject <attempt_id>`, and `/<action> manual`
  fallback dispatcher. Three new handlers; total ≤ ~50 lines.
- `backend/app/config.py` — `AI_PERMISSIONS = {"...": False, ...}`
  default-deny dict.
- `backend/tests/test_ai_control_plane.py` (NEW) — deterministic
  tests: default-deny, approve path, reject path, manual fallback
  path, append-only invariant.
- `backend/README.md` — note the permission table and the audit row.

**Out of scope (v2-AI control-plane v1):**

- **The AI itself.** No model integration. Every shipped `attempt()`
  call is a *stub* that returns a deterministic placeholder payload and
  a synthetic evidence card (`StockEntry` ids synthesized from a
  fixture file). Real model integration is each v2-AI feature's job
  (18+, 19+, 20+, etc.).
- **Per-feature prompts.** Each v2-AI feature registers its own
  `attempt()` caller; the control plane is the dispatcher, not the
  caller.
- **Owner-facing config UI.** Permissions are edited in
  `backend/app/config.py` for v1; a future v3 could surface them in
  the owner web UI.
- **Telemetry dashboard.** The audit table is queryable; the v3
  dashboard is a separate pick.

## Description

Three honest cross-section signals converged on 2026-08-12:

1. **`sirquy/bestie`** (153★, pushed 2026-08-12) — *Local-first AI
   action assistant for operators: memory, skills, tools, and
   permission gates to turn work into controlled action.* Same
   shape, just-pushed, mature star count. Strongest external anchor.
2. **`RobbieRao/hci-paper-writing`** (3★, pushed 2026-08-12) —
   *Open-source agent skill that diagnoses HCI contributions, traces
   claims to evidence, and red-teams papers before reviewers do.*
   The evidence-card + red-team UX is exactly the audit shape we need
   on the LE31 side.
3. **OpenAlex `Hakka Kitchen: Culinary Cultural Heritage Through
   Immersive Game Play`** (W7172068431, 2026-07-28) and **`UTAUT+
   generative AI identity and trust`** (W7171961487, 2026-07-31) —
   the literature has caught up: operator-facing AI is moving from
   tool to control surface.

LE31's job today is **not** to build a bestie-clone. LE31's job is to
build the *back-end* to a bestie-clone on top of the existing audit
tables, so the next v2-AI feature gets permission gating and an audit
trail for free.

## Data model

```sql
CREATE TABLE ai_action_attempt (
    id              BIGSERIAL PRIMARY KEY,
    action_name     TEXT NOT NULL,             -- e.g. "feature_19.suggest"
    proposed_payload JSONB NOT NULL,          -- what the AI wanted to do
    evidence_link_ids JSONB NOT NULL DEFAULT '[]'::jsonb,
        -- array of StockEntry/VoidRationale/AuditLog ids
    status          TEXT NOT NULL,             -- pending|approved|rejected|fallback
    owner_decision_at TIMESTAMPTZ,
    owner_id        INTEGER,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
-- APPEND-ONLY at the API layer: never UPDATE proposed_payload or
-- evidence_link_ids once written. Status transitions are a separate
-- AuditLog row, written by approve()/reject().
```

The existing `AuditLog` (feature 30) carries the human-readability; the
new `AIActionAttempt` carries the AI-decision-shape.

## Implementation steps

1. Add `backend/app/models/ai_action.py` with `AIActionAttempt`
   SQLModel.
2. Add Alembic migration `XXXX_add_ai_action_attempt.py`.
3. Add `backend/app/services/ai_control_plane.py` — `attempt()`,
   `approve()`, `reject()`, `permission_table_get()`,
   `fallback_path_for()`.
4. Add `AI_PERMISSIONS` to `backend/app/config.py` (default-deny).
5. Add 3 handlers to `backend/app/bot/cook_bot.py` (`/ai-actions`,
   `/approve <id>`, `/reject <id>`) and the `/<action> manual`
   dispatcher (1 line per registered action).
6. Add `backend/tests/test_ai_control_plane.py` (5 fixtures:
   default-deny, approve, reject, manual fallback, append-only).
7. Add `backend/README.md` section.

## Telegram interaction if any

- `/ai-actions` — owner-only. Returns last 10 attempts with the
  evidence-card link and a one-tap inline `/approve <id>` /
  `/reject <id>` reply.
- `/approve <attempt_id>` — owner-only. Marks the attempt approved,
  dispatches the action, writes the result to the existing ledger,
  and posts the result row to the owner.
- `/reject <attempt_id>` — owner-only. Marks rejected with a
  mandatory `/reject <attempt_id> reason=<text>` reason field.
- `/<action> manual` — owner-only. Bypass the AI path entirely, run
  the deterministic fallback, log an `AIActionAttempt` row with
  `status='fallback'`.

## Dependencies

- **Feature 30** (`append-only-audit-redirect`) — every AI action
  attempt writes an `AuditLog` row.
- **Feature 49** (`postledger-tamper-evident-hash`) — the
  `AIActionAttempt` rows participate in the same append-only hash
  chain.
- **Feature 47** (`decision-rationale-mixin`) — the `/reject`
  reason field uses the same rationale table.

No new pip dependencies. No schema change outside `ai_action_attempt`.

## Why this matters

LE31's charter invariant for AI is unambiguous (observable evidence +
non-AI fallback), but a control plane is the *only* way to enforce it
across v2-AI features without reinventing the audit row per feature.

`bestie` is the strongest OSS precedent in 30 days for an operator-
facing AI surface that is local-first and permission-gated. LE31 does
not need to compete with `bestie`. LE31 needs the *back-end* so that
when (not if) a future v2-AI feature wants to call `bestie`'s shape,
the audit and permission table already exist and the AI is just a
caller.

This is a **build, M effort, ≤1 week** pick. The risk is scope creep
("also do menu engineering, also do waste prediction"). The slice
boundary is hard: no model call inside the control plane, ever. A
feature that needs a model calls `attempt(...)` with a payload; the
control plane handles permission, evidence, audit, fallback.

## Open questions

- Should the permission table live in code (`config.py`) or in the DB
  so the owner can edit it at runtime? Recommendation: code (v1),
  promote to DB in v3.
- Should `/<action> manual` be owner-only or allow cook too?
  Recommendation: owner-only at v1; the cook already has feature 4
  (`menu-photo-bot`) and the stock bot for direct paths.
- Is `AIActionAttempt` evidence restricted to the existing three
  tables (`StockEntry`/`VoidRationale`/`AuditLog`)? Recommendation:
  yes for v1; the v3 follow-up could extend to `Order`/`OrderItem`
  and the new `OwnerRecap` table.

## Evidence (recorded)

- **Cross-section anchor 1**: `sirquy/bestie` (153★, pushed
  2026-08-12, Python). Read at
  `/tmp/le31-brainstorm-2026-08-12/gh_topic_telegram-bot.json`.
- **Cross-section anchor 2**: `RobbieRao/hci-paper-writing` (3★,
  pushed 2026-08-12, Python).
- **Cross-section anchor 3**: `dmirain/OctoForge` (20★, pushed
  2026-08-07) — typed Python core with Protocol ports, self-hosted
  agent platform for teams.
- **Literature anchor**: OpenAlex `Extending the UTAUT model to
  explore the acceptance and use of generative AI: the roles of
  generative AI identity and trust` (W7171961487, 2026-07-31).
- **Literature bound**: OpenAlex `Would you rely on an eerie agent?
  A systematic review of the impact of the uncanny valley effect on
  trust in human-agent interaction` (W4417084818, 2026-07-22).
- **Restaurant anchor**: `BethanyJep/Safaricom-Decode-Agents-
  Workshop` (16★, pushed 2026-07-16) — bilingual restaurant AI agent.
