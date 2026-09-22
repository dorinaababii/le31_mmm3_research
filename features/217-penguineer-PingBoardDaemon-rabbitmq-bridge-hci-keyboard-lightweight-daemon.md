# Feature 217 — `penguineer-PingBoardDaemon-rabbitmq-bridge-hci-keyboard-lightweight-daemon` (defer)

> **NEW observation (2026-09-22) — HONEST DISCLOSURE: previously surfaced 2026-09-21 as NOT-picked.** Documents in-window GitHub Search `topic:hci` query result: `penguineer/PingBoardDaemon` (**2★/0⑂**, **MIT ✓**, Python, **pushed 2026-09-21T05:44:42Z = YESTERDAY (~24h before fetch time)** (in-window by `pushed_at`) + **created 2022-04-04T18:57:55Z = ~4.4 years before the 2026-08-23 window-start = OUT-OF-WINDOW** (in-window by `pushed_at` only per SKILL hard rule), **516 KB modest repo**, default_branch=`main`, archived=`False`, `updated_at=2026-09-21T05:44:44Z`). **5 topics** (parent-verified verbatim from raw JSON): `amqp`, `hci`, `keyboard`, `productivity`, `rabbitmq`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-22): *"Connecting the PingBoard to RabbitMQ"*. The **PingBoard-to-RabbitMQ-bridge pattern** = the *lightweight-daemon-as-cross-channel-event-bus* primitive — the PingBoard is a physical-device button that emits keyboard events; the daemon converts the keyboard events to AMQP messages on a RabbitMQ broker; the AMQP messages are then consumed by any downstream consumer (e.g., a Telegram bot, a webhook receiver, a database writer). **HONEST DISCLOSURE**: this repo was previously surfaced in `/opt/data/le31-brainstorm-2026-09-21.md` §Operator UX and HCI signals section as a NOT-picked candidate — parent explicitly declined to pick it yesterday because of the thin description + low topic count; the subagent surfaced it again today and parent re-evaluates positively based on the *lightweight-RabbitMQ-bridge-daemon* primitive value, but the cross-section JTBD value is moderate and the prior-rejection is recorded honestly in this report. Charter §3.1 alignment (the *AMQP-message-bus* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension* — every physical-event transition is converted to an explicit AMQP message; no silent transition; the AMQP message is the explicit operator-action record); §3.2 STRICTLY-COMPATIBLE (MIT permissive); §3.4 not triggered (no AI surface; the *PingBoard-to-RabbitMQ-bridge* pattern is *operator-tooling*, not customer-facing AI). Sister-shape to features 144 (`silphe` operator-pointer-biometric HCI) + 211 (`alxndr-bnd/javi` delivery-comms-messenger-channel) via the *HCI-event-detection + cross-channel-event-bus + operator-tooling* cluster.

## Goal

Retain the **PingBoard-to-RabbitMQ-bridge pattern** + **the *AMQP-message-bus* discipline** + **the *lightweight-daemon-as-cross-channel-event-bus* primitive** as the persistent v2 HCI-cross-channel-event-bus reference for any future LE31 v2 maintainer asking the *physical-event-integration* question (does LE31 v2 ever need a cook-bell integration? does LE31 v2 ever need a receipt-printer integration? does LE31 v2 ever need a kitchen-pass-button integration? does LE31 v2 ever need a foot-traffic-counter integration?). The artifact is the persistent *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary as a *named* v2 HCI-cross-channel-event-bus reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `penguineer/PingBoardDaemon` cross-section vocabulary: the **only in-window-by-pushed-at-only v2 HCI-cross-channel-event-bus candidate today**; the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon-as-cross-channel-event-bus* triple primitive explicitly named in the description.
- A written record of the **AMQP-message-bus primitive**: the *AMQP-message-bus* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension* — every physical-event transition is converted to an explicit AMQP message; no silent transition; the AMQP message is the explicit operator-action record; the AMQP broker (RabbitMQ) routes the message to all subscribed consumers (Telegram bot, webhook receiver, database writer).
- A written record of the **lightweight-daemon-as-cross-channel-event-bus primitive**: the *lightweight-daemon* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension* — the daemon is a small, focused process that reads from one input (the PingBoard keyboard events) and writes to one output (the AMQP broker); the daemon does not process the events; the daemon only routes the events; the downstream consumers do the processing.
- A written record of the **MIT permissive license as §3.2 STRICTLY-COMPATIBLE**: the codebase CAN be imported as a v2 dependency under MIT permissive licensing (no copyleft restrictions, no source-disclosure requirements).
- A decision record: today's verdict is `defer (parking-lot)` because the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary is a v2 HCI-cross-channel-event-bus reference, not a v1 or v2 build implication. v1 has no physical-event-integration surface today; the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary documents the *future-extension* for the next v2 maintainer asking the *physical-event-integration* question. **HONEST DISCLOSURE**: this repo was previously surfaced in `/opt/data/le31-brainstorm-2026-09-21.md` §Operator UX and HCI signals section as a NOT-picked candidate — parent explicitly declined to pick it yesterday because of the thin description + low topic count; the subagent surfaced it again today and parent re-evaluates positively based on the *lightweight-RabbitMQ-bridge-daemon* primitive value, but the cross-section JTBD value is moderate and the prior-rejection is recorded honestly in this report.

