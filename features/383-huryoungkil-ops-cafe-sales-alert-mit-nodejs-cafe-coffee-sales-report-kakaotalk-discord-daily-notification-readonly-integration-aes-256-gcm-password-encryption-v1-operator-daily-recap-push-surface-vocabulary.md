# Feature 383 — `huryoungkil-ops/cafe-sales-alert`: the operator's daily recap is a *push* surface, and its cost was counted

> **NEW observation (2026-10-26).** Documents in-window GitHub repo `huryoungkil-ops/cafe-sales-alert` (**licence: `mit` ✓ §3.2 STRICTLY-COMPATIBLE — the *vocabulary-shape* is the transferable item; the *code-shape* is NOT adopted**), **★0/⑂0 — no traction evidence in either direction**, **5,351 KB**, `default_branch=main`, `archived=false`, `fork=false`, Node.js/JavaScript **✗ off-stack**, created **2026-10-25T12:30:10Z AND pushed 2026-10-25T13:51:34Z = IN-WINDOW BY BOTH FIELDS** (a **same-day** repo — created and last pushed on 2026-10-25 itself). All field values read from a **direct `/repos/` GET** by the parent on 2026-10-26, not from search-result numbers. Description (verbatim from GitHub API): *"☕ 유로머신 매출 알리미 — 유로커피머신 어제 매출을 매일 아침 카카오톡·디스코드로 (보고서 이미지). 비밀번호 AES-256 암호화"*.
>
> **The README was also read** (parent, 2026-10-26, `/tmp/le31-daily-2026-10-26/rd/huryoungkil-ops_cafe-sales-alert.md`). The repo is written in Korean; the quoted strings below are the parent's translations of the README's own text, with the original Korean retained where the wording is load-bearing.
>
> Bucket: **v1 (operator-recap surface vocabulary)** — Pick B of Daily Research 2026-10-26. Build verdict: **`defer`** (parking-lot; **vocabulary reference only** — no code changes, no schema change, and **no licence to copy the implementation from**).

## Goal

Retain `huryoungkil-ops/cafe-sales-alert` as the external arrival that does two things LE31's own artefacts have not done:

1. **It counts the cost of a recurring operator task in hours per year** — *"A day takes 3 minutes, so a year takes about 18 hours"* (README: *"하루 3분이면 1년에 약 18시간"*). **This is the first frequency-quantified operator-pain claim in the 88-pass series.**
2. **It shows a push-notification recap surface that is safe by construction** — read-only integration, credentials encrypted with a separated key, and polling that stops the moment authentication fails.

**The deliverable is one document** recording the cost arithmetic, the read-only credential pattern, and the stop-polling rule — as inputs to a decision about `features/39-owner-daily-recap-telegram.md`, which already exists and is **not** re-opened here.

## Scope

**In scope (v1 — documentation only):**
- One document recording the **"3 minutes a day → 18 hours a year"** cost arithmetic as the *one quantified frequency claim* in this series, with the caveat that it applies to an **unattended** venue and **has not been validated for LE31's waiter-and-cook setting**.
- One document recording the **read-only integration rule**: the service holds the operator's vendor credentials and *deliberately* has no code path that changes anything upstream.
- One document recording the **credential-handling pattern**: password hashed with scrypt, payload encrypted with **AES-256-GCM**, **key held in a server-side `.env` separated from the database**.
- One document recording the **stop-polling-on-auth-failure rule**: *"If the password changes and login fails, stop querying immediately and notify — do not keep trying, or the account gets locked"* (README: *"유로 로그인 시도는 한 사람당 1시간에 6번까지"* — at most 6 login attempts per person per hour).
- A note that **the report is rendered as an image card** (SVG → PNG) and delivered to two chat surfaces.

## Out of scope

