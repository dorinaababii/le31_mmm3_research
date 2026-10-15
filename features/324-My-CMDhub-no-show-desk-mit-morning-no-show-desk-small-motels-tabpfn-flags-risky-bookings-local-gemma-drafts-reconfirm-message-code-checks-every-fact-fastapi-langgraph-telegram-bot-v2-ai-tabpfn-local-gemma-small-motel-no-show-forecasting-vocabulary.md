# Feature 324 — `My-CMDhub/no-show-desk` v2-AI TabPFN+local-Gemma+small-motel-no-show-forecasting-vocabulary (defer)

> **NEW observation (2026-10-15).** Documents in-window GitHub repo `My-CMDhub/no-show-desk` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, **270 KB modest**, language Python ✓ ON-STACK + FastAPI + LangGraph + TabPFN + local Gemma + Telegram-bot, **pushed 2026-10-14T07:50:41Z AND created 2026-10-14T07:36:00Z = IN-WINDOW BY BOTH FIELDS**, parent-direct-GitHub-API-GET-verified 2026-10-15 from `/tmp/le31-brainstorm-2026-10-15/verify/ghverify__parent_My-CMDhub_no-show-desk.json` — note: subagent initially reported `pushed_at` as `2026-10-14T07:50:54Z`, parent-caught 13-second discrepancy and corrected to `07:50:41Z`). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-15): *"Find out which guests won't turn up, days before they don't. A morning no-show desk for small motels: TabPFN flags risky bookings, local Gemma drafts a reconfirm message, code checks every fact."* Topics (verbatim, parent-verified): `fastapi`, `gemma`, `hospitality`, `langgraph`, `local-llm`, `no-show`, `tabpfn`, `tabular-data`, `telegram-bot`, `webgpu` = **10 topics including `fastapi + hospitality + telegram-bot` (the v2-AI hospitality-cross-section match) + `local-llm + tabpfn + langgraph` (the v2-AI small-data + local-LLM + agent-harness triple) + `gemma + no-show + tabular-data + webgpu` (the v2-AI tabular-prediction + on-device-LLM + WebGPU primitives)** = **canonical v2-AI TabPFN+local-Gemma+small-motel-no-show-forecasting-vocabulary of the 77-pass brainstorm series**. Bucket: **v2-AI (parking-lot, vocabulary reference)** — Pick B of Daily Brainstorm 2026-10-15. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **TabPFN-flags-risky-bookings + local-Gemma-drafts-reconfirm-message + code-checks-every-fact + FastAPI + Telegram-bot-glue** quintuple-primitive as a persistent cross-section reference for the LE31 v2-AI *operator-side predictive-forecasting-with-fact-verification* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (1-day-old repo with first in-window push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **TabPFN-flags-risky-bookings + local-Gemma-drafts-reconfirm-message + code-checks-every-fact** triple-discipline: (1) *TabPFN* is a transformer-based ML model designed for small tabular datasets — it flags which bookings are likely to no-show based on historical no-show patterns; (2) *Local Gemma* is a small open LLM that drafts a reconfirm message for the flagged bookings — local inference keeps PII off-cloud; (3) *Code checks every fact* is a deterministic-fact-verification layer that verifies every fact in the LLM-drafted message against the booking database before the message is sent. This is the §3.4 + §3.7 deterministic-rule-only + local-LLM + fact-verification charter invariant applied to the *small-business-no-show-forecasting* dimension
- A written record of the **FastAPI + LangGraph + Telegram-bot-glue** stack-shape: this is **3 of 4 LE31 backend stack primitives matched** (Python + FastAPI + LangGraph is on-stack; Telegram-bot is portable to LE31's aiogram v3 framework; local-LLM is the §3.7 PII-on-device invariant); the **Python + FastAPI + LangGraph + Telegram-bot** infrastructure is the LE31-stack-match primitive
- A written record of the **operator-side predictive-forecasting-with-fact-verification** operator-surface-shape: every morning, the operator opens the *no-show-desk* view, sees the flagged bookings for today/tomorrow, sees the auto-drafted reconfirm messages (with fact-checkmarks showing which facts were verified against the database), reviews each message, clicks to send or edit. Sister-shape to features 232 (lpalbou/AbstractGateway — durable AI control plane) + 287 (noise01/endoxa — governed beliefs for LLM agents) + 288 (pete-builds/mcp-nixreview — advisory NixOS change-review with CVE attestation gate) + 289 (shivamk01here/LedgerLoop — Python runtime for financial AI agents with idempotent exactly-once execution)
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with no community traction signal; (2) the stack-shape match is the value, not the code (LE31 v1 has no AI agent; v2-AI surface is OFF v1 charter); (3) the *demand-signal* is the value, not the code-adoption opportunity

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3) or owner daily-recap
- Any change to LE31 v1's `audit_logs` schema (the v2-AI surface would extend `audit_logs` with a *fact-verification-ledger* table on first v2 PR)
- Adoption of the `no-show-desk` codebase (1-day-old single-maintainer repo with no observed production usage; total size 270 KB is small but unproven)
- Cross-pollination with the v2-AI approval primitive in v1 (LE31 v1 has no AI agent)

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "the *operator-side predictive-forecasting-with-fact-verification* surface that predicts which events will happen (low-stock / no-show / expiry), drafts a reconfirm message (local LLM, PII-off-cloud), and verifies every fact in the message before sending (deterministic-rule-on-the-database)" (e.g., a v2-AI surface that introduces an AI-assisted owner-side workflow like "the no-show-desk surface predicts which no-show bookings are likely for today's check-ins, the AI assistant drafts a reconfirm message for each flagged booking, the message-facts are verified against the booking database, the operator reviews and sends"), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "predictive-forecasting + local-LLM + fact-verification + Telegram-bot" is a real demand signal*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `tabpfn + gemma + local-llm + langgraph + telegram-bot + hospitality`)
- **Confidence**: medium-high for the vocabulary match (the verbatim description names the 5-primitive set + the tech-stack); low for transferability (LE31 v1 has no AI agent; v2-AI surface is OFF v1 charter)
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no AI agent); the value is the *operator-side predictive-forecasting-with-fact-verification* vocabulary — when the first v2-AI PR that adds an AI agent surface lands, the `no-show-desk` pattern is a ready-made *named primitive*

