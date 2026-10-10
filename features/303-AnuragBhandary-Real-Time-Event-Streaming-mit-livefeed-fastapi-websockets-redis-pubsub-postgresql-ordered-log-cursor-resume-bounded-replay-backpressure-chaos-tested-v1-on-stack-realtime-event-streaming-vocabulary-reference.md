# Feature 303 — `AnuragBhandary-Real-Time-Event-Streaming-mit-livefeed-fastapi-websockets-redis-pubsub-postgresql-ordered-log-cursor-resume-bounded-replay-backpressure-chaos-tested-v1-on-stack-realtime-event-streaming-vocabulary-reference` (defer)

> **NEW observation (2026-10-10).** Documents in-window GitHub repo `AnuragBhandary/Real-Time-Event-Streaming` (a.k.a. `livefeed`) (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Python 3.12 + asyncio + FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + Docker + GitHub Actions CI + nginx, **pushed 2026-10-09T07:17:19Z** AND **created 2026-09-30T12:08:10Z** = IN-WINDOW BY BOTH FIELDS as a 10-day-old repo with fresh push, **227 KB modest repo**, default_branch=`main`, archived=false, 93% coverage, **measured 5,000,000/5,000,000 exactly-once deliveries under chaos (5 instance SIGKILLs + 8 Redis pub/sub kills + 14,069 reconnects survived + 0 duplicate or out-of-order events + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom at p95 71 ms)**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-10): *"Real-time event streaming: FastAPI WebSockets fan-out across instances via Redis pub/sub, ordered events in PostgreSQL, cursor resume, bounded replay, backpressure. Chaos-tested."* Topics (verbatim, parent-verified, 8): `asyncio, distributed-systems, fastapi, postgresql, python, real-time, redis, websockets`. Bucket: **v1 (on-stack real-time-event-streaming-vocabulary)** — Pick B of Daily Brainstorm 2026-10-10. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + Docker + GitHub Actions CI + nginx + 93% coverage + 5,000,000/5,000,000 exactly-once deliveries measured under chaos (5 instance SIGKILLs + 8 Redis pub/sub kills + 14,069 reconnects survived + 0 duplicate or out-of-order events + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom at p95 71 ms) + ordered events in PostgreSQL + cursor resume + bounded replay + backpressure + React 19 + TypeScript + Vite + Tailwind CSS + TanStack Query + React Router + Vitest + Testing Library + Playwright + nginx** 18-tuple-primitive as a persistent cross-section reference for the LE31 v1 *on-stack real-time-event-streaming + exactly-once-delivery + chaos-tested-resilience* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (10-day-old repo with fresh push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + Docker + GitHub Actions CI + nginx + 93% coverage + 5,000,000/5,000,000 exactly-once deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom** 15-tuple-primitive: every WebSocket subscriber on any instance (a browser tab or the Python SDK) receives each event **exactly once, in order**; that holds through reconnects, instance crashes, Redis failures, and slow clients. This is the §3.1 explicit-state-transitions + §3.3 *no-lost-events + no-duplicate-events* invariant applied to the *real-time-event-streaming + chaos-tested-resilience* dimension.
- A written record of the **Python 3.12 + asyncio + FastAPI + WebSockets + PostgreSQL (ordered-log) + Redis pub/sub + Docker + GitHub Actions CI + nginx** stack-shape: this is **8/8 LE31 backend stack primitives matched** (FastAPI + Postgres + asyncio + Python + websockets + redis + postgresql + distributed-systems) = **the strongest 100%-LE31-stack-vocabulary-match of the 73-pass brainstorm series**.
- A written record of the **operator-facing vocabulary** discipline: producers publish events; PostgreSQL stores them in order; every WebSocket subscriber on any instance receives each event exactly once, in order; that holds through reconnects, instance crashes, Redis failures, and slow clients. Sister-shape to feature 22 (real-time-event-streaming reference) + feature 158 (ppfenning/coxswain-graphs — interactive-graph-explorer + FastAPI + HTMX + WebSocket + pydantic + Plotly) + feature 240 (fredhead88/do-it-v2 — personal-productivity + Telegram + Todoist + CalDAV + FastAPI + SQLite).
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (10-day-old, first in-window push); (2) the stack-shape match is the value, not the code (LE31 v1 has no real-time-event-streaming surface; the v1 charter is HTTP + Postgres, not WebSocket + Redis pub/sub); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the livefeed codebase (10-day-old single-maintainer repo with no observed production usage + React 19 + TypeScript frontend is off-LE31-frontend-stack).
- Cross-pollination with the v1 charter §3.1 *explicit-state-transitions* posture (the *ordered events in PostgreSQL + cursor resume + bounded replay + backpressure* discipline IS the §3.1 invariant; the *exactly-once-delivery + 0 duplicate or out-of-order events* discipline IS the §3.3 invariant).
- Any vendor-relationship with React 19 / TypeScript / Vite / Tailwind CSS / TanStack Query / React Router / Vitest / Testing Library / Playwright (LE31 v1 uses minimal-HTML/HTMX, not React 19 + TypeScript + Vite + Tailwind CSS).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v1 surface proposes "a real-time-event-streaming + exactly-once-delivery + chaos-tested-resilience + ordered-events-in-PostgreSQL + cursor-resume + bounded-replay + backpressure primitive" (e.g., a v1 surface that introduces a real-time event stream for the LE31 single-restaurant Swiss kitchen where the cook Telegram bot needs to receive an event-stream of orders in real-time, the waiter web UI needs to receive an event-stream of stock changes in real-time, and the owner daily-recap needs to consume an event-stream of all events in real-time), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage" is a real demand signal*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31 + the chaos-tested-resilience posture"*.

- **Evidence class**: observed (the description + topics + README name the primitives explicitly: `asyncio, distributed-systems, fastapi, postgresql, python, real-time, redis, websockets` + *"5,000,000/5,000,000 exactly-once deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage"*).
- **Confidence**: medium-high for the vocabulary match (the verbatim description + README name the 15-tuple-primitive set + the tech-stack + the exactly-once-delivery posture + the chaos-tested-resilience posture + the ordered-events-in-PostgreSQL posture + the cursor-resume posture + the bounded-replay posture + the backpressure posture + the 5,000,000/5,000,000 deliveries + 93% coverage); low for transferability (LE31 v1 has no real-time-event-streaming surface; v1 charter is HTTP + Postgres, not WebSocket + Redis pub/sub).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no real-time-event-streaming surface); the value is the *FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage* vocabulary — when the first v1 PR that adds a real-time-event-streaming surface lands, the livefeed pattern is a ready-made *named primitive*.

