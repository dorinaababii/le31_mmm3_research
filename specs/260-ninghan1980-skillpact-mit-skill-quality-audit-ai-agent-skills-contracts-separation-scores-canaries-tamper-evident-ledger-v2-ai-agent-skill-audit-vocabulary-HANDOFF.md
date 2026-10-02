# Pick A — `ninghan1980/skillpact` — v2-AI agent-skill-audit-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/260-ninghan1980-skillpact-mit-skill-quality-audit-ai-agent-skills-contracts-separation-scores-canaries-tamper-evident-ledger-v2-ai-agent-skill-audit-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2-AI PR that adds a `SkillContract` SQLModel table (`contract_id, skill_name, input_schema, output_schema, version, recorded_at`).
2. First v2-AI PR that adds a `SkillCanary` SQLModel table (`canary_id, skill_name, input_payload, expected_output, recorded_at`).
3. First v2-AI PR that adds a `SkillSeparationScore` SQLModel table (`score_id, skill_name, separation_score, eval_set_hash, recorded_at`).
4. First v2-AI PR that adds a `SkillAuditLedgerEntry` SQLModel table (or extends the existing `audit_logs` table with a `skill_audit_id` column).
5. First v2-AI PR that adds a `/skills audit <skill_name>` / `/skills verify <skill_name>` / `/skills canary <skill_name>` Telegram command set on the cook-bot (operator-tooling only; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**).
6. First v2-AI PR that adds a Hermes Agent hook integration that enforces the canary-test + separation-score against the existing `skills/le31-*/SKILL.md` corpus.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When the Hermes agent orchestrates a daily-research pass, it wants to enforce the seven-check feature gate against incoming research picks, but struggles because the gate is enforced ad-hoc via LLM-judgment per pick, so that the gate becomes a **machine-checkable** canary-test + separation-score + tamper-evident-ledger primitive."* — PASS (links to features 149 + 232 + 236 + 237 + 258; justifies a new pain).
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the *gate-verdict* + *pick-slug* outputs. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 not triggered (no AI surface); confidence **high** for vocabulary transferability, **low** for immediate LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling only; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v2-AI** outcome (cross-section to features 149+232+236+237+258). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today (the ad-hoc LLM-judgment works); pain is forecast for the era when multiple agents (Codex + Claude Code + Hermes) co-orchestrate. Implementation cost = low-medium (~20-50 lines of YAML/JSON + canary-test-harness code; 1-2 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/skill_audit.py` (new) — `SkillContract` + `SkillCanary` + `SkillSeparationScore` + `SkillAuditLedgerEntry` SQLModel tables
- `le31/app/services/skill_audit.py` (new) — service layer for `audit_skill` + `verify_skill` + `evaluate_canary` + `compute_separation_score`
- `le31/app/hermes/hooks/skill_canary.py` (new) — Hermes Agent hook integration that enforces the canary-test + separation-score against `skills/le31-*/SKILL.md`
- `le31/app/api/v1/skill_audit.py` (new) — HTTP endpoints: `GET /api/skill-audit/<skill_name>` + `POST /api/skill-audit/<skill_name>/verify` + `POST /api/skill-audit/<skill_name>/canary`
- `le31/app/cook_bot/handlers/skill_audit.py` (new) — Telegram command handlers: `/skills audit <skill_name>` + `/skills verify <skill_name>` + `/skills canary <skill_name>` (operator-tooling only; NOT customer-facing)
- `le31/migrations/versions/<revision>_skill_audit.py` (new) — Alembic migration for the four new tables
- `skills/le31-conventions/SKILL.md` — append the *skill-quality-audit + contracts + separation-scores + canaries + tamper-evident-ledger* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the four new tables
- **Revert the skill-audit service** (remove the `le31/app/services/skill_audit.py` file + remove the import from `le31/app/services/__init__.py`)
- **Revert the Hermes Agent hook** (remove the `le31/app/hermes/hooks/skill_canary.py` file + remove the hook registration from `le31/app/hermes/hooks/__init__.py`)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/skill_audit.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the Telegram command handlers** (remove the `le31/app/cook_bot/handlers/skill_audit.py` file + remove the registration from `le31/app/cook_bot/handlers/__init__.py`)
- **No data loss** if the rollback happens BEFORE any skill-audit-row is written
- **Full data retention** if the rollback happens AFTER rows are written (the four tables are dropped but the skill-audit rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked] (workspace plan-limit error — 13th consecutive day; verified today via `save_issue` write-probe with requestId `a441ca79aa0965da`; parent fallback at `/opt/data/le31-daily-research-2026-10-02.linear-fallback.json`)