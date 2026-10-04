# Pick A — `bablobanov/hermes-agent-telegram-dashboard` — v2 owner-pains Telegram-pinned-status-dashboard-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/272-bablobanov-hermes-agent-telegram-dashboard-mit-hermes-plugin-pinned-telegram-msg-freshness-config-drift-v2-owner-pains-telegram-pinned-status-dashboard-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2 PR that adds a `FloorPinTelegramMessage` SQLModel table (`message_id, chat_id, message_text, last_refresh_at, refresh_strategy`).
2. First v2 PR that adds a `FloorPinTelegramMessageRefresh` SQLModel table (`refresh_id, message_id, refresh_at, refresh_strategy, refresh_payload`) for the *re-render-on-cron-tick* discipline.
3. First v2 PR that adds a Hermes-Plugin surface (`le31/hermes/plugins/telegram_status_dashboard.py`) that pins a single Telegram message and re-renders it on every cron tick.
4. First v2 PR that adds an `/api/floor-pin-telegram-message` + `/api/floor-pin-telegram-message/<message_id>` + `/api/floor-pin-telegram-message/<message_id>/refresh` FastAPI endpoint set.
5. First v2 PR that adds a `floor-pin-telegram-message.html` minimal-HTML/HTMX template that renders *pinned-Telegram-message-as-status-dashboard* (note: this is the Hermes-Plugin HTML surface, not the pinned Telegram message itself).
6. First v2 PR that adopts the *freshness + account-limits + config-drift + last-backup* observability primitives on the existing owner-dashboard.
7. First v2 PR that adopts the *no-bot-token + no-Mini-App* security-minimization discipline on the existing cook-Telegram-bot.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v2 surface wants to add a **pinned-Telegram-message-status-dashboard** surface to the existing owner-dashboard + cook-Telegram-bot stack (e.g., a v2 surface that lets the owner glance at *agent-status / config-drift / last-backup* from a single pinned Telegram message in the existing cook-Telegram-bot chat WITHOUT requiring a separate Mini App or bot token), the owner wants a known-good Hermes-Plugin + Telegram-pinned-status-message + read-only-dashboard blueprint with freshness + account-limits + config-drift + last-backup + no-bot-token + no-Mini-App posture, but LE31 today has no pinned-Telegram-message-status-dashboard surface + no Hermes-Plugin surface + no config-drift-detection, so that any future v2 extension has a documented reference."* — PASS (links to features 254 + 258 + 264; justifies a new v2 pain).
2. **Viability** — Owner does not need to understand the implementation; they only see the *pinned-Telegram-message + read-only-dashboard + freshness + account-limits + config-drift + last-backup* surface on the existing minimal-HTML/HTMX owner-dashboard + the existing cook-Telegram-bot. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 STRICTLY-COMPATIBLE (operator-tooling + observable-evidence + non-AI-fallback posture; the *Telegram-pinned-status-message* is a NON-AI primitive); confidence **high** for vocabulary transferability, **low** for immediate LE31 v2 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling + observable-evidence + non-AI-surface; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v2 owner-pains** outcome (cross-section to features 197 + 246 + 254 + 264). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = low-medium (~100-200 lines of SQLModel + FastAPI + Hermes-Plugin + minimal-HTML/HTMX code; 5-10 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/floor_pin_telegram_message.py` (new) — `FloorPinTelegramMessage` + `FloorPinTelegramMessageRefresh` SQLModel tables
- `le31/app/services/floor_pin_telegram_message.py` (new) — service layer for `record_floor_pin_telegram_message` + `record_floor_pin_telegram_message_refresh` + `re_render_floor_pin_telegram_message`
- `le31/app/hermes/plugins/telegram_status_dashboard.py` (new) — Hermes-Plugin surface that pins a single Telegram message and re-renders it on every cron tick (operator-tooling only; **NO customer-facing AI per charter §3.4**)
- `le31/app/owner_dashboard/floor_pin_telegram_message.py` (new) — pinned-Telegram-message + read-only-dashboard + freshness + account-limits + config-drift + last-backup primitive (SQLite-based local-cache + cloud-sync-when-online; **no-AI-surface + operator-tooling-only per charter §3.4**)
- `le31/app/api/v1/floor_pin_telegram_message.py` (new) — HTTP endpoints: `GET /api/floor-pin-telegram-message` + `POST /api/floor-pin-telegram-message` + `GET /api/floor-pin-telegram-message/<message_id>` + `POST /api/floor-pin-telegram-message/<message_id>/refresh`
- `le31/app/owner_dashboard/templates/floor_pin_telegram_message.html` (new) — minimal-HTML/HTMX owner-dashboard template for floor-pin-telegram-message status-dashboard
- `le31/migrations/versions/<revision>_floor_pin_telegram_message.py` (new) — Alembic migration for the two new tables

## Verification protocol reference

- Run `pytest le31/tests/test_floor_pin_telegram_message.py -v` to verify the new tables + endpoints + minimal-HTML/HTMX template
- Run `pytest le31/tests/test_hermes_plugin_telegram_status_dashboard.py -v` to verify the Hermes-Plugin surface
- Run `pytest le31/tests/test_charter_3_4_no_customer_facing_ai.py -v` to verify §3.4 no-customer-facing-AI invariant
- Run `pytest le31/tests/test_charter_3_6_money_primitive.py -v` to verify §3.6 money-primitive invariant (the *pinned-Telegram-message* is NOT a money-primitive)

## Rollback path

- Revert the SQLModel migration: `alembic downgrade -1`
- Delete the four new files (`le31/app/models/floor_pin_telegram_message.py` + `le31/app/services/floor_pin_telegram_message.py` + `le31/app/hermes/plugins/telegram_status_dashboard.py` + `le31/app/owner_dashboard/floor_pin_telegram_message.py` + `le31/app/api/v1/floor_pin_telegram_message.py` + `le31/app/owner_dashboard/templates/floor_pin_telegram_message.html` + `le31/migrations/versions/<revision>_floor_pin_telegram_message.py`)
- Unpin the pinned Telegram message (the existing cook-Telegram-bot can unpin via `bot.unpin_chat_message(chat_id=chat_id, message_id=message_id)`)
- Restart the FastAPI server

## Mandatory LE31 skill list

- `le31-conventions` (charter §3.1 + §3.2 + §3.3 + §3.4 + §3.6 + §3.7 invariants; seven-check feature gate)
- `le31-feature-pipeline` (vocabulary-to-build pipeline + parking-lot-vs-build decision)
- `le31-v1-feature-pattern` (existing v1 feature patterns + Hermes-Plugin architecture)
- `le31-cook-bot-ux` (existing cook-Telegram-bot surface; pinned-message discipline is an extension)
- `le31-data` (existing audit_logs + sqlmodel-extensions patterns)