# Feature 208 — `njbbaer-simulacra-telegram-llm-template-based-context-system-openrouter-multi-provider` (defer)

> **NEW observation (2026-09-20).** Documents in-window GitHub Search `topic:telegram-bot` query result: `njbbaer/simulacra` (**MIT ✓**, **4★/1⑂**, Python, **pushed 2026-09-20T18:31:08Z = TODAY** (in-window by `pushed_at` only — *created 2023-09-14T00:00:00Z = OUT-OF-WINDOW* = 3 years before the 30-day window start; **the repo is IN-WINDOW BY PUSH ONLY per the SKILL hard rule**), **1556 KB substantial repo**, default_branch=`master`). Topics (verbatim from raw JSON, **6 topics**): `ai`, `llm`, `openrouter`, `python`, **`telegram`**, **`telegram-bot`**. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-20): *"Build LLM-powered Telegram bots with a template-based context system."* The **template-based-bot-context primitive** + the **Telegram-LLM-template-based-context + OpenRouter-multi-provider + AI-but-operator-only** triple-primitive: the *template-as-context* pattern — when a Telegram bot's context is *templated* (a template file with placeholders + a renderer that fills the placeholders with runtime data), the bot's *behavior* is *defined-by-the-template*, not *defined-by-LLM-prompts*. The *template-based* discipline is the **charter §3.4-compatible** alternative to free-form LLM-prompts: the AI cannot *invent* context (the template constrains the structure), the AI can only *fill* context (the renderer applies LLM-generated values to the templated slots). The *"openrouter"* topic names the **multi-provider-LLM-abstraction** primitive (OpenRouter = a multi-provider LLM API gateway; the abstraction layer lets a Telegram bot switch between OpenAI/Anthropic/Google/local-LLM providers without changing the bot code; LE31 v1 has NO LLM provider surface today; the *multi-provider-abstraction* is the *future v2-AI owner-assist surface*). The *"llm"* + *"ai"* topics are the **LLM-assisted-bot** surface (the bot uses LLM to *interpret* the user's message + *generate* the bot's reply; the *interpretation + generation* are LLM-driven; the *structure* is template-driven; the *trust-boundary* is the template). **MIT ✓ §3.2 STRICTLY-COMPATIBLE** for vocabulary + architecture-reference adoption; **§3.4 territory-future-review** — the *template-based-context-system* primitive IS the *observable-evidence + non-AI-fallback* pattern by construction (the template is the evidence; the deterministic-template-renderer is the non-AI-fallback). Bucket: **v2 owner-assist (Telegram-LLM + template-based-context + multi-provider-abstraction + AI-but-operator-only primitive, parking-lot defer)** — vocabulary + template-based-context primitive + OpenRouter-multi-provider + AI-but-operator-only documentation, zero build time today.

## Goal

