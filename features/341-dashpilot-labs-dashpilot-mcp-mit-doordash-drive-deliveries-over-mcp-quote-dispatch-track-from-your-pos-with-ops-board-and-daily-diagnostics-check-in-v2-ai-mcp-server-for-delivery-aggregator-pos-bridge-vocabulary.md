# Feature 341 — `dashpilot-labs-dashpilot-mcp-mit-doordash-drive-deliveries-over-mcp-quote-dispatch-track-from-your-pos-with-ops-board-and-daily-diagnostics-check-in-v2-ai-mcp-server-for-delivery-aggregator-pos-bridge-vocabulary` (defer)

> **NEW observation (2026-10-18).** Documents in-window GitHub repo `dashpilot-labs/dashpilot-mcp` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, **Python ✓ ON-STACK** + MCP + Model-Context-Protocol + DoorDash + delivery + POS + restaurant, **pushed 2026-10-07T11:20:52Z AND created 2026-10-04T09:10:47Z = IN-WINDOW BY BOTH FIELDS** (~14-day-old repo with in-window `pushed_at` and `created_at`; both fields in window), **252 KB modest repo**, default_branch=`main`, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-18): *"DoorDash Drive deliveries over MCP — quote, dispatch, and track from your POS, with an ops board and a daily diagnostics check-in."*. Topics (verbatim, parent-verified, **6 topics**): `delivery, doordash, mcp, model-context-protocol, pos, restaurant`. Bucket: **v2-AI (MCP-server-for-delivery-aggregator-+-POS-bridge-vocabulary)** — Pick A of Daily Brainstorm 2026-10-18. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **MCP-server-for-Delivery-Aggregator-+-POS-bridge + quote-dispatch-track + ops-board + daily-diagnostics-check-in + DoorDash-Drive + restaurant + MCP + Model-Context-Protocol** 6-tuple-primitive as a persistent cross-section reference for the LE31 v2-AI *delivery-aggregator-MCP-bridge* wedge, and document the **MCP-as-cross-system-tooling-for-delivery-aggregators + ops-board + daily-diagnostics-check-in** primitive that an independent maintainer shipped in 2026 (~14-day-old repo with in-window `created_at` AND `pushed_at`) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **MCP-server-for-Delivery-Aggregator-+-POS-bridge + quote-dispatch-track + ops-board + daily-diagnostics-check-in + DoorDash-Drive + restaurant + MCP + Model-Context-Protocol** 6-tuple-primitive: an MCP server that wraps a delivery aggregator (DoorDash Drive) so that an LLM agent (or a POS UI surface) can quote, dispatch, and track a delivery; the server exposes the delivery aggregator as MCP tools; an ops board surfaces the delivery state to operators; a daily-diagnostics-check-in audits the delivery health overnight. This is the §3.4 *MCP-as-cross-system-tooling + observable-evidence + non-AI-fallback* invariant applied to the *delivery-aggregator-MCP-bridge* dimension.
- A written record of the **MIT + 0★/0⑨ + 252 KB modest + 6-topic array + Python ✓ ON-STACK + MCP + Model-Context-Protocol + DoorDash + restaurant + delivery + POS** stack-shape: this is the **first MCP-server-for-delivery-aggregator-+-POS-bridge vocabulary of the 80-pass brainstorm series**; the prior `sanjibani/cleancloud-mcp` (2026-10-17 brainstorm Pick C) covered the *MCP-server-for-CleanCloud-POS-API-+-small-business* dimension; today's pick extends the *MCP-server-as-POS-/aggregator-bridge* cluster to the *delivery-aggregator* dimension.
- A written record of the **operator-facing vocabulary** discipline: the operator does not directly interact with DoorDash; the operator interacts with the ops board; the ops board is fed by the MCP server; the MCP server calls the DoorDash Drive API; the daily-diagnostics-check-in audits the delivery health overnight; the LLM agent (when permitted by charter §3.4 scope) can call the MCP server tools to quote, dispatch, and track a delivery on demand. Sister-shape to today's research PICK B `FlashyLabs/flashy-ledger` (TypeScript AAO-stack-ledger-rules) + 2026-10-17 brainstorm Pick C `sanjibani/cleancloud-mcp` (MCP-server-for-CleanCloud-POS-API-+-small-business) + features 263 (v2-AI *MCP-server-as-cross-system-tooling* reference) + 286 (v2-AI *MCP-server-as-cross-system-tooling* sister-shape) + 288 (v2-AI *MCP-server-CVE/KEV-attestation-gate*) + 306 (v2-AI *MCP-as-cross-system-tooling* concierge) — the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* posture IS the canonical v2-AI *delivery-aggregator-MCP-bridge-vocabulary* applied to the *LE31-v2-AI-delivery-aggregator* dimension.
- A decision record: today's verdict is `defer` because (1) the v2 charter has *no delivery-aggregator-MCP-bridge surface* (LE31 v2 is owner-pains + AI-assisted, not delivery-aggregator-bridged); (2) the stack-shape match is the value, not the code (LE31 v2 uses Python + FastAPI + Postgres, not MCP-server-for-DoorDash-Drive + ops-board); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v2's planned AI-assisted owner-pains surfaces.
- Adoption of the dashpilot-mcp codebase (MIT + 0★/0⑨ + 14-day-old repo with in-window `created_at` AND `pushed_at`).
- Cross-pollination with the v2 charter §3.4 *MCP-as-cross-system-tooling + observable-evidence + non-AI-fallback* posture (the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* discipline IS the §3.4 invariant; the *delivery-aggregator-bridge + ops-board* posture IS the §3.7 *minimal-PII-only-aggregator-API-bridge* invariant).
- Any vendor-relationship with DoorDash / "all aggregators" (LE31 v2 has no delivery-aggregator integration today; v1 is on-premise single-restaurant + take-away + no-delivery-aggregator).
- Cross-section candidate for v1 if LE31 ever adds a delivery-aggregator surface (charter §3.7 review required: the *aggregator-API + delivery-tracking + ops-board* posture requires explicit non-AI-fallback and explicit PII-minimal-bridge scope before any v1 PR).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v2-AI code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "an MCP-server-for-delivery-aggregator-+-POS-bridge + quote-dispatch-track + ops-board + daily-diagnostics-check-in primitive" (e.g., a v2-AI surface that wraps DoorDash Drive or a similar delivery aggregator as MCP tools so that an LLM agent can quote, dispatch, and track a delivery on demand; an ops board surfaces the delivery state to operators; a daily-diagnostics-check-in audits the delivery health overnight), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "MCP-server-for-delivery-aggregator-+-POS-bridge + quote-dispatch-track + ops-board + daily-diagnostics-check-in" is a real demand signal*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in posture"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `delivery, doordash, mcp, model-context-protocol, pos, restaurant` + *"DoorDash Drive deliveries over MCP — quote, dispatch, and track from your POS, with an ops board and a daily diagnostics check-in"*).
- **Confidence**: medium-high for the vocabulary match (the verbatim description + topics name the 6-tuple-primitive set + the MCP-server-for-delivery-aggregator posture + the ops-board posture + the daily-diagnostics-check-in posture); low for transferability (LE31 v2 has no delivery-aggregator-MCP-bridge surface; v2 charter is owner-pains + AI-assisted, not delivery-aggregator-bridged).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v2 is owner-pains + AI-assisted with no delivery-aggregator surface); the value is the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* vocabulary — when the first v2-AI PR that adds a delivery-aggregator-MCP-bridge surface lands, the dashpilot-mcp pattern is a ready-made *named primitive*.

