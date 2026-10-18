# Feature 343 — `warpusTOM-StockWise-Group6-BT-204-mit-offline-inventory-and-pos-system-oop-python-sqlite-customtkinter-gui-v1-offline-first-inventory-and-pos-vocabulary` (defer)

> **NEW observation (2026-10-18).** Documents in-window GitHub repo `warpusTOM/StockWise_Group6_BT-204` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, **Python ✓ ON-STACK** + SQLite + CustomTkinter + inventory-management + POS, **pushed 2026-09-27T06:31:50Z AND created 2026-09-27T05:54:34Z = IN-WINDOW BY BOTH FIELDS** (~21-day-old repo with in-window `pushed_at` and `created_at`; both fields in window), **26312 KB substantial = THE LARGEST in-window brainstorm-vocabulary pick of the 80-pass series** (vs today's Pick A `dashpilot-labs/dashpilot-mcp` 252 KB = 104x larger; vs 2026-10-17 Pick A `tangwenhai839-create/qingyu` 1446 KB = 18x larger; vs 2026-10-17 Pick C `sanjibani/cleancloud-mcp` 40 KB = 658x larger), default_branch=`main`, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-18): *"Offline Inventory & POS System — OOP Python, SQLite, CustomTkinter GUI"*. Topics (verbatim, parent-verified, **5 topics**): `customtkinter, inventory-management, pos, python, sqlite`. Bucket: **v1 (offline-first-inventory-and-POS-vocabulary)** — Pick C of Daily Brainstorm 2026-10-18. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **offline-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI + inventory-management + POS** vocabulary as a persistent cross-section reference for the LE31 v1 *offline-first-inventory-and-POS* wedge, and document the **offline-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI** primitive that an independent maintainer shipped in 2026 (~21-day-old repo with in-window `created_at` AND `pushed_at`) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 *offline-first-inventory-and-POS* gap-area. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **offline-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI + inventory-management + POS** 6-tuple-primitive: an offline-first inventory and POS system built as OOP Python with SQLite for local persistence and CustomTkinter for the desktop GUI; the system runs without internet; the inventory ledger is local; the POS sales are recorded locally; the system syncs to a central server when the network is available. This is the §3.1 *offline-first + explicit-state-transitions* + §3.7 *local-PII-minimal-bridge* invariant applied to the *offline-first-inventory-and-POS* dimension.
- A written record of the **MIT + 0★/0⑨ + 26312 KB substantial = THE LARGEST + 5-topic array + Python ✓ ON-STACK + SQLite + CustomTkinter + inventory-management + POS** stack-shape: this is the **largest in-window brainstorm-vocabulary pick of the 80-pass series**; the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* discipline IS the canonical §3.1 *offline-first + explicit-state-transitions* + §3.7 *local-PII-minimal-bridge* invariant applied to the *offline-first-inventory-and-POS* dimension.
- A written record of the **operator-facing vocabulary** discipline: the operator does not need internet for the smallest-pos-workflow; the operator interacts with the CustomTkinter desktop GUI; the inventory ledger is local SQLite; the POS sales are recorded locally; the system syncs to a central server when the network is available. Sister-shape to today's research PICK B `FlashyLabs/flashy-ledger` (TypeScript AAO-stack-ledger-rules) + 2026-10-17 brainstorm Pick B `ALPHAMAN-0/burgerCodeEmployes` (FastAPI+SQLite+Pydantic+restaurant+employee-management+shift-scheduling+tips) + features 03 (`kitchen-stock-tracker`) + 67 (`offline-attestation-record-sovereign-offline-audit`) + 151 (`offline-attestation-record-sovereign-offline-audit`) + 314 (`Samarty-1/payout-recon`) + `LelecHub/pdv-superlelecmarket` (Flet+PostgreSQL+offline-first SQLite PDV for supermarket in Portuguese) — the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* posture IS the canonical v1 *offline-first-inventory-and-POS-vocabulary* applied to the *LE31-v1-offline-first-inventory-and-POS* dimension.
- A decision record: today's verdict is `defer` because (1) the v1 charter has *no offline-first-inventory-and-POS surface* (LE31 v1 has feature 03 `kitchen-stock-tracker` but it is feature-class-b as a v1 polish gap-area, not a full offline-first-POS); (2) the stack-shape match is the value, not the code (LE31 v1 uses Python + FastAPI + Postgres + aiogram v3 + minimal-HTML/HTMX, not OOP-Python + SQLite + CustomTkinter); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the StockWise codebase (MIT + 0★/0⑨ + 21-day-old repo; same-instant push).
- Cross-pollination with the v1 charter §3.1 *offline-first + explicit-state-transitions* posture (the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* discipline IS the §3.1 invariant; the *offline-first-POS + SQLite + CustomTkinter* posture IS OFF-§3.5 — LE31 v1 is online + Postgres + minimal-HTML/HTMX, not offline-first + SQLite + CustomTkinter).
- Any vendor-relationship with CustomTkinter / SQLite (LE31 v1 has no offline-first-inventory-and-POS surface today; v1 is online + Postgres + minimal-HTML/HTMX).
- Cross-section candidate for v1 if LE31 ever adds an offline-first surface (charter §3.5 review required: the *offline-first + SQLite + CustomTkinter* posture requires explicit offline-first-scope and explicit SQLite-vs-Postgres trade-off before any v1 PR).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v1 surface proposes "an offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI primitive" (e.g., a v1 surface that adds an offline-first-inventory-and-POS to the existing feature 03 `kitchen-stock-tracker`; the offline-first-POS works without internet; the inventory ledger is local SQLite; the POS sales are recorded locally; the system syncs to a central server when the network is available), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI" is a real demand signal*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI posture"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `customtkinter, inventory-management, pos, python, sqlite` + *"Offline Inventory & POS System — OOP Python, SQLite, CustomTkinter GUI"*).
- **Confidence**: medium-high for the vocabulary match (the verbatim description + topics name the 6-tuple-primitive set + the offline-first-inventory-+-POS-system posture + the OOP-Python posture + the SQLite posture + the CustomTkinter-GUI posture); low for transferability (LE31 v1 has feature 03 `kitchen-stock-tracker` but it is feature-class-b as a v1 polish gap-area; an offline-first-POS is OFF-§3.5 unless explicit charter-decision is made).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has feature 03 `kitchen-stock-tracker` as a v1 polish gap-area, but no offline-first-inventory-and-POS surface); the value is the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* vocabulary — when the first v1 PR that adopts an offline-first surface lands, the StockWise pattern is a ready-made *named primitive*.

