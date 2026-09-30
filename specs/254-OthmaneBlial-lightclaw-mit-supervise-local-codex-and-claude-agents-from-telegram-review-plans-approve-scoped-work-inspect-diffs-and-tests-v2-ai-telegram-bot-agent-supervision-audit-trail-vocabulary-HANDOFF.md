# HANDOFF: feature 254 — `OthmaneBlial/lightclaw` (v2-AI Telegram-bot agent-supervision + audit-trail + human-in-the-loop vocabulary reference, defer parking-lot)

> **Date filed:** 2026-09-30
> **Author:** Daily Brainstorm Cron (LE31) — parent-verified pick
> **Parent research issue:** Brainstorm 2026-09-30 — daily (Linear parent index)
> **Bucket:** v2-AI Telegram-bot agent-supervision + audit-trail + human-in-the-loop primitive (parking-lot, future-v2-AI-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/OthmaneBlial/lightclaw
> **Reference data:** MIT, 21★/3⑂, Python, 6432 KB substantial repo, pushed **2026-09-30T06:53:31Z = TODAY** (in-window by `pushed_at` = strongest fresh-discovery signal of the 62-pass brainstorm series), created **2026-02-16T21:13:58Z** (~7.5 months before window-start = OUT-OF-WINDOW by `created_at` = in-window by push only)

## Active feature path

`features/254-OthmaneBlial-lightclaw-mit-supervise-local-codex-and-claude-agents-from-telegram-review-plans-approve-scoped-work-inspect-diffs-and-tests-v2-ai-telegram-bot-agent-supervision-audit-trail-vocabulary.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v2-AI surface introduces AI-assisted owner/staff workflows (e.g., menu-pricing-suggestion, prep-scheduling-suggestion, supplier-reorder-suggestion), the owner wants the AI to **not act unilaterally** but to **propose each step + wait for human approval + leave an audit trail**, but LE31 today has no agent-supervision surface (charter §3.4 explicit invariant: NO customer-facing AI + LE31 v1 has no AI surface at all), so that the future v2-AI surface has a documented reference.* Maps to charter §3.4 (operator-tooling-AI with observable evidence + non-AI fallback). |
| 2 | Viability | ✅ | MIT permissive; 21★/3⑂ community; TODAY's fresh-push = strongest fresh-discovery signal of the 62-pass brainstorm series. |
| 3 | Practicability | ✅ | Python + Telegram-bot + audit-trail + human-in-the-loop = all on-LE31-stack-vocabulary-envelope; requires aiogram-equivalent-Telegram-bot-vocabulary (LE31 v1 has aiogram v3). |
| 4 | Conflict | none | MIT permissive; *supervise-local-AI-coding-agents-from-Telegram* surface is **operator-tooling-AI** (charter §3.4-compatible: the supervisor watches AI-agents, no customer-facing interaction); *audit-trail + human-in-the-loop* = charter §3.4's *observable-evidence + non-AI-fallback* requirement satisfied. |
| 5 | Outcome / appetite / scope | ✅ v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (6432 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v2-AI build-trigger. The verbatim description + the 5 named primitives + the TODAY fresh-push + the 15 topics + the 6432 KB substantial-repo size are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/254-OthmaneBlial-lightclaw-...md` (the vocabulary contract; READ for context)
  - `specs/254-OthmaneBlial-lightclaw-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [x] Evidence and confidence recorded. ✅ (2026-02-16 created + 2026-09-30 pushed-TODAY + MIT permissive + 15 topics + 5 named primitives + 21★/3⑂ community traction = **observed event** for the push + **inferred** for the vocabulary; confidence medium for mechanism / low for present urgency)
- [x] All seven checks answered. ✅ (see table above; all checks pass cleanly)
- [x] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [x] No unresolved source-of-truth conflict was guessed through. ✅ (no caveats; charter §3.4-compatible via audit-trail + human-in-the-loop)
- [x] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2026-02-16 created + 2026-09-30 pushed-TODAY confirmed by raw `created_at` + `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/254-*.md` + this HANDOFF file `specs/254-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `AgentAction` + `AgentSupervisor` + `AgentAuditTrail` + `CodeReview` tables; (2) drop the *supervisor-bot* Telegram-bot-channel + the agent-supervision FastAPI endpoints. All future rollbacks are explicit because the artifact is read-only.

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