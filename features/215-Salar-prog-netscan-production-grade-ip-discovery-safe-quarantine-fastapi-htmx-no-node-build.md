# Feature 215 — `Salar-prog-netscan-production-grade-ip-discovery-safe-quarantine-fastapi-htmx-no-node-build` (defer)

> **NEW observation (2026-09-22).** Documents in-window GitHub Search `htmx+no-build` query result: `Salar-prog/netscan` (**1★/0⑂**, **MIT ✓**, Python, **pushed 2026-09-01T16:42:48Z = 21 days ago** (in-window by `pushed_at`) + **created 2026-08-24T07:19:43Z = 29 days ago** (in-window by `created_at` — **BOTH fields in-window** = the *only of today's 3 picks that is a fresh discovery, not just an off-window creation re-activated by a today push*), **532 KB modest repo**, default_branch=`main`, archived=`False`, `updated_at=2026-08-28T04:03:46Z`). **9 topics** (parent-verified verbatim from raw JSON): `fastapi`, `htmx`, `ip-address-management`, `ipam`, `network-monitoring`, `network-scanner`, `nmap`, `self-hosted`, `subnet-scanner`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-22): *"Production-grade IP discovery and availability tracking — nmap multi-probe engine, safe quarantine model, FastAPI + HTMX dashboard, no Node build step"*. The **FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling** quintuple primitive — the *safe-quarantine-model* discipline is the *charter §3.1 explicit-state-transition discipline applied to the network-state dimension* (a network resource is either healthy+active or quarantined+inactive; no silent transition); the *FastAPI + HTMX + no-Node-build* posture matches LE31 v1's waiter web UI stack; the *self-hosted* topic matches LE31 v1's deployment posture (LE31 is self-hosted at the restaurant). Charter §3.1 alignment (the *safe-quarantine-model* discipline IS the *charter §3.1 explicit-state-transition discipline* applied to the network-state dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive); §3.4 not triggered (no AI surface; the *network-monitoring + safe-quarantine* pattern is *operator-tooling*, not customer-facing AI). Sister-shape to features 25 + 142 + 143 + 214 via the *FastAPI + HTMX + no-Node-build + operator-tooling posture* cluster.

## Goal

Retain the **FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling** cross-section architectural vocabulary + **the *safe-quarantine-model* discipline** + **the *FastAPI + HTMX + no-Node-build* posture** as the persistent v2 no-build reactive-web network-ops reference for any future LE31 v2 maintainer asking the *network-monitoring + safe-quarantine* question (does LE31 v2 ever need a network-monitoring surface? does LE31 v2 ever need a safe-quarantine-model? does LE31 v2 ever need a FastAPI + HTMX + no-Node-build dashboard?). The artifact is the persistent *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary as a *named* v2 no-build reactive-web network-ops reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `Salar-prog/netscan` cross-section vocabulary: the **only v2-network-ops candidate with both `pushed_at` AND `created_at` in-window today**; the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* quintuple primitive explicitly named in the description.
- A written record of the **safe-quarantine-model primitive**: the *safe-quarantine-model* discipline is the *charter §3.1 explicit-state-transition discipline applied to the network-state dimension* (a network resource is either healthy+active or quarantined+inactive; the resource cannot move between states silently; the move requires an explicit operator action).
- A written record of the **FastAPI + HTMX + no-Node-build posture**: matches LE31 v1's waiter web UI stack (FastAPI backend + HTMX frontend + no-Node-build step); the *no-Node-build* posture means no npm install, no webpack, no React/Vue/Svelte; the operator-dashboard is rendered with HTMX's server-side-rendering + minimal JavaScript.
- A written record of the **MIT permissive license as §3.2 STRICTLY-COMPATIBLE**: the codebase CAN be imported as a v2 dependency under MIT permissive licensing (no copyleft restrictions, no source-disclosure requirements).
- A written record of the **self-hosted deployment posture**: matches LE31 v1's deployment posture (LE31 is self-hosted at the restaurant, not cloud-hosted); the *self-hosted* topic explicitly names the *self-hosted-software* vocabulary.
- A decision record: today's verdict is `defer (parking-lot)` because the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary is a v2 no-build reactive-web network-ops reference, not a v1 or v2 build implication. v1 has no network-monitoring surface today; the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine* vocabulary documents the *future-extension* for the next v2 maintainer asking the *network-monitoring + safe-quarantine* question.

**Out of scope (defer artifact):**
- Any change to the LE31 v1 surface (no network-monitoring surface today, no safe-quarantine-model today, no nmap-multi-probe-engine today).
- Any change to the LE31 v1 cook Telegram bot (no network-state-detection today; the cook-bot is purely transactional).
- Any change to the LE31 v1 waiter web UI (no network-monitoring dashboard today; the waiter UI is for table-management + order-taking + bill-closing, not network-monitoring).
- Adoption of the `Salar-prog/netscan` code as a v2 dependency (the repo is 1★/0⑂ at 532 KB with MIT permissive license; the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine* vocabulary would need to be independently re-implemented and validated against the LE31 v1's no-network-monitoring posture, not simply imported; vocabulary-only artifact today).
- Any change to the `audit_logs` table or `StockEntry` ledger today.
- Any new dependency on the `Salar-prog` maintainer.

## Evidence / JTBD

When a future LE31 v2 maintainer asks *"if v2 introduces a network-monitoring surface, a safe-quarantine-model surface, or a FastAPI + HTMX + no-Node-build dashboard for any operator-tooling surface, what is the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary that preserves the existing v1 no-network-monitoring + no-safe-quarantine posture?"*, the maintainer wants *evidence that another independent 2026 Python repo at 532 KB with 1★/0⑂ + MIT permissive license + 9 topics + both `pushed_at` AND `created_at` in-window is shipping the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* primitive as the v2 no-build reactive-web network-ops discipline*, but struggles because *v1 has no documented network-monitoring primitive in the charter*, so that *v2 can introduce the network-monitoring + safe-quarantine-model vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*.

- **Evidence class**: observed (the `Salar-prog/netscan` description explicitly names *"Production-grade IP discovery and availability tracking — nmap multi-probe engine, safe quarantine model, FastAPI + HTMX dashboard, no Node build step"* = the FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling sextuple primitive).
- **Confidence**: medium for the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary (1★/0⑂ + MIT permissive license + 9 topics + both fields in-window + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *safe-quarantine-model* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the network-state dimension*).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine documentation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine documentation**: when (if) LE31 v2 introduces a network-monitoring surface, a safe-quarantine-model surface, or a FastAPI + HTMX + no-Node-build dashboard for any operator-tooling surface, the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary is documented.

## Description

GitHub `Salar-prog/netscan` (1★/0⑂, MIT ✓, Python, pushed 2026-09-01T16:42:48Z + created 2026-08-24T07:19:43Z = both fields in-window, 532 KB modest repo).

Description (verbatim): *"Production-grade IP discovery and availability tracking — nmap multi-probe engine, safe quarantine model, FastAPI + HTMX dashboard, no Node build step"*.

Topics: `fastapi`, `htmx`, `ip-address-management`, `ipam`, `network-monitoring`, `network-scanner`, `nmap`, `self-hosted`, `subnet-scanner`.

The **6 named v2-network-ops primitives**:

| `Salar-prog/netscan` primitive | LE31 v1 primitive | Match status |
|---|---|---|
| `Production-grade` (production-grade posture) | (LE31 v1 is production-grade; the *production-grade* qualifier matches LE31 v1's posture) | **★ MATCH** |
| `IP discovery and availability tracking` (network-state-detection) | (LE31 v1 has no IP-discovery surface today) | **★ GAP: LE31 v1 has no IP-discovery surface today** |
| `nmap multi-probe engine` (nmap-multi-probe-engine) | (LE31 v1 has no nmap-multi-probe-engine today) | **★ GAP: LE31 v1 has no nmap-multi-probe-engine today** |
| `safe quarantine model` (safe-quarantine-model) | (LE31 v1 has no safe-quarantine-model today) | **★ GAP: LE31 v1 has no safe-quarantine-model today** |
| `FastAPI + HTMX dashboard` (operator-dashboard) | (LE31 v1 waiter web UI = FastAPI + HTMX + no-Node-build = **stack-matched**) | **★ STACK-MATCHED** |
| `no Node build step` (no-Node-build posture) | (LE31 v1 = FastAPI + HTMX + no-Node-build = **stack-matched**) | **★ STACK-MATCHED** |

The **safe-quarantine-model primitive**: the *safe-quarantine-model* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the network-state dimension* — when a network resource is detected as unhealthy by the nmap-multi-probe-engine, the *safe-quarantine-model* moves it to a quarantine state; the *quarantine* state means the resource is excluded from the production routing; the *quarantine* discipline requires explicit operator action to transition (the operator confirms the quarantine; the resource cannot move to quarantine silently; the resource cannot move back to *healthy+active* without an explicit operator action).

The **FastAPI + HTMX + no-Node-build posture**: the *FastAPI* topic matches LE31 v1's primary backend framework; the *HTMX* topic matches LE31 v1's primary no-build reactive-frontend library; the *no-Node-build* posture matches LE31 v1's no-npm-install + no-webpack + no-React/Vue/Svelte posture; the operator-dashboard is rendered with HTMX's server-side-rendering + minimal JavaScript.

The **MIT permissive license**: MIT = permissive license compatible with the LE31 charter §3.2 stack-invariant posture; the codebase CAN be imported as a v2 dependency under MIT permissive licensing (no copyleft restrictions, no source-disclosure requirements).

The **self-hosted deployment posture**: the *self-hosted* topic matches LE31 v1's deployment posture (LE31 is self-hosted at the restaurant, not cloud-hosted); the *self-hosted-software* vocabulary is the future-extension for any v2 surface that needs to be deployed at the restaurant without a cloud dependency.

## Data model

**No LE31 data model change today.** The defer artifact is documentation only. The *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* primitive names the *network-monitoring + safe-quarantine-model + FastAPI + HTMX + no-Node-build dashboard* extensions that any future v2 schema change should consider; v2 maintainer decision required before adopting the network-monitoring surface (LE31 v1 currently operates no network-monitoring surface; network-monitoring is a v2 architecture-decision, not a v1 implementation task today).

## Implementation steps

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a network-monitoring surface to the LE31 v2 operator surface, a safe-quarantine-model surface, or a FastAPI + HTMX + no-Node-build dashboard for any operator-tooling surface):

- `app/netmonitor/` — possibly add (the network-monitoring module; depends on the v2 change).
- `app/netmonitor/quarantine.py` — possibly add (the safe-quarantine-model primitive that moves network resources between healthy+active and quarantined+inactive states; depends on the v2 change).
- `app/netmonitor/nmap_probe.py` — possibly add (the nmap-multi-probe-engine wrapper; depends on the v2 change).
- `app/dashboards/network_dashboard.py` — possibly add (the FastAPI + HTMX + no-Node-build dashboard for the network-monitoring surface; depends on the v2 change).
- `tests/test_netmonitor_quarantine.py` + `tests/test_nmap_probe.py` + `tests/test_network_dashboard.py` — possibly add (the integration tests for the network-monitoring + safe-quarantine-model + nmap-multi-probe-engine + FastAPI + HTMX + no-Node-build dashboard surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no network-monitoring surface added.

## Telegram interaction if any

None today. If a future v2 trigger fires (network-monitoring surface), the Telegram interaction could be extended with netmonitor-notifications: the cook/owner gets a Telegram notification when a network resource moves to *quarantined+inactive* state; the cook/owner confirms the quarantine via the cook-bot; the safe-quarantine-model discipline ensures the resource is excluded from production routing until the cook/owner confirms the move back to *healthy+active*. The *safe-quarantine-model* discipline ensures the cook/owner is notified of every state transition (no silent transition; the cook/owner must confirm every move).

## Dependencies

No new dependencies today. If the future v2 trigger fires, the dependencies would be:
- `nmap` (the network-mapper binary; not in `requirements.txt` today).
- `python-nmap` (the Python wrapper for nmap; not in `requirements.txt` today).
- `aio-pika` (the async Python AMQP client; not in `requirements.txt` today).

LE31 v1 currently operates no network-monitoring surface; the dependencies above would need to be added to `requirements.txt` only when the v2 surface is triggered.

## Open questions

1. **Does LE31 v2 ever need a network-monitoring surface?** The cross-section value is the *safe-quarantine-model + FastAPI + HTMX + no-Node-build + nmap-multi-probe-engine + operator-tooling* vocabulary; v2 maintainer decision required before adopting the network-monitoring surface.
2. **Does LE31 v2 ever need a safe-quarantine-model?** The *safe-quarantine-model* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the network-state dimension*; v2 maintainer decision required before adopting the safe-quarantine-model surface.
3. **Does LE31 v2 ever need a FastAPI + HTMX + no-Node-build dashboard for any operator-tooling surface?** LE31 v1's waiter web UI is already FastAPI + HTMX + no-Node-build; the *FastAPI + HTMX + no-Node-build + operator-tooling* posture is already in use; v2 maintainer decision required before adopting the *FastAPI + HTMX + no-Node-build dashboard* surface for network-monitoring.
4. **What triggers the v2 network-monitoring surface?** The trigger condition is the first v2 PR that adds a network-monitoring surface to the LE31 v2 operator surface, a safe-quarantine-model surface, or a FastAPI + HTMX + no-Node-build dashboard for any operator-tooling surface.

## Why this matters

The **FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling** primitive is the most direct documented reference for any future LE31 v2 surface that asks the *network-monitoring + safe-quarantine* question. Without this artifact, the next v2 maintainer would need to independently discover the *safe-quarantine-model* discipline from scratch; with this artifact, the next v2 maintainer has a *named* reference that documents the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary as the v2 no-build reactive-web network-ops reference.

The cross-section value is the *safe-quarantine-model* discipline as the *charter §3.1 explicit-state-transition discipline applied to the network-state dimension* — when (if) LE31 v2 introduces a network-monitoring surface, the *safe-quarantine-model* discipline ensures the resource is either healthy+active or quarantined+inactive, never silently transitioned; the *charter §3.1 explicit-state-transition discipline* is preserved at the network-state dimension.

The MIT permissive license is §3.2 STRICTLY-COMPATIBLE — the codebase CAN be imported as a v2 dependency under MIT permissive licensing (no copyleft restrictions, no source-disclosure requirements); this gives LE31 v2 maintainers the option to *import* the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* primitives rather than re-implementing them.