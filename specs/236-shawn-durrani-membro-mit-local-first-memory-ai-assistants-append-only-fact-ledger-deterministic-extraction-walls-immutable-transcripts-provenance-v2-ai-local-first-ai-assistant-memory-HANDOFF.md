# HANDOFF: feature 236 — `shawn-durrani/membro` (v2-AI local-first-AI-assistant-memory, defer parking-lot)

> **Date filed:** 2026-09-27
> **Author:** Daily Research Cron (LE31) — parent-surfaced pick after subagent bug (HN Algolia HTTP 400 + GitHub Search empty-stub bug)
> **Parent research issue:** [linear: blocked — see /opt/data/le31-daily-research-2026-09-27.linear-fallback.json]
> **Bucket:** v2-AI (parking-lot, future-v2-AI-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/shawn-durrani/membro
> **Reference data:** MIT, 1★/0⑂, Python, 661 KB modest repo, pushed **2026-09-27T02:20:40Z = TODAY** (in-window by `pushed_at` only — ~5 hours before fetch), created 2026-08-20T03:11:24Z (~5-week-old repo with in-window `pushed_at`; OUT-OF-WINDOW by ~5 weeks by `created_at`)

## Active feature path

`features/236-shawn-durrani-membro-mit-local-first-memory-ai-assistants-append-only-fact-ledger-deterministic-extraction-walls-immutable-transcripts-provenance-v2-ai-local-first-ai-assistant-memory.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When an AI assistant's memory layer needs to be local-first + append-only + deterministic-extraction-walls + immutable + provenance-carrying, and the operator wants verifiable fact-ledger semantics for the AI's outputs, but today LE31 has no AI surface at all (charter §3.4 invariant), so that the vocabulary is a future v2-AI reference.* Maps onto charter §3.4. |
| 2 | Viability | ✅ | MIT permissive; 661 KB modest repo; 1★/0⑂ community (early-traction but TODAY push indicates active development). |
| 3 | Practicability | ✅ | Python + MIT permissive + local-first posture matches LE31's charter §3.1 explicit-state-transition discipline. |
| 4 | Conflict | none | MIT permissive; no §3.4 customer-facing-AI (this is operator-tooling-AI memory layer). |
| 5 | Outcome / appetite / scope | ✅ v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (661 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v2-AI build-trigger. The verbatim description + the 5 named primitives + the TODAY push are the load-bearing value.

**OBSERVATION**: the **TODAY push (2026-09-27T02:20:40Z, ~5 hours before fetch time)** is the strongest in-window signal today for any v2-AI vocabulary candidate; combined with MIT permissive + the *local-first + AI-assistant-memory + append-only-fact-ledger + deterministic-extraction-walls + immutable-transcripts + provenance-carrying-summaries* quintuple-primitive, this is the most actionable new finding of the day.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/236-shawn-durrani-membro-...md` (the vocabulary contract; READ for context)
  - `specs/236-shawn-durrani-membro-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (TODAY push + MIT permissive + 5 named primitives = **observed event** for the push + **inferred** for the vocabulary; confidence medium for mechanism / low for present urgency)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; TODAY push confirmed by raw `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/236-*.md` + this HANDOFF file `specs/236-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `fact` + `transcript` + `provenance_chain` tables; (2) drop the `/fact status` + `/fact show` + `/fact verify` commands. All future rollbacks are explicit because the artifact is read-only.

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