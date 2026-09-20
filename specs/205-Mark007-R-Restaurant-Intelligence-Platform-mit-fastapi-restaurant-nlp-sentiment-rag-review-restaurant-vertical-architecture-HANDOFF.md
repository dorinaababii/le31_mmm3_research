# 205 — Mark007-R-Restaurant-Intelligence-Platform-mit-fastapi-restaurant-nlp-sentiment-rag-review-restaurant-vertical-architecture HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 customer-feedback-ingest surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/205-Mark007-R-Restaurant-Intelligence-Platform-mit-fastapi-restaurant-nlp-sentiment-rag-review-restaurant-vertical-architecture.md` (defer artifact; **no code today**).

Bucket: **v1 restaurant-vertical reference (architecture-reference)**. Build verdict: **`defer`** (charter §3.1 + §3.4 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 owner wants to *ingest customer feedback* (e.g., from Google Reviews, Yelp, TripAdvisor) and surface a *measured-NLP summary* (sentiment + complaint classification), the owner wants *a single source of truth that records feedback with measurable quality*, but struggles because *v1 has no customer-feedback-ingest surface (v1 is waiter-web-UI + cook-Telegram-bot + StockEntry ledger; no sentiment, no complaint classification, no RAG chat)*, so that *v1 can offer customer-feedback-ingest without violating §3.1 (every state transition attributable) or §3.4 (no customer-facing AI)*." **PASS** (zero-pain today; v1 is small enough that customer-feedback is not a build-need; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; live on HuggingFace Spaces (no new infrastructure to inspect); no new stack dependencies; no new permissions. Confidence medium for the architectural match (the *measured-NLP + dual-surface + FastAPI* combination is well-established in the GitHub 1★-community-adoption cluster; MIT permissive license is charter-compatible per §3.2). Stack caveats: Redis ≠ LE31's Postgres-only stack; HuggingFace Spaces ≠ LE31's self-hosted deployment. **PASS**. |
| 4 | **Conflict** | None for the manager dashboard (operator-tooling = §3.4-permitted). **PARTIAL** for the customer app: customer-facing AI = charter §3.4 HARD-BLOCK unless non-AI-fallback is implemented; ripgrep-required on the customer-app code path before any v1 port. The *measured-NLP* primitive is §3.1 invariant-compatible. **PASS** (with §3.4 ripgrep-required condition for the customer-app port). |
| 5 | **Outcome, appetite, scope** | v1 restaurant-vertical reference (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/205-Mark007-R-Restaurant-Intelligence-Platform-mit-fastapi-restaurant-nlp-sentiment-rag-review-restaurant-vertical-architecture-HANDOFF.md` and `features/205-Mark007-R-Restaurant-Intelligence-Platform-mit-fastapi-restaurant-nlp-sentiment-rag-review-restaurant-vertical-architecture.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v1 architecture-review moment; §3.4 ripgrep-required condition for any future customer-app port).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a customer-feedback-ingest surface):