## Description

GitHub `dashpilot-labs/dashpilot-mcp` (MIT, 0★/0⑨, Python, pushed 2026-10-07T11:20:52Z, created 2026-10-04T09:10:47Z, 252 KB, default_branch=`main`, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-18): *"DoorDash Drive deliveries over MCP — quote, dispatch, and track from your POS, with an ops board and a daily diagnostics check-in."*.

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **MCP-server-for-Delivery-Aggregator-+-POS-bridge** — an MCP server that wraps a delivery aggregator (DoorDash Drive) so that an LLM agent (or a POS UI surface) can quote, dispatch, and track a delivery. The *MCP-server-for-Delivery-Aggregator-+-POS-bridge* primitive maps 1:1 onto any future v2-AI surface that needs an MCP-bridged delivery aggregator for the LE31 owner-pains surfaces.
2. **Quote-dispatch-track** — the three primitives an LLM agent (or POS UI) needs to interact with a delivery aggregator. The *quote-dispatch-track* posture IS the §3.1 *explicit-state-transitions* charter invariant applied to the *delivery-aggregator* dimension (quote = read, dispatch = state-transition, track = read-state).
3. **Ops-board** — the operator-facing surface that shows the delivery state. The *ops-board* posture IS the §3.1 *operator-orchestrates-the-aggregator* charter invariant applied to the *delivery-aggregator-ops* dimension.
4. **Daily-diagnostics-check-in** — an overnight audit of the delivery health (failed deliveries, untracked deliveries, late deliveries, etc.). The *daily-diagnostics-check-in* posture IS the §3.3 *append-only-audit-* charter invariant applied to the *delivery-aggregator-audit* dimension.
5. **DoorDash-Drive + restaurant + POS** — the delivery aggregator + the restaurant domain + the POS integration. The *DoorDash-Drive + restaurant + POS* posture IS the §3.7 *minimal-PII-only-aggregator-API-bridge* charter invariant applied to the *delivery-aggregator-PII* dimension.
6. **MCP + Model-Context-Protocol** — the cross-system-tooling protocol. The *MCP + Model-Context-Protocol* posture IS the §3.4 *MCP-as-cross-system-tooling* charter invariant applied to the *delivery-aggregator* dimension.