**Out of scope (defer artifact):**
- Any change to the LE31 v1 surface (no physical-event-integration surface today, no cook-bell integration today, no receipt-printer integration today, no kitchen-pass-button integration today, no foot-traffic-counter integration today).
- Any change to the LE31 v1 cook Telegram bot (no AMQP-message-bus today; the cook-bot is purely transactional).
- Any change to the LE31 v1 waiter web UI (no lightweight-daemon-as-cross-channel-event-bus today; the waiter UI is purely transactional).
- Adoption of the `penguineer/PingBoardDaemon` code as a v2 dependency (the repo is 2★/0⑂ at 516 KB with MIT permissive license; the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary would need to be independently re-implemented and validated against the LE31 v1's no-physical-event-integration posture, not simply imported; vocabulary-only artifact today).
- Any change to the `audit_logs` table or `StockEntry` ledger today.
- Any new dependency on RabbitMQ or AMQP today.
- Any new dependency on the `penguineer` maintainer.

## Evidence / JTBD

When a future LE31 v2 maintainer asks *"if v2 introduces a physical-event-integration surface (cook-bell, receipt-printer, kitchen-pass-button, foot-traffic-counter), what is the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary that preserves the existing v1 no-physical-event-integration + no-AMQP-message-bus + no-lightweight-daemon posture?"*, the maintainer wants *evidence that another independent 2022 Python repo at 516 KB with 2★/0⑂ + MIT permissive license + 5 topics + in-window-by-pushed-at-only is shipping the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon-as-cross-channel-event-bus* primitive as the v2 HCI-cross-channel-event-bus discipline*, but struggles because *v1 has no documented physical-event-integration primitive in the charter*, so that *v2 can introduce the physical-event-integration + AMQP-message-bus + lightweight-daemon vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*.

- **Evidence class**: observed (the `penguineer/PingBoardDaemon` description explicitly names *"Connecting the PingBoard to RabbitMQ"* = the PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon triple primitive).
- **Confidence**: medium for the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary (2★/0⑂ + MIT permissive license + 5 topics + in-window-by-pushed-at-only + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *AMQP-message-bus* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension*; the *lightweight-daemon-as-cross-channel-event-bus* discipline is the *small-focused-process* pattern).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon documentation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon documentation**: when (if) LE31 v2 introduces a physical-event-integration surface, an AMQP-message-bus surface, or a lightweight-daemon-as-cross-channel-event-bus surface, the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary is documented.

## Description

GitHub `penguineer/PingBoardDaemon` (2★/0⑂, MIT ✓, Python, pushed 2026-09-21T05:44:42Z + created 2022-04-04T18:57:55Z = in-window by pushed_at only, 516 KB modest repo).

Description (verbatim): *"Connecting the PingBoard to RabbitMQ"*.

Topics: `amqp`, `hci`, `keyboard`, `productivity`, `rabbitmq`.

The **3 named v2 HCI-cross-channel-event-bus primitives**:

| `penguineer/PingBoardDaemon` primitive | LE31 v1 primitive | Match status |
|---|---|---|
| `PingBoard` (physical-device button) | (LE31 v1 has no physical-device integration today) | **★ GAP: LE31 v1 has no physical-device integration today** |
| `RabbitMQ` (AMQP broker) | (LE31 v1 has no AMQP broker today) | **★ GAP: LE31 v1 has no AMQP broker today** |
| `daemon` (lightweight cross-channel-event-bus daemon) | (LE31 v1 has no cross-channel-event-bus daemon today) | **★ GAP: LE31 v1 has no cross-channel-event-bus daemon today** |

The **PingBoard primitive**: the PingBoard is a physical-device button that emits keyboard events when pressed; the device is plugged into a USB port on the cook's terminal; the keyboard events are received by the daemon; the daemon converts the keyboard events to AMQP messages on a RabbitMQ broker.

The **AMQP-message-bus primitive**: the *AMQP-message-bus* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension* — every physical-event transition is converted to an explicit AMQP message; no silent transition; the AMQP message is the explicit operator-action record; the AMQP broker (RabbitMQ) routes the message to all subscribed consumers (Telegram bot, webhook receiver, database writer).

The **lightweight-daemon-as-cross-channel-event-bus primitive**: the *lightweight-daemon* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension* — the daemon is a small, focused process that reads from one input (the PingBoard keyboard events) and writes to one output (the AMQP broker); the daemon does not process the events; the daemon only routes the events; the downstream consumers do the processing.

## Data model

**No LE31 data model change today.** The defer artifact is documentation only. The *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* primitive names the *physical-event-integration + AMQP-message-bus + lightweight-daemon-as-cross-channel-event-bus* extensions that any future v2 schema change should consider; v2 maintainer decision required before adopting the physical-event-integration surface (LE31 v1 currently operates no physical-event-integration surface; physical-event-integration is a v2 architecture-decision, not a v1 implementation task today).

## Implementation steps

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a physical-event-integration surface to the LE31 v2 operator surface, an AMQP-message-bus surface, or a lightweight-daemon-as-cross-channel-event-bus surface):

