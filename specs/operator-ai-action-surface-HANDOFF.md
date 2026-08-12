# operator-ai-action-surface — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/58-operator-ai-action-surface.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `58`
- Slug: `operator-ai-action-surface`
- Contract file: `features/58-operator-ai-action-surface.md`
- Bucket: **v2-AI control-plane** (NEW bucket name; justified in contract)
- Linear parent: HMM-66 (Brainstorm 2026-08-12 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (4 in-source anchors today: `sirquy/bestie` just-pushed
2026-08-12, 153★; `RobbieRao/hci-paper-writing` pushed 2026-08-12,
3★; `dmirain/OctoForge` 2026-08-07; OpenAlex W7171961487 + W4417084818
in-window). Confidence: **high**.

**Decision: build (v2-AI control-plane, M effort, ≤1 week).** No failed
checks; the only requirement is a written permission table at scope time.

The charter invariant *"AI may assist owner/staff, with observable
evidence and a non-AI fallback"* is the *central* design constraint,
not an ancillary one — a control plane for AI is its own bucket.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2-AI, the slicing discipline
   inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract
   back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/config.py                            # NEW: AI_PERMISSIONS = {"...": False, ...} default-deny
backend/app/models/ai_action.py                  # NEW: AIActionAttempt SQLModel
backend/alembic/versions/XXXX_add_ai_action_attempt.py   # NEW: one migration
backend/app/services/ai_control_plane.py         # NEW: attempt(), approve(), reject(), permission_table_get(), fallback_path_for()
backend/app/bot/cook_bot.py                      # EDIT: register /ai-actions, /approve <id>, /reject <id> handlers + /<action> manual dispatcher (~50 lines)
backend/tests/test_ai_control_plane.py           # NEW: 5 fixtures (default-deny, approve, reject, manual fallback, append-only)
backend/README.md                                # note the permission table + the audit row
```

No new pip dependencies. One new SQLModel table (`ai_action_attempt`).
One new Alembic migration.

## Endpoints and bot commands added

No new HTTP routes. New bot commands on the existing `cook_bot.py`:

- `/ai-actions` — owner-only. Returns last 10 attempts with the
  evidence-card link and a one-tap inline `/approve <id>` /
  `/reject <id>` reply.
- `/approve <attempt_id>` — owner-only. Marks approved, dispatches
  the action, writes the result row to the existing ledger.
- `/reject <attempt_id> reason=<text>` — owner-only. Marks rejected
  with a mandatory reason field.
- `/<action> manual` — owner-only. Bypass the AI path, run the
  deterministic fallback.

The `/reject` reason field uses the existing `VoidRationale` schema
(feature 47). The dispatch path writes to the existing
`AuditLog` (feature 30) — no new audit infrastructure.

## Schema (AIActionAttempt)

```sql
CREATE TABLE ai_action_attempt (
    id              BIGSERIAL PRIMARY KEY,
    action_name     TEXT NOT NULL,
    proposed_payload JSONB NOT NULL,
    evidence_link_ids JSONB NOT NULL DEFAULT '[]'::jsonb,
    status          TEXT NOT NULL,             -- pending|approved|rejected|fallback
    owner_decision_at TIMESTAMPTZ,
    owner_id        INTEGER,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

APPEND-ONLY at the API layer: never UPDATE `proposed_payload` or
`evidence_link_ids` once written. Status transitions are a separate
`AuditLog` row.

## Permission table (default-deny)

```python
# backend/app/config.py
AI_PERMISSIONS: dict[str, bool] = {
    # pre-approved per v2-AI feature as it ships:
    "feature_19.menu_engineering_suggest": False,
    "feature_20.waste_prediction_suggest": False,
    "feature_21.recipe_generation_suggest": False,
    # everything else: not in the dict => deny
}
```

The permission check is `permission_table_get()` — key lookup; if the
key is missing or `False`, return denied without invoking the action.

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent MUST:

1. Unit-test default-deny: assert that an attempt with an action name
   not in the permission table returns denied without writing a row.
2. Unit-test approve path: assert `approve(id)` writes the result row
   to the destination table and the `AIActionAttempt` is marked
   `approved` (status transition only).
3. Unit-test reject path: assert `reject(id, reason)` writes the
   reason to `VoidRationale` and the `AIActionAttempt` is marked
   `rejected`.
4. Unit-test manual fallback path: assert `/<action> manual`
   produces the same destination row as `/approve <id>` plus the
   `AIActionAttempt.status='fallback'` flag.
5. Append-only test: assert that a second `UPDATE proposed_payload
   ...` raises an explicit error (or is silently ignored).

After implementation, run the parent's verify-before-fixing protocol
on the slice branch.

## Rollback path

- This slice adds a feature flag `AI_CONTROL_PLANE_ENABLED=0` (default
  OFF in the first deploy). The dispatcher short-circuits to the
  existing v1 paths when the flag is OFF.
- The `ai_action_attempt` table is a new SQLModel; the migration is
  reversible. Dropping the table + the handler is a single PR.
- Reversible in <5 min: env-set + restart.

## What is explicitly NOT in this slice

- **No model call.** The control plane never invokes an LLM. It only
  *dispatches* user-approved actions and writes them as append-only
  ledger events.
- **No per-feature prompts.** Each v2-AI feature registers its own
  `attempt()` caller.
- **No owner-facing config UI.** Permissions edited in `config.py`
  for v1.
- **No telemetry dashboard.** The audit table is queryable; the v3
  dashboard is a separate pick.

## Charter conformance

- Charter invariant: *"AI may assist owner/staff, with observable
  evidence and a non-AI fallback."* ✓ — the slice exists precisely
  to enforce this invariant *across* v2-AI features.
- Stock invariant: A new `StockEntry` row is written only when an
  AI action writes one; the control plane never synthesizes a
  StockEntry directly. ✓
- State invariant: All AI actions require explicit owner approval
  (`approve()` or `manual` fallback). No automatic transitions. ✓
- Money invariant: N/A at v1 — the slice ships with no model, no
  payments. v2-AI features that touch money (e.g. feature 19 menu
  engineering) must layer their money derivation on top of this
  slice.