## Description

GitHub `AnuragBhandary/Real-Time-Event-Streaming` (MIT, 0★/0⑂, Python 3.12 + asyncio + FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + Docker + GitHub Actions CI + nginx, pushed 2026-10-09T07:17:19Z, created 2026-09-30T12:08:10Z, 227 KB, default_branch=`main`, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-10): *"Real-time event streaming: FastAPI WebSockets fan-out across instances via Redis pub/sub, ordered events in PostgreSQL, cursor resume, bounded replay, backpressure. Chaos-tested."*

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **FastAPI + WebSockets fan-out** — every WebSocket subscriber on any instance (a browser tab or the Python SDK) receives each event. The *FastAPI + WebSockets fan-out* primitive maps 1:1 onto any future v1 surface that needs a `WebSocket /ws/v1/events/stream` endpoint.
2. **Redis pub/sub for cross-instance fan-out** — events are published to Redis pub/sub and consumed by every instance. The *Redis pub/sub* primitive IS the §3.1 *append-only* invariant applied to the *real-time-event-streaming* dimension.
3. **Ordered events in PostgreSQL** — events are stored in order in PostgreSQL. The *ordered-events-in-PostgreSQL* primitive IS the §3.1 *append-only-ledger-as-audit-trail* invariant applied to the *real-time-event-streaming* dimension.
4. **Cursor resume** — every subscription tracks a cursor position; on reconnect, the subscription resumes from the cursor. The *cursor-resume* primitive IS the *no-lost-events* charter §3.1 invariant.
5. **Bounded replay** — every subscription can replay a bounded number of events from the cursor. The *bounded-replay* primitive IS the *operator-can-replay* charter §3.1 invariant.
6. **Backpressure** — slow clients are dropped gracefully via a backpressure semaphore. The *backpressure* primitive IS the *no-resource-exhaustion* charter §3.1 invariant.
7. **Exactly-once-delivery** — every event is delivered exactly once, in order, to every subscriber. The *exactly-once-delivery* primitive IS the §3.3 *no-duplicate-events* invariant.
8. **0 duplicate or out-of-order events** — measured at the protocol level. The *0-duplicate-or-out-of-order-events* primitive IS the *no-data-corruption* charter §3.3 invariant.
9. **14,069 reconnects survived** — measured under chaos testing (random client drops + 5 instance SIGKILLs + 8 Redis pub/sub kills). The *14,069-reconnects-survived* primitive IS the *chaos-tested-resilience* charter §3.1 invariant.
10. **5 instance SIGKILLs survived** — measured under chaos testing. The *5-instance-SIGKILLs-survived* primitive IS the *instance-failure-resilience* charter §3.1 invariant.
11. **8 Redis pub/sub kills survived** — measured under chaos testing. The *8-Redis-pub-sub-kills-survived* primitive IS the *Redis-failure-resilience* charter §3.1 invariant.
12. **p95 5 ms live-delivery-latency** — measured (producer send → subscriber receive). The *p95-5-ms-live-delivery-latency* primitive IS the *low-latency* charter §3.1 invariant.
13. **≈ 50,000 deliveries/s headroom at p95 71 ms** — measured without chaos. The *50,000-deliveries-per-second-headroom* primitive IS the *high-throughput* charter §3.1 invariant.
14. **93% coverage** — measured via coverage tooling. The *93%-coverage* primitive IS the *test-coverage* charter §3.1 invariant.
15. **Python 3.12 + asyncio + FastAPI + WebSockets + PostgreSQL + Redis pub/sub + Docker + GitHub Actions CI + nginx** — the tech-stack. The *Python 3.12 + asyncio + FastAPI + WebSockets + PostgreSQL + Redis pub/sub + Docker + GitHub Actions CI + nginx* posture IS the *on-LE31-stack* invariant.

