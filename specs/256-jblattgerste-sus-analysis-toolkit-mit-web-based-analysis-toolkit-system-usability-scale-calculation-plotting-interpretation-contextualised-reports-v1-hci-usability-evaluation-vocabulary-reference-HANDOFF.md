# HANDOFF: feature 256 — `jblattgerste/sus-analysis-toolkit` (v1 HCI-evaluation SUS-survey vocabulary reference, defer parking-lot)

> **Date filed:** 2026-09-30
> **Author:** Daily Brainstorm Cron (LE31) — parent-verified pick
> **Parent research issue:** Brainstorm 2026-09-30 — daily (Linear parent index)
> **Bucket:** v1 HCI-evaluation SUS-survey-vocabulary primitive (parking-lot, future-v1-usability-evaluation-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/jblattgerste/sus-analysis-toolkit
> **Reference data:** MIT, 30★/7⑂, Python, 19003 KB substantial production-grade repo, pushed **2026-09-25T18:45:07Z** (5 days ago, in-window by `pushed_at`), created **2022-01-03T13:07:32Z** (~4.7 years before window-start = OUT-OF-WINDOW by `created_at` = in-window by push only)

## Active feature path

`features/256-jblattgerste-sus-analysis-toolkit-mit-web-based-analysis-toolkit-system-usability-scale-calculation-plotting-interpretation-contextualised-reports-v1-hci-usability-evaluation-vocabulary-reference.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v1 surface wants to **measure waiter-UI + cook-Telegram-bot + owner-dashboard usability**, the owner wants a **standardised-questionnaire + scoring + interpretation primitive**, but LE31 today has no formal HCI-evaluation discipline, so that any future usability-evaluation has a documented reference.* Maps to charter §3.1 (Python 3.13 + FastAPI + SQLModel + minimal HTML/HTMX posture). |
| 2 | Viability | ✅ | MIT permissive; 30★/7⑂ community; **19 MB substantial** = production-grade; 4-year-old repo (2022-01-03) with 2026-09-25 fresh-push = sustained-active-developer signal. |
| 3 | Practicability | ✅ | Python + Flask-style web-toolkit + matplotlib + data-viz = transferable to FastAPI + HTMX + matplotlib (charter §3.1 + §3.2 STRICTLY-COMPATIBLE). |
| 4 | Conflict | none | MIT permissive; **10/10 topics on the literal HCI-evaluation axis**; no AI surface = §3.4 NOT triggered. |
| 5 | Outcome / appetite / scope | ✅ v1 | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (19003 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1 build-trigger. The verbatim description + the 5 named primitives + the 5-day-ago fresh-push + the 10/10 topics on literal HCI-evaluation-axis + the 19003 KB substantial production-grade-repo size are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/256-jblattgerste-sus-analysis-toolkit-...md` (the vocabulary contract; READ for context)
  - `specs/256-jblattgerste-sus-analysis-toolkit-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [x] Evidence and confidence recorded. ✅ (2022-01-03 created + 2026-09-25 pushed + MIT permissive + 10/10 topics on literal HCI-evaluation-axis + 5 named primitives + 30★/7⑂ community traction + 19003 KB substantial production-grade repo = **observed event** for the push + **inferred** for the vocabulary; confidence high for mechanism / low for present urgency)
- [x] All seven checks answered. ✅ (see table above; all checks pass cleanly)
- [x] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [x] No unresolved source-of-truth conflict was guessed through. ✅ (no caveats; charter §3.1-aligned via Python + Flask-style web-toolkit + matplotlib + data-viz)
- [x] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2022-01-03 created + 2026-09-25 pushed confirmed by raw `created_at` + `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/256-*.md` + this HANDOFF file `specs/256-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v1 PR adopts the vocabulary**, the rollback path is: (1) drop the `Sussurvey` + `Susquestion` + `Susscore` + `Susreport` tables; (2) drop the SUS-survey HTMX surface + the SUS-survey Flask-style web-toolkit. All future rollbacks are explicit because the artifact is read-only.

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