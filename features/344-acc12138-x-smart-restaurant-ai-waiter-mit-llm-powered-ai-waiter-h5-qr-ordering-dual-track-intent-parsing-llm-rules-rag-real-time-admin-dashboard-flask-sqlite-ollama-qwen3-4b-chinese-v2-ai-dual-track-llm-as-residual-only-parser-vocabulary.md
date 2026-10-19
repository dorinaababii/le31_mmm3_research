# Feature 344 — `acc12138-x-smart-restaurant-ai-waiter-mit-llm-powered-ai-waiter-h5-qr-ordering-dual-track-intent-parsing-llm-rules-rag-real-time-admin-dashboard-flask-sqlite-ollama-qwen3-4b-chinese-v2-ai-dual-track-llm-as-residual-only-parser-vocabulary` (defer)

> **NEW observation (2026-10-19).** Documents in-window GitHub repo `acc12138-x/smart-restaurant-ai-waiter` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, **Python ✓ ON-STACK** + Flask + SQLite + LangChain + Ollama/Qwen3-4B + RAG + SSE + JWT + admin-dashboard + AI-assistant + ChartJS + Docker + github-actions + Chroma + openpyxl + pos-system + chinese + restaurant + llm + qwen, **pushed 2026-10-15T03:54:27Z AND created 2026-09-21T09:58:36Z = IN-WINDOW BY BOTH FIELDS** (~28-day-old repo with in-window `pushed_at` and `created_at`; both fields in window), **50778 KB substantial = THE LARGEST in-window brainstorm-vocabulary pick of the 81-pass series by file-size** (vs pass-80 Pick C `warpusTOM/StockWise_Group6_BT-204` 26312 KB = 1.93x larger; vs pass-78 Pick B `texas-aerosim-dev/Silica-Vault` ~11800 KB = 4.3x larger; vs pass-77 Pick B 9000 KB = 5.6x larger; the *chinese-language + Ollama-local-Qwen3-4B + 50778 KB* posture is the largest chinese-language-restaurant-LLM-waiter-repo of the 81-pass series), default_branch=`main`, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-19): *"🍜 Restaurant ordering system with an LLM-powered AI waiter. H5 QR-code ordering + dual-track intent parsing (LLM + rules) + RAG + real-time admin dashboard. Built with Flask, SQLite, Ollama/Qwen3-4B, …"*. Topics (verbatim, parent-verified, **20 topics**): `admin-dashboard, ai-assistant, chartjs, chinese, chroma, docker, flask, github-actions, jwt, langchain, llm, ollama, openpyxl, pos-system, python, qwen, rag, restaurant, sqlite, sse`. Bucket: **v2-AI (LLM-waiter-+-dual-track-intent-+-RAG-+-H5-QR-ordering-+-real-time-admin-dashboard-+-on-premise-+-Chinese-language-vocabulary)** — Pick A of Daily Brainstorm 2026-10-19. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **LLM-powered-AI-waiter + H5-QR-ordering + dual-track intent parsing (LLM + rules) + RAG + real-time admin dashboard + Flask + SQLite + Ollama/Qwen3-4B + LangChain + Chroma + SSE + JWT + admin-dashboard + chinese** vocabulary as a persistent cross-section reference for the LE31 v2-AI *LLM-waiter-as-feature* wedge, and document the **dual-track intent parsing (LLM + rules)** primitive that an independent maintainer shipped in 2026 (~28-day-old repo with in-window `created_at` AND `pushed_at`) without reading the LE31 charter. The dual-track-intent-parsing posture (rules own the canonical intent-state-machine; LLM only fires when the rule misses) IS the canonical §3.4 *LLM-as-residual-only-parser* charter invariant applied to the *AI-waiter-intent-parsing* dimension. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI *LLM-waiter-as-feature* gap-area. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **LLM-powered-AI-waiter + H5-QR-ordering + dual-track intent parsing (LLM + rules) + RAG + real-time admin dashboard + Flask + SQLite + Ollama/Qwen3-4B + LangChain + Chroma + SSE + JWT + admin-dashboard + chinese** 13-tuple-primitive: a restaurant-ordering system where the customer scans an H5 QR-code to open the menu; the order is parsed by a *dual-track intent parser* that ALWAYS tries the rule-based intent parser FIRST; the LLM (Ollama/Qwen3-4B local on-premise) only fires when the rule misses; the parsed intent is enriched by RAG over Chroma; the order flows to a Flask backend with SQLite persistence; the admin dashboard is fed by SSE for real-time updates. This is the §3.4 *chokepoint-governed + non-AI-fallback-first + observable-evidence* invariant applied to the *AI-waiter-intent-parsing* dimension.
- A written record of the **MIT + 0★/0⑨ + 50778 KB substantial = THE LARGEST + 20-topic array + Python ✓ ON-STACK + Flask + SQLite + LangChain + Ollama + Qwen3-4B + RAG + SSE + JWT + admin-dashboard + AI-assistant + ChartJS + Docker + github-actions + Chroma + openpyxl + pos-system + chinese + restaurant + llm + qwen** stack-shape: this is the **first LLM-waiter + dual-track-intent + RAG + H5-QR-ordering + real-time-admin-dashboard + on-premise + Ollama + local-Qwen3-4B + chinese-language vocabulary of the 81-pass brainstorm series**; the *dual-track intent parsing (LLM + rules)* discipline IS the canonical §3.4 *non-AI-fallback-first* invariant applied to the *LLM-as-feature* dimension; the *Ollama + local-Qwen3-4B + on-premise* posture IS the canonical §3.4 *on-premise-LLM-as-feature* invariant; the *chinese-language + RAG + Chroma* posture IS the canonical §3.7 *Chinese-cultural-context + RAG-over-Cantonese-menu* invariant.
- A written record of the **operator-facing vocabulary** discipline: the operator does not interact with the LLM directly; the operator interacts with the admin dashboard; the admin dashboard is fed by SSE; the LLM is a residual-tail-parser (charter §3.4 *non-AI-fallback-first*); the rules own the canonical intent-state-machine (charter §3.1); the RAG over Chroma is local (charter §3.7 *local-PII-minimal-bridge*); the SSE log is append-only (charter §3.3). Sister-shape to pass-80 PICK A `dashpilot-labs/dashpilot-mcp` (MCP-server-for-Delivery-Aggregator-+-POS-bridge) + features 263 + 286 + 288 + 306 + 332 + 333 + 334 — the *LLM-waiter-as-feature + dual-track-intent-parsing + RAG + H5-QR-ordering + admin-dashboard + on-premise + Ollama + local-Qwen3-4B* posture IS the canonical v2-AI *LLM-waiter-as-feature-vocabulary* applied to the *LE31-v2-AI-LLM-waiter* dimension.
- A decision record: today's verdict is `defer` because (1) the v2-AI charter has *no LLM-waiter-as-feature surface* (LE31 v2-AI is append-only-ledger + persona-charter + chokepoint-governed + human-gate, not LLM-waiter-as-feature); (2) the stack-shape match is the value, not the code (LE31 v2-AI uses Python + FastAPI + Postgres + minimal-HTML/HTMX, not Flask + Ollama + Qwen3-4B + Chroma + chinese-language); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v2-AI's planned agent-governance + audit-ledger + persona-charter surfaces.
- Adoption of the smart-restaurant-ai-waiter codebase (MIT + 0★/0⑨ + ~28-day-old repo with in-window `created_at` AND `pushed_at`).
- Cross-pollination with the v2-AI charter §3.4 *chokepoint-governed + non-AI-fallback-first + observable-evidence* posture (the *LLM-as-residual-only-parser + rules-own-canonical-intent-state-machine + Ollama-local-Qwen3-4B-on-premise* discipline IS the §3.4 invariant; the *Flask + SQLite + LangChain + Chroma + Chinese-language* posture IS OFF-§3.1 — LE31 v2-AI is FastAPI + Postgres + append-only-ledger + Italian-only, not Flask + SQLite + LangChain + Chroma + Chinese).
- Any vendor-relationship with Ollama / Qwen3-4B / Chroma / LangChain (LE31 v2-AI has no LLM-waiter surface today; v2-AI is on-agent-governance-surface).
- Cross-section candidate for v2-AI if LE31 ever adds a *LLM-waiter-as-feature* surface (charter §3.4 + §3.7 review required: the *dual-track intent parsing (LLM + rules) + Ollama + local-Qwen3-4B + RAG over Chroma* posture requires explicit §3.4 *non-AI-fallback-first* + §3.7 *local-PII-minimal-bridge* + Chinese-only market scope before any v2-AI PR).
- Cross-section candidate for v1 if LE31 ever adds an *AI-waiter-as-feature* surface (charter §3.1 + §3.2 + §3.4 + §3.7 review required: the *dual-track intent parsing + LLM-as-residual-only-parser* posture requires explicit §3.1 *rules-own-canonical-intent-state-machine* + §3.4 *non-AI-fallback-first* + §3.7 *Italian-only market + no-Chinese-cultural-context* scope before any v1 PR).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v2-AI code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "an LLM-waiter-as-feature surface with a dual-track intent parser (LLM + rules), RAG over Chroma, H5-QR-ordering, SSE-fed real-time admin dashboard, Ollama local Qwen3-4B on-premise (the rules own the canonical intent-state-machine; the LLM only fires when the rule misses)", the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "LLM-waiter + dual-track intent + RAG + H5-QR-ordering + admin-dashboard + on-premise + Ollama + local-Qwen3-4B" is a real demand signal*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same dual-track-intent-parsing + LLM-as-residual-only-parser + on-premise-LLM + Chinese-RAG posture"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `llm, ollama, qwen, rag, chroma, langchain, sqlite, flask, sse, jwt, chartjs, docker, admin-dashboard, ai-assistant, pos-system, chinese, restaurant, github-actions, openpyxl, python` + *"dual-track intent parsing (LLM + rules) + RAG + real-time admin dashboard. Built with Flask, SQLite, Ollama/Qwen3-4B, …"* + *"🍜 Restaurant ordering system with an LLM-powered AI waiter. H5 QR-code ordering"*).
- **Confidence**: medium-high for the vocabulary match (the verbatim description + topics name the 13-tuple-primitive set + the dual-track-intent-parsing posture + the LLM-as-residual-only-parser posture + the on-premise-Ollama-Qwen3-4B posture + the RAG-over-Chroma posture + the SSE-fed-admin-dashboard posture + the H5-QR-ordering posture + the chinese-language posture); low for transferability (LE31 v2-AI has no LLM-waiter-as-feature surface today; an LLM-waiter is OFF-§3.1 + §3.4 unless explicit charter-decision is made).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v2-AI has no LLM-waiter surface; today the LE31 waiter is HTMX-driven + aiogram-cook-bot-driven; the v1 waiter is *non-LLM*, *Italian-only*, *HTMX-only*); the value is the *dual-track-intent-parsing + LLM-as-residual-only-parser + on-premise-Ollama-Qwen3-4B + RAG-over-Chroma + SSE-fed-admin-dashboard + H5-QR-ordering + chinese-language* vocabulary — when the first v2-AI PR that adopts an LLM-waiter-as-feature lands (with §3.4 *non-AI-fallback-first* + §3.7 *local-PII-minimal-bridge* + Italian-only market scope), the smart-restaurant-ai-waiter pattern is a ready-made *named primitive*.