## Description

GitHub `warpusTOM/StockWise_Group6_BT-204` (MIT, 0★/0⑨, Python, pushed 2026-09-27T06:31:50Z, created 2026-09-27T05:54:34Z, 26312 KB substantial = THE LARGEST in-window brainstorm-vocabulary pick of the 80-pass series, default_branch=`main`, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-18): *"Offline Inventory & POS System — OOP Python, SQLite, CustomTkinter GUI"*.

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **Offline-inventory-+-POS-system** — the system runs without internet; the inventory ledger is local; the POS sales are recorded locally. The *offline-first-inventory-+-POS-system* primitive maps 1:1 onto any future v1 surface that needs an offline-first-inventory-and-POS for the LE31 feature 03 `kitchen-stock-tracker`.
2. **OOP-Python** — the system is built as OOP Python (classes for `Product`, `InventoryItem`, `Sale`, `Customer`, etc.). The *OOP-Python* posture IS the §3.1 *explicit-state-transitions* charter invariant applied to the *inventory-+-POS* dimension.
3. **SQLite** — the local persistence layer. The *SQLite* posture IS the §3.5 *offline-first-SQLite* charter invariant (LE31 v1 is online + Postgres; SQLite is OFF-§3.5 unless explicit charter-decision is made).
4. **CustomTkinter-GUI** — the desktop GUI. The *CustomTkinter-GUI* posture IS OFF-§3.1 — LE31 v1 is minimal-HTML/HTMX + Telegram-bot, not desktop-CustomTkinter-GUI; explicit charter-decision needed for any v1 PR that adopts this discipline.
5. **Inventory-management + POS** — the two domains. The *inventory-management + POS* posture IS the §3.1 *explicit-state-transitions* charter invariant applied to the *inventory-+-POS* dimension.
6. **Sync-to-central-server-when-network-available** — the offline-first-sync discipline. The *sync-to-central-server-when-network-available* posture IS the §3.5 *offline-first-sync* charter invariant (LE31 v1 is online; sync-to-central-server is OFF-§3.5 unless explicit charter-decision is made).

The defer artifact retains the **6-tuple-primitive** (offline-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI + inventory-management + POS) as a persistent cross-section reference.

## Data model

None today. The defer artifact is documentation only.

When the first v1 PR that adopts the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* discipline lands, the data model is:

```sql
-- hypothetical future v1 surface (NOT IMPLEMENTED TODAY)
-- Local SQLite (offline-first; syncs to central Postgres when network is available)

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    category TEXT,
    price_eur NUMERIC(10, 2) NOT NULL,
    prep_station TEXT,
    active INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE inventory_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL REFERENCES product(id),
    quantity NUMERIC(10, 3) NOT NULL DEFAULT 0,
    reorder_threshold NUMERIC(10, 3),
    last_counted_at TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE sale (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pos_terminal_id TEXT NOT NULL,
    total_eur NUMERIC(10, 2) NOT NULL,
    payment_method TEXT NOT NULL,         -- 'cash' | 'card' | 'mobile' | ...
    status TEXT NOT NULL DEFAULT 'pending',  -- 'pending' | 'completed' | 'voided' | 'synced'
    synced_at TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- append-only inventory event log (the §3.3 append-only-ledger invariant)
CREATE TABLE inventory_event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL REFERENCES product(id),
    event_type TEXT NOT NULL,             -- 'restock' | 'sale' | 'waste' | 'adjustment' | 'count' | ...
    delta_quantity NUMERIC(10, 3) NOT NULL,
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
```

