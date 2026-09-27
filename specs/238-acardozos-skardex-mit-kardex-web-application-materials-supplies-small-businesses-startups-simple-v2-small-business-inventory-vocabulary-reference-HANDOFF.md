# HANDOFF: feature 238 — `acardozos/skardex` (v2 small-business-inventory-vocabulary-reference, defer parking-lot)

> **Date filed:** 2026-09-27
> **Author:** Daily Research Cron (LE31) — parent-surfaced pick after subagent bug (HN Algolia HTTP 400 + GitHub Search empty-stub bug)
> **Parent research issue:** [linear: blocked — see /opt/data/le31-daily-research-2026-09-27.linear-fallback.json]
> **Bucket:** v2 (parking-lot, future-v2-horizontal-expansion-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/acardozos/skardex
> **Reference data:** MIT, **0★/0⑂** (weak signal; explicitly NOT offered as evidence of restaurant need), Python, 367 KB modest repo, pushed 2026-09-23T05:18:19Z (in-window by `pushed_at` only — 4 days before fetch), created 2026-09-20T15:21:13Z (~7-day-old repo with IN-WINDOW `created_at`)

## Active feature path

`features/238-acardozos-skardex-mit-kardex-web-application-materials-supplies-small-businesses-startups-simple-v2-small-business-inventory-vocabulary-reference.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ⚠️ inferred (weak) | *When a small restaurant needs to track raw materials (ingredients + packaging + supplies) for cost + reorder decisions, and the owner wants a simple kardex-style FIFO/LIFO accounting layer, but today LE31 v1's `StockEntry` schema tracks only prepared-item quantities (charter §3.1 single-restaurant-vertical discipline), so that the vocabulary is a future v2 raw-materials-inventory reference.* Maps onto charter §3.1 and a hypothetical future v2 inventory-horizontal-expansion surface. |
| 2 | Viability | ⚠️ | MIT permissive; 0★/0⑂ community (early-traction; 2026-09-23 push indicates active development); **0★ is explicitly NOT offered as evidence of restaurant need**. |
| 3 | Practicability | ✅ | Python + MIT permissive + simple-web-app posture. |
| 4 | Conflict | none | MIT permissive; no AI surface (the *kardex* is a deterministic-inventory discipline, not an AI discipline). |
| 5 | Outcome / appetite / scope | ⚠️ v2 | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (367 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. **The 0★/0⑂ is the weakest of today's 3 picks and is explicitly NOT offered as evidence of restaurant need.** The cross-section reference is informative, not a v2 build-trigger. The verbatim description + the 6 named primitives + the MIT permissive license are the load-bearing value.

**WEAK SIGNAL DISCLOSURE**: the 0★/0⑂ + the ~7-day-old repo + the small (367 KB) size = the *weakest* of today's 3 picks; the verdict is `defer, parking-lot` with the explicit understanding that the owner has not requested this surface and the operational need is hypothetical. This pick is **filed at true weight** with no upward bias.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/238-acardozos-skardex-...md` (the vocabulary contract; READ for context)
  - `specs/238-acardozos-skardex-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (2026-09-23 push + MIT permissive + 6 named primitives = **observed event** for the push + **inferred** for the vocabulary; confidence low for mechanism / low for present urgency; **0★ is explicitly NOT offered as evidence**)
- [ ] All seven checks answered. ✅ (see table above; checks 1/2/5 carry the weak-signal warning)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (weak-signal warning explicitly recorded)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2026-09-23 push confirmed by raw `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/238-*.md` + this HANDOFF file `specs/238-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2 PR adopts the vocabulary**, the rollback path is: (1) drop the `kardex_entry` + `material` + `supplier` tables; (2) drop the `/kardex list` + `/kardex show` + `/kardex receive` commands. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

For any future coding agent that picks up this contract, the mandatory skill load-out per `le31-coding-agent-brief/SKILL.md` is:
- `le31-conventions` — global decision layer; the seven-check gate
- `le31-v1-feature-pattern` — the v1 feature template (Goal / Scope / Out of scope / Description / Data model / Implementation steps / Telegram interaction / Dependencies / Open questions / Why this matters)
- `le31-data` — LE31 data-correctness rules
- `le31-backend` — FastAPI + SQLModel + Postgres conventions
- `le31-frontend` — HTMX + minimal HTML conventions (for any future owner-web-UI-for-kardex surface)
- `le31-handoff-spec` — slice-contract authoring conventions
- `le31-coding-agent-brief` — paste-in prompt generation
- `le31-verification-protocol` — verification + rollback protocol
- `le31-quality-gates` — gates before merge
- `le31-arch-patterns` — FastAPI + aiogram + Postgres architectural patterns
- `le31-data-correctness` — decimal EUR, timezone-aware instants, append-only invariants

Today's parent (Daily Research Cron) only READ the relevant skill files; no LE31 source code was touched.