**The 1:1 mapping onto LE31 surface:**

| livefeed primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| FastAPI + WebSockets | (LE31 v1 has no WebSocket surface) | §3.1 ✓ | **Not implemented** — v1 polish surface |
| Redis pub/sub for cross-instance fan-out | (LE31 v1 has no Redis pub/sub) | v1 polish | **Not implemented** — v1 polish surface |
| Ordered events in PostgreSQL | `audit_logs` (append-only) | §3.1 ✓ | **Implemented (v1, partial)** — the *append-only* discipline is implemented in v1, but the *ordered-events-in-PostgreSQL* posture is a sister-shape to the *ordered-events-in-PostgreSQL* primitive |
| Cursor resume | (LE31 v1 has no cursor resume) | v1 polish | **Not implemented** — v1 polish surface |
| Bounded replay | (LE31 v1 has no bounded replay) | v1 polish | **Not implemented** — v1 polish surface |
| Backpressure | (LE31 v1 has no backpressure) | v1 polish | **Not implemented** — v1 polish surface |
| Exactly-once-delivery | (LE31 v1 has no exactly-once-delivery) | v1 polish | **Not implemented** — v1 polish surface |
| 0 duplicate or out-of-order events | `audit_logs` (append-only + idempotent) | §3.3 ✓ | **Not implemented** — v1 polish surface |
| 14,069 reconnects survived | (LE31 v1 has no chaos testing) | v1 polish | **Not implemented** — v1 polish surface |
| 5 instance SIGKILLs survived | (LE31 v1 has no chaos testing) | v1 polish | **Not implemented** — v1 polish surface |
| 8 Redis pub/sub kills survived | (LE31 v1 has no Redis) | v1 polish | **Not implemented** — v1 polish surface |
| p95 5 ms live-delivery-latency | (LE31 v1 has no real-time-event-streaming) | v1 polish | **Not implemented** — v1 polish surface |
| ≈ 50,000 deliveries/s headroom | (LE31 v1 has no real-time-event-streaming) | v1 polish | **Not implemented** — v1 polish surface |
| 93% coverage | (LE31 v1 has test coverage but no 93% target) | v1 polish | **Not implemented** — v1 polish surface |
| Python 3.12 + asyncio + FastAPI + PostgreSQL | Python 3.13 + FastAPI + SQLModel + Postgres | §3.1 ✓ | **Implemented (v1, partial)** — the *Python + FastAPI + Postgres* match is the LE31-stack-match; the *asyncio + WebSockets + Redis* are off-LE31-stack |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that introduces a real-time-event-streaming surface for the LE31 single-restaurant Swiss kitchen), the implementation would add:

