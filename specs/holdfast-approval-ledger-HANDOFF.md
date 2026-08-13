# holdfast-approval-ledger — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/61-holdfast-approval-ledger.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `61`
- Slug: `holdfast-approval-ledger`
- Contract file: `features/61-holdfast-approval-ledger.md`
- Bucket: **v2-AI control-plane** (companion to feature 58)
- Linear parent: HMM-71 (Brainstorm 2026-08-13 — daily)
- Linear sub-issue: HMM-72 (see `le31 v1 — Core MVP` project, label `Feature`; matches the v2-AI control-plane sub-issue convention used by feature 58 HMM-67)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (`dallascrilley/holdfast` pushed 2026-08-12, MIT,
TypeScript, ★0, same-shape anchor; `chiga0/marshal-harness`
pushed 2026-08-13, Go, ★1, corroborating anchor). Confidence:
**high**.

**Decision: build (v2-AI control-plane companion, M effort,
≤1 week).** Seven checks all pass: no charter conflict, fits the
fixed stack, ≤80 lines added to feature 58's service module,
reuses features 30 + 47 + 49 + 50 + 55 + 58, circuit-breaker is
"disable the propose()/decide() calls; the dispatcher still works
on its own".

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2-AI, the slicing discipline
   inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror
   contract back).
4. `le31-daily-brainstorm` (this pick came from the daily
   brainstorm job on 2026-08-13).
5. `le31-feature-pipeline` (so the agent understands how this
   slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request
them from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/models/decision_ledger.py                     # NEW: DecisionRow SQLModel
backend/alembic/versions/XXXX_add_decision_ledger.py      # NEW: one migration
backend/app/services/decision_ledger.py                   # NEW: propose(), decide(), chain_for(), audit_dump()
backend/app/services/ai_control_plane.py                  # EDIT: 3 functions, ≤80 lines added
backend/app/bot/cook_bot.py                               # EDIT: /decisions handler, extend /approve /reject (≤30 lines)
backend/tests/test_decision_ledger.py                     # NEW: 5 fixtures
backend/scripts/verify_decision_chain.py                  # NEW: read-only CLI
backend/README.md                                         # note the new table + /decisions command
```

No new pip dependencies. One new SQLModel table. One new
Alembic migration. Reuses the `prev_hash → row_hash` helper
from feature 49 — do not reimplement.

## Endpoints and bot commands added

No new HTTP routes. New bot command on the existing
`cook_bot.py`:

- `/decisions` — owner-only. Returns last 10 `DecisionRow`
  entries with attempt id, kind, actor kind, and a one-line
  rationale (if present). Distinct from feature 55's
  `/explain` and feature 58's `/ai-actions`.

Existing commands extended:

- `/approve <attempt_id>` — reply card now reports both the
  `attempt_id` and the new `decision_row` id.
- `/reject <attempt_id> reason=<text>` — reply card now
  reports both ids.
- `/<action> manual` — invokes the fallback dispatcher,
  which now writes one `DecisionRow(kind='fallback_dispatch')`
  automatically.

## Schema (DecisionRow)

```sql
CREATE TABLE decision_row (
    id              BIGSERIAL PRIMARY KEY,
    kind            TEXT NOT NULL,           -- ai_proposal|owner_decision|fallback_dispatch
    attempt_id      BIGINT NOT NULL REFERENCES ai_action_attempt(id),
    evidence_id     BIGINT,                  -- optional EvidenceLink row id (feature 55)
    payload         JSONB NOT NULL,
    rationale       TEXT,                    -- owner rationale (for kind=owner_decision)
    actor_kind      TEXT NOT NULL,           -- 'ai' | 'owner' | 'system'
    actor_id        INTEGER,
    prev_hash       BYTEA NOT NULL,
    row_hash        BYTEA NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX decision_row_attempt_kind_idx ON decision_row (attempt_id, kind);
CREATE INDEX decision_row_created_at_idx   ON decision_row (created_at);
```

APPEND-ONLY at the API layer: never UPDATE or DELETE a
`decision_row` row once written. `propose()` and `decide()`
are the only writers; read paths are `chain_for()` and
`audit_dump()`. Status transitions of an AI action attempt
are a separate `AuditLog` row (feature 30).

## Hash chain reference

Reuse `backend/app/services/postledger_hash.py` (feature 49).
`row_hash = sha256(prev_hash || row_json_canonical())`. The
canonicalisation function already exists for feature 49's
ledger; do not reimplement.

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent
MUST:

1. Write all 5 test fixtures; `pytest backend/tests/test_decision_ledger.py`
   must pass.
2. Manually exercise the new `/decisions` command on the
   Telegram bot in the dev environment, observing the
   proposal/decision row pair for one real `/approve` cycle.
3. Run `python -m backend.scripts.verify_decision_chain.py <attempt_id>`
   and confirm both rows print.
4. Confirm the `decision_row` rows are NOT visible to the cook
   or waiter (only owner chat ids see them).
5. Update `features/61-holdfast-approval-ledger.md`'s
   "Dependencies" section if any new file lands.

## Rollback / feature-removal path

The control plane (feature 58) keeps working when
`decision_ledger.propose()` and `.decide()` calls are removed;
delete the calls, leave the empty migration in place (the
`decision_row` table can be dropped by `alembic downgrade`).
Estimated rollback cost: ≤1 hour + one alembic downgrade.

## Files for the coding agent to verify against

```
features/61-holdfast-approval-ledger.md
specs/holdfast-approval-ledger-HANDOFF.md              (this file)
features/58-operator-ai-action-surface.md             (parent)
features/55-evidence-review-surface.md                (evidence-card sibling)
features/49-postledger-tamper-evident-hash.md         (hash chain sibling)
specs/operator-ai-action-surface-HANDOFF.md           (parent's hand-off)
specs/postledger-tamper-evident-hash-HANDOFF.md       (hash-chain sibling's hand-off)
skills/le31-conventions/SKILL.md
skills/le31-v1-feature-pattern/SKILL.md
skills/le31-handoff-spec/SKILL.md
PROJECT_CHARTER.md
```