- `app/physical_events/` — possibly add (the physical-event-integration module; depends on the v2 change).
- `app/physical_events/cook_bell.py` — possibly add (the cook-bell integration; depends on the v2 change).
- `app/physical_events/receipt_printer.py` — possibly add (the receipt-printer integration; depends on the v2 change).
- `app/physical_events/kitchen_pass_button.py` — possibly add (the kitchen-pass-button integration; depends on the v2 change).
- `app/amqp/bus.py` — possibly add (the AMQP-message-bus surface; depends on the v2 change).
- `app/amqp/daemon.py` — possibly add (the lightweight-daemon-as-cross-channel-event-bus surface; depends on the v2 change).
- `tests/test_cook_bell.py` + `tests/test_receipt_printer.py` + `tests/test_amqp_bus.py` + `tests/test_amqp_daemon.py` — possibly add (the integration tests for the physical-event-integration + AMQP-message-bus + lightweight-daemon surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no physical-event-integration surface added.

## Telegram interaction if any

None today. If a future v2 trigger fires (physical-event-integration surface), the Telegram interaction could be extended with physical-event-notifications: the cook gets a Telegram notification when the cook-bell is pressed; the cook gets a Telegram notification when the receipt-printer prints a receipt; the cook gets a Telegram notification when the kitchen-pass-button is pressed (the order is ready for pickup); the AMQP-message-bus routes the physical-event-notifications to the cook Telegram bot. The *lightweight-daemon* discipline ensures the physical-event-integration is decoupled from the Telegram bot (the daemon only routes the events; the Telegram bot processes the events).

## Dependencies

No new dependencies today. If the future v2 trigger fires, the dependencies would be:
- `aio-pika` (the async Python AMQP client; not in `requirements.txt` today).
- `pika` (the sync Python AMQP client; not in `requirements.txt` today).
- RabbitMQ broker (the AMQP broker; not deployed today).

LE31 v1 currently operates no physical-event-integration surface; the dependencies above would need to be added to `requirements.txt` only when the v2 surface is triggered.

## Open questions

1. **Does LE31 v2 ever need a physical-event-integration surface (cook-bell, receipt-printer, kitchen-pass-button, foot-traffic-counter)?** The cross-section value is the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary; v2 maintainer decision required before adopting the physical-event-integration surface.
2. **Does LE31 v2 ever need an AMQP-message-bus?** The *AMQP-message-bus* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension*; v2 maintainer decision required before adopting the AMQP-message-bus surface.
3. **Does LE31 v2 ever need a lightweight-daemon-as-cross-channel-event-bus?** The *lightweight-daemon* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension*; v2 maintainer decision required before adopting the lightweight-daemon surface.
4. **What triggers the v2 physical-event-integration surface?** The trigger condition is the first v2 PR that adds a physical-event-integration surface to the LE31 v2 operator surface, an AMQP-message-bus surface, or a lightweight-daemon-as-cross-channel-event-bus surface.

## Why this matters

The **PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon-as-cross-channel-event-bus** primitive is the most direct documented reference for any future LE31 v2 surface that asks the *physical-event-integration* question. Without this artifact, the next v2 maintainer would need to independently discover the *AMQP-message-bus + lightweight-daemon* discipline from scratch; with this artifact, the next v2 maintainer has a *named* reference that documents the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary as the v2 HCI-cross-channel-event-bus reference.

The cross-section value is the *AMQP-message-bus* discipline as the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension* — when (if) LE31 v2 introduces a physical-event-integration surface, the *AMQP-message-bus* discipline ensures every physical-event transition is converted to an explicit AMQP message; the *charter §3.1 explicit-state-transition discipline* is preserved at the cross-channel-event-routing dimension.

**HONEST DISCLOSURE**: the cross-section JTBD value is moderate; the repo's thin description (*"Connecting the PingBoard to RabbitMQ"*) does not provide a deep architectural reference; the parent previously declined to pick this repo in 2026-09-21 for the same reason; the parent re-evaluates positively today based on the *lightweight-RabbitMQ-bridge-daemon* primitive value but the cross-section JTBD value remains moderate.

The MIT permissive license is §3.2 STRICTLY-COMPATIBLE — the codebase CAN be imported as a v2 dependency under MIT permissive licensing (no copyleft restrictions, no source-disclosure requirements); this gives LE31 v2 maintainers the option to *import* the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* primitives rather than re-implementing them.