# Feature 200 — `jerthermit-stockpile-hermitedge-location-aware-inventory-fastapi-nextjs-postgresql-barcode-warehouse` (defer)

> **NEW observation (2026-09-19).** Documents in-window GitHub repo `jerthermit/stockpile-hermitedge` (**license=null** (`spdx_id: null` in raw JSON), **0★/0⑂**, Python, **pushed 2026-09-04T13:49:58Z** (15-day-old push, in-window by `pushed_at` only — the most recent push is the 4-day-old newest find of the 51-pass series that *intentionally* shows up here), **created 2026-08-30T21:23:46Z** (20-day-old repo with in-window `created_at` — *both* fields in-window), **9792 KB substantial repo**, default_branch=`main`). Topics (verbatim from raw JSON): `barcode-scanner, fastapi, inventory-control, inventory-management-system, nextjs, postgresql, small-business, together-ai, typescript, warehouse-management`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-19): *"Location-aware AI inventory system customized around how businesses receive, store, move, sell, and check stock."* The **stock-ledger-as-physical-place primitive** + the **5-verbs vocabulary** (receive + store + move + sell + check = the verbs of the StockEntry ledger mapped onto the physical kitchen floor): LE31's `StockEntry` SQLModel table tracks *what was added* + *what was used* + *what remains*, but does not track *where it physically is*; the topic triple `barcode-scanner + inventory-control + warehouse-management` is the **physical-floor vocabulary** that LE31 v1 has never had a direct reference for. The **fastapi + postgresql + nextjs** topic triple is the **LE31 v1 backend+frontend stack mirror**. The **null license** blocks §3.2 code adoption (LE31 would have to re-implement the primitive against its own FastAPI + SQLModel + aiogram v3 stack, not import the TypeScript + Next.js frontend or the `together-ai` integration), but the **vocabulary** is the brainstorm value. The `together-ai` topic names a *staff-facing AI-assist surface* (the AI helps with inventory decisions, not customer-facing AI) — explicitly **charter §3.4-compatible**. Bucket: **v1 architecture-reference (stock-ledger-as-physical-place primitive, parking-lot defer)** — vocabulary + 5-verbs vocabulary + barcode-scanner + warehouse-management primitive documentation, zero build time today.

## Goal

