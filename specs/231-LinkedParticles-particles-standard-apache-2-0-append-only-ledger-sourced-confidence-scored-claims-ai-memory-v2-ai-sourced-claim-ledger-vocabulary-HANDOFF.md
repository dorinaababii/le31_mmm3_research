# HANDOFF: feature 231 — `LinkedParticles/particles-standard` (v2-AI sourced-claim-ledger vocabulary, defer parking-lot)

> **Date filed:** 2026-09-26
> **Author:** Daily Research Cron (LE31) — parent-verified override of subagent's proposed pick
> **Parent research issue:** [linear: blocked — see /opt/data/le31-daily-research-2026-09-26.linear-fallback.json]
> **Bucket:** v2-AI (parking-lot, future-v2-AI-surface-vocabulary-reference)
> **License:** Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE (vocabulary + architecture-reference adoption permitted; future code adoption possible)
> **Reference URL:** https://github.com/LinkedParticles/particles-standard
> **Reference data:** Apache-2.0, 7★/0⑂, Python (vocabulary reference; serialization is JSON-LD/SHACL/RDF), 1116 KB substantial repo, pushed 2026-09-25T19:13:00Z (in-window by `pushed_at` only), created 2026-08-09T00:00:00Z (OUT-OF-WINDOW by ~7 weeks)

## Active feature path

`features/231-LinkedParticles-particles-standard-apache-2-0-append-only-ledger-sourced-confidence-scored-claims-ai-memory-v2-ai-sourced-claim-ledger-vocabulary.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When an AI surface extracts claims from documents, and the operator wants to verify each claim's source + confidence, but today there's no standard for serializing claim + source + confidence atomically, so that the AI's outputs are auditable and interopable.* Maps onto charter §3.4. |
| 2 | Viability | ✅ | Apache-2.0 permissive; org-account `LinkedParticles`; 7★ community adoption; whitepaper + SHACL shapes included. |
| 3 | Practicability | ✅ | Python + JSON-LD + SHACL; 1116 KB substantial; Apache-2.0 permissive vocabulary directly transferable. **Stack caveat**: JSON-LD/RDF is not LE31 v1's Postgres-only stack. |
| 4 | Conflict | none | Apache-2.0 permissive; no §3.4 customer-facing-AI; operator-tooling specification. |
| 5 | Outcome / appetite / scope | ✅ v2-AI | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (1116 KB); vocabulary-only artifact; the whitepaper is the load-bearing value. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v2-AI build-trigger. The 12 named topics + the verbatim description + the JSON-LD/SHACL/RDF serialization vocabulary are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/231-LinkedParticles-particles-standard-...md` (the vocabulary contract; READ for context)
  - `specs/231-LinkedParticles-particles-standard-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (inferred; medium for mechanism / low for present urgency; 7★ community signal)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + topics + description all verbatim)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/231-*.md` + this HANDOFF file `specs/231-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2-AI PR adopts the vocabulary**, the rollback path is: (1) drop the `claim` + `claim_source` + `claim_confidence_history` tables; (2) drop the `/claim list` + `/claim show` + `/claim verify` commands; (3) drop the JSON-LD `@context` + `@type` serialization layer. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

When a future v2-AI PR triggers the artifact, the coding agent MUST load:
- `le31-conventions/SKILL.md` (always; the §3 hard invariants + the seven-check gate)
- `le31-v1-feature-pattern/SKILL.md` (for the v1-feature-pattern canonical contract shape — even though this is v2-AI, the contract shape carries over)
- `le31-feature-pipeline/SKILL.md` (for the feature-pipeline procedure)
- `le31-handoff-spec/SKILL.md` (for the slice handoff contract — this file is an example)
- `le31-coding-agent-brief/SKILL.md` (for the paste-in prompt to the coding agent)
- `le31-backend/SKILL.md` (for any SQLModel/Python/FastAPI work)
- `le31-data/SKILL.md` (for any data-model extension; **JSON-LD/RDF serialization requires special data-model handling**)
- `le31-frontend/SKILL.md` (for any web-UI extension)
- `le31-finance-analytics/SKILL.md` (for any EUR/tax-derivation work)

## Trigger condition

A future PR that adopts the artifact must explicitly note in its description: *"adopts the vocabulary from `features/231-LinkedParticles-particles-standard-...md`"*, and must trigger **all** of:
- A `claim` SQLModel table with `claim_id, claim_text, claim_type, source_id, confidence_score, recorded_at, claim_hash`
- A `claim_source` SQLModel table with `source_id, source_type, source_uri, source_hash, retrieved_at`
- A `claim_confidence_history` SQLModel table with `confidence_id, claim_id, confidence_score, recorded_at, scoring_method`
- JSON-LD `@context` + `@type` serialization on the claim records (interop with external knowledge graphs)
- A `/claim list` + `/claim show <claim_id>` + `/claim verify <claim_id>` Telegram command set on the cook-bot (operator-tooling; charter §3.4 NOT triggered)

Until the trigger fires, **no code is written, no schema is changed, no command is added**.

## Open questions for the owner / charter

- Will LE31 v2-AI ever introduce a sourced-claim-ledger surface? If yes, the artifact is the vocabulary reference.
- Will LE31 v2-AI ever introduce a confidence-scored claim store? If yes, the artifact is the vocabulary reference.
- Will LE31 v2-AI ever introduce a JSON-LD/SHACL/RDF serialization layer? If yes, the artifact is the vocabulary reference.
- Will LE31 v2-AI ever introduce a knowledge-graph surface? If yes, the artifact is the vocabulary reference.
- Will LE31 v2-AI ever introduce an external-knowledge-graph interop surface? If yes, the artifact is the vocabulary reference.
- **Open question that may kill any future PR**: who would ever need to consume a JSON-LD/SHACL/RDF serialization of LE31's internal claim ledger? LE31's owner is the only stakeholder; external interop with the broader semantic-web ecosystem is unlikely for a single-restaurant operations system.

## Parent override rationale (recorded for transparency)

Subagent proposed 3 picks (`HannaneGhz/restaurant-order-bot` + `GabrielAlmeida-backend/restaurant-orders-api` + `siraj-motaung/orc-shark-api`); parent re-scored g5 (append-only+ledger) directly against raw JSON and surfaced 3 stronger candidates. This is the **3rd parent override of the 57-pass series** (prior overrides: 09-19 + 09-22; pattern established). Subagent's 3 picks were all 0★/0⑂/null-license/created-in-last-6-days = the **weakest candidates** of the 57-pass series. The parent-override picks (P1: `mentu-ai/commitment-protocol` MIT 10★/4⑂ + P2: `LinkedParticles/particles-standard` Apache-2.0 7★/0⑂ + P3: `lpalbou/AbstractGateway` MIT 4★/0⑂ with license upgrade `null → MIT`) have 10+7+4 = **21 stars total vs subagent's 0**. Per `le31-daily-research/SKILL.md` hard rule *"the subagent summary is a self-report, not a verified fact"*.

## Verification checklist

- [x] Active feature path documented: `features/231-LinkedParticles-particles-standard-...md`
- [x] Seven-check gate verdict recorded (all 7 checks answered; verdict = `defer`)
- [x] Files to touch listed (READ ONLY; no edits)
- [x] Verification protocol referenced
- [x] Rollback path documented (delete the 3 files = complete rollback)
- [x] Mandatory LE31 skill list recorded
- [x] Trigger condition explicit (requires 3 SQLModel tables + JSON-LD serialization + 3 Telegram commands)
- [x] Open questions documented (6 questions; 1 that may kill any future PR)
- [x] Parent override rationale recorded for transparency