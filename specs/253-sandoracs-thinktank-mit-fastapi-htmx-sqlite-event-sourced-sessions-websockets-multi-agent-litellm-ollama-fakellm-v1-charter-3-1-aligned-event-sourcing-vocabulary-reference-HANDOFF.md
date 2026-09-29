# HANDOFF: feature 253 — `sandoracs/thinktank` (v1 charter-§3.1-aligned event-sourced-sessions + WebSockets + multi-agent-LLM-control-plane vocabulary reference, defer parking-lot)

> **Date filed:** 2026-09-29
> **Author:** Daily Brainstorm Cron (LE31) — parent-verified pick
> **Parent research issue:** Brainstorm 2026-09-29 — daily (Linear parent index)
> **Bucket:** v1 charter-§3.1-aligned event-sourced-sessions + WebSockets + multi-agent-LLM-control-plane primitive (parking-lot, future-v1-or-v2-AI-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/sandoracs/thinktank
> **Reference data:** MIT, 0★/0⑂, Python, 494 KB modest repo, pushed **2026-09-27T23:42:24Z** (2 days ago, in-window by `pushed_at`), created **2026-09-27T21:16:15Z** (~2.5 hours before push, **both fields in-window by same-day-fresh-repo created+committed-today 2026-09-27** = the *freshest in-window* of today's 3 picks = the *strongest fresh-discovery signal*)

## Active feature path

`features/253-sandoracs-thinktank-mit-fastapi-htmx-sqlite-event-sourced-sessions-websockets-multi-agent-litellm-ollama-fakellm-v1-charter-3-1-aligned-event-sourcing-vocabulary-reference.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v1 owner-web-UI-session-event-sourcing surface or v2-AI multi-agent-LLM-control-plane surface proposes an event-sourced-sessions + WebSockets + multi-agent-LLM-control-plane + SQLite + LiteLLM + Ollama + FakeLLM-fallback primitive, the owner wants the verbatim 10-primitive vocabulary from a real-world 2026 multi-agent-debate-system, but today LE31 has no multi-agent-LLM surface at all (charter §3.4), so that the future v1/v2-AI surface has a documented reference.* Maps onto charter §3.1 + §3.4. |
| 2 | Viability | ✅ | MIT permissive; 0★/0⑂ community (same-day-fresh-repo + 2-day-ago fresh push + 16 topics = richest-vocabulary pick of today's brainstorm). |
| 3 | Practicability | ✅ | Python + MIT permissive + on-LE31-stack-vocabulary (FastAPI + HTMX + Python + SQLite are all LE31-stack-aligned; SQLite is on-pattern for v1 development per charter §3.1 known-conflict note; multi-agent-LLM + LiteLLM + Ollama + FakeLLM are charter §3.4-compatible with non-AI-fallback). |
| 4 | Conflict | none | MIT permissive; *multi-agent-LLM* is **operator-tooling-AI** (charter §3.4-compatible: the agents debate on a virtual table, supervised by an owner/staff, no customer-facing interaction); *offline FakeLLM + local Ollama* = charter §3.4's *non-AI-fallback* requirement satisfied. |
| 5 | Outcome / appetite / scope | ✅ v1 / v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (494 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1/v2-AI build-trigger. The verbatim description + the 10 named primitives + the same-day-fresh-repo + the 16 topics + the 494 KB modest-repo size are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/253-sandoracs-thinktank-...md` (the vocabulary contract; READ for context)
  - `specs/253-sandoracs-thinktank-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (2026-09-27 created + 2026-09-27 pushed + MIT permissive + 16 topics + 10 named primitives + same-day-fresh-repo + 2-day-ago fresh push + 494 KB modest repo = **observed event** for the push + **inferred** for the vocabulary; confidence medium for mechanism / low for present urgency)
- [ ] All seven checks answered. ✅ (see table above; all checks pass cleanly)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (no caveats; charter §3.4-compatible via non-AI-fallback)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2026-09-27 created + 2026-09-27 pushed confirmed by raw `created_at` + `pushed_at`; README fetched and verified single-machine-SQLite-deployment + LiteLLM-Ollama-FakeLLM-fallback claims)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/253-*.md` + this HANDOFF file `specs/253-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v1/v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `SessionEvent` + `Persona` + `MemoryLayer` + `LLMProvider` tables; (2) drop the WebSockets route + the multi-agent-debate endpoints. All future rollbacks are explicit because the artifact is read-only.

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
