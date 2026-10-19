# HANDOFF — Feature 346: `caglarutkuguler-cubicle-mit-live-pixel-art-office-ai-agents-paperclip-claude-code-codex-gemini-cli-kpi-board-telegram-alerts-zero-dependency-read-only-multi-ai-agent-v2-ai-operator-facing-control-of-AI-agents-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/346-caglarutkuguler-cubicle-mit-live-pixel-art-office-ai-agents-paperclip-claude-code-codex-gemini-cli-kpi-board-telegram-alerts-zero-dependency-read-only-multi-ai-agent-v2-ai-operator-facing-control-of-AI-agents-vocabulary.md` — defer/parking-lot (Pick C of Daily Brainstorm 2026-10-19).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *KPI-board-+-Telegram-alerts-+-zero-dependency-+-read-only-+-multi-AI-agent-+-chokepoint-governed-+-human-gate-via-Telegram primitive*, the owner wants *evidence that this operator-facing-control-of-AI-agents-vocabulary exists in 2026 with the same KPI-board-+-Telegram-alerts-+-zero-dependency-+-read-only-+-multi-AI-agent-+-chokepoint-governed-+-human-gate-via-Telegram posture AND the 40★/⑂1 = HIGHEST-STAR IN-WINDOW MIT PICK of the 81-pass series*, but struggles because *LE31 has no documented v2-AI operator-facing-control-of-AI-agents-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram) without specialist help. The **40★/⑂1 = HIGHEST-STAR IN-WINDOW MIT PICK of the 81-pass series** with maintainer activity (created 2026-09-18 = ~31-day-old pushed-TODAY repo, pushed 2026-10-18T12:08:31Z = TODAY = STRONGEST IN-WINDOW-PUSH SIGNAL OF THE DAY, 6661 KB modest) makes vocabulary viable, but code adoption is not viable (LE31 v2-AI has no operator-facing-control-of-AI-agents surface today; v2-AI is on agent-governance + audit-ledger + chokepoint + persona-charter). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: JavaScript ✗ OFF-STACK (LE31 v2-AI is Python + FastAPI + Postgres, not JavaScript + Node.js) + Node.js OFF-STACK (LE31 v2-AI is Python + FastAPI, not Node.js) + Paperclip OFF-STACK (LE31 v2-AI has no Paperclip surface today) + Claude-Code + Codex + Gemini-CLI + Cursor OFF-STACK (LE31 v2-AI has no AI-agent-vendor-pivot surface today; charter §3.4 review needed) + Telegram-bot ✓ ON-PATTERN (LE31 v1 has aiogram-driven-cook-bot + Telegram-bot is a portable surface) + KPI-board ✓ ON-PATTERN (the §3.4 *observable-evidence* posture is portable; LE31 v1 has no KPI-board surface today) + dashboard ✓ ON-PATTERN (the §3.4 + §3.7 operator-facing-control surface is portable) + visualization ✓ ON-PATTERN (the §3.4 *observable-evidence* posture is portable) + zero-dependency ✓ ON-PATTERN (the §3.4 *non-AI-fallback-first* posture is portable) + read-only ✓ ON-PATTERN (the §3.4 *minimal-state-modification-surface* posture is portable) + multi-AI-agent via chokepoint ✓ ON-PATTERN (the §3.4 *chokepoint-governed* posture is portable) + agent-dashboard + agent-monitoring + agent-orchestration + ai-agents + ai-office + kpi-dashboard + llm-agents OFF-STACK (LE31 v2-AI has no operator-facing-control-of-AI-agents surface today; charter §3.4 review needed). Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX + aiogram v3 + Telegram-bot. Rabbit hole: the *JavaScript + Node.js + Paperclip + Claude-Code + Codex + Gemini-CLI + Cursor* stack is off-LE31-stack (LE31 v2-AI is Python + FastAPI + Postgres + append-only-ledger, not JavaScript + Node.js + Paperclip + Claude-Code/Codex/Gemini-CLI). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram* primitives are §3.4 + §3.7-aligned (chokepoint-governed + observable-evidence + non-AI-fallback-first + human-gate-via-Telegram + minimal-PII-only-aggregator-bridge). The *zero-dependency + read-only* posture IS the §3.4 *non-AI-fallback-first + minimal-state-modification-surface* invariant. No §3.4 customer-facing AI outside the AI-agent observability surface. No data rule violation (charter §3.7 PII review needed: the *Telegram-alerts* surface minimizes PII; the *operator-chat-id* field is the only PII; charter-decision needed). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI defer outcome (operator-facing-control-of-AI-agents + KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram surface for the LE31 v2-AI). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v2-AI surfaces (planned agent-governance + AI-assisted) may adopt the *KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram* discipline; the reference is *naming*, not new build. The **40★/⑂1 = HIGHEST-STAR IN-WINDOW MIT PICK of the 81-pass series** makes this the strongest possible vocabulary reference (the highest-star + IN-WINDOW + MIT + every-possible-cluster-match signal of the 81-pass series). |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable today (JavaScript + Node.js + Paperclip + Claude-Code/Codex/Gemini-CLI stack off-LE31-v2-AI-stack + no operator-facing-control-of-AI-agents surface in v2-AI charter). The vocabulary IS portable AND the **40★/⑂1 = HIGHEST-STAR IN-WINDOW MIT PICK of the 81-pass series** makes this the strongest possible vocabulary reference.

