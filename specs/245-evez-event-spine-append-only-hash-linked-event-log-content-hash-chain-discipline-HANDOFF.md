# HANDOFF: feature 245 — `EvezArt/evez-event-spine` (v1 content-hash-chain-discipline-reference, defer parking-lot)

> **Date filed:** 2026-09-28
> **Author:** Daily Brainstorm Cron (LE31) — parent-surfaced pick
> **Parent research issue:** [linear: blocked — see /opt/data/le31-brainstorm-2026-09-28.linear-fallback.json]
> **Bucket:** v1 content-hash-chain-discipline-reference (parking-lot, future-v1-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/EvezArt/evez-event-spine
> **Reference data:** MIT, 0★/0⑂, Python, **45 KB tiny repo**, pushed **2026-09-24T21:48:47Z** (in-window by `pushed_at` only), created **2026-06-22T13:11:00Z** (off-window by `created_at` = *in-window by push only* — *4-day-ago fresh-push*). Description (verbatim): *"Append-only hash-linked event log — immutable, verifiable, readable truth."*

## Active feature path

`features/245-EvezArt-evez-event-spine-mit-append-only-hash-linked-event-log-immutable-verifiable-readable-truth-content-hash-chain-discipline-python.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v1 surface proposes a content-hash-chain on `audit_logs` (each row carries a `prev_hash` column referencing the prior row's content-hash), the owner/waiter wants the verbatim 3-property content-hash-chain-discipline + the *readable-truth-as-explorer* primitive from a real-world 2026 event log, so that any auditor can walk from the latest row backwards through all predecessors and re-compute the content-hash chain to verify integrity.* Maps onto charter §3.1 explicit-state-transitions. |
| 2 | Viability | ✅ | MIT permissive (STRICTLY-ADOPTABLE); 0★/0⑂ community (single-maintainer-discoverability); the *45 KB tiny repo* signals *single-file-implementability* = easy to re-implement against LE31 v1's SQLModel + audit_logs discipline. |
| 3 | Practicability | ✅ | Python + the verbatim description *"Append-only hash-linked event log — immutable, verifiable, readable truth"* = a *content-hash-chain-discipline primitive* that LE31 v1's existing `audit_logs` SQLModel schema *partially* implements via row-insert discipline but does NOT implement as a *content-hash-chained-event-log* (no `prev_hash` column on `audit_logs` today). |
| 4 | Conflict | none | MIT permissive; no §3.4 customer-facing-AI (the artifact is operator-tooling for owner/admin audit-chain-exploration); charter §3.1 explicit-state-transitions-compatible. |
| 5 | Outcome / appetite / scope | ✅ v1 | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (45 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1 build-trigger. The verbatim description + the 5-primitive quintuple (append-only + hash-linked + immutable + verifiable + readable truth) + the 3-property content-hash-chain-discipline are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/245-EvezArt-evez-event-spine-...md` (the vocabulary contract; READ for context)
  - `specs/245-evez-event-spine-append-only-hash-linked-event-log-content-hash-chain-discipline-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema (no `prev_hash` column added), the `StockEntry` schema, the waiter web UI, the cook Telegram bot, or the `index.html` views (no `index.html#/audit` view added).

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (MIT permissive + 0★ + 45 KB tiny + 2026-09-24 pushed + 2026-06-22 created + verbatim 5-primitive quintuple = **observed event** for the push + **inferred** for the vocabulary transferability; confidence high for the discipline-match / medium for the cross-section transferability)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (5-property quintuple + 3-property discipline + verbatim description all recorded)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + size + description all verbatim; 2026-09-24 pushed + 2026-06-22 created confirmed by raw `created_at` + `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/245-*.md` + this HANDOFF file `specs/245-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v1 PR adopts the vocabulary**, the rollback path is: (1) drop the `prev_hash` column on `audit_logs` (Alembic migration downgrade); (2) drop the `audit_chain_walker` module (additive); (3) drop the `/audit_chain` + `/verify_chain` Telegram commands. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

For any future coding agent that picks up this contract, the mandatory skill load-out per `le31-coding-agent-brief/SKILL.md` is:
- `le31-conventions` — global decision layer; the seven-check gate
- `le31-v1-feature-pattern` — the v1 feature template (Goal / Scope / Out of scope / Description / Data model / Implementation steps / Telegram interaction / Dependencies / Open questions / Why this matters)
- `le31-data` — LE31 data-correctness rules
- `le31-backend` — FastAPI + SQLModel + Postgres conventions
- `le31-frontend` — HTMX + minimal HTML conventions (for any future owner-web-UI surface, e.g. the `index.html#/audit` content-hash-chain-explorer view)
- `le31-handoff-spec` — slice-contract authoring conventions
- `le31-coding-agent-brief` — paste-in prompt generation
- `le31-verification-protocol` — verification + rollback protocol
- `le31-quality-gates` — gates before merge
- `le31-arch-patterns` — FastAPI + aiogram + Postgres architectural patterns
- `le31-data-correctness` — decimal EUR, timezone-aware instants, append-only invariants

Today's parent (Daily Brainstorm Cron) only READ the relevant skill files; no LE31 source code was touched.
