# Slice Contract — `Antosha122-qr_qod_mobile_menu-mit-qr-menu-telegram-bot-restaurant-business-fine-tuning-ordering-in-telegram-bot-v1-qr-menu-telegram-bot-cross-section` (defer, parking-lot, vocabulary reference)

> **Active feature path:** `features/248-Antosha122-qr_qod_mobile_menu-mit-qr-menu-telegram-bot-restaurant-business-fine-tuning-ordering-in-telegram-bot-v1-qr-menu-telegram-bot-cross-section.md`
> **Linear sub-issue:** [linear: blocked] (workspace plan-limit error: *"You've exceeded the free issue limit for this workspace"* — 10th consecutive day; intended project `le31 v1 — Core MVP` P-HMM-3; intended label `Feature`; parent fallback at `/opt/data/le31-daily-research-2026-09-29.linear-fallback.json`)
> **Status:** defer (parking-lot, vocabulary reference; zero build time today)
> **Bucket:** v1 (cross-section to feature 11)
> **Trigger condition:** the first v1 PR that proposes a customer-facing Telegram-bot ordering surface, a QR-menu-as-entry-point surface, or a QR-menu + Telegram-bot integration.

## Seven-check gate verdict

| Gate item | Verdict | Evidence |
|---|---|---|
| 1. License (charter §3.2) | **PASS** — MIT ✓ STRICTLY-COMPATIBLE | parent-verified GitHub API direct-GET 2026-09-29: `license.spdx_id = "MIT"` |
| 2. Stack fit (charter §3.1 + Python) | **PASS** — Python + restaurant-domain + Telegram-bot | description verbatim: *"QR codes for menus and food ordering in a Telegram bot"* |
| 3. Customer-facing AI (charter §3.4) | **NOT TRIGGERED** — pure menu browsing + order placement, no AI in the loop | description contains no AI/LLM references; surface is operator-tooling for the restaurant, customer-facing-but-AI-free |
| 4. Stars (signal) | **PASS** — 1★ (modest signal) | parent-verified GitHub API direct-GET: `stargazers_count = 1`, `watchers_count = 1` |
| 5. In-window (≤7 days) | **PASS** — by `pushed_at` (2026-09-27T18:03:49Z) | parent-verified: `created_at = 2026-06-18T17:29:41Z` is OUT-OF-WINDOW but `pushed_at` is in-window |
| 6. LE31-shape-fit | **PASS** — feature 11 (QR-menu) cross-section with Telegram-bot vocabulary | the only in-window 2026 Python repo combining QR-menu + Telegram-bot + restaurant ordering |
| 7. No observed pain | **DEFER** — no LE31 owner pain (v1 has no QR-bot feature) | the artifact is vocabulary-only; trigger condition requires explicit owner/charter sign-off |
| **Final verdict** | **defer (parking-lot)** — vocabulary reference only | per le31-daily-research/SKILL.md hard rule "do not fabricate" + charter §3.1 invariant (v1 surface expansion requires explicit owner/charter sign-off) |

## Files to touch (when triggered)

If a future v1 PR is triggered by the trigger condition above, the implementation would touch:
1. `backend/app/models/qr_table.py` (new file) — SQLModel schema for the `qr_table` table
2. `backend/app/models/customer_session.py` (new file) — SQLModel schema for the `customer_session` table
3. `backend/app/routers/qr_menu.py` (new file) — FastAPI router for the `/qr_menu/<qr_token>` endpoint
4. `backend/app/bots/customer_bot.py` (new file) — aiogram 3.31.0 customer-facing Telegram-bot instance
5. `backend/app/bots/cook_bot.py` (modify) — add relay handler for customer-bot orders
6. `backend/app/services/stock_entry.py` (modify) — add `decrement_from_customer_order()` method
7. `frontend/templates/qr_menu.html` (new file) — HTMX template for the customer-facing QR-menu page
8. `tests/test_qr_menu.py` (new file) — pytest tests for the QR-menu + customer-bot flow
9. `docs/qr-menu.md` (new file) — owner documentation for the QR-menu surface
10. `specs/qr-menu-HANDOFF.md` (new file) — coding-agent handoff contract for the QR-menu surface

## Verification protocol reference

Per `verification-protocol/SKILL.md` (LE31 charter §3.5): every PR must pass:
1. `make test` — pytest full suite
2. `make lint` — ruff + mypy strict
3. `make type-check` — mypy --strict on all backend/app/**/*.py
4. `make smoke` — docker-compose up + curl health check
5. Manual: scan QR code at table → verify Telegram bot opens → place order → verify cook-bot receives → verify StockEntry decremented

## Rollback path

1. `git revert <commit-sha>` — single-commit revert
2. Drop the new tables (`qr_table`, `customer_session`, `customer_order`) — these are additive-only, no data loss
3. Stop the customer-bot instance — `docker-compose stop customer-bot`
4. Remove the QR-menu template — `rm frontend/templates/qr_menu.html`

## Mandatory LE31 skill list

When the coding agent starts work on this feature, the load MUST consult these skills in order:
1. `le31-conventions` — project conventions + git workflow
2. `le31-v1-feature-pattern` — v1 feature contract template
3. `le31-coding-agent-brief` — paste-in prompt template
4. `development` — full development pipeline (specify → plan → tasks → implement)
5. `speckit-implement` — task execution protocol
7. `pre-merge-review` — independent review before merge

## Notes on the trigger

LE31 v1 today does NOT have a customer-facing Telegram-bot surface. The cook-bot is text-only (texts sent to a fixed chat_id). The QR-menu + Telegram-bot ordering primitive would introduce a new customer-facing surface that requires:
- A separate aiogram bot instance for customer orders (different bot token, different chat_id namespace)
- A relay mechanism from customer-bot to cook-bot (separate from the cook-bot's existing chat)
- A QR-code-per-table generation flow (per-restaurant + per-table QR codes)
- A customer-session lifecycle (scan QR → land in bot → browse menu → place order → session ends)

This is a substantial v1 surface expansion that requires explicit owner/charter sign-off per charter §3.1 invariant. The defer artifact documents the *vocabulary* so the next owner review can scope it properly.

## Out of scope reminder

The artifact is vocabulary-only. Do NOT:
- Implement the QR-menu + Telegram-bot ordering surface today
- Add new dependencies (aiogram 3.31.0 is already pinned; no new deps required for vocabulary-only)
- Modify any v1 SQLModel schema
- Modify any v1 FastAPI router
- Modify any v1 aiogram bot handler
- Modify the audit_logs table
- Modify the StockEntry table

If any of the above is requested, escalate to the owner for explicit charter §3.1 sign-off before any code change.