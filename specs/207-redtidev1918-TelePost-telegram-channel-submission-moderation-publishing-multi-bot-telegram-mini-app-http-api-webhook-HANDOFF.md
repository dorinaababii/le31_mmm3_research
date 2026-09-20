# 207 — redtidev1918/TelePost telegram-multi-bot-channel-moderation + Mini-App + HTTP-API + webhook + self-hosted HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 Telegram-operator + multi-bot + moderation + Mini-App + HTTP-API + webhook question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/207-redtidev1918-TelePost-telegram-channel-submission-moderation-publishing-multi-bot-telegram-mini-app-http-api-webhook.md` (defer artifact; **no code today**).

Bucket: **v2 Telegram-operator (Telegram-channel-operations + multi-bot + moderation + Mini-App + HTTP-API + webhook + self-hosted primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a Telegram-channel-bot for restaurant operations, multi-bot-coordination across multiple Telegram bots, a moderation-bot with human-review-queue, or a Mini App surface for guest-facing order placement, what is the Telegram-multi-bot-channel-moderation operator-tooling primitive that preserves the existing v1 single-bot + aiogram v3 + Telegram long-polling + no-Mini-App posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 2458 KB with MIT license + in-window-by-push-only + 16★/3⑂ + 15 topics including telegram + telegram-bot + telegram-channel + telegram-mini-app + multi-bot + publishing + moderation + http-api + webhook + submission + self-hosted + automation + content-management + python + python-telegram-bot is shipping the Telegram-channel-operations primitive as the v2 operator-tooling discipline*, but struggles because *v1 has no documented Telegram-channel-operations primitive in the charter*, so that *v2 can introduce the Telegram-channel-coordination + multi-bot + moderation + Mini-App + HTTP-API + webhook vocabulary with the explicit channel-operations discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no Telegram-channel-operations trigger; the JTBD is primitive vocabulary extension + Telegram-channel-operations documentation, not a build-need). |
| 2 | **Viability** | Owner can read 2458 KB repo description + 15-topic vocabulary + Telegram-multi-bot-channel-moderation + Mini-App + HTTP-API + webhook + self-hosted topic set? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v2 (the Telegram-channel-operations vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the python-telegram-bot code; LE31 v1 uses aiogram v3 not python-telegram-bot). Confidence: medium-high for the Telegram-multi-bot-channel-moderation + Mini-App + HTTP-API + webhook + self-hosted vocabulary (MIT + Python + 2458 KB substantial + in-window-by-push-only + 16★/3⑂ + 15 topics + explicit Telegram-channel-operations description + multi-bot + telegram-mini-app + moderation + http-api + webhook + submission + publishing + self-hosted = §3.2 STRICTLY-COMPATIBLE + §3.4 explicitly aligned for moderation-bot + Mini App requires future §3.4 review). Stack: FastAPI + PostgreSQL backend = on-pattern for v2 primitives; python-telegram-bot library = off-pattern for v1 (LE31 v1 uses aiogram v3, not python-telegram-bot); self-hosted + Python = on-pattern for v2; Mini App = customer-facing surface = charter §3.4 future-review required. Practicability of adoption: high for vocabulary + architecture-reference adoption (MIT §3.2 STRICTLY-COMPATIBLE); medium for code reuse (LE31 would re-implement against its own aiogram v3 stack, not import python-telegram-bot code). **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The Telegram-multi-bot-channel-moderation primitive is an *extension* of the existing v1 single-bot + aiogram v3 posture — not a replacement; the existing single cook-bot serves the cook channel; the multi-bot pattern would add new bots for new channels (waiter-bot + reservation-bot + review-bot + promo-bot + moderation-bot). Charter §3.1 alignment (multi-bot + content-pipeline + moderation-queue + explicit-state-transitions = explicit-state-transitions applied to Telegram channel content); §3.2 STRICTLY-COMPATIBLE (MIT license); §3.4 explicitly aligned for moderation-bot (operator-tooling, not customer-facing AI); Mini App requires future §3.4 review (customer-facing surface). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 Telegram-operator (Telegram-channel-operations + multi-bot + moderation + Mini-App + HTTP-API + webhook + self-hosted vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2458 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (2458 KB is substantial; only the *Telegram-multi-bot-channel-moderation + Mini-App + HTTP-API + webhook + self-hosted* vocabulary + the in-window-by-push-only signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/207-redtidev1918-TelePost-telegram-channel-submission-moderation-publishing-multi-bot-telegram-mini-app-http-api-webhook-HANDOFF.md` and `features/207-redtidev1918-TelePost-telegram-channel-submission-moderation-publishing-multi-bot-telegram-mini-app-http-api-webhook.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + Telegram-channel-operations + multi-bot + moderation + Mini-App + HTTP-API + webhook + self-hosted documentation for the next v2 Telegram-operator-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a Telegram-channel-bot to the LE31 operator surface, a multi-bot coordination pattern across multiple Telegram bots, a moderation-bot with human-review-queue, or a Mini App surface for guest-facing order placement):

- `app/bot/channels/` — possibly add (the multi-bot-coordination directory; each channel gets its own bot module; depends on the v2 change).
- `app/bot/moderation.py` — possibly add (the moderation-bot that applies AI-assist moderation + human-review; depends on the v2 change).
- `app/api/telegram_webhook.py` — possibly add (the HTTP-webhook endpoint for inbound Telegram events; replaces the aiogram v3 long-polling; depends on the v2 change).
- `app/api/telegram_http_api.py` — possibly add (the HTTP-API endpoint for outbound Telegram content-submission + status-check; depends on the v2 change).
- `app/web/mini_app.py` — possibly add (the Mini App web-app surface for guest-facing menu + order placement; depends on the v2 change; **charter §3.4 future-review required**).
- `tests/test_multi_bot.py` + `tests/test_moderation.py` + `tests/test_telegram_webhook.py` + `tests/test_telegram_http_api.py` + `tests/test_mini_app.py` — possibly add (the integration tests for the multi-bot-coordination + moderation + HTTP-webhook + HTTP-API + Mini App surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no Mini App added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/207-redtidev1918-TelePost-telegram-channel-submission-moderation-publishing-multi-bot-telegram-mini-app-http-api-webhook.md` exists and is read back by the parent.
- [ ] `specs/207-redtidev1918-TelePost-telegram-channel-submission-moderation-publishing-multi-bot-telegram-mini-app-http-api-webhook-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `redtidev1918/TelePost` description is quoted verbatim (2458 KB repo).
- [ ] The 16★/3⑂ + MIT license (§3.2 STRICTLY-COMPATIBLE for code adoption) + Python + in-window-by-push-only + 15 topics (the highest topic-count of any 2026-09-20 in-window Telegram-bot pick) is documented.
- [ ] The charter §3.1 alignment via *multi-bot + content-pipeline + moderation-queue + explicit-state-transitions* (explicit-state-transitions applied to Telegram channel content) is documented.
- [ ] The charter §3.4 explicitly-aligned-for-moderation-bot + Mini-App-future-review-required split is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a Telegram-channel-bot to the LE31 operator surface, a multi-bot coordination pattern across multiple Telegram bots, a moderation-bot with human-review-queue, or a Mini App surface for guest-facing order placement lands):**
- [ ] The PR is read back by the parent.
- [ ] The `redtidev1918/TelePost` Telegram-multi-bot-channel-moderation + Mini-App + HTTP-API + webhook + self-hosted vocabulary is evaluated against the PR's changes: does the change address the *multi-bot-coordination* discipline? does the change preserve the *content-moderation + moderation-bot* primitive? does the change preserve the *Mini-App + customer-facing-surface* future-review? does the change preserve the *HTTP-API + webhook* pair?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the `app/bot/channels/` multi-bot-coordination directory; remove the `app/bot/moderation.py` moderation-bot; remove the `app/api/telegram_webhook.py` HTTP-webhook endpoint; remove the `app/api/telegram_http_api.py` HTTP-API endpoint; remove the `app/web/mini_app.py` Mini App surface; restore the original `app/bot/cook.py` Telegram handler.
- Migration cost: depends on the v2 change; the Telegram-multi-bot-channel-moderation vocabulary is *additive architecture* (the new bots are *added alongside* the existing cook-bot; the moderation-bot is *new* code, not a schema change; the HTTP-webhook + HTTP-API endpoints are *new* routes; the Mini App is *new* code, not a schema change).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `StockEntry` table retains all rows; the new `bot_state` table is *new* data, not a schema change; the new `moderation_queue` table is *new* data, not a schema change; the verification log is a *new* document, not a schema change.

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
