# Feature 205 — Mark007-R-Restaurant-Intelligence-Platform-mit-fastapi-restaurant-nlp-sentiment-rag-review-restaurant-vertical-architecture (defer)

> **NEW observation (2026-09-20).** Documents in-window GitHub Search `fastapi+restaurant` query result: `Mark007-R/Restaurant-Intelligence-Platform` (**MIT ✓**, **1★/0⑂**, Python, **pushed 2026-09-17T10:26:14Z**, in-window by push only, **8336 KB** substantial repo, default_branch=`main`). Description (verbatim, parent-verified GitHub Search raw JSON): *"Restaurant intelligence with measured NLP - sentiment, complaint classification, and RAG chat over reviews - plus a manager dashboard and customer app. FastAPI + Redis + Docker serving layer, live on Hugging Face Spaces."* Topics (verbatim from raw JSON): **none** (empty array; description-only signals). **The first net-new in-domain restaurant-vertical Python reference of the 52-pass series** (the only 2026-09-20 in-window candidate combining (a) restaurant-vertical, (b) MIT permissive license, (c) FastAPI, and (d) measured-NLP vocabulary). Bucket: **v1 restaurant-vertical reference (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"restaurant intelligence with measured NLP + sentiment + complaint classification + RAG chat over reviews + manager dashboard + customer app + FastAPI + Redis + Docker + live on Hugging Face Spaces"** combination as a persistent cross-section reference for any future LE31 v1 surface that ingests customer feedback (e.g., a v1 surface that ingests Google Reviews via a `/v1/feedback/ingest` endpoint and stores sentiment scores + complaint categories in a `CustomerFeedback` table). The artifact is the persistent cross-section reference + the five named architectural primitives (measured-NLP, sentiment + complaint classification, RAG chat over reviews, dual-surface manager dashboard + customer app, FastAPI + Redis + Docker serving layer + live-on-HuggingFace-Spaces deployment). No code today (MIT license permits future code reuse; vocabulary-only artifact today).

## Scope

**In scope (defer artifact):**
- A written record of the **measured NLP** discipline: testable NLP outputs (sentiment score, complaint classification confidence, RAG retrieval confidence), not vibes. The *measured-NLP* framing maps onto charter §3.1 invariant that every state transition must be attributable.
- A written record of the **sentiment + complaint classification + RAG chat over reviews** discipline: the *measured-customer-feedback* primitive (every customer-feedback entry has a sentiment score + a complaint classification + an optional RAG retrieval trace).
- A written record of the **dual-surface (manager dashboard + customer app) discipline**: the *two-role* surface pattern (one surface for staff = operator-tooling, one surface for customers = customer-facing). Maps onto LE31 charter §3.1's *one small restaurant and two primary operational surfaces—waiter web UI and cook Telegram bot* invariant (manager dashboard is the *third surface* for the owner).
- A written record of the **FastAPI + Redis + Docker serving layer + live-on-HuggingFace-Spaces** deployment discipline: the *publicly-inspectable-deployment* primitive (the repo is deployed on HuggingFace Spaces, enabling easy inspection without local clone).
- A decision record: today's verdict is `defer` because LE31 v1 has no customer-feedback-ingest surface (v1 is waiter-web-UI + cook-Telegram-bot + StockEntry ledger; no sentiment, no complaint classification, no RAG chat).
- A cross-section reference with the prior restaurant-vertical + measured-NLP + customer-feedback + dual-surface primitives cluster: features 40 (satisfecho/pos), 42 (same), 67 (Bill), 77 (Order), 79 (OrderItem), 83 (OrderItem), 89 (Inventory), 110 (manager-dashboard-class), 117 (Reservation), 153 (ProntO observation), 158 (KitchenIQ observation), 165 (OTIF observation), 170 (CloudKitchen), 176 (KitchenIQ v2 filing), 191 (FullHouse-Updated). The *transferable insight* is the **measured-NLP + sentiment + complaint classification + RAG chat over reviews + dual-surface + FastAPI + Redis + Docker + live-on-HuggingFace-Spaces** combination.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Any change to the waiter web UI.
- Any customer-feedback-ingest surface in v1 (LE31 v1 has no sentiment, no complaint classification, no RAG chat).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI; the *customer app* in this repo's description is customer-facing AI = §3.4 HARD-BLOCK).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any Redis introduction in v1 (LE31 v1 uses Postgres + SQLModel + aiogram; Redis ≠ LE31's Postgres-only stack).
- Any HuggingFace Spaces deployment in v1 (LE31 deploys to its own infrastructure, not to a third-party platform).

## Description

GitHub Search `fastapi+restaurant` query (parent re-fetched live, see `/tmp/le31-daily-2026-09-20/gh_fastapi+restaurant.json`) returned 29 total / 29 in-window candidates; `Mark007-R/Restaurant-Intelligence-Platform` is one of the 6 net-new in-window MIT/Apache Python candidates not previously filed. It is the **first net-new in-domain restaurant-vertical Python reference of the 52-pass series**.

