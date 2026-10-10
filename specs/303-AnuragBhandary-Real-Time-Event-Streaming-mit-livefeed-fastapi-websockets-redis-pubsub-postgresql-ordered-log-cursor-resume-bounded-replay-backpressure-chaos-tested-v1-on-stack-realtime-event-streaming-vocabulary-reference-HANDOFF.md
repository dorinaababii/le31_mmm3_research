# HANDOFF — Feature 303: `AnuragBhandary-Real-Time-Event-Streaming-...-v1-on-stack-realtime-event-streaming-vocabulary-reference`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/303-AnuragBhandary-Real-Time-Event-Streaming-mit-livefeed-fastapi-websockets-redis-pubsub-postgresql-ordered-log-cursor-resume-bounded-replay-backpressure-chaos-tested-v1-on-stack-realtime-event-streaming-vocabulary-reference.md` — defer/parking-lot (Pick B of Daily Brainstorm 2026-10-10).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes a *real-time-event-streaming + exactly-once-delivery + chaos-tested-resilience + ordered-events-in-PostgreSQL + cursor-resume + bounded-replay + backpressure primitive*, the owner wants *evidence that this on-stack real-time-event-streaming-vocabulary exists in 2026 with the same stack as LE31*, but struggles because *LE31 has no documented v1 on-stack real-time-event-streaming-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage) without specialist help. The 0★ with single-maintainer cadence (10-day-old repo, first in-window push) makes code adoption not viable, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: **8/8 LE31 backend stack primitives matched** (FastAPI + Postgres + asyncio + Python + websockets + redis + postgresql + distributed-systems = the strongest 100%-LE31-stack-vocabulary-match of the 73-pass brainstorm series). Required data + permissions + infrastructure: Python 3.12 + asyncio + FastAPI + WebSockets + PostgreSQL (ordered-log) + Redis pub/sub + Docker + GitHub Actions CI + nginx. No AI capability required (the real-time-event-streaming primitive is deterministic). Rabbit hole: the *React 19 + TypeScript + Vite + Tailwind CSS + TanStack Query + React Router + Vitest + Testing Library + Playwright* frontend is off-LE31-frontend-stack (LE31 v1 uses minimal-HTML/HTMX, not React 19 + TypeScript + Vite + Tailwind CSS). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage* primitives are §3.1 + §3.3-aligned (operator-can-keep-working-during-network-outage + no-lost-events + no-duplicate-events). The *ordered-events-in-PostgreSQL* posture IS the §3.1 *append-only-ledger-as-audit-trail* invariant. No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (real-time-event-streaming surface for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry`) already implement the *append-only + idempotent* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + 10-day-old repo + React 19 + TypeScript frontend off-LE31-frontend-stack + no v1 real-time-event-streaming surface in v1 charter).

## Bucket

**v1** (on-stack real-time-event-streaming-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + README name the 15-tuple-primitive set (FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + Docker + GitHub Actions CI + nginx + 93% coverage + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom) + the tech-stack (Python 3.12 + asyncio + FastAPI + WebSockets + Redis pub/sub + PostgreSQL + Docker + GitHub Actions CI + nginx).

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds a real-time-event-streaming surface for the LE31 single-restaurant Swiss kitchen):

