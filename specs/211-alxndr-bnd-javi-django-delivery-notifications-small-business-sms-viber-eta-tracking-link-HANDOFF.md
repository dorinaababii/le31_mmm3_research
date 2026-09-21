# 211 — alxndr-bnd/javi django-delivery-notifications-small-business-sms-viber-eta-tracking-link HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 delivery-rider-integration + customer-facing-messenger-channel + delivery-status-comms-automation + tracking-link-generation question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/211-alxndr-bnd-javi-django-delivery-notifications-small-business-sms-viber-eta-tracking-link.md` (defer artifact; **no code today**).

Bucket: **small-business delivery-comms operator-tooling (automated-delivery-status-comms-for-SMB-without-own-delivery-system-via-Viber/SMS + messenger-channel-as-customer-comms + ETA + tracking-link primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a delivery-rider-integration surface, a customer-facing-messenger-channel surface, a delivery-status-comms-automation primitive, or a tracking-link-generation primitive, what is the *automated-delivery-status-comms-for-SMB-without-own-delivery-system-via-Viber/SMS + messenger-channel-as-customer-comms + ETA + tracking-link* vocabulary that preserves the existing v1 no-delivery-notification + no-customer-facing-messenger-channel + no-Viber/SMS-integration posture?'*, the maintainer wants *evidence that another independent 2026 Python (Django) repo at 2605 KB with 0★/0⑂ + MIT permissive + in-window-by-push-only + 9 topics including delivery-notifications + delivery-tracking + logistics + small-business + sms + viber is shipping the *automated-delivery-status-comms-for-SMB-without-own-delivery-system-via-Viber/SMS + messenger-channel-as-customer-comms + ETA + tracking-link* primitive as the small-business delivery-comms operator-tooling discipline*, but struggles because *v1 has no documented delivery-notification primitive in the charter*, so that *v2 can introduce the delivery-rider-integration + customer-facing-messenger-channel + delivery-status-comms-automation + tracking-link-generation vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no delivery-notification trigger; the JTBD is primitive vocabulary extension + automated-delivery-status-comms + messenger-channel-as-customer-comms + ETA + tracking-link documentation, not a build-need). |
| 2 | **Viability** | Owner can read 2605 KB repo description + 9-topic vocabulary + automated-delivery-status-comms + messenger-channel-as-customer-comms + ETA + tracking-link quintuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v2 (the *automated-delivery-status-comms* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + Telegram-bot stack, not imported from the Django + Viber/SMS code; LE31 v1 has no delivery-notification surface today). Confidence: medium for the *automated-delivery-status-comms-for-SMB-without-own-delivery-system-via-Viber/SMS + messenger-channel-as-customer-comms + ETA + tracking-link* vocabulary (MIT + Python (Django) + 2605 KB substantial + in-window-by-push-only + 0★/0⑂ + 9 topics + explicit automated-delivery-status-comms description + 6 LE31-relevant topics = §3.2 STRICTLY-COMPATIBLE + §3.4 NOT triggered; the *messenger-channel-as-customer-comms* discipline IS the *customer-facing-communication-channel* primitive, not *customer-facing AI*; the **§3.4 hard block is on customer-facing *AI*, not customer-facing *messages***). Stack: FastAPI + PostgreSQL backend = on-pattern for v2 primitives; Telegram-bot = on-pattern for v2 messenger channel (LE31 v1 already uses aiogram 3.31.0 for the cook-bot); Viber/SMS = off-pattern for v1 (LE31 v1 has no Viber/SMS surface); MIT permissive = on-pattern for code adoption. Practicability of adoption: high for vocabulary + architecture-reference adoption (MIT §3.2 STRICTLY-COMPATIBLE); low for code reuse (LE31 would re-implement against its own FastAPI + aiogram v3 + Telegram-bot stack, not import the Django + Viber/SMS code). **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *messenger-channel-as-customer-comms* discipline IS the *charter §3.4 customer-facing-communication-channel* primitive (the §3.4 hard block is on customer-facing *AI*, not customer-facing *messages*; the Viber/SMS messages are deterministic-template-based-comms, not LLM-generated); the *SME-without-own-delivery-system* posture IS the *charter §3.1 one-small-restaurant* primitive applied to the delivery-tracking dimension. Charter §3.1 alignment (the *messenger-channel-as-customer-comms* vocabulary is *operator-tooling-messenger-channel*, not *customer-facing-action*; the *customer-confirms-before-action* discipline is preserved because the *automatic-status-comms* is purely informational, no customer-action-required); §3.2 STRICTLY-COMPATIBLE (MIT permissive); §3.4 NOT triggered (no AI surface; the *customer-facing-messenger-channel* is the *customer-facing-communication channel* not *customer-facing AI*). **PASS**. |
| 5 | **Outcome, appetite, scope** | small-business delivery-comms operator-tooling (automated-delivery-status-comms-for-SMB-without-own-delivery-system-via-Viber/SMS + messenger-channel-as-customer-comms + ETA + tracking-link vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2605 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (2605 KB is substantial; only the *automated-delivery-status-comms-for-SMB-without-own-delivery-system-via-Viber/SMS + messenger-channel-as-customer-comms + ETA + tracking-link* vocabulary + the in-window-by-push-only signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/211-alxndr-bnd-javi-django-delivery-notifications-small-business-sms-viber-eta-tracking-link-HANDOFF.md` and `features/211-alxndr-bnd-javi-django-delivery-notifications-small-business-sms-viber-eta-tracking-link.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + automated-delivery-status-comms + messenger-channel-as-customer-comms + ETA + tracking-link documentation for the next v2 small-business-delivery-comms-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a delivery-rider-integration surface to the LE31 v2 operator surface, a customer-facing-messenger-channel surface to the LE31 v2 architecture, a delivery-status-comms-automation primitive, or a tracking-link-generation primitive):

- `app/delivery/` — possibly add (the delivery-notification module; depends on the v2 change).
- `app/delivery/notifications.py` — possibly add (the automatic-delivery-status-comms module that pushes ETA + tracking-link updates via messenger channels; depends on the v2 change).
- `app/delivery/messenger_channels.py` — possibly add (the messenger-channel-as-customer-comms module that supports Viber/SMS/Telegram; depends on the v2 change).
- `app/delivery/eta.py` — possibly add (the automatic-ETA module that calculates ETA based on rider location + traffic; depends on the v2 change).
- `app/delivery/tracking_link.py` — possibly add (the tracking-link-generation module that generates a tracking link for the customer; depends on the v2 change).
- `tests/test_delivery_notifications.py` + `tests/test_messenger_channels.py` + `tests/test_eta.py` + `tests/test_tracking_link.py` — possibly add (the integration tests for the delivery-notification + messenger-channel-as-customer-comms + ETA + tracking-link-generation surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no delivery-notification surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/211-alxndr-bnd-javi-django-delivery-notifications-small-business-sms-viber-eta-tracking-link.md` exists and is read back by the parent.
- [ ] `specs/211-alxndr-bnd-javi-django-delivery-notifications-small-business-sms-viber-eta-tracking-link-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `alxndr-bnd/javi` description is quoted verbatim (2605 KB repo).
- [ ] The 0★/0⑂ + MIT permissive license (§3.2 STRICTLY-COMPATIBLE for code adoption) + Python (Django) + in-window-by-push-only + 9 topics (delivery-notifications + delivery-tracking + logistics + small-business + sms + viber = 6 LE31-relevant topics) is documented.
- [ ] The charter §3.1 alignment via *messenger-channel-as-customer-comms = operator-tooling-messenger-channel* + *SME-without-own-delivery-system = charter §3.1 one-small-restaurant applied to delivery-tracking dimension* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (MIT permissive) is documented.
- [ ] The charter §3.4 NOT-triggered (no AI surface; the *customer-facing-messenger-channel* is the *customer-facing-communication channel* not *customer-facing AI*) is documented.
- [ ] The Serbian-context territory-annotation (topic `serbia` is a *territory-context* annotation, not an architecture annotation) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a delivery-rider-integration surface to the LE31 v2 operator surface, a customer-facing-messenger-channel surface to the LE31 v2 architecture, a delivery-status-comms-automation primitive, or a tracking-link-generation primitive lands):**
- [ ] The PR is read back by the parent.
- [ ] The `alxndr-bnd/javi` *automated-delivery-status-comms-for-SMB-without-own-delivery-system-via-Viber/SMS + messenger-channel-as-customer-comms + ETA + tracking-link* vocabulary is evaluated against the PR's changes: does the change address the *automatic-status-comms-via-messenger-channel* discipline? does the change preserve the *messenger-channel-as-customer-comms* primitive? does the change preserve the *automatic-ETA + automatic-tracking-link* primitive? does the change preserve the *charter §3.1 explicit-state-transition* pattern? does the change preserve the *charter §3.4 no-customer-facing-AI* posture (the messenger channel is *customer-facing-communication*, not *customer-facing AI*)?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the `app/delivery/` delivery-notification module; remove the `app/delivery/notifications.py` automatic-delivery-status-comms module; remove the `app/delivery/messenger_channels.py` messenger-channel-as-customer-comms module; remove the `app/delivery/eta.py` automatic-ETA module; remove the `app/delivery/tracking_link.py` tracking-link-generation module; restore the original `app/main.py` FastAPI app.
- Migration cost: depends on the v2 change; the *automated-delivery-status-comms* vocabulary is *additive architecture* (the delivery module is *new* files; the notifications module is *new* code; the messenger-channels module is *new* code; the ETA module is *new* code; the tracking-link module is *new* code, not a schema change).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `StockEntry` table retains all rows; the new `delivery` table is *new* data, not a schema change; the new `delivery_eta` table is *new* data, not a schema change; the new `delivery_tracking_link` table is *new* data, not a schema change; the verification log is a *new* document, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:
1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.