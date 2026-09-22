# 214 — ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 frontend-architecture surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/214-ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference.md` (defer artifact; **no code today**).

Bucket: **v1 frontend-architecture-reference (architecture-reference)**. Build verdict: **`defer`** (charter §3.1 + §3.4 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 surface needs a queue-monitor dashboard (e.g., a `/v1/jobs/queue` route for the owner to inspect + retry failed reconciliation jobs), the owner wants *a server-rendered HTMX dashboard with library-distribution*, but struggles because *v1 has no async job queue today*, so that *v1 can offer queue-monitoring without violating §3.4 (no-SPA-no-build invariant)*." **PASS** (zero-pain today; v1 has no async job queue; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies (Toro is a Python library, Redis is a subprocess); no new permissions. Confidence high for the architectural match (the *FastAPI+HTMX+Tailwind+server-rendered+no-SPA-no-build+library-distribution* multi-primitive set is well-established in the GitHub 1★-community-adoption cluster; matador's 9-topic coverage including `fastapi` + `htmx` + `dashboard` confirms a real implementation, not just a proposal). MIT license is charter-compatible per §3.2. **PASS**. |
| 4 | **Conflict** | None. The *FastAPI+HTMX+Tailwind+server-rendered+no-SPA-no-build+library-distribution* multi-primitive set is charter §3.1 + §3.4 invariant-compatible (server-rendered posture preserved; operator-tooling with observable evidence + non-AI fallback; no customer-facing AI; minimal HTML/HTMX for waiter web UI). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v1 frontend-architecture-reference (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/214-ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference-HANDOFF.md` and `features/214-ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v1 frontend-architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 surface that needs a queue-monitor dashboard):

- `app/models/jobs_queue.py` — possibly add a `jobs_queue` SQLModel table (job_id, queue_name, status, payload, created_at, started_at, completed_at, failed_at, error_message, retry_count).
- `app/models/jobs_queue_snapshot.py` — possibly add a `jobs_queue_snapshot` SQLModel table (snapshot_id, queue_name, status_counts JSONB, created_at).
- `app/sub_apps/job_register_routes.py` — possibly add a `job_register_routes` FastAPI sub-app that exposes the queue-monitor routes (`/v1/jobs/queue`, `/v1/jobs/queue/{name}`, `/v1/jobs/{id}/retry`); the *library-distribution* primitive from matador.
- `app/jobs/snapshot_jobs_queue.py` — possibly add a periodic `snapshot_jobs_queue` job that computes derived views (queue status counts, pending jobs, failed jobs) and stores them as a snapshot table; the *server-rendered-dashboard* primitive from matador.
- `app/bot/jobs_queue_status.py` — possibly add a Telegram-bot command for the owner to view a *queue status snapshot* (e.g., `/jobs queue status`).
- `app/bot/jobs_retry.py` — possibly add a Telegram-bot command for the owner to retry a failed job (e.g., `/jobs retry <job_id>`).
- `setup.py` or `pyproject.toml` — possibly add `pip install le31-jobs-queue-dashboard` library-distribution pattern (charter §3.2: MIT permissive license compatible).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [x] `features/214-ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference.md` exists and is read back by the parent.
- [x] `specs/214-ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference-HANDOFF.md` (this file) exists and is read back by the parent.
- [x] The GitHub repo description is quoted verbatim: *"Live server-rendered dashboard for toro queues: watch queues, inspect and retry jobs. FastAPI + HTMX + Tailwind, no SPA, no build step. pip install matador-dashboard"*
- [x] The 9 topics are documented: `dashboard`, `fastapi`, `htmx`, `jobs`, `monitoring`, `python`, `queue`, `redis`, `toro`.
- [x] The MIT permissive license is documented.
- [x] The *FastAPI+HTMX+Tailwind+server-rendered+no-SPA-no-build+library-distribution* multi-primitive set is documented.
- [x] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/` + INDEX.md row + parent research report file.

**Future v1 trigger (when the first v1 surface needs a queue-monitor dashboard):**
- [ ] The PR is read back by the parent.
- [ ] The *FastAPI+HTMX+Tailwind+server-rendered+no-SPA-no-build+library-distribution* multi-primitive set is evaluated against the PR's changes: does the change preserve *server-rendered posture*? Does the change add *queue-inspect-retry*? Does the change add *no-SPA-no-build*? Does the change add *library-distribution*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `jobs_queue` table; remove the new `jobs_queue_snapshot` table; remove the new `job_register_routes` sub-app; restore the original schemas.
- Migration cost: depends on the v1 change; the *FastAPI+HTMX+Tailwind+server-rendered+no-SPA-no-build+library-distribution* multi-primitive set's design implies *additive schema* (the new `jobs_queue` + `jobs_queue_snapshot` tables are additive on top of the existing v1 schemas).
- Retained data: the new `jobs_queue` table retains all rows; the verification log is a *new* document, not a schema change.

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
| Feature ID | 214 |
| Slug | `ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference` |
| Bucket | v1 frontend-architecture-reference (architecture-reference, parking-lot defer) |
| Parent research issue | linear: blocked (workspace plan limit; see /opt/data/le31-daily-research-2026-09-22.linear-fallback.json); intended title `Research 2026-09-22 — daily` |
| Linear sub-issue | linear: blocked (workspace plan limit); intended title `Feature 214 — ilovepixelart-matador-mit-fastapi-htmx-tailwind-toro-queue-dashboard-no-spa-no-build-step-v1-frontend-architecture-reference` |
| Status today | defer (parking-lot) |
| No code today | yes |
| Verifiability today | feature file + HANDOFF file + INDEX.md row + parent research report file |
| Trigger condition (future v1) | first v1 surface that needs a queue-monitor dashboard |
| Disable path | delete `features/214-...md` + `specs/214-...-HANDOFF.md` |
| Migration cost | additive schema only (depends on v1 change) |
| Retained data | none |
| Parent research report | `/opt/data/le31-daily-research-2026-09-22.md` (53rd consecutive daily-research pass) |
| Raw fetches path | `/tmp/le31-daily-2026-09-22/` (54 files; anti-fabrication canary 0/53) |
| Linear fallback path | `/opt/data/le31-daily-research-2026-09-22.linear-fallback.json` |
| License | MIT ✓ (charter §3.2 compatible) |
| GitHub repo | `ilovepixelart/matador` (1star/0forks, Python, 1522 KB, pushed **2026-09-22T06:03:15Z = TODAY**) |
| Topics (verbatim) | `dashboard`, `fastapi`, `htmx`, `jobs`, `monitoring`, `python`, `queue`, `redis`, `toro` (9 topics) |
| Description (verbatim) | *"Live server-rendered dashboard for toro queues: watch queues, inspect and retry jobs. FastAPI + HTMX + Tailwind, no SPA, no build step. pip install matador-dashboard"* |
| LE31-shape-score | 7 (highest of any 2026-09-22 GitHub Search candidate; 9 topics hit 7 keywords: fastapi + htmx + dashboard + jobs + monitoring + python + queue) |
| Companion artifacts | features 23, 25, 67, 142, 144, 154, 156, 162, 168, 178, 191 (eddiedzhang-FullHouse-Updated — repo now 404, vocabulary-only), 206 (djust-org/djust phoenix-liveview-style), 210 (duckframework/duck server-side-reactive-web-no-frontend-framework), 212 (sister-pick A), 213 (sister-pick B) (ripgrep-verified distinct) |
| Sister-picks from 2026-09-22 | feature 212 (Rooster-glitch/Hardtack v2-AI sovereign-context-ledger), feature 213 (hseshadr/avow v2-AI signed-evidence-receipts) |

## 8. Verification log

*(Empty — to be populated by the parent if/when the future v1 trigger condition fires.)*

---

**OPERATOR NOTE (2026-09-22):** Today's Linear MCP write endpoint returned a workspace plan-limit error (`You've exceeded the free issue limit for this workspace` — carry-over from 2026-09-19); per `le31-daily-research/SKILL.md` hard rule, the parent research issue + the 3 Linear sub-issues were NOT created today. The fallback JSON at `/opt/data/le31-daily-research-2026-09-22.linear-fallback.json` documents the intended issues for resync after the workspace quota resets. The feature files + HANDOFFs were written to the repo regardless, per spec hard rule *"treat the report file as the source of truth; the Linear issue is the index"*.