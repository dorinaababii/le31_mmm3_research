# Handoff — Feature 280 — v1 append-only-ops-dashboard-vocabulary (defer)

> **Pick:** `11pyo/ai-collab-dashboard` — v1 cross-section reference for **concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data + ops** primitive.
> **Status:** `defer (parking-lot, vocabulary reference)` — zero build time today; the artifact is vocabulary-only and persists as a future-cast reference for any future LE31 v1 surface that adopts the *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* primitives.
> **Source:** Daily Brainstorm 2026-10-05 (67th consecutive daily-brainstorm pass) → Pick C.
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/280-11pyo-ai-collab-dashboard-mit-concurrency-safe-ops-task-inquiry-dashboard-kanban-toyota-inspired-append-only-id-merge-log-no-backend-v1-append-only-ops-dashboard-vocabulary.md`
> **Raw fetches:** `/tmp/le31-brainstorm-2026-10-05/verify_alt_11pyo_ai-collab-dashboard.json` (parent-verified direct GitHub API GET, raw JSON, 6.0 KB)

---

## Seven-check gate verdict (LE31 charter §3.1 + §3.2 + §3.4)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✓ justified as a NEW pain | When the LE31 cook wants to see a kanban-board-of-prep-tasks with append-only-id-merge-log event-sourcing, the cook wants concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data, but struggles because the existing cook-Telegram-bot has no kanban-board + no append-only-id-merge-log + no ops-dashboard surface, so the v1 surface-extension needs a *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* discipline. **v1 expansion → NEW pain** |
| 2 | Viability | ✓ viable | Non-technical owner CAN understand (the *kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* primitive is operator-readable); CAN recover (the *append-only-id-merge-log + audit_logs* discipline is recoverable via Postgres backup); CAN maintain (the *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log* surface is documentation-only at v1; v1 surface would require FastAPI + SQLModel + Postgres + WebSocket expertise). **§3.1 owner-readable profile** |
| 3 | Strategic fit | ✓ aligned | Cross-section with feature 197 (rajo69/ledgerkb Apache-2.0 v2-owner-pains evidence-bearing-assertions-position-over-time-append-only-ledger-rag-knowledge-graph = *position-over-time + multiple-projections-from-one-ledger + evidence-bearing-assertion* triple-primitive) + 240 (huoyunpili/xiaomaipu Apache-2.0 v1 SMB-order-management-with-per-order-profit). The *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* posture IS the canonical **v1 append-only-ops-dashboard-vocabulary** |
| 4 | Charter conflict | ✓ none hard | §3.1 STRICTLY-COMPATIBLE (Python + minimal-HTML posture; the *concurrency-safe + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* posture IS the §3.1 *single-restaurant + single-owner + on-premise-deployment + safe-for-concurrent-cooks-and-waiters* invariant applied to the *ops-dashboard* dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive + 0★/0⑨ community traction start); §3.4 NOT TRIGGERED (the *ops-dashboard* surface is operator-tooling per charter §3.4 invariant; the *append-only-id-merge-log* posture IS the *operator-tooling + observable-evidence + non-AI-fallback* charter §3.4 invariant applied to the *ops-dashboard* dimension); §3.7 N/A (no privacy primitive change). **No hard conflict** |
| 5 | Outcome, appetite, scope | ✓ alignable | v1 outcome (append-only-ops-dashboard-vocabulary). Max time worth spending = 0 minutes today (defer artifact); future v1 PR = 1-2 weeks for design + 2-3 weeks for *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* surface + 1 week for verification = 1-2 months total |
| 6 | Cost to operational value | ✓ marginal | Pain frequency = low (LE31 v1 has no v1 ops-dashboard surface today; no operator has asked for v1 ops-dashboard); money vocabulary = minimal; implementation cost = 1-2 months v1 PR. **MARGINAL VALUE at v1** |
| 7 | Circuit breaker and reversibility | ✓ reversible | Stop evidence = explicit owner/charter rejection of *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* adoption; review point = first v1 PR that proposes *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* surface; migration/rollback = trivial (vocabulary-only artifact, zero code shipped); retained data = N/A |

**Final decision: `defer (parking-lot, vocabulary reference)`.**

## Files to touch (future v1 PR trigger)

If a future v1 PR is triggered by the trigger condition below, the implementation would touch:

| File | Purpose | Notes |
|---|---|---|
| `app/models/ops_task.py` (NEW) | `OpsTask` SQLModel table | `task_id, task_name, task_markdown, task_owner_id, task_status, task_kanban_position, task_updated_at` |
| `app/models/ops_kanban_column.py` (NEW) | `OpsKanbanColumn` SQLModel table | `column_id, column_name, column_order, column_protocol_id` for *kanban-Toyota-inspired* discipline |
| `app/models/ops_id_merge_log.py` (NEW) | `OpsIdMergeLog` SQLModel table | `merge_id, merge_event_id, merge_event_kind, merge_event_payload_json, merge_event_at, merge_event_parent_id` for *append-only-id-merge-log* discipline |
| `app/models/ops_inquiry.py` (NEW) | `OpsInquiry` SQLModel table | `inquiry_id, inquiry_markdown, inquiry_owner_id, inquiry_status, inquiry_kanban_position` for *inquiry-dashboard* discipline |
| `app/api/ops_dashboard.py` (NEW) | FastAPI route + endpoint | `/api/ops-dashboard` (POST create task, GET list, GET show, POST move-task, GET append-only-id-merge-log) |
| `app/templates/ops_dashboard.html` (NEW) | minimal-HTML/HTMX template | cook-facing surface for ops-dashboard with kanban-board-of-prep-tasks |
| `app/static/js/ops-dashboard-kanban.js` (NEW) | minimal vanilla JS for HTMX kanban | Optional: only if HTMX drag-drop proves insufficient |
| `migrations/versions/<hash>_add_ops_dashboard_tables.py` (NEW) | alembic migration | creates `ops_task + ops_kanban_column + ops_id_merge_log + ops_inquiry` tables |
| `tests/test_ops_dashboard_api.py` (NEW) | pytest coverage | covers OpsTask CRUD + kanban-move + append-only-id-merge-log + concurrency-safe |
| `tests/test_ops_dashboard_concurrency.py` (NEW) | pytest coverage | covers concurrency-safe (multiple-cooks-and-waiters safe) |

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md` + `development` skill, the future v1 PR would:
1. Run `pytest tests/test_ops_dashboard_api.py tests/test_ops_dashboard_concurrency.py -v` to confirm all tests pass.
2. Run `alembic upgrade head` to confirm migrations apply cleanly.
3. Run `python -c "from app.models.ops_task import OpsTask; print(OpsTask.__tablename__)"` to confirm SQLModel loads.
4. Manually verify via `curl http://localhost:8000/api/ops-dashboard/status` that the FastAPI endpoint returns 200 with the expected schema.
5. Manually verify via the cook-ops-dashboard that the *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* discipline works end-to-end (create task → move-task on kanban → verify append-only-id-merge-log → verify concurrency-safe).
6. Run `mypy app/` + `ruff check app/` to confirm static analysis passes.
7. Confirm feature is in `Backlog` status + parent (this brainstorm parent) is in `Done` status in Linear.

