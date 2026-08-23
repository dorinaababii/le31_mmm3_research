# Slice Handoff — `nightmux-stdlib-telegram-bridge`

> **Pick**: 102-nightmux-stdlib-telegram-bridge (defer, watch-list)
> **Source brainstorm**: 2026-08-23 (Pick A)
> **Generated**: 2026-08-23 by daily-brainstorm cron

## Active feature path

- `features/102-nightmux-stdlib-telegram-bridge.md`
- This `specs/nightmux-stdlib-telegram-bridge-HANDOFF.md`

## Seven-check gate verdict

**Decision: defer, watch-list.** The cross-section informs LE31 v2 cook-assistant (feature 68) architectural decomposition without changing the v1 roadmap. No code today.

**Gate summary**:
1. **JTBD**: When LE31 v2 revisits the cook-assistant architecture, knowing that pure-stdlib Telegram transports are technically viable informs the transport-layer attack-surface-minimalization decision. Defer (not currently blocking).
2. **Viability**: n/a (no new feature to operate).
3. **Practicability + confidence**: medium (peer repo 22★ + MIT + Python stdlib only; architecture straightforward). Low confidence in LE31-specific urgency (LE31 already has the transport).
4. **Conflict**: none. Pattern strengthens existing feature 58/61/63/68 line.
5. **Outcome, appetite, scope**: v2-AI watch-list. S effort. ≤1 day. Defer.
6. **Cost to operational value**: zero implementation cost; pure pattern-record artifact.
7. **Circuit breaker + reversibility**: fully reversible. Watch-list artifact; can be deleted without consequence.

## Files to touch

**ZERO files in LE31 source tree.** This is a research-only artifact.

If the slice is ever un-deferred (i.e., when the peer crosses ≥50★ OR 2+ independent repos converge on the stdlib-only constraint), the slice will touch:
- `backend/app/bot/transport.py` (new file) — thin aiogram transport wrapper.
- `backend/app/bot/orchestrator.py` (new file) — deterministic-gate orchestrator.
- `backend/app/bot/decision.py` (new file) — per-domain decision module.

These files do **not exist today** and **will not be created by this slice**.

## Verification protocol reference

- **Today**: verify that this `HANDOFF.md` exists + `features/102-nightmux-stdlib-telegram-bridge.md` exists + the `INDEX.md` row was added + the `le31_daily_brainstorm_2026_08_23` Linear issue (HMM-133) was created with the parent body.
- **Daily (next 7 days)**: track `mmr710/nightmux` star velocity via `GET https://api.github.com/repos/mmr710/nightmux` (via `$HERMES_GITHUB_TOKEN`).
- **Re-check threshold**: if stars ≥50 OR ≥2 independent repos in the same `topic:telegram-bot` cluster ship with the same stdlib-only constraint, the slice is un-deferred.

## Rollback path

**Fully reversible.** Delete `features/102-nightmux-stdlib-telegram-bridge.md` + this `HANDOFF.md` + the `INDEX.md` row + the `le31_daily_brainstorm_2026_08_23` sub-issue + the `le31_v1_core_mvp` Linear sub-issue. Zero risk of code regression (no code changed).

## Mandatory LE31 skill list

Before resuming this slice, load:
- `le31-conventions` — verify no charter violation.
- `le31-feature-pipeline` — verify the contract is up-to-date.
- `le31-coding-agent-brief` — generate the paste-in prompt only if the slice is un-deferred.

If any skill is updated during the lifetime of this slice, patch it via `skill_manage(action='patch')` and re-verify before proceeding.
