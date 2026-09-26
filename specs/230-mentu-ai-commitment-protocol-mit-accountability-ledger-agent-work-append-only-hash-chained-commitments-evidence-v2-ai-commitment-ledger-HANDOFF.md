# HANDOFF: feature 230 — `mentu-ai/commitment-protocol` (v2-AI commitment-ledger, defer parking-lot)

> **Date filed:** 2026-09-26
> **Author:** Daily Research Cron (LE31) — parent-verified override of subagent's proposed pick
> **Parent research issue:** [linear: blocked — see /opt/data/le31-daily-research-2026-09-26.linear-fallback.json]
> **Bucket:** v2-AI (parking-lot, future-v2-AI-surface-vocabulary-reference)
> **License:** MIT ✓ §3.2 STRICTLY-COMPATIBLE (vocabulary + architecture-reference adoption permitted; future code adoption possible)
> **Reference URL:** https://github.com/mentu-ai/commitment-protocol
> **Reference data:** MIT, 10★/4⑂, Python, 108 KB modest repo, pushed 2026-09-24T02:48:39Z (in-window by `pushed_at` only), created 2025-12-31T16:00:00Z (OUT-OF-WINDOW by ~9 months)

## Active feature path

`features/230-mentu-ai-commitment-protocol-mit-accountability-ledger-agent-work-append-only-hash-chained-commitments-evidence-v2-ai-commitment-ledger.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When an AI agent makes a commitment (e.g., "I will prepare Y"), and the operator wants to verify the commitment was honored, but today there's no record that ties the commitment to the closeout action, so that the operator has evidence the AI worked as claimed.* Maps onto charter §3.4. |
| 2 | Viability | ✅ | MIT permissive; org-account `mentu-ai`; 10★ community adoption; reference verifier is part of the artifact. |
| 3 | Practicability | ✅ | Python native; 108 KB small; MIT permissive vocabulary directly transferable. |
| 4 | Conflict | none | MIT permissive; no §3.4 customer-facing-AI; no stack conflict. |
| 5 | Outcome / appetite / scope | ✅ v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (108 KB); vocabulary-only; zero ongoing maintenance cost. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v2-AI build-trigger. The 8 named topics + the verbatim description are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/230-mentu-ai-commitment-protocol-...md` (the vocabulary contract; READ for context)
  - `specs/230-mentu-ai-commitment-protocol-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (inferred; medium-high for mechanism / low for present urgency; 10★ community signal)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/230-*.md` + this HANDOFF file `specs/230-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `commitment` + `commitment_evidence` + `commitment_hash_chain` tables; (2) drop the `/commitment status` + `/commitment close` commands; (3) drop the `/commitment show` + `/commitment verify` commands. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

When a future v2-AI PR triggers the artifact, the coding agent MUST load:
- `le31-conventions/SKILL.md` (always; the §3 hard invariants + the seven-check gate)
- `le31-v1-feature-pattern/SKILL.md` (for the v1-feature-pattern canonical contract shape — even though this is v2-AI, the contract shape carries over)
- `le31-feature-pipeline/SKILL.md` (for the feature-pipeline procedure)
- `le31-handoff-spec/SKILL.md` (for the slice handoff contract — this file is an example)
- `le31-coding-agent-brief/SKILL.md` (for the paste-in prompt to the coding agent)
- `le31-backend/SKILL.md` (for any SQLModel/Python/FastAPI work)
- `le31-data/SKILL.md` (for any data-model extension)
- `le31-frontend/SKILL.md` (for any web-UI extension)
- `le31-finance-analytics/SKILL.md` (for any EUR/tax-derivation work)

## Trigger condition

A future PR that adopts the artifact must explicitly note in its description: *"adopts the vocabulary from `features/230-mentu-ai-commitment-protocol-...md`"*, and must trigger **all** of:
- A `commitment` SQLModel table with `commitment_id, agent_id, opened_at, closed_at, evidence_id, hash_chain_link`
- A `commitment_evidence` SQLModel table with `evidence_id, commitment_id, evidence_type, evidence_payload, evidence_hash, recorded_at`
- A `commitment_hash_chain` SQLModel table with `link_id, prev_link_hash, current_commitments_root_hash, recorded_at`
- A `/commitment status` + `/commitment close <id> <evidence>` + `/commitment show <id>` + `/commitment verify <id>` Telegram command set on the cook-bot (operator-tooling; charter §3.4 NOT triggered)

Until the trigger fires, **no code is written, no schema is changed, no command is added**.

## Open questions for the owner / charter

- Will LE31 v2-AI ever introduce a commitment-ledger surface? If yes, the artifact is the vocabulary reference.
- Will LE31 v2-AI ever introduce a hash-chained audit log? If yes, the artifact is the vocabulary reference.
- Will LE31 v2-AI ever introduce an explicit *commitment* record vs the current `audit_logs` which records *state transitions* but not *commitments*?
- Will LE31 v2-AI ever introduce an evidence-tie primitive (every commitment paired with the evidence that proves it was honored)?
- Will LE31 v2-AI ever introduce an agent-accountability primitive (the ledger is specifically designed for AI agents, not for human operators)?
- **Open question that may kill any future PR**: who would ever run the offline verifier of a commitment-ledger? LE31 has exactly one stakeholder (the owner) who can just ask the AI what it did. The *commitment-ledger* may be over-engineering for a single-tenant single-operator scenario.

## Parent override rationale (recorded for transparency)

Subagent proposed 3 picks (`HannaneGhz/restaurant-order-bot` + `GabrielAlmeida-backend/restaurant-orders-api` + `siraj-motaung/orc-shark-api`); parent re-scored g5 (append-only+ledger) directly against raw JSON and surfaced 3 stronger candidates. This is the **3rd parent override of the 57-pass series** (prior overrides: 09-19 + 09-22; pattern established). Subagent's 3 picks were all 0★/0⑂/null-license/created-in-last-6-days = the **weakest candidates** of the 57-pass series. The parent-override picks (P1: `mentu-ai/commitment-protocol` MIT 10★/4⑂ + P2: `LinkedParticles/particles-standard` Apache-2.0 7★/0⑂ + P3: `lpalbou/AbstractGateway` MIT 4★/0⑂ with license upgrade `null → MIT`) have 10+7+4 = **21 stars total vs subagent's 0**. Per `le31-daily-research/SKILL.md` hard rule *"the subagent summary is a self-report, not a verified fact"*.

## Verification checklist

- [x] Active feature path documented: `features/230-mentu-ai-commitment-protocol-...md`
- [x] Seven-check gate verdict recorded (all 7 checks answered; verdict = `defer`)
- [x] Files to touch listed (READ ONLY; no edits)
- [x] Verification protocol referenced
- [x] Rollback path documented (delete the 3 files = complete rollback)
- [x] Mandatory LE31 skill list recorded
- [x] Trigger condition explicit (requires 3 SQLModel tables + 4 Telegram commands)
- [x] Open questions documented (6 questions; 1 that may kill any future PR)
- [x] Parent override rationale recorded for transparency