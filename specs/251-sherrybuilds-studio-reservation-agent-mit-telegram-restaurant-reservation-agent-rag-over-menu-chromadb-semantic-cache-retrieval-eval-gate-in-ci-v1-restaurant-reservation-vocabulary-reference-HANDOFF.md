# HANDOFF: feature 251 — `sherrybuilds-studio/reservation-agent` (v1 restaurant-reservation + retrieval-eval-gate-in-CI vocabulary reference, defer parking-lot)

> **Date filed:** 2026-09-29
> **Author:** Daily Brainstorm Cron (LE31) — parent-verified pick
> **Parent research issue:** Brainstorm 2026-09-29 — daily (Linear parent index)
> **Bucket:** v1 restaurant-reservation + retrieval-eval-gate-in-CI vocabulary reference (parking-lot, future-v1-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/sherrybuilds-studio/reservation-agent
> **Reference data:** MIT, 0★/0⑂, Python, 59 KB tiny repo, pushed **2026-09-28T07:13:58Z** (1 day ago, in-window by `pushed_at`), created **2026-05-14T03:25:58Z** (~4.5 months before window start, off-window by `created_at` = *in-window by push only*)

## Active feature path

`features/251-sherrybuilds-studio-reservation-agent-mit-telegram-restaurant-reservation-agent-rag-over-menu-chromadb-semantic-cache-retrieval-eval-gate-in-ci-v1-restaurant-reservation-vocabulary-reference.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v1 surface proposes a Telegram-restaurant-reservation-agent + RAG-over-menu + ChromaDB + semantic-cache + retrieval-eval-gate-in-CI primitive, the owner wants the verbatim 8-primitive vocabulary from a real-world 2026 Telegram-restaurant-reservation-agent, but today LE31 has no RAG surface at all and no customer-reservation-handling surface, so that the future v1 surface has a documented reference.* Maps onto charter §3.1 + §3.4. |
| 2 | Viability | ✅ | MIT permissive; 0★/0⑂ community (1-day-old push + 59 KB tiny repo = single-maintainer-discoverability). |
| 3 | Practicability | ⚠️ | Python + MIT permissive + Telegram-restaurant-reservation-agent. **Stack caveats**: (i) ChromaDB is additional storage beyond LE31 v1's Postgres-only stack (charter §3.1 known-conflict note); (ii) any future v1 surface adopting this pattern would require a `Reservation` SQLModel table + a `MenuItemEmbedding` SQLModel table; (iii) the *retrieval-eval-gate-in-CI* requires a retrieval-quality-metric that LE31 v1 does NOT have today. |
| 4 | Conflict | ⚠️ §3.4 borderline | MIT permissive; *the vocabulary itself is operator-tooling-AI* (charter §3.4-compatible); *the Telegram-restaurant-reservation-agent surface itself is borderline* because the Telegram-bot is the customer's interface for reservation requests (potentially customer-facing AI = charter §3.4 strict prohibition). Owner decision required before any future v1 PR adopts this vocabulary. |
| 5 | Outcome / appetite / scope | ✅ v1 | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (59 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1 build-trigger. The verbatim description + the 6 named primitives + the 1-day-ago fresh push + the 59 KB tiny repo size are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/251-sherrybuilds-studio-reservation-agent-...md` (the vocabulary contract; READ for context)
  - `specs/251-sherrybuilds-studio-reservation-agent-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (2026-05-14 created + 2026-09-28 pushed + MIT permissive + 8 topics + 6 named primitives + 1-day-ago fresh push + 59 KB tiny repo = **observed event** for the push + **inferred** for the vocabulary; confidence medium for mechanism / low for present urgency)
- [ ] All seven checks answered. ✅ (see table above; checks 3 + 4 carry the stack caveat + §3.4 borderline flag)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (stack caveat explicitly recorded; §3.4 borderline explicitly flagged)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2026-05-14 created + 2026-09-28 pushed confirmed by raw `created_at` + `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/251-*.md` + this HANDOFF file `specs/251-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v1 PR adopts the vocabulary**, the rollback path is: (1) drop the `Reservation` + `MenuItemEmbedding` + `SemanticCacheEntry` + `RetrievalEvalResult` tables; (2) drop the `/reserve` + `/menu_search` + `/eval_results` commands. All future rollbacks are explicit because the artifact is read-only.

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
