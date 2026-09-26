# Feature 234 — `narumiruna-gurume-mit-python-cli-tui-mcp-server-japanese-restaurant-tabelog-search-agent-skills-fastmcp-v2-ai-mcp-cli-tui-operator-tooling-vocabulary` (defer)

> **NEW observation (2026-09-26).** Documents in-window GitHub Search `restaurant+language:python` query result: `narumiruna/gurume` (**MIT ✓**, **8★/2⑂**, Python, **pushed 2026-09-24T03:10:03Z** (in-window by `pushed_at` — *2 days before fetch time*; recent), **created 2025-08-21T12:14:46Z** (~13-month-old repo with in-window `pushed_at`; **IN-WINDOW BY PUSH ONLY**; `created_at` is OUT-OF-WINDOW by ~12 months), **2203 KB** modest repo, default_branch=`main`). Topics (verbatim from raw JSON, **10 topics**): `agent-skills`, `cli`, `fastmcp`, `food-search`, `mcp`, `python`, `restaurants`, `skills`, `tabelog`, `tui`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-26): *"Python CLI, TUI, and MCP server for searching Japanese restaurants on Tabelog"*. **The only 2026-09-26 in-window v2-AI MCP/CLI/TUI operator-tooling-vocabulary-reference that pins all 7 of `agent-skills + cli + fastmcp + mcp + python + restaurants + skills` in the topic array** = **7/10 LE31-relevant topics** = **the first v2-AI MCP/CLI/TUI vocabulary of the 58-pass series**. Bucket: **v2-AI MCP/CLI/TUI operator-tooling-vocabulary-reference (defer, parking-lot)** — watch-list entry, zero build time today. **HONEST DISCLOSURE**: the *tabelog + food-search + restaurants* surface is **off-pattern for LE31 v1's restaurant-vertical posture** per charter §3.1 (*"one small restaurant"* = ops, not discovery); the pick is filed as a **vocabulary reference for the MCP + CLI + TUI + agent-skills primitives**, NOT as a v1 or v2 surface that LE31 would adopt wholesale; the *agent-skills + mcp + fastmcp + cli + tui* primitive cluster is the *operator-tooling-AI* posture — §3.4 NOT triggered because the AI surface is operator-tooling not customer-facing.

## Goal

Retain the **"Python CLI, TUI, and MCP server for searching Japanese restaurants on Tabelog"** + **"agent-skills + cli + fastmcp + mcp + python + restaurants + skills + tabelog + tui + food-search"** decuple-primitive as a persistent v2-AI operator-tooling-vocabulary-reference for any future LE31 v2 maintainer asking the *MCP-server-as-FastAPI-app + CLI + TUI + agent-skills-as-package + operator-tooling-AI-not-customer-facing-AI* question (does LE31 v2 expose `audit_logs` + `StockEntry` + `MenuItem` + `Order` to MCP-aware AI tools? does LE31 v2 introduce a CLI for owner workflows? does LE31 v2 introduce a TUI for keyboard-driven owner workflows? does LE31 v2 adopt FastMCP as the MCP-server framework?). The artifact is the persistent *CLI + TUI + MCP + agent-skills + fastmcp + operator-tooling-AI* vocabulary as a *named* v2-AI operator-tooling reference. No code today (MIT license permits future code reuse; vocabulary-only artifact today; 2203 KB modest-repo size makes source-code inspection feasible for the v2 maintainer).

## Scope