1. `backend/app/events/models.py` — add new `RealtimeEventStream` SQLModel table with columns: `id` (UUID), `stream_name` (str), `description` (str), `created_at`, `updated_at`.
2. `backend/app/events/models.py` — add new `RealtimeEvent` SQLModel table with columns: `id` (UUID), `stream_id` (UUID FK), `event_type` (str), `event_payload` (JSON), `occurred_at` (timezone-aware datetime), `sequence_number` (int), `created_at`. The `sequence_number` is monotonic per stream.
3. `backend/app/events/models.py` — add new `RealtimeEventSubscription` SQLModel table with columns: `id` (UUID), `stream_id` (UUID FK), `subscriber_id` (str), `cursor_sequence_number` (int, default=0), `last_event_at` (timezone-aware datetime), `is_active` (bool, default=true), `created_at`, `updated_at`.
4. `backend/app/events/models.py` — add new `RealtimeEventSubscriptionCheckpoint` SQLModel table with columns: `id` (UUID), `subscription_id` (UUID FK), `last_acked_sequence_number` (int), `acked_at` (timezone-aware datetime), `created_at`.
5. `backend/alembic/versions/` — add Alembic migration for the new tables.
6. `backend/app/events/broadcaster.py` — NEW: `RealtimeEventBroadcaster` asyncio coroutine that publishes events to Redis pub/sub.
7. `backend/app/events/subscriber.py` — NEW: `RealtimeEventSubscriber` asyncio coroutine that consumes events from Redis pub/sub.
8. `backend/app/events/storage.py` — NEW: `RealtimeEventStorage` SQLModel repository that writes ordered events to PostgreSQL.
9. `backend/app/events/cursor.py` — NEW: `RealtimeEventCursor` SQLModel repository that tracks per-subscription cursor position.
10. `backend/app/events/replay.py` — NEW: `RealtimeEventReplay` SQLModel repository that supports bounded replay from a cursor.
11. `backend/app/events/backpressure.py` — NEW: `RealtimeEventBackpressure` asyncio semaphore that drops slow clients gracefully.
12. `backend/app/api/v1/events/stream.py` — NEW: `WebSocket /ws/v1/events/stream` FastAPI endpoint that streams events to WebSocket clients.
13. `backend/app/api/v1/events/publish.py` — NEW: `POST /api/v1/events/publish` FastAPI endpoint that publishes events to a stream.
14. `backend/app/api/v1/events/replay.py` — NEW: `GET /api/v1/events/replay?stream_id=<>&from_sequence_number=<>&to_sequence_number=<>` FastAPI endpoint that supports bounded replay.
15. `backend/tests/events/test_chaos.py` — NEW: chaos-test suite that simulates 5 instance SIGKILLs + 8 Redis pub/sub kills + 14,069 reconnects + 0 duplicate or out-of-order events + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom at p95 71 ms + 93% coverage.
16. `.github/workflows/events-chaos.yml` — NEW: CI workflow (GitHub Actions) that runs the chaos-test suite on every PR.

## Verification protocol

1. `git clone https://github.com/AnuragBhandary/Real-Time-Event-Streaming` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/AnuragBhandary/Real-Time-Event-Streaming/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set + 15-tuple-primitive set + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage posture).
3. `curl -sS -H "Authorization: Bearer ***" "https://api.github.com/repos/AnuragBhandary/Real-Time-Event-Streaming"` for star count, fork count, license, language, pushed_at, created_at, topics, description, default_branch, archived (parent-verified 2026-10-10).
4. `curl -sS -H "Authorization: Bearer ***" -H "Accept: application/vnd.github.raw" "https://api.github.com/repos/AnuragBhandary/Real-Time-Event-Streaming/readme"` for the README body (parent-verified 2026-10-10).
5. `grep -cF 'LE31' /tmp/le31-brainstorm-2026-10-10/verify/AnuragBhandary_Real-Time-Event-Streaming.json` (parent-verified 2026-10-10: 0 matches — PASS).
6. `grep -cF 'LE31' /tmp/le31-brainstorm-2026-10-10/verify/mhmd2042_cafe-pos.json /tmp/le31-brainstorm-2026-10-10/verify/AnuragBhandary_Real-Time-Event-Streaming.json /tmp/le31-brainstorm-2026-10-10/verify/drwjkirkpatrick-web_the-pass.json` (parent-verified 2026-10-10: 0 matches — PASS).
7. `grep -lE 'github.com/AnuragBhandary/Real-Time-Event-Streaming|AnuragBhandary/Real-Time-Event-Streaming' features/*.md` (parent-verified 2026-10-10: 0 matches — feature 303 is the only reference; the new feature file itself matches but the contract says it is the first).
8. If the future v1 trigger fires, run the v1 real-time-event-streaming surface (FUTURE): `pytest backend/tests/events/test_chaos.py -v` for chaos tests; `pytest backend/tests/events/test_chaos.py --cov=backend.app.events --cov-report=term-missing` for coverage; `pytest backend/tests/events/test_chaos.py -k "test_5_instance_sigkills_survived" -v` for the 5 instance SIGKILLs chaos test; `pytest backend/tests/events/test_chaos.py -k "test_8_redis_pubsub_kills_survived" -v` for the 8 Redis pub/sub kills chaos test; `pytest backend/tests/events/test_chaos.py -k "test_14069_reconnects_survived" -v` for the 14,069 reconnects chaos test; `pytest backend/tests/events/test_chaos.py -k "test_0_duplicate_or_out_of_order_events" -v` for the 0 duplicate or out-of-order events chaos test; `pytest backend/tests/events/test_chaos.py -k "test_p95_5ms_live_delivery_latency" -v` for the p95 5 ms live-delivery-latency chaos test; `pytest backend/tests/events/test_chaos.py -k "test_50000_deliveries_per_second_headroom" -v` for the ≈ 50,000 deliveries/s headroom chaos test.

