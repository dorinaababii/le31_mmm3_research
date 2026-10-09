# Pick B — `koorbmeh/minerva` — v2-AI personal-AI-agent-runtime governed-tool-gateway-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research/features/267-koorbmeh-minerva-mit-personal-ai-agent-runtime-governed-tool-gateway-hash-chained-audit-ledger-job-orchestration-test-suite-1-day-old-fresh-v2-ai-personal-agent-runtime-governed-tool-gateway-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2-AI PR that adds a `PersonalAgentRuntime` SQLModel table (`runtime_id, runtime_name, runtime_version, runtime_status, recorded_at`).
2. First v2-AI PR that adds a `GovernedToolGateway` SQLModel table (`gateway_id, gateway_name, gateway_policy_id, recorded_at`).
3. First v2-AI PR that adds a `HashChainedAuditLedger` SQLModel table (`entry_id, entry_payload, entry_payload_hash, entry_previous_hash, entry_hash, recorded_at`).
4. First v2-AI PR that adds a `JobOrchestration` SQLModel table (`job_id, job_runtime_id, job_name, job_status, job_started_at, job_completed_at, job_retry_count, recorded_at`).
5. First v2-AI PR that adds a `TestSuite` SQLModel table (`suite_id, suite_runtime_id, suite_name, suite_result, suite_started_at, suite_completed_at, recorded_at`).
6. First v2-AI PR that extends the existing `audit_logs` table with a `hash_chain` column.
7. First v2-AI PR that adds a `/runtime list` / `/runtime show <runtime_id>` / `/runtime test <runtime_id>` / `/runtime audit <runtime_id>` Telegram command set on the cook-bot (operator-tooling only; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**).
8. First v2-AI PR that adds a Hermes Agent self-test-harness-as-first-class-citizen extension that exposes the personal-AI-agent-runtime + governed-tool-gateway + hash-chained-audit-ledger + job-orchestration to the owner-only channel.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When the Hermes agent orchestrates a daily-research pass + daily-brainstorm pass + LE31-feature-pipeline, it wants a *personal-AI-agent-runtime* with a *governed-tool-gateway* + *hash-chained-audit-ledger* + *job-orchestration* + *test-suite-as-first-class-citizen*, but struggles because the current Hermes runtime has no first-class test-suite-as-first-class-citizen discipline, so that the *self-test-harness-as-runtime-concern* primitive becomes a future-v2-AI surface-extension recipe."* — PASS (links to features 03 + 121 + 198 + 232 + 236 + 237 + 245 + 257 + 258 + 264; justifies a new pain).
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the *runtime-audit-lineage* + *test-suite-output* surfaces. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 not triggered (operator-tooling; no customer-facing AI); confidence **high** for vocabulary transferability, **low** for immediate LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling only; §3.1 explicit-state-transitions preserved; §3.2 MIT permissive. PASS.
5. **Outcome, appetite, and scope** — **v2-AI** outcome (cross-section to features 03+121+198+232+236+237+245+257+258+264). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today (LE31 has no v2-AI surface yet); pain is forecast for v2-AI adoption era. Implementation cost = low-medium (~50-100 lines of Hermes-runtime + governed-tool-gateway + hash-chained-audit-ledger code; 2-3 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/personal_agent_runtime.py` (new) — `PersonalAgentRuntime` + `GovernedToolGateway` + `HashChainedAuditLedger` + `JobOrchestration` + `TestSuite` SQLModel tables
- `le31/app/services/personal_agent_runtime.py` (new) — service layer for `start_personal_agent_runtime` + `register_governed_tool_gateway` + `record_hash_chained_audit_ledger_entry` + `orchestrate_job` + `run_test_suite`
- `le31/app/hermes/runtime/` (new package) — Hermes Agent self-test-harness-as-first-class-citizen extension that exposes the personal-AI-agent-runtime + governed-tool-gateway + hash-chained-audit-ledger + job-orchestration to the owner-only channel
- `le31/app/api/v1/personal_agent_runtime.py` (new) — HTTP endpoints: `GET /api/runtime/list` + `GET /api/runtime/show/<runtime_id>` + `POST /api/runtime/test/<runtime_id>` + `GET /api/runtime/audit/<runtime_id>`
- `le31/app/cook_bot/handlers/personal_agent_runtime.py` (new) — Telegram command handlers: `/runtime list` + `/runtime show <runtime_id>` + `/runtime test <runtime_id>` + `/runtime audit <runtime_id>` (operator-tooling only; NOT customer-facing)
- `le31/migrations/versions/<revision>_personal_agent_runtime.py` (new) — Alembic migration for the five new tables + the new `audit_logs` `hash_chain` column
- `skills/le31-conventions/SKILL.md` — append the *personal-AI-agent-runtime + governed-tool-gateway + hash-chained-audit-ledger + job-orchestration + test-suite-as-first-class-citizen* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the five new tables + revert the new `audit_logs` `hash_chain` column
- **Revert the personal-agent-runtime service** (remove the `le31/app/services/personal_agent_runtime.py` file + remove the import from `le31/app/services/__init__.py`)
- **Revert the Hermes Agent runtime package** (remove the `le31/app/hermes/runtime/` package + remove the import from `le31/app/hermes/__init__.py`)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/personal_agent_runtime.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the Telegram command handlers** (remove the `le31/app/cook_bot/handlers/personal_agent_runtime.py` file + remove the registration from `le31/app/cook_bot/handlers/__init__.py`)
- **No data loss** if the rollback happens BEFORE any `HashChainedAuditLedger` entry is written
- **Full data retention** if the rollback happens AFTER entries are written (the five tables are dropped but the entries are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked] (workspace plan-limit error — 14th consecutive day; verified today via `save_issue` write-probe with requestId `a449f6e6bc89bb71`; parent fallback at `/opt/data/le31-daily-research-2026-10-03.linear-fallback.json`)
