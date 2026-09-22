# 217 — penguineer/PingBoardDaemon rabbitmq-bridge-hci-keyboard-lightweight-daemon HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 physical-event-integration + AMQP-message-bus + lightweight-daemon question becomes buildable. **Do not implement today.**
>
> **HONEST DISCLOSURE**: this repo was previously surfaced in `/opt/data/le31-brainstorm-2026-09-21.md` §Operator UX and HCI signals section as a NOT-picked candidate — parent explicitly declined to pick it yesterday because of the thin description + low topic count; the subagent surfaced it again today and parent re-evaluates positively based on the *lightweight-RabbitMQ-bridge-daemon* primitive value, but the cross-section JTBD value is moderate and the prior-rejection is recorded honestly in this report.

## 1. Active feature path

`features/217-penguineer-PingBoardDaemon-rabbitmq-bridge-hci-keyboard-lightweight-daemon.md` (defer artifact; **no code today**).

Bucket: **v2 HCI-cross-channel-event-bus + RabbitMQ-bridge + lightweight-daemon (PingBoard-to-RabbitMQ-bridge pattern = lightweight-daemon-as-cross-channel-event-bus primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a physical-event-integration surface (cook-bell, receipt-printer, kitchen-pass-button, foot-traffic-counter), what is the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary that preserves the existing v1 no-physical-event-integration + no-AMQP-message-bus + no-lightweight-daemon posture?'*, the maintainer wants *evidence that another independent 2022 Python repo at 516 KB with 2★/0⑂ + MIT permissive license + 5 topics + in-window-by-pushed-at-only is shipping the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon-as-cross-channel-event-bus* primitive as the v2 HCI-cross-channel-event-bus discipline*, but struggles because *v1 has no documented physical-event-integration primitive in the charter*, so that *v2 can introduce the physical-event-integration + AMQP-message-bus + lightweight-daemon vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no physical-event-integration trigger; the JTBD is primitive vocabulary extension + PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon documentation, not a build-need; **cross-section JTBD value is moderate**, honest disclosure recorded). |
| 2 | **Viability** | Owner can read 516 KB repo description + 5-topic vocabulary + PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon-as-cross-channel-event-bus triple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the MIT-permissive code; LE31 v1 has no physical-event-integration surface today). Confidence: medium for the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary (2★/0⑂ + MIT permissive license + 5 topics + in-window-by-pushed-at-only + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *AMQP-message-bus* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension*; the *lightweight-daemon* discipline IS the *small-focused-process* pattern). Stack: FastAPI + PostgreSQL backend = on-pattern for v1 primitives; physical-event-integration = off-pattern for v1 (LE31 v1 has no physical-event surface); AMQP-message-bus = off-pattern for v1 (LE31 v1 has no AMQP surface); lightweight-daemon = off-pattern for v1 (LE31 v1 has no daemon surface); MIT permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *AMQP-message-bus* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-channel-event-routing dimension* (every physical-event transition is converted to an explicit AMQP message; no silent transition). Charter §3.1 alignment (the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* vocabulary is *explicit-state-transition* applied to the cross-channel-event-routing dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive); §3.4 not triggered (no AI surface; the *PingBoard-to-RabbitMQ-bridge* pattern is *operator-tooling*, not customer-facing AI). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 HCI-cross-channel-event-bus + RabbitMQ-bridge + lightweight-daemon (PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon-as-cross-channel-event-bus vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 516 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: moderate** (516 KB is modest; the *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon* triple + the in-window-by-pushed-at-only signal need to be referenced; **cross-section JTBD value is moderate, honest disclosure recorded**). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/217-penguineer-PingBoardDaemon-rabbitmq-bridge-hci-keyboard-lightweight-daemon-HANDOFF.md` and `features/217-penguineer-PingBoardDaemon-rabbitmq-bridge-hci-keyboard-lightweight-daemon.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon documentation for the next v2 HCI-cross-channel-event-bus review moment; **cross-section JTBD value is moderate, honest disclosure recorded**).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a physical-event-integration surface to the LE31 v2 operator surface, an AMQP-message-bus surface, or a lightweight-daemon-as-cross-channel-event-bus surface):

