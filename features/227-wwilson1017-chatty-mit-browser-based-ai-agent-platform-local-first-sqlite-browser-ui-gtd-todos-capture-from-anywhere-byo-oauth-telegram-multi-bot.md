# Feature 227 — wwilson1017-chatty-mit-browser-based-ai-agent-platform-local-first-sqlite-browser-ui-gtd-todos-capture-from-anywhere-byo-oauth-telegram-multi-bot (defer)

> **NEW observation (2026-09-25).** Documents in-window GitHub Search `topic:small-business+language:python` query result: `wwilson1017/chatty` (**MIT ✓**, **9★/5⑂** (parent-direct-GET 2026-09-25 confirms; subagent scored stars=`None` from search-result JSON), Python, **pushed 2026-09-20T17:07:14Z** (in-window by `pushed_at` only — *4 days before fetch time*), **created 2026-03-24T14:07:21Z** (~6-month-old repo with in-window `pushed_at` — `created_at` is OUT-OF-WINDOW by ~5 months), **5.8 KB** small repo, `default_branch=master`, archived=`False`). **10 topics** (verbatim from raw JSON): `ai`, `ai-agent`, `anthropic`, `chatbot`, `fastapi`, `gemini`, `open-source`, `openai`, `react`, `small-business`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-25): *"A free, open-source browser-based AI agent platform; great for personal agents, professional work agents and small business owners. Agent teams ready. Local-first or deployed. Odoo, Quickbooks Online, Google Workspace and BambooHR connection built in. Agent curated CRM system included."* README confirms (parent-fetched `/opt/data/le31-brainstorm-2026-09-25/verify/readme_wwilson1017_chatty.md`): **browser-based UI** + **multi-agent** + **multi-provider AI** (Anthropic/OpenAI/Gemini/Ollama/Together) + **heartbeat scheduled background tasks** + **reminders** + **memory with semantic vector search + temporal fact tracking** + **meeting recording with real-time chunked transcription + agent coach** + **playbooks & learning loop** + **commitments (inferred follow-ups)** + **usage & cost dashboard** + **GTD todos (Inbox/Next Actions/Projects/Waiting/Someday/Done/Review)** + **capture-from-anywhere (`/capture` no-login page + Telegram `capture buy milk` deterministic-intercept + agent `todo_*` tools + UI)** + **integrations (Gmail, Google Calendar, Google Drive, QuickBooks Online, Todoist, Telegram multiple bots, Odoo, BambooHR, Paperclip, CRM Lite)** + **agent orchestration via Paperclip** + **file uploads** + **2FA (TOTP)** + **brandable** + **BYO OAuth for Google/QuickBooks** + **Local-first SQLite** + **one-click deploy to Railway**. **The only in-window 2026 *small-business AI-agent-platform with LE31-shape posture (Local-first SQLite + browser-UI + GTD todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration)* candidate of the 57-pass brainstorm series**. Bucket: **v2 owner-assist (parking-lot, future-operator-tooling-vocabulary-reference)** — watch-list entry, zero build time today.

## Goal

Retain the **AI-agent-platform-for-small-business + Local-first SQLite + browser-UI + GTD todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration** octuple-primitive as a persistent cross-section reference for any future LE31 v2 expansion that introduces an AI-assisted owner-facing surface. The artifact is the persistent cross-section reference + the eight named architectural primitives. No code today (MIT license permits future code reuse; vocabulary-only artifact today; 5.8 KB small-repo size limits source-code inspection depth — the *vocabulary* is high-value, the *code* is reference-only).

## Scope

