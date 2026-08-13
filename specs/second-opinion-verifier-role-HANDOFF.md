# second-opinion-verifier-role — PARKING-LOT HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/63-second-opinion-verifier-role.md` before touching
> any code. Do not paste chat excerpts back into the build.
>
> **This slice is parked today.** Do not implement until both
> prerequisites (see *Status: PARKING-LOT* below) are resolved.

## Frozen identifiers (do not rename)

- Feature ID: `63`
- Slug: `second-opinion-verifier-role`
- Contract file: `features/63-second-opinion-verifier-role.md`
- Bucket: **v2-AI control-plane, long-lead (parking-lot)**
- Linear parent: HMM-71 (Brainstorm 2026-08-13 — daily)
- Linear sub-issue: HMM-74 (see `le31 v1 — Core MVP` project, label `Feature`, state **Backlog**; parking-lot convention matching feature 60 HMM-69)

## Status: PARKING-LOT (today)

Two prerequisites block implementation:

1. **Charter revision (§3.2 / §4 single-model assumption)** —
   the slice adds a *second model* in the dispatch chain
   (the verifier). Charter §4 assumes one LLM provider at
   most. A charter revision explicitly authorising
   multi-model orchestration must land before this slice
   passes the Conflict check in the seven-check feature gate.
2. **Operational prerequisite** — feature 55
   (`evidence-review-surface`) already covers the *"show
   receipts"* need; a verifier model adds cost without an
   observed LE31 pain. The natural unblock is when LE31 ships
   a *second* LLM provider, most plausibly a stronger
   multimodal model for the menu-photo OCR pipeline.

This file is preserved on disk so the slice is unblockable
without redoing the brainstorm once the prerequisites clear.
Until they do, the Linear sub-issue state stays **Backlog**;
no code lands.

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (`Frantz103/agent-os-opensource` pushed 2026-08-13,
1★, Python, Apache-2.0 — *"Local-first task, evidence, and
independent-review layer for AI coding runtimes"*;
`chiga0/marshal-harness` pushed 2026-08-13, Go, ★1 —
*"independent verification"*; OpenAlex `The Enterprise AI
Governance Buyer's Guide` DOI 10.5281/zenodo.18002693,
2026-07-16 — governance context). Confidence: **high** for
the cross-section pattern; **low** for the LE31 application
because of the charter constraint.

**Decision: parking-lot** (cross-section anchor is real; LE31
application is blocked by charter §4). Seven checks:

| Check | Verdict |
|---|---|
| 1. JTBD | ✓ but speculative until a second model is on the table. |
| 2. Viability | ✓ when unblocked. |
| 3. Practicability | ✗ currently; needs a second LLM provider not yet authorised. |
| 4. Conflict | ✗ **charter conflict** on the single-model assumption. |
| 5. Outcome / appetite | parked. |
| 6. Cost / value | unproven. |
| 7. Circuit breaker | covered by the parking-lot itself; deletion cost is zero code, one issue state change. |

## Mandatory LE31 skill list (load these first IF unblocking)

If a future agent unblocks this slice, the agent MUST load
before starting:

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

## Files the slice would touch when unblocked

```
backend/app/models/verification_report.py              # NEW: VerificationReport SQLModel
backend/alembic/versions/XXXX_add_verification_report.py # NEW: one migration
backend/app/services/verifier.py                       # NEW: verify() LLM-calling wrapper
backend/app/services/ai_control_plane.py              # EDIT: require pass report before exposing proposal
backend/app/config.py                                 # NEW: VERIFIER_MODEL_ID, LLM_BASE_URL_VERIFIER
backend/tests/test_verifier.py                         # NEW: 4 fixtures
backend/README.md                                     # note verifier policy + /verify-policy command
```

No new pip dependency expected (httpx is already used for the
first model call). One new SQLModel table. One new Alembic
migration.

## Endpoints and bot commands (when unblocked)

New bot command on the existing `cook_bot.py`:

- `/verify-policy` — owner-only. Prints the current verifier
  model id and whether the gate is `bypass`, `enforce`, or
  `insufficient-evidence-only`.

Extension to feature 58's `/ai-actions` reply card: a new
field `"verifier": "pass" | "reject" | "insufficient" |
"bypassed"`.

## Schema (VerificationReport, when unblocked)

```sql
CREATE TABLE verification_report (
    id                BIGSERIAL PRIMARY KEY,
    proposal_row_id   BIGINT NOT NULL REFERENCES decision_row(id),
    verifier_model_id TEXT NOT NULL,
    decision          TEXT NOT NULL,        -- pass|reject|insufficient_evidence
    rationale         TEXT,
    prev_hash         BYTEA NOT NULL,
    row_hash          BYTEA NOT NULL,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX verification_report_proposal_idx ON verification_report (proposal_row_id);
```

APPEND-ONLY at the API layer. Hash chain mirror of feature 49
+ feature 61.

## Default behaviour (when unblocked)

`VERIFIER_MODEL_ID = None` and `LLM_BASE_URL_VERIFIER = None`
both mean *bypass* — the proposal is shown to the owner
without any verifier row, matching today's v1 behavior. This
preserves the existing v2-AI control plane backward
compatibility.

## Rollback / feature-removal path

Set `VERIFIER_MODEL_ID = None`; verifier passes through. Or
delete the table with `alembic downgrade`; the control plane
calls verifier only when configured. Estimated rollback cost:
≤15 minutes.

## Files to verify against (when unblocking)

```
features/63-second-opinion-verifier-role.md
specs/second-opinion-verifier-role-HANDOFF.md          (this file)
features/58-operator-ai-action-surface.md             (parent)
features/61-holdfast-approval-ledger.md               (sibling)
features/62-agents-yaml-ontology-config.md            (sibling — verifier policy belongs in agents.yaml)
features/55-evidence-review-surface.md                (evidence-card pattern)
specs/operator-ai-action-surface-HANDOFF.md           (parent's hand-off)
specs/holdfast-approval-ledger-HANDOFF.md             (sibling's hand-off)
specs/agents-yaml-ontology-config-HANDOFF.md          (sibling's hand-off)
PROJECT_CHARTER.md                                    (check §3.2 + §4 for the conflict that blocks)
skills/le31-conventions/SKILL.md
skills/le31-v1-feature-pattern/SKILL.md
skills/le31-handoff-spec/SKILL.md
```
