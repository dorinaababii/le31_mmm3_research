# HANDOFF: feature 235 — `maojiebc/majia-huiyuan` (v2-AI owner-analytics-vocabulary, defer parking-lot)

> **Date filed:** 2026-09-26
> **Author:** Daily Brainstorm Cron (LE31) — parent-verified pick
> **Parent research issue:** [linear: blocked — see /opt/data/le31-brainstorm-2026-09-26.linear-fallback.json]
> **Bucket:** v2-AI owner-analytics-vocabulary-reference (parking-lot, future-v2-AI-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE** — permissive
> **Reference URL:** https://github.com/maojiebc/majia-huiyuan
> **Reference data:** MIT, 12★/2⑂ (the most-starred of today's 3 picks), Python, 11001 KB substantial repo, pushed 2026-09-14T03:55:14Z (in-window by `pushed_at` only), created 2026-07-11T17:13:08Z (OUT-OF-WINDOW by ~6 weeks); **8/12 topics LE31-relevant = the first v2-AI owner-analytics-vocabulary of the 58-pass series**
> **HONEST DISCLOSURE:** the *chinese + crm + guandata + workbuddy* surface is **off-pattern for LE31 v1's European-restaurant posture** per charter §3.1 (single-restaurant, France, EUR, Paris timezone); the pick is filed as a **vocabulary reference for the BI + data-warehouse + membership + agent-skills + llm-friendly primitives**, NOT as a v1 or v2 surface that LE31 would adopt wholesale.

## Active feature path

`features/235-maojiebc-majia-huiyuan-mit-bi-data-warehouse-membership-restaurant-retail-agent-skills-llm-friendly-chinese-v2-ai-owner-analytics-vocabulary-reference.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When LE31 v2 introduces an owner-analytics surface (e.g. a daily-P&L dashboard, a membership-loyalty surface, a weekly-business-review workflow), the maintainer wants a named vocabulary for BI + data-warehouse + membership + LLM-friendly-analytics, but today no LE31 feature documents the pattern, so that v2 owner-analytics can adopt the primitives without reinventing them.* Maps onto charter §3.1 + §3.2 + §3.4. |
| 2 | Viability | ✅ | MIT permissive; 12★ community adoption; 11001 KB substantial repo. |
| 3 | Practicability | ✅ | Python; *data-warehouse-as-derived-tables-from-StockEntry* primitive directly transferable to LE31's existing SQLModel + Postgres stack; charter §3.1's *append-only-StockEntry-ledger* discipline maps directly onto a *derived-tables-from-StockEntry* pattern. |
| 4 | Conflict | none | MIT permissive; the *agent-skills + llm-friendly* primitive cluster is the *owner-analytics-AI* posture — §3.4 NOT triggered because the AI surface is owner-analytics not customer-facing. |
| 5 | Outcome / appetite / scope | ✅ v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Substantial ingest (11001 KB); vocabulary-only artifact; zero ongoing maintenance. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v2-AI build-trigger. The 12 named topics + the verbatim description + the 8 named primitives are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/235-maojiebc-majia-huiyuan-...md` (the vocabulary contract; READ for context)
  - `specs/235-maojiebc-majia-huiyuan-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (vocabulary = inferred from the description + 12 topics + 8 named primitives; confidence medium-high for vocabulary transferability)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; stars + topics + description all verbatim)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/235-*.md` + this HANDOFF file `specs/235-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `daily_pnl` + `membership_metrics` + `coupon_batch` + `stored_value_analytics` derived views; (2) drop the `GET /analytics/daily-pnl` + `GET /analytics/membership/{member_id}` FastAPI endpoints; (3) drop the LLM-friendly JSON export endpoints. All future rollbacks are explicit because the artifact is read-only.

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

Do NOT implement today. The artifact is a vocabulary-only reference; any future implementation must re-run the seven-check gate and re-verify the v2 stack-invariant posture (charter §3.1 *append-only-StockEntry-ledger* discipline preserved; charter §3.2 *MIT-permissive*; charter §3.4 *owner-analytics-AI-not-customer-facing-AI*). Trigger condition = first v2-AI PR that introduces an owner-analytics surface (e.g. a `daily_pnl` derived view from `StockEntry` + a `membership_metrics` derived view from a future `CustomerVisit` table + a `coupon_batch` derived view from a future `Discount` table + a `stored_value_analytics` derived view from a future `StoredValueTransaction` table + LLM-friendly JSON export endpoints for owner AI-assist queries).

## Distinct from existing features

The majia-huiyuan vocabulary is **distinct from features 158 (`azizsekerdil-smart-restaurant-management-system`) + 190 (`ilyautov/small-business-ru`) + 195 (`skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management`) + 203 (`shawn-durrani/membro`) + 224 (`celerp/celerp`) + 225 (`anugrhaswi-shop-ledger`) + 226 (`ficilcom/bootstrap-startup-skills`)** because majia-huiyuan is the *only one that pins BI + data-warehouse + membership + restaurant + retail + agent-skills + llm-friendly + open-data simultaneously* = the *first v2-AI owner-analytics-vocabulary reference of the 58-pass series*. The existing features cover subsets (celerp covers FastAPI-ERP; shop-ledger covers small-business-bookkeeping; bootstrap-startup-skills covers bootstrap-finance; small-business-ru covers owner-assist-AI-skills); majia-huiyuan combines the BI + data-warehouse + membership + LLM-friendly-analytics vocabulary into a single named primitive.