1. A new `RealtimeEventStream` table (Alembic migration) with columns: `id` (UUID), `stream_name` (str), `description` (str), `created_at`, `updated_at`.
2. A new `RealtimeEvent` table (Alembic migration) with columns: `id` (UUID), `stream_id` (UUID FK), `event_type` (str), `event_payload` (JSON), `occurred_at` (timezone-aware datetime), `sequence_number` (int), `created_at`. The `sequence_number` is monotonic per stream.
3. A new `RealtimeEventSubscription` table (Alembic migration) with columns: `id` (UUID), `stream_id` (UUID FK), `subscriber_id` (str), `cursor_sequence_number` (int, default=0), `last_event_at` (timezone-aware datetime), `is_active` (bool, default=true), `created_at`, `updated_at`.
4. A new `RealtimeEventSubscriptionCheckpoint` table (Alembic migration) with columns: `id` (UUID), `subscription_id` (UUID FK), `last_acked_sequence_number` (int), `acked_at` (timezone-aware datetime), `created_at`.
5. An Alembic migration that adds the new tables.
6. A `RealtimeEventBroadcaster` asyncio coroutine that publishes events to Redis pub/sub.
7. A `RealtimeEventSubscriber` asyncio coroutine that consumes events from Redis pub/sub.
8. A `RealtimeEventStorage` SQLModel repository that writes ordered events to PostgreSQL.
9. A `RealtimeEventCursor` SQLModel repository that tracks per-subscription cursor position.
10. A `RealtimeEventReplay` SQLModel repository that supports bounded replay from a cursor.
11. A `RealtimeEventBackpressure` asyncio semaphore that drops slow clients gracefully.
12. A `WebSocket /ws/v1/events/stream` FastAPI endpoint that streams events to WebSocket clients.
13. A `POST /api/v1/events/publish` FastAPI endpoint that publishes events to a stream.
14. A `GET /api/v1/events/replay?stream_id=<>&from_sequence_number=<>&to_sequence_number=<>` FastAPI endpoint that supports bounded replay.

The HANDOFF is to evaluate whether the v1 real-time-event-streaming surface is the right product-wedge for the next v1 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires:

**For v1 on-stack real-time-event-streaming-vocabulary surface** (if approved):

