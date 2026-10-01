# Pick A — `yaoyuxiang-gnn/agent-ledger` — v2-AI append-only-decision-ledger — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/257-yaoyuxiang-gnn-agent-ledger-apache-2-0-append-only-signed-ledger-ai-agent-delegations-zero-dependencies-v2-ai-append-only-decision-ledger.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2-AI PR that adds an `AIAgentDelegation` SQLModel table, an `AIAgentAction` SQLModel table, an `AIAuditTrail` SQLModel table, or an `AITransparencyLog` SQLModel table.
2. First v2-AI PR that adds a `/ai-audit list` / `/ai-audit show <delegation_id>` / `/ai-audit verify <delegation_id>` Telegram command set on the cook-bot (operator-tooling only; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**).
3. First v2-AI PR that extends the existing `audit_logs` write-path with stdlib-only `cryptography` + `hashlib` signatures (the *zero-dependencies* primitive).
4. First v2-AI PR that exposes a *public-read-only* transparency-log endpoint (requires charter §3.4 amendment).

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When the owner/staff runs an AI-assisted workflow (e.g., menu-pricing suggestions, prep-scheduling), they want to know who authorised that AI agent — and who answers for the result, but struggle because there is no append-only signed ledger recording the chain of AI-agent delegations, so that every AI decision carries cryptographically-signed attribution back to a human owner + the agent's parent process."* — PASS (links to feature 187 as adjacent v2-AI append-only-ledger vocabulary; justifies a new pain)
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the audit-logged outputs. PASS.
3. **Practicability and confidence** — Apache-2.0 permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 NOT triggered (operator-tooling AI, not customer-facing AI); confidence **medium** for mechanism, **low** for present urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling-AI; §3.4 NOT triggered; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v2-AI** outcome (cross-section to features 121+187+243). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today; pain is forecast for v2-AI era. Implementation cost = low (~50-100 lines; 1-2 days when triggered). Cost-value ratio favorable when triggered. PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/ai_audit.py` (new) — `AIAgentDelegation` + `AIAgentAction` + `AIAuditTrail` + `AITransparencyLog` SQLModel tables
- `le31/app/services/ai_audit.py` (new) — service layer for `record_delegation` + `record_action` + `verify_signature` + `verify_audit_trail` + `list_transparency_log`
- `le31/app/api/v1/ai_audit.py` (new) — HTTP endpoints: `GET /api/ai-audit/delegations` + `GET /api/ai-audit/delegations/<id>` + `GET /api/ai-audit/verify/<signature_hash>` + `GET /api/ai-audit/transparency-log`
- `le31/app/cook_bot/handlers/ai_audit.py` (new) — Telegram command handlers: `/ai-audit list` + `/ai-audit show <delegation_id>` + `/ai-audit verify <delegation_id>` (operator-tooling only; NOT customer-facing)
- `le31/migrations/versions/<revision>_ai_audit.py` (new) — Alembic migration for the four new tables
- `tests/pyodicity.yaml` — test cases for AI-authored mutations
- `skills/le31-conventions/SKILL.md` — append the *SDK over agents = append-only + signed + zero-dependencies* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the four new tables
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/ai_audit.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the Telegram command handlers** (remove the `le31/app/cook_bot/handlers/ai_audit.py` file + remove the registration from `le31/app/cook_bot/handlers/__init__.py`)
- **No data loss** if the rollback happens BEFORE any AI-agent-delegation rows are written
- **Full data retention** if the rollback happens AFTER rows are written (the four tables are dropped but the AI-agent-delegation rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked] (workspace plan-limit error — 12th consecutive day; verified today via `save_issue` write-probe with requestId `a4396da65c72d371`; parent fallback at `/opt/data/le31-daily-research-2026-10-01.linear-fallback.json`)