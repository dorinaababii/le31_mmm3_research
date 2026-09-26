# HANDOFF: feature 232 — `lpalbou/AbstractGateway` (v2-AI durable-control-plane + LICENSE UPGRADE `null → MIT`, defer parking-lot)

> **Date filed:** 2026-09-26
> **Author:** Daily Research Cron (LE31) — parent-verified override of subagent's proposed pick
> **Parent research issue:** [linear: blocked — see /opt/data/le31-daily-research-2026-09-26.linear-fallback.json]
> **Bucket:** v2-AI (parking-lot, future-v2-AI-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE (LICENSE UPGRADE `null → MIT` observed between 09-23 and 09-26)** — was `null` on 09-23 per carry-over observation; the upgrade unblocks the §3.2 gate that previously prevented feature filing
> **Reference URL:** https://github.com/lpalbou/AbstractGateway
> **Reference data:** MIT (upgraded), 4★/0⑂, Python, 11539 KB substantial repo, pushed 2026-09-25T01:41:25Z (in-window by `pushed_at` only), created 2026-01-07T20:45:36Z (OUT-OF-WINDOW by ~8.5 months)

## Active feature path

`features/232-lpalbou-AbstractGateway-mit-replay-first-durable-ai-control-plane-http-telegram-persistence-append-only-ledger-v2-ai-durable-control-plane.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When an AI workflow runs across multiple surfaces (terminal + browser + Telegram), and the operator wants to replay + audit the workflow, but today each client has its own run-history, so that observability is fragmented.* Maps onto charter §3.4. |
| 2 | Viability | ✅ | MIT permissive (LICENSE UPGRADE `null → MIT` observed today); 4★ community adoption; 11539 KB substantial repo. |
| 3 | Practicability | ✅ | Python; large repo (11539 KB) provides substantial vocabulary to read; *replay-first + durable + HTTP control plane + Telegram client + append-only-ledger + memory* vocabulary directly transferable to LE31's aiogram cook-bot. |
| 4 | Conflict | none | MIT permissive now (was `null` on 09-23); no §3.4 customer-facing-AI for the gateway itself (operator-tooling); **Telegram-client exposure requires §3.4 review** because Telegram could be customer-facing. |
| 5 | Outcome / appetite / scope | ✅ v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Moderate ingest (11539 KB); vocabulary-only artifact; zero ongoing maintenance. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v2-AI build-trigger. The 12 named topics + the verbatim description + the 7 named primitives + the LICENSE UPGRADE observation are the load-bearing value.

**CRITICAL OBSERVATION**: the LICENSE UPGRADE `null → MIT` between 09-23 and 09-26 is the **most actionable single finding of today's pass**; the §3.2 gate that previously blocked feature filing is now lifted. Recommend a manual LICENSE file inspection to confirm the upgrade is permanent (not a GitHub API metadata fluctuation).

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/232-lpalbou-AbstractGateway-...md` (the vocabulary contract; READ for context)
  - `specs/232-lpalbou-AbstractGateway-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (LICENSE UPGRADE = **observed event** between 09-23 and 09-26; vocabulary = inferred from the description + topics + 12 named primitives; confidence medium-high for license status / medium for vocabulary transferability)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; LICENSE UPGRADE confirmed by raw `license.spdx_id == "MIT"`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/232-*.md` + this HANDOFF file `specs/232-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `workflow_run` + `workflow_replay_history` + `workflow_client` tables; (2) drop the `/workflow list` + `/workflow show` + `/workflow replay` commands; (3) drop the HTTP-control-plane orchestration layer. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

When a future v2-AI PR triggers the artifact, the coding agent MUST load:
- `le31-conventions/SKILL.md` (always; the §3 hard invariants + the seven-check gate)
- `le31-v1-feature-pattern/SKILL.md` (for the v1-feature-pattern canonical contract shape — even though this is v2-AI, the contract shape carries over)
- `le31-feature-pipeline/SKILL.md` (for the feature-pipeline procedure)
- `le31-handoff-spec/SKILL.md` (for the slice handoff contract — this file is an example)
- `le31-coding-agent-brief/SKILL.md` (for the paste-in prompt to the coding agent)
- `le31-backend/SKILL.md` (for any SQLModel/Python/FastAPI work)
- `le31-data/SKILL.md` (for any data-model extension)
- `le31-frontend/SKILL.md` (for any web-UI extension)
- `le31-finance-analytics/SKILL.md` (for any EUR/tax-derivation work)

## Trigger condition

A future PR that adopts the artifact must explicitly note in its description: *"adopts the vocabulary from `features/232-lpalbou-AbstractGateway-...md`"*, and must trigger **all** of:
- A `workflow_run` SQLModel table with `run_id, workflow_type, started_at, completed_at, status, client_surface, replay_history_id`
- A `workflow_replay_history` SQLModel table with `history_id, run_id, recorded_at, state_snapshot, hash_chain_link`
- A `workflow_client` SQLModel table with `client_id, client_type, client_uri, last_seen_at, authenticated`
- A `/workflow list` + `/workflow show <run_id>` + `/workflow replay <run_id>` Telegram command set on the cook-bot (operator-tooling; charter §3.4 NOT triggered for the operator-tooling layer; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**)
- An HTTP-control-plane orchestration layer (FastAPI sub-app + middleware) for cross-process / cross-client workflow orchestration

Until the trigger fires, **no code is written, no schema is changed, no command is added**.

## Open questions for the owner / charter

- Will LE31 v2-AI ever introduce a durable-AI-control-plane surface? If yes, the artifact is the vocabulary reference (now that the license is MIT).
- Will LE31 v2-AI ever introduce a replay-first architecture? If yes, the artifact is the vocabulary reference.
- Will LE31 v2-AI ever introduce an HTTP-control-plane primitive? If yes, the artifact is the vocabulary reference.
- Will LE31 v2-AI ever introduce a multi-client (terminal + browser + tray + Telegram + email) workflow access? If yes, the artifact is the vocabulary reference (**with §3.4 review for Telegram-client exposure**).
- Will LE31 v2-AI ever introduce a hash-chained append-only-ledger? If yes, the artifact is the vocabulary reference.
- **Open question that may kill any future PR**: who would ever run the offline replay verifier of a workflow-run history? LE31 has exactly one stakeholder (the owner) who can just ask the AI what it did. The *replay-first architecture* may be over-engineering for a single-tenant single-operator scenario.
- **CRITICAL LICENSE UPGRADE QUESTION**: when exactly did the `lpalbou/AbstractGateway` LICENSE change from `null` to `MIT`? The 09-23 observation recorded `null`; the 09-25 record (per subagent) recorded `null`; today's 09-26 record recorded `MIT`. The upgrade must have occurred between 2026-09-25T01:41:25Z (last push before license change) and the parent re-fetch today (2026-09-26). Recommend a manual LICENSE file inspection to confirm the upgrade is permanent (not a GitHub API metadata fluctuation).

## Parent override rationale (recorded for transparency)

Subagent proposed 3 picks (`HannaneGhz/restaurant-order-bot` + `GabrielAlmeida-backend/restaurant-orders-api` + `siraj-motaung/orc-shark-api`); parent re-scored g5 (append-only+ledger) directly against raw JSON and surfaced 3 stronger candidates. This is the **3rd parent override of the 57-pass series** (prior overrides: 09-19 + 09-22; pattern established). Subagent's 3 picks were all 0★/0⑂/null-license/created-in-last-6-days = the **weakest candidates** of the 57-pass series. The parent-override picks (P1: `mentu-ai/commitment-protocol` MIT 10★/4⑂ + P2: `LinkedParticles/particles-standard` Apache-2.0 7★/0⑂ + P3: `lpalbou/AbstractGateway` MIT 4★/0⑂ with license upgrade `null → MIT`) have 10+7+4 = **21 stars total vs subagent's 0**. Per `le31-daily-research/SKILL.md` hard rule *"the subagent summary is a self-report, not a verified fact"*.

## Verification checklist

- [x] Active feature path documented: `features/232-lpalbou-AbstractGateway-...md`
- [x] Seven-check gate verdict recorded (all 7 checks answered; verdict = `defer`)
- [x] Files to touch listed (READ ONLY; no edits)
- [x] Verification protocol referenced
- [x] Rollback path documented (delete the 3 files = complete rollback)
- [x] Mandatory LE31 skill list recorded
- [x] Trigger condition explicit (requires 3 SQLModel tables + 3 Telegram commands + HTTP-control-plane orchestration layer)
- [x] Open questions documented (6 questions; 1 critical license-upgrade question; 1 that may kill any future PR)
- [x] Parent override rationale recorded for transparency
- [x] LICENSE UPGRADE `null → MIT` observation recorded prominently (the most actionable single finding of today's pass)