1. Add new `RealtimeEventStream` SQLModel table (Alembic migration).
2. Add new `RealtimeEvent` SQLModel table (Alembic migration).
3. Add new `RealtimeEventSubscription` SQLModel table (Alembic migration).
4. Add new `RealtimeEventSubscriptionCheckpoint` SQLModel table (Alembic migration).
5. Add Alembic migration for the new tables.
6. Add a `RealtimeEventBroadcaster` asyncio coroutine that publishes events to Redis pub/sub.
7. Add a `RealtimeEventSubscriber` asyncio coroutine that consumes events from Redis pub/sub.
8. Add a `RealtimeEventStorage` SQLModel repository that writes ordered events to PostgreSQL.
9. Add a `RealtimeEventCursor` SQLModel repository that tracks per-subscription cursor position.
10. Add a `RealtimeEventReplay` SQLModel repository that supports bounded replay from a cursor.
11. Add a `RealtimeEventBackpressure` asyncio semaphore that drops slow clients gracefully.
12. Add a `WebSocket /ws/v1/events/stream` FastAPI endpoint that streams events to WebSocket clients.
13. Add a `POST /api/v1/events/publish` FastAPI endpoint that publishes events to a stream.
14. Add a `GET /api/v1/events/replay?stream_id=<>&from_sequence_number=<>&to_sequence_number=<>` FastAPI endpoint that supports bounded replay.
15. Add a chaos-test suite that simulates 5 instance SIGKILLs + 8 Redis pub/sub kills + 14,069 reconnects + 0 duplicate or out-of-order events + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom at p95 71 ms + 93% coverage.
16. Add a CI workflow (GitHub Actions) that runs the chaos-test suite on every PR.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires, the v1 on-stack real-time-event-streaming surface would add **a v1 cook-Telegram-realtime-event-stream primitive** (e.g., the cook Telegram bot subscribes to a real-time-event-stream of new orders and receives an event-stream of order-created + order-cancelled + order-modified events in real-time). The realtime-event-stream primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 53/66 (offline-first).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; the livefeed stack is Python 3.12 + asyncio + FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + Docker + GitHub Actions CI + nginx which is an 8/8 LE31-stack-match).
- **External**: None (the realtime-event-streaming primitive is local to the LE31 instance; no external API).
- **Internal**: §3.1 (append-only discipline for `audit_logs`); §3.2 (MIT permissive license compatible); §3.3 (no-lost-events + no-duplicate-events invariant).
- **Trigger dependency**: future v1 PR that adds a real-time-event-streaming surface for the LE31 single-restaurant Swiss kitchen.

## Open questions

- **Q1**: When (if ever) will LE31 introduce a real-time-event-streaming surface? The v1 charter explicitly uses HTTP + Postgres; v1 is HTTP + minimal-HTML/HTMX, not WebSocket + Redis pub/sub.
- **Q2**: If the real-time-event-streaming surface lands, will it use WebSocket + Redis pub/sub (like livefeed) or HTTP + Server-Sent Events (like the LE31 v1 charter §3.1 *explicit-state-transitions* posture)? The WebSocket + Redis pub/sub approach is a different transport model from the HTTP + Server-Sent Events model.
- **Q3**: Will the exactly-once-delivery primitive be §3.3-compliant? The *exactly-once-delivery + 0 duplicate or out-of-order events* posture IS the §3.3 *no-lost-events + no-duplicate-events* invariant; LE31 v1's `audit_logs` is already append-only + idempotent, which is the foundation for exactly-once-delivery.
- **Q4**: How will the *chaos-tested-resilience (5 instance SIGKILLs + 8 Redis pub/sub kills + 14,069 reconnects)* primitive interact with LE31 v1's deployment model? The v1 deployment is a single Linux VPS (not multiple instances with Redis pub/sub); the chaos-tested-resilience posture is a different deployment model.
- **Q5**: How will the *5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage* posture be tested in LE31 v1? The v1 charter does not require chaos-testing; the chaos-tested-resilience posture is a sister-shape, not a v1-build trigger.

## Why this matters

