# Feature 304 — `drwjkirkpatrick-web-the-pass-mit-hermes-powered-restaurant-kitchen-pass-agent-v1-vocabulary` (defer)

> **NEW observation (2026-10-10).** Documents in-window GitHub repo `drwjkirkpatrick-web/the-pass` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Python + Flask + Hermes-agent + SQLite, **pushed 2026-10-02T02:58:03Z** AND **created 2026-10-02T01:29:55Z** = IN-WINDOW BY BOTH FIELDS as an 8-day-old repo, **192 KB modest repo**, default_branch=`main`, archived=false, 22 modules, 316 tests, one simulated service day end-to-end). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-10): *"A Hermes-powered restaurant agent for the pass — helping one chef and one server earn a Michelin star. 22 modules, 317 tests, human-gated ordering."* The README reveals the actual product = **The Pass** = *"A Hermes-powered restaurant agent that lives at the pass — built to help one chef and one server earn a Michelin star. The pass is where a kitchen wins or loses its night. Every plate crosses it; every fire, every 86, every 'how long?' lands there. The Pass is a local-first agent that sits at that exact spot — watching ingredients, timing orders, guarding the cold chain, photographing plates, and keeping front and back of house in one conversation — so the two people it serves can put their whole attention on food and hospitality. It runs on a Jetson in the corner, talks to you on Telegram, and keeps every number it reports traceable to something that actually happened in your kitchen. Status: fully implemented — 30 modules, 316 tests, one simulated service day end to end. Hardware still to come: the pass camera and the temperature probes (both are single adapters behind interfaces that already exist)."* Topics (verbatim, parent-verified, 10): `flask, hermes-agent, kitchen-operations, michelin, michelin-star, prompts, python, restaurant, restaurant-agent, sqlite`. Bucket: **v1 (restaurant-vertical kitchen-pass-agent-vocabulary)** — Pick C of Daily Brainstorm 2026-10-10. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **Hermes-powered + restaurant-agent + kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + Telegram-interface-for-chef-server + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists + supplier-p90-delay-planning** 16-tuple-primitive as a persistent cross-section reference for the LE31 v1 *restaurant-vertical kitchen-pass-agent* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (8-day-old repo) using the same **Hermes framework** as this very cron runs on. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **Hermes-powered + restaurant-agent + kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + Telegram-interface-for-chef-server + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists + supplier-p90-delay-planning** 16-tuple-primitive: The Pass is a local-first agent that sits at the kitchen pass — watching ingredients, timing orders, guarding the cold chain, photographing plates, and keeping front and back of house in one conversation — so the two people it serves can put their whole attention on food and hospitality. It runs on a Jetson in the corner, talks to you on Telegram, and keeps every number it reports traceable to something that actually happened in your kitchen. This is the §3.1 *operator-observed-state* + §3.4 *non-AI-fallback + human-gate* invariant applied to the *chef-server-pair + Michelin-star-track + kitchen-pass + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line* dimension.
- A written record of the **Python + Flask + Hermes-agent + SQLite** stack-shape: this is **3/3 LE31-related stack primitives matched** (Python is the LE31 backend stack primitive; Flask is a sister-shape to FastAPI; Hermes-agent is the same framework as this very cron; SQLite is a sister-shape to Postgres). The **Hermes-powered** framing is the **same Hermes framework as this very cron runs on**; the *kitchen-pass* discipline IS the *LE31-cook-Telegram-bot-and-waiter-web-UI-cross-surface* primitive applied to the **single-restaurant + chef-server-pair + Michelin-star-track** dimension.
- A written record of the **operator-facing vocabulary** discipline: the chef (back of house) gets ingredient-list drafts from photos + recipe-scaling + supplier-delivery-record-learning + temperature-logging-against-HACCP-zones + prep-timers + mise-checks + order-cutoffs + delivery-windows + plate-counting + rack-counting; the server/host (front of house) gets briefings + sidework-checklists + restock + occasion-reminders + 86-warnings-before-pull + two-lane-urgent-vs-digest-line; the star track gets plate-photographs + live-dish-review + plate-scoring-trend. Sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 53/66 (offline-first) + feature 290 (restaurant-P&L-analytics).
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (8-day-old); (2) the stack-shape match is the value, not the code (LE31 v1 has no kitchen-pass-agent surface; the v1 charter is web-UI + Telegram-bot, not Hermes-agent + Jetson + HACCP-zones + temperature-probes); (3) the **Hermes-framework** connection is unique — the same Hermes framework as this very cron runs on; (4) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of The Pass codebase (8-day-old single-maintainer repo with no observed production usage + Flask + SQLite is a sister-shape to FastAPI + Postgres; the **Hermes-framework** import is a vendor dependency).
- Cross-pollination with the v1 charter §3.4 customer-facing-AI posture (The Pass is operator-tooling; the *human-gated-ordering* posture IS the §3.4 invariant; the *two-lane-urgent-vs-digest-line* posture IS the *operator-non-interruption* charter §3.4 invariant).
- Any vendor-relationship with the Hermes framework as a runtime dependency (LE31 v1 uses FastAPI + Postgres, not Hermes-agent + Flask + SQLite; the *Hermes-powered* framing is a sister-shape, not a 1:1 match).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v1 surface proposes "a kitchen-pass-agent + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists primitive" (e.g., a v1 surface that introduces a kitchen-pass-agent for the LE31 single-restaurant Swiss kitchen where the chef and server need to coordinate the pass, the chef needs HACCP-zone temperature logging, the server needs 86-warnings from live inventory, and the owner needs plate-scoring-trend for the Michelin-star-track), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "kitchen-pass-agent + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line" is a real demand signal*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same Hermes framework as this very cron runs on"*.

