# Handoff — Feature 278 — v2-AI Telegram-bridge-for-AI-coding-agents-vocabulary (defer)

> **Pick:** `littlebearapps/untether` — v2-AI cross-section reference for **Telegram-bridge-for-AI-coding-agents + Claude-Code + Codex + OpenCode + Pi + Gemini-CLI + Amp + stream-progress + approve-actions + send-tasks-by-voice-from-phone + remote-control + remote-development** primitive.
> **Status:** `defer (parking-lot, vocabulary reference)` — zero build time today; the artifact is vocabulary-only and persists as a future-cast reference for any future LE31 v2-AI surface that adopts the *Telegram-bridge-for-AI-coding-agents + send-tasks-by-voice-from-phone + approve-actions + stream-progress + remote-control* primitives.
> **Source:** Daily Brainstorm 2026-10-05 (67th consecutive daily-brainstorm pass) → Pick A.
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/278-littlebearapps-untether-mit-telegram-bridge-ai-coding-agents-claude-code-codex-opencode-pi-gemini-cli-amp-stream-progress-approve-actions-voice-from-phone-v2-ai-telegram-bridge-ai-coding-agents-vocabulary.md`
> **Raw fetches:** `/tmp/le31-brainstorm-2026-10-05/verify_final_littlebearapps_untether.json` (parent-verified direct GitHub API GET, raw JSON, 6.6 KB)

---

## Seven-check gate verdict (LE31 charter §3.1 + §3.2 + §3.4)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✓ justified as a NEW pain | When the LE31 operator wants to supervise AI-coding-agent work from a phone (e.g., a kitchen-owner reviewing a cook's prep-AI-routine) without being at the desk, the operator wants Telegram-bridge-for-AI-coding-agents + Claude-Code + Codex + OpenCode + Pi + Gemini-CLI + Amp + stream-progress + approve-actions + send-tasks-by-voice-from-phone + remote-control + remote-development, but struggles because the existing cook-Telegram-bot is unidirectional (cook → owner) with no remote-supervisor-from-phone surface, so the v2-AI surface needs a *remote-supervisor-from-phone* discipline that adopts the *Telegram-bridge-for-AI-coding-agents + send-tasks-by-voice-from-phone + approve-actions + stream-progress + remote-control* primitives. **v2 expansion → NEW pain** |
| 2 | Viability | ✓ viable | Non-technical owner CAN understand (the *Telegram-bridge-for-AI-coding-agents + send-tasks-by-voice-from-phone + approve-actions* primitive is operator-readable); CAN recover (the *stream-progress + audit_logs* discipline is recoverable via Postgres backup); CAN maintain (the *Telegram-bridge-for-AI-coding-agents* surface is documentation-only at v1; v2-AI surface would require aiogram + FastAPI + SQLModel + Postgres expertise). **§3.1 owner-readable profile** |
| 3 | Strategic fit | ✓ aligned | Cross-section with feature 254 (OthmaneBlial/lightclaw MIT 21★/3⑂ v2-AI telegram-bot-agent-supervision-audit-trail-vocabulary) + 272 (bablobanov/hermes-agent-telegram-dashboard MIT v2 owner-pains telegram-pinned-status-dashboard-vocabulary) + 274 (Mfrostbutter/ageniusdesk-ce MIT fastapi-control-plane-dashboard-observability-mcp-self-hosted-workflow-automation v2 owner-pains operator-console-vocabulary). The *Telegram-bridge-for-AI-coding-agents + send-tasks-by-voice-from-phone + approve-actions + stream-progress + remote-control* posture IS the canonical **v2-AI remote-supervisor-from-phone-vocabulary** |
| 4 | Charter conflict | ✓ none hard | §3.1 STRICTLY-COMPATIBLE (Python + aiogram + minimal-HTML posture; the *remote-supervisor-from-phone* posture IS the §3.1 *single-restaurant + single-owner* invariant applied to the *v2-AI-supervisor-from-phone* dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive + 72★/11⑨ solid 4-star community traction base); §3.4 RIPGL_REVIEW REQUIRED (the *Telegram-bridge-for-AI-coding-agents* surface is operator-tooling per charter §3.4 invariant; the *approve-actions* primitive IS the *human-gate-as-auditable-test* charter §3.4 invariant; the *send-tasks-by-voice-from-phone* posture IS the *charter §3.1 hands-busy* invariant applied to the *v2-AI-supervisor-from-phone* dimension); §3.7 N/A (no privacy primitive change). **No hard conflict; §3.4 review required for any future implementation** |
| 5 | Outcome, appetite, scope | ✓ alignable | v2-AI outcome (remote-supervisor-from-phone-vocabulary). Max time worth spending = 0 minutes today (defer artifact); future v2-AI PR = 2-3 weeks for design + 4-6 weeks for *Telegram-bridge-for-AI-coding-agents + send-tasks-by-voice-from-phone + approve-actions + stream-progress + remote-control* surface + 1-2 weeks for verification = 2-3 months total |
| 6 | Cost to operational value | ✓ marginal | Pain frequency = low (LE31 v1 has no v2-AI surface today; no operator has asked for v2-AI remote-supervisor-from-phone); money vocabulary = minimal; implementation cost = 2-3 months v2-AI PR. **MARGINAL VALUE at v1; HIGH VALUE at v2-AI scope** |
| 7 | Circuit breaker and reversibility | ✓ reversible | Stop evidence = explicit owner/charter rejection of *Telegram-bridge-for-AI-coding-agents + send-tasks-by-voice-from-phone + approve-actions + stream-progress + remote-control* adoption; review point = first v2-AI PR that proposes *Telegram-bridge-for-AI-coding-agents + send-tasks-by-voice-from-phone + approve-actions + stream-progress + remote-control* surface; migration/rollback = trivial (vocabulary-only artifact, zero code shipped); retained data = N/A |

**Final decision: `defer (parking-lot, vocabulary reference)`.**

## Files to touch (future v2-AI PR trigger)

If a future v2-AI PR is triggered by the trigger condition below, the implementation would touch:

| File | Purpose | Notes |
|---|---|---|
| `app/models/remote_supervisor.py` (NEW) | `RemoteSupervisor` SQLModel table | `session_id, supervisor_phone, supervisor_via_telegram, supervisor_via_voice, supervisor_stream_progress_json, supervisor_approve_action_json, supervisor_started_at, supervisor_ended_at, supervisor_status` |
| `app/models/remote_supervisor_agent.py` (NEW) | `RemoteSupervisorAgent` SQLModel table | `agent_id, agent_kind, agent_payload_json, agent_version` for *Claude-Code + Codex + OpenCode + Pi + Gemini-CLI + Amp* discipline |
| `app/models/remote_supervisor_voice.py` (NEW) | `RemoteSupervisorVoice` SQLModel table | `voice_id, voice_payload_json, voice_version` for *send-tasks-by-voice-from-phone* discipline |
| `app/api/remote_supervisor.py` (NEW) | FastAPI route + endpoint | `/api/remote-supervisor` (POST start, GET status, POST approve, GET stream-progress) |
| `app/templates/remote_supervisor.html` (NEW) | minimal-HTML/HTMX template | owner-facing surface for remote-supervisor-from-phone |
| `app/bots/cook_supervisor.py` (NEW) | aiogram bot supervisor-from-phone bridge | *Telegram-bridge-for-AI-coding-agents + Claude-Code + Codex + OpenCode + Pi + Gemini-CLI + Amp + stream-progress + approve-actions* discipline |
| `app/bots/cook_supervisor_voice.py` (NEW) | aiogram voice processing | *send-tasks-by-voice-from-phone* discipline |
| `migrations/versions/<hash>_add_remote_supervisor_tables.py` (NEW) | alembic migration | creates `remote_supervisor + supervisor_agent + supervisor_voice` tables |
| `tests/test_remote_supervisor_api.py` (NEW) | pytest coverage | covers RemoteSupervisor CRUD + approve-actions + stream-progress + send-tasks-by-voice-from-phone |
| `tests/test_remote_supervisor_bot.py` (NEW) | pytest coverage | covers aiogram bot supervisor-from-phone bridge |
| `app/static/js/remote-supervisor-stream-progress.js` (NEW) | minimal vanilla JS for HTMX stream-progress | Optional: only if HTMX SSE proves insufficient |

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md` + `development` skill, the future v2-AI PR would:
1. Run `pytest tests/test_remote_supervisor_api.py tests/test_remote_supervisor_bot.py -v` to confirm all tests pass.
2. Run `alembic upgrade head` to confirm migrations apply cleanly.
3. Run `python -c "from app.models.remote_supervisor import RemoteSupervisor; print(RemoteSupervisor.__tablename__)"` to confirm SQLModel loads.
4. Manually verify via `curl http://localhost:8000/api/remote-supervisor/status` that the FastAPI endpoint returns 200 with the expected schema.
5. Manually verify via the cook-supervisor aiogram bot that the *Telegram-bridge-for-AI-coding-agents + Claude-Code + Codex + OpenCode + Pi + Gemini-CLI + Amp + stream-progress + approve-actions + send-tasks-by-voice-from-phone + remote-control* discipline works end-to-end (start session → stream-progress → approve-action → end session).
6. Run `mypy app/` + `ruff check app/` to confirm static analysis passes.
7. Confirm feature is in `Backlog` status + parent (this brainstorm parent) is in `Done` status in Linear.