## Implementation steps

None today. The defer artifact is documentation only.

When the first v1 PR that adopts the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* discipline lands, the implementation steps are:

1. Add Alembic migration for `Product`, `InventoryItem`, `Sale`, `InventoryEvent` tables in the central Postgres (the local SQLite is the offline-first layer; the central Postgres is the source-of-truth).
2. Add `backend/services/offline_first_sync.py` with `OfflineFirstSync` class (syncs local SQLite to central Postgres when network is available).
3. Add `backend/services/inventory_management.py` with `InventoryManagement` class (OOP Python; wraps the `InventoryItem` + `InventoryEvent` tables).
4. Wire the new service into the existing feature 03 `kitchen-stock-tracker` surface.
5. Add `frontend/templates/inventory-dashboard.html` minimal-HTML/HTMX template for the inventory dashboard (if §3.5 *online-first-HTML* posture is kept) OR add `desktop/inventory_app.py` CustomTkinter GUI (if §3.5 *offline-first-CustomTkinter* posture is adopted).
6. Add `tests/test_offline_first_sync.py` + `tests/test_inventory_management.py`.

## Telegram interaction if any

The owner Telegram bot's daily-recap surface consumes the local-Sale-count as the daily-sales-summary (synced from local SQLite to central Postgres). The cook Telegram bot's existing notification surface is fed by the local-InventoryEvent (when a `sale` event is recorded locally, the cook bot is notified of the depleted inventory). No new Telegram-bot surface today.

## Dependencies

When the first v1 PR that adopts the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* discipline lands, the dependencies are:

- `sqlite3` (stdlib; offline-first SQLite)
- `customtkinter` (desktop GUI; OFF-§3.1 unless explicit charter-decision is made)
- Existing LE31 v1 stack: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX

## Open questions

- **§3.5 offline-first-vs-online-first review**: LE31 v1 is online + Postgres + minimal-HTML/HTMX. The *offline-first + SQLite + CustomTkinter* posture is OFF-§3.5 unless explicit charter-decision is made.
- **§3.5 SQLite-vs-Postgres review**: LE31 v1 is Postgres-only. The *SQLite* posture is OFF-§3.5 unless explicit charter-decision is made. The *sync-to-central-Postgres* discipline is the standard way to reconcile offline-first-SQLite with online-first-Postgres.
- **CustomTkinter vs minimal-HTML/HTMX**: today's pick is CustomTkinter-specific. The transferable discipline is the *offline-first-inventory-+-POS-system* posture, not the CustomTkinter GUI. The first v1 PR must decide whether to ship a CustomTkinter desktop GUI (charter §3.5 review) or a minimal-HTML/HTMX web GUI (charter §3.1 aligned).
- **Single-shop vs multi-shop**: today's pick is single-shop-specific. The transferable discipline is the *offline-first-inventory-+-POS-system* posture, not the single-shop discipline. The first v1 PR must decide whether to ship single-shop (LE31 v1 charter) or multi-shop (charter-decision needed).

## Why this matters

The *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* primitive is the **canonical v1 offline-first-inventory-and-POS-vocabulary of the 80-pass brainstorm series**. The verbatim description + topics name the 6-tuple-primitive set explicitly. The vocabulary is the value, not the code (LE31 v1 has feature 03 `kitchen-stock-tracker` as a v1 polish gap-area but no offline-first-inventory-and-POS surface). When the first v1 PR that adopts an offline-first surface lands, the StockWise pattern is a ready-made *named primitive*. Sister-shape to features 03 (`kitchen-stock-tracker`) + 67 (`offline-attestation-record-sovereign-offline-audit`) + 151 (`offline-attestation-record-sovereign-offline-audit`) + 314 (`Samarty-1/payout-recon`) + `LelecHub/pdv-superlelecmarket` (carry-over from 2026-10-16 + 2026-10-17) + 2026-10-17 brainstorm Pick B `ALPHAMAN-0/burgerCodeEmployes`.

The transferable items are:

1. The *offline-first-inventory-+-POS-system* primitive (the §3.1 *offline-first + explicit-state-transitions* invariant applied to inventory-+-POS).
2. The *OOP-Python* posture (the §3.1 *explicit-state-transitions* invariant applied to inventory-+-POS).
3. The *SQLite* posture (the §3.5 *offline-first-SQLite* invariant; charter-decision needed for v1).
4. The *CustomTkinter-GUI* posture (OFF-§3.1; charter-decision needed).
5. The *inventory-management + POS* posture (the §3.1 *explicit-state-transitions* invariant applied to inventory-+-POS).
6. The *sync-to-central-server-when-network-available* posture (the §3.5 *offline-first-sync* invariant; charter-decision needed for v1).

The defer artifact is **fully reversible** (vocabulary-only). No code today.