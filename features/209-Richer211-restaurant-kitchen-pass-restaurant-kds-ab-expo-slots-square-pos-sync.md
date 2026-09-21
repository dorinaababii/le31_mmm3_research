# Feature 209 — `Richer211-restaurant-kitchen-pass-restaurant-kds-ab-expo-slots-square-pos-sync` (defer)

> **NEW observation (2026-09-21).** Documents in-window GitHub Search `restaurant+language:python` query result: `Richer211/restaurant-kitchen-pass` (**1★/0⑂**, Python, **pushed 2026-09-01T12:51:53Z = 20 days ago** (in-window by `pushed_at`) + **created 2026-08-31T09:25:19Z = 21 days ago** (in-window by `created_at` — **BOTH fields in-window** = the *only of today's 3 picks that is a fresh discovery*, not just an off-window creation re-activated by a today push; the *only in-domain Python restaurant-KDS candidate of the 53-pass brainstorm series with both `pushed_at` AND `created_at` in-window*), **8866 KB substantial repo**, default_branch=`main`, archived=`False`, **0 topics — empty array**). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-21): *"Restaurant kitchen pass KDS: A/B slots and Square order sync."* The **kitchen-pass + A/B expo slots + Square POS sync** triple primitive — the *A/B expo slots* discipline is the *kitchen-display-system routing primitive* = *order-passes-to-slot-A-or-slot-B-based-on-cook-availability-or-order-type*; the *kitchen-pass* surface is the *expo-pass* primitive (the physical pass-through between kitchen and dining room where finished plates wait for waiters; the *expo-pass-discipline* is the *order-completion-notification* pattern); the *Square order sync* primitive is the *POS-integration pattern* (Square = a popular SMB POS; *Square order sync* = the *POS-side-order-inbox* that LE31 v1's webhook surface would need to ingest). The **only in-domain Python restaurant-KDS candidate of the 53-pass series with both fields in-window** is the *strongest in-domain restaurant-tech data point* of the 53-pass series; the **null license** (`spdx_id: null` in raw JSON) blocks §3.2 code adoption (vocabulary-only artifact). Charter §3.1 alignment (the *A/B expo slots* discipline is the *order-routing-to-cook* pattern applied to charter §3.1's *explicit-state-transition* discipline; the *Square order sync* discipline is the *POS-side-order-inbox* pattern applied to charter §3.1's *explicit-state-transition* discipline); §3.2 BLOCKER (null license; vocabulary-only artifact); §3.4 not triggered (no AI surface; the *A/B expo slots + Square POS sync* vocabulary is *operator-tooling*, not customer-facing AI). Sister-shape to features 40/77/79/83/110/117/153/170/176/191/195 (the *restaurant-POS + kitchen-workflow + cook-Telegram-bot* cluster) via the *kitchen-pass + A/B expo slots + Square POS sync* triple primitive. The phrase *"A/B slots"* names the *kitchen-display-system routing primitive* — when an order enters the kitchen, the KDS routes it to *slot A* or *slot B* based on cook availability or order type; the *A/B expo slots* discipline is the *order-routing-to-cook* pattern that any future LE31 v2 kitchen-display-system surface would need. The phrase *"Square order sync"* names the *POS-integration primitive* (Square = a popular SMB POS; *Square order sync* = the *POS-side-order-inbox* that LE31 v1's webhook surface would need to ingest). The phrase *"kitchen pass"* names the *expo-pass* surface (the expo-pass is the physical pass-through between kitchen and dining room where finished plates wait for waiters; the *expo-pass-discipline* is the *order-completion-notification* pattern that LE31 v1's `Order` SQLModel table supports). Cross-section with features 12/40/77/79/83/110/117/153/170/176/191/195 (the *restaurant-POS + kitchen-workflow + cook-Telegram-bot* cluster). **Fully reversible** (vocabulary-only artifact).

## Goal

Retain the **kitchen-pass + A/B expo slots + Square POS sync** cross-section architectural vocabulary + **the *A/B expo slots* discipline** + **the *kitchen-pass / expo-pass* primitive** + **the *Square POS sync / POS-side-order-inbox* primitive** as the persistent v1 in-domain restaurant-KDS reference for any future LE31 v1 maintainer asking the *kitchen-display-system / expo-pass / POS-integration* question (does LE31 v1 ever need a kitchen-display-system surface? does LE31 v1 ever need an expo-pass surface? does LE31 v1 ever need an A/B-slot-routing primitive? does LE31 v1 ever need a Square-POS-integration surface?). The artifact is the persistent *kitchen-pass + A/B expo slots + Square POS sync* vocabulary as a *named* v1 in-domain restaurant-KDS reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `Richer211/restaurant-kitchen-pass` cross-section vocabulary: the **only in-domain Python restaurant-KDS candidate of the 53-pass series with both `pushed_at` AND `created_at` in-window**; the *A/B expo slots + Square POS sync + kitchen pass* triple primitive explicitly named in the description.
- A written record of the **kitchen-pass / expo-pass primitive**: the *expo-pass* surface is the physical pass-through between kitchen and dining room where finished plates wait for waiters; the *expo-pass-discipline* is the *order-completion-notification* pattern that LE31 v1's `Order` SQLModel table supports (the `Order.status` SQLModel column tracks `pending → in-kitchen → ready → served → closed`; the *order-completion-notification* primitive = when the cook marks the order `ready`, the expo-pass surface notifies the waiter).
- A written record of the **A/B expo slots primitive**: the *A/B expo slots* discipline is the *kitchen-display-system routing primitive* = *order-passes-to-slot-A-or-slot-B-based-on-cook-availability-or-order-type*; when an order enters the kitchen, the KDS routes it to *slot A* or *slot B* based on cook availability or order type; the *A/B expo slots* discipline is the *order-routing-to-cook* pattern that any future LE31 v2 kitchen-display-system surface would need.
- A written record of the **Square POS sync primitive**: the *Square order sync* discipline is the *POS-side-order-inbox* pattern (Square = a popular SMB POS; *Square order sync* = the *POS-side-order-inbox* that LE31 v1's webhook surface would need to ingest); the *POS-integration* primitive is the *POS-side-event-stream* pattern (the SMB POS pushes events to LE31; LE31 ingests the events into its `Order` SQLModel table).
- A written record of the **null license as a documented strictly-vocabulary-only artifact**: the codebase CANNOT be adopted as a v1 dependency without an explicit relicense (null = §3.2 BLOCKER for code adoption, vocabulary-only artifact); LE31 would re-implement the *A/B expo slots + Square POS sync + kitchen pass* vocabulary against its own FastAPI + SQLModel + aiogram v3 + Postgres stack, not import the null-license code (LE31 v1 has no kitchen-display-system surface today).
- A decision record: today's verdict is `defer (parking-lot)` because the *kitchen-pass + A/B expo slots + Square POS sync* vocabulary is a v1 in-domain restaurant-KDS reference, not a v1 or v2 build implication. v1 has no kitchen-display-system surface today; the *A/B expo slots + Square POS sync + kitchen pass* vocabulary documents the *future-extension* for the next v1 maintainer asking the *kitchen-display-system / expo-pass / POS-integration* question.

**Out of scope (defer artifact):**
- Any change to the LE31 v1 surface (no kitchen-display-system surface today, no A/B expo slots today, no Square POS sync today).
- Any change to the LE31 v1 cook Telegram bot (no A/B-slot-routing today; the cook-bot is purely transactional).
- Any change to the LE31 v1 waiter web UI (no expo-pass surface today).
- Adoption of the `Richer211/restaurant-kitchen-pass` code as a v1 dependency (the repo is 1★/0⑂ at 8866 KB with null license; the *A/B expo slots + Square POS sync* vocabulary would need to be independently re-implemented and validated against the LE31 v1's no-kitchen-display-system posture, not simply imported; the null license blocks §3.2 code adoption).
- Any change to the `audit_logs` table or `StockEntry` ledger today.
- Any new dependency on the `Richer211` maintainer.

## Evidence / JTBD

When a future LE31 v1 maintainer asks *"if v1 introduces a kitchen-display-system surface, an expo-pass surface, an A/B-slot-routing primitive, or a Square-POS-integration surface, what is the *A/B expo slots + kitchen-pass + Square POS sync* vocabulary that preserves the existing v1 no-kitchen-display-system + no-expo-pass + no-POS-integration posture?"*, the maintainer wants *evidence that another independent 2026 Python repo at 8866 KB with 1★/0⑂ + null license + 0 topics + both `pushed_at` AND `created_at` in-window is shipping the *kitchen-pass + A/B expo slots + Square POS sync* primitive as the v1 in-domain restaurant-KDS discipline*, but struggles because *v1 has no documented kitchen-display-system primitive in the charter*, so that *v1 can introduce the kitchen-display-system + A/B expo slots + Square POS sync vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*.

- **Evidence class**: observed (the `Richer211/restaurant-kitchen-pass` description explicitly names *"Restaurant kitchen pass KDS: A/B slots and Square order sync"* = the kitchen-pass + A/B expo slots + Square POS sync triple primitive).
- **Confidence**: medium for the *A/B expo slots + Square POS sync + kitchen pass* vocabulary (1★/0⑂ + null license + 0 topics + both fields in-window + description verbatim = §3.2 BLOCKER for code adoption, vocabulary-only artifact; the *A/B expo slots* discipline IS the *order-routing-to-cook* pattern applied to charter §3.1's *explicit-state-transition* discipline).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + A/B expo slots + Square POS sync documentation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + A/B expo slots + Square POS sync documentation**: when (if) LE31 v1 introduces a kitchen-display-system surface, an expo-pass surface, an A/B-slot-routing primitive, or a Square-POS-integration surface, the *kitchen-pass + A/B expo slots + Square POS sync* vocabulary is documented.

## Description

GitHub `Richer211/restaurant-kitchen-pass` (1★/0⑂, Python, pushed 2026-09-01T12:51:53Z + created 2026-08-31T09:25:19Z = both fields in-window, 8866 KB substantial repo).

Description (verbatim): *"Restaurant kitchen pass KDS: A/B slots and Square order sync."*

Topics: `[]` (no GitHub topics — empty array).

The **3 named in-domain restaurant-KDS primitives**:

| Richer211/restaurant-kitchen-pass primitive | LE31 v1 primitive | Match status |
|---|---|---|
| `kitchen-pass` (expo-pass surface) | (LE31 v1 has no expo-pass surface today; the `Order.status` SQLModel column tracks `pending → in-kitchen → ready → served → closed`) | **★ GAP: LE31 v1 has no expo-pass surface today** |
| `A/B slots` (A/B expo slots routing primitive) | (LE31 v1 has no A/B-slot-routing primitive today; the cook-bot is purely transactional) | **★ GAP: LE31 v1 has no A/B-slot-routing primitive today** |
| `Square order sync` (POS-integration primitive) | (LE31 v1 has no POS-integration surface today; the order-inbox is purely manual) | **★ GAP: LE31 v1 has no POS-integration primitive today** |

The **kitchen-pass / expo-pass primitive**: the *expo-pass* surface is the physical pass-through between kitchen and dining room where finished plates wait for waiters; the *expo-pass-discipline* is the *order-completion-notification* pattern that LE31 v1's `Order` SQLModel table supports (the `Order.status` SQLModel column tracks `pending → in-kitchen → ready → served → closed`; the *order-completion-notification* primitive = when the cook marks the order `ready`, the expo-pass surface notifies the waiter).

The **A/B expo slots primitive**: the *A/B expo slots* discipline is the *kitchen-display-system routing primitive* = *order-passes-to-slot-A-or-slot-B-based-on-cook-availability-or-order-type*; when an order enters the kitchen, the KDS routes it to *slot A* or *slot B* based on cook availability or order type; the *A/B expo slots* discipline is the *order-routing-to-cook* pattern that any future LE31 v2 kitchen-display-system surface would need. Example: a restaurant with 2 cooks; cook A handles hot dishes; cook B handles cold dishes; the KDS routes a hot-dish order to slot A and a cold-dish order to slot B; the *order-routing-to-cook* pattern is the *charter §3.1 explicit-state-transition discipline* applied to the cook-availability dimension.

The **Square POS sync primitive**: the *Square order sync* discipline is the *POS-side-order-inbox* pattern (Square = a popular SMB POS; *Square order sync* = the *POS-side-order-inbox* that LE31 v1's webhook surface would need to ingest); the *POS-integration* primitive is the *POS-side-event-stream* pattern (the SMB POS pushes events to LE31; LE31 ingests the events into its `Order` SQLModel table). The *POS-integration* primitive is the *charter §3.1 explicit-state-transition discipline* applied to the POS-side dimension: every POS-side event is an explicit user action (the waiter confirms the order on the POS → POS pushes event → LE31 ingests event → `Order` SQLModel row updated).

The **null license as a documented strictly-vocabulary-only artifact**: the codebase CANNOT be adopted as a v1 dependency without an explicit relicense (null = §3.2 BLOCKER for code adoption, vocabulary-only artifact); LE31 would re-implement the *A/B expo slots + Square POS sync + kitchen pass* vocabulary against its own FastAPI + SQLModel + aiogram v3 + Postgres stack, not import the null-license code (LE31 v1 has no kitchen-display-system surface today).

## Data model

**No LE31 data model change today.** The defer artifact is documentation only. The *A/B expo slots + Square POS sync + kitchen pass* primitive names the *kitchen-display-system + A/B-slot-routing + POS-integration* extensions that any future v1 schema change should consider; v1 maintainer decision required before adopting the kitchen-display-system surface (LE31 v1 currently operates no kitchen-display-system surface; kitchen-display-system is a v1 architecture-decision, not a v1 implementation task today).

## Implementation steps

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a kitchen-display-system surface to the LE31 v1 operator surface, an A/B-slot-routing primitive to the LE31 v1 cook-Telegram-bot, or a Square-POS-integration surface to the LE31 v1 webhook surface):

- `app/kds/` — possibly add (the kitchen-display-system module; depends on the v1 change).
- `app/kds/slots.py` — possibly add (the A/B-slot-routing primitive that routes orders to slot A or slot B; depends on the v1 change).
- `app/kds/expo_pass.py` — possibly add (the expo-pass surface that notifies waiters when orders are ready; depends on the v1 change).
- `app/integrations/square.py` — possibly add (the Square-POS-integration module; depends on the v1 change).
- `app/webhooks/square_webhook.py` — possibly add (the webhook receiver for Square POS events; depends on the v1 change).
- `tests/test_kds_slots.py` + `tests/test_expo_pass.py` + `tests/test_square_webhook.py` — possibly add (the integration tests for the kitchen-display-system + A/B-slot-routing + Square-POS-integration surfaces; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no kitchen-display-system surface added.

## Telegram interaction if any

None today. If a future v1 trigger fires (kitchen-display-system surface), the Telegram interaction could be extended with KDS-notifications: the cook sees an order assigned to slot A or slot B; the cook marks the order `ready` via the cook-bot; the expo-pass surface sends a notification to the waiter via Telegram; the waiter picks up the order from the expo-pass. The *A/B-slot-routing* discipline ensures the order is routed to the correct cook based on cook availability or order type; the *expo-pass* discipline ensures the waiter is notified when the order is ready.

## Dependencies

- No new dependency today.
- If a future v1 trigger fires:
  - Software: a Square POS SDK (e.g. `squareup` for Python; LE31 currently has no POS SDK dependency).
  - Software: a webhook receiver library (e.g. FastAPI's built-in webhook support; LE31 currently has no webhook receiver).
  - Schema: a `kds_slot` table for slot assignment + a `kds_assignment` table for order-to-slot mapping + a `square_event` table for POS-side event ingestion; depends on the v1 change.

## Open questions

- Should LE31 v1 introduce a kitchen-display-system surface (e.g. `app/kds/`)?
- Should LE31 v1 introduce an A/B-slot-routing primitive (e.g. `app/kds/slots.py`)?
- Should LE31 v1 introduce an expo-pass surface (e.g. `app/kds/expo_pass.py`)?
- Should LE31 v1 introduce a Square-POS-integration surface (e.g. `app/integrations/square.py`)?
- If yes to any of the above: should the v1 PR cross-reference this feature 209 contract + HANDOFF as the named architectural reference?

## Why this matters

The *kitchen-pass + A/B expo slots + Square POS sync* primitive is the **gap** between LE31 v1's no-kitchen-display-system + no-expo-pass + no-POS-integration posture and a *kitchen-display-system + A/B-slot-routing + POS-integration* v1 surface. The *A/B expo slots* discipline IS the *charter §3.1 explicit-state-transition discipline* applied to the cook-availability dimension; the *Square POS sync* discipline IS the *charter §3.1 explicit-state-transition discipline* applied to the POS-side dimension. For LE31 v1's kitchen-display-system + A/B-slot-routing + POS-integration surface, the Richer211/restaurant-kitchen-pass pattern is the *future-extension reference*: when (if) LE31 v1 introduces a kitchen-display-system surface, an A/B-slot-routing primitive, a Square-POS-integration surface, or an expo-pass surface, the *kitchen-pass + A/B expo slots + Square POS sync* vocabulary is documented. **The only in-domain Python restaurant-KDS candidate of the 53-pass series with both `pushed_at` AND `created_at` in-window** is the *strongest in-domain restaurant-tech data point* of the 53-pass series; the null license blocks §3.2 code adoption, but the *A/B expo slots + Square POS sync + kitchen pass* vocabulary is the **cross-section reference for any future LE31 v1 kitchen-display-system surface**.