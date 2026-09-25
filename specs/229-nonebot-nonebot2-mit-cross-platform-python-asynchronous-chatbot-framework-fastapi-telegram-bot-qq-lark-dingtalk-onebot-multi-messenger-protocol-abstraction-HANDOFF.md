# 229 — nonebot/nonebot2 v2-cross-platform-messenger-framework-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 cross-platform-messenger-framework question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/229-nonebot-nonebot2-mit-cross-platform-python-asynchronous-chatbot-framework-fastapi-telegram-bot-qq-lark-dingtalk-onebot-multi-messenger-protocol-abstraction.md` (defer artifact; **no code today**).

Bucket: **v2 cross-platform-messenger-framework-reference (cross-platform + async + Python + chatbot-framework + FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + cqhttp + mirai + multi-messenger-protocol-abstraction, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a second messenger surface (Discord/Slack/QQ/Lark/DingTalk), a multi-messenger-protocol-abstraction layer, or a cross-platform-chatbot-framework reference (NOT replacement), what is the *cross-platform + async + Python + chatbot-framework + FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + multi-messenger-protocol-abstraction* vocabulary that preserves the existing v1 aiogram-Telegram-only posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 14.5 KB with 7722★/661⑂ + MIT permissive license + 14 topics + in-window-by-pushed_at-only + maintained-continuously-since-2020 is shipping the *cross-platform + async + Python + chatbot-framework + FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + multi-messenger-protocol-abstraction* primitive as the v2 cross-platform-messenger-framework discipline*, but struggles because *v1 has no documented multi-messenger-protocol-abstraction primitive in the charter*, so that *v2 can introduce the multi-messenger-protocol-abstraction vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no multi-messenger-protocol-abstraction trigger; the JTBD is primitive vocabulary extension + multi-messenger-protocol-abstraction documentation, not a build-need; **cross-section JTBD value is moderate-to-high** — the highest-star-count cross-platform Python chatbot framework candidate of the 57-pass brainstorm series = the *multi-messenger-protocol-abstraction* vocabulary reference, but the *chatbot-framework replacement* is off-pattern for LE31 v1 today because LE31 v1 uses aiogram per charter §3.2). |
| 2 | **Viability** | Maintainer can read 14.5 KB repo description + 14-topic vocabulary + cross-platform + async + Python + chatbot-framework + FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + cqhttp + mirai + multi-messenger-protocol-abstraction decuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *multi-messenger-protocol-abstraction* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + Telegram-only stack, not imported from the MIT-permissive code; LE31 v1 has no multi-messenger-protocol-abstraction surface today). Confidence: medium-to-high for the *multi-messenger-protocol-abstraction* vocabulary (7722★/661⑂ + MIT permissive license + 14 topics + in-window-by-pushed_at-only + maintained-continuously-since-2020 + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *cross-platform + async + Python + chatbot-framework + multi-messenger-protocol-abstraction* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-platform-messenger-abstraction dimension*; the *FastAPI + Telegram-bot* discipline IS the *FastAPI-as-application-server + Telegram-messenger-protocol-implementation* posture). Stack: FastAPI + SQLModel + PostgreSQL backend = on-pattern for v1 primitives (matches v1 charter §3.2 baseline); cross-platform = off-pattern for v1 (LE31 v1 is Telegram-only per charter §3.2); async = on-pattern for v1 (LE31 v1 uses asyncio via aiogram); Python + chatbot-framework = on-pattern for v1 (LE31 v1 uses aiogram = Python chatbot-framework); multi-messenger-protocol-abstraction = off-pattern for v1 (LE31 v1 has 1 messenger-protocol-implementation today); QQ + Lark + DingTalk = off-pattern for v1 (LE31 v1 is Telegram-only per charter §3.2); MIT permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *multi-messenger-protocol-abstraction* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the cross-platform-messenger-abstraction dimension* (every state transition is an explicit SQLModel row; no silent transition; the *aiogram-cook-bot* pattern IS the *single-messenger-protocol-implementation* posture). Charter §3.1 alignment (the *multi-messenger-protocol-abstraction* discipline IS the *explicit-state-transition* applied to the cross-platform-messenger-abstraction dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive); **§3.4 NOT triggered** (nonebot2 is *developer/staff-tooling* — chatbot-framework for developers, NOT customer-facing-AI). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 cross-platform-messenger-framework-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 14.5 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours with caveat: 14.5 KB modest-repo size limits inspection depth — the *vocabulary* is high-value, the *code* is reference-only). **Cost-to-value ratio: moderate-to-high** (the *cross-platform + async + Python + chatbot-framework + FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + multi-messenger-protocol-abstraction* decuple + the longest-maintained + highest-star-count signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/229-nonebot-nonebot2-mit-cross-platform-python-asynchronous-chatbot-framework-fastapi-telegram-bot-qq-lark-dingtalk-onebot-multi-messenger-protocol-abstraction-HANDOFF.md` and `features/229-nonebot-nonebot2-mit-cross-platform-python-asynchronous-chatbot-framework-fastapi-telegram-bot-qq-lark-dingtalk-onebot-multi-messenger-protocol-abstraction.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + multi-messenger-protocol-abstraction documentation for the next v2 cross-platform-messenger-framework review moment; **cross-section JTBD value is moderate-to-high, the highest-star-count cross-platform Python chatbot framework candidate of the 57-pass brainstorm series = the *multi-messenger-protocol-abstraction* vocabulary reference, but the *chatbot-framework replacement* is off-pattern for LE31 v1 today because LE31 v1 uses aiogram per charter §3.2**).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a second messenger surface (Discord/Slack/QQ/Lark/DingTalk), a multi-messenger-protocol-abstraction layer, or a cross-platform-chatbot-framework reference):

