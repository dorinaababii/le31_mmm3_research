# HANDOFF — Feature 271: `KeremCanArslan-telegram-business-bot-...-v1-telegram-operator-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/271-KeremCanArslan-telegram-business-bot-mit-telegram-bot-for-restaurants-menu-cart-orders-table-booking-owner-notifications-python-telegram-bot-v1-telegram-operator-vocabulary.md` — defer/parking-lot (Pick C of Daily Research 2026-10-09).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes a `Telegram-bot-for-restaurants + menu + cart orders + table booking + owner notifications` operator surface, the owner wants *evidence that this operator-UX shape exists in 2026*, but struggles because *LE31 has no documented in-window Telegram-operator reference*, so that *the v1 polish surface can be defended*. |
| 2 | Viability | ✓ | The owner can understand the operator UX. The 0-day-old single-maintainer repo makes code adoption not viable. |
| 3 | Practicability and confidence | ✓ | Uses `python-telegram-bot` (NOT aiogram) — partial stack match. The *operator-UX vocabulary* (menu/cart/booking/notifications) is portable to aiogram but the code is not. Evidence strength: high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant as a vocabulary reference. The `python-telegram-bot` library is NOT on LE31 stack (LE31 uses aiogram v3). The operator-UX primitives are §3.1-aligned. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 outcome (telegram-operator surface). Maximum time: 30 min documentation. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | ~15 min documentation; zero code cost. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. |

**Gate verdict**: **`defer` (parking-lot)`** — 7/7 checks pass; build verdict `defer` because the code is not adoptable (`python-telegram-bot` partial stack match + 0-day-old repo + 8 KB tiny size sketch-level implementation).

## Bucket

**v1** (telegram-operator-vocabulary) — the *operator-UX vocabulary* is the value, not the code. The `python-telegram-bot` partial stack match is the known caveat; the vocabulary is portable to aiogram v3.

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that extends the cook Telegram bot to a guest-facing surface, or first v1 PR that adds a guest-facing Telegram bot):

1. `backend/app/booking/models.py` — NEW: `Booking` SQLModel with `start_at + end_at + table_id` (Alembic migration).
2. `backend/app/notifications/models.py` — NEW: `NotificationSubscription` SQLModel with `chat_id + trigger_state` (Alembic migration).
3. `backend/app/order/models.py` — add `cart_state: String` column on `OrderItem` (Alembic migration).
4. `backend/app/bot/guest_dispatcher.py` — NEW: aiogram v3 guest-facing dispatcher with `view_menu`, `add_to_cart`, `confirm_order`, `book_table` handlers.
5. `backend/app/bot/owner_notifications.py` — NEW: aiogram v3 owner-notification handler that fires on every Order state transition.
6. New feature file at `features/NNN-guest-facing-telegram-bot.md` (NOT this defer artifact).

## Verification protocol

1. `git clone https://github.com/KeremCanArslan/telegram-business-bot` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/KeremCanArslan/telegram-business-bot/main/README.md` (deferred; the README is the source of truth for the verbatim description).
3. `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN" "https://api.github.com/repos/KeremCanArslan/telegram-business-bot"` for star count, fork count, license, language, pushed_at, created_at, topics (parent-verified 2026-10-09).
4. Pre-implementation §3.1 invariant check REQUIRED: every Order state transition (cart → confirmed → prepared → served → closed) must have an explicit user-action gate; no silent transitions.
5. Per `le31-conventions/SKILL.md`: load `le31-conventions`, `le31-research`, `le31-v1-feature-pattern`, `le31-handoff-spec`.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v1 trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop `Booking` + `NotificationSubscription` + `cart_state` columns + delete `guest_dispatcher.py` + `owner_notifications.py`.
- The existing cook bot is unaffected (the new surface is guest-facing only).

## Mandatory LE31 skill list

Before any implementation, the coding agent must load:
1. `le31-conventions` — the global LE31 decision layer (charter invariants + feature gate).
2. `le31-research` — the research workflow.
3. `le31-v1-feature-pattern` — v1 feature-pattern enforcement (aiogram v3 dispatcher pattern + explicit state transitions).
4. `le31-handoff-spec` — the handoff-spec requirements.

## Linear sub-issue reference

Sub-issue draft (deferred pending Linear MCP write endpoint recovery): `Research 2026-10-09 / Pick C — v1 telegram-operator-vocabulary (KeremCanArslan/telegram-business-bot)`. Parent fallback JSON captures the intended sub-issue at `/opt/data/le31-daily-research-2026-10-09.linear-fallback.json`.