- **Evidence class**: observed (the description + topics + README name the primitives explicitly: `flask, hermes-agent, kitchen-operations, michelin, michelin-star, prompts, python, restaurant, restaurant-agent, sqlite` + *"22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line"*).
- **Confidence**: medium-high for the vocabulary match (the verbatim description + README name the 16-tuple-primitive set + the tech-stack + the kitchen-pass posture + the human-gated-ordering posture + the HACCP-zones posture + the temperature-probes posture + the p90-supplier-delivery-delay-planning posture + the plate-photograph-linking posture + the plate-scoring-trend posture + the Jetson-deployable posture + the 86-warnings-from-live-inventory posture + the two-lane-urgent-vs-digest-line posture); low for transferability (LE31 v1 has no kitchen-pass-agent surface; v1 charter is web-UI + Telegram-bot, not Hermes-agent + Jetson + HACCP-zones + temperature-probes).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no kitchen-pass-agent surface); the value is the *kitchen-pass-agent + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line* vocabulary — when the first v1 PR that adds a kitchen-pass-agent surface lands, The Pass pattern is a ready-made *named primitive* (and the **Hermes-framework** connection is unique — the same Hermes framework as this very cron runs on).

## Description

GitHub `drwjkirkpatrick-web/the-pass` (MIT, 0★/0⑂, Python + Flask + Hermes-agent + SQLite, pushed 2026-10-02T02:58:03Z, created 2026-10-02T01:29:55Z, 192 KB, default_branch=`main`, archived=false, 22 modules, 316 tests, one simulated service day end-to-end). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-10): *"A Hermes-powered restaurant agent for the pass — helping one chef and one server earn a Michelin star. 22 modules, 317 tests, human-gated ordering."*

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **Hermes-powered** — the agent is built on the Hermes framework, the same framework as this very cron runs on. The *Hermes-powered* primitive IS the *on-Hermes-framework* primitive applied to the *restaurant-vertical* dimension.
2. **Restaurant-agent for the pass** — The Pass is a local-first agent that sits at the kitchen pass. The *restaurant-agent* primitive IS the *restaurant-vertical-AI-agent* primitive applied to the *kitchen-pass* dimension.
3. **22 modules + 316 tests + one simulated service day end-to-end** — the codebase has 22 modules + 316 tests + one simulated service day end-to-end. The *22-modules + 316-tests + one-simulated-service-day-end-to-end* primitive IS the *test-coverage + end-to-end-simulation* discipline.
4. **Human-gated ordering** — every order requires an explicit human-gate before the agent executes. The *human-gated-ordering* primitive IS the *non-AI-fallback + human-gate* charter §3.4 invariant applied to the *kitchen-order* dimension.
5. **HACCP-zones + temperature-probes** — the agent logs temperatures against the owner's own HACCP zones; two breaches in a row becomes an urgent call to the kitchen. The *HACCP-zones + temperature-probes* primitive IS the *operator-observed-state* charter §3.1 invariant applied to the *food-safety* dimension.
6. **p90-supplier-delivery-delay-planning** — the agent learns each supplier's real delivery record and tells the owner the day to order so it lands the day before they need it (it plans against their p90 delay, not their average — order early to survive the bad delivery, not the typical one). The *p90-supplier-delivery-delay-planning* primitive IS the *deterministic-rules* charter §3.4 invariant applied to the *supplier-ordering* dimension.
7. **Plate-photograph-linking + plate-scoring-trend** — the agent photographs every dish on the pass, linked to the plate and the ticket; live dish review allows scoring a plate in seconds on a phone; the trend tells the owner whether tonight looked like last night. The *plate-photograph-linking + plate-scoring-trend* primitive IS the *deterministic-plate-quality-feedback* discipline applied to the *plate-quality-improvement* dimension.
8. **Jetson-deployable** — the agent runs on a Jetson in the corner. The *Jetson-deployable* primitive IS the §3.1 *on-premise-deployment* invariant.
9. **Telegram-interface-for-chef-server** — the agent talks to the chef and server on Telegram. The *Telegram-interface-for-chef-server* primitive IS the §3.1 *cook-Telegram-bot* invariant.
10. **86-warnings-from-live-inventory** — the agent issues 86 warnings before the chef has to pull the dish, straight from live inventory. The *86-warnings-from-live-inventory* primitive IS the *StockEntry-driven-86-warning* primitive applied to the *menu-availability* dimension.
11. **Two-lane-urgent-vs-digest-line** — urgent calls (allergies, 86s, a plate dying) need an acknowledgement and repeat until they get one; everything else queues into a digest so nobody is interrupted for rosemary. The *two-lane-urgent-vs-digest-line* primitive IS the *operator-non-interruption* charter §3.4 invariant applied to the *kitchen-line* dimension.
12. **Briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists** — the agent sends briefings, sidework checklists, restock and occasion reminders from the owner's own lists, never a preset. The *briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists* primitive IS the *charter-as-code* posture applied to the *front-of-house-routine* dimension.
13. **Python + Flask + Hermes-agent + SQLite** — the tech-stack. The *Python + Flask + Hermes-agent + SQLite* posture IS the *on-LE31-stack-sister-shape* invariant (Python is the LE31 backend stack primitive; Flask is a sister-shape to FastAPI; Hermes-agent is the same framework as this very cron; SQLite is a sister-shape to Postgres).