## Rollback path

The defer artifact is vocabulary-only, zero code shipped, so no rollback is needed today. If a future v1 PR ships and the *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* discipline is rejected by the owner/charter:
1. Run `alembic downgrade -1` to drop the `ops_task + ops_kanban_column + ops_id_merge_log + ops_inquiry` tables.
2. Delete `app/models/ops_task.py` + `app/models/ops_kanban_column.py` + `app/models/ops_id_merge_log.py` + `app/models/ops_inquiry.py` + `app/api/ops_dashboard.py` + `app/templates/ops_dashboard.html` + `app/static/js/ops-dashboard-kanban.js` + the alembic migration + the pytest files.
3. Re-run `alembic upgrade head` to confirm clean state.
4. Re-run `pytest -v` to confirm no regressions.

## Mandatory LE31 skill list

The future v1 PR author MUST load + apply these skills before any code is written:

| Skill | Why |
|---|---|
| `le31-conventions` | Repository-wide Python + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX conventions |
| `le31-v1-feature-pattern` | Existing v1 feature pattern (table management, cook-channel, stock-ledger) |
| `le31-handoff-spec` | Slice handoff format |
| `le31-coding-agent-brief` | Paste-in prompt generation from this slice contract |
| `systematic-debugging` | 4-phase root cause debugging if any test fails |
| `verify-before-fixing` | Verify diagnostic / CI / delegated subagent before fixing |
| `pre-merge-review` | Independent non-author review before merging |

## Bucket

**v1** (attached to `le31 v1 — Core MVP` P-HMM-3 per the verified workspace project list of 2026-10-05; the `le31 v2 owner-pains` and `le31 v2-AI` projects do NOT exist per `le31-feature-pipeline/SKILL.md` line 33).

## Trigger condition

First v1 PR that adds an `ops_dashboard` SQLModel table + a `/api/ops-dashboard` FastAPI endpoint + a `ops-dashboard.html` minimal-HTML/HTMX template with kanban-Toyota-inspired + append-only-id-merge-log; OR first v1 PR that adopts the *concurrency-safe-ops-task-and-inquiry-dashboard + kanban-Toyota-inspired + append-only-id-merge-log + no-backend + fictional-sample-data* discipline on the existing cook-Telegram-bot.

## Charter compatibility

§3.1 + §3.2 STRICTLY-COMPATIBLE; §3.4 NOT TRIGGERED (the *ops-dashboard* surface is operator-tooling per charter §3.4 invariant).

## Companion artifacts

- Feature file: `/opt/data/le31_mmm3_research_work/features/280-11pyo-ai-collab-dashboard-mit-concurrency-safe-ops-task-inquiry-dashboard-kanban-toyota-inspired-append-only-id-merge-log-no-backend-v1-append-only-ops-dashboard-vocabulary.md`
- Spec file: `/opt/data/le31_mmm3_research_work/specs/280-11pyo-ai-collab-dashboard-mit-concurrency-safe-ops-task-inquiry-dashboard-kanban-toyota-inspired-append-only-id-merge-log-no-backend-v1-append-only-ops-dashboard-vocabulary-HANDOFF.md`
- Linear sub-issue: BLOCKED (workspace plan-limit error: *\"You've exceeded the free issue limit for this workspace\"* — **16th consecutive day**; verified today via 2 write-probes with requestId `a45aac5e0a9ad368`; parent fallback at `/opt/data/le31-brainstorm-2026-10-05.linear-fallback.json`)
- Report: `/opt/data/le31-brainstorm-2026-10-05.md`
- Raw fetches: `/tmp/le31-brainstorm-2026-10-05/verify_alt_11pyo_ai-collab-dashboard.json` (parent-verified direct GitHub API GET, raw JSON, 6.0 KB)