Retain the **"Build LLM-powered Telegram bots with a template-based context system"** cross-section architectural vocabulary + **template-based-bot-context primitive** + **Telegram-LLM-template-based-context + OpenRouter-multi-provider + AI-but-operator-only** triple as the persistent v2 owner-assist reference for any future LE31 v2 maintainer asking the *LLM-with-deterministic-fallback* question (does LE31 v2 ever need an LLM-assisted surface? does LE31 v2 ever need a template-based-context pattern? does LE31 v2 ever need a multi-provider-LLM-abstraction layer? does LE31 v2 ever need an AI-but-operator-only surface?). The artifact is the persistent *template-based-context primitive + OpenRouter-multi-provider + AI-but-operator-only* vocabulary as a *named* v2 architectural reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `njbbaer/simulacra` cross-section vocabulary: the **first in-window 2026 Python Telegram-LLM-template-based-context repo of the 44-pass brainstorm series** with the *ai + llm + openrouter + python + telegram + telegram-bot* 6-topic set; the *template-based context system* description explicitly names the *template-as-context* discipline.
- A written record of the **template-based-bot-context primitive**: the *template-as-context* pattern — when a Telegram bot's context is *templated* (a template file with placeholders + a renderer that fills the placeholders with runtime data), the bot's *behavior* is *defined-by-the-template*, not *defined-by-LLM-prompts*. The *template-based* discipline is the **charter §3.4-compatible** alternative to free-form LLM-prompts: the AI cannot *invent* context (the template constrains the structure), the AI can only *fill* context (the renderer applies LLM-generated values to the templated slots).
- A written record of the **multi-provider-LLM-abstraction primitive (OpenRouter)**: the *"openrouter"* topic names the **multi-provider-LLM-abstraction** primitive (OpenRouter = a multi-provider LLM API gateway; the abstraction layer lets a Telegram bot switch between OpenAI/Anthropic/Google/local-LLM providers without changing the bot code; LE31 v1 has NO LLM provider surface today; the *multi-provider-abstraction* is the *future v2-AI owner-assist surface*).
- A written record of the **AI-but-operator-only posture**: the bot uses LLM to *interpret* the user's message + *generate* the bot's reply; the *interpretation + generation* are LLM-driven; the *structure* is template-driven; the *trust-boundary* is the template. This is the **AI-but-operator-only** posture — the AI assists the operator (the bot user is the operator, not a customer) without making autonomous decisions.
- A written record of the **charter §3.4 observable-evidence + non-AI-fallback primitive by construction**: the *template-based-context-system* primitive IS the *observable-evidence + non-AI-fallback* pattern by construction (the template is the evidence; the deterministic-template-renderer is the non-AI-fallback; the renderer works without the LLM; the LLM only fills the templated slots with values). The **template-as-context IS the charter §3.4 invariant language** — *"AI may assist owner/staff with observable evidence and non-AI fallback"* — applied to the LLM-context layer.
- A written record of the **MIT license as a documented strictly-adoptable artifact**: the codebase CAN be adopted as a reference for the *template-based-context + OpenRouter-multi-provider pattern* (MIT = §3.2 STRICTLY-COMPATIBLE for vocabulary AND architecture-reference adoption); LE31 would re-implement the template-as-context pattern against its own FastAPI + SQLModel + aiogram v3 stack, not import the OpenRouter integration or the LLM-provider code (LE31 v1 has no LLM surface today).
- A decision record: today's verdict is `defer (parking-lot)` because the *template-based-context + OpenRouter-multi-provider + AI-but-operator-only* vocabulary is a v2 owner-assist reference, not a v1 or v2 build implication. v1 has no LLM surface today; the *template-as-context + multi-provider-abstraction + AI-but-operator-only* vocabulary documents the *future-extension* for the next v2 maintainer asking the *LLM-with-deterministic-fallback* question.

