# HANDOFF — Feature 304: `drwjkirkpatrick-web-the-pass-...-v1-restaurant-vertical-kitchen-pass-agent-vocabulary-reference`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/304-drwjkirkpatrick-web-the-pass-mit-hermes-powered-restaurant-agent-kitchen-pass-22-modules-316-tests-human-gated-ordering-p90-supplier-delivery-planning-haccp-zones-telegram-chef-server-v1-restaurant-vertical-kitchen-pass-agent-vocabulary-reference.md` — defer/parking-lot (Pick C of Daily Brainstorm 2026-10-10).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes a *kitchen-pass-agent + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists primitive*, the owner wants *evidence that this restaurant-vertical kitchen-pass-agent-vocabulary exists in 2026 with the same Hermes framework as this very cron runs on*, but struggles because *LE31 has no documented v1 restaurant-vertical kitchen-pass-agent-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same Hermes framework + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (kitchen-pass + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists) without specialist help. The 0★ with single-maintainer cadence (8-day-old repo) makes code adoption not viable, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: **Python + Hermes-agent on-stack-sister-shape** (LE31 stack match for Python; the **Hermes-framework** is the same framework as this very cron; Flask is a sister-shape to FastAPI; SQLite is a sister-shape to Postgres). Required data + permissions + infrastructure: Python + Hermes-agent + Flask + SQLite + Jetson hardware. No AI capability required (the kitchen-pass-agent primitive is operator-tooling with human-gated-ordering; the *two-lane-urgent-vs-digest-line* posture IS the *operator-non-interruption* charter §3.4 invariant). Rabbit hole: the **Hermes-framework** import is a vendor dependency (LE31 v1 uses FastAPI + Postgres, not Hermes-agent + Flask + SQLite). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + Telegram-interface-for-chef-server + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists* primitives are §3.1 + §3.4-aligned (operator-observed-state + non-AI-fallback + human-gate + operator-non-interruption). The *HACCP-zones + temperature-probes* posture IS the §3.1 *operator-observed-state* invariant applied to the *food-safety* dimension. The *human-gated-ordering* posture IS the *non-AI-fallback + human-gate* charter §3.4 invariant. The *two-lane-urgent-vs-digest-line* posture IS the *operator-non-interruption* charter §3.4 invariant. No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (kitchen-pass-agent surface for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + cook-Telegram-bot) already implement the discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + 8-day-old repo + Hermes-framework vendor dependency + Flask + SQLite is a sister-shape to FastAPI + Postgres + Jetson hardware is off-LE31-deployment + no v1 kitchen-pass-agent surface in v1 charter).

## Bucket

**v1** (restaurant-vertical kitchen-pass-agent-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + README name the 16-tuple-primitive set (Hermes-powered + restaurant-agent + kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + Telegram-interface-for-chef-server + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists) + the tech-stack (Python + Flask + Hermes-agent + SQLite).

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds a kitchen-pass-agent surface for the LE31 single-restaurant Swiss kitchen):