**In scope (defer artifact):**
- A written record of the **AI-agent-platform-for-small-business** discipline: the *personal/professional/small-business-AI-agent* primitive (the *AI-agent-platform-for-business-owner* discipline IS the *operator-assist-by-AI* pattern).
- A written record of the **Local-first SQLite** discipline: the *SQLite-as-deployment-DB* primitive (LE31 v1 uses SQLite-for-dev per charter §3.2 known-conflicts note; the *Local-first* discipline IS the *on-device-data-sovereignty* posture; the *SQLite-as-deployment-DB* choice is documented as a known-conflict that LE31 v1 currently navigates with dual-interpretation).
- A written record of the **browser-UI** discipline: the *non-Telegram-non-command-line operator surface* primitive (LE31 v1's waiter web UI is browser-based per charter §3.1; the *browser-UI* discipline IS the *no-installation-required operator surface* posture).
- A written record of the **GTD todos** discipline: the *Getting-Things-Done-todo-system* primitive (the *GTD* discipline IS the *Inbox/Next Actions/Projects/Waiting/Someday/Done/Review* pattern — a *single-owner-task-management* system).
- A written record of the **capture-from-anywhere** discipline: the *multi-surface-capture* primitive (chatty's *`/capture` no-login page + Telegram `capture buy milk` deterministic-intercept + agent `todo_*` tools + UI* combination IS the *capture-from-anywhere* pattern; LE31 v1 has feature 29 `owner-no-account-live-floor-link` as a partial implementation; chatty names the *full* capture-from-anywhere vocabulary).
- A written record of the **BYO-OAuth** discipline: the *bring-your-own-OAuth-credentials* primitive (the *BYO-OAuth* discipline IS the *vendor-agnostic-OAuth* posture — operator brings their own Google/QuickBooks OAuth credentials for full control).
- A written record of the **Telegram-multi-bot** discipline: the *multiple-bots-per-deployment* primitive (the *Telegram-multi-bot* discipline IS the *one-operator-multiple-roles* pattern — e.g., one bot for the cook, one bot for the manager, one bot for the owner, all running in the same deployment).
- A written record of the **multi-integration** discipline: the *integrations-as-built-in* primitive (chatty's *Gmail + Google Calendar + Google Drive + QuickBooks Online + Todoist + Telegram multiple bots + Odoo + BambooHR + Paperclip + CRM Lite* combination IS the *integrations-as-built-in* posture).
- A decision record: today's verdict is `defer` because LE31 v1 is not built today and v2 surface expansion is not in scope; the cross-section reference is informative, not a build-trigger.
- A cross-section reference with the prior v2 AI-but-operator-only cluster: features 48 (`pipecat-voice-watch`), 86 (`salestrics-mcp-native-crm-watch`), 119 (`Mormolykos-epcore-mit-deterministic-licensing-kernel`), 149 (`personal-agent-blueprint-telegram-chokepoint-architecture-pattern`), 208 (`njbbaer-simulacra-telegram-llm-template-based-context-system`). The *transferable insight* is the **AI-agent-platform-for-small-business + Local-first SQLite + browser-UI + GTD todos + capture-from-anywhere + BYO-OAuth + Telegram-multi-bot + multi-integration** octuple-primitive.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2 horizontal-expansion surface in v2 (charter §3.1 + §3.2 invariant: v2 surface expansion is the next boundary; this is a vocabulary reference, not a v2 expansion trigger).
- Any third-party integration in v1 (LE31 v1 today has zero third-party OAuth; multi-integration is a v2 expansion candidate).
- Any Telegram-multi-bot deployment in v1 (LE31 v1 has 1 bot per charter §3.1; multi-bot is a v2 expansion candidate).
- Any GTD-todo-system in v1 (LE31 v1 has feature 69 `owner-no-account-shift-recap-link` but no GTD-todo-system; GTD is a v2 expansion candidate).
- Any Local-first SQLite deployment change (LE31 v1 uses SQLite-for-dev per charter §3.2; chatty's *Local-first SQLite + browser-UI + capture-from-anywhere + GTD-todos + multi-integration* posture is *structurally identical* to LE31 v1's deployment posture, so no change needed).

## Description

The pick is **wwilson1017/chatty** — a Python + FastAPI + browser-UI + Local-first SQLite + GTD-todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration AI-agent platform for small business owners. Charter §3.4 NOT triggered because chatty is operator/business-owner-facing, NOT customer-facing-AI. The *AI-agent-platform* is a tool for the *owner/staff*, not a tool that interacts with restaurant diners. The *integrations* (Gmail/QuickBooks/BambooHR) are operator-side, not customer-side. The artifact is the persistent cross-section reference for the 8 named primitives.

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v2 surface that adopts any of the 8 primitives would extend the LE31 v1 data model with appropriate new tables (e.g., a `GTDTodo` table for the GTD discipline; an `Integration` table for the multi-integration discipline; a `OAuthCredential` table for the BYO-OAuth discipline; a `BotInstance` table for the Telegram-multi-bot discipline). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v2 PR is triggered by the trigger condition below, the implementation would:
1. Read the chatty README at `/opt/data/le31-brainstorm-2026-09-25/verify/readme_wwilson1017_chatty.md` for the *Local-first SQLite + browser-UI + GTD todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration* architecture pattern.
2. Cross-reference with LE31 v1's *SQLite-for-dev + browser-UI + owner-no-account-live-floor-link (feature 29) + 1-bot-per-deployment* posture to identify the *delta* (the *delta* = chatty has 5 primitives that LE31 v1 doesn't have: GTD-todos, BYO-OAuth, Telegram-multi-bot, multi-integration, AI-agent-platform).
3. Apply charter §3.1 surface-expansion review to the *delta* (any new v2 surface requires explicit owner/charter sign-off; the AI-agent-platform delta is the most charter-sensitive because of charter §3.4 operator-tooling boundary).
4. Implement the surface with the LE31 v1 + FastAPI + SQLModel + aiogram stack; the chatty reference is the *vocabulary*, not the *code*.

## Telegram interaction

Zero new Telegram interaction today. Future v2 PR that adopts the *Telegram-multi-bot* primitive would extend the existing aiogram-bot (cook-bot per charter §3.1) with a second bot (e.g., owner-bot for owner-recap). The chatty *capture-from-anywhere* + *Telegram-multi-bot* + *deterministic-intercept* pattern is the load-bearing finding: chatty's *"Message your bot `capture buy milk` — a deterministic intercept logs it instantly with zero AI processing, so it's fast and costs nothing"* is the *deterministic-Telegram-capture* primitive (the *capture-command* is *intercepted-deterministic* before any AI processing; this maps 1:1 onto LE31 v1's charter §3.4 *operator-must-confirm* posture).

## Dependencies

- LE31 charter §3.1 surface-expansion review (for any v2 surface adoption).
- LE31 charter §3.4 operator-tooling boundary (for any AI-surface adoption; chatty's *operator/business-owner-facing* posture confirms NOT triggered today).
- LE31 charter §3.2 license-compatible (MIT permissive; future code adoption is possible).
- Features 23 (`sse-cook-channel`), 29 (`owner-no-account-live-floor-link`), 48 (`pipecat-voice-watch`), 69 (`owner-no-account-shift-recap-link`), 86 (`salestrics-mcp-native-crm-watch`), 116 (`aiogram-3-31-0-stable-track`), 119 (`Mormolykos-epcore-mit-deterministic-licensing-kernel`), 149 (`personal-agent-blueprint-telegram-chokepoint-architecture-pattern`), 208 (`njbbaer-simulacra-telegram-llm-template-based-context-system`).
- Cross-section reference `wwilson1017/chatty` at https://github.com/wwilson1017/chatty (MIT, 9★/5⑂, Python, FastAPI + Local-first SQLite + browser-UI + GTD-todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration).

## Open questions

- Will LE31 v2 ever introduce a third-party-integration layer (Gmail/QuickBooks/BambooHR/Todoist/Odoo)? If yes, chatty is the vocabulary reference.
- Will LE31 v2 ever introduce a GTD-todo-system? If yes, chatty is the vocabulary reference.
- Will LE31 v2 ever introduce a BYO-OAuth layer? If yes, chatty is the vocabulary reference.
- Will LE31 v2 ever introduce a Telegram-multi-bot deployment (cook-bot + manager-bot + owner-bot)? If yes, chatty is the vocabulary reference.
- Will LE31 v2 ever introduce an AI-assisted owner-facing surface (charter §3.4 operator-tooling boundary)? If yes, chatty is the vocabulary reference.
- Will LE31 v2 ever adopt a *Local-first SQLite + browser-UI + capture-from-anywhere + GTD-todos + multi-integration* posture? (LE31 v1 already adopts *SQLite-for-dev + browser-UI + owner-no-account-live-floor-link* as partial implementation; the *delta* is GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration + AI-agent-platform.)
- The 9★/5⑂ is explicitly NOT offered as evidence of *LE31 needing the AI-agent-platform primitive*; the 9★/5⑂ is for the *AI-agent-platform-for-small-business* domain, not for the *Local-first SQLite + browser-UI + GTD-todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration* primitive.

## Why this matters

The 8 primitives in chatty are the **5-missing-primitive checklist** that LE31 v1 today does NOT have: (i) **AI-agent-platform surface** (charter §3.4 conditional; not a build-need today), (ii) **multi-integration layer** (Gmail/QuickBooks/BambooHR/Todoist/Odoo = the *integrations-as-built-in* discipline), (iii) **Telegram-multi-bot** (LE31 v1 has 1 bot per charter §3.1; multi-bot = future-v2), (iv) **BYO-OAuth** (LE31 v1 today has zero third-party OAuth; BYO-OAuth = future-v2), (v) **GTD-todo-system** (LE31 v1 has feature 69 owner-no-account-shift-recap-link but no GTD-todo-system). **LE31 v1 today covers 4/8 of these primitives** (SQLite ✓, browser-UI ✓, capture-from-anywhere = feature 29, GTD-todo-system = NOT-YET); chatty names the 5-missing-primitive checklist. When v2 introduces any of these 5 missing primitives, chatty is the vocabulary reference. **HONEST DISCLOSURE**: chatty's 9★/5⑂ is for the *AI-agent-platform-for-small-business* domain, not for the 8 primitives; the 9★/5⑂ is explicitly NOT offered as evidence of LE31's need for the AI-agent-platform primitive.