# HANDOFF: feature 255 — `t0mer/Wazy` (v1 self-hosted-Telegram-bot + FastAPI-REST-API + aiogram-deployment-blueprint cross-section vocabulary reference, defer parking-lot)

> **Date filed:** 2026-09-30
> **Author:** Daily Brainstorm Cron (LE31) — parent-verified pick
> **Parent research issue:** Brainstorm 2026-09-30 — daily (Linear parent index)
> **Bucket:** v1 self-hosted-Telegram-bot + FastAPI-REST-API + aiogram-deployment-blueprint primitive (parking-lot, future-v1-surface-vocabulary-reference)
> **License:** **Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/t0mer/Wazy
> **Reference data:** Apache-2.0, 19★/4⑂, Python, 81 KB tiny repo = deployment-blueprint-not-the-application, pushed **2026-09-30T02:08:27Z = TODAY** (in-window by `pushed_at`), created **2022-10-25T07:29:20Z** (~4 years before window-start = OUT-OF-WINDOW by `created_at` = in-window by push only)

## Active feature path

`features/255-t0mer-Wazy-apache-2-0-self-hosted-telegram-bot-and-fastapi-rest-api-checks-waze-travel-times-routes-scheduled-checks-v1-self-hosted-telegram-bot-fastapi-rest-api-aiogram-deployment-blueprint-vocabulary.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v1 surface needs a **production-ready-deployment-blueprint** (self-hosted + Docker + FastAPI + Telegram-bot + scheduled-checks), the owner wants a known-good reference that has 19★ + 4⑂ + sustained-active-development (4-year-old repo + TODAY's fresh-push), but LE31 today has no documented deployment-blueprint, so that any future owner-self-hosted-deployment has a reference.* Maps to charter §3.1 (Python 3.13 + FastAPI + SQLModel + Postgres + aiogram v3 + on-premise stack). |
| 2 | Viability | ✅ | Apache-2.0 permissive; 19★/4⑂ community; TODAY's fresh-push; **81 KB tiny = deployment-blueprint-not-the-application**; **3/12 topics on the literal LE31 v1 stack** = on-LE31-stack-vocabulary-envelope. |
| 3 | Practicability | ✅ | Python + FastAPI + Telegram-bot + Docker + self-hosted = all on-LE31-stack-vocabulary-envelope; LE31 v1's cook-bot already uses this exact primitive set. |
| 4 | Conflict | none | Apache-2.0 permissive; *self-hosted-Telegram-bot + FastAPI-REST-API + Docker* = charter §3.1 alignment (Python 3.13 + FastAPI + Postgres + on-premise posture); no AI surface = §3.4 NOT triggered. |
| 5 | Outcome / appetite / scope | ✅ v1 | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (81 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1 build-trigger. The verbatim description + the 5 named primitives + the TODAY fresh-push + the 12 topics + the 81 KB tiny-deployment-blueprint-not-the-application-repo size are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/255-t0mer-Wazy-...md` (the vocabulary contract; READ for context)
  - `specs/255-t0mer-Wazy-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [x] Evidence and confidence recorded. ✅ (2022-10-25 created + 2026-09-30 pushed-TODAY + Apache-2.0 permissive + 12 topics + 5 named primitives + 19★/4⑂ community traction + 81 KB tiny-deployment-blueprint-not-the-application = **observed event** for the push + **inferred** for the vocabulary; confidence high for mechanism / low for present urgency)
- [x] All seven checks answered. ✅ (see table above; all checks pass cleanly)
- [x] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [x] No unresolved source-of-truth conflict was guessed through. ✅ (no caveats; charter §3.1-aligned via Python + FastAPI + Telegram-bot + Docker + self-hosted)
- [x] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2022-10-25 created + 2026-09-30 pushed-TODAY confirmed by raw `created_at` + `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/255-*.md` + this HANDOFF file `specs/255-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v1 PR adopts the vocabulary**, the rollback path is: (1) drop the `ScheduledCheck` + `DeploymentBlueprint` tables; (2) drop the deployment-blueprint-as-documentation discipline. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

For any future coding agent that picks up this contract, the mandatory skill load-out per `le31-coding-agent-brief/SKILL.md` is:
- `le31-conventions` — global decision layer; the seven-check gate
- `le31-v1-feature-pattern` — the v1 feature template (Goal / Scope / Out of scope / Description / Data model / Implementation steps / Telegram interaction / Dependencies / Open questions / Why this matters)
- `le31-data` — LE31 data-correctness rules
- `le31-backend` — FastAPI + SQLModel + Postgres conventions
- `le31-frontend` — HTMX + minimal HTML conventions (for any future owner-web-UI surface)
- `le31-handoff-spec` — slice-contract authoring conventions
- `le31-coding-agent-brief` — paste-in prompt generation
- `le31-verification-protocol` — verification + rollback protocol
- `le31-quality-gates` — gates before merge
- `le31-arch-patterns` — FastAPI + aiogram + Postgres architectural patterns
- `le31-data-correctness` — decimal EUR, timezone-aware instants, append-only invariants

Today's parent (Daily Brainstorm Cron) only READ the relevant skill files; no LE31 source code was touched.