# Feature 296 — `kerryshi/china-garden-call-agent` v1 in-domain restaurant-vertical phone-order-agent-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v1 (attach to `le31 v1 — Core MVP` P-HMM-3 as the parent of the sub-issue)
> **Date:** 2026-10-09
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/296-kerryshi-china-garden-call-agent-mit-bilingual-en-chinese-ai-phone-order-agent-family-chinese-takeout-rules-claude-haiku-parsing-state-machine-enforces-read-back-175-tests-v1-restaurant-vertical-phone-order-agent-vocabulary-reference.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/296-kerryshi-china-garden-call-agent-mit-bilingual-en-chinese-ai-phone-order-agent-family-chinese-takeout-rules-claude-haiku-parsing-state-machine-enforces-read-back-175-tests-v1-restaurant-vertical-phone-order-agent-vocabulary-HANDOFF.md`
> **Source daily brainstorm:** `/opt/data/le31-brainstorm-2026-10-09.md` (pass 72, pick A)
> **Parent-verified via:** direct GitHub API GET `/repos/kerryshi/china-garden-call-agent` at `/tmp/le31-brainstorm-2026-10-09/verify_kerryshi_china-garden-call-agent.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed; v1 in-domain restaurant-vertical phone-order-agent cross-section pick is a future-extension signal)

## Goal

Surface a v1 in-domain restaurant-vertical phone-order-agent-vocabulary reference for **bilingual-EN-Chinese-AI-phone-order-agent-for-family-Chinese-takeout + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests** as a forward-looking pattern for any future LE31 v1 surface that exposes a phone-order-agent with deterministic rules + LLM-parsing + operator-read-back enforcement + comprehensive tests.

## Evidence / JTBD

**Evidence classification:** inferred. The *bilingual-EN-Chinese-AI-phone-order-agent-for-family-Chinese-takeout + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests* discipline is forward-looking for any future LE31 v1 phone-order-agent-with-rules-parsing-state-machine-read-back surface; no LE31 v1 surface today has phone-order-handling. **Confidence: high** (0★/0⑂ + 98 KB tiny + MIT permissive + Python ✓ on-stack + 7-topic array including `claude + fastapi + llm + python + restaurant + state-machine + voice-agent` + IN-WINDOW BY BOTH FIELDS (2-day-old repo) + `175 tests` discipline visible in description = strongest v1 in-domain restaurant-vertical phone-order-agent cross-section pick of the 72-pass series).

**When** the LE31 owner wants to handle phone orders for the restaurant, **the owner wants to** see a working Python + FastAPI + state-machine-enforced-read-back + Claude-Haiku-parsing implementation that demonstrates the *bilingual-AI-phone-order-agent + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests* discipline, **but struggles because** the existing v1 `audit_logs + StockEntry + MenuItem` SQLModel tables are LE31-internal primitives with no phone-order-handling surface, **so that** the owner cannot see how a similar single-vertical phone-order-agent would be structured. The *bilingual-AI-phone-order-agent + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests* discipline IS the *phone-order-agent-as-audit-trail + deterministic-rules + LLM-parsing + state-machine + human-gate* charter §3.1 + §3.4 invariant applied to the *phone-order* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *bilingual-EN-Chinese-AI-phone-order-agent-for-family-Chinese-takeout + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests* sextuple-primitive as a candidate vocabulary for any future LE31 v1 phone-order-agent-with-rules-parsing-state-machine-read-back surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres mapping for each primitive (Claude-Haiku-parsing is borderline §3.4; the state-machine + deterministic-rules + read-back + 175-tests posture IS the §3.1 + §3.4 invariant applied to the *phone-order* dimension).
- Record the §3.1/§3.2/§3.3/§3.4/§3.6 alignment per `le31-conventions/SKILL.md`.
- Note the **7-topic array** = the most in-domain-restaurant-vertical-phone-order-agent-leveraging-claude-and-state-machine candidate of the 72-pass series.
- Note the *bilingual-EN-Chinese + family-Chinese-takeout + 175-tests* discipline = the strongest restaurant-vertical phone-order-agent *family-restaurant* analog for any future v1 PR that adopts the *phone-order-agent* posture.

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No Claude-Haiku-parsing integration; v1 uses deterministic-rule parsing only per charter §3.4 (`AI sandbox` rule: *no LLM in the order-parsing loop*; the *Claude-Haiku-parsing* posture IS the *AI-as-phone-order-parser* §3.4 candidate).
- No Twilio integration; v1 has no phone-line channel today.
- No bilingual menu support; v1 uses single-language FR/EN minimal-HTML/HTMX.

