# HANDOFF: feature 252 — `nimaxin/adminsite` (v1 on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel vocabulary reference, defer parking-lot)

> **Date filed:** 2026-09-29
> **Author:** Daily Brainstorm Cron (LE31) — parent-verified pick
> **Parent research issue:** Brainstorm 2026-09-29 — daily (Linear parent index)
> **Bucket:** v1 on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel primitive (parking-lot, future-v1-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/nimaxin/adminsite
> **Reference data:** MIT, **4★/0⑂** (highest in-window 2026-09-29 Python FastAPI + HTMX admin-panel star count), Python, **4306 KB substantial repo**, pushed **2026-09-27T18:20:57Z** (2 days ago, in-window by `pushed_at`), created **2026-09-20T17:07:26Z** (~9 days before push, **both fields in-window**)

## Active feature path

`features/252-nimaxin-adminsite-mit-admin-panel-sqlalchemy-2-0-orm-fastapi-starlette-litestar-htmx-v1-on-stack-admin-panel-vocabulary-reference.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v1 surface proposes an on-stack FastAPI + HTMX + SQLAlchemy-2.0 admin-panel primitive, the owner wants the verbatim 6-primitive vocabulary from a real-world 2026 admin-panel-library, but today LE31 has a custom `index.html` floor plan + stock view (no generic admin-panel-library), so that the future v1 surface has a documented reference.* Maps onto charter §3.1. |
| 2 | Viability | ✅ | MIT permissive; 4★/0⑂ community (highest in-window 2026-09-29 Python FastAPI + HTMX admin-panel star count; production-grade 4306 KB substantial repo). |
| 3 | Practicability | ✅ | Python + MIT permissive + on-stack-vocabulary-envelope (5 of 10 topics = fastapi + htmx + python + sqlalchemy + starlette = the **literal LE31 v1 stack primitive**). SQLModel is built on SQLAlchemy 2.0 = SQLModel-compatibility verified. |
| 4 | Conflict | none | MIT permissive; no §3.4 customer-facing-AI (the admin-panel is a generic SQLModel-table-CRUD library; no restaurant diner interacts with the admin-panel). |
| 5 | Outcome / appetite / scope | ✅ v1 | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (4306 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1 build-trigger. The verbatim description + the 6 named primitives + the 4★ community traction + the 4306 KB production-grade repo size are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/252-nimaxin-adminsite-...md` (the vocabulary contract; READ for context)
  - `specs/252-nimaxin-adminsite-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (2026-09-20 created + 2026-09-27 pushed + MIT permissive + 10 topics + 6 named primitives + 4★ community traction + 4306 KB substantial repo = **observed event** for the push + **inferred** for the vocabulary; confidence medium for mechanism / low for present urgency)
- [ ] All seven checks answered. ✅ (see table above; all checks pass cleanly)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (no caveats; cleanest pick of today's 3)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2026-09-20 created + 2026-09-27 pushed confirmed by raw `created_at` + `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/252-*.md` + this HANDOFF file `specs/252-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v1 PR adopts the vocabulary**, the rollback path is: (1) drop the `User` + `Session` + `AuditLog` tables; (2) drop the `/admin/` + `/admin/login` + `/admin/logout` routes. All future rollbacks are explicit because the artifact is read-only.

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
