# Pick B — `fuleinist/csl` — v2-AI agent-guardrails-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/258-fuleinist-csl-mit-common-sense-layer-agent-harnesses-one-line-falsifiable-rules-append-only-validation-ledger-claude-code-codex-hermes-openclaw-v2-ai-agent-guardrails-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2-AI PR that adds a `GuardrailRule` SQLModel table, a `ValidationLedgerEntry` SQLModel table, or a YAML/JSON config file encoding the seven-check feature gate (per `le31-conventions/SKILL.md`) as 7 one-line-falsifiable rules.
2. First v2-AI PR that adds a `/rules list` / `/rules show <rule_id>` / `/rules evaluate <rule_id> <input>` Telegram command set on the cook-bot (operator-tooling only; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**).
3. First v2-AI PR that adds a Hermes Agent hook integration that enforces the guardrail rules against incoming research picks.
4. First v2-AI PR that exposes a *public-read-only* guardrail-rule-evaluation-results endpoint (requires charter §3.4 amendment).

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When the Hermes-driven agent pipeline (which orchestrates the daily-research cron + the daily-brainstorm cron + the le31-feature-pipeline cron) encounters a research pick that fails the seven-check gate, it currently logs the failure to stdout and skips the pick; the owner/staff want a clear string view of which rule was violated and why, but struggle because the seven-check gate is enforced ad-hoc, so that every agent decision carries a falsifiable-rule reference and an append-only validation ledger entry."* — PASS (links to feature 237 as adjacent v2-AI markdown-contextlib vocabulary; justifies a new pain)
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the falsifiable-rule-report outputs. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 NOT triggered (operator-tooling AI, not customer-facing AI); `hermes-agent` topic = direct transferability; confidence **medium-high** for mechanism, **low** for present urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling-AI; §3.4 NOT triggered; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v2-AI** outcome (cross-section to features 230+236+237+243). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low-medium today (the daily-research cron runs once per day; ad-hoc gate-enforcement is acceptable for now); pain is forecast for v2-AI era. Implementation cost = low-medium (~100-200 lines of Hermes-skill code; 1-3 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/guardrail.py` (new) — `GuardrailRule` + `ValidationLedgerEntry` SQLModel tables
- `le31/app/services/guardrail.py` (new) — service layer for `register_rule` + `evaluate_rule` + `list_validation_ledger` + `verify_rule_evaluation`
- `le31/config/guardrail_rules.yaml` (new) — YAML config file encoding the seven-check feature gate as 7 one-line-falsifiable rules (Practicability + Conflict + Outcome are the 3 that are one-line-falsifiable; the remaining 4 require multi-line structured inputs and are out-of-scope for the initial implementation)
- `le31/app/api/v1/guardrail.py` (new) — HTTP endpoints: `GET /api/guardrail/rules` + `GET /api/guardrail/rules/<rule_id>` + `POST /api/guardrail/evaluate/<rule_id>` + `GET /api/guardrail/validation-ledger`
- `le31/app/cook_bot/handlers/guardrail.py` (new) — Telegram command handlers: `/rules list` + `/rules show <rule_id>` + `/rules evaluate <rule_id> <input>` (operator-tooling only; NOT customer-facing)
- `le31/hermes_hooks/guardrail.py` (new) — Hermes Agent hook integration: `pre_research_pick` hook that calls `evaluate_rule` for each of the 7 one-line-falsifiable rules and records the result in the `ValidationLedgerEntry` table
- `le31/migrations/versions/<revision>_guardrail.py` (new) — Alembic migration for the two new tables
- `skills/le31-conventions/SKILL.md` — append the *falsifiable-rules-as-encoded-commonsense-layer* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the two new tables
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/guardrail.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the Telegram command handlers** (remove the `le31/app/cook_bot/handlers/guardrail.py` file + remove the registration from `le31/app/cook_bot/handlers/__init__.py`)
- **Revert the Hermes Agent hook integration** (remove the `le31/hermes_hooks/guardrail.py` file + remove the registration from `le31/hermes_hooks/__init__.py`)
- **Revert the YAML config file** (delete `le31/config/guardrail_rules.yaml`)
- **No data loss** if the rollback happens BEFORE any guardrail-rule-evaluation rows are written
- **Full data retention** if the rollback happens AFTER rows are written (the two tables are dropped but the guardrail-rule-evaluation rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked] (workspace plan-limit error — 12th consecutive day; verified today via `save_issue` write-probe with requestId `a4396da65c72d371`; parent fallback at `/opt/data/le31-daily-research-2026-10-01.linear-fallback.json`)