**Out of scope (defer artifact):**
- Any change to the LE31 v1 surface (no LLM surface today, no template-based-context today, no multi-provider-LLM-abstraction today).
- Any change to the LE31 v1 Telegram bot (no LLM-assist surface today, the cook-bot is purely transactional).
- Any change to the LE31 v1 waiter web UI (no LLM-assist surface today).
- Adoption of the `njbbaer/simulacra` code as a v2 dependency (the repo is 4★/1⑂ at 1556 KB; the *template-based-context + OpenRouter-multi-provider + AI-but-operator-only* vocabulary would need to be independently re-implemented and validated against the LE31 v1's no-LLM-surface posture, not simply imported; the OpenRouter integration is off-pattern for LE31 v1; the LLM-provider code is off-pattern for LE31 v1).
- Any change to the `audit_logs` table or `StockEntry` ledger today.
- Any new dependency on the `njbbaer` maintainer.

## Evidence / JTBD

When a future LE31 v2 maintainer asks *"if v2 introduces an LLM-assisted surface, a template-based-context pattern, a multi-provider-LLM-abstraction layer, or an AI-but-operator-only surface, what is the template-based-context + OpenRouter-multi-provider + AI-but-operator-only primitive that preserves the existing v1 no-LLM-surface + pure-transactional-cook-bot posture?"*, the maintainer wants *evidence that another independent 2026 Python repo at 1556 KB with MIT license + in-window-by-push-only + 4★/1⑂ + 6 topics including ai + llm + openrouter + python + telegram + telegram-bot is shipping the template-based-context + multi-provider-abstraction + AI-but-operator-only primitive as the v2 owner-assist discipline*, but struggles because *v1 has no documented LLM-surface primitive in the charter*, so that *v2 can introduce the LLM-assisted-surface + template-based-context + multi-provider-abstraction vocabulary with the explicit charter §3.4 observable-evidence + non-AI-fallback discipline rather than reinventing the pattern*.

- **Evidence class**: observed (the `njbbaer/simulacra` description explicitly names *"Build LLM-powered Telegram bots with a template-based context system"* = the template-based-context primitive; the *openrouter* topic names the *multi-provider-LLM-abstraction* primitive; the *ai + llm* topics name the *LLM-assisted-bot* surface).
- **Confidence**: medium for the template-based-context + OpenRouter-multi-provider + AI-but-operator-only vocabulary (MIT + Python + 1556 KB substantial + in-window-by-push-only + 4★/1⑂ + 6 topics + explicit template-based-context description + OpenRouter multi-provider topic = §3.2 STRICTLY-COMPATIBLE + §3.4 territory-future-review; the template-based-context discipline IS the *charter §3.4 observable-evidence + non-AI-fallback* pattern by construction).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + template-based-context documentation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + template-based-context documentation**: when (if) LE31 v2 introduces an LLM-assisted surface, a template-based-context pattern, a multi-provider-LLM-abstraction layer, or an AI-but-operator-only surface, the *template-based-context + OpenRouter-multi-provider + AI-but-operator-only* vocabulary is documented.

## Description

GitHub `njbbaer/simulacra` (MIT, 4★/1⑂, Python, pushed 2026-09-20T18:31:08Z = in-window by `pushed_at` only; created 2023-09-14T00:00:00Z = out-of-window, 1556 KB substantial repo).

Description (verbatim): *"Build LLM-powered Telegram bots with a template-based context system."*

Topics (verbatim from raw JSON, 6 topics): `ai`, `llm`, `openrouter`, `python`, `telegram`, `telegram-bot`.

The **3 named LLM-assisted-bot primitives**:

| njbbaer/simulacra primitive | LE31 v1 primitive | Match status |
|---|---|---|
| `llm` + `ai` (LLM-assisted-bot surface) | (LE31 v1 has no LLM surface today; the cook-bot is purely transactional) | **★ GAP: LE31 v1 has no LLM-assisted surface today** |
| `openrouter` (multi-provider-LLM-abstraction) | (LE31 v1 has no LLM provider surface today; the *provider-abstraction* is a v2-AI concern) | **★ GAP: LE31 v1 has no multi-provider-LLM-abstraction primitive today** |
| `template-based-context-system` (template-as-context discipline) | (LE31 v1 has no template-based-context today; the cook-bot context is implicit) | **★ GAP: LE31 v1 has no template-based-context primitive today** |

The **template-based-bot-context primitive**: the *template-as-context* pattern — when a Telegram bot's context is *templated* (a template file with placeholders + a renderer that fills the placeholders with runtime data), the bot's *behavior* is *defined-by-the-template*, not *defined-by-LLM-prompts*. The *template-based* discipline is the **charter §3.4-compatible** alternative to free-form LLM-prompts: the AI cannot *invent* context (the template constrains the structure), the AI can only *fill* context (the renderer applies LLM-generated values to the templated slots).

Example template (illustrative, not from simulacra):
```
Bot context template:
- Today's date: {{date}}
- Restaurant name: {{restaurant_name}}
- Stock levels: {{stock_levels}}
- Recent orders: {{recent_orders}}
- User query: {{user_query}}
```

The renderer fills `{{date}}`, `{{restaurant_name}}`, `{{stock_levels}}`, `{{recent_orders}}` with deterministic-data from the database (no LLM); the renderer calls the LLM to fill `{{user_query}}` with an interpreted-form of the user's message; the assembled context is sent to the LLM as the prompt; the LLM generates a response based on the templated-context.

The *template-constrains-structure* discipline is the **trust-boundary** between the LLM and the persistent-store: only deterministic-data (date, restaurant_name, stock_levels, recent_orders) comes from the database; only the user-query interpretation comes from the LLM. The LLM cannot *invent* stock_levels (the template constrains the structure); the LLM can only *interpret* the user-query.

The **multi-provider-LLM-abstraction primitive (OpenRouter)**: OpenRouter = a multi-provider LLM API gateway; the abstraction layer lets a Telegram bot switch between OpenAI/Anthropic/Google/local-LLM providers without changing the bot code; LE31 v1 has NO LLM provider surface today; the *multi-provider-abstraction* is the *future v2-AI owner-assist surface*. The OpenRouter-API surface is the *provider-abstraction-as-a-service* pattern.

The **AI-but-operator-only posture**: the bot uses LLM to *interpret* the user's message + *generate* the bot's reply; the *interpretation + generation* are LLM-driven; the *structure* is template-driven; the *trust-boundary* is the template. This is the **AI-but-operator-only** posture — the AI assists the operator (the bot user is the operator, not a customer) without making autonomous decisions. The *operator-confirms-before-action* discipline is the *AI-but-operator-only* posture.

The **charter §3.4 observable-evidence + non-AI-fallback primitive by construction**: the *template-based-context-system* primitive IS the *observable-evidence + non-AI-fallback* pattern by construction (the template is the evidence; the deterministic-template-renderer is the non-AI-fallback; the renderer works without the LLM; the LLM only fills the templated slots with values). The **template-as-context IS the charter §3.4 invariant language** — *"AI may assist owner/staff with observable evidence and non-AI fallback"* — applied to the LLM-context layer.

The **MIT license as a documented strictly-adoptable artifact**: the codebase CAN be adopted as a reference for the *template-based-context + OpenRouter-multi-provider pattern* (MIT = §3.2 STRICTLY-COMPATIBLE for vocabulary AND architecture-reference adoption); LE31 would re-implement the template-as-context pattern against its own FastAPI + SQLModel + aiogram v3 stack, not import the OpenRouter integration or the LLM-provider code (LE31 v1 has no LLM surface today).

## Data model

**No LE31 data model change today.** The defer artifact is documentation only. The template-based-bot-context primitive names the *template-as-context + OpenRouter-multi-provider + AI-but-operator-only* extensions that any future v2 schema change should consider; v2 maintainer decision required before adopting the LLM-assisted surface (LE31 v1 currently operates no LLM surface; LLM-assisted is a v2 architecture-decision, not a v1 implementation task).

## Implementation steps

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a template-based-context-bot to the LE31 operator surface, a multi-provider-LLM-abstraction layer to the LE31 v2 architecture, or a deterministic-template-renderer for any LLM-assisted workflow):

