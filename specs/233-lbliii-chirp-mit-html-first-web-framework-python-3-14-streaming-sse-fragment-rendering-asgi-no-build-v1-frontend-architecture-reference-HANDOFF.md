# HANDOFF: feature 233 — `lbliii/chirp` (v1 frontend-architecture-reference, defer parking-lot)

> **Date filed:** 2026-09-26
> **Author:** Daily Brainstorm Cron (LE31) — parent-verified pick
> **Parent research issue:** [linear: blocked — see /opt/data/le31-brainstorm-2026-09-26.linear-fallback.json]
> **Bucket:** v1 frontend-architecture-reference (parking-lot, future-v1-frontend-architecture-evolution-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE** — permissive
> **Reference URL:** https://github.com/lbliii/chirp
> **Reference data:** MIT, 9★/2⑂, Python, 9471 KB substantial repo, pushed 2026-09-05T14:00:41Z (in-window by `pushed_at` only), created 2026-02-07T16:56:19Z (OUT-OF-WINDOW by ~6 months); **11/11 topics LE31-relevant = 100% topic-overlap score = the only 100% topic-overlap of any 2026-09 candidate**
> **HONEST DISCLOSURE:** chirp was surfaced as *adjacent-evidence* in features 54 + 210 (carry-over from 2026-08-10 + 2026-09-21 reports); **today's pick promotes it to a standalone v1 frontend-architecture-reference** because the 11/11 topic-overlap score is unique among 2026-09 candidates.

## Active feature path

`features/233-lbliii-chirp-mit-html-first-web-framework-python-3-14-streaming-sse-fragment-rendering-asgi-no-build-v1-frontend-architecture-reference.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When LE31 v1 considers evolving the existing HTMX stack to add streaming + SSE + fragment-rendering (e.g. for cook-ticket-streaming from cook-bot to waiter-web-UI), the maintainer wants a named framework-level primitive for the pattern, but today chirp is only referenced as adjacent-evidence, so that the v1 frontend-architecture-evolution has a vocabulary baseline to compare against.* Maps onto charter §3.1 + §3.2 + §3.4. |
| 2 | Viability | ✅ | MIT permissive; 9★ community adoption; 9471 KB substantial repo. |
| 3 | Practicability | ✅ | Python; existing FastAPI + uvicorn + HTMX stack already implements the *HTML-first + no-build + ASGI + htmx + hypermedia + server-sent-events* subset; the *streaming + fragment-rendering* primitive is small enough to independently re-implement in <100 LOC if needed. |
| 4 | Conflict | none | MIT permissive; no §3.4 customer-facing-AI; the *HTML-first + streaming + SSE + fragment-rendering* primitive is operator-tooling UI territory. |
| 5 | Outcome / appetite / scope | ✅ v1 | Reading-only artifact; no code today. |
| 6 | Cost vs operational value | ✅ | Moderate ingest (9471 KB); vocabulary-only artifact; zero ongoing maintenance. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1 frontend-architecture-evolution trigger. The 11 named topics + the verbatim description + the 7 named primitives are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/233-lbliii-chirp-...md` (the vocabulary contract; READ for context)
  - `specs/233-lbliii-chirp-...-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code, the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, or the cook Telegram bot.

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (vocabulary = inferred from the description + 11 topics + 7 named primitives; confidence medium-high for vocabulary transferability)
- [ ] All seven checks answered. ✅ (see table above)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; stars + topics + description all verbatim)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/233-*.md` + this HANDOFF file `specs/233-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v1 PR adopts the vocabulary**, the rollback path is: (1) drop the `hx-sse` HTMX attribute from the cook-status fragment; (2) revert the `text/event-stream` response type on the `cook_ticket_stream` FastAPI endpoint; (3) revert any Python 3.14+ free-threading evaluation PR. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

The external coding agent must load these skills before acting on this handoff:
- `le31-conventions` (global decision layer; verifies the seven-check gate)
- `le31-feature-pipeline` (turns the proposal into ready-to-build artefacts)
- `le31-v1-feature-pattern` (v1 feature template + pattern library)
- `le31-handoff-spec` (packages the decision into a frozen build contract)
- `le31-coding-agent-brief` (produces the paste-in prompt automatically from the slice contract)
- `development` (router for all coding work; decides process and next skill)
- `speckit-specify` (captures what/why for a feature before any code or plan)

## Trigger policy

Do NOT implement today. The artifact is a vocabulary-only reference; any future implementation must re-run the seven-check gate and re-verify the v1 stack-invariant posture (Python 3.13 stable in production; HTMX + FastAPI + uvicorn; charter §3.2). Trigger condition = first v1 PR that adopts the chirp *streaming + SSE + fragment-rendering* primitive for cook-ticket-streaming (e.g. a `hx-sse` HTMX attribute on the cook-status fragment + a `text/event-stream` FastAPI endpoint + a Python 3.14+ free-threading evaluation PR for uvicorn ASGI server).

## Distinct from existing features

The chirp vocabulary is **distinct from features 23 (`sse-cook-channel`) + 25 (`fastapi-frontend-dev-loop`) + 54 (`corner-mart POS reference`) + 142 (`feldroy-air-fastapi-htmx-ai-write-framework`) + 206 (`djust-org/djust`) + 210 (`duckframework/duck`)** because chirp is the *named framework-level support* for the primitive that features 23 + 25 + 210 implement ad-hoc (chirр provides a single framework that combines HTML-first + streaming + SSE + fragment-rendering + ASGI + free-threading; the existing features implement subsets of these primitives without a unifying framework). The chirp vocabulary is the *future-extension-vocabulary* for LE31 v1's frontend-architecture-evolution.
