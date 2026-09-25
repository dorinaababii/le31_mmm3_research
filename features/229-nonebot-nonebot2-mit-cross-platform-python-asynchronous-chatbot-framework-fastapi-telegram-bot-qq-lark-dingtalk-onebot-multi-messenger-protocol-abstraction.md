# Feature 229 — nonebot-nonebot2-mit-cross-platform-python-asynchronous-chatbot-framework-fastapi-telegram-bot-qq-lark-dingtalk-onebot-multi-messenger-protocol-abstraction (defer)

> **NEW observation (2026-09-25).** Documents in-window GitHub Search `topic:telegram-bot+language:python` query result: `nonebot/nonebot2` (**MIT ✓**, **7722★/661⑂** = the **highest-star-count cross-platform Python chatbot framework candidate of the 57-pass brainstorm series**; 16× higher star count than feature 222 `donbarbos/telegram-bot-template`'s 476★; parent-direct-GET confirms; subagent scored stars=`None` from search-result JSON), Python, **pushed 2026-09-22T07:59:12Z** (in-window by `pushed_at` only — *3 days before fetch time*), **created 2020-08-23T03:02:18Z** (~5.5-year-old continuously-maintained repo with in-window `pushed_at` — the **longest-maintained cross-platform Python chatbot framework** of the 57-pass series; `created_at` is OUT-OF-WINDOW by ~5.5 years), **14.5 KB** modest repo, `default_branch=master`, archived=`False`). **14 topics** (verbatim from raw JSON): `bot`, `chatbot`, `cqhttp`, `dingtalk-robot`, `fastapi`, `lark-bot`, `mirai-bot`, `nonebot`, `nonebot2`, `onebot`, `python`, `qq`, `qq-guild`, `telegram-bot`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-25): *"跨平台 Python 异步聊天机器人框架 / Asynchronous multi-platform chatbot framework written in Python"*. The **cross-platform + async + Python + chatbot-framework + FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + cqhttp + mirai + multi-messenger-protocol-abstraction** decuple primitive. Bucket: **v2 cross-platform-messenger-framework-reference (parking-lot, future-second-messenger-surface-vocabulary-reference)** — watch-list entry, zero build time today.

## Goal

Retain the **cross-platform + async + Python + chatbot-framework + FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + cqhttp + mirai + multi-messenger-protocol-abstraction** decuple-primitive as a persistent cross-section reference for any future LE31 v2 expansion that introduces a second messenger surface (Discord/Slack/QQ/Lark/DingTalk) or a multi-messenger-protocol-abstraction layer. The artifact is the persistent cross-section reference + the 13 named architectural primitives. No code today (MIT license permits future code reuse; vocabulary-only artifact today; 14.5 KB modest-repo size limits source-code inspection depth — the *vocabulary* is high-value, the *code* is reference-only).

## Scope

**In scope (defer artifact):**
- A written record of the **cross-platform + async + Python + chatbot-framework** discipline: the *cross-platform-async-Python-chatbot-framework* primitive (LE31 v1 today uses aiogram per charter §3.2; the *cross-platform-chatbot-framework* discipline IS the *abstract-over-multiple-messenger-platform-protocols* posture).
- A written record of the **FastAPI** discipline: the *FastAPI-as-chatbot-framework-backend* primitive (nonebot2 uses FastAPI as the backend HTTP server; the *FastAPI-as-chatbot-framework-backend* discipline IS the *FastAPI-as-the-application-server* posture).
- A written record of the **Telegram-bot** discipline: the *Telegram-bot-framework* primitive (LE31 v1 uses aiogram which is Telegram-specific; the *Telegram-bot-framework* discipline IS the *Telegram-messenger-protocol-implementation* posture).
- A written record of the **QQ + Lark + DingTalk + OneBot + cqhttp + mirai** discipline: the *multi-messenger-protocol-abstraction* primitive (nonebot2 abstracts over multiple messenger-platform-protocols: OneBot = QQ, cqhttp = CoolQ HTTP API, mirai-bot = mirai QQ, Lark = Feishu, DingTalk = DingTalk enterprise messenger; the *multi-messenger-protocol-abstraction* discipline IS the *cross-platform-messenger-abstraction* posture).
- A decision record: today's verdict is `defer` because LE31 v1 is not built today and v2 cross-platform-messenger surface expansion is not in scope; the cross-section reference is informative, not a build-trigger.
- A cross-section reference with the prior v2 Telegram-bot-framework cluster: features 48 (`pipecat-voice-watch`), 116 (`aiogram-3-31-0-stable-track`), 120 (`geminka-agent-aiogram-3-telegram-premium-markup-pattern`), 149 (`personal-agent-blueprint-telegram-chokepoint-architecture-pattern`), 222 (`donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template`). The *transferable insight* is the **cross-platform-async-Python-chatbot-framework + FastAPI + Telegram-bot + multi-messenger-protocol-abstraction** decuple-primitive.

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
- Any second messenger surface in v1 (LE31 v1 is aiogram-Telegram-only per charter §3.2; Discord/Slack/QQ/Lark/DingTalk is a v2 expansion candidate).
- Any chatbot-framework replacement in v1 (LE31 v1 uses aiogram per charter §3.2; nonebot2 is the vocabulary reference for *cross-platform-messenger-protocol-abstraction*, NOT for *chatbot-framework replacement*).
- Any multi-messenger-protocol-abstraction layer in v1 (LE31 v1 has 1 messenger-protocol-implementation today; multi-protocol-abstraction is a v2 expansion candidate).

## Description

The pick is **nonebot/nonebot2** — a Python + async + FastAPI + cross-platform + chatbot-framework that abstracts over multiple messenger-platform-protocols (Telegram + QQ + Lark + DingTalk + OneBot + cqhttp + mirai). Charter §3.4 NOT triggered because nonebot2 is a chatbot-framework for developers/staff, NOT customer-facing-AI. The *chatbot-framework* is a tool for the *developer/staff*, not a tool that interacts with restaurant diners. The artifact is the persistent cross-section reference for the 13 named primitives.

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v2 surface that adopts any of the 13 primitives would extend the LE31 v1 data model with appropriate new tables (e.g., a `MessengerPlatform` table for the multi-messenger-protocol-abstraction primitive; a `BotAdapter` table for the per-platform-adapter discipline; a `CrossPlatformMessage` table for the cross-platform-message-routing discipline). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v2 PR is triggered by the trigger condition below, the implementation would:
1. Read the nonebot2 README at https://github.com/nonebot/nonebot2 for the *cross-platform + async + Python + chatbot-framework + FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + cqhttp + mirai + multi-messenger-protocol-abstraction* architecture pattern.
2. Cross-reference with LE31 v1's *aiogram-Telegram-only* posture to identify the *delta* (the *delta* = nonebot2 abstracts over multiple messenger-platform-protocols; LE31 v1 is single-platform).
3. Apply charter §3.1 surface-expansion review to the *delta* (any new v2 surface requires explicit owner/charter sign-off; the second-messenger-surface delta is the most charter-sensitive because of charter §3.2 *Telegram-only* baseline).
4. Implement the surface with the LE31 v1 + FastAPI + SQLModel + aiogram stack; the nonebot2 reference is the *vocabulary* for *multi-messenger-protocol-abstraction*, NOT for *chatbot-framework replacement*.

## Telegram interaction

Zero new Telegram interaction today. Future v2 PR that adopts the *cross-platform-messenger-protocol-abstraction* primitive would extend the existing aiogram-bot (cook-bot per charter §3.1) with a *multi-protocol-adapter* layer that allows the same operator-tooling to be deployed on multiple messenger-platforms (Telegram + Discord + Slack + QQ + Lark + DingTalk). The *multi-protocol-adapter* discipline is *operator-tooling* (developer/operator deploys the same chat-interface on multiple platforms), NOT customer-facing-AI; charter §3.4 is NOT triggered.

## Dependencies

- LE31 charter §3.1 surface-expansion review (for any v2 surface adoption).
- LE31 charter §3.2 surface-expansion review (for any second-messenger-surface adoption; the *Telegram-only* baseline is the charter §3.2 known-context).
- LE31 charter §3.4 operator-tooling boundary (for any chatbot-framework adoption; nonebot2's *developer/staff-tooling* posture confirms NOT triggered today).
- LE31 charter §3.2 license-compatible (MIT permissive; future code adoption is possible).
- Features 48 (`pipecat-voice-watch`), 116 (`aiogram-3-31-0-stable-track`), 120 (`geminka-agent-aiogram-3-telegram-premium-markup-pattern`), 149 (`personal-agent-blueprint-telegram-chokepoint-architecture-pattern`), 222 (`donbarbos-telegram-bot-template-mit-aiogram-postgresql-docker-poetry-pydantic-sqlalchemy-redis-ruff-uv-admin-panel-production-template`).
- Cross-section reference `nonebot/nonebot2` at https://github.com/nonebot/nonebot2 (MIT, 7722★/661⑂, Python, FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + cqhttp + mirai + multi-messenger-protocol-abstraction).

## Open questions

- Will LE31 v2 ever introduce a second messenger surface (Discord/Slack/QQ/Lark/DingTalk)? If yes, nonebot2 is the vocabulary reference.
- Will LE31 v2 ever introduce a multi-messenger-protocol-abstraction layer? If yes, nonebot2 is the vocabulary reference.
- Will LE31 v2 ever adopt a cross-platform-chatbot-framework reference (NOT replacement)? If yes, nonebot2 is the vocabulary reference.
- Will LE31 v2 ever introduce a per-platform-adapter discipline (Telegram-adapter + Discord-adapter + Slack-adapter + QQ-adapter + Lark-adapter + DingTalk-adapter)? If yes, nonebot2 is the vocabulary reference.
- Will LE31 v2 ever introduce a cross-platform-message-routing discipline (one-message-multiple-platforms)? If yes, nonebot2 is the vocabulary reference.
- Will LE31 v2 ever introduce a FastAPI-as-chatbot-framework-backend posture? (LE31 v1 already uses FastAPI as the backend; this is a vocabulary-confirmation, not a build-trigger.)
- The 7722★/661⑂ is explicitly NOT offered as evidence of *LE31 needing chatbot-framework replacement*; the 7722★/661⑂ is for the *chatbot-framework domain*, not for the *multi-messenger-protocol-abstraction* primitive. The transferable item is the *technique* (OneBot + cqhttp + mirai + Lark + DingTalk + Telegram multi-protocol-abstraction), not the *chatbot-framework* itself.

## Why this matters

The 13 primitives in nonebot2 are the **canonical v2 cross-platform-messenger-framework vocabulary** that LE31 v1's `aiogram-cook-bot` (feature 48 / charter §3.1) and v2's future second-messenger surface would inherit. Specifically: (i) **cross-platform + async + Python + chatbot-framework** (the *cross-platform-async-Python-chatbot-framework* discipline) is the *abstract-over-multiple-messenger-platform-protocols* posture; (ii) **FastAPI-as-chatbot-framework-backend** is the *FastAPI-as-the-application-server* posture; (iii) **Telegram-bot** is the *Telegram-messenger-protocol-implementation* posture; (iv) **QQ + Lark + DingTalk + OneBot + cqhttp + mirai** is the *multi-messenger-protocol-abstraction* discipline; (v) **multi-messenger-protocol-abstraction** is the *cross-platform-messenger-abstraction* posture. When v2 introduces any of these 5 primitives, nonebot2 is the vocabulary reference. **HONEST DISCLOSURE**: nonebot2's 7722★ is for the *chatbot-framework domain*, not for the *multi-messenger-protocol-abstraction* primitive; the 7722★ is explicitly NOT offered as evidence of LE31's need for the chatbot-framework replacement.