1. `backend/app/kitchen_pass/models.py` — add new `KitchenPassHaccpZone` SQLModel table with columns: `id` (UUID), `zone_name` (str), `min_temperature_celsius` (Decimal), `max_temperature_celsius` (Decimal), `created_at`, `updated_at`.
2. `backend/app/kitchen_pass/models.py` — add new `KitchenPassTemperatureProbe` SQLModel table with columns: `id` (UUID), `zone_id` (UUID FK), `probe_name` (str), `temperature_celsius` (Decimal), `recorded_at` (timezone-aware datetime), `is_breach` (bool, computed).
3. `backend/app/kitchen_pass/models.py` — add new `KitchenPassSupplierP90DelayPlan` SQLModel table with columns: `id` (UUID), `supplier_id` (UUID FK), `p90_delay_days` (int), `order_lead_days` (int), `last_calculated_at` (timezone-aware datetime), `created_at`, `updated_at`.
4. `backend/app/kitchen_pass/models.py` — add new `KitchenPassPlatePhotograph` SQLModel table with columns: `id` (UUID), `order_id` (UUID FK), `plate_id` (str), `photograph_url` (str), `photographed_at` (timezone-aware datetime), `created_at`.
5. `backend/app/kitchen_pass/models.py` — add new `KitchenPassPlateScore` SQLModel table with columns: `id` (UUID), `plate_photograph_id` (UUID FK), `score` (int, 1-5), `scored_by_user_id` (UUID FK), `scored_at` (timezone-aware datetime), `created_at`.
6. `backend/app/kitchen_pass/models.py` — add new `KitchenPassUrgentLane` + `KitchenPassDigestLane` SQLModel table with columns: `id` (UUID), `lane_type` (enum: `urgent`, `digest`), `message` (str), `acknowledged_at` (nullable timezone-aware datetime), `created_at`.
7. `backend/app/kitchen_pass/models.py` — add new `KitchenPassBriefing` + `KitchenPassSidework` + `KitchenPassRestock` + `KitchenPassOccasionReminder` SQLModel table with columns: `id` (UUID), `reminder_type` (enum: `briefing`, `sidework`, `restock`, `occasion`), `message` (str), `scheduled_at` (timezone-aware datetime), `created_at`, `updated_at`.
8. `backend/app/kitchen_pass/models.py` — add new `KitchenPass86Warning` SQLModel table with columns: `id` (UUID), `menu_item_id` (UUID FK), `warning_message` (str), `warned_at` (timezone-aware datetime), `pulled_at` (nullable timezone-aware datetime), `created_at`.
9. `backend/alembic/versions/` — add Alembic migration for the new tables.
10. `backend/app/kitchen_pass/haccp_monitor.py` — NEW: `KitchenPassHaccpZoneMonitor` service that polls the temperature probes every N seconds and emits a `KitchenPassUrgentLane` message if two breaches in a row.
11. `backend/app/kitchen_pass/supplier_p90.py` — NEW: `KitchenPassSupplierP90DelayPlanCalculator` service that calculates the p90 delay from the supplier's delivery history.
12. `backend/app/kitchen_pass/plate_photograph.py` — NEW: `KitchenPassPlatePhotographCapture` service that captures a photograph of each plate on the pass and links it to the order.
13. `backend/app/kitchen_pass/warning_emitter.py` — NEW: `KitchenPass86WarningEmitter` service that emits a `KitchenPass86Warning` when the inventory for a menu item drops below a threshold.
14. `backend/app/kitchen_pass/message_router.py` — NEW: `KitchenPassTwoLaneMessageRouter` service that routes urgent messages to the urgent lane (with acknowledgement + repeat) and digest messages to the digest lane.
15. `backend/app/templates/kitchen_pass.html` — NEW: `kitchen-pass.html` minimal-HTML/HTMX template with HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders discipline.

## Verification protocol

1. `git clone https://github.com/drwjkirkpatrick-web/the-pass` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/drwjkirkpatrick-web/the-pass/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set + 16-tuple-primitive set + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line posture).
3. `curl -sS -H "Authorization: Bearer ***" "https://api.github.com/repos/drwjkirkpatrick-web/the-pass"` for star count, fork count, license, language, pushed_at, created_at, topics, description, default_branch, archived (parent-verified 2026-10-10).
4. `curl -sS -H "Authorization: Bearer ***" -H "Accept: application/vnd.github.raw" "https://api.github.com/repos/drwjkirkpatrick-web/the-pass/readme"` for the README body (parent-verified 2026-10-10).
5. `grep -cF 'LE31' /tmp/le31-brainstorm-2026-10-10/verify/drwjkirkpatrick-web_the-pass.json` (parent-verified 2026-10-10: 0 matches — PASS).
6. `grep -cF 'LE31' /tmp/le31-brainstorm-2026-10-10/verify/mhmd2042_cafe-pos.json /tmp/le31-brainstorm-2026-10-10/verify/AnuragBhandary_Real-Time-Event-Streaming.json /tmp/le31-brainstorm-2026-10-10/verify/drwjkirkpatrick-web_the-pass.json` (parent-verified 2026-10-10: 0 matches — PASS).
7. `grep -lE 'github.com/drwjkirkpatrick-web/the-pass|drwjkirkpatrick-web/the-pass' features/*.md` (parent-verified 2026-10-10: 0 matches — feature 304 is the only reference; the new feature file itself matches but the contract says it is the first).
8. If the future v1 trigger fires, run the v1 kitchen-pass-agent surface (FUTURE): `pytest backend/tests/kitchen_pass/test_haccp_monitor.py -v` for HACCP-zone-monitor tests; `pytest backend/tests/kitchen_pass/test_supplier_p90.py -v` for supplier-p90-delay-plan tests; `pytest backend/tests/kitchen_pass/test_plate_photograph.py -v` for plate-photograph tests; `pytest backend/tests/kitchen_pass/test_warning_emitter.py -v` for 86-warning-emitter tests; `pytest backend/tests/kitchen_pass/test_message_router.py -v` for two-lane-message-router tests; `pytest backend/tests/kitchen_pass/test_integration.py -v` for integration tests; `curl -X POST http://localhost:8000/api/kitchen-pass/haccp-zone` for smoke test; `curl -X GET http://localhost:8000/api/kitchen-pass/temperature-probe` for temperature-probe retrieval; `curl -X GET http://localhost:8000/api/kitchen-pass/plate-photograph` for plate-photograph retrieval.