- `app/bot/templates/` — possibly add (the template directory; each bot gets its own template file with placeholders; depends on the v2 change).
- `app/bot/renderer.py` — possibly add (the deterministic-template-renderer that fills the placeholders with runtime-data; depends on the v2 change).
- `app/llm/openrouter.py` — possibly add (the OpenRouter multi-provider-LLM-abstraction layer; depends on the v2 change).
- `app/llm/providers/` — possibly add (the individual LLM provider implementations: OpenAI, Anthropic, Google, local-LLM; depends on the v2 change).
- `app/bot/llm_assist.py` — possibly add (the LLM-assisted-bot handler that calls the renderer + the LLM provider; depends on the v2 change; **charter §3.4 future-review required**).
- `tests/test_template_renderer.py` + `tests/test_openrouter_provider.py` + `tests/test_llm_assist_bot.py` — possibly add (the integration tests for the template-based-context + OpenRouter-multi-provider + LLM-assisted-bot surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no LLM surface added.

## Telegram interaction if any

None today. If a future v2 trigger fires (template-based-context-bot), the Telegram interaction could be extended with LLM-assist: the cook sends a typed message (e.g. *"what's running low?"*); the bot's template is filled with today's stock-levels + recent-orders; the LLM interprets the cook's query + generates a reply; the cook receives a templated + LLM-generated response (e.g. *"Schnitzel is running low (3 portions left); Fries is fine (8 portions left)"*). The *template-as-context* discipline ensures the LLM cannot invent stock-levels (the template constrains the structure); the LLM can only interpret the cook's query.

## Dependencies

- No new dependency today.
- If a future v2 trigger fires:
  - Software: an LLM provider library (e.g. `openai` for OpenAI, `anthropic` for Anthropic, `openrouter` for OpenRouter; LE31 currently has no LLM dependency).
  - Software: a template-renderer library (e.g. `jinja2` for Python template-rendering; LE31 currently has no template-renderer dependency).
  - Schema: a `bot_template` table for bot-template storage + a `bot_context` table for runtime-context; depends on the v2 change.

## Open questions

- Should LE31 v2 introduce a template-based-context-bot to the LE31 operator surface (e.g. owner-recap-bot with templated daily-summary)?
- Should LE31 v2 introduce a multi-provider-LLM-abstraction layer (OpenRouter or equivalent)?
- Should LE31 v2 introduce a deterministic-template-renderer for any LLM-assisted workflow (charter §3.4 observable-evidence + non-AI-fallback)?
- Should LE31 v2 introduce an AI-but-operator-only surface (charter §3.4 territory)?
- If yes to any of the above: should the v2 PR cross-reference this feature 208 contract + HANDOFF as the named architectural reference?

## Why this matters

The *template-based-context + OpenRouter-multi-provider + AI-but-operator-only* primitive is the **gap** between LE31 v1's no-LLM-surface + pure-transactional-cook-bot posture and a *template-based-context + multi-provider-LLM-abstraction + AI-but-operator-only* v2 owner-assist surface. The *template-as-context IS the charter §3.4 observable-evidence + non-AI-fallback primitive by construction* — the template is the evidence; the deterministic-template-renderer is the non-AI-fallback; the LLM only fills the templated slots. For LE31 v2's owner-assist surface (template-based-context + multi-provider-LLM-abstraction + AI-but-operator-only), the simulacra pattern is the *future-extension reference*: when (if) LE31 v2 introduces an LLM-assisted surface, a template-based-context pattern, a multi-provider-LLM-abstraction layer, or an AI-but-operator-only surface, the *template-based-context + OpenRouter-multi-provider + AI-but-operator-only* vocabulary is documented.