- `app/physical_events/` — possibly add (the physical-event-integration module; depends on the v2 change).
- `app/physical_events/cook_bell.py` — possibly add (the cook-bell integration; depends on the v2 change).
- `app/physical_events/receipt_printer.py` — possibly add (the receipt-printer integration; depends on the v2 change).
- `app/physical_events/kitchen_pass_button.py` — possibly add (the kitchen-pass-button integration; depends on the v2 change).
- `app/amqp/bus.py` — possibly add (the AMQP-message-bus surface; depends on the v2 change).
- `app/amqp/daemon.py` — possibly add (the lightweight-daemon-as-cross-channel-event-bus surface; depends on the v2 change).
- `tests/test_cook_bell.py` + `tests/test_receipt_printer.py` + `tests/test_amqp_bus.py` + `tests/test_amqp_daemon.py` — possibly add (the integration tests for the physical-event-integration + AMQP-message-bus + lightweight-daemon surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no physical-event-integration surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/217-penguineer-PingBoardDaemon-rabbitmq-bridge-hci-keyboard-lightweight-daemon.md` exists and is read back by the parent.
- [ ] `specs/217-penguineer-PingBoardDaemon-rabbitmq-bridge-hci-keyboard-lightweight-daemon-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `penguineer/PingBoardDaemon` description is quoted verbatim (516 KB repo).
- [ ] The 2★/0⑂ + MIT permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption) + Python + in-window-by-pushed-at-only + 5 topics + description *"Connecting the PingBoard to RabbitMQ"* is documented.
- [ ] The charter §3.1 alignment via *AMQP-message-bus = explicit-state-transition discipline applied to cross-channel-event-routing* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (MIT permissive) is documented.
- [ ] The charter §3.4 not-triggered (no AI surface) is documented.
- [ ] The HONEST DISCLOSURE of prior-rejection in `/opt/data/le31-brainstorm-2026-09-21.md` §Operator UX and HCI signals section is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a physical-event-integration surface to the LE31 v2 operator surface, an AMQP-message-bus surface, or a lightweight-daemon-as-cross-channel-event-bus surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `penguineer/PingBoardDaemon` *PingBoard-to-RabbitMQ-bridge + AMQP-message-bus + lightweight-daemon-as-cross-channel-event-bus* vocabulary is evaluated against the PR's changes: does the change address the *physical-event-integration* discipline? does the change preserve the *AMQP-message-bus* primitive? does the change preserve the *lightweight-daemon* primitive? does the change preserve the *charter §3.1 explicit-state-transition* pattern?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 trigger (if the v2 physical-event-integration surface is adopted):**
- Disable path: feature flag `LE31_PHYSICAL_EVENTS_ENABLED = False` (default; gates all `app/physical_events/` routes); no data loss.
- Delete path: `rm -rf app/physical_events/ app/amqp/` + `rm -rf tests/test_cook_bell.py tests/test_receipt_printer.py tests/test_amqp_bus.py tests/test_amqp_daemon.py`; remove `aio-pika + pika` from `requirements.txt`; no retained data; no safe-failure-mode concern.
- Migration/rollback cost: low (no schema change; no `audit_logs` or `StockEntry` change).

## 6. Mandatory LE31 skill list (per `le31-feature-pipeline/SKILL.md` step 5)

The following skills MUST be loaded by the coding agent before any v2 trigger fires:

- `le31-conventions` — for the seven-check feature gate + charter §3.1 + §3.2 + §3.4 invariants.
- `le31-verification-protocol` — for the verification protocol + the "done means observed, not asserted" principle.
- `le31-feature-pattern` — for the existing v1 feature pattern (FastAPI + SQLModel + aiogram v3 + Postgres; first-class prepared-item stock via append-only `StockEntry` ledger).
- `le31-handoff-spec` — for the slice contract format (this file is an example).
- `le31-coding-agent-brief` — for the paste-in prompt that the coding agent will use to start work.

The following skills MAY be loaded depending on the trigger:

- `le31-research` — if the v2 trigger requires additional cross-section vocabulary.
- `le31-v1-feature-pattern` — if the v2 trigger requires extending the v1 feature pattern.
- `le31-frontend` / `le31-backend` — if the v2 trigger requires frontend or backend changes.