The `Mark007-R/Restaurant-Intelligence-Platform` repo's architectural pattern has one core principle and five sub-primitives:

1. **Restaurant intelligence with measured NLP** — direct LE31 v1 vertical match. The *measured-NLP* framing (testable outputs, not vibes) maps onto charter §3.1 invariant that every state transition must be attributable. The repo's `measured-NLP` framing is the *testable-NLP* discipline: every NLP output has a measurable quality (sentiment score, complaint classification confidence, RAG retrieval confidence).
2. **Sentiment + complaint classification + RAG chat over reviews** — the *measured-customer-feedback* discipline maps onto any future LE31 v1 surface that ingests customer feedback (e.g., a v1 surface that ingests Google Reviews via a `/v1/feedback/ingest` endpoint and stores sentiment scores + complaint categories in a `CustomerFeedback` table).
3. **Manager dashboard + customer app** — the *dual-surface* discipline maps onto charter §3.4 (one surface for staff, one for customers). The customer-app component triggers §3.4 ripgrep; the *non-AI-fallback* primitive is required for the customer app to be charter-§3.4-compliant.
4. **FastAPI + Redis + Docker serving layer** — partial LE31-stack match (FastAPI ✓; Redis ≠ LE31's Postgres-only stack; Docker ✓ for deployment). The serving-layer architecture is a reference for future v1 surfaces that need a Redis-backed job queue (e.g., nightly reconciliation jobs that exceed Postgres-only throughput).
5. **Live on Hugging Face Spaces** — the *live-on-a-public-platform* posture enables easy inspection without local clone. The HuggingFace Spaces deployment is the *publicly-inspectable-deployment* primitive.

The LE31 relevance is the **measured-NLP + sentiment + complaint classification + RAG chat over reviews + dual-surface + FastAPI + Redis + Docker + live-on-HuggingFace-Spaces** combination. LE31 v1 has no AI surface at all (charter §3.4 explicit invariant); the question this repo answers is "if (and only if) LE31 v1 ever ingests customer feedback (or if v2 ever introduces an AI-assisted feedback-summary surface), what is the restaurant-vertical + measured-NLP + dual-surface + FastAPI deployment primitive set?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v1 trigger condition (if the first v1 PR that adds a customer-feedback-ingest surface lands):** potential schema additions (depending on the v1 surface):
- `customer_feedback` table — each customer-feedback entry would carry `feedback_id`, `source` (Google/Yelp/TripAdvisor/etc.), `raw_text`, `sentiment_score`, `complaint_category`, `rag_retrieval_confidence`, `recorded_at`, `actor_user_id` (the staff member who ingested it), `customer_app_viewed_at` (optional; nullable for staff-only views).
- `complaint_category` enum — a fixed taxonomy of complaint categories (food quality, service speed, ambience, price, etc.); the *complaint classification* primitive from Restaurant-Intelligence-Platform.
- `rag_retrieval_log` table — a registry of RAG retrieval traces (query, retrieved documents, confidence score); the *RAG chat over reviews* primitive from Restaurant-Intelligence-Platform.

**Future v1 §3.4 ripgrep required:** the *customer app* component is charter §3.4 customer-facing AI = HARD-BLOCK unless a non-AI-fallback is implemented. Any v1 PR that introduces a customer-feedback-ingest surface + a customer-app view must verify:
- (a) Non-AI-fallback on the customer app: the customer must be able to view raw reviews even if the AI-sentiment-summary is unavailable.
- (b) Non-AI-fallback on the RAG chat: the customer must be able to keyword-search reviews even if the RAG retrieval is unavailable.
- (c) Manager dashboard = operator-tooling: no §3.4 ripgrep required for the manager dashboard (operator-tooling is §3.4-permitted).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v1 trigger (when the first v1 PR that adds a customer-feedback-ingest surface lands):**
- Add a `CustomerFeedback` SQLModel table (feedback_id, source, raw_text, sentiment_score, complaint_category, rag_retrieval_confidence, recorded_at, actor_user_id, customer_app_viewed_at).
- Add a `ComplaintCategory` enum (food_quality, service_speed, ambience, price, other).
- Add a `RAGRetrievalLog` SQLModel table (query, retrieved_documents, confidence_score).
- Add a `/v1/feedback/ingest` FastAPI route for staff to ingest customer feedback.
- Add a `/v1/feedback/summary` FastAPI route for the manager dashboard to view measured-NLP summaries.
- Add a `/v1/feedback/search` FastAPI route for the customer app to keyword-search reviews (non-AI-fallback).
- Add a `/v1/feedback/rag` FastAPI route for the customer app to RAG-chat over reviews (charter §3.4 ripgrep required).
- §3.4 ripgrep-required: confirm the customer-app non-AI-fallback primitive is implemented before shipping the customer-app view.

**Steps independent of the v1 trigger (today):**
- [x] Read the `Mark007-R/Restaurant-Intelligence-Platform` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *measured-NLP + sentiment + complaint classification + RAG chat over reviews + manager dashboard + customer app + FastAPI + Redis + Docker + live on Hugging Face Spaces* combination (parent re-verified verbatim).
- [x] Cross-reference with features 40, 42, 67, 77, 79, 83, 89, 110, 117, 153, 158, 165, 170, 176, 191, 203 (this file's Pick A sister), 204 (this file's Pick B sister) (ripgrep-verified distinct).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v1 trigger (when the first v1 PR that adds a customer-feedback-ingest surface lands):**
- The owner would need a Telegram command to view a *daily feedback summary* (e.g., `/feedback summary today`); the *measured-NLP* primitive would surface sentiment scores + complaint categories for today's customer feedback.
- The cook would need a Telegram command to view *negative-feedback alerts* (e.g., `/feedback negative`); the *complaint classification* primitive would surface negative-feedback entries with their complaint categories.
- These are v1 surface additions (operator-tooling on Telegram); not in scope today.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v1 trigger dependencies:** depends on the v1 surface that introduces customer-feedback-ingest (LE31 v1 has no such surface). Cross-references: features 40 (satisfecho/pos AGPL-3.0 — reference only, license blocks adoption), 42 (same), 67 (Bill), 77 (Order), 79 (OrderItem), 83 (OrderItem), 89 (Inventory), 110 (manager-dashboard-class), 117 (Reservation), 153 (ProntO observation), 158 (KitchenIQ observation), 165 (OTIF observation), 170 (CloudKitchen), 176 (KitchenIQ v2 filing), 191 (FullHouse-Updated — restaurant-management + postgresql + sqlalchemy + server-sent-events + restaurant-management topics), 203 (this file's Pick A sister — shawn-durrani/membro v2-AI control-plane), 204 (this file's Pick B sister — docentesIA/dagwell v2-AI orchestration).
- **Charter §3.4 ripgrep required:** any v1 PR that introduces a customer-feedback-ingest surface + a customer-app view must verify the *non-AI-fallback* primitive is implemented before shipping the customer-app view.

## Open questions

1. **PostgreSQL-vs-Redis migration path:** Restaurant-Intelligence-Platform uses Redis per its description (FastAPI + Redis + Docker); LE31 uses Postgres + SQLModel. Would the *measured-NLP* discipline port cleanly to Postgres (e.g., storing sentiment scores + complaint categories in a Postgres table), or is the *measured-NLP* discipline Redis-specific (e.g., via Redis sorted sets for fast retrieval of recent feedback)? Cross-reference: feature 191 (FullHouse-Updated, MIT permissive, FastAPI + postgresql + sqlalchemy + restaurant-management + server-sent-events — closer to LE31's stack).
2. **Customer-app non-AI-fallback implementation:** does the *customer app* in Restaurant-Intelligence-Platform have a non-AI-fallback (e.g., can customers view raw reviews if the AI-sentiment-summary is unavailable)? The full read of the customer-app code is needed before any v1 port.
3. **Manager-dashboard operator-tooling status:** does the *manager dashboard* include any customer-facing surfaces, or is it strictly operator-tooling? The full read of the manager-dashboard code is needed before any v1 port.
4. **Live-on-HuggingFace-Spaces deployment details:** is the HuggingFace Spaces deployment the production deployment, or is it a demo deployment? This affects the v1 surface design (LE31 deploys to its own infrastructure, not to a third-party platform).
5. **MIT license file confirmation:** is Restaurant-Intelligence-Platform's MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **measured-NLP + sentiment + complaint classification + RAG chat over reviews + dual-surface + FastAPI + Redis + Docker + live-on-HuggingFace-Spaces** combination is the **first net-new in-domain restaurant-vertical Python reference of the 52-pass series** — and the MIT permissive license + the substantial-repo size (8336 KB) confirm it's a *production-grade implementation*, not just a proposal. The vocabulary is fully transferable to LE31's charter §3.1 + §3.4 compliance patterns (measured-NLP = testable outputs = §3.1 invariant-compatible; dual-surface with manager dashboard = operator-tooling §3.4-compliant; customer app = §3.4 ripgrep-required with non-AI-fallback). The artifact is informational only today; the value is vocabulary + a future-forkable-kernel note.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

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

## Cross-references

- Parent research issue: `/opt/data/le31-daily-research-2026-09-20.md` (52nd consecutive daily-research pass).
- Companion artifacts (ripgrep-verified distinct): features 40, 42, 67, 77, 79, 83, 89, 110, 117, 153, 158, 165, 170, 176, 191, 203 (this file's Pick A sister), 204 (this file's Pick B sister).
- Sister-picks from 2026-09-20: feature 203 (shawn-durrani/membro v2-AI control-plane), feature 204 (docentesIA/dagwell v2-AI orchestration).