## Rollback path

No code today. The handbook + HANDOFF can be reverted by `git rm features/304-drwjkirkpatrick-web-the-pass-...md specs/304-drwjkirkpatrick-web-the-pass-...-HANDOFF.md`.

If the future v1 trigger fires and the implementation is later rejected: `alembic downgrade -1` to drop the new tables; `git rm backend/app/kitchen_pass/models.py backend/app/kitchen_pass/haccp_monitor.py backend/app/kitchen_pass/supplier_p90.py backend/app/kitchen_pass/plate_photograph.py backend/app/kitchen_pass/warning_emitter.py backend/app/kitchen_pass/message_router.py backend/app/templates/kitchen_pass.html backend/alembic/versions/<new_migration>.py`.

## Mandatory LE31 skill list

The coding agent must load the following skills before starting any future implementation of feature 304:

- `le31-conventions` — for the seven-check feature gate and the charter §3.1 + §3.2 + §3.4 invariants
- `le31-backend` — for the FastAPI + SQLModel + Postgres + Alembic stack patterns
- `le31-frontend` — for the minimal-HTML/HTMX waiter-UI patterns
- `le31-data` — for the `StockEntry` + `audit_logs` SQLModel table patterns
- `le31-v1-feature-pattern` — for the v1 feature contract template + bucket + cross-section references
- `le31-handoff-spec` — for the slice contract structure (active feature path + seven-check gate verdict + files to touch + verification protocol + rollback path)
- `le31-coding-agent-brief` — for the coding-agent-brief generation pattern (this HANDOFF IS the brief; the agent does not need to re-generate it)

## Why this matters

The **Hermes-powered + restaurant-agent + kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + Telegram-interface-for-chef-server + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists** 16-tuple-primitive is the **strongest direct LE31 v1 restaurant-vertical kitchen-pass-agent-vocabulary reference of the 73-pass series** because it is the only in-window 2026-10 Python Hermes-powered restaurant-vertical kitchen-pass-agent-vocabulary candidate that combines all 16 sub-primitives (Hermes-powered + restaurant-agent + kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + Telegram-interface-for-chef-server + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists) in a single 8-day-old repo with 22-modules + 316-tests + one simulated service day end-to-end, AND the **Hermes-framework** connection is unique — the same Hermes framework as this very cron runs on.

Sister-shape to features 39 (owner-daily-recap-telegram) + 16 (supplier-orders-bot) + 53/66 (offline-first) + 290 (restaurant-P&L-analytics) + 295 (artisanal-bakery-operations POS) + 296 (bilingual-EN-Chinese + AI-phone-order-agent + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests) + 297 (open-source-business-engine + AI-agents + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country) + 298 (cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt + customer-loyalty). The Pass pattern is the **strongest direct Hermes-powered + restaurant-agent + kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that adds a kitchen-pass-agent surface for the LE31 single-restaurant Swiss kitchen.

**Fully reversible** (vocabulary-only artifact). No code today.