The defer artifact retains the **6-tuple-primitive** (MCP-server-for-Delivery-Aggregator-+-POS-bridge + quote-dispatch-track + ops-board + daily-diagnostics-check-in + DoorDash-Drive + restaurant + POS + MCP + Model-Context-Protocol + delivery) as a persistent cross-section reference.

## Data model

None today. The defer artifact is documentation only.

When the first v2-AI PR that adopts the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* discipline lands, the data model is:

```sql
-- hypothetical future v2-AI surface (NOT IMPLEMENTED TODAY)
CREATE TABLE delivery_aggregator_bridge (
    id SERIAL PRIMARY KEY,
    aggregator TEXT NOT NULL,            -- 'doordash' | 'ubereats' | 'wolt' | 'deliveroo' | ...
    api_endpoint TEXT NOT NULL,
    api_credentials_ref TEXT,            -- reference to an external secret manager; never raw credentials
    status TEXT NOT NULL DEFAULT 'active',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE delivery_quote (
    id SERIAL PRIMARY KEY,
    aggregator_id INT NOT NULL REFERENCES delivery_aggregator_bridge(id),
    external_quote_id TEXT,              -- the aggregator's quote id (nullable until quote is fetched)
    origin_address TEXT NOT NULL,
    destination_address TEXT NOT NULL,
    quoted_price_eur NUMERIC(10, 2),
    quoted_eta_seconds INT,
    status TEXT NOT NULL DEFAULT 'pending', -- 'pending' | 'quoted' | 'dispatched' | 'picked_up' | 'delivered' | 'cancelled' | 'failed'
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE delivery_dispatch (
    id SERIAL PRIMARY KEY,
    quote_id INT NOT NULL REFERENCES delivery_quote(id),
    aggregator_id INT NOT NULL REFERENCES delivery_aggregator_bridge(id),
    external_dispatch_id TEXT,
    driver_name TEXT,
    driver_phone TEXT,                   -- PII: charter §3.7 review required
    dispatched_at TIMESTAMPTZ,
    picked_up_at TIMESTAMPTZ,
    delivered_at TIMESTAMPTZ,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- append-only delivery event log (the §3.3 append-only-ledger invariant)
CREATE TABLE delivery_event (
    id BIGSERIAL PRIMARY KEY,
    delivery_id INT NOT NULL,             -- references delivery_quote OR delivery_dispatch
    delivery_kind TEXT NOT NULL,          -- 'quote' | 'dispatch'
    event_type TEXT NOT NULL,             -- 'quoted' | 'dispatched' | 'picked_up' | 'delivered' | 'cancelled' | 'failed' | 'tracking_update' | ...
    payload JSON NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- overnight delivery diagnostics check-in (the §3.3 daily-diagnostics-check-in invariant)
CREATE TABLE delivery_daily_diagnostics (
    id SERIAL PRIMARY KEY,
    run_date DATE NOT NULL UNIQUE,
    total_quotes INT NOT NULL,
    total_dispatches INT NOT NULL,
    total_delivered INT NOT NULL,
    total_failed INT NOT NULL,
    total_cancelled INT NOT NULL,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

## Implementation steps

None today. The defer artifact is documentation only.

When the first v2-AI PR that adopts the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* discipline lands, the implementation steps are:

1. Add Alembic migration for `DeliveryAggregatorBridge`, `DeliveryQuote`, `DeliveryDispatch`, `DeliveryEvent`, `DeliveryDailyDiagnostics` tables.
2. Add `backend/services/delivery_aggregator_bridge.py` with `DeliveryAggregatorBridge` class (wraps DoorDash Drive API; supports `quote`, `dispatch`, `track`).
3. Add `backend/services/delivery_daily_diagnostics.py` with `DeliveryDailyDiagnostics` class (overnight check-in; appends to `delivery_daily_diagnostics`).
4. Add `backend/mcp_server_delivery.py` FastMCP sub-app exposing `quote_delivery`, `dispatch_delivery`, `track_delivery` as MCP tools (the §3.4 *MCP-as-cross-system-tooling* posture).
5. Add `frontend/templates/delivery-ops-board.html` minimal-HTML/HTMX template for the ops board.
6. Wire the new sub-app into the parent uvicorn app.
7. Add `tests/test_delivery_aggregator_bridge.py` + `tests/integration/test_mcp_delivery.py`.
8. Add `cron/delivery_daily_diagnostics.py` for the overnight check-in.

## Telegram interaction if any

The MCP server is the primary interaction surface for the LLM agent. The ops board is the primary interaction surface for the operator. A Telegram notification is sent to the operator when a delivery is dispatched (via the cook Telegram bot's existing notification surface) and when the daily-diagnostics-check-in completes (via the owner Telegram bot's daily-recap surface). No new Telegram-bot surface today.

## Dependencies

When the first v2-AI PR that adopts the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* discipline lands, the dependencies are:

- `fastmcp` (Python MCP server framework; charter §3.4 *MCP-as-cross-system-tooling* required)
- `httpx` (async HTTP client for the DoorDash Drive API)
- Existing LE31 v1 stack: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX

## Open questions

- **§3.7 PII review**: the `delivery_dispatch.driver_name` + `delivery_dispatch.driver_phone` fields are PII; charter §3.7 *minimal-PII-only-aggregator-API-bridge* review required before any v2-AI PR that adopts this discipline lands.
- **§3.7 aggregator-credentials review**: the `delivery_aggregator_bridge.api_credentials_ref` is a reference to an external secret manager; charter §3.7 *no-raw-API-credentials* review required before any v2-AI PR.
- **DoorDash vs all aggregators**: today's pick is DoorDash-Drive-specific. The transferable discipline is the *MCP-server-for-delivery-aggregator-+-POS-bridge* posture, not the DoorDash-Drive API surface. The first v2-AI PR must decide whether to abstract over multiple aggregators (Wolt + UberEats + Deliveroo + DoorDash) or to start with a single aggregator (DoorDash Drive).
- **Ops board as HTMX vs rich UI**: today's pick is ops-board-shaped but does not specify the UI. The first v2-AI PR must decide whether to ship a minimal-HTML/HTMX ops board (LE31 v1-style) or a richer UI surface (separate v2-AI style).

## Why this matters

The *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* primitive is the **canonical v2-AI delivery-aggregator-MCP-bridge-vocabulary of the 80-pass brainstorm series**. The verbatim description + topics name the 6-tuple-primitive set explicitly. The vocabulary is the value, not the code (LE31 v2 has no delivery-aggregator surface today). When the first v2-AI PR that adds a delivery-aggregator-MCP-bridge surface lands, the dashpilot-mcp pattern is a ready-made *named primitive*. The prior `sanjibani/cleancloud-mcp` (2026-10-17 brainstorm Pick C) covered the *MCP-server-for-CleanCloud-POS-API-+-small-business* dimension; today's pick extends the *MCP-server-as-POS-/aggregator-bridge* cluster to the *delivery-aggregator* dimension. Sister-shape to features 263 + 286 + 288 + 306 + today's research PICK B + 2026-10-17 brainstorm Pick C.

The transferable items are:

1. The *MCP-server-for-delivery-aggregator-+-POS-bridge* primitive (the §3.4 *MCP-as-cross-system-tooling* invariant applied to delivery aggregators).
2. The *quote-dispatch-track* triple (the §3.1 *explicit-state-transitions* invariant applied to delivery aggregators).
3. The *ops-board* posture (the §3.1 *operator-orchestrates-the-aggregator* invariant applied to delivery-aggregator-ops).
4. The *daily-diagnostics-check-in* posture (the §3.3 *append-only-audit-* invariant applied to delivery-aggregator-audit).
5. The *DoorDash-Drive + restaurant + POS* posture (the §3.7 *minimal-PII-only-aggregator-API-bridge* invariant applied to delivery aggregators).
6. The *MCP + Model-Context-Protocol* posture (the §3.4 *MCP-as-cross-system-tooling* invariant applied to delivery aggregators).

The defer artifact is **fully reversible** (vocabulary-only). No code today.