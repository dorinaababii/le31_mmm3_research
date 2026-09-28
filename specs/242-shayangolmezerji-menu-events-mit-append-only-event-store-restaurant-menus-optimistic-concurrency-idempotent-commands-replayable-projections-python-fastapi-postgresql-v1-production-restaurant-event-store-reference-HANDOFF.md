# HANDOFF: feature 242 — `shayangolmezerji/menu-events` (v1 production-restaurant-event-store-reference, defer parking-lot)

> **Date filed:** 2026-09-28
> **Author:** Daily Research Cron (LE31) — parent-surfaced pick after subagent bug-free run (HN Algolia HTTP 400 fix + GitHub Search empty-stub fix both verified)
> **Parent research issue:** [linear: blocked — see /opt/data/le31-daily-research-2026-09-28.linear-fallback.json]
> **Bucket:** v1 production-restaurant-event-store-reference (parking-lot, future-v1-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/shayangolmezerji/menu-events
> **Reference data:** MIT, 1★/0⑂, Python, 114 KB modest repo, pushed **2026-09-27T09:42:37Z** (in-window by `pushed_at`), created **2026-09-26T16:37:40Z** (in-window by `created_at` — 2-day-old repo)

## Active feature path

`features/242-shayangolmezerji-menu-events-mit-append-only-event-store-restaurant-menus-optimistic-concurrency-idempotent-commands-replayable-projections-python-fastapi-postgresql-v1-production-restaurant-event-store-reference.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v1 surface proposes restaurant-event-store + append-only + idempotency + optimistic concurrency, the owner/waiter wants the verbatim 4-primitive vocabulary from a real-world 2026 event store, but today LE31 has no menu-event-store surface, so that the v1 surface is documented against a real-world 2026 reference.* Maps onto charter §3.3 stock-discipline. |
| 2 | Viability | ✅ | MIT permissive; 1★/0⑂ community (2-day-old repo; 2026-09-27 push indicates active development pipeline); the *exact-stack-match* (Python + FastAPI + PostgreSQL = LE31 v1 stack) is the load-bearing primitive. |
| 3 | Practicability | ✅ | Python + FastAPI + PostgreSQL = **the EXACT LE31 v1 stack** (FastAPI + SQLModel + Postgres are all on the LE31 pin set); LE31's SQLModel is built on SQLAlchemy 2.0 which supports the same idempotency/optimistic-concurrency patterns. |
| 4 | Conflict | none | MIT permissive; no §3.4 customer-facing-AI (the artifact is operator-tooling for menu-state-history); charter §3.3 stock-discipline-compatible. |
| 5 | Outcome / appetite / scope | ✅ v1 | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (114 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1 build-trigger. The verbatim description + the 4 named primitives + the *exact-stack-match* are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/242-shayangolmezerji-menu-events-...md` (the vocabulary contract; READ for context)
  - `specs/242-shayangolmezerji-menu-events-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (2026-09-26 created + 2026-09-27 pushed + MIT permissive + 4 named primitives + exact-stack-match = **observed event** for the push + **inferred** for the vocabulary; confidence high for the stack-match / medium for the vocabulary transferability)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (stack-match explicitly recorded)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2026-09-26 created + 2026-09-27 pushed confirmed by raw `created_at` + `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/242-*.md` + this HANDOFF file `specs/242-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v1 PR adopts the vocabulary**, the rollback path is: (1) drop the `menu_event` + `menu_projection` tables OR delete the `current_menu_state` view; (2) drop the `/menu_history` + `/menu_replay` commands. All future rollbacks are explicit because the artifact is read-only.

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

Today's parent (Daily Research Cron) only READ the relevant skill files; no LE31 source code was touched.