Retain the **"Location-aware AI inventory system customized around how businesses receive, store, move, sell, and check stock"** cross-section architectural vocabulary + **stock-ledger-as-physical-place primitive** + **5-verbs vocabulary** (receive + store + move + sell + check) as the persistent v1 architecture reference for any future LE31 v1 maintainer asking the *stock-entry-physical-location* question (does LE31 v1 ever need to track *where a stock item physically is* on the kitchen floor, with a barcode-scanner-equipped staff device?). The artifact is the persistent *physical-floor inventory-management primitive* as a *named* v1 architectural reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `stockpile-hermitedge` cross-section vocabulary: the **first in-window 2026 Python inventory-management repo of the 51-pass series** with the *physical-floor-verbs (receive + store + move + check)* vocabulary; the `barcode-scanner + inventory-control + warehouse-management` topic triple; the 5-verbs vocabulary mapped onto the StockEntry ledger + Bill consumption primitives.
- A written record of the **stock-ledger-as-physical-place primitive**: the *stock-entry-physical-location* vocabulary — the discipline of tracking *where a stock item physically is* on the kitchen floor (vs LE31 v1's *digital-only* tracking which tracks *what was added* + *what was used* + *what remains* but not *where*).
- A written record of the **5-verbs vocabulary**: `receive` + `store` + `move` + `sell` + `check` = the verbs of the StockEntry ledger mapped onto the physical kitchen floor; the verb *receive* maps onto the StockEntry `added_at` field; the verb *store* maps onto a hypothetical `storage_location_id` field; the verb *move* maps onto a hypothetical `transferred_at` + `from_location_id` + `to_location_id` chained audit trail; the verb *sell* maps onto the Bill SQLModel consumption + StockEntry consumption; the verb *check* maps onto a hypothetical `counted_at` + `counted_by_actor` + `physical_count` discrepancy check.
- A written record of the **LE31-stack-mirror vocabulary**: the topics `fastapi + postgresql + nextjs` mirror the LE31 v1 backend (FastAPI 0.141.1) + database (PostgreSQL via SQLModel 0.0.42) + frontend (HTMX server-side-rendering on FastAPI); the TypeScript + Next.js stack IS NOT on-pattern for LE31 v1 (LE31 v1 uses HTMX not Next.js), but the *FastAPI + PostgreSQL* backend primitive IS on-pattern.
- A written record of the **null license as a documented vocabulary-only artifact**: the codebase cannot be adopted as a library (null license = §3.2 blocker for *import-and-extend*); the *5-verbs + stock-ledger-as-physical-place + barcode-scanner + warehouse-management* vocabulary is the value, not the code; LE31 would re-implement the primitive against its own FastAPI + SQLModel + aiogram v3 stack, not import the TypeScript + Next.js frontend or the `together-ai` integration.
- A decision record: today's verdict is `defer (parking-lot)` because the *5-verbs + stock-ledger-as-physical-place + barcode-scanner + warehouse-management* vocabulary is a v1 architecture reference, not a v1 build implication. v1 covers *what was added* + *what was used* + *what remains* today; the physical-floor vocabulary documents the *where is it physically* + *barcode-scanner + warehouse-management* extensions for the next v1 maintainer.

**Out of scope (defer artifact):**
- Any change to the LE31 v1 schema (no `storage_location_id` field on StockEntry today, no barcode-scanner integration today, no warehouse-management surface today).
- Any change to the waiter web UI (HTMX) or cook Telegram bot.
- Adoption of the `stockpile-hermitedge` code as a v1 dependency (the repo is 0★/0⑂ at 9792 KB; the *5-verbs + stock-ledger-as-physical-place* vocabulary would need to be independently re-implemented and validated against the LE31 append-only StockEntry ledger + audit_logs, not simply imported; the null license is a §3.2 blocker for *import-and-extend*; the TypeScript + Next.js frontend is off-pattern for LE31 v1's HTMX-server-side-rendering posture). The cross-section is *primitive vocabulary extension + stock-ledger-as-physical-place documentation*, not *library adoption*.
- Any change to the `audit_logs` table or `StockEntry` ledger today.
- Any new dependency on the `jerthermit` maintainer.

## Evidence / JTBD

When a future LE31 v1 maintainer asks *"if v1 introduces a barcode-scanner-equipped staff device, a physical-floor stock-location SQLModel field, or a warehouse-management surface, what is the stock-ledger-as-physical-place primitive that preserves the existing v1 StockEntry + audit_logs + cook-bot invariants?"*, the maintainer wants *evidence that another independent 2026 Python repo at 9792 KB with null license + both fields in-window + restaurant-inventory + barcode-scanner + warehouse-management topics is shipping the 5-verbs vocabulary (receive + store + move + sell + check) as the physical-floor inventory discipline*, but struggles because *v1 has no documented stock-ledger-as-physical-place primitive in the charter*, so that *v1 can introduce the physical-floor inventory vocabulary with the explicit 5-verbs rather than inventing a new one*.

- **Evidence class**: observed (the `stockpile-hermitedge` description explicitly names *"receive, store, move, sell, and check stock"* = the 5-verbs vocabulary that maps onto LE31's existing StockEntry + Bill consumption primitives + 3 hypothetical storage-location primitives; the topics `barcode-scanner + inventory-control + warehouse-management` are the *physical-floor* vocabulary).
- **Confidence**: medium-high for the 5-verbs + stock-ledger-as-physical-place vocabulary (null + Python + 9792 KB substantial + both fields in-window + explicit 5-verbs description + staff-facing AI topic = §3.4-compatible); low for *adoption* (LE31 should re-implement the physical-floor primitive against its own StockEntry + audit_logs + aiogram v3 stack, not import the TypeScript + Next.js frontend or the `together-ai` integration; the null license is a §3.2 blocker; the React/Next.js frontend is off-pattern).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + stock-ledger-as-physical-place documentation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + stock-ledger-as-physical-place documentation**: when (if) LE31 v1 introduces a barcode-scanner-equipped staff device, a physical-floor stock-location SQLModel field, or a warehouse-management surface, the *5-verbs + stock-ledger-as-physical-place + barcode-scanner + warehouse-management* vocabulary is documented.

## Description

GitHub `jerthermit/stockpile-hermitedge` (license=null, 0★/0⑂, Python, pushed 2026-09-04T13:49:58Z, created 2026-08-30T21:23:46Z = *both fields in-window*, 9792 KB substantial repo).

Description (verbatim): *"Location-aware AI inventory system customized around how businesses receive, store, move, sell, and check stock."*

Topics (verbatim from raw JSON): `barcode-scanner, fastapi, inventory-control, inventory-management-system, nextjs, postgresql, small-business, together-ai, typescript, warehouse-management`.

The **5 named physical-floor verbs**:

| `stockpile-hermitedge` verb | LE31 v1 primitive | Match status |
|---|---|---|
| `receive` | `StockEntry.entry_type='receive'` + `audit_logs.recorded_at` (when a stock item physically arrives at the kitchen) | ✓ direct match |
| `store` | (LE31 v1 has no `storage_location_id` field on StockEntry; physical-storage-location is implicit) | **★ GAP: LE31 v1 has no storage-location primitive** |
| `move` | (LE31 v1 has no `transferred_at` + `from_location_id` + `to_location_id` chained audit trail; physical-movement is implicit) | **★ GAP: LE31 v1 has no storage-location-transfer primitive** |
| `sell` | `Bill` SQLModel table + `StockEntry.entry_type='consumption'` (when a stock item is sold to a guest via a bill) | ✓ direct match |
| `check` | (LE31 v1 has no `counted_at` + `counted_by_actor` + `physical_count` discrepancy check; physical-counts are implicit) | **★ GAP: LE31 v1 has no physical-count-check primitive** |

The **stock-ledger-as-physical-place primitive**: a *physical-place* in the kitchen context is a *shelf* or a *crate* or a *fridge* — a container in which a stock item physically exists. LE31 v1's StockEntry schema is `id, item_name, quantity, unit, entry_type, recorded_at, actor_user_id` (the LE31 charter §3.1 schema); the `stockpile-hermitedge` primitive adds `storage_location_id` (FK to `StorageLocation` SQLModel table) + `transferred_at` (timestamp of last physical-movement) + `from_location_id` + `to_location_id` (chained audit trail of physical-movement) + `counted_at` + `counted_by_actor` + `physical_count` (discrepancy-check audit trail).

The **barcode-scanner primitive**: a *barcode-scanner* is a hardware device (a PDA, a tablet, or a hand-held scanner with a USB or Bluetooth barcode-reader interface) that scans a *barcode* (a 1D or 2D machine-readable label affixed to a physical item) and emits a string (the barcode's value). The barcode-value is then mapped onto a database row (typically the `stock_items` table or `menu_items` table). The barcode-scanner primitive is *hardware-mediated* — the staff device emits a string, the backend matches it to a row, and the row's `quantity` field is updated. LE31 v1's cook Telegram bot could in principle be barcode-scanner-equipped (a future v1 PR would replace the cook's *typed-message* with a *scanned-barcode* on a tablet device).

The **warehouse-management primitive**: a *warehouse* in this context is any physical-storage surface — a shelf, a crate, a fridge, a freezer. The *warehouse-management* discipline is the *physical-storage-surface* vocabulary that tracks *which stock items are in which physical surface*. LE31 v1 has no warehouse-management surface today; the kitchen-floor-stock vocabulary is implicit (the cook *knows* where things are physically but the system doesn't track it).

The **null license as a documented vocabulary-only artifact**: the codebase cannot be adopted as a library (null license = §3.2 blocker for *import-and-extend*); the *5-verbs + stock-ledger-as-physical-place + barcode-scanner + warehouse-management* vocabulary is the value, not the code; LE31 would re-implement the primitive against its own FastAPI + SQLModel + aiogram v3 stack, not import the TypeScript + Next.js frontend or the `together-ai` integration. The `together-ai` topic is the **AI surface** — the description's *AI inventory system* framing names a *staff-facing AI-assist surface* (the AI helps with inventory decisions, not customer-facing AI) — explicitly **charter §3.4-compatible** (operator-tooling not customer-facing AI; the AI surface is *suggestions to staff*, not decisions for guests).

## Data model

**No LE31 data model change today.** The defer artifact is documentation only. The stock-ledger-as-physical-place primitive names the *storage_location_id + transferred_at + from_location_id + to_location_id + counted_at + counted_by_actor + physical_count* fields that any future v1 schema change should consider; v1 maintainer decision required before adopting the warehouse-management surface (LE31 v1 currently operates a digital-only stock ledger; warehouse-management is a v1 architecture-decision, not a v1 implementation task).

## Implementation steps

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a barcode-scanner integration, a physical-floor stock-location SQLModel field, or a warehouse-management surface):

- `app/models/storage_location.py` — possibly add (the SQLModel table for the physical storage location surface; depends on the v1 change).
- `app/models/stock_entry.py` — possibly add `storage_location_id` FK + `transferred_at` + `from_location_id` + `to_location_id` + `counted_at` + `counted_by_actor` + `physical_count` fields (the 5-verbs vocabulary extensions; depends on the v1 change).
- `app/api/barcode_scan.py` — possibly add (the FastAPI route that handles barcode-scanner input from a staff device; depends on the v1 change).
- `app/bot/cook.py` — possibly modify to add the *barcode-scanner-equipped cook flow* (the cook-bot surface when input comes from a scanned barcode, not a typed message; depends on the v1 change).
- `tests/test_warehouse_management.py` — possibly add (the integration test for the warehouse-management surface; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Telegram interaction if any

None today. If a future v1 trigger fires (barcode-scanner-equipped cook bot), the Telegram interaction would be replaced by a barcode-scan emit (the cook scans a barcode, the backend matches it to a row, the row's `quantity` field is updated via the same `audit_logs` chain as today). The cook-bot surface might persist for non-barcode interactions (typed text input), but the *primary* cook-bot entry-point would shift to barcode-scan.

## Dependencies

- No new dependency today.
- If a future v1 trigger fires:
  - Hardware: a barcode-scanner-equipped staff device (tablet or PDA with a USB or Bluetooth barcode-reader interface).
  - Software: a barcode-reading library (e.g. `pyzbar` for QR-codes + 1D barcodes; or `zxing-cpp` for higher-performance decoding; LE31 currently has no barcode-reading dependency).
  - Schema: a `StorageLocation` SQLModel table + the storage-location fields on `StockEntry`.

## Open questions

- Should LE31 v1 introduce a `storage_location_id` field on StockEntry (the *physical-place* primitive)?
- Should LE31 v1 introduce a barcode-scanner-equipped cook bot (the *hardware-mediated input* primitive)?
- Should LE31 v1 introduce a warehouse-management surface (the *physical-storage-surface tracking* discipline)?
- Should LE31 v1 introduce a `counted_at + counted_by_actor + physical_count` discrepancy-check audit trail (the *physical-floor verification* primitive)?
- If yes to any of the above: should the v1 PR cross-reference this feature 200 contract + HANDOFF as the named architectural reference?

## Why this matters

The *stock-ledger-as-physical-place* primitive is the **gap** between LE31 v1's digital-only stock ledger and a *physical-floor* kitchen where the cook walks to a shelf to grab stock. The 5-verbs vocabulary (receive + store + move + sell + check) is the *physical-floor* extension that maps the existing 2 LE31 StockEntry verbs (receive + sell → mapped to `entry_type='receive'` + `entry_type='consumption'`) onto 3 hypothetical storage-location verbs (store + move + check). The barcode-scanner primitive is the *hardware-mediated input* primitive that could in principle replace the cook's typed-message workflow. The warehouse-management primitive is the *physical-storage-surface* discipline.

The **charter §3.1 invariant alignment**: LE31 v1's charter §3.1 says *"append-only StockEntry ledger"* — the 5-verbs vocabulary preserves the append-only invariant (every receive/store/move/sell/check event is an `audit_logs` row with `recorded_at` + `actor_user_id`, not an UPDATE of a mutable row). The 3 hypothetical fields (`storage_location_id` + `transferred_at` + `counted_at` + `counted_by_actor` + `physical_count`) compose with the existing `recorded_at + actor_user_id` provenance pattern; the chain-verifier (`audit_logs.recorded_at` ordering) remains the source-of-truth for *what happened when*; the storage-location fields add *where* provenance.

The **first in-window 2026 Python inventory-management repo of the 51-pass series** with the *physical-floor-verbs (receive + store + move + check)* vocabulary: this is the strongest external-evidence observation of the 5-verbs vocabulary in the 51-pass series. The cumulative cluster of `stockpile-hermitedge + ladle + KitchenIQ + azizsekerdil + sausageos + shopdesk + bamideleadedeji + FullHouse-Updated + ledgerkb + arbiter` documents the *restaurant-domain + Python + FastAPI + PostgreSQL + inventory-management + kitchen-workflow + append-only + audit-log + warehouse-management* cluster from multiple angles. The brainstorm value is the **v1-architecture vocabulary validation** + the **physical-floor vocabulary extension** + the **barcode-scanner + warehouse-management primitive documentation** for the next v1 schema-extension moment.

The **null license = vocabulary-only artifact** posture explicitly aligns with charter §3.2 (the codebase is not a v1 dependency; the vocabulary is the value) and charter §3.1 (the *where* + 5-verbs vocabulary preserves the append-only invariant). The **§3.4-compatible** posture (staff-facing AI-assist via `together-ai`, NOT customer-facing AI) explicitly aligns with charter §3.4 (operator-tooling not customer-facing AI).

Trigger for re-evaluation: first v1 PR that adds a barcode-scanner integration, a `storage_location_id` field on StockEntry, a `transferred_at` + `from_location_id` + `to_location_id` chained audit trail, a `counted_at` + `counted_by_actor` + `physical_count` discrepancy-check audit trail, or a warehouse-management surface.

Trigger for cross-section: first v1 PR that adds a *physical-floor assistant* (a PDA, a tablet, a barcode-scanner-equipped device for staff) — the *hardware-mediated input* primitive would need to compose with the existing cook-Telegram-bot surface (the *typed-message input* primitive) for the *physical-floor + digital-floor* hybrid operator model.