**The 1:1 mapping onto LE31 surface:**

| The-Pass primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Hermes-powered | (LE31 v1 is server-side + FastAPI; this very cron runs on Hermes) | v1 polish | **Not implemented** — v1 polish surface |
| Restaurant-agent for the pass | (LE31 v1 has no kitchen-pass surface) | v1 polish | **Not implemented** — v1 polish surface |
| 22 modules + 316 tests + one simulated service day end-to-end | (LE31 v1 has test coverage but no 22-modules + 316-tests target) | v1 polish | **Not implemented** — v1 polish surface |
| Human-gated ordering | (LE31 v1 has explicit-state-transitions but no AI-human-gate) | §3.1 / §3.4 ✓ | **Not implemented** — v1 polish surface |
| HACCP-zones + temperature-probes | (LE31 v1 has no HACCP-zone surface) | §3.1 ✓ | **Not implemented** — v1 polish surface |
| p90-supplier-delivery-delay-planning | `audit_logs` (append-only) | §3.4 ✓ | **Not implemented** — v1 polish surface |
| Plate-photograph-linking + plate-scoring-trend | (LE31 v1 has no plate-photograph surface) | v1 polish | **Not implemented** — v1 polish surface |
| Jetson-deployable | (LE31 v1 is server-side + Linux VPS, not Jetson) | §3.1 ✓ | **Not implemented** — different deployment |
| Telegram-interface-for-chef-server | (LE31 v1 has cook-Telegram-bot; v1 charter §3.1) | §3.1 ✓ | **Implemented (v1, partial)** — the *cook-Telegram-bot* is implemented in v1, but The Pass's *chef-server-pair* posture is a sister-shape, not a 1:1 match |
| 86-warnings-from-live-inventory | `StockEntry` (append-only) | §3.1 ✓ | **Not implemented** — v1 polish surface |
| Two-lane-urgent-vs-digest-line | (LE31 v1 has no two-lane-urgent-vs-digest-line) | v1 polish | **Not implemented** — v1 polish surface |
| Briefing + sidework + restock + occasion-reminders | (LE31 v1 has no briefing + sidework surface) | v1 polish | **Not implemented** — v1 polish surface |
| Python + Flask + Hermes-agent + SQLite | Python 3.13 + FastAPI + SQLModel + Postgres | §3.1 ✓ (Python match) | **Not implemented** — different stack |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that introduces a kitchen-pass-agent surface for the LE31 single-restaurant Swiss kitchen), the implementation would add:

1. A new `KitchenPassHaccpZone` table (Alembic migration) with columns: `id` (UUID), `zone_name` (str), `min_temperature_celsius` (Decimal), `max_temperature_celsius` (Decimal), `created_at`, `updated_at`.
2. A new `KitchenPassTemperatureProbe` table (Alembic migration) with columns: `id` (UUID), `zone_id` (UUID FK), `probe_name` (str), `temperature_celsius` (Decimal), `recorded_at` (timezone-aware datetime), `is_breach` (bool, computed).
3. A new `KitchenPassSupplierP90DelayPlan` table (Alembic migration) with columns: `id` (UUID), `supplier_id` (UUID FK), `p90_delay_days` (int), `order_lead_days` (int), `last_calculated_at` (timezone-aware datetime), `created_at`, `updated_at`.
4. A new `KitchenPassPlatePhotograph` table (Alembic migration) with columns: `id` (UUID), `order_id` (UUID FK), `plate_id` (str), `photograph_url` (str), `photographed_at` (timezone-aware datetime), `created_at`.
5. A new `KitchenPassPlateScore` table (Alembic migration) with columns: `id` (UUID), `plate_photograph_id` (UUID FK), `score` (int, 1-5), `scored_by_user_id` (UUID FK), `scored_at` (timezone-aware datetime), `created_at`.
6. A new `KitchenPassUrgentLane` + `KitchenPassDigestLane` table (Alembic migration) with columns: `id` (UUID), `lane_type` (enum: `urgent`, `digest`), `message` (str), `acknowledged_at` (nullable timezone-aware datetime), `created_at`.
7. A new `KitchenPassBriefing` + `KitchenPassSidework` + `KitchenPassRestock` + `KitchenPassOccasionReminder` table (Alembic migration) with columns: `id` (UUID), `reminder_type` (enum: `briefing`, `sidework`, `restock`, `occasion`), `message` (str), `scheduled_at` (timezone-aware datetime), `created_at`, `updated_at`.
8. A new `KitchenPass86Warning` table (Alembic migration) with columns: `id` (UUID), `menu_item_id` (UUID FK), `warning_message` (str), `warned_at` (timezone-aware datetime), `pulled_at` (nullable timezone-aware datetime), `created_at`.
9. An Alembic migration that adds the new tables.
10. A `KitchenPassHaccpZoneMonitor` service that polls the temperature probes every N seconds and emits a `KitchenPassUrgentLane` message if two breaches in a row.
11. A `KitchenPassSupplierP90DelayPlanCalculator` service that calculates the p90 delay from the supplier's delivery history.
12. A `KitchenPassPlatePhotographCapture` service that captures a photograph of each plate on the pass and links it to the order.
13. A `KitchenPass86WarningEmitter` service that emits a `KitchenPass86Warning` when the inventory for a menu item drops below a threshold.

The HANDOFF is to evaluate whether the v1 kitchen-pass-agent surface is the right product-wedge for the next v1 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires:

**For v1 restaurant-vertical kitchen-pass-agent-vocabulary surface** (if approved):