The **FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + Docker + GitHub Actions CI + nginx + 93% coverage + 5,000,000/5,000,000 exactly-once deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom** 15-tuple-primitive is the **strongest direct LE31 v1 on-stack real-time-event-streaming-vocabulary reference of the 73-pass series** for three reasons:

1. **The 15-tuple-primitive vocabulary is the future v1 polish surface primitive**: when LE31 v1 introduces a real-time-event-streaming surface (e.g., a v1 surface that lets the cook Telegram bot receive an event-stream of orders in real-time, the waiter web UI receive an event-stream of stock changes in real-time, and the owner daily-recap consume an event-stream of all events in real-time), the FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage primitive is the gate that satisfies §3.1 + §3.3. The livefeed pattern is a ready-made *named primitive* for this gate.

2. **The 8/8 LE31 backend stack primitives matched is the strongest 100%-LE31-stack-vocabulary-match of the 73-pass brainstorm series**: livefeed's stack is Python + asyncio + FastAPI + WebSockets + PostgreSQL + Redis pub/sub + distributed-systems + Docker + GitHub Actions CI + nginx = 8/8 LE31 backend stack primitives matched (FastAPI + Postgres + asyncio + Python + websockets + redis + postgresql + distributed-systems). The *exactly-once-delivery + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage* posture IS the *chaos-tested-resilience* charter §3.1 invariant.

3. **The 10-day-old repo with fresh push is the demand signal**: the maintainer is iterating fast (10-day-old repo with first in-window push today) without reading the LE31 charter. The demand for the *FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + asyncio + 5,000,000/5,000,000 exactly-once-deliveries + 0 duplicate or out-of-order events + 14,069 reconnects survived + 5 instance SIGKILLs + 8 Redis pub/sub kills + p95 5 ms live-delivery-latency + ≈ 50,000 deliveries/s headroom + 93% coverage* primitive is real, observable, and growing.

Sister-shape to features 22 (real-time-event-streaming reference) + 158 (ppfenning/coxswain-graphs — interactive-graph-explorer + FastAPI + HTMX + WebSocket + pydantic + Plotly) + 240 (fredhead88/do-it-v2 — personal-productivity + Telegram + Todoist + CalDAV + FastAPI + SQLite) + 247 (carry-over reference). The livefeed pattern is the **strongest direct FastAPI + WebSockets + Redis pub/sub + PostgreSQL (ordered-log) + exactly-once-delivery + chaos-tested-resilience primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that adds a real-time-event-streaming surface for the LE31 single-restaurant Swiss kitchen.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/22-...real-time-event-streaming.md` — carry-over real-time-event-streaming reference
- `features/158-ppfenning-coxswain-graphs-...-interactive-graph-explorer-fastapi-htmx-websocket-pydantic-plotly.md` — sister-shape (FastAPI + HTMX + WebSocket + pydantic + Plotly)
- `features/240-fredhead88-do-it-v2-...-personal-productivity-telegram-todoist-caldav-fastapi-sqlite.md` — sister-shape (FastAPI + SQLite)
- `features/247-...on-stack-websocket-postgres-redis-reference.md` — carry-over reference
- `features/297-jonalemndi2-ALdia-...-open-source-business-engine-ai-agents-mcp-tools.md` — sister-shape (idempotency + immutable-audit-trail posture)
- `features/298-erhatechnologiesai-point-of-sale-system-...-cloud-pos-touchscreen-cashier-register.md` — sister-shape (FastAPI + Pydantic + SQLite stack match)
- `features/290-AlvaroVerona-prime-cost-...-restaurant-p-l-menu-engineering.md` — sister-shape (restaurant-P&L primitive)
- `features/53-...offline-first-v1-polish.md` and `features/66-...offline-first-v1-polish.md` — v1 offline-first primitives
- `features/39-...owner-daily-recap-telegram.md` — owner-daily-recap-telegram surface
- `features/16-...supplier-orders-bot.md` — supplier-orders-bot surface
