# HANDOFF: feature 234 — `narumiruna/gurume` (v2-AI MCP/CLI/TUI operator-tooling-vocabulary, defer parking-lot)

> **Date filed:** 2026-09-26
> **Author:** Daily Brainstorm Cron (LE31) — parent-verified pick
> **Parent research issue:** [linear: blocked — see /opt/data/le31-brainstorm-2026-09-26.linear-fallback.json]
> **Bucket:** v2-AI operator-tooling-vocabulary-reference (parking-lot, future-v2-AI-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE** — permissive
> **Reference URL:** https://github.com/narumiruna/gurume
> **Reference data:** MIT, 8★/2⑂, Python, 2203 KB modest repo, pushed 2026-09-24T03:10:03Z (in-window by `pushed_at` only), created 2025-08-21T12:14:46Z (OUT-OF-WINDOW by ~12 months); **7/10 topics LE31-relevant = the first v2-AI MCP/CLI/TUI vocabulary of the 58-pass series**
> **HONEST DISCLOSURE:** the *tabelog + food-search + restaurants* surface is **off-pattern for LE31 v1's restaurant-vertical posture** per charter §3.1 (*"one small restaurant"* = ops, not discovery); the pick is filed as a **vocabulary reference for the MCP + CLI + TUI + agent-skills primitives**, NOT as a v1 or v2 surface that LE31 would adopt wholesale.

## Active feature path

`features/234-narumiruna-gurume-mit-python-cli-tui-mcp-server-japanese-restaurant-tabelog-search-agent-skills-fastmcp-v2-ai-mcp-cli-tui-operator-tooling-vocabulary.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When LE31 v2 introduces an owner-assist AI tool surface (e.g. an LLM agent that can query the daily stock summary or audit a specific order), the maintainer wants a named vocabulary for MCP-server-as-FastAPI-app + CLI + TUI + agent-skills-as-package, but today no LE31 feature documents the pattern, so that v2 owner-assist can adopt the primitives without reinventing them.* Maps onto charter §3.1 + §3.4. |
| 2 | Viability | ✅ | MIT permissive; 8★ community adoption; 2203 KB modest repo. |
| 3 | Practicability | ✅ | Python; *MCP + fastmcp + CLI + TUI + agent-skills* primitives directly transferable to LE31's FastAPI + uvicorn + aiogram v3 stack; FastMCP is the *de-facto* standard MCP-server framework for Python 2026. |
| 4 | Conflict | none | MIT permissive; the *agent-skills + mcp + fastmcp + cli + tui* primitive cluster is the *operator-tooling-AI* posture — §3.4 NOT triggered because the AI surface is operator-tooling not customer-facing. |
| 5 | Outcome / appetite / scope | ✅ v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Modest ingest (2203 KB); vocabulary-only artifact; zero ongoing maintenance. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v2-AI build-trigger. The 10 named topics + the verbatim description + the 7 named primitives are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/234-narumiruna-gurume-...md` (the vocabulary contract; READ for context)
  - `specs/234-narumiruna-gurume-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (vocabulary = inferred from the description + 10 topics + 7 named primitives; confidence medium-high for vocabulary transferability)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; stars + topics + description all verbatim)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/234-*.md` + this HANDOFF file `specs/234-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `le31-mcp-server` Python package + FastMCP app; (2) drop the 3-5 MCP tools (`audit_logs.query`, `stock_entry.list`, `order.status`, `menu.list`, `staff.shift_summary`); (3) drop the `le31-cli` Click + Rich console-script entrypoint; (4) drop the `le31-tui` Textual app. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

The external coding agent must load these skills before acting on this handoff:
- `le31-conventions` (global decision layer; verifies the seven-check gate)
- `le31-feature-pipeline` (turns the proposal into ready-to-build artefacts)
- `le31-v1-feature-pattern` (v1 feature template + pattern library)
- `le31-handoff-spec` (packages the decision into a frozen build contract)
- `le31-coding-agent-brief` (produces the paste-in prompt automatically from the slice contract)
- `development` (router for all coding work; decides process and next skill)
- `speckit-specify` (captures what/why for a feature before any code or plan)

## Trigger policy

Do NOT implement today. The artifact is a vocabulary-only reference; any future implementation must re-run the seven-check gate and re-verify the v2 stack-invariant posture (charter §3.4 *operator-tooling-AI-not-customer-facing-AI* + charter §3.1 *single-restaurant-vertical* + charter §3.2 *MIT-permissive*). Trigger condition = first v2-AI PR that exposes LE31's `audit_logs` or `StockEntry` via an MCP server surface (e.g. a `le31-mcp-server` Python package + FastMCP app + 3-5 MCP tools for `audit_logs.query`, `stock_entry.list`, `order.status`, `menu.list`, `staff.shift_summary`), or first v2 PR that adopts a *CLI + TUI* primitive for keyboard-driven owner workflows (e.g. a `le31-cli` Python package + Click + Rich + Textual).

## Distinct from existing features

The gurume vocabulary is **distinct from features 102 (`nightmux-stdlib-telegram-bridge`) + 117 (`nematjon555-telegram-restaurant-bot-watch`) + 190 (`ilyautov/small-business-ru`) + 222 (`donbarbos/telegram-bot-template`) + 224 (`celerp/celerp`)** because gurume is the *only one that pins MCP + fastmcp + CLI + TUI + agent-skills simultaneously* = the *first v2-AI MCP/CLI/TUI vocabulary reference of the 58-pass series*. The existing features cover subsets of these primitives (Telegram-bridge + Telegram-bot-template cover CLI-side; small-business-ru covers agent-skills; celerp covers FastAPI-ERP-vocabulary); gurume combines them all into a single named framework.
