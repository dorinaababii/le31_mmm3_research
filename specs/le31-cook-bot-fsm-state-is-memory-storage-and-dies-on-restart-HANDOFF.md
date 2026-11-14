# Slice contract — `le31-cook-bot-fsm-state-is-memory-storage-and-dies-on-restart`

## Active feature path

`features/478-le31-cook-bot-fsm-state-is-memory-storage-and-dies-on-restart-first-party-the-dispatcher-uses-memorystorage-so-state-is-lost-across-workers-and-restarts-v1-cook-fsm-persistent-storage.md`

## Seven-check gate verdict

**BUILD.** Evidence class: **observed**, execution-proven against aiogram 3.31.0 and LE31's own dispatcher; confidence high for the storage behavior and medium for operational frequency.

1. **JTBD:** When the cook starts the morning menu flow, they want the bot to remember it until the photo arrives, but process-local state is lost across the documented second worker or a restart.
2. **Viability:** pass; storage is invisible to the cook and recoverable by restarting `/start_today`.
3. **Practicability:** pass; the main decision is filesystem versus Redis and must remain explicit.
4. **Conflict:** none; strengthens explicit-state semantics and does not implement feature 403's allowlist.
5. **Outcome/scope:** v1 cook-bot reliability; scope limited to storage for the existing FSM.
6. **Cost/value:** moderate cost; prevents silent loss of a P0 cook flow.
7. **Circuit breaker:** stop if the bot is not deployed; revert the storage configuration; no ledger data affected.

## Files to touch

- `backend/app/bot/cook_bot.py` — `build_dp()` and storage wiring.
- `backend/app/config.py` — explicit storage setting/path.
- `backend/README.md` — deployment and storage note.
- Focused bot tests for cross-dispatcher and restart survival.

Do not implement the Telegram allowlist (feature 403), derive the help list (feature 468), register `on_photo`, wire OCR/LLM, or add a command.

## Verification protocol reference

Follow the feature contract's `## Verification protocol`:

1. Run the new cross-dispatcher test before the fix and observe it fail.
2. Run it after the fix and observe it pass.
3. Run the restart-survival test.
4. Assert the production dispatcher does not use `MemoryStorage`.
5. Exercise `/start_today`, replace the dispatcher, and assert the persisted state is readable by the replacement dispatcher. **Do not require `on_photo` to run:** it is not registered (`backend/app/bot/cook_bot.py:85`) and registering it is outside this slice. Report the full photo-flow acceptance check as blocked until that registration lands.

A skipped persistence test is not a pass and must be reported as a skip. **The implementer must establish the test harness if the repository does not already contain one.**

## Rollback path

Revert to the default dispatcher construction and remove the setting. FSM state is transient; no business rows or ledger events are affected.

## Mandatory LE31 skill list

- `le31-conventions`
- `le31-v1-feature-pattern`
- `development`
- `speckit-specify`
- `speckit-plan`
- `speckit-tasks`
- `speckit-implement`
- `verify-before-fixing`
- `pre-merge-review`

## Linear reference

Created as a draft Feature sub-issue under the 2026-11-14 research issue. If Linear writes remain blocked, use `/opt/data/le31-daily-research-2026-11-14.linear-fallback.json` and record `linear: blocked`.