## Rollback path

The defer artifact is vocabulary-only, zero code shipped, so no rollback is needed today. If a future v2-AI PR ships and the *Telegram-bridge-for-AI-coding-agents + send-tasks-by-voice-from-phone + approve-actions + stream-progress + remote-control* discipline is rejected by the owner/charter:
1. Run `alembic downgrade -1` to drop the `remote_supervisor + supervisor_agent + supervisor_voice` tables.
2. Delete `app/models/remote_supervisor.py` + `app/models/remote_supervisor_agent.py` + `app/models/remote_supervisor_voice.py` + `app/api/remote_supervisor.py` + `app/templates/remote_supervisor.html` + `app/bots/cook_supervisor.py` + `app/bots/cook_supervisor_voice.py` + the alembic migration + the pytest files.
3. Re-run `alembic upgrade head` to confirm clean state.
4. Re-run `pytest -v` to confirm no regressions.

## Mandatory LE31 skill list

The future v2-AI PR author MUST load + apply these skills before any code is written:

| Skill | Why |
|---|---|
| `le31-conventions` | Repository-wide Python + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX conventions |
| `le31-v1-feature-pattern` | Existing v1 feature pattern (table management, cook-channel, stock-ledger) |
| `le31-handoff-spec` | Slice handoff format |
| `le31-coding-agent-brief` | Paste-in prompt generation from this slice contract |
| `systematic-debugging` | 4-phase root cause debugging if any test fails |
| `verify-before-fixing` | Verify diagnostic / CI / delegated subagent before fixing |
| `pre-merge-review` | Independent non-author review before merging |