## Description

GitHub `acc12138-x/smart-restaurant-ai-waiter` (MIT, 0★/0⑨, Python, pushed 2026-10-15T03:54:27Z, created 2026-09-21T09:58:36Z, 50778 KB substantial = THE LARGEST in-window brainstorm-vocabulary pick of the 81-pass series by file-size, default_branch=`main`, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-19): *"🍜 Restaurant ordering system with an LLM-powered AI waiter. H5 QR-code ordering + dual-track intent parsing (LLM + rules) + RAG + real-time admin dashboard. Built with Flask, SQLite, Ollama/Qwen3-4B, …"*.

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **LLM-powered-AI-waiter** — the AI-waiter replaces the human waiter for *intent parsing* (the customer says "I'd like a Margherita pizza and a Coke" → the AI-waiter parses the intent into structured-order-items). The *LLM-powered-AI-waiter* primitive maps 1:1 onto any future v2-AI surface that needs an *LLM-as-feature-as-waiter*.
2. **H5-QR-ordering** — the customer scans a QR code to open the menu in their mobile browser (H5 = HTML5 mobile-web). The *H5-QR-ordering* primitive maps 1:1 onto any future v2-AI surface that needs a *customer-facing-mobile-ordering surface*.
3. **Dual-track intent parsing (LLM + rules)** — the rule-based intent parser is ALWAYS tried FIRST; the LLM only fires when the rule misses. The *dual-track intent parsing (LLM + rules)* primitive IS the canonical §3.4 *non-AI-fallback-first* + §3.1 *rules-own-canonical-intent-state-machine* charter invariant applied to the *LLM-as-feature-as-waiter* dimension. This is the **UNIQUE vocabulary primitive of the 81-pass series** — never before seen in any prior pick.
4. **RAG over Chroma** — the parsed intent is enriched by Retrieval-Augmented Generation over a Chroma vector database of menu items, dietary-restrictions, restaurant-style guidelines, etc. The *RAG over Chroma* primitive IS the canonical §3.7 *RAG-as-restaurant-context-window* invariant applied to the *LLM-as-feature-as-waiter* dimension.
5. **Real-time admin dashboard** — the operator (kitchen + manager) sees the orders in real-time via an admin dashboard fed by SSE (server-sent events). The *real-time admin dashboard* primitive IS the canonical §3.3 *append-only-event-log* + §3.4 *observable-evidence* charter invariant applied to the *real-time-ordering-surface* dimension.
6. **Flask + SQLite** — the backend is Flask (Python micro-framework) with SQLite for local persistence. The *Flask + SQLite* posture IS OFF-§3.1 — LE31 v2-AI is FastAPI + Postgres, not Flask + SQLite; explicit charter-decision needed for any v2-AI PR that adopts this stack-shape.
7. **Ollama + local Qwen3-4B** — the LLM is local (on-premise via Ollama) and uses Qwen3-4B (a Chinese-language-tuned small-LLM). The *Ollama + local-Qwen3-4B* posture IS the canonical §3.4 *on-premise-LLM-as-feature* charter invariant (the LLM does not call out to a remote API; the LLM runs locally on the operator's hardware).
8. **LangChain** — the LLM orchestration is via LangChain. The *LangChain* posture IS OFF-§3.4 — LangChain is a complex-multi-LLM-orchestration-framework that introduces *implicit-state-machines* via chain-of-thought; LE31 v2-AI is *explicit-state-machine* per §3.1; explicit charter-decision needed for any v2-AI PR that adopts LangChain.
9. **SSE** — the admin dashboard is fed by server-sent events for real-time updates. The *SSE* posture IS the canonical §3.4 *observable-evidence* invariant.
10. **JWT** — the admin dashboard is auth-gated by JWT. The *JWT* posture IS the canonical §3.7 *minimal-PII-only-auth-bridge* invariant.
11. **ChartJS** — the admin dashboard uses ChartJS for charts. The *ChartJS* posture is UI-only; OFF-§3.1 unless explicitly named in the v2-AI charter.
12. **Docker** — the system is containerized via Docker. The *Docker* posture IS the canonical *single-binary-deploy* invariant for v2-AI.
13. **Chinese-language + RAG** — the menu + restaurant-context is in Chinese. The *chinese-language + RAG* posture IS OFF-§3.1 — LE31 is Italian-only; explicit charter-decision needed for any v2-AI PR that adopts the *Chinese-language + RAG* posture.

The defer artifact retains the **13-tuple-primitive** (LLM-powered-AI-waiter + H5-QR-ordering + dual-track intent parsing (LLM + rules) + RAG + real-time admin dashboard + Flask + SQLite + Ollama/Qwen3-4B + LangChain + SSE + JWT + ChartJS + Docker + Chinese-language) as a persistent cross-section reference.

## Data model

None today. The defer artifact is documentation only.

When the first v2-AI PR that adopts the *dual-track-intent-parsing + LLM-as-residual-only-parser + Ollama + local-Qwen3-4B + RAG over Chroma* discipline lands, the data model is:

```python
# hypothetical future v2-AI surface (NOT IMPLEMENTED TODAY)
# Local SQLite (RAG-over-Chroma; SSE-fed admin dashboard)

class IntentRuleParser:
    """Rule-based intent parser. ALWAYS tried FIRST.
    
    Charter §3.1: rules own the canonical intent-state-machine.
    Charter §3.4: non-AI-fallback-first — LLM only fires on rule-miss.
    """
    
    def parse(self, text: str) -> Intent | None:
        # Try regex + lookup-table rules first
        for rule in self.rules:
            if match := rule.match(text):
                return Intent(...)
        return None  # Rule miss — LLM fallback


class IntentLLMParser:
    """LLM-based intent parser. ONLY fires when IntentRuleParser returns None.
    
    Charter §3.4: LLM-as-residual-only-parser.
    Charter §3.1: rules own the canonical intent-state-machine.
    Charter §3.4: on-premise Ollama + local Qwen3-4B (no remote API).
    """
    
    def __init__(self, ollama_client, chroma_client):
        self.ollama = ollama_client  # Ollama local LLM
        self.chroma = chroma_client  # Chroma RAG
    
    async def parse(self, text: str, menu_chroma: chroma.Collection) -> Intent:
        # RAG over Chroma for menu context
        context_docs = menu_chroma.query(text, n_results=3)
        # Ollama local Qwen3-4B for intent parsing
        prompt = f"Parse: {text}\nMenu: {context_docs}"
        response = await self.ollama.generate(model="qwen3-4b", prompt=prompt)
        return Intent.parse(response)


class DualTrackIntentParser:
    """The dual-track intent parser.
    
    Charter §3.1: rules own the canonical intent-state-machine.
    Charter §3.4: LLM is residual-only; rules-first.
    Charter §3.7: RAG-over-Chroma for restaurant-context-window.
    """
    
    def __init__(self, rules: IntentRuleParser, llm: IntentLLMParser):
        self.rules = rules
        self.llm = llm
    
    async def parse(self, text: str, menu_chroma: chroma.Collection) -> Intent:
        # 1. Try rules FIRST (charter §3.4 non-AI-fallback-first)
        if intent := self.rules.parse(text):
            return intent
        # 2. LLM fallback (charter §3.4 LLM-as-residual-only-parser)
        return await self.llm.parse(text, menu_chroma)
```

## Implementation steps

None today. The defer artifact is documentation only.

When the first v2-AI PR that adopts the *dual-track-intent-parsing + LLM-as-residual-only-parser + Ollama + local-Qwen3-4B + RAG over Chroma* discipline lands, the implementation steps are:

1. Add an `IntentRuleParser` to the LE31 v2-AI codebase (charter §3.1 rules-own-canonical-intent-state-machine).
2. Add an `IntentLLMParser` to the LE31 v2-AI codebase using Ollama + local Qwen3-4B (charter §3.4 on-premise-LLM-as-feature + non-AI-fallback-first).
3. Add a `DualTrackIntentParser` to the LE31 v2-AI codebase that ALWAYS tries rules FIRST and only fires the LLM on rule-miss (charter §3.4 LLM-as-residual-only-parser).
4. Add a `menu_chroma` Chroma collection for RAG over menu items + restaurant-context (charter §3.7 RAG-as-restaurant-context-window).
5. Add a SSE-fed admin dashboard that surfaces real-time orders to the operator (charter §3.3 + §3.4 observable-evidence).
6. Add a JWT auth-gate to the admin dashboard (charter §3.7 minimal-PII-only-auth-bridge).
7. Containerize the system via Docker for *single-binary-deploy* (charter §3.4).
8. Update the v2-AI charter to explicitly authorize Italian-only market scope (the smart-restaurant-ai-waiter is chinese-language-tuned; the LE31 charter is Italian-only).

## Telegram interaction

None today. The defer artifact is documentation only.

When the first v2-AI PR that adopts the *dual-track-intent-parsing + LLM-as-residual-only-parser + Ollama + local-Qwen3-4B + RAG over Chroma* discipline lands, the Telegram interaction is:

- The cook receives the order via the existing aiogram-driven-cook-bot (charter §3.1 cook-bot-driven).
- The admin receives real-time updates via the SSE-fed admin dashboard (charter §3.4 + §3.7).
- The LLM-driven AI-waiter interactively takes the customer's order via the H5-QR-ordering surface (charter §3.7 customer-facing-H5-QR).

The Telegram bot is *not* the customer-facing surface in this discipline; the Telegram bot is the cook-facing surface. The H5-QR-ordering surface is the customer-facing surface.

## Dependencies

- Charter §3.4 *on-premise-LLM-as-feature* review (Ollama + local Qwen3-4B)
- Charter §3.4 *non-AI-fallback-first* review (rules own the canonical intent-state-machine)
- Charter §3.7 *RAG-as-restaurant-context-window* review (Chroma over menu + restaurant-context)
- Charter §3.7 *Italian-only-market-scope* review (the smart-restaurant-ai-waiter is chinese-language-tuned; LE31 is Italian-only charter)
- Charter §3.2 STRICTLY-COMPATIBLE review (MIT permissive — STRICTLY-COMPATIBLE)
- LangChain OFF-§3.4 review (LangChain is a *complex-multi-LLM-orchestration-framework* that introduces *implicit-state-machines*; LE31 v2-AI is *explicit-state-machine* per §3.1; explicit charter-decision needed)
- Flask OFF-§3.1 review (Flask + SQLite; LE31 v2-AI is FastAPI + Postgres; explicit charter-decision needed)
- Docker ON-§3.4 review (single-binary-deploy posture is portable)

## Open questions

- Does the *Ollama + local Qwen3-4B* discipline map onto LE31 v2-AI's *on-premise-LLM-as-feature* surface? Charter §3.4 review needed.
- Does the *dual-track intent parsing (LLM + rules)* discipline map onto LE31 v2-AI's *LLM-as-residual-only-parser* surface? Charter §3.4 review needed.
- Does the *RAG over Chroma* discipline map onto LE31 v2-AI's *RAG-as-restaurant-context-window* surface? Charter §3.7 review needed.
- Does the *H5-QR-ordering* discipline map onto LE31 v2-AI's *customer-facing-mobile-ordering* surface? Charter §3.7 review needed.
- Does the *SSE-fed real-time admin dashboard* discipline map onto LE31 v2-AI's *operator-facing-control-of-AI-agents* surface? Charter §3.4 + §3.7 review needed.
- Does the *Chinese-language + RAG* posture map onto LE31 v2-AI's *Italian-only market scope*? Explicit charter-decision needed (LE31 is Italian-only charter today; the smart-restaurant-ai-waiter is chinese-language-tuned).
- Does the *LangChain* posture map onto LE31 v2-AI's *explicit-state-machine*? Charter §3.1 review needed (LangChain is a *complex-multi-LLM-orchestration-framework* that introduces *implicit-state-machines*).
- Does the *Flask + SQLite* posture map onto LE31 v2-AI's *FastAPI + Postgres* posture? Charter §3.1 review needed (the stack-shape is OFF-§3.1 unless explicitly named in the v2-AI charter).

## Why this matters

The **dual-track intent parsing (LLM + rules)** posture is the **unique vocabulary primitive of the 81-pass series** — never before seen in any prior pick. The *rules-own-the-canonical-intent-state-machine* + *LLM-only-fires-on-rule-miss* discipline IS the canonical §3.4 *non-AI-fallback-first* charter invariant applied to the *LLM-as-feature* dimension. Today LE31 v2-AI has no LLM-waiter-as-feature surface; when the first v2-AI PR that adopts an LLM-waiter-as-feature lands (with §3.4 *non-AI-fallback-first* + §3.7 *local-PII-minimal-bridge* + Italian-only market scope), the smart-restaurant-ai-waiter pattern is a ready-made *named primitive*.

The transferable vocabulary of this artifact:
1. **Dual-track intent parsing (LLM + rules)** — rules first, LLM as residual-only fallback; charter §3.4 + §3.1 invariant.
2. **Ollama + local Qwen3-4B** — on-premise-LLM-as-feature; charter §3.4 invariant.
3. **RAG over Chroma** — RAG-as-restaurant-context-window; charter §3.7 invariant.
4. **H5-QR-ordering** — customer-facing-mobile-ordering; charter §3.7 invariant.
5. **SSE-fed admin dashboard** — observable-evidence; charter §3.3 + §3.4 invariant.
6. **JWT auth-gate** — minimal-PII-only-auth-bridge; charter §3.7 invariant.
7. **Docker single-binary-deploy** — single-binary-deploy posture; charter §3.4 invariant.

The NOT-portable vocabulary of this artifact (explicit charter-decision needed for any v2-AI PR):
1. **Flask + SQLite** — OFF-§3.1; LE31 v2-AI is FastAPI + Postgres.
2. **LangChain** — OFF-§3.4; LangChain introduces *implicit-state-machines*.
3. **Chinese-language + RAG** — OFF-§3.1; LE31 is Italian-only charter.

This artifact is **defer, vocabulary-only, parking-lot**; zero build time today; the *demand-signal* is the value, not the code-adoption opportunity.
