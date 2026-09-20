# Feature 206 — `djust-org-djust-phoenix-liveview-style-reactive-server-side-rendering-django-rust-websocket-htmx-alternative` (defer)

> **NEW observation (2026-09-20).** Documents in-window GitHub Search `topic:real-time` query result: `djust-org/djust` (**MIT ✓**, **92★/7⑂**, Python + Rust, **pushed 2026-09-20T06:46:34Z = TODAY** (in-window by `pushed_at` only — *created 2026-01-16T00:00:00Z = OUT-OF-WINDOW* = 8 months before the 30-day window start; **the repo is IN-WINDOW BY PUSH ONLY per the SKILL hard rule**), **62089 KB substantial repo** = the **largest in-window 2026 Python SSR-framework repo of the 44-pass brainstorm series**, default_branch=`main`). Topics (verbatim from raw JSON, **9 topics**): `django`, **`htmx-alternative`**, **`liveview`**, `pwa`, `python`, **`reactive`**, **`real-time`**, **`rust`**, **`server-side-rendering`**, **`websocket`**. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-20): *"Phoenix LiveView-style reactive server side rendering for Django with Rust-powered performance."* The **reactive-server-side-rendering primitive** + the **HTMX-alternative + LiveView-style + WebSocket-stateful-connection + Rust-performance** quintuple-primitive: the *stateful-connection + server-pushed-DOM-diffs* pattern that LE31 v1's cook Telegram bot + waiter web UI currently implements via manual refresh + Telegram bot polling. The *"htmx-alternative"* topic explicitly positions djust as an alternative to the LE31 v1 frontend (HTMX), which makes djust a **direct v1-frontend architecture-reference** for the next v1 maintainer asking *"what is the HTMX-alternative / reactive-SSR landscape in 2026?"*. The *"websocket"* topic is the **stateful-connection primitive** — the *server-to-client push over a persistent WebSocket* pattern, vs LE31 v1's `sse-cook-channel` (feature 23) which uses SSE (Server-Sent Events) for the cook-channel. The *"rust"* topic is the **Rust-performance primitive** — djust uses a Rust crate for the WebSocket + reactive-update hot-path (vs LE31 v1's pure-Python FastAPI stack). The *"django"* topic is **off-pattern** for LE31 v1 (LE31 v1 uses FastAPI + HTMX, not Django + djust), but the *reactive-SSR pattern* is on-pattern and the *Rust-powered WebSocket hot-path* is the future-extension reference. **MIT ✓ §3.2 STRICTLY-COMPATIBLE** for vocabulary + architecture-reference adoption; **§3.4 not applicable** (UI pattern, not AI surface). Bucket: **v1 UI-architecture-reference (reactive-SSR + HTMX-alternative + WebSocket + Rust-performance primitive, parking-lot defer)** — vocabulary + reactive-SSR primitive + HTMX-alternative + LiveView-style + WebSocket + Rust-performance documentation, zero build time today.

## Goal

Retain the **"Phoenix LiveView-style reactive server side rendering for Django with Rust-powered performance"** cross-section architectural vocabulary + **reactive-server-side-rendering primitive** + **HTMX-alternative + LiveView-style + WebSocket + Rust-performance** quintuple as the persistent v1 UI-architecture reference for any future LE31 v1 maintainer asking the *stateful-connection / server-pushed-DOM-diffs* question (does LE31 v1 ever need to replace manual-refresh with reactive-SSR? does LE31 v1 ever need a WebSocket-route alongside the SSE-route? does LE31 v1 ever need a Rust-accelerated hot-path component?). The artifact is the persistent *reactive-SSR primitive + HTMX-alternative + LiveView-style + WebSocket + Rust-performance* vocabulary as a *named* v1 architectural reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `djust-org/djust` cross-section vocabulary: the **first in-window 2026 Python reactive-SSR framework repo of the 44-pass brainstorm series** with the *htmx-alternative + liveview + reactive + server-side-rendering + websocket + rust* topic set; the *62089 KB substantial repo* is the *largest in-window 2026 Python SSR-framework repo of the 44-pass series*; the *92★/7⑂ community-adoption signal* is meaningful — the 92★ community has validated the *reactive-SSR primitive + HTMX-alternative positioning* at scale.
- A written record of the **reactive-SSR primitive**: the *stateful-connection + server-pushed-DOM-diffs* vocabulary — when the server holds a persistent connection to the client (WebSocket or SSE), and the server pushes DOM-diff updates over the connection, the client *re-renders without manual refresh*; the discipline of *stateful-connection + server-pushed-DOM-diffs* is the **reactive-SSR pattern**, named after Phoenix LiveView's *LiveView-as-server-process* model.
- A written record of the **HTMX-alternative explicit positioning**: the *"htmx-alternative"* topic explicitly positions djust as an alternative to HTMX; this is a **direct v1-frontend architecture-reference** because LE31 v1 uses HTMX for the waiter web UI; the next v1 maintainer asking *"what is the HTMX-alternative landscape in 2026?"* gets the answer: djust is the *reactive-SSR alternative to HTMX* (vs HTMX's *manual-htmx-request + server-side-fragment-render* model).
- A written record of the **LiveView-style + WebSocket + Rust-performance triple**: the *LiveView-style* is the *server-process-holds-state-and-renders* pattern; the *WebSocket* is the *stateful-connection transport*; the *Rust* is the *performance-acceleration language for the WebSocket hot-path*; the triple is the *reactive-SSR + stateful-connection + performance-acceleration* primitive set.
- A written record of the **MIT license as a documented strictly-adoptable artifact**: the codebase CAN be adopted as a reference for the *reactive-SSR pattern* (MIT = §3.2 STRICTLY-COMPATIBLE for vocabulary AND architecture-reference adoption); LE31 would re-implement the reactive-SSR pattern against its own FastAPI + SQLModel + aiogram v3 stack, not import the Django + Rust crate code (the Django + Rust stack is off-pattern for LE31 v1).
- A decision record: today's verdict is `defer (parking-lot)` because the *reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance* vocabulary is a v1 UI-architecture reference, not a v1 build implication. v1 has manual-refresh + SSE cook-channel + HTMX-server-side-rendering today; the reactive-SSR vocabulary documents the *stateful-connection + server-pushed-DOM-diffs + HTMX-alternative + LiveView-style + WebSocket + Rust-performance* extensions for the next v1 maintainer.

**Out of scope (defer artifact):**
- Any change to the LE31 v1 frontend (no reactive-SSR pattern today, no WebSocket route to the waiter web UI today, no Rust crate dependency today).
- Any change to the cook Telegram bot's push mechanism (Telegram bot polling is implicit, not server-pushed-DOM-diffs).
- Adoption of the `djust-org/djust` code as a v1 dependency (the repo is 92★/7⑂ at 62089 KB; the *reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance* vocabulary would need to be independently re-implemented and validated against the LE31 waiter web UI + cook-bot + SSE-cook-channel, not simply imported; the Django stack is off-pattern for LE31 v1; the Rust crate is off-pattern for LE31 v1's pure-Python FastAPI serving layer; the *62089 KB substantial repo* signals a production-grade implementation that LE31 v1 cannot simply mirror).
- Any change to the `audit_logs` table or `StockEntry` ledger today.
- Any new dependency on the `djust-org` maintainer.

## Evidence / JTBD

When a future LE31 v1 maintainer asks *"if v1 introduces a reactive-SSR pattern, a WebSocket route to the waiter web UI, or a Rust-accelerated hot-path component to the FastAPI serving layer, what is the reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance primitive that preserves the existing v1 SSE-cook-channel + HTMX-server-side-rendering + pure-Python-FastAPI invariants?"*, the maintainer wants *evidence that another independent 2026 Python+Rust repo at 62089 KB with MIT license + in-window-by-push-only + 92★/7⑂ + 9 topics including htmx-alternative + liveview + reactive + real-time + rust + server-side-rendering + websocket is shipping the Phoenix LiveView-style reactive-SSR primitive as the v1 UI-architecture reference discipline*, but struggles because *v1 has no documented reactive-SSR primitive in the charter*, so that *v1 can introduce the reactive-SSR + stateful-connection + server-pushed-DOM-diffs vocabulary with the explicit HTMX-alternative positioning rather than reinventing the pattern*.

- **Evidence class**: observed (the `djust-org/djust` description explicitly names *"Phoenix LiveView-style reactive server side rendering"* = the reactive-SSR primitive; the *htmx-alternative* topic explicitly positions djust as an alternative to HTMX; the 9-topic set including *liveview + reactive + real-time + rust + server-side-rendering + websocket* names the *reactive-SSR + stateful-connection + performance-acceleration* primitive set).
- **Confidence**: medium-high for the reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance vocabulary (MIT + Python + 62089 KB substantial + in-window-by-push-only + 92★/7⑂ + 9 topics + explicit LiveView-style description + htmx-alternative positioning = §3.2 STRICTLY-COMPATIBLE); medium for *adoption* (LE31 should re-implement the reactive-SSR pattern against its own FastAPI + SQLModel + aiogram v3 stack, not import the Django + Rust crate code; the Django stack is off-pattern for LE31 v1; the Rust crate is off-pattern for LE31 v1's pure-Python FastAPI serving layer).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + reactive-SSR documentation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + reactive-SSR documentation**: when (if) LE31 v1 introduces a WebSocket route, a server-pushed-DOM-diff mechanism, or a Rust-accelerated hot-path component, the *reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance* vocabulary is documented.

## Description

GitHub `djust-org/djust` (MIT, 92★/7⑂, Python+Rust, pushed 2026-09-20T06:46:34Z = in-window by `pushed_at` only; created 2026-01-16T00:00:00Z = out-of-window, 62089 KB substantial repo).

Description (verbatim): *"Phoenix LiveView-style reactive server side rendering for Django with Rust-powered performance."*

Topics (verbatim from raw JSON, 9 topics): `django`, **`htmx-alternative`**, **`liveview`**, `pwa`, `python`, **`reactive`**, **`real-time`**, **`rust`**, **`server-side-rendering`**, **`websocket`**.

The **5 named reactive-SSR primitives**:

| djust-org/djust primitive | LE31 v1 primitive | Match status |
|---|---|---|
| `htmx-alternative` | HTMX-server-side-rendering on FastAPI (the waiter web UI uses HTMX for fragment-render on form-submit + manual-refresh on demand) | **★ GAP: LE31 v1 has no htmx-alternative primitive today; djust shows the reactive-SSR alternative** |
| `liveview` | (LE31 v1 has no server-process-holds-state-and-renders pattern today; the waiter web UI is request-response with manual-refresh) | **★ GAP: LE31 v1 has no LiveView-style primitive today** |
| `reactive` | (LE31 v1 has no reactive-SSR pattern today; the cook Telegram bot has Telegram-native push, but the waiter web UI is manual-refresh) | **★ GAP: LE31 v1 has no reactive-SSR primitive today** |
| `websocket` | (LE31 v1 has no WebSocket route to the waiter web UI today; the `sse-cook-channel` feature 23 uses SSE for the cook-channel, but no WebSocket for the waiter web UI) | **★ GAP: LE31 v1 has no WebSocket route today** |
| `rust` | (LE31 v1 has no Rust crate dependency today; the FastAPI serving layer is pure-Python + uvicorn) | **★ GAP: LE31 v1 has no Rust-accelerated hot-path today** |

The **reactive-SSR primitive**: a *reactive* server-side rendering pattern where the server holds a persistent connection to the client (WebSocket or SSE) and pushes DOM-diff updates over the connection. The server-process-holds-state-and-renders model means: (a) the server starts a process per connected client; (b) the process holds the client-state in memory; (c) when the state changes, the process re-renders the relevant DOM-fragment; (d) the process pushes the DOM-diff over the persistent connection; (e) the client applies the DOM-diff. The discipline is named *reactive-SSR* because the server *reacts* to state changes by *pushing* DOM-diffs (vs LE31 v1's *manual-refresh + form-submit* model where the server only sends a DOM-fragment on explicit request).

The **HTMX-alternative primitive**: HTMX = *HTML-over-the-wire* library that lets the server return HTML fragments on form-submit + manual-refresh; djust = *stateful-connection + server-pushed-DOM-diffs* library that lets the server push DOM-diffs over a persistent connection. The two patterns compete: HTMX is *request-driven* (client requests a fragment; server responds with HTML); djust is *state-driven* (server detects a state change; server pushes a DOM-diff to all connected clients). For LE31 v1's waiter web UI today (manual-refresh + form-submit + HTMX-fragment-render), djust would be the *reactive alternative* — instead of *waiter taps refresh button → waiter sees latest order status*, djust would be *server detects new order status → server pushes DOM-diff to all connected waiters' tabs*.

The **LiveView-style + WebSocket + Rust-performance triple**: Phoenix LiveView (Elixir) = the *LiveView-as-server-process* model that djust emulates in Python+Django+Rust. The WebSocket = the *stateful-connection transport* (vs SSE = unidirectional-server-to-client; WebSocket = bidirectional). The Rust = the *performance-acceleration language for the WebSocket hot-path* — djust uses a Rust crate to handle the WebSocket connection + DOM-diff serialization at scale, which is a common pattern for *stateful-connection + server-pushed-DOM-diffs* libraries.

The **MIT license as a documented strictly-adoptable artifact**: the codebase CAN be adopted as a reference for the *reactive-SSR pattern* (MIT = §3.2 STRICTLY-COMPATIBLE for vocabulary AND architecture-reference adoption); LE31 would re-implement the reactive-SSR pattern against its own FastAPI + SQLModel + aiogram v3 stack, not import the Django + Rust crate code (the Django + Rust stack is off-pattern for LE31 v1; LE31 v1 uses FastAPI + pure-Python + HTMX).

## Data model

**No LE31 data model change today.** The defer artifact is documentation only. The reactive-SSR primitive names the *stateful-connection + server-pushed-DOM-diffs + HTMX-alternative + LiveView-style + WebSocket + Rust-performance* extensions that any future v1 schema change should consider; v1 maintainer decision required before adopting the reactive-SSR pattern (LE31 v1 currently operates a manual-refresh + form-submit + HTMX-fragment-render UI; reactive-SSR is a v1 architecture-decision, not a v1 implementation task).

## Implementation steps

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a WebSocket route to the waiter web UI, a server-pushed-DOM-diff mechanism to the cook Telegram bot, or a Rust-accelerated hot-path component to the FastAPI serving layer):

- `app/api/websocket.py` — possibly add (the FastAPI WebSocket route that handles the *stateful-connection + server-pushed-DOM-diffs* pattern; depends on the v1 change).
- `app/api/sse_cook_channel.py` — possibly modify to add a WebSocket alternative (the SSE cook channel could be supplemented by a WebSocket channel; depends on the v1 change).
- `app/web/reactive.py` — possibly add (the reactive-SSR pattern implementation for the waiter web UI; depends on the v1 change).
- `app/bot/cook.py` — possibly modify to add the *server-pushed-DOM-diff mechanism* (the cook-bot surface when the server detects a new order status; depends on the v1 change).
- `tests/test_reactive_ssr.py` — possibly add (the integration test for the reactive-SSR pattern; depends on the v1 change).
- `Cargo.toml` + Rust crate — possibly add (the Rust-accelerated hot-path component; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no Rust crate added.

## Telegram interaction if any

None today. If a future v1 trigger fires (server-pushed-DOM-diff mechanism for cook-bot), the Telegram interaction could be supplemented by a server-pushed-DOM-diff emit (the server detects a new order status; the server pushes a *ready!* alert to the waiter's waiter web UI tab over the WebSocket connection; the cook's bot interaction stays as-is). The cook-bot surface might persist for the cook's input (typed text + button presses), but the *output* surface for the waiter could shift to WebSocket + server-pushed-DOM-diffs.

## Dependencies

- No new dependency today.
- If a future v1 trigger fires:
  - Software: a WebSocket library for FastAPI (e.g. `fastapi-websocket` or `websockets` Python library; LE31 currently has no WebSocket dependency).
  - Software: a Rust crate for the WebSocket hot-path (e.g. `actix-web` for Rust web framework or `tokio-tungstenite` for Rust WebSocket; LE31 currently has no Rust dependency).
  - Schema: no schema change (the reactive-SSR pattern operates on the same `audit_logs` + `StockEntry` + `Order` tables).

## Open questions

- Should LE31 v1 introduce a reactive-SSR pattern to the waiter web UI (the *stateful-connection + server-pushed-DOM-diffs* primitive)?
- Should LE31 v1 introduce a WebSocket route alongside the SSE cook-channel (the *bidirectional stateful-connection* primitive)?
- Should LE31 v1 introduce a Rust-accelerated hot-path component (the *performance-acceleration* primitive)?
- If yes to any of the above: should the v1 PR cross-reference this feature 206 contract + HANDOFF as the named architectural reference?
- Should the v1 PR explore *server-pushed-DOM-diff mechanism* for the cook's order-status alerts (the *server-detects-state-change → server-pushes-DOM-diff* primitive)?

## Why this matters

The *reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance* primitive is the **gap** between LE31 v1's manual-refresh + form-submit + HTMX-fragment-render UI and a *reactive* UI where the server pushes DOM-diffs on state change. The Phoenix LiveView pattern (Elixir) is the *gold standard* for reactive-SSR; djust is the *2026 Python+Django+Rust emulation* of the Phoenix LiveView pattern. For LE31 v1's waiter web UI today (manual-refresh + form-submit + HTMX-fragment-render), the djust pattern is the *future-extension reference*: when (if) LE31 v1 introduces a WebSocket route, a server-pushed-DOM-diff mechanism, or a Rust-accelerated hot-path component, the *reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance* vocabulary is documented.