## Description

GitHub `My-CMDhub/no-show-desk` (MIT, 0★/0⑂, Python + FastAPI + LangGraph + TabPFN + local Gemma + Telegram-bot, pushed 2026-10-14T07:50:41Z, created 2026-10-14T07:36:00Z = 1-day-old repo with both-window, 270 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-15): *"Find out which guests won't turn up, days before they don't. A morning no-show desk for small motels: TabPFN flags risky bookings, local Gemma drafts a reconfirm message, code checks every fact."*

The architectural primitive has five sub-primitives that map 1:1 onto the LE31 v2-AI *predictive-forecasting-with-fact-verification* surface:

1. **TabPFN flags risky bookings** — TabPFN (Transformer-based model for tabular data) flags which bookings in the system are likely to no-show based on historical patterns. The *TabPFN-as-small-data-ML-model* primitive maps 1:1 onto LE31's potential v2-AI surface that needs a *predictive-forecasting-on-historical-data* capability without training a custom model from scratch.
2. **Local Gemma drafts a reconfirm message** — A small open Gemma LLM running on-device drafts a reconfirm message for each flagged booking. The *local-LLM-as-edge-inference* primitive maps 1:1 onto LE31's §3.7 PII-on-device invariant (LE31 must not send diner PII to a remote cloud LLM).
3. **Code checks every fact** — Before sending any message, deterministic code verifies every fact in the LLM-drafted message against the booking database (booking ID, guest name, check-in date, room number, special requests). The *code-checks-every-fact* primitive maps 1:1 onto LE31's §3.4 fact-verification-before-action invariant (LE31 must not let an LLM trigger a real-world action without fact-verification).
4. **FastAPI + LangGraph** — Python backend with FastAPI + LangGraph as the agent harness. The *FastAPI + LangGraph* primitive maps 1:1 onto LE31's Python + FastAPI + SQLModel backend stack.
5. **Telegram-bot-glue** — The no-show-desk outputs are sent to the operator via a Telegram bot (the operator reviews + sends from the Telegram app). The *Telegram-bot-glue* primitive maps 1:1 onto LE31's aiogram v3 cook-bot (LE31 could extend the cook-bot to support operator-side no-show-review via a new bot command set).

