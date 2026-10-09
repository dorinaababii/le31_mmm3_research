# HANDOFF — 296-kerryshi-china-garden-call-agent-v1-restaurant-vertical-phone-order-agent-vocabulary

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-09
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/296-kerryshi-china-garden-call-agent-mit-bilingual-en-chinese-ai-phone-order-agent-family-chinese-takeout-rules-claude-haiku-parsing-state-machine-enforces-read-back-175-tests-v1-restaurant-vertical-phone-order-agent-vocabulary-reference.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; strongest v1 in-domain restaurant-vertical phone-order-agent cross-section pick of the 72-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window v1 in-domain restaurant-vertical phone-order-agent vocabulary reference (`kerryshi/china-garden-call-agent`, MIT, 0★/0⑨, 98 KB tiny, Python ✓ on-stack, 7 topics, IN-WINDOW BY BOTH FIELDS, 175 tests) for the next time the LE31 owner opens a v1 phone-order-agent surface window.

If the trigger condition (v1 phone-order-agent surface window opens) is met, the external coding agent should:

1. Read the active feature file in full.
2. Confirm the `kerryshi/china-garden-call-agent` repo is still in-window (pushed within last 7 days from the trigger date) and the description is still the same.
3. Implement the `PhoneOrder + PhoneOrderLineItem + PhoneOrderStateMachine` SQLModel tables as described in the active feature's Data model section.
4. Implement the deterministic-rules + Claude-Haiku-parsing pipeline (with charter-§3.4-review-approved Claude-Haiku usage).
5. Implement the state-machine (DRAFTING → PARSING → READ_BACK → CONFIRMED → SUBMITTED → ARCHIVED).
6. Implement the read-back-Twilio-TTS discipline (every call-back must read back the order to the caller before submitting).
7. Set up Twilio voice webhook endpoint.
8. Write 175+ tests covering state-machine transitions + parsing edge cases + read-back failures + bilingual menu items.
9. Run the v1 test suite + the new v1 phone-order test suite.
10. Surface any test failures to the owner (LE31 v1 has no phone-order handling today; the test suite will be green if `PhoneOrder + PhoneOrderLineItem + PhoneOrderStateMachine` are empty, but the read-back discipline must be verified against the v1 stack).
11. Verify the v1 `audit_logs + StockEntry + MenuItem` SQLModel tables are untouched (the v1 `PhoneOrder + PhoneOrderLineItem + PhoneOrderStateMachine` tables are NEW, not a migration of v1 `audit_logs`).
12. **CHARTER §3.4 RIPGL_REVIEW REQUIRED before implementation begins** — the *Claude-Haiku-parsing* posture IS the §3.4 *AI-as-phone-order-parser* candidate; the *state-machine-enforces-read-back + deterministic-rules + 175-tests* posture IS the *non-AI-fallback + observable-evidence + human-gate* §3.4 invariant. Explicit charter-§3.4-review needed before any v1 PR that adopts the *AI-phone-order-agent* posture with a customer-facing AI on the phone line.

If the trigger condition is **not** met, do nothing. The defer artifact can be safely ignored until the owner opens a v1 phone-order-agent surface window.

## Mandatory inputs

- **Active feature**: `features/296-kerryshi-china-garden-call-agent-mit-bilingual-en-chinese-ai-phone-order-agent-family-chinese-takeout-rules-claude-haiku-parsing-state-machine-enforces-read-back-175-tests-v1-restaurant-vertical-phone-order-agent-vocabulary-reference.md`
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-10-09.md` (pass 72, pick A)
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-09/verify_kerryshi_china-garden-call-agent.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 72-pass series**:
  - **Feature 295 — `23f3000434/CakeShopManagement`** — v1 in-domain bakery-POS
  - **Feature 195 — `skaslam1407/Restaurant-and-Cloud-Kitchen-Operations-Management`** — v1 frappe-erpnext-cloud-kitchen
  - **Feature 176 — `Sholu021/KitchenIQ`** — v1 fastapi-postgresql-restaurant-erp-fefo-ai-copilot
  - **Feature 218 — `LuisRG98/restaurant-saas-api`** — v1 production-restaurant-api-reference
  - **Feature 276 — `Mu7ammad01/Snacki-ndb`** — v1 restaurant-pwa-fastapi-vocabulary
  - **Yesterday's adjacent-evidence (2026-10-08)** — `ALPHAMAN-0/burgerCodeEmployes` (MIT, 0★/0⑨, 5KB tiny, Python, "Lightweight FastAPI employee management API for burger restaurants — employees, shifts, tips, weekly reports.") — off-pattern for v1 today (no tips surface in v1)

## Verification protocol

Per `le31-conventions/SKILL.md` verification protocol:
- All SQLModel tables must use `Decimal` for `unit_price_eur + line_total_eur + subtotal_eur + tax_eur + total_eur` fields (charter §3.6)
- All datetime fields must be timezone-aware (Europe/Paris per charter §3.6)
- All state-transitions must write to `audit_logs` via the standard LE31 audit-pipeline (charter §3.1 + §3.3)
- All on-stack dependencies (FastAPI, Pydantic) per charter §3.1 stack constraint
- All off-stack dependencies (Twilio, Claude Haiku, state-machine library) require explicit charter review

## Rollback path

The pick is a parking-lot vocabulary reference. If the trigger condition is met and the implementation does not work, the implementation can be rolled back by:
1. Dropping the `PhoneOrder + PhoneOrderLineItem + PhoneOrderStateMachine` SQLModel tables (no data loss expected; vocabulary-only references do not have production data)
2. Removing the Twilio webhook endpoint
3. Removing the `phone-order.html` minimal-HTML/HTMX template
4. Disabling the Claude Haiku integration

The rollback is fully reversible; no v1 data is touched.

## Mandatory LE31 skill list

The coding agent MUST load before starting any implementation:
- `le31-conventions` — for the standard v1 conventions (audit_logs, money discipline, Paris timezone)
- `le31-v1-feature-pattern` — for the standard v1 feature pattern (SQLModel tables + FastAPI endpoints + minimal-HTML/HTMX templates + Telegram interaction if any)
- `le31-handoff-spec` — for the slice handoff format (this document)
- `le31-coding-agent-brief` — for the paste-in prompt format (this slice contract is the paste-in prompt)

This is a **defer artifact**; the coding agent does NOT need to start implementation today. The trigger condition (v1 phone-order-agent surface window opens) is not met. The artifact is preserved on file for future surfacing.