1. Add new `KitchenPassHaccpZone` SQLModel table (Alembic migration).
2. Add new `KitchenPassTemperatureProbe` SQLModel table (Alembic migration).
3. Add new `KitchenPassSupplierP90DelayPlan` SQLModel table (Alembic migration).
4. Add new `KitchenPassPlatePhotograph` SQLModel table (Alembic migration).
5. Add new `KitchenPassPlateScore` SQLModel table (Alembic migration).
6. Add new `KitchenPassUrgentLane` + `KitchenPassDigestLane` SQLModel table (Alembic migration).
7. Add new `KitchenPassBriefing` + `KitchenPassSidework` + `KitchenPassRestock` + `KitchenPassOccasionReminder` SQLModel table (Alembic migration).
8. Add new `KitchenPass86Warning` SQLModel table (Alembic migration).
9. Add Alembic migration for the new tables.
10. Add a `KitchenPassHaccpZoneMonitor` service that polls the temperature probes every N seconds and emits a `KitchenPassUrgentLane` message if two breaches in a row.
11. Add a `KitchenPassSupplierP90DelayPlanCalculator` service that calculates the p90 delay from the supplier's delivery history.
12. Add a `KitchenPassPlatePhotographCapture` service that captures a photograph of each plate on the pass and links it to the order.
13. Add a `KitchenPass86WarningEmitter` service that emits a `KitchenPass86Warning` when the inventory for a menu item drops below a threshold.
14. Add a `KitchenPassTwoLaneMessageRouter` service that routes urgent messages to the urgent lane (with acknowledgement + repeat) and digest messages to the digest lane.
15. Add a `kitchen-pass.html` minimal-HTML/HTMX template with HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders discipline.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires, the v1 restaurant-vertical kitchen-pass-agent surface would add **a v1 cook-Telegram-kitchen-pass-agent primitive** (e.g., the cook Telegram bot subscribes to the kitchen-pass-agent's two-lane-urgent-vs-digest-line + HACCP-zone + temperature-probe + p90-supplier-delivery-delay + 86-warning events and receives them in real-time). The kitchen-pass-agent primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 53/66 (offline-first).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; The Pass stack is Python + Flask + Hermes-agent + SQLite which is a sister-shape, not a 1:1 match; the **Hermes-framework** connection is unique — the same Hermes framework as this very cron runs on).
- **External**: Jetson hardware (for The Pass deployment; LE31 v1 is server-side + Linux VPS, not Jetson).
- **Internal**: §3.1 (operator-observed-state + on-premise-deployment + cook-Telegram-bot invariant); §3.2 (MIT permissive license compatible); §3.4 (non-AI-fallback + human-gate + operator-non-interruption invariant).
- **Trigger dependency**: future v1 PR that adds a kitchen-pass-agent surface for the LE31 single-restaurant Swiss kitchen.

## Open questions

- **Q1**: When (if ever) will LE31 introduce a kitchen-pass-agent surface? The v1 charter explicitly uses HTTP + Postgres + FastAPI; v1 is server-side + Linux VPS, not Hermes-agent + Flask + SQLite + Jetson.
- **Q2**: If the kitchen-pass-agent surface lands, will it use the Hermes framework (like The Pass) or FastAPI (like LE31 v1)? The Hermes-framework approach is a different runtime model from the FastAPI approach; the **Hermes-framework** connection is unique — the same Hermes framework as this very cron runs on.
- **Q3**: Will the *human-gated-ordering* primitive be §3.4-compliant? The *human-gated-ordering* posture IS the *non-AI-fallback + human-gate* charter §3.4 invariant; LE31 v1's `audit_logs` is already append-only + idempotent, which is the foundation for human-gated-ordering.
- **Q4**: How will the *HACCP-zones + temperature-probes* primitive interact with LE31 v1's deployment model? The v1 deployment is a single Linux VPS (not Jetson + temperature-probe hardware); the HACCP-zones + temperature-probes posture is a different hardware model.
- **Q5**: How will the *86-warnings-from-live-inventory* posture interact with LE31 v1's `StockEntry` schema? The v1 `StockEntry` is append-only + idempotent; the *86-warnings-from-live-inventory* posture IS the *StockEntry-driven-86-warning* primitive applied to the *menu-availability* dimension; a future v1 PR could add a `menu_availability_warning` column to `StockEntry` or a separate `KitchenPass86Warning` table.

## Why this matters

The **Hermes-powered + restaurant-agent + kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + Telegram-interface-for-chef-server + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists** 16-tuple-primitive is the **strongest direct LE31 v1 restaurant-vertical kitchen-pass-agent-vocabulary reference of the 73-pass series** for three reasons:

1. **The 16-tuple-primitive vocabulary is the future v1 polish surface primitive**: when LE31 v1 introduces a kitchen-pass-agent surface (e.g., a v1 surface that lets the chef and server coordinate the pass, the chef get HACCP-zone temperature logging, the server get 86-warnings from live inventory, and the owner get plate-scoring-trend for the Michelin-star-track), the Hermes-powered + restaurant-agent + kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + Telegram-interface-for-chef-server + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line + briefing + sidework + restock + occasion-reminders-from-the-owners-own-lists primitive is the gate that satisfies §3.1 + §3.4. The Pass pattern is a ready-made *named primitive* for this gate.

2. **The Hermes-framework connection is unique — the same Hermes framework as this very cron runs on**: The Pass is built on the Hermes framework, the same framework that this very cron runs on. The *kitchen-pass* discipline IS the *LE31-cook-Telegram-bot-and-waiter-web-UI-cross-surface* primitive applied to the **single-restaurant + chef-server-pair + Michelin-star-track** dimension.

3. **The 8-day-old repo with 22-modules + 316-tests + one simulated service day end-to-end is the demand signal**: the maintainer has shipped a fully-implemented 30-modules + 316-tests + one simulated service day end-to-end product in 8 days without reading the LE31 charter. The demand for the *Hermes-powered + restaurant-agent + kitchen-pass + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line* primitive is real, observable, and growing.

Sister-shape to features 39 (owner-daily-recap-telegram) + 16 (supplier-orders-bot) + 53/66 (offline-first) + 290 (restaurant-P&L-analytics) + 295 (artisanal-bakery-operations POS) + 296 (bilingual-EN-Chinese + AI-phone-order-agent + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests) + 297 (open-source-business-engine + AI-agents + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country) + 298 (cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt + customer-loyalty). The Pass pattern is the **strongest direct Hermes-powered + restaurant-agent + kitchen-pass + 22-modules + 316-tests + one simulated service day end-to-end + human-gated-ordering + HACCP-zones + temperature-probes + p90-supplier-delivery-delay-planning + plate-photograph-linking + plate-scoring-trend + Jetson-deployable + 86-warnings-from-live-inventory + two-lane-urgent-vs-digest-line primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that adds a kitchen-pass-agent surface for the LE31 single-restaurant Swiss kitchen.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/39-...owner-daily-recap-telegram.md` — owner-daily-recap-telegram surface
- `features/16-...supplier-orders-bot.md` — supplier-orders-bot surface
- `features/53-...offline-first-v1-polish.md` and `features/66-...offline-first-v1-polish.md` — v1 offline-first primitives
- `features/290-AlvaroVerona-prime-cost-...-restaurant-p-l-menu-engineering.md` — restaurant-P&L + menu-engineering + demand-forecast + staffing-optimization + monte-carlo; sister-shape (restaurant-P&L primitive)
- `features/295-23f3000434-CakeShopManagement-...-artisanal-bakery-operations-pos.md` — artisanal-bakery-operations POS + Flask + React 19 + Aiven-PostgreSQL; sister-shape (in-domain restaurant-vertical POS)
- `features/296-kerryshi-china-garden-call-agent-...-bilingual-en-chinese-ai-phone-order-agent.md` — bilingual-EN-Chinese + AI-phone-order-agent + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests; sister-shape (restaurant-vertical human-gated-ordering primitive)
- `features/297-jonalemndi2-ALdia-...-open-source-business-engine-ai-agents-mcp-tools.md` — open-source-business-engine + AI-agents + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country; sister-shape (idempotency + immutable-audit-trail posture)
- `features/298-erhatechnologiesai-point-of-sale-system-...-cloud-pos-touchscreen-cashier-register.md` — cloud-POS + touchscreen-cashier-register + mock-payments + automated-receipt + customer-loyalty + FastAPI + Pydantic + SQLite; sister-shape (FastAPI + Pydantic + SQLite stack match)
