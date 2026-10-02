# Pick B — `random-guy-05/vec-runlog` — v2-AI append-only-submission-ledger-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/261-random-guy-05-vec-runlog-mit-append-only-experiment-submission-provenance-ledger-virtual-embryo-challenge-v2-ai-append-only-submission-ledger-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2-AI PR that adds an `ExperimentLedgerEntry` SQLModel table (`entry_id, experiment_id, experiment_name, input_payload, output_payload, recorded_at`).
2. First v2-AI PR that adds a `SubmissionLedgerEntry` SQLModel table (`submission_id, submission_name, submitter_id, parent_experiment_id, parent_lineage_hash, recorded_at`).
3. First v2-AI PR that adds an `ExperimentChallenge` SQLModel table (`challenge_id, challenge_name, challenge_start_at, challenge_end_at, challenge_status`).
4. First v2-AI PR that extends the existing `audit_logs` table with `experiment_id` + `submission_id` columns.
5. First v2-AI PR that adds a `/submission list` / `/submission show <submission_id>` / `/submission verify <submission_id>` Telegram command set on the cook-bot (operator-tooling only; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**).
6. First v2-AI PR that adds a Hermes Agent experiment-execution-recording extension that records every experiment-execution as an immutable row in `audit_logs`.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When the Hermes agent files a feature pick, it wants to record the pick as an immutable `SubmissionLedgerEntry` (append-only + submission-provenance), but struggles because the current INDEX.md + GitHub commit + features/<slug>.md triple is not provably tamper-evident, so that the *who-filed-what-when* lineage is verifiable by the agent."* — PASS (links to features 03 + 121 + 257 + 258 + 259; justifies a new pain).
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the *pick-lineage* + *pick-verification* outputs. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 not triggered (no AI surface); confidence **high** for vocabulary transferability, **low** for immediate LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling only; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v2-AI** outcome (cross-section to features 03+121+257+258+259). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = low-medium (~20-50 lines of SQLModel + hash-chained-append-only code; 1-2 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/submission_ledger.py` (new) — `ExperimentLedgerEntry` + `SubmissionLedgerEntry` + `ExperimentChallenge` SQLModel tables
- `le31/app/services/submission_ledger.py` (new) — service layer for `record_experiment` + `record_submission` + `verify_submission` + `verify_lineage`
- `le31/app/hermes/hooks/experiment_recording.py` (new) — Hermes Agent hook integration that records every experiment-execution as an immutable row in `audit_logs`
- `le31/app/api/v1/submission_ledger.py` (new) — HTTP endpoints: `GET /api/submissions` + `GET /api/submissions/<submission_id>` + `POST /api/submissions/<submission_id>/verify` + `GET /api/experiments/<experiment_id>` + `GET /api/challenges`
- `le31/app/cook_bot/handlers/submission_ledger.py` (new) — Telegram command handlers: `/submission list` + `/submission show <submission_id>` + `/submission verify <submission_id>` (operator-tooling only; NOT customer-facing)
- `le31/migrations/versions/<revision>_submission_ledger.py` (new) — Alembic migration for the three new tables + the two new `audit_logs` columns
- `skills/le31-conventions/SKILL.md` — append the *append-only-experiment-ledger + submission-provenance-ledger + challenge-context* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the three new tables + revert the two new `audit_logs` columns
- **Revert the submission-ledger service** (remove the `le31/app/services/submission_ledger.py` file + remove the import from `le31/app/services/__init__.py`)
- **Revert the Hermes Agent hook** (remove the `le31/app/hermes/hooks/experiment_recording.py` file + remove the hook registration from `le31/app/hermes/hooks/__init__.py`)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/submission_ledger.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the Telegram command handlers** (remove the `le31/app/cook_bot/handlers/submission_ledger.py` file + remove the registration from `le31/app/cook_bot/handlers/__init__.py`)
- **No data loss** if the rollback happens BEFORE any submission-ledger-row is written
- **Full data retention** if the rollback happens AFTER rows are written (the three tables are dropped but the submission-ledger rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked] (workspace plan-limit error — 13th consecutive day; verified today via `save_issue` write-probe with requestId `a441ca79aa0965da`; parent fallback at `/opt/data/le31-daily-research-2026-10-02.linear-fallback.json`)