## Rollback path

No code today. The handbook + HANDOFF can be reverted by `git rm features/303-AnuragBhandary-Real-Time-Event-Streaming-...md specs/303-AnuragBhandary-Real-Time-Event-Streaming-...-HANDOFF.md`.

If the future v1 trigger fires and the implementation is later rejected: `alembic downgrade -1` to drop the new tables; `git rm backend/app/events/models.py backend/app/events/broadcaster.py backend/app/events/subscriber.py backend/app/events/storage.py backend/app/events/cursor.py backend/app/events/replay.py backend/app/events/backpressure.py backend/app/api/v1/events/stream.py backend/app/api/v1/events/publish.py backend/app/api/v1/events/replay.py backend/tests/events/test_chaos.py .github/workflows/events-chaos.yml backend/alembic/versions/<new_migration>.py`.

## Mandatory LE31 skill list

The coding agent must load the following skills before starting any future implementation of feature 303:

- `le31-conventions` — for the seven-check feature gate and the charter §3.1 + §3.2 + §3.3 invariants
- `le31-backend` — for the FastAPI + SQLModel + Postgres + Alembic stack patterns
- `le31-frontend` — for the minimal-HTML/HTMX waiter-UI patterns
- `le31-data` — for the `StockEntry` + `audit_logs` SQLModel table patterns
- `le31-v1-feature-pattern` — for the v1 feature contract template + bucket + cross-section references
- `le31-handoff-spec` — for the slice contract structure (active feature path + seven-check gate verdict + files to touch + verification protocol + rollback path)
- `le31-coding-agent-brief` — for the coding-agent-brief generation pattern (this HANDOFF IS the brief; the agent does not need to re-generate it)

## Why this matters

The **FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + Docker + GitHub Actions CI + nginx + 93% coverage + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom** 15-tuple-primitive is the **strongest direct LE31 v1 on-stack real-time-event-streaming-vocabulary reference of the 73-pass series** because it is the only in-window 2026-10 Python on-stack real-time-event-streaming-vocabulary candidate that combines all 15 sub-primitives (FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + Docker + GitHub Actions CI + nginx + 93% coverage + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom) in a single 10-day-old repo with first in-window push + **8/8 LE31 backend stack primitives matched = the strongest 100%-LE31-stack-vocabulary-match of the 73-pass brainstorm series**.

Sister-shape to features 22 (carry-over real-time-event-streaming reference) + 158 (ppfenning/coxswain-graphs — interactive-graph-explorer + FastAPI + HTMX + WebSocket + pydantic + Plotly) + 240 (fredhead88/do-it-v2 — personal-productivity + Telegram + Todoist + CalDAV + FastAPI + SQLite) + 247 (carry-over reference) + 297 (jonalemndi2/ALdia — open-source-business-engine + AI-agents + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country). The livefeed pattern is the **strongest direct FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + exactly-once-delivery + chaos-tested-resilience primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that adds a real-time-event-streaming surface for the LE31 single-restaurant Swiss kitchen.

**Fully reversible** (vocabulary-only artifact). No code today.
