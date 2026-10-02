# Pick C — `TAKUYA0608-dev/cmn-c2-701` — v2-AI enterprise-agent-audit-ledger-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/262-TAKUYA0608-dev-cmn-c2-701-mit-enterprise-ai-agent-audit-ledger-governance-qa-agent-v2-ai-enterprise-agent-audit-ledger-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2-AI PR that adds an `AIAgentDecision` SQLModel table (`decision_id, ai_agent_id, decision_payload, decision_reasoning, decision_policy_id, recorded_at`).
2. First v2-AI PR that adds an `AIQueryLog` SQLModel table (`query_id, query_text, query_asker_id, query_response_text, query_response_decision_id, recorded_at`).
3. First v2-AI PR that adds a `GovernancePolicy` SQLModel table (`policy_id, policy_name, policy_body, policy_version, recorded_at`).
4. First v2-AI PR that extends the existing `audit_logs` table with `decision_id` + `decision_reasoning` + `decision_policy_id` columns.
5. First v2-AI PR that adds a `/audit qa <question>` / `/audit policy <policy_id>` / `/audit decision <decision_id>` Telegram command set on the cook-bot (operator-tooling only; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**).
6. First v2-AI PR that adds a Hermes Agent natural-language-query extension that exposes the audit-ledger to the owner-only channel via natural-language questions.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When the owner reviews an AI-suggested menu-price or prep-schedule change, they want a `*why did the AI do that?*` answer grounded in an append-only-audit-ledger queryable by natural language, but struggles because the current `audit_logs` table is human-readable only, so that the *audit-log-query-by-natural-language* + *governance-policy-lookup* surface is the *Q&A-agent* primitive."* — PASS (links to features 149 + 232 + 236 + 237 + 199 + 257 + 258; justifies a new pain).
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the *Q&A-output* + *audit-ledger-lineage* outputs. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 not triggered (operator-tooling; no customer-facing AI); confidence **high** for vocabulary transferability, **low** for immediate LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling only; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v2-AI** outcome (cross-section to features 149+199+232+236+237+257+258). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today (LE31 has no v2-AI surface yet); pain is forecast for v2-AI adoption era. Implementation cost = low-medium (~50-100 lines of SQLModel + Q&A-agent surface code; 2-3 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/ai_agent_audit.py` (new) — `AIAgentDecision` + `AIQueryLog` + `GovernancePolicy` SQLModel tables
- `le31/app/services/ai_agent_audit.py` (new) — service layer for `record_ai_agent_decision` + `query_audit_ledger` + `lookup_governance_policy`
- `le31/app/hermes/hooks/audit_qa.py` (new) — Hermes Agent hook integration that exposes the audit-ledger to the owner-only channel via natural-language questions
- `le31/app/api/v1/ai_agent_audit.py` (new) — HTTP endpoints: `GET /api/ai-agent-audit/decisions/<decision_id>` + `POST /api/ai-agent-audit/qa` + `GET /api/ai-agent-audit/policies/<policy_id>`
- `le31/app/cook_bot/handlers/ai_agent_audit.py` (new) — Telegram command handlers: `/audit qa <question>` + `/audit policy <policy_id>` + `/audit decision <decision_id>` (operator-tooling only; NOT customer-facing)
- `le31/migrations/versions/<revision>_ai_agent_audit.py` (new) — Alembic migration for the three new tables + the three new `audit_logs` columns
- `skills/le31-conventions/SKILL.md` — append the *enterprise-AI-agent-audit-ledger + governance-Q&A-agent* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the three new tables + revert the three new `audit_logs` columns
- **Revert the AI-agent-audit service** (remove the `le31/app/services/ai_agent_audit.py` file + remove the import from `le31/app/services/__init__.py`)
- **Revert the Hermes Agent hook** (remove the `le31/app/hermes/hooks/audit_qa.py` file + remove the hook registration from `le31/app/hermes/hooks/__init__.py`)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/ai_agent_audit.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the Telegram command handlers** (remove the `le31/app/cook_bot/handlers/ai_agent_audit.py` file + remove the registration from `le31/app/cook_bot/handlers/__init__.py`)
- **No data loss** if the rollback happens BEFORE any AI-agent-decision-row is written
- **Full data retention** if the rollback happens AFTER rows are written (the three tables are dropped but the AI-agent-decision rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked] (workspace plan-limit error — 13th consecutive day; verified today via `save_issue` write-probe with requestId `a441ca79aa0965da`; parent fallback at `/opt/data/le31-daily-research-2026-10-02.linear-fallback.json`)