## Description

`kerryshi/china-garden-call-agent` is a **bilingual-EN-Chinese AI phone-order-agent for a family Chinese takeout** with the following properties:

- **Bilingual (EN/中文)** — phone orders accepted in both English and Chinese
- **Rules + Claude Haiku parsing** — deterministic rules + Claude Haiku LLM-parser for menu-item extraction
- **State machine enforces read-back** — the agent reads back the order to the caller before submitting
- **175 tests** — comprehensive test coverage for the state-machine + LLM-parsing + read-back discipline
- **Voice-agent stack** — Twilio + FastAPI + Python (per description + topics)
- **Single-family-takeout focus** — narrow vertical: family Chinese takeout (analog to LE31's single-restaurant focus)

Topics (verbatim, parent-verified): `claude + fastapi + llm + python + restaurant + state-machine + voice-agent` = **5/7 LE31 v1 restaurant-vertical phone-order-agent-vocabulary envelope**.

## Data model

The candidate vocabulary suggests these SQLModel tables (none built today; vocabulary-only):

```
PhoneOrder:
  id: int (primary key)
  caller_phone: str
  language: str  # 'en' or 'zh'
  raw_transcript: str  # Twilio call transcript
  parsed_items_json: str  # Claude Haiku-parsed items
  read_back_transcript: str  # the read-back delivered to caller
  state: str  # state-machine enum (DRAFTING → PARSING → READ_BACK → CONFIRMED → SUBMITTED → ARCHIVED)
  audit_log_ref: str  # reference to audit_logs row
  created_at: datetime
  confirmed_at: datetime
  archived_at: datetime

PhoneOrderLineItem:
  id: int (primary key)
  phone_order_id: int (foreign key)
  menu_item_name: str  # raw text from parser
  menu_item_id: int (nullable, foreign key to MenuItem if matched)
  quantity: int
  unit_price_eur: Decimal
  line_total_eur: Decimal
  parser_rule_id: str  # which rule matched this item

PhoneOrderStateMachine:
  id: int (primary key)
  phone_order_id: int (foreign key)
  from_state: str
  to_state: str
  actor: str  # 'claude-haiku' or 'operator' or 'caller'
  evidence: str  # the rule or read-back transcript that triggered the transition
  audit_log_ref: str
  created_at: datetime
```

## Implementation steps

If the trigger condition (v1 phone-order-agent surface window opens) is met:

1. Read the active feature file in full
2. Confirm `kerryshi/china-garden-call-agent` is still in-window (pushed within last 7 days from trigger date)
3. Set up Twilio voice webhook endpoint
4. Implement `PhoneOrder + PhoneOrderLineItem + PhoneOrderStateMachine` SQLModel tables
5. Implement the deterministic-rules + Claude-Haiku-parsing pipeline (with charter-§3.4-review-approved Claude-Haiku usage)
6. Implement the state-machine (DRAFTING → PARSING → READ_BACK → CONFIRMED → SUBMITTED → ARCHIVED)
7. Implement the read-back-Twilio-TTS discipline (every call-back must read back the order to the caller before submitting)
8. Write 175+ tests covering state-machine transitions + parsing edge cases + read-back failures + bilingual menu items
9. Run the v1 test suite + the new phone-order test suite
10. Surface any test failures to the owner

## Telegram interaction if any

The phone-order-agent is *not* a Telegram-bot surface; it is a Twilio-voice surface. **However**, the read-back state-machine SHOULD send a Telegram-message to the LE31 owner alerting them to the confirmed phone-order (so the operator can see what was ordered + the read-back transcript). This Telegram-message is operator-tooling, not customer-facing AI.

## Dependencies

- Twilio API (for phone line + TwiML voice webhook)
- FastAPI (already on-stack ✓ per LE31 v1)
- Claude Haiku (borderline §3.4; explicit charter-§3.4-review required)
- Pydantic (already on-stack ✓ per LE31 v1)
- state-machine library (XState or python-statemachine)

## Open questions

1. Does the Claude-Haiku-parsing posture comply with charter §3.4 (`AI sandbox` rule: no LLM in the order-parsing loop)? **Answer: borderline §3.4** — the *Claude-Haiku-parsing* posture IS the *AI-as-order-parser* §3.4 candidate; the *state-machine-enforces-read-back + 175-tests + deterministic-rules* posture IS the *non-AI-fallback + human-gate + observable-evidence* §3.4 invariant — but explicit charter-§3.4-review required before any v1 PR that adopts this.
2. Does the Twilio-voice channel respect the LE31 owner-only-data-pipeline? **Answer: yes** — Twilio stores call transcripts; the LE31 v1 audit-trail surface IS the *append-only-audit-log-as-evidence* charter §3.3 invariant.
3. Does the bilingual-EN-Chinese menu support breach charter §3.7 privacy? **Answer: no** — the language field is a single `language: str` ('en' or 'zh'); no PII beyond `caller_phone` (which is the Twilio-provided caller-ID, scoped per Twilio ToS).

## Why this matters

The **bilingual-EN-Chinese-AI-phone-order-agent-for-family-Chinese-takeout + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests** discipline is the canonical v1 restaurant-vertical phone-order-agent-vocabulary. LE31 v1 today is server-side + Postgres + FastAPI + cook-Telegram-bot + minimal-HTML/HTMX waiter-UI + append-only StockEntry; the v1 has *no phone-order-agent surface* (the LE31 owner has no way to handle phone orders; the *bilingual-AI-phone-order-agent + rules + Claude-Haiku-parsing + state-machine-enforces-read-back + 175-tests* discipline IS the canonical v1 restaurant-vertical phone-order-agent-vocabulary that would let a future v1 PR add a *phone-order-agent-with-rules-parsing-state-machine-read-back + 175 tests* surface that handles the phone-order line with deterministic rules + LLM-parsing + operator-read-back enforcement). The Python + 7-topic + 0★/0⑨ stack is **§3.1 + §3.2 ON-PATTERN** for LE31; the *rules + Claude-Haiku-parsing + state-machine-enforces-read-back* discipline IS stack-agnostic; the cross-section vocabulary is informative, not a v1-build trigger.

## Charter compatibility

- **§3.1** (explicit-state-transitions) ✓ — the *state-machine-enforces-read-back* posture IS the §3.1 *explicit-state-transition* invariant applied to the *phone-order* dimension.
- **§3.2** (privacy, counts-not-identity) ✓ — only `caller_phone` stored (Twilio-provided caller-ID, not customer identity); no PII beyond Twilio ToS scoping.
- **§3.3** (audit-log-immutability) ✓ — every state-transition writes to `audit_logs` via the standard LE31 audit-pipeline.
- **§3.4** (AI sandbox, observable evidence, non-AI fallback) **RIPGL_REVIEW REQUIRED** — the *Claude-Haiku-parsing* posture IS the §3.4 *AI-as-order-parser* candidate; the *state-machine-enforces-read-back + deterministic-rules + 175-tests* posture IS the *non-AI-fallback + observable-evidence + human-gate* §3.4 invariant. Explicit charter-§3.4-review needed before any v1 PR that adopts the *AI-phone-order-agent* posture with a customer-facing AI on the phone line.
- **§3.5** (EUR money discipline) ✓ — `unit_price_eur + line_total_eur` use `Decimal` per charter §3.6.
- **§3.6** (Paris timezone) ✓ — `created_at + confirmed_at + archived_at` are timezone-aware datetimes (Europe/Paris).
- **§3.7** (privacy) ✓ — only caller-ID stored, scoped per Twilio ToS.