## Bucket

**v2-AI** (operator-facing-control-of-AI-agents-+-KPI-board-+-Telegram-alerts-+-zero-dependency-+-read-only-+-multi-AI-agent-+-chokepoint-governed-+-human-gate-via-Telegram-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 13-tuple-primitive set (live-pixel-art-office-for-AI-agents + KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + Claude Code + Codex + Gemini CLI + Paperclip + Cursor + chokepoint-governed + human-gate-via-Telegram) + the tech-stack (JavaScript ✗ OFF-STACK + Node.js + Paperclip + Claude Code + Codex + Gemini CLI + Cursor + Telegram-bot + KPI-board + dashboard + visualization + zero-dependency + agent-dashboard + agent-monitoring + agent-orchestration + ai-agents + ai-office + kpi-dashboard + llm-agents + multi-agent + pixel-art + pixel-office).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *operator-facing-control-of-AI-agents + KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `AI_Agent_State`, `AI_Agent_Needs_Operator_State`, `AI_Agent_Failed_State`, `KPI_Board`, `Telegram_Alert` tables.
- `backend/services/ai_agent_observability.py` — new file with `AI_Agent_Observability` class (charter §3.4 *non-AI-fallback-first + minimal-state-modification-surface* posture).
- `backend/services/kpi_board.py` — new file with `KPI_Board` class (charter §3.4 *observable-evidence* posture).
- `backend/services/telegram_alert_dispatcher.py` — new file with `TelegramAlertDispatcher` class (charter §3.4 + §3.7 *human-gate-via-Telegram + minimal-PII-only-aggregator-bridge* posture).
- `backend/services/multi_ai_agent_chokepoint.py` — new file with `MultiAiAgentChokepoint` class (charter §3.4 *chokepoint-governed* posture; gates every AI-agent action via Claude Code + Codex + Gemini CLI + Cursor + Paperclip).
- `backend/services/agent_state_observer.py` — new file with `AgentStateObserver` class (charter §3.4 *non-AI-fallback-first + minimal-state-modification-surface* posture; observes AI-agent-state via chokepoint; does NOT modify).
- `frontend/templates/kpi-board.html` — new minimal-HTML/HTMX template for the operator-facing-KPI-board.
- `frontend/templates/agent-list.html` — new minimal-HTML/HTMX template for the operator-facing-multi-AI-agent-list.
- `frontend/static/kpi-board-app.js` — new minimal-JS for the KPI-board rendering (charter §3.4 *observable-evidence* posture; minimal-HTML/HTMX-style).
- `backend/main.py` — wire the new sub-apps into the parent uvicorn app.
- `tests/test_ai_agent_observability.py` — new unit test for `AI_Agent_Observability`.
- `tests/test_kpi_board.py` — new unit test for `KPI_Board`.
- `tests/test_telegram_alert_dispatcher.py` — new unit test for `TelegramAlertDispatcher`.
- `tests/test_multi_ai_agent_chokepoint.py` — new unit test for `MultiAiAgentChokepoint`.
- `tests/integration/test_agent_state_observer.py` — new integration test for `AgentStateObserver` (verify read-only + zero-dependency posture).

## Verification protocol reference

When the first v2-AI PR that adopts the *operator-facing-control-of-AI-agents + KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram* discipline lands, the verification protocol is:

1. Run `pytest tests/test_ai_agent_observability.py` and verify the `AI_Agent_Observability` produces a valid observability-surface for the multi-AI-agent chokepoint.
2. Run `pytest tests/test_kpi_board.py` and verify the `KPI_Board` surfaces *who-works + who-needs-you + who-failed* correctly.
3. Run `pytest tests/test_telegram_alert_dispatcher.py` and verify the `TelegramAlertDispatcher` fires on AI-agent-state-change correctly.
4. Run `pytest tests/test_multi_ai_agent_chokepoint.py` and verify the `MultiAiAgentChokepoint` gates every AI-agent action via Claude Code + Codex + Gemini CLI + Cursor + Paperclip correctly.
5. Run `pytest tests/integration/test_agent_state_observer.py` and verify the `AgentStateObserver` observes AI-agent-state via chokepoint + does NOT modify.
6. Run `uvicorn backend.main:app` and curl the KPI-board endpoint to verify the operator-facing-KPI-board is callable.
7. Open `frontend/templates/kpi-board.html` in a browser and verify the operator-facing-KPI-board renders the *who-works + who-needs-you + who-failed* correctly.
8. Verify the operator's Telegram chat receives an alert on AI-agent-state-change.
9. Inspect the `AI_Agent_State` + `AI_Agent_Needs_Operator_State` + `AI_Agent_Failed_State` + `KPI_Board` + `Telegram_Alert` tables in Postgres and verify every AI-agent-state-transition is recorded (the §3.3 append-only-ledger invariant).
10. Verify the observability surface has zero third-party deps (charter §3.4 *non-AI-fallback-first* posture).

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *operator-facing-control-of-AI-agents + KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the five tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.
5. Stop the multi-AI-agent chokepoint service.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:

- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-v1-feature-pattern/SKILL.md` — for the v1 feature contract shape and slicing rules.
- `skills/le31-research/SKILL.md` — for the research workflow and report shape.
- `skills/le31-feature-pipeline/SKILL.md` — for the feature pipeline (lease to coding agent).
- `skills/le31-handoff-spec/SKILL.md` — for the handoff spec (this file).
- `skills/le31-coding-agent-brief/SKILL.md` — for the paste-in brief.
- `skills/le31-backend/SKILL.md` — for the backend conventions (if applicable).
- `skills/le31-frontend/SKILL.md` — for the frontend conventions (if applicable).
- `skills/le31-data/SKILL.md` — for the data conventions (if applicable).
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

This defer artifact is documentation only. It becomes a build trigger when the **first v2-AI PR that adds an operator-facing-control-of-AI-agents + KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram surface to the LE31 v2-AI** lands. At that point:

1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which multi-AI-agent chokepoint discipline (Claude Code + Codex + Gemini CLI + Cursor + Paperclip vs single-AI-agent + chokepoint vs multi-AI-agent + per-agent-chokepoint) becomes the canonical.
3. Decide which KPI-board discipline (who-works + who-needs-you + who-failed vs who-works + who-is-blocked + who-failed vs who-works + who-needs-operator-input + who-is-pending) becomes the canonical.
4. Decide which Telegram-alerts discipline (on-state-change vs on-failed-only vs on-needs-operator-only) becomes the canonical.
5. Apply charter §3.4 review to the *KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram* posture before any v2-AI PR.
6. Apply charter §3.7 review to the *Telegram-alerts + minimal-PII-only-aggregator-bridge* posture (the *operator-chat-id* field is the only PII).
7. Adopt the *operator-facing-control-of-AI-agents + KPI-board + Telegram-alerts + zero-dependency + read-only + multi-AI-agent + chokepoint-governed + human-gate-via-Telegram* discipline on the chosen surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v2-AI code is shipped.