- `app/messenger_platforms/` — possibly add (the multi-messenger-protocol-abstraction module; depends on the v2 change).
- `app/messenger_platforms/telegram_adapter.py` — possibly add (the Telegram-adapter; depends on the v2 change).
- `app/messenger_platforms/discord_adapter.py` — possibly add (the Discord-adapter; depends on the v2 change).
- `app/messenger_platforms/slack_adapter.py` — possibly add (the Slack-adapter; depends on the v2 change).
- `app/messenger_platforms/qq_adapter.py` — possibly add (the QQ-adapter; depends on the v2 change).
- `app/messenger_platforms/lark_adapter.py` — possibly add (the Lark-adapter; depends on the v2 change).
- `app/messenger_platforms/dingtalk_adapter.py` — possibly add (the DingTalk-adapter; depends on the v2 change).
- `app/messenger_platforms/router.py` — possibly add (the cross-platform-message-routing handler; depends on the v2 change).
- `app/models/messenger_platform.py` — possibly add (the `messenger_platform` SQLModel table; depends on the v2 change).
- `app/models/cross_platform_message.py` — possibly add (the `cross_platform_message` SQLModel table; depends on the v2 change).
- `tests/test_messenger_platforms.py` + `tests/test_cross_platform_routing.py` — possibly add (the integration tests for the multi-messenger-protocol-abstraction + cross-platform-message-routing surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no second messenger surface added, no multi-messenger-protocol-abstraction layer added, no cross-platform-message-routing layer added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/229-nonebot-nonebot2-mit-cross-platform-python-asynchronous-chatbot-framework-fastapi-telegram-bot-qq-lark-dingtalk-onebot-multi-messenger-protocol-abstraction.md` exists and is read back by the parent.
- [ ] `specs/229-nonebot-nonebot2-mit-cross-platform-python-asynchronous-chatbot-framework-fastapi-telegram-bot-qq-lark-dingtalk-onebot-multi-messenger-protocol-abstraction-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `nonebot/nonebot2` description is quoted verbatim (14.5 KB repo, Chinese + English bilingual).
- [ ] The 7722★/661⑂ + MIT permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption) + Python + in-window-by-pushed_at-only + 14 topics + description *"跨平台 Python 异步聊天机器人框架 / Asynchronous multi-platform chatbot framework written in Python"* is documented.
- [ ] The charter §3.1 alignment via *multi-messenger-protocol-abstraction = explicit-state-transition discipline applied to cross-platform-messenger-abstraction* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (MIT permissive) is documented.
- [ ] The charter §3.4 NOT-triggered (nonebot2 is developer/staff-tooling, NOT customer-facing-AI) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a second messenger surface (Discord/Slack/QQ/Lark/DingTalk), a multi-messenger-protocol-abstraction layer, or a cross-platform-chatbot-framework reference lands):**
- [ ] The PR is read back by the parent.
- [ ] The `nonebot/nonebot2` *cross-platform + async + Python + chatbot-framework + FastAPI + Telegram-bot + QQ + Lark + DingTalk + OneBot + multi-messenger-protocol-abstraction* vocabulary is evaluated against the PR's changes: does the change address the *cross-platform-messenger-abstraction* discipline? does the change preserve the *multi-messenger-protocol-abstraction* primitive? does the change preserve the *charter §3.1 explicit-state-transition* pattern? does the change preserve the *charter §3.4 developer/staff-tooling boundary*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