**The 1:1 mapping onto LE31 surface:**

| `no-show-desk` primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| TabPFN flags risky bookings | (LE31 has no predictive-forecasting surface today) | v2-AI | **Not implemented** — v2-AI surface |
| Local Gemma drafts message | (LE31 has no LLM surface today) | v2-AI | **Not implemented** — v2-AI surface |
| Code checks every fact | (LE31 has no fact-verification surface today) | v2-AI | **Not implemented** — v2-AI surface |
| FastAPI + LangGraph | Python + FastAPI + SQLModel | §3.1 ✓ | **Implemented (v1)** — LangGraph is not yet integrated |
| Telegram-bot-glue | aiogram v3 cook-bot | §3.1 ✓ | **Implemented (v1)** — new bot command set for operator-side no-show review |

## Dependencies

- [05-payment-tip-reconciliation.md](../features/05-payment-tip-reconciliation.md) — the v2-AI surface would extend the audit_logs schema with a *fact-verification-ledger* table
- [260/261/286](../features/260-...) — the persistent v2-AI agent-orchestrator + chokepoint + human-gate + append-only-ledger cluster (features 232/287/288/289/296/299/300/301)

## Open questions

- How does the v2-AI surface integrate TabPFN with LE31's existing Postgres data without a separate ML training pipeline? (Answer: TabPFN is a small-data model; no training pipeline needed)
- How does the v2-AI surface keep PII on-device for the local-Gemma inference? (Answer: LE31 v2-AI surface must require local-LLM-only by charter; no cloud-LLM surface)
- How does the v2-AI surface verify LLM-generated message facts against the booking database? (Answer: deterministic code check before message send; the operator reviews in a /review-no-show Telegram command before send)

## Why this matters

The **TabPFN + local Gemma + LangGraph + small-motel-no-show-forecasting + Telegram-bot-glue + code-checks-every-fact** quintuple-primitive is a *stronger* v2-AI cross-section vocabulary than any of features 232/287/288/289 alone. The TabPFN discipline IS the §3.4 *small-data-ML-model-as-deterministic-prediction* invariant. The local-Gemma discipline IS the §3.4 *local-LLM-as-edge-inference* invariant + the §3.7 *PII-on-device* invariant. The code-checks-every-fact discipline IS the §3.4 *fact-verification-before-publish* invariant. The FastAPI + LangGraph ON-STACK posture aligns with §3.1. The Telegram-bot-glue posture IS portable to LE31's aiogram v3 framework. The 10 topics IS the **strongest v2-AI topic-diversity signal of the 77-pass brainstorm series**.

## Rollback path

This defer artifact is fully reversible:
- Delete the feature file: `rm /opt/data/le31_mmm3_research/features/324-My-CMDhub-no-show-desk-...md`
- Delete the HANDOFF: `rm /opt/data/le31_mmm3_research/specs/324-My-CMDhub-no-show-desk-...-HANDOFF.md`
- No code change was made today, so no rollback of code is required
- No database migration was made today, so no rollback of schema is required
- No pin change was made today (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1)
- The TabPFN + Gemma + LangGraph stack would add new pin entries on a future v2-AI PR; today no pins are added