- **Any code, schema, or migration in LE31.** No scheduled job, no cron entry, no notification table, no report renderer, no external credential store.
- **Any port or vendor of the Node.js implementation.** The licence is MIT, so it is *legally* adoptable — **but the stack is Node.js + SQLite, and LE31's is Python 3.13 / FastAPI / SQLModel / Postgres.** Adopting it would be a §3.2 stack change requiring an explicit charter decision. **The transferable content is the *rule set*, not the code.**
- **Any vendor-integration pattern in LE31.** LE31 has **no third-party vendor system to connect to.** The read-only rule is recorded because it is the right shape *if* LE31 ever integrates one (e.g. a payment terminal or an accounting package) — **not because LE31 is about to integrate one.**
- **Any new owner-facing surface.** §3.1 names **two** operational surfaces: the waiter web UI and the cook Telegram bot. **An owner-facing recurring-report surface is a §3.1 surface question, and `features/39-owner-daily-recap-telegram.md` already proposes one on the existing bot.** This artifact adds evidence; it does not add a surface.
- **Any KakaoTalk or Discord integration.** LE31's chat surface is Telegram. Both are chat surfaces; only one is LE31's.
- **Re-opening `features/39-owner-daily-recap-telegram.md`.** That feature exists. This artifact is **evidence for** it, not a replacement for it.
- **Any money, cost, or valuation surface.** §3.3 forbids it. "Yesterday's sales" here is a *turnover figure*, which is already a first-class LE31 concept (`Bill`, `DerivedTip`) — **but no valuation or margin is in scope here.**

## Description