Fully reversible. Delete `specs/229-nonebot-nonebot2-mit-cross-platform-python-asynchronous-chatbot-framework-fastapi-telegram-bot-qq-lark-dingtalk-onebot-multi-messenger-protocol-abstraction-HANDOFF.md` and `features/229-nonebot-nonebot2-mit-cross-platform-python-asynchronous-chatbot-framework-fastapi-telegram-bot-qq-lark-dingtalk-onebot-multi-messenger-protocol-abstraction.md`. The git revert path is `git revert HEAD~0 -- features/229-...md specs/229-...-HANDOFF.md` (or whichever commit introduced the files). No retained data; no safe-failure-mode concern; no operator-visible behavior change.

## 6. Mandatory LE31 skill list

The coding agent MUST load and follow these skills before starting work on this HANDOFF (per `le31-coding-agent-brief/SKILL.md`):

- `le31-conventions/SKILL.md` — the canonical seven-check feature gate + the v1/v2/v2-AI bucket taxonomy.
- `le31-daily-brainstorm/SKILL.md` — the parent context for cross-section picks + the daily-brainstorm-no-fabrication-canary.
- `le31-daily-research/SKILL.md` — the sister daily-research skill for source-family coverage.
- `le31-feature-pipeline/SKILL.md` — the immediate parent skill for this HANDOFF.
- `le31-verification-protocol/SKILL.md` — the verification protocol referenced in §4.
- `le31-coding-agent-brief/SKILL.md` — the skill that produces the paste-in prompt-in prompt automatically from this slice contract; do not paste chat excerpts.
- `le31-handoff-spec/SKILL.md` — the skill that defines this HANDOFF format.
- `le31-v1-feature-pattern/SKILL.md` — the v1 feature pattern reference.

**Do not start any code work today.** The HANDOFF is documentation-only.

## 7. Honest disclosure

- The 7722★/661⑂ is explicitly NOT offered as evidence of *LE31 needing chatbot-framework replacement*; the 7722★/661⑂ is for the *chatbot-framework domain*, not for the *multi-messenger-protocol-abstraction* primitive. The transferable item is the *technique* (OneBot + cqhttp + mirai + Lark + DingTalk + Telegram multi-protocol-abstraction), not the *chatbot-framework* itself.
- LE31 v1 today uses aiogram per charter §3.2 and does not need a *chatbot-framework replacement*; v2's *second-messenger surface* — Discord or Slack for the cook-bot — would inherit the *multi-messenger-protocol-abstraction* primitive.
- The 14.5 KB size is modest; source-code inspection depth is limited; the *vocabulary* is high-value, the *code* is reference-only.
- The repo is maintained continuously since 2020 (5.5 years); the *longest-maintained cross-platform Python chatbot framework* of the 57-pass series.
- Charter §3.4 NOT triggered because nonebot2 is developer/staff-tooling (chatbot-framework for developers), NOT customer-facing-AI.