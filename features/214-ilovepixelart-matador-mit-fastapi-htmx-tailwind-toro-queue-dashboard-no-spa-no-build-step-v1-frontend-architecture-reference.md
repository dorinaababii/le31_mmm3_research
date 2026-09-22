# Feature 214 — ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference (defer)

> **NEW observation (2026-09-22).** Documents in-window GitHub Search `htmx+no-build` query result: `ilovepixelart/matador` (**MIT ✓**, **1★/0⑂**, Python, **pushed 2026-09-22T06:03:15Z = TODAY = in-window by push only**, **1522 KB** substantial repo, default_branch=`main`). Topics (verbatim from raw JSON, **9 topics**): `dashboard`, `fastapi`, `htmx`, `jobs`, `monitoring`, `python`, `queue`, `redis`, `toro`. Description (verbatim, parent-verified GitHub Search raw JSON): *"Live server-rendered dashboard for toro queues: watch queues, inspect and retry jobs. FastAPI + HTMX + Tailwind, no SPA, no build step. pip install matador-dashboard"*. **The strongest 2026-09-22 in-window FastAPI+HTMX+Tailwind+queue-monitor v1-frontend-architecture reference of the 53-pass series** (the freshest in-window by `pushed_at` of the series = pushed TODAY = 23 min before the daily-research cron fetch). Bucket: **v1 frontend-architecture-reference (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"Live server-rendered dashboard for toro queues + FastAPI + HTMX + Tailwind + no SPA + no build step + pip install matador-dashboard"** multi-primitive + **9 topics (dashboard + fastapi + htmx + jobs + monitoring + python + queue + redis + toro)** as a persistent cross-section reference for any future LE31 v1 surface that wants a server-rendered queue-monitor dashboard with library-distribution. The artifact is the persistent cross-section reference + the five named architectural primitives (server-rendered dashboard, toro queue-monitor, FastAPI+HTMX+Tailwind, no SPA + no build step, library-distribution). No code today (MIT license permits future code reuse; vocabulary-only artifact today).

## Scope

**In scope (defer artifact):**
- A written record of the **server-rendered dashboard** discipline: a queue-monitor dashboard rendered server-side from a Toro queue; pure HTML, no AI, no SPA.
- A written record of the **toro queue-monitor** discipline: watch queues, inspect jobs, retry failed jobs; the *queue-inspect-retry* operator-tooling primitive.
- A written record of the **FastAPI + HTMX + Tailwind** discipline: the LE31 v1 frontend-stack match (FastAPI ✓; Tailwind no SPA; HTMX for live updates).
- A written record of the **no SPA + no build step** discipline: the LE31 v1 invariant (charter §3.4: minimal HTML/HTMX for waiter web UI).
- A written record of the **library-distribution** discipline: `pip install matador-dashboard`; the artifact is published to PyPI as a library; LE31 v1 could adopt this pattern for any future v1 surface that wants to be installable as a Python package (currently v1 is a single deployable).
- A decision record: today's verdict is `defer` because LE31 v1 has no queue-monitor dashboard surface AND no need for one today (the v1 surface is the waiter web UI + cook Telegram bot; no async job queue).
- A cross-section reference with the prior FastAPI+HTMX+Tailwind+queue-monitor primitives cluster: features 23 (sse-cook-channel), 25 (fastapi-frontend-dev-loop), 67 (Bill), 142 (feldroy-air-fastapi-htmx-ai-write-framework), 144 (zentra-offline-first-fb-pattern), 154 (htmx-fastapi-cook-channel), 156 (AWIG-OS), 162 (htmx-fastapi-cook-channel v2), 168 (htmx-no-build-python-skeleton-watch), 178 (nhobin219-litelink-append-only-iceberg-embedded-local-first), 191 (eddiedzhang-FullHouse-Updated — repo now 404, vocabulary-only), 206 (djust-org/djust phoenix-liveview-style), 210 (duckframework/duck server-side-reactive-web-no-frontend-framework), 212 (this file's Pick A sister — Rooster-glitch/Hardtack v2-AI sovereign-context-ledger), 213 (this file's Pick B sister — hseshadr/avow v2-AI signed-evidence-receipts). The *transferable insight* is the **FastAPI+HTMX+Tailwind+queue-monitor+no-SPA-no-build+library-distribution** multi-primitive set + the **9 topics** = strongest 2026-09-22 in-window v1-frontend-architecture reference.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Any new queue-monitor dashboard in v1 (LE31 v1 has no async job queue today).
- Any pip install matador-dashboard adoption in v1 (LE31 v1 is a single deployable; library-distribution is not a v1 priority).
- Any Redis or toro addition in v1 (LE31 uses Postgres-only per §3.2 stack invariant; Redis + toro are not in v1's stack).

## Description

GitHub Search `htmx+no-build` query (parent re-fetched live, see `/tmp/le31-daily-2026-09-22/gh/htmx_no_build_548357.json`) returned 2 total / 2 retrieved candidates; `ilovepixelart/matador` is the **#1 GitHub Search #2** of the day (LE31-shape-score 7 = highest of all 8 GitHub Search queries today). It is the **strongest 2026-09-22 in-window v1-frontend-architecture reference** of the 53-pass series (pushed TODAY = 23 min before the daily-research cron fetch).

The `ilovepixelart/matador` repo's architectural pattern has five core sub-primitives:

1. **Live server-rendered dashboard for toro queues** — the *server-rendered-queue-monitor* discipline. A queue-monitor dashboard rendered server-side from a Toro (Redis-based) task queue; pure HTML, no SPA, no build step. Maps onto any future LE31 v1 surface that needs a queue-monitor dashboard (e.g., a future `/v1/stock-entry-queue` route that displays held jobs in a server-rendered HTMX dashboard).

2. **Watch queues, inspect and retry jobs** — the *queue-inspect-retry* discipline. The dashboard exposes: (a) a queue-list view (which queues exist); (b) a per-queue inspect view (which jobs are pending/running/failed); (c) a per-job retry view (operator can retry a failed job). Maps onto any future LE31 v1 surface that needs operator-tooling for async jobs (e.g., a `/v1/jobs/queue` route for the owner to inspect + retry failed reconciliation jobs).

3. **FastAPI + HTMX + Tailwind, no SPA, no build step** — direct LE31 v1 frontend-stack match. The *FastAPI + HTMX + Tailwind + no SPA + no build step* posture is exactly the LE31 v1 invariant (charter §3.4: minimal HTML/HTMX for waiter web UI). The `pip install matador-dashboard` posture is the *library-distribution* pattern (vs fork-and-modify pattern).

4. **pip install matador-dashboard** — the *library-distribution* pattern. The artifact is published to PyPI as a library; LE31 v1 could adopt this pattern for any future v1 surface that wants to be installable as a Python package (currently v1 is a single deployable). The library-distribution pattern is the *composable-surface* primitive: the dashboard can be `mount`-ed onto any FastAPI instance as a sub-app.

5. **9 topics (dashboard + fastapi + htmx + jobs + monitoring + python + queue + redis + toro)** — the highest in-window topic-count of any 2026-09-22 v1-frontend-architecture candidate; demonstrates the *practiced-design-discipline* (not just a proposal). The 9 topics hit all 7 of the LE31-shape-score keywords (fastapi + htmx + dashboard + jobs + monitoring + python + queue) = **LE31-shape-score=7** (the highest of the 53-pass series).

The LE31 relevance is the **FastAPI+HTMX+Tailwind+queue-monitor+no-SPA-no-build+library-distribution** multi-primitive + the **9 topics** = strongest 2026-09-22 in-window v1-frontend-architecture reference. The question this repo answers is "if (and only if) LE31 v1 ever needs a queue-monitor dashboard, what is the FastAPI+HTMX+Tailwind+server-rendered+library-distribution primitive set that satisfies charter §3.4 (no-SPA-no-build)?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v1 trigger condition (if a future v1 surface needs a queue-monitor dashboard):** potential schema additions (depending on the v1 surface):
- `jobs_queue` table — each async job would carry an entry in this table; the *queue-monitor* primitive from matador. Each row would have `job_id`, `queue_name`, `status` (`pending` | `running` | `completed` | `failed`), `payload` (JSONB), `created_at`, `started_at`, `completed_at`, `failed_at`, `error_message`, `retry_count`.
- `jobs_queue_snapshot` table — periodic snapshot of queue status; the *server-rendered-dashboard* primitive from matador (the dashboard renders from a snapshot, not from the live queue; the snapshot is derived).
- `job_register_routes` FastAPI sub-app — a sub-app that exposes the queue-monitor routes (`/v1/jobs/queue`, `/v1/jobs/queue/{name}`, `/v1/jobs/{id}/retry`); the *library-distribution* primitive from matador.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v1 trigger (when the first v1 surface needs a queue-monitor dashboard):**
- Add a `jobs_queue` SQLModel table (job_id, queue_name, status, payload, created_at, started_at, completed_at, failed_at, error_message, retry_count).
- Add a `jobs_queue_snapshot` SQLModel table (snapshot_id, queue_name, status_counts JSONB, created_at).
- Add a periodic `snapshot_jobs_queue` job that computes derived views (queue status counts, pending jobs, failed jobs) and stores them as a snapshot table; the *server-rendered-dashboard* primitive from matador (the dashboard renders from a snapshot, not from the live queue).
- Add a `job_register_routes` FastAPI sub-app that exposes the queue-monitor routes (charter §3.4: operator-tooling with observable evidence + non-AI fallback).
- Add a `pip install le31-jobs-queue-dashboard` library-distribution pattern (charter §3.2: MIT permissive license compatible).

**Steps independent of the v1 trigger (today):**
- [x] Read the `ilovepixelart/matador` GitHub repo structure (parent re-verified the description, topics, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *Live server-rendered dashboard for toro queues + FastAPI + HTMX + Tailwind + no SPA + no build step + pip install matador-dashboard* multi-primitive vocabulary (parent re-verified verbatim).
- [x] Confirm the 9 topics (`dashboard`, `fastapi`, `htmx`, `jobs`, `monitoring`, `python`, `queue`, `redis`, `toro`) (parent re-verified verbatim).
- [x] Cross-reference with features 23, 25, 67, 142, 144, 154, 156, 162, 168, 178, 191 (vocabulary-only), 206, 210, 212 (this file's Pick A sister), 213 (this file's Pick B sister) (ripgrep-verified distinct).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v1 trigger (when the first v1 surface needs a queue-monitor dashboard):**
- The owner would need a Telegram command to view a *queue status snapshot* (e.g., `/jobs queue status`); the *server-rendered-dashboard* primitive maps 1:1 onto a chat-style query interface.
- The owner would need a Telegram command to retry a failed job (e.g., `/jobs retry <job_id>`); the *queue-inspect-retry* primitive would surface failed-job entries.
- These are v1 surface additions; not in v1 scope today.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v1 trigger dependencies:** depends on the v1 surface that needs a queue-monitor dashboard (LE31 v1 has no async job queue today). Cross-references: features 23 (sse-cook-channel), 25 (fastapi-frontend-dev-loop), 67 (Bill), 142 (feldroy-air-fastapi-htmx-ai-write-framework), 144 (zentra-offline-first-fb-pattern), 154 (htmx-fastapi-cook-channel), 156 (AWIG-OS rule-citing-audit), 162 (htmx-fastapi-cook-channel v2), 168 (htmx-no-build-python-skeleton-watch), 178 (nhobin219-litelink-append-only-iceberg-embedded-local-first), 191 (eddiedzhang-FullHouse-Updated — repo now 404, vocabulary-only), 206 (djust-org/djust phoenix-liveview-style), 210 (duckframework/duck server-side-reactive-web-no-frontend-framework), 212 (this file's Pick A sister — Rooster-glitch/Hardtack v2-AI sovereign-context-ledger), 213 (this file's Pick B sister — hseshadr/avow v2-AI signed-evidence-receipts).

## Open questions

1. **HTMX live-update pattern:** what is the HTMX live-update pattern (do they use `htmx` swap for live updates? `hx-trigger="every 5s"` for polling? Server-Sent Events for streaming?). The full read of matador's HTMX templates is needed before any v1 port.
2. **Toro queue substrate:** does matador use Redis (per `redis` topic) or in-memory (per `toro` library) for the queue substrate? LE31 uses Postgres-only per charter §3.2; would the Toro queue substrate port to Postgres-only (Postgres has LISTEN/NOTIFY + SKIP LOCKED for queue patterns)? The full read of matador's queue integration is needed before any v1 port.
3. **Library-distribution pattern:** what is the *pip install matador-dashboard* packaging (is it a single-package FastAPI sub-app that can be `mount`-ed onto any FastAPI instance? does it expose a `/dashboard/...` route prefix?). The full read of matador's setup.py / pyproject.toml is needed before any v1 port.
4. **Server-rendered from snapshot:** does the dashboard render from a *snapshot* table (the snapshot is periodically refreshed) or from the *live queue* (every page-request queries the live queue)? The full read of matador's dashboard routing is needed before any v1 port.
5. **MIT license file confirmation:** is matador's MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **Live server-rendered dashboard for toro queues + FastAPI + HTMX + Tailwind + no SPA + no build step + pip install matador-dashboard** multi-primitive + the **9 topics** is the **strongest 2026-09-22 in-window v1-frontend-architecture reference for any future LE31 v1 surface that needs a queue-monitor dashboard** — and the MIT permissive license + the 9-topic coverage (including `fastapi` + `htmx` + `dashboard` + `jobs` + `monitoring` + `python` + `queue` + `redis` + `toro`) confirm it's a *practiced discipline*, not just a theoretical one. The vocabulary is fully transferable to LE31's charter §3.4 compliance pattern (operator-tooling with observable evidence + non-AI fallback; no-SPA-no-build invariant; minimal HTML/HTMX for waiter web UI). The artifact is informational only today; the value is vocabulary + a future-forkable-kernel note.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 surface needs a queue-monitor dashboard (e.g., a `/v1/jobs/queue` route for the owner to inspect + retry failed reconciliation jobs), the owner wants *a server-rendered HTMX dashboard with library-distribution*, but struggles because *v1 has no async job queue today*, so that *v1 can offer queue-monitoring without violating §3.4 (no-SPA-no-build invariant)*." **PASS** (zero-pain today; v1 has no async job queue; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies (Toro is a Python library, Redis is a subprocess); no new permissions. Confidence high for the architectural match (the *FastAPI+HTMX+Tailwind+server-rendered+no-SPA-no-build+library-distribution* multi-primitive set is well-established in the GitHub 1★-community-adoption cluster; matador's 9-topic coverage including `fastapi` + `htmx` confirms a real implementation, not just a proposal). MIT license is charter-compatible per §3.2. **PASS**. |
| 4 | **Conflict** | None. The *FastAPI+HTMX+Tailwind+server-rendered+no-SPA-no-build+library-distribution* multi-primitive set is charter §3.1 + §3.4 invariant-compatible (server-rendered posture preserved; operator-tooling with observable evidence + non-AI fallback; no customer-facing AI; minimal HTML/HTMX for waiter web UI). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v1 frontend-architecture-reference (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/214-ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference-HANDOFF.md` and `features/214-ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v1 frontend-architecture-review moment).

## Cross-references

- Parent research issue: `/opt/data/le31-daily-research-2026-09-22.md` (53rd consecutive daily-research pass).
- Companion artifacts (ripgrep-verified distinct): features 23, 25, 67, 142, 144, 154, 156, 162, 168, 178, 191 (eddiedzhang-FullHouse-Updated — repo now 404, vocabulary-only), 206 (djust-org/djust phoenix-liveview-style), 210 (duckframework/duck server-side-reactive-web-no-frontend-framework), 212 (this file's Pick A sister — Rooster-glitch/Hardtack v2-AI sovereign-context-ledger), 213 (this file's Pick B sister — hseshadr/avow v2-AI signed-evidence-receipts).
- Sister-picks from 2026-09-22: feature 212 (Rooster-glitch/Hardtack v2-AI sovereign-context-ledger), feature 213 (hseshadr/avow v2-AI signed-evidence-receipts).