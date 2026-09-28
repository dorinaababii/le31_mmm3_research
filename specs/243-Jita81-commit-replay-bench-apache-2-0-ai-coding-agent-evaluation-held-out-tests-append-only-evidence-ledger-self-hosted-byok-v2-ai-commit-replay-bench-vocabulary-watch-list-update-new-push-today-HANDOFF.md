# HANDOFF: feature 243 — `Jita81/commit-replay-bench` (v2-AI commit-replay-bench-vocabulary, defer parking-lot, watch-list update to feature 220)

> **Date filed:** 2026-09-28
> **Author:** Daily Research Cron (LE31) — watch-list update to feature 220 (filed 2026-09-23)
> **Parent research issue:** [linear: blocked — see /opt/data/le31-daily-research-2026-09-28.linear-fallback.json]
> **Bucket:** v2-AI commit-replay-bench-vocabulary (parking-lot, future-v2-AI-surface-vocabulary-reference; watch-list update to feature 220)
> **License:** **Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/Jita81/commit-replay-bench
> **Reference data:** Apache-2.0, 0★/0⑂, Python, **16413 KB** (was 5066 KB on 09-23 = **+11347 KB / +224% in 5 days = 4th-consecutive-day NEW PUSH streak = the biggest sustained-active-developer signal of the 59-pass series**), pushed **2026-09-28T06:20:04Z = TODAY** (was 2026-09-23T05:51:17Z on 09-23 filing day)

## Active feature path

`features/243-Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-vocabulary-watch-list-update-new-push-today.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v2-AI surface proposes AI-coding-agent-evaluation + append-only-evidence-ledger + class-of-change-routing, the owner wants the verbatim 5-tuple-primitive vocabulary from a real-world 2026 evidence-ledger, but today LE31 has no AI surface at all (charter §3.4), so that the future v2-AI surface has a documented reference.* Maps onto charter §3.4. |
| 2 | Viability | ✅ | Apache-2.0 permissive; 0★/0⑂ community but **+11347 KB / +224% in 5 days = 4th-consecutive-day NEW PUSH streak = biggest sustained-active-developer signal of the 59-pass series for any candidate**. |
| 3 | Practicability | ⚠️ | Python + Apache-2.0 permissive + commit-replay + held-out-tests + append-only evidence ledger vocabulary. **Stack caveat**: held-out-tests + class-of-change-routing is novel infrastructure that LE31 v1 does not have; future v2-AI adoption would require designing new surfaces (held-out-tests, AI-evaluation-ledger, class-of-change-routing). |
| 4 | Conflict | none | Apache-2.0 permissive; no §3.4 customer-facing-AI (this is operator-tooling-AI evaluation; the operator reads the evidence ledger; no restaurant diner interacts with the AI-coding-agent). |
| 5 | Outcome / appetite / scope | ✅ v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (16413 KB; comfortably readable); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference; watch-list update to feature 220).** No build time spent. The cross-section reference is informative, not a v2-AI build-trigger. The verbatim description + the 5 named primitives + the **+11347 KB / +224% in 5 days sustained-active-developer signal** are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/243-Jita81-commit-replay-bench-...md` (the vocabulary contract; READ for context)
  - `specs/243-Jita81-commit-replay-bench-...-HANDOFF.md` (this file; READ for context)
  - `features/220-Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-evidence-ledger.md` (the predecessor feature file; READ for context)
  - `specs/220-Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-evidence-ledger-HANDOFF.md` (the predecessor HANDOFF file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (2026-09-28 NEW PUSH + Apache-2.0 permissive + 5 named primitives + +11347 KB / +224% in 5 days sustained-discovery signal = **observed event** for the push + **inferred** for the vocabulary; confidence high for mechanism / low for present urgency)
- [ ] All seven checks answered. ✅ (see table above; check 3 carries the stack caveat)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot, watch-list update to feature 220`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (stack caveat explicitly recorded; the original feature 220 observation is unchanged)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim; 2026-09-28 pushed confirmed by raw `pushed_at`; size delta +11347 KB / +224% confirmed by raw `size` field vs the 09-23 baseline)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/243-*.md` + this HANDOFF file `specs/243-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `commit_replay_verdict` + `held_out_test_set` + `class_of_change_routing` tables; (2) drop the `/ai_eval_history` + `/ai_eval_replay` commands. All future rollbacks are explicit because the artifact is read-only.

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
