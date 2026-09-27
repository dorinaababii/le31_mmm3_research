# HANDOFF: feature 237 — `willykeenan/agentbrain-contextlib` (v2-AI markdown-contextlib, defer parking-lot)

> **Date filed:** 2026-09-27
> **Author:** Daily Research Cron (LE31) — parent-surfaced pick after subagent bug (HN Algolia HTTP 400 + GitHub Search empty-stub bug)
> **Parent research issue:** [linear: blocked — see /opt/data/le31-daily-research-2026-09-27.linear-fallback.json]
> **Bucket:** v2-AI (parking-lot, future-v2-AI-surface-vocabulary-reference)
> **License:** **Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/willykeenan/agentbrain-contextlib
> **Reference data:** Apache-2.0, 1★/0⑂, Python, 100 KB modest repo, pushed **2026-09-26T22:57:33Z** (in-window by `pushed_at` only — 1 day before fetch), created 2026-09-25T16:07:10Z (~2-day-old repo with in-window `pushed_at`; OUT-OF-WINDOW by ~2 days by `created_at`)

## Active feature path

`features/237-willykeenan-agentbrain-contextlib-apache-2-0-markdown-long-term-memory-append-only-deterministic-contextlib-v2-ai-markdown-context-lib.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a project needs long-term memory for AI context, and the operator wants the memory to be human-readable (Markdown files in Finder) + append-only + no-database-required, but today LE31 has no AI context memory surface at all (charter §3.4 invariant), so that the vocabulary is a future v2-AI reference.* Maps onto charter §3.4. |
| 2 | Viability | ✅ | Apache-2.0 permissive; 1★/0⑂ community (early-traction; 2026-09-26 push indicates active development). |
| 3 | Practicability | ⚠️ | Python + Apache-2.0 permissive + Markdown-files posture. **Stack caveat**: Markdown is not LE31 v1's Postgres-only stack; the *plain-Markdown-as-long-term-memory* vocabulary is transferable but the serialization format may not be directly adopted. |
| 4 | Conflict | none | Apache-2.0 permissive; no §3.4 customer-facing-AI (this is operator-tooling-AI contextlib). |
| 5 | Outcome / appetite / scope | ✅ v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (100 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v2-AI build-trigger. The verbatim description + the 4 named primitives + the Apache-2.0 license are the load-bearing value.

**STACK CAVEAT**: Markdown is not LE31 v1's Postgres-only stack. The *plain-Markdown-as-long-term-memory* vocabulary is transferable but the serialization format may not be directly adopted. Future v2-AI adoption could either (a) adopt the Markdown serialization format directly (file-system-as-database for the contextlib) or (b) adopt a Postgres-backed *contextlib* table that mimics the Markdown-as-memory discipline. The Markdown serialization is the load-bearing primitive, not the file-system-vs-database choice.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/237-willykeenan-agentbrain-contextlib-...md` (the vocabulary contract; READ for context)
  - `specs/237-willykeenan-agentbrain-contextlib-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (2026-09-26 push + Apache-2.0 permissive + 4 named primitives = **observed event** for the push + **inferred** for the vocabulary; confidence medium for mechanism / low for present urgency)
- [ ] All seven checks answered. ✅ (see table above; check 3 carries the stack caveat)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (stack caveat explicitly recorded)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2026-09-26 push confirmed by raw `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/237-*.md` + this HANDOFF file `specs/237-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `contextlib_entry` + `contextlib_file` tables OR delete the `~/le31-contextlib/*.md` directory tree; (2) drop the `/contextlib list` + `/contextlib show` + `/contextlib append` commands. All future rollbacks are explicit because the artifact is read-only.

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