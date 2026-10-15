# Feature 323 — `movsarusumov172-crypto/KitchenQ` v1 tiny-FastAPI+WebSocket+crossover-restaurant-stack-shape-vocabulary (defer)

> **NEW observation (2026-10-15).** Documents in-window GitHub repo `movsarusumov172-crypto/KitchenQ` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, **43 KB tiny**, language Python ✓ ON-STACK + FastAPI + SQLite + WebSocket + vanilla-JS, **pushed 2026-10-11T17:00:26Z AND created 2026-10-11T17:00:20Z = IN-WINDOW BY BOTH FIELDS**, parent-direct-GitHub-API-GET-verified 2026-10-15 from `/tmp/le31-brainstorm-2026-10-15/verify/ghverify__parent_movsarusumov172-crypto_KitchenQ.json`). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-15): *"Real-time restaurant ordering: waiter, kitchen and hall screens over WebSocket with a stop-list, table bills and a daily report."* Topics (verbatim, parent-verified): `fastapi`, `python`, `realtime`, `restaurant`, `sqlite`, `vanilla-js`, `websocket` = **7 topics including `fastapi + python + realtime + restaurant` (the v1 in-domain cross-section match) + `sqlite + websocket + vanilla-js` (the §3.1 portable-to-Postgres + §3.5 real-time + §3.1 portable-to-HTMX primitives)** = **canonical v1 tiny-FastAPI+WebSocket+crossover-restaurant-stack-shape-vocabulary of the 77-pass brainstorm series**. Bucket: **v1 (parking-lot, vocabulary reference)** — Pick A of Daily Brainstorm 2026-10-15. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **real-time-restaurant-ordering + waiter/kitchen/hall-screens + WebSocket + stop-list + table-bills + daily-report** sextuple-primitive as a persistent cross-section reference for the LE31 v1 *real-time waiter/kitchen/hall screens over WebSocket + per-table stop-list* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (4-day-old repo with first in-window push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **real-time-restaurant-ordering + waiter/kitchen/hall-screens + WebSocket + stop-list + table-bills + daily-report** sextuple-primitive: (1) *Real-time restaurant ordering* (orders flow from the table-side to the kitchen-side in real-time); (2) *Waiter/kitchen/hall screens* (three operator surfaces, all driven by the same ordering pipeline); (3) *WebSocket* (the real-time transport for stateful push from server to clients); (4) *Stop-list* (per-item stock-out signal that propagates to waiter + hall + kitchen in real-time); (5) *Table bills* (running per-table total displayed on the waiter/hall screens); (6) *Daily report* (end-of-day total summary). This is the §3.1 explicit-state-transition + §3.5 real-time-operator-coordination charter invariant applied to the *crossover-restaurant-app + kitchen-workflow + live-floor-link* dimension
- A written record of the **Python + FastAPI + SQLite + WebSocket + vanilla-JS** stack-shape: this is **2 of 4 LE31 backend stack primitives matched** (Python + FastAPI is on-stack; SQLite is portable to LE31's Postgres + SQLModel; WebSocket is portable to LE31's SSE cook-channel feature 23; vanilla-JS is portable to LE31's minimal-HTML/HTMX); the **Python + FastAPI backend** is the LE31-stack-match primitive
- A written record of the **real-time-waiter/kitchen/hall-screens-over-WebSocket** operator-surface-shape: every order change is pushed from the server to the waiter/kitchen/hall screens over a single WebSocket connection; the kitchen can stop accepting an item and the waiter/hall screens update in < 1 second. Sister-shape to features 02 (waiter order-taking) + 09 (kitchen delay visibility) + 23 (sse-cook-channel) + 25 (viability ledger)
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with no community traction signal; (2) the stack-shape match is the value, not the code (LE31 v1's *real-time-over-WebSocket* future surface could adopt the shape but not the codebase — too small + too new); (3) the *demand-signal* is the value, not the code-adoption opportunity

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3)
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema
- Adoption of the `KitchenQ` codebase (4-day-old single-maintainer repo with no observed production usage; total size 43 KB is too small for production-grade real-time REST + WebSocket)
- Cross-pollination with the v1 cook-Telegram-bot (LE31's cook-bot uses aiogram Telegram transport; `KitchenQ` uses WebSocket; the *3-operator-screens-over-WebSocket* shape is the transferable item, not the WebSocket transport itself)

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v1 surface proposes "the *3-operator-screens (waiter/kitchen/hall) over a single real-time transport + per-table stop-list propagation + running-table-bill + end-of-day daily-report*" surface (e.g., a v1 PR that introduces a *real-time-per-table-floor-view* for the waiter that subscribes via WebSocket to a FastAPI server and sees the kitchen's stop-list updates + the hall screen's table statuses in real-time, with a per-table running bill that updates with every order), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "real-time-3-operator-screens + per-table-stop-list + running-table-bill + daily-report" is a real demand signal*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `realtime + restaurant + websocket + fastapi + sqlite + vanilla-js`)
- **Confidence**: medium-high for the vocabulary match (the verbatim description names the 6-primitive set + the tech-stack); low for transferability (LE31 v1 today is single-restaurant + aiogram + HTMX + Postgres; the *real-time-3-operator-screens-over-WebSocket* shape is new)
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1's waiter-side polling-HTMX is 30-second, not real-time; the v1 charter has no real-time-floor-view surface); the value is the *real-time-3-operator-screens-over-WebSocket* vocabulary — when the first v1 PR that adds a *real-time-per-table-floor-view* surface lands, the `KitchenQ` pattern is a ready-made *named primitive*

## Description

GitHub `movsarusumov172-crypto/KitchenQ` (MIT, 0★/0⑂, Python + FastAPI + SQLite + WebSocket + vanilla-JS, pushed 2026-10-11T17:00:26Z, created 2026-10-11T17:00:20Z = 4-day-old repo with both-window, 43 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-15): *"Real-time restaurant ordering: waiter, kitchen and hall screens over WebSocket with a stop-list, table bills and a daily report."*

The architectural primitive has six sub-primitives that map 1:1 onto the LE31 v1 *real-time-floor-view* surface:

1. **Real-time restaurant ordering** — orders flow from the table-side to the kitchen-side in real-time over WebSocket. The *real-time-restaurant-ordering* primitive maps 1:1 onto LE31's `OrderItem` state-change schema (which already supports atomic state transitions).
2. **Waiter/kitchen/hall screens** — three operator surfaces, all driven by the same ordering pipeline. The *3-operator-screens* primitive maps 1:1 onto LE31's existing *waiter-app (feature 02) + cook-bot (feature 03) + owner-recap (feature 04)* surfaces, extended with a *hall screen* for the maître d'.
3. **WebSocket** — the real-time transport for stateful push from server to clients. The *WebSocket* primitive maps 1:1 onto any future v1 surface that needs real-time push (vs today's 30-second-polling-HTMX).
4. **Stop-list** — per-item stock-out signal that propagates to waiter + hall + kitchen in real-time. The *stop-list* primitive maps 1:1 onto LE31's `StockEntry` schema (which already implements stop-list-item as a stock-event).
5. **Table bills** — running per-table total displayed on the waiter/hall screens. The *table-bill* primitive maps 1:1 onto LE31's `Visit` (table-state) + `OrderItem` (line-item) schema (which already supports running-totals).
6. **Daily report** — end-of-day total summary. The *daily-report* primitive maps 1:1 onto LE31's `tips_daily` view (feature 05) + a future v1 *daily-summary* surface.

**The 1:1 mapping onto LE31 surface:**

| `KitchenQ` primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Real-time restaurant ordering | `OrderItem` (atomic state transitions) | §3.1 ✓ | **Implemented (v1)** |
| Waiter/kitchen/hall screens | waiter-app (02) + cook-bot (03) + owner-recap (04) + (new: hall-screen) | n/a | **Partially implemented; hall-screen = new v1 surface** |
| WebSocket | (LE31 v1 uses 30-second-polling-HTMX + SSE for cook-channel feature 23) | §3.5 | **Not implemented — new v1 surface (WebSocket route in FastAPI)** |
| Stop-list | `StockEntry` (already implements stop-list-item) | §3.1 ✓ | **Implemented (v1)** — the propagation logic is new |
| Table bills | `Visit` (table-state) + `OrderItem` (line-item) running-totals | §3.6 | **Implemented (v1)** — the *real-time-table-bill* display is new |
| Daily report | `tips_daily` view (feature 05) + (new: daily-summary surface) | §3.6 | **Partially implemented** |
| Python + FastAPI | Python + FastAPI + SQLModel | §3.1 ✓ | **Implemented (v1)** |
| SQLite | (LE31 v1 uses Postgres + SQLModel) | §3.2 | **Portable to LE31 Postgres** |
| vanilla-JS | (LE31 v1 uses minimal-HTML/HTMX) | §3.1 | **Portable to LE31 HTMX** |

## Dependencies

- [02-order-taking.md](../features/02-order-taking.md) — orders belong to a visit; the waiter-side order-taking surface exists in v1 today
- [03-kitchen-stock-tracker.md](../features/03-kitchen-stock-tracker.md) — the stop-list-item event is already implemented as a `StockEntry` schema
- [23-sse-cook-channel](../features/23) (assumed) — the existing cook-channel uses SSE; the *real-time-3-operator-screens-over-WebSocket* shape could replace SSE with WebSocket for sub-second latency (vs SSE's at-least-one-event-per-30-second-polling)

## Open questions

- Should the WebSocket transport replace SSE for the cook-channel, or coexist (SSE for cook-only, WebSocket for waiter + hall + kitchen)?
- Should the per-table stop-list propagation be a per-item-pushed WebSocket event, or a per-`StockEntry`-change-pushed WebSocket event?
- Should the daily-report be a separate WebSocket event at midnight (operator-pushed) or a FastAPI `/daily-report` GET endpoint called at midnight by the owner's daily-recap bot?

## Why this matters

The **real-time-3-operator-screens + per-table-stop-list + running-table-bill + daily-report** sextuple-primitive is a *stronger* v1 cross-section vocabulary than any of features 02/09/23/25 alone. The 43 KB tiny posture IS the §3.1 *single-concern-library* invariant. The Python + FastAPI ON-STACK posture aligns with §3.1. The WebSocket posture IS portable to LE31's existing SSE cook-channel. The stop-list discipline IS the §3.5 *operator-can-keep-working-during-supply-shortage* invariant applied to the *real-time-stop-list-propagation* dimension. The 0★/0⑂ + 4-day-old-repo + both-window + MIT permissive + Python + FastAPI ON-STACK + ~6 active files = the cleanest v1 cross-section demand-signal of the 77-pass brainstorm series. Sister-shape to feature 22 (MhlG67/grid-table-manager — the v1 live-floor-view HTML-table-updates-via-WebSocket-connection, 0★ MIT, Python FastAPI + WebSocket, the only other v1 cross-section reference that uses WebSocket-over-HTTP for live-floor-updates in the entire features/ directory).

## Rollback path

This defer artifact is fully reversible:
- Delete the feature file: `rm /opt/data/le31_mmm3_research/features/323-movsarusumov172-crypto-KitchenQ-...md`
- Delete the HANDOFF: `rm /opt/data/le31_mmm3_research/specs/323-movsarusumov172-crypto-KitchenQ-...-HANDOFF.md`
- No code change was made today, so no rollback of code is required
- No database migration was made today, so no rollback of schema is required
- No pin change was made today (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1)