**In scope (defer artifact):**
- A written record of the **MCP + fastmcp + agent-skills + skills** discipline: the *MCP-server-as-FastAPI-app + agent-skills-as-package* primitive (the *fastmcp* topic explicitly names the *FastMCP-server-framework* primitive — a *MCP-server-as-FastAPI-app* pattern is the standard way to expose Python services to MCP-aware AI tools; the *agent-skills + skills* topic explicitly names the *AI-agent-skills-as-discrete-package* primitive — the *AI-skill-as-package* discipline is the v2 charter §3.4 *observable-evidence + non-AI-fallback* pattern documented in features 121 + 122 + 190 + 220; gurume uses *agent-skills* in the CLI/TUI/MCP-server context which is the *operator-tooling-AI* posture — §3.4 NOT triggered).
- A written record of the **CLI + TUI + python** discipline: the *CLI + TUI + Python* primitive (the *CLI* posture IS the *command-line-interface-as-operator-UX* alternative to web-UI; the *TUI* posture IS the *terminal-UI-as-secondary-operator-surface* discipline; the *python* topic explicitly names the *Python-first stack* posture that matches LE31 v1's Python 3.13 stack per charter §3.2).
- A written record of the **restaurants + tabelog + food-search** discipline: the *restaurant-domain-data-source* primitive (LE31 v1 has no third-party-data-source dependency today; the *restaurants + tabelog + food-search* triplet is the *third-party-restaurant-data-source* vocabulary that LE31 v2 may or may not adopt; the *tabelog + food-search + restaurants* surface is off-pattern for v1's European-restaurant posture per charter §3.1 but the *restaurant-search-as-tool* discipline is informative for any v2 surface that introduces an owner-facing-restaurant-discovery surface).
- A cross-section reference with the prior CLI + TUI + MCP + agent-skills + small-business cluster: features 102 (`nightmux-stdlib-telegram-bridge`) + 117 (`nematjon555-telegram-restaurant-bot-watch`) + 190 (`ilyautov/small-business-ru` operator-AI owner-assist) + 222 (`donbarbos/telegram-bot-template` aiogram-cook-bot-deployment-blueprint) + 224 (`celerp/celerp` self-hosted-FastAPI-ERP-vocabulary) + 226 (`ficilcom/bootstrap-startup-skills` v2 bootstrap-finance-vocabulary). The *transferable insight* is the **MCP + fastmcp + CLI + TUI + agent-skills + skills + operator-tooling-AI-not-customer-facing-AI** septuple-primitive.
- A decision record: today's verdict is `defer (parking-lot)` because (a) LE31 v1 has no MCP-server surface today (charter §3.1 *single-restaurant-vertical* discipline + charter §3.4 *no-customer-facing-AI* discipline + charter §3.4 *AI-may-assist-owner-with-observable-evidence* posture); (b) the *tabelog + food-search + restaurants* surface is off-pattern for v1's European-restaurant posture; (c) the *MCP + fastmcp + CLI + TUI + agent-skills* primitives are *forward-looking* primitives that LE31 v2 may adopt when (or if) it introduces an *owner-assist AI tool surface*.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Adoption of gurume's source code as a v2 dependency (gurume's *tabelog + food-search* surface is Japanese-market-restaurant-discovery-specific; the *MCP + fastmcp + CLI + TUI + agent-skills* primitives would need to be independently re-implemented and validated against LE31's existing FastAPI + uvicorn + aiogram v3 stack, not simply imported). The cross-section is *primitive vocabulary extension + architecture-reference*, not *library adoption*.
- Any third-party-data-source dependency (charter §3.1 *single-restaurant-vertical* discipline: LE31 v1 has no Tabelog-equivalent dependency today).

## Description

`narumiruna/gurume` is a 2203 KB Python repository that exposes Japanese restaurant search via three surface types: **CLI** (command-line interface), **TUI** (terminal user interface), and **MCP server** (Model Context Protocol server for AI-tool consumption). The framework's design philosophy is *operator-tooling-AI not customer-facing-AI*: the CLI/TUI/MCP-server surfaces are *operator-facing* (the *operator-tooling-AI* posture — §3.4 NOT triggered). The 10-topic array includes `agent-skills + cli + fastmcp + food-search + mcp + python + restaurants + skills + tabelog + tui`; the *mcp + fastmcp* pair is the *MCP-server-as-FastAPI-app* primitive; the *agent-skills + skills* pair is the *AI-agent-skills-as-discrete-package* primitive; the *cli + tui* pair is the *command-line + terminal-UI* operator-UX primitive. The MCP surface is the most-recently-added operator-tooling pattern of 2026 (LE31 v2 may adopt FastMCP as the MCP-server framework when introducing an owner-assist surface).

## Data model

N/A (defer artifact; vocabulary-only; no schema change). If a future v2 PR adopts the gurume *MCP-server-as-FastAPI-app* primitive for owner-assist, the data-model impact would be a `McpServer` SQLModel table + a `McpTool` SQLModel table mapping MCP tool names to underlying `audit_logs` / `StockEntry` / `MenuItem` / `Order` queries, not a new SQLModel table for the *underlying* LE31 v1 data model.

## Implementation steps

N/A (defer artifact; zero build time today). If a future v2 PR adopts the gurume *MCP-server-as-FastAPI-app* primitive, the implementation steps would be:
1. Add `fastmcp` to v2's `pyproject.toml` as an optional dependency.
2. Create `app/mcp_server/__init__.py` with a `Le31McpServer` class extending FastMCP.
3. Register 3-5 MCP tools: `audit_logs.query(start, end, user_id)`, `stock_entry.list(item_id, start, end)`, `order.status(order_id)`, `menu.list()`, `staff.shift_summary(date)`.
4. Add `le31-mcp` console-script entrypoint in `pyproject.toml`.
5. Add a CLI subcommand `le31-cli` using Click + Rich for keyboard-driven owner workflows.
6. Test end-to-end: external AI tool (e.g. Claude Desktop or Cline) connects to `le31-mcp` MCP server via stdio → AI tool calls `stock_entry.list(item_id=42, start=2026-09-01, end=2026-09-26)` → receives JSON list of stock entries.

## Telegram interaction

N/A (defer artifact; no Telegram surface change). The gurume *MCP + CLI + TUI* primitive extends a *future v2 operator-tooling surface*, not the cook-bot surface; the cook-bot's `aiogram v3` Telegram-send flow is unchanged.

## Dependencies

**Existing LE31 v1 dependencies (unchanged):** Python 3.13, FastAPI, SQLModel, aiogram v3, uvicorn, Postgres.
**New v2 dependencies (if adopted):** `fastmcp` (MCP-server framework) + `click` (CLI framework) + `rich` (terminal-UI framework) + `textual` (TUI framework) — all optional v2 dependencies, not v1 dependencies.

## Open questions

- **Open question 1 (may kill any future PR)**: does LE31 v2 actually need an MCP-server surface? The MCP-server primitive is a *forward-looking* v2 surface that LE31 v2 may adopt when (or if) it introduces an *owner-assist AI tool surface*; today LE31 v1 has no owner-assist AI tool surface.
- **Open question 2 (may kill any future PR)**: does LE31 v2 actually need a CLI for owner workflows? The owner-today uses a web UI for everything; a CLI is a *nice-to-have* for keyboard-driven workflows, not a *must-have*.
- **Open question 3 (may kill any future PR)**: does LE31 v2 actually need a TUI for owner workflows? A TUI is a *terminal-UI-as-secondary-operator-surface* primitive; today's owner uses a web UI for everything; a TUI is a *nice-to-have* for low-effort-keyboard-driven workflows, not a *must-have*.
- **Open question 4 (architecture reference only)**: does LE31 v2 adopt gurume's source code as a v2 dependency, or independently re-implement the *MCP + CLI + TUI + agent-skills* primitives against LE31's existing FastAPI + uvicorn + aiogram v3 stack? Recommendation: independently re-implement (gurume's *tabelog + food-search* surface is Japanese-market-restaurant-discovery-specific; the *MCP + fastmcp + CLI + TUI + agent-skills* primitives are small enough to re-implement in <500 LOC across MCP-server + CLI + TUI).

## Why this matters

The **MCP + fastmcp + CLI + TUI + agent-skills + skills + operator-tooling-AI-not-customer-facing-AI** septuple-primitive is the **first v2-AI MCP/CLI/TUI operator-tooling vocabulary of the 58-pass series**. The *mcp + fastmcp* pair is the *MCP-server-as-FastAPI-app* primitive that any LE31 v2 owner-assist MCP-server surface would need to inherit (FastMCP is the *de-facto* standard MCP-server framework for Python 2026). The *agent-skills + skills* pair is the *AI-agent-skills-as-discrete-package* primitive that maps onto LE31 v2's charter §3.4 *AI-skill-as-package* discipline (each MCP tool is a *discrete AI-skill* that the owner-facing-AI-tool can invoke; the *non-AI-fallback* is the underlying CLI/TUI that works without the AI layer). The *CLI + TUI* pair is the *command-line + terminal-UI* operator-UX primitive that LE31 v2 may adopt for keyboard-driven owner workflows. The *operator-tooling-AI-not-customer-facing-AI* posture is the load-bearing §3.4 finding (the AI surface is in the *operator-tooling layer* per charter §3.4 *"AI may assist owner/staff, with observable evidence and a non-AI fallback"*; the *non-AI-fallback* is the CLI/TUI that works without the AI layer; the *observable-evidence* is the JSON output of each MCP tool call). The gurume pattern is the *future-v2-AI-architecture-vocabulary* for LE31 v2's owner-tooling-evolution.

**Fully reversible** (vocabulary-only artifact). Trigger condition = first v2-AI PR that exposes LE31's `audit_logs` or `StockEntry` via an MCP server surface (e.g. a `le31-mcp-server` Python package + FastMCP app + 3-5 MCP tools for `audit_logs.query`, `stock_entry.list`, `order.status`, `menu.list`, `staff.shift_summary`), or first v2 PR that adopts a *CLI + TUI* primitive for keyboard-driven owner workflows (e.g. a `le31-cli` Python package + Click + Rich + Textual).