## Bucket

**v2-AI** (no `le31 v2 owner-pains` or `le31 v2-AI` project exists per `le31-feature-pipeline/SKILL.md` line 33; this pick attaches to `le31 Research` P-HMM-1 as the parent of the sub-issue per the verified workspace project list of 2026-10-05).

## Trigger condition

First v2-AI PR that adds a `remote_supervisor` SQLModel table + a `/api/remote-supervisor` FastAPI endpoint + a `remote-supervisor.html` minimal-HTML/HTMX template; OR first v2-AI PR that adopts the *Telegram-bridge-for-AI-coding-agents + Claude-Code + Codex + OpenCode + Pi + Gemini-CLI + Amp + stream-progress + approve-actions + send-tasks-by-voice-from-phone + remote-control* discipline on the existing cook-Telegram-bot surface.

## Charter compatibility

§3.1 + §3.2 STRICTLY-COMPATIBLE; §3.4 RIPGL_REVIEW REQUIRED if any customer-facing surface is added (the *Telegram-bridge-for-AI-coding-agents* surface is operator-tooling per charter §3.4 invariant; the *approve-actions* primitive IS the *human-gate-as-auditable-test* charter §3.4 invariant).

## Companion artifacts

- Feature file: `/opt/data/le31_mmm3_research_work/features/278-littlebearapps-untether-mit-telegram-bridge-ai-coding-agents-claude-code-codex-opencode-pi-gemini-cli-amp-stream-progress-approve-actions-voice-from-phone-v2-ai-telegram-bridge-ai-coding-agents-vocabulary.md`
- Spec file: `/opt/data/le31_mmm3_research_work/specs/278-littlebearapps-untether-mit-telegram-bridge-ai-coding-agents-claude-code-codex-opencode-pi-gemini-cli-amp-stream-progress-approve-actions-voice-from-phone-v2-ai-telegram-bridge-ai-coding-agents-vocabulary-HANDOFF.md`
- Linear sub-issue: BLOCKED (workspace plan-limit error: *\"You've exceeded the free issue limit for this workspace\"* — **16th consecutive day**; verified today via 2 write-probes with requestId `a45aac5e0a9ad368`; parent fallback at `/opt/data/le31-brainstorm-2026-10-05.linear-fallback.json`)
- Report: `/opt/data/le31-brainstorm-2026-10-05.md`
- Raw fetches: `/tmp/le31-brainstorm-2026-10-05/verify_final_littlebearapps_untether.json` (parent-verified direct GitHub API GET, raw JSON, 6.6 KB)