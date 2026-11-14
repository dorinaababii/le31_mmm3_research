# Feature 478 — The cook bot's FSM state lives in aiogram `MemoryStorage`, so it disappears across workers and restarts

> **Pick B of Daily Research 2026-11-14.** **First-party, execution-proven.**
>
> **Executed against aiogram 3.31.0 and LE31's own dispatcher (2026-11-14):**
>
> ```text
> type(dp.fsm.storage).__name__ == 'MemoryStorage'
> writer dispatcher state   -> awaiting_photo
> second dispatcher reads   -> None
> fresh dispatcher reads    -> None
> ```
>
> `backend/app/bot/cook_bot.py:81` calls `Dispatcher()` without `storage=`. `backend/app/main.py:8` documents production as `uvicorn … --workers 2`.

## Goal

Make the cook's in-flight `/start_today` flow survive the deployment realities LE31 already documents: multiple workers and process restarts.

**The single sentence this feature exists to make true:** *a cook who started `/start_today` can send the photo after a worker restart or a second-worker handoff without losing the flow.*

## Scope

**In scope (v1):**

- One explicit persistent FSM storage configuration for `build_dp()`.
- One storage backend and serialization format for the existing `CookFlow` states.
- One test that writes a state, creates a second dispatcher against the same storage, and reads the state back.
- One restart-survival test or deterministic equivalent.

**Out of scope (v1):**

- The bot allowlist and role model (feature 403).
- Deriving `/help` from the dispatcher registry (feature 468).
- Registering `on_photo`, the OCR pipeline, the LLM call, or any new command.
- The cook menu-photo workflow beyond preserving its existing FSM states.
- Customer-facing AI or any new AI behavior.

## Out of scope

The exclusions listed under **Scope** are binding: the Telegram allowlist (feature 403), deriving `/help` (feature 468), registering `on_photo`, OCR/LLM wiring, new commands, and the broader menu-photo workflow.

## Description

`cmd_start_today` writes `CookFlow.awaiting_photo` into the dispatcher's `FSMContext`. The dispatcher's storage defaults to `MemoryStorage`, which holds state in the Python process.

That makes the state correct only while the same process continues serving the same user. Under the documented `--workers 2` topology, Telegram polling can deliver the photo to a worker that did not handle `/start_today`; the handler reads no state and silently returns. A restart loses every in-flight flow.

The failure is quiet because the photo handler explicitly ignores a photo when the state is not `awaiting_photo`. The cook sees no response and no explanation.

## Data model

No LE31 business-model change. The storage backend owns its own serialization. For a filesystem or Redis-backed aiogram storage, the stored key must include the bot/session identity so one restaurant's flow cannot be read by another context.

The persisted FSM payload remains exactly the existing `CookFlow` state values; no new state is introduced.

## Implementation steps

1. Choose and document one persistent aiogram storage backend compatible with the fixed stack. The default is a filesystem-backed implementation unless the owner chooses Redis, which would add infrastructure and must be an explicit decision.
2. Pass it explicitly to `Dispatcher(storage=...)` in `build_dp()`; do not rely on the default.
3. Ensure the storage path or connection setting comes from `Settings` with an explicit development default. **aiogram 3.31.0 does not ship a filesystem storage implementation**; the implementer must therefore either use an already-approved compatible backend or explicitly add one as a named dependency decision. This contract does not pretend a no-dependency filesystem option exists.
4. Write a failing test first: create dispatcher A, set `CookFlow.awaiting_photo`, create dispatcher B over the same storage, and assert dispatcher B reads `awaiting_photo`. On the current code this fails.
5. Add a restart-survival test: close dispatcher A, construct dispatcher C over the same storage, and assert the state remains.
6. Run the full bot test suite and verify the existing `/start_today` behavior still passes.

## Telegram interaction if any

No new command or visible message. The existing `/start_today` prompt and the existing photo acknowledgement remain the visible interaction. The improvement is that a photo arriving after a restart or on another worker is still accepted.

## Dependencies

- `backend/app/bot/cook_bot.py` — `build_dp()`, `cmd_start_today()`, `on_photo()`, `CookFlow`.
- `backend/app/config.py` — the storage path/connection setting.
- `backend/app/main.py:8` — the documented multi-worker deployment topology.
- aiogram 3.x persistent storage APIs. The probe was executed against aiogram 3.31.0.
- Feature 468 edits the same file's help text and dispatcher construction; feature 403 may add an allowlist. The regions are mostly disjoint, but the dispatcher construction line is shared and requires rebase awareness.

## Open questions

1. Filesystem or Redis? Filesystem keeps the stack fixed and is adequate for one VPS; Redis adds an operational dependency and should be chosen explicitly if the deployment becomes multi-host.
2. What is the retention period for abandoned flows? The default is to retain state until a normal FSM transition or a bounded expiry; no sensitive guest data is involved.
3. Should the bot fail closed if persistent storage is unavailable, or fall back to memory? The default is to fail visibly rather than silently accept a lossy mode in production.

## Why this matters

The morning menu-photo flow is one of the cook bot's P0 jobs. A cook who receives no reply after sending the photo cannot tell whether the bot failed, the message was lost, or they did something wrong. Silent state loss converts a normal morning step into a support incident.

## Adjacent evidence

- The photo handler is not currently registered; feature 468 scopes registration out. That does not change this contract: the storage defect exists independently and must be fixed before the handler is wired.
- Feature 403's role/allowlist is a separate authorization concern. This feature must not implement it.

## Verification protocol

1. The failing-before/passing-after cross-dispatcher test.
2. The restart-survival test.
3. Assert `type(dp.fsm.storage).__name__ != 'MemoryStorage'` in the production construction.
4. Exercise `/start_today`, write state, simulate dispatcher replacement, and assert the persisted state is readable by the new dispatcher. **Do not require the photo handler to run in this slice:** `on_photo` is not registered (`backend/app/bot/cook_bot.py:85`), and registering it belongs to another feature. A full photo-flow acceptance check is possible only after that registration lands and must be reported as blocked until then.
5. Verify the storage setting is documented in `backend/README.md` and no secret is written to the state payload.

## Rollback path

Revert to `Dispatcher()` with the default memory storage and remove the setting. No business data, ledger rows, or persisted business state exist in the FSM; only transient cook-flow state is affected.