**What the thing is.** An **unattended coffee machine** (a Korean brand's operator admin site) that reports yesterday's sales to the owner **every morning** — to KakaoTalk ("나에게 보내기", send-to-me) and to Discord via webhook — with a rendered report card image.

**The delivered report contains**, per the README's own table:

- *Daily (default 7am, configurable):* yesterday's sales + points used · comparison to the same weekday last week ▲▼ · this month's cumulative and projected sales · hot/cold/other cup counts · **yesterday's menu Top 5 (by count and by value)** · espresso pump 1/2/3 usage (with ⚠️ when a pump shows 0).
- *Monthly (1st of the month):* last month's sales + ▲▼ vs the prior month · daily average · best day · monthly menu Top 5.

**The cost claim, verbatim in intent:** *"Unattended-cafe sales require the owner to log into the admin page every day, pick a date, and read a number. That's 3 minutes a day — about 18 hours a year. So I opened my own sales-alert bot as a site anyone can use."* (README: *"하루 3분이면 1년에 약 18시간."*)

**Why this claim is the artifact's real value.** Every prior pick in this series has offered a *shape* with no frequency attached — "here is how someone built X". This one attaches a number: **18 hours per year, per venue.** That is a frequency, and the gate's check 6 (cost to operational value) needs one. **The caveat is equally important and is recorded here rather than buried:** the 3-minute figure is for an **unattended** venue where the only task is reading one number, and it is **self-reported by the author, unvalidated, and not measured for a waiter-and-cook setting.** LE31's owner has a richer surface (visits, orders, stock) and a correspondingly richer potential recap — **so the 18 hours is a floor-shaped anecdote, not a forecast for LE31.** It is recorded as `inferred`, not `observed`.

**The security pattern is the second, quieter contribution.** The README is unusually explicit about what it does with a stranger's vendor password:

| README rule | What it means |
|---|---|
| *"유로 비밀번호는 AES-256-GCM 으로 암호화해 저장. 키는 DB 와 분리된 서버 `.env` 에만 있음"* | Password stored encrypted with **AES-256-GCM**; the key lives **only in a server-side `.env` separated from the database** |
| *"매출 화면 API 를 읽기만 함 — 메뉴·가격·기계 설정을 바꾸는 코드가 없음"* | The sales API is **read-only**: *"there is no code that changes menus, prices, or machine settings"* |
| *"저장 전에 실제로 로그인해 보고, 맞을 때만 저장"* | Credentials are **verified by an actual login** before being stored, and stored only if they work |
| *"비밀번호가 바뀌어 로그인이 안 되면 즉시 조회를 멈추고 알림"* | **On auth failure, stop querying immediately and notify** — explicitly to avoid locking the owner's account |
| *"유로 로그인 시도는 한 사람당 1시간에 6번까지"* | At most **6 login attempts per person per hour** |
| *"이 사이트 가입에 이메일·전화번호·실명을 받지 않음"* | **The service collects no email, phone, or real name** |
| *"탈퇴하면 계정·암호화된 비밀번호·매출 기록·보고서를 즉시 전부 삭제"* | **Immediate full deletion** on account closure |

**Why this is worth filing for LE31.** LE31's §3.7 invariant is *"store only data needed for restaurant operations; v1 guest demographics are counts, not identity or contact data."* This artifact is an instance of that principle applied to a **third-party credential** rather than a guest: *the operator's own vendor password is the most sensitive thing the system holds, and the design says so out loud.* **The "read-only" rule is also a §3.4-shaped rule**: the integration **observes** and never transitions. It is the same explicit-transition discipline LE31 applies to orders, applied to an external system.

**And the delivery shape is a real precedent.** The report is rendered **server-side as SVG → PNG** and delivered as an image to two chat surfaces — not as a formatted text message. The reason is legible from the README: a **report card image** carries the chart, the deltas, and the Top-5 table without the recipient needing to scroll a chat log. **Whether LE31's Telegram bot should send a recap as an image is a question this artifact raises and does not answer.**

**Two structural observations that are easy to misread and are recorded explicitly:**
- **The schedule is a *push*, not a pull.** The owner does not log in to see anything. This is the artifact's shape, and it is a **different** shape from `features/39-owner-daily-recap-telegram.md` if that feature is a reply-to-command surface. **The distinction is noted, not resolved here.**
- **The service holds a credential for a machine the operator owns — it is not a customer-data system.** **None of this touches LE31's guest-data model**, and the CNIL items in this window (2026-10-19 telephone-prospecting consent webinar; 2026-10-22 plenary agenda) are unrelated and are recorded as unrelated.

## Data model

**No data model change. This artifact is a document.**

For the record, the *shape* of the rules being documented, in LE31's own terms (**not proposed as a schema**):

- A **recurring report** is derived from existing facts — never stored as a new ledger entry. LE31's facts for such a report would be `Bill` (closed visits, `total_due`, `total_paid`), `DerivedTip`, and `StockEntry` aggregates — **all already exist** (`models.py:158-179`, `models.py:113-126`).
- A **notification delivery** is an operational fact about a *message sent*, not about the *business event*. **Whether LE31 needs a notification record at all is an open question** — a pure push with no record is possible, and the report itself is **derived**, so §3.3's append-only rule is not engaged unless a delivery is recorded.
- **No external-credential model is created.** LE31 has no vendor integration today, so a credential table would be a schema change for a system that does not exist. **Recorded as a rule, not as a table.**
- **No report-rendering model.** A rendered image is a **derived artifact**, not a fact — the same category as LE31's derived stock.

## Implementation steps

**There are no implementation steps. The deliverable is one document.**

The steps that *would* apply **if and only if** the owner later asks for it, and which this artifact explicitly does **not** authorise:

1. **The owner answers the frequency question with LE31's own numbers.** *"How long does it take you to check yesterday's numbers — and how many times a day?"* This artifact supplies **an anecdote**, not LE31's number.
2. **Re-run the feature gate** with the owner's answer as `reported` evidence. This artifact's evidence class is **`inferred`**.
3. **If a recap surface is approved, reuse `features/39-owner-daily-recap-telegram.md`** rather than creating a parallel one. **A second recap surface would be a §3.1 surface-count problem and a duplicate.**
4. **Decide push vs pull explicitly.** Push (a scheduled delivery the owner never requests) and pull (a bot command) have different privacy, cost, and failure profiles — **a scheduled push must also define what happens when nobody opens it.**
5. **If any external integration is ever proposed, the acceptance path is observable:** the integration is verified to perform **no write** against the third party, and to **stop** on auth failure rather than retrying.

## Telegram interaction if any

**None from this artifact. This is deliberate and is stated plainly.**

The artifact's own delivery surfaces are **KakaoTalk** and **Discord** — **neither is LE31's**. LE31's chat surface is Telegram (`backend/app/bot/cook_bot.py`, aiogram v3).

**What the artifact contributes to the Telegram surface is a rule, not a delivery:** *if* LE31 ever sends a recurring recap on the bot, then **the credential-holding and stop-on-failure rules transfer**, because Telegram's bot API token is itself a credential held on LE31's side, and Telegram's API can fail for reasons LE31 does not control.

**The bot must not become a report-rendering surface in this pass.** Rendering an SVG→PNG card is a Node.js/headless-browser shape, and LE31 has no such toolchain. **The transferable idea is "the recap is a picture, not a wall of text"** — a rendering decision that belongs to whichever surface eventually ships it, and that **is not decided here**.

## Dependencies

- **The LE31 owner** — the frequency question must be answered by a person.
- **`features/39-owner-daily-recap-telegram.md`** — **the existing proposal this artifact is evidence for.** Load it before writing anything about a daily recap.
- **`le31-conventions`** — the seven-check gate; and the §3.1 two-surface invariant and the §3.7 data-minimisation invariant.
- **`le31-v1-feature-pattern`** — for the shape of any future contract derived from this artifact.
- **`PROJECT_CHARTER.md` §3.1** — *one small restaurant and two primary operational surfaces: waiter web UI and cook Telegram bot.*
- **`PROJECT_CHARTER.md` §3.7** — *store only data needed for restaurant operations.*
- **No third-party integration.** LE31 has no vendor system to connect to, so the credential rules are recorded **as principles**, not as an implementation dependency.

## Open questions

1. **How long does the LE31 owner actually spend on this?** — the artifact supplies an **18-hours-per-year anecdote** from an unattended venue, unvalidated for a staffed one. **Unanswered, and the single most load-bearing question for this artifact.**
2. **Push or pull?** — a scheduled daily delivery the owner never requests, or a bot command the owner asks for? The artifact is a push; LE31's existing feature may be a pull. **Unresolved.**
3. **Should the recap be an image or a message?** — the artifact renders a card image; the reason (a chart + deltas + Top-5 without chat scrolling) is legible, but LE31's bot has no rendering toolchain today.
4. **Should a push notification be recorded at all?** — a delivery is a fact about a message, not about the business. **Recording it may be unnecessary; not recording it may lose the audit trail. Open.**
5. **Does an owner-facing recap surface count against §3.1's two surfaces?** — `features/39-owner-daily-recap-telegram.md` proposes putting it on the **existing** cook bot, which keeps the surface count at two. **This artifact does not reopen that.**
6. **What is LE31's equivalent of "stop polling on auth failure"?** — the closest LE31 analogue is a **bot token** or a **payment provider** failing; the rule would be *stop and tell the owner*, not retry into a lockout. **Not specified here.**

## Why this matters

**Because it is the first artifact in 88 passes that attaches a number to a recurring operator chore, and because its security section is an unusually honest instance of LE31's own §3.7 principle applied to something other than guests.**

Every previous pick answered *"what shape exists?"*. This one answers *"what does the shape cost?"* — **3 minutes a day, 18 hours a year** — and that is the input the gate's check 6 asks for and that no prior artifact has supplied. **It is an anecdote, and it is labelled as one**: self-reported, unvalidated, from an unattended venue, and not transferable to a staffed one without the owner confirming it. **A number from the wrong setting is still better than no number, provided it is labelled.** That is the whole discipline this artifact demonstrates.

**The security section is why the artifact survives even if the recap never ships.** Three rules transfer to any future LE31 integration regardless of what that integration is: **read-only by construction** (the code that would change upstream state does not exist), **encrypt the credential with a key held apart from the database**, and **stop on authentication failure rather than retrying into a lockout**. LE31's §3.7 says *store only data needed for restaurant operations*; this artifact is the same sentence written by someone who had to hold a stranger's machine password, and it had to mean it.

**And it is filed as `defer` anyway.** There is **no reported owner pain** about a daily recap in LE31 — check 1 fails, the evidence class is `inferred`, and no build time is spent. The artifact sits in the parking lot as **a quotable cost figure and a quotable credential rule**, ready for the moment an owner asks. **Recording is not building, and a rule that arrives before the question is cheaper than one that arrives after.**