- `app/models/customer_feedback.py` — possibly add a `CustomerFeedback` SQLModel table (feedback_id, source, raw_text, sentiment_score, complaint_category, rag_retrieval_confidence, recorded_at, actor_user_id, customer_app_viewed_at).
- `app/models/complaint_category.py` — possibly add a `ComplaintCategory` enum (food_quality, service_speed, ambience, price, other).
- `app/models/rag_retrieval_log.py` — possibly add a `RAGRetrievalLog` SQLModel table (query, retrieved_documents, confidence_score).
- `app/api/feedback_ingest.py` — possibly add a `/v1/feedback/ingest` FastAPI route for staff to ingest customer feedback.
- `app/api/feedback_summary.py` — possibly add a `/v1/feedback/summary` FastAPI route for the manager dashboard to view measured-NLP summaries.
- `app/api/feedback_search.py` — possibly add a `/v1/feedback/search` FastAPI route for the customer app to keyword-search reviews (non-AI-fallback).
- `app/api/feedback_rag.py` — possibly add a `/v1/feedback/rag` FastAPI route for the customer app to RAG-chat over reviews (**charter §3.4 ripgrep-required**; non-AI-fallback must be implemented before shipping the customer-app view).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [x] `features/205-Mark007-R-Restaurant-Intelligence-Platform-mit-fastapi-restaurant-nlp-sentiment-rag-review-restaurant-vertical-architecture.md` exists and is read back by the parent.
- [x] `specs/205-Mark007-R-Restaurant-Intelligence-Platform-mit-fastapi-restaurant-nlp-sentiment-rag-review-restaurant-vertical-architecture-HANDOFF.md` (this file) exists and is read back by the parent.
- [x] The GitHub repo description is quoted verbatim: *"Restaurant intelligence with measured NLP - sentiment, complaint classification, and RAG chat over reviews - plus a manager dashboard and customer app. FastAPI + Redis + Docker serving layer, live on Hugging Face Spaces."*
- [x] The MIT permissive license is documented.
- [x] The *measured-NLP + sentiment + complaint classification + RAG chat over reviews + dual-surface + FastAPI + Redis + Docker + live-on-HuggingFace-Spaces* combination is documented.
- [x] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/` + INDEX.md row + parent research report file.

**Future v1 trigger (when the first v1 PR that adds a customer-feedback-ingest surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The *measured-NLP + sentiment + complaint classification + RAG chat over reviews + dual-surface* combination is evaluated against the PR's changes: does the change preserve *testable outputs (measured-NLP)*? Does the change add *sentiment + complaint classification*? Does the change add *RAG chat over reviews*? Does the change add *dual-surface (manager dashboard + customer app)*?
- [ ] **Charter §3.4 ripgrep required:** confirm the customer-app non-AI-fallback primitive is implemented before shipping the customer-app view.
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `CustomerFeedback` table; remove the new `ComplaintCategory` enum; remove the new `RAGRetrievalLog` table; remove the new `/v1/feedback/ingest` route; remove the new `/v1/feedback/summary` route; remove the new `/v1/feedback/search` route; remove the new `/v1/feedback/rag` route; restore the original schema.
- Migration cost: depends on the v1 change; the *measured-NLP + dual-surface + FastAPI* combination's design implies *additive schema* (the new `CustomerFeedback` + `RAGRetrievalLog` tables are additive on top of the existing StockEntry + audit_logs tables).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the verification log is a *new* document, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:

1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.

## 7. Handoff summary

| Field | Value |
|---|---|
| Feature ID | 205 |
| Slug | `Mark007-R-Restaurant-Intelligence-Platform-mit-fastapi-restaurant-nlp-sentiment-rag-review-restaurant-vertical-architecture` |
| Bucket | v1 restaurant-vertical reference (architecture-reference, parking-lot defer) |
| Parent research issue | linear: blocked (workspace plan limit; see /opt/data/le31-daily-research-2026-09-20.linear-fallback.json); intended title `Research 2026-09-20 — daily` |
| Linear sub-issue | linear: blocked (workspace plan limit); intended title `Feature 205 — Mark007-R-Restaurant-Intelligence-Platform-mit-fastapi-restaurant-nlp-sentiment-rag-review-restaurant-vertical-architecture` |
| Status today | defer (parking-lot) |
| No code today | yes |
| Verifiability today | feature file + HANDOFF file + INDEX.md row + parent research report file |
| Trigger condition (future v1) | first v1 PR that adds a customer-feedback-ingest surface (sentiment + complaint classification + RAG chat over reviews) |
| Disable path | delete `features/205-...md` + `specs/205-...-HANDOFF.md` |
| Migration cost | additive schema only (depends on v1 change) |
| Retained data | none |
| Parent research report | `/opt/data/le31-daily-research-2026-09-20.md` (52nd consecutive daily-research pass) |
| Raw fetches path | `/tmp/le31-daily-2026-09-20/` (68 files; anti-fabrication canary 0/67) |
| Linear fallback path | `/opt/data/le31-daily-research-2026-09-20.linear-fallback.json` |
| License | MIT ✓ (charter §3.2 compatible) |
| GitHub repo | `Mark007-R/Restaurant-Intelligence-Platform` (1star/0forks, Python, 8336 KB, pushed 2026-09-17T10:26:14Z) |
| Topics (verbatim) | none (empty array; description-only signals) |
| Description (verbatim) | *"Restaurant intelligence with measured NLP - sentiment, complaint classification, and RAG chat over reviews - plus a manager dashboard and customer app. FastAPI + Redis + Docker serving layer, live on Hugging Face Spaces."* |
| LE31-shape-score | 2 (description-only signals; *measured-NLP + sentiment + complaint classification + RAG chat over reviews + manager dashboard + customer app + FastAPI + Redis + Docker + live on Hugging Face Spaces*) |
| Companion artifacts | features 40, 42, 67, 77, 79, 83, 89, 110, 117, 153, 158, 165, 170, 176, 191, 203 (sister-pick A), 204 (sister-pick B) (ripgrep-verified distinct) |
| Sister-picks from 2026-09-20 | feature 203 (shawn-durrani/membro v2-AI control-plane), feature 204 (docentesIA/dagwell v2-AI orchestration) |
| Charter §3.4 ripgrep-required | YES — for the customer-app port (customer-facing AI = §3.4 HARD-BLOCK unless non-AI-fallback is implemented); the manager dashboard = operator-tooling §3.4-permitted without ripgrep |

## 8. Verification log

*(Empty — to be populated by the parent if/when the future v1 trigger condition fires.)*

---

**OPERATOR NOTE (2026-09-20):** Today's Linear MCP write endpoint returned a workspace plan-limit error (`You've exceeded the free issue limit for this workspace` — carry-over from 2026-09-19); per `le31-daily-research/SKILL.md` hard rule, the parent research issue + the 3 Linear sub-issues were NOT created today. The fallback JSON at `/opt/data/le31-daily-research-2026-09-20.linear-fallback.json` documents the intended issues for resync after the workspace quota resets. The feature files + HANDOFFs were written to the repo regardless, per spec hard rule *"treat the report file as the source of truth; the Linear issue is the index"*.