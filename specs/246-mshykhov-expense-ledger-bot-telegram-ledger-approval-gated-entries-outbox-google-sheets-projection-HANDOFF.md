# HANDOFF: feature 246 — `mshykhov/expense-ledger-bot` (v1 telegram-ledger-extension+approval-gating+outbox+google-sheets-projection-reference, defer parking-lot)

> **Date filed:** 2026-09-28
> **Author:** Daily Brainstorm Cron (LE31) — parent-surfaced pick
> **Parent research issue:** [linear: blocked — see /opt/data/le31-brainstorm-2026-09-28.linear-fallback.json]
> **Bucket:** v1 telegram-ledger-extension+approval-gating+outbox+google-sheets-projection-reference (parking-lot, future-v1-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/mshykhov/expense-ledger-bot
> **Reference data:** MIT, 0★/0⑂, Python, **233 KB substantial repo**, pushed **2026-09-13T05:19:30Z** + created **2026-09-13T05:17:59Z** = **both fields in-window by same-day-fresh-repo created+committed-today** (the *freshest in-window* of today's 3 picks). Description (verbatim): *"Telegram expense ledger with approval-based entries, PostgreSQL transactions, an outbox, and optional Google Sheets projection."*

## Active feature path

`features/246-mshykhov-expense-ledger-bot-mit-telegram-expense-ledger-approval-based-entries-postgresql-transactions-outbox-google-sheets-projection-python.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v1 surface proposes (a) approval-gating on StockEntry commits (a `/approve <entry_id>` Telegram bot command that walks an owner through the `DRAFT → PENDING_APPROVAL → COMMITTED` state-machine), (b) transactional-outbox pattern on audit_logs (a `StockEntryOutbox` SQLModel table that records publish-intent events atomically with the StockEntry insert via the same `with session.begin():` transaction), and/or (c) Google-Sheets-projection of the StockEntry ledger for owner-facing-visibility, the owner wants the verbatim 5-primitive quintuple from a real-world 2026 Telegram-ledger discipline.* Maps onto charter §3.1 explicit-state-transitions. |
| 2 | Viability | ✅ | MIT permissive (STRICTLY-ADOPTABLE); 0★/0⑂ community (single-maintainer-discoverability); 233 KB substantial-repo size = multi-file-implementability = easy to re-implement against LE31 v1's SQLModel + aiogram-v3 + `audit_logs` discipline. |
| 3 | Practicability | ✅ | Python + the verbatim description *"Telegram expense ledger with approval-based entries, PostgreSQL transactions, an outbox, and optional Google Sheets projection"* = a *5-primitive quintuple* that LE31 v1's existing cook-Telegram-bot + StockEntry + audit_logs triple surface *partially* implements via row-insert discipline but does NOT implement as an *approval-gated-outbox-Sheets-projection ledger* (no `state=PENDING_APPROVAL` on `StockEntry` today; no `StockEntryOutbox` table today; no Google-Sheets-projection worker today). |
| 4 | Conflict | none | MIT permissive; no §3.4 customer-facing-AI (the artifact is operator-tooling for owner-facing-admin-approval + Sheets-export); charter §3.1 explicit-state-transitions-compatible. |
| 5 | Outcome / appetite / scope | ✅ v1 | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (233 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1 build-trigger. The verbatim description + the 5-primitive quintuple (Telegram-ledger + approval-gated-entries + Postgres-transactions + outbox + Google-Sheets-projection) are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/246-mshykhov-expense-ledger-bot-...md` (the vocabulary contract; READ for context)
  - `specs/246-mshykhov-expense-ledger-bot-telegram-ledger-approval-gated-entries-outbox-google-sheets-projection-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `StockEntry` schema (no `state=PENDING_APPROVAL` column added), the `audit_logs` schema (no `StockEntryOutbox` table added), the waiter web UI, the cook Telegram bot (no `/approve <entry_id>` + `/reject <entry_id>` commands added), or any Google Sheets API integration (none added).

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (MIT permissive + 0★ + 233 KB substantial + 2026-09-13 pushed + 2026-09-13 created + verbatim 5-primitive quintuple = **observed event** for the push + **inferred** for the vocabulary transferability; confidence high for the *fresh-discovery-signal* / medium for the cross-section transferability)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (5-primitive quintuple + Telegram-ledger-vocabulary + verbatim description all recorded)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + size + description all verbatim; 2026-09-13 pushed + 2026-09-13 created confirmed by raw `created_at` + `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/246-*.md` + this HANDOFF file `specs/246-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v1 PR adopts the vocabulary**, the rollback path is: (1) drop the `state=PENDING_APPROVAL` column on `StockEntry` (Alembic migration downgrade); (2) drop the `StockEntryOutbox` SQLModel table; (3) drop the `sheets_projection_cursor` SQLModel table; (4) drop the `/approve <entry_id>` + `/reject <entry_id>` Telegram bot commands. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

For any future coding agent that picks up this contract, the mandatory skill load-out per `le31-coding-agent-brief/SKILL.md` is:
- `le31-conventions` — global decision layer; the seven-check gate
- `le31-v1-feature-pattern` — the v1 feature template (Goal / Scope / Out of scope / Description / Data model / Implementation steps / Telegram interaction / Dependencies / Open questions / Why this matters)
- `le31-data` — LE31 data-correctness rules
- `le31-backend` — FastAPI + SQLModel + Postgres conventions
- `le31-frontend` — HTMX + minimal HTML conventions (for any future owner-web-UI surface, e.g. a Sheets-projection-view)
- `le31-handoff-spec` — slice-contract authoring conventions
- `le31-coding-agent-brief` — paste-in prompt generation
- `le31-verification-protocol` — verification + rollback protocol
- `le31-quality-gates` — gates before merge
- `le31-arch-patterns` — FastAPI + aiogram + Postgres architectural patterns (including the approval-gating + transactional-outbox + Sheets-projection disciplinary patterns)
- `le31-data-correctness` — decimal EUR, timezone-aware instants, append-only invariants

Today's parent (Daily Brainstorm Cron) only READ the relevant skill files; no LE31 source code was touched.
