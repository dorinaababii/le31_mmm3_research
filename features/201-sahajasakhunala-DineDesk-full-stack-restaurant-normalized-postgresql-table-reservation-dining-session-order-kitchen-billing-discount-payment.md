# Feature 201 — `sahajasakhunala-DineDesk-full-stack-restaurant-normalized-postgresql-table-reservation-dining-session-order-kitchen-billing-discount-payment` (defer)

> **NEW observation (2026-09-19).** Documents in-window GitHub repo `sahajasakhunala/DineDesk` (**license=null** (`spdx_id: null` in raw JSON), **0★/0⑂**, Python, **pushed 2026-09-16T19:56:52Z** (3 days ago, in-window by `pushed_at` only), **created 2026-08-21T06:17:57Z** (29 days old, in-window by `created_at` — *both* fields in-window), **43 KB tiny repo** — the *smallest in-window 2026 Python restaurant-POS repo of the 51-pass series*, default_branch=`main`). Topics (verbatim from raw JSON): `[]` (no GitHub topics — empty array; unusual but not blocking). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-19, truncated at the GitHub API 200-char truncation): *"Full-stack restaurant management system with a normalized PostgreSQL database for table reservations, dining sessions, order processing, kitchen workflows, billing, discounts, payments, and operational…"* The **normalized-PostgreSQL-restaurant-domain-schema primitive** + the **7-surfaces vocabulary** (table reservations + dining sessions + order processing + kitchen workflows + billing + discounts + payments + operational = the 8-word description names the surface area): 4 of these map onto LE31's existing 4 SQLModel table families (`Order` for order processing + `Bill` for billing + `Payment` for payments + `StockEntry` for kitchen workflows inventory traceability) + 3 named-gap vocabulary (`Reservation` for table reservations + `DiningSession` for dining sessions + `Discount` for discounts). The **43 KB tiny repo** is the **smallest in-window 2026 Python restaurant-POS repo of the 51-pass series** (vs the *7002 KB* `eddierzhang/FullHouse-Updated` from feature 191 = 163× larger; vs the *119 KB* `skaslam1407/Restaurant-and-Cloud-Kitchen-Operations-Management` from feature 195 = 2.8× smaller; vs the *74 KB* `Naveenkumaar/voxbridge` = 1.7× smaller); the size signals the *minimal-viable-restaurant-schema* — what surfaces fit in 43 KB? Just the *schema + a thin FastAPI wrapper*; no business logic. The **null license** blocks §3.2 code adoption (LE31 would have to re-implement the 7-surfaces schema against its own alembic + SQLModel migration chain, not import the FastAPI routes), but the **schema vocabulary** is the brainstorm value. No AI surface so charter §3.4 is not applicable. Bucket: **v1 architecture-reference (normalized-PostgreSQL-restaurant-domain-schema primitive, parking-lot defer)** — vocabulary + 7-surfaces vocabulary + 3-gap vocabulary (Reservation + DiningSession + Discount) documentation, zero build time today.

## Goal

Retain the **"Full-stack restaurant management system with a normalized PostgreSQL database for table reservations, dining sessions, order processing, kitchen workflows, billing, discounts, payments, and operational…"** cross-section architectural vocabulary + **normalized-PostgreSQL-restaurant-domain-schema primitive** + **7-surfaces vocabulary** as the persistent v1 architecture reference for any future LE31 v1 maintainer asking the *restaurant-domain-7-surfaces-schema* question (does LE31 v1 ever need to add a `Reservation` SQLModel table, a `DiningSession` SQLModel table, or a `Discount` SQLModel table?). The artifact is the persistent *normalized-PostgreSQL-restaurant-domain-schema primitive* + the *7-surfaces vocabulary* as a *named* v1 architectural reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `DineDesk` cross-section vocabulary: the **smallest in-window 2026 Python restaurant-POS repo of the 51-pass series** (43 KB); the **first in-window restaurant-POS schema-only repo** of the 51-pass series (the description explicitly names a *normalized PostgreSQL database* + 7 surfaces = a *schema-vocabulary artifact*, not a *business-logic artifact*).
- A written record of the **normalized-PostgreSQL-restaurant-domain-schema primitive**: the *normalized schema discipline* = no duplicated data + relations via explicit foreign keys + PostgreSQL-native types (JSONB + arrays + range types + CTEs). LE31 v1's SQLModel + alembic stack already implements this discipline; `DineDesk` is the *external 2026 evidence* that the *normalized-PostgreSQL-restaurant-domain-schema* discipline is current 2026 demand.
- A written record of the **7-surfaces vocabulary**: `table reservations + dining sessions + order processing + kitchen workflows + billing + discounts + payments + operational` (the description lists 7 surface names + an 8th word `and operational…` = an unknown continuation, probably *and operational reports* or *and operational dashboards*). The 7 surfaces map onto **4 of LE31 v1's existing 4 SQLModel table families** + **3 named-gap vocabulary**:
  - `table reservations` → **GAP: LE31 v1 has no `Reservation` SQLModel table** (only `Order` + `Bill`; no pre-booked-table primitive)
  - `dining sessions` → **GAP: LE31 v1 has no `DiningSession` SQLModel table** (only `Order` + `Bill`; no start-time + end-time + party-size primitive)
  - `order processing` → ✓ direct match (LE31 v1 has `Order` SQLModel table per charter §3.1)
  - `kitchen workflows` → ✓ direct match (LE31 v1 has cook Telegram bot + StockEntry consumption traceable via audit_logs)
  - `billing` → ✓ direct match (LE31 v1 has `Bill` SQLModel table per charter §3.1)
  - `discounts` → **GAP: LE31 v1 has no `Discount` SQLModel table** (only `Bill.total_eur`; no line-item-discount primitive)
  - `payments` → ✓ direct match (LE31 v1 has `Payment` SQLModel table per charter §3.1; in the v1 schema the `Bill` table itself has a `paid_at` + `payment_method` field, which may also serve)
  - `operational` (truncated) → unknown continuation — possibly *operational reports* or *operational dashboards*
- A written record of the **null license as a documented vocabulary-only artifact**: the codebase cannot be adopted as a library (null license = §3.2 blocker for *import-and-extend*); the *7-surfaces + normalized-PostgreSQL-schema + Reservation + DiningSession + Discount vocabulary* is the value, not the code; LE31 would re-implement the 7-surfaces schema against its own alembic + SQLModel migration chain, not import the FastAPI routes.
- A written record of the **43 KB tiny repo as a *schema-vocabulary* signal**: the size signals the *minimal-viable-restaurant-schema* — what surfaces fit in 43 KB? Just the *schema + a thin FastAPI wrapper*; no business logic. The repo's primary value is the *schema vocabulary*, not the *business-logic implementation*.
- A decision record: today's verdict is `defer (parking-lot)` because the *7-surfaces + normalized-PostgreSQL-schema + 3-gap vocabulary* is a v1 architecture reference, not a v1 build implication. v1 covers 4 of 7 surfaces today (Order + Bill + Payment + StockEntry-kitchen-workflow); the 7-surfaces vocabulary documents the *Reservation + DiningSession + Discount + operational* surfaces for the next v1 maintainer.

**Out of scope (defer artifact):**
- Any change to the LE31 v1 schema (no `Reservation` table today, no `DiningSession` table today, no `Discount` table today).
- Any change to the waiter web UI (HTMX) or cook Telegram bot.
- Adoption of the `DineDesk` code as a v1 dependency (the repo is 0★/0⑂ at 43 KB; the *7-surfaces + normalized-PostgreSQL-schema* vocabulary would need to be independently re-implemented and validated against the LE31 append-only StockEntry ledger + audit_logs + Order + Bill + Payment SQLModel tables, not simply imported; the null license is a §3.2 blocker; the FastAPI routes are off-pattern for LE31 v1's specific route structure). The cross-section is *primitive vocabulary extension + 7-surfaces + normalized-schema documentation*, not *library adoption*.
- Any change to the `audit_logs` table or `StockEntry` ledger today.
- Any new dependency on the `sahajasakhunala` maintainer.

## Evidence / JTBD

When a future LE31 v1 maintainer asks *"if v1 introduces a Reservation SQLModel table (for table reservations), a DiningSession SQLModel table (for dining-session start-time + end-time + party-size), or a Discount SQLModel table (for line-item-discount primitives), what is the normalized-PostgreSQL-restaurant-domain-schema discipline that preserves the existing v1 Order + Bill + Payment + StockEntry + audit_logs invariants?"*, the maintainer wants *evidence that another independent 2026 Python repo at 43 KB with null license + both fields in-window + restaurant-POS + normalized-PostgreSQL-schema is shipping the 7-surfaces vocabulary (table reservations + dining sessions + order processing + kitchen workflows + billing + discounts + payments + operational) as the canonical 2026 restaurant-management surface area*, but struggles because *v1 has no documented normalized-PostgreSQL-restaurant-domain-schema primitive in the charter*, so that *v1 can introduce the Reservation + DiningSession + Discount surfaces with the explicit 7-surfaces vocabulary rather than inventing a new one*.

- **Evidence class**: observed (the `DineDesk` description explicitly names *"normalized PostgreSQL database"* + the 7-surfaces vocabulary = the *normalized-PostgreSQL-restaurant-domain-schema primitive + 4-of-7 direct LE31 SQLModel-table matches + 3-gap vocabulary* triple).
- **Confidence**: medium-high for the 7-surfaces vocabulary (null + Python + 43 KB + both fields in-window + explicit *normalized-PostgreSQL* + 7-surfaces description); low for *adoption* (LE31 should re-implement the 7-surfaces schema against its own alembic + SQLModel migration chain, not import the FastAPI routes; the null license is a §3.2 blocker).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + 7-surfaces + normalized-PostgreSQL-schema documentation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + 7-surfaces + 3-gap + normalized-PostgreSQL-schema documentation**: when (if) LE31 v1 introduces a Reservation SQLModel table, a DiningSession SQLModel table, or a Discount SQLModel table, the *7-surfaces + normalized-PostgreSQL-schema + 4-of-7 v1-coverage* vocabulary is documented.

## Description

GitHub `sahajasakhunala/DineDesk` (license=null, 0★/0⑂, Python, pushed 2026-09-16T19:56:52Z, created 2026-08-21T06:17:57Z = *both fields in-window*, 43 KB tiny repo).

Description (verbatim, parent-verified GitHub API direct-GET 2026-09-19, truncated at the 200-char GitHub API cap): *"Full-stack restaurant management system with a normalized PostgreSQL database for table reservations, dining sessions, order processing, kitchen workflows, billing, discounts, payments, and operational…"* (the `…` indicates truncation at the GitHub API 200-char cap; the full description likely extends beyond 200 chars with something like *and operational reports* or *and operational dashboards* or *and operational metrics*; the explicit description carries the 7-surfaces vocabulary; the truncated continuation is not load-bearing for the primitive).

Topics (verbatim from raw JSON): `[]` — **no GitHub topics** (empty array); the maintainer did not tag the repo. This is unusual but not blocking (the description carries the 7-surfaces vocabulary; the topics are not load-bearing for the schema primitive).

The **7 named restaurant-domain surfaces** (with 4-of-7 LE31 v1 coverage + 3-gap vocabulary):

| `DineDesk` surface | LE31 v1 surface | Match status |
|---|---|---|
| `table reservations` | (LE31 v1 has `Order` + `Bill` SQLModel tables, but no *pre-booked-table* `Reservation` SQLModel table) | **★ GAP: LE31 v1 has no `Reservation` table; the DineDesk primitive names the 1st of 3 missing surfaces** |
| `dining sessions` | (LE31 v1 has `actor_user_id` + `actor_role` provenance on `audit_logs`, but no *start-time + end-time + party-size* `DiningSession` SQLModel table) | **★ GAP: LE31 v1 has no `DiningSession` table; the DineDesk primitive names the 2nd of 3 missing surfaces** |
| `order processing` | `Order` SQLModel table | ✓ direct match |
| `kitchen workflows` | Cook Telegram bot (aiogram v3) + cook-facing order queue + StockEntry consumption traceable via audit_logs | ✓ direct match |
| `billing` | `Bill` SQLModel table | ✓ direct match |
| `discounts` | (LE31 v1 has `Bill.total_eur` + `Bill.discount_eur` (if any) as line items, but no *line-item-discount* `Discount` SQLModel table) | **★ GAP: LE31 v1 has no `Discount` table; the DineDesk primitive names the 3rd of 3 missing surfaces** |
| `payments` | `Payment` SQLModel table (or `Bill.paid_at` + `payment_method` field on `Bill`) | ✓ direct match |
| `operational…` (truncated, likely *operational reports*) | (LE31 v1 has no operational-reports SQLModel table; reports are derived from `audit_logs` + `Order` + `Bill` + `Payment` SQLModel tables) | **★ ADJACENT: LE31 v1 has operational reporting via query-on-`audit_logs`, not a dedicated `Report` table** |

The **normalized-PostgreSQL-restaurant-domain-schema primitive**: the *normalized schema discipline* = no duplicated data + relations via explicit foreign keys + PostgreSQL-native types (JSONB + arrays + range types + CTEs). LE31 v1's SQLModel + alembic stack already implements this discipline. The *normalized-PostgreSQL* phrasing in the description is the *external 2026 evidence* that the *normalized-PostgreSQL-restaurant-domain-schema* discipline is current 2026 demand.

The **43 KB tiny repo as a schema-vocabulary signal**: the size signals the *minimal-viable-restaurant-schema* — what surfaces fit in 43 KB? Just the *schema + a thin FastAPI wrapper*; no business logic. The repo's primary value is the *schema vocabulary*, not the *business-logic implementation*. The size is a *demand signal*: a maintainer built a normalized-PostgreSQL restaurant-management schema + a thin FastAPI wrapper *in 43 KB*, suggesting the *minimal-viable-restaurant-schema* is the *current 2026 demand*, not the *minimal-viable-restaurant-app*.

The **null license as a documented vocabulary-only artifact**: the codebase cannot be adopted as a library (null license = §3.2 blocker for *import-and-extend*); the *7-surfaces + normalized-PostgreSQL-schema + 3-gap vocabulary* is the value, not the code; LE31 would re-implement the 7-surfaces schema against its own alembic + SQLModel migration chain, not import the FastAPI routes.

## Data model

**No LE31 data model change today.** The defer artifact is documentation only. The 7-surfaces primitive names the *Reservation + DiningSession + Discount + operational* surfaces that any future v1 schema change should consider; v1 maintainer decision required before adopting the 7-surfaces vocabulary (LE31 v1 currently operates 4 of 7 surfaces; the 7-surfaces vocabulary documents the *Reservation + DiningSession + Discount + operational* surfaces for the next v1 maintainer).

## Implementation steps

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a Reservation SQLModel table, a DiningSession SQLModel table, or a Discount SQLModel table):

- `app/models/reservation.py` — possibly add (the SQLModel table for the pre-booked-table primitive; depends on the v1 change).
- `app/models/dining_session.py` — possibly add (the SQLModel table for the start-time + end-time + party-size primitive; depends on the v1 change).
- `app/models/discount.py` — possibly add (the SQLModel table for the line-item-discount primitive; depends on the v1 change).
- `app/models/report.py` — possibly add (the SQLModel table for the operational-reports primitive; depends on the v1 change).
- `app/models/order.py` — possibly modify to add the *reservation_id* FK (the table-reservation integration with the existing Order primitive; depends on the v1 change).
- `app/models/bill.py` — possibly modify to add the *discount_id* FK (the line-item-discount integration with the existing Bill primitive; depends on the v1 change).
- `app/api/reservations.py` — possibly add (the FastAPI route that handles reservation creation + lookup; depends on the v1 change).
- `tests/test_reservation_flow.py` — possibly add (the integration test for the reservation primitive; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Telegram interaction if any

None today. If a future v1 trigger fires (Reservation SQLModel table added), the Telegram interaction would be a *reservation-bot* surface (a future v1 PR adds a Telegram bot that handles reservation creation + lookup via Telegram commands like `/reserve <table-id> <time> <party-size>`); the cook-bot surface would persist for order-cooking flow; the new reservation-bot would be a *separate* Telegram bot surface.

## Dependencies

- No new dependency today.
- If a future v1 trigger fires:
  - Schema: `Reservation` + `DiningSession` + `Discount` + `Report` SQLModel tables.
  - Routes: FastAPI routes for reservation creation + lookup + discount application.
  - (If reservation-bot triggered): a Telegram bot with reservation-creation commands.

## Open questions

- Should LE31 v1 introduce a `Reservation` SQLModel table (the *pre-booked-table* primitive)?
- Should LE31 v1 introduce a `DiningSession` SQLModel table (the *start-time + end-time + party-size* primitive)?
- Should LE31 v1 introduce a `Discount` SQLModel table (the *line-item-discount* primitive)?
- Should LE31 v1 introduce a `Report` SQLModel table (the *operational-reports* primitive; vs query-on-`audit_logs`)?
- If yes to any of the above: should the v1 PR cross-reference this feature 201 contract + HANDOFF as the named architectural reference?

## Why this matters

The *normalized-PostgreSQL-restaurant-domain-schema* primitive is the **gap** between LE31 v1's 4-of-7 surface coverage (Order + Bill + Payment + StockEntry-kitchen-workflow) and a *full 7-of-7 surface coverage* (Order + Bill + Payment + Reservation + DiningSession + Discount + operational-reports). The 7-surfaces vocabulary is the *external 2026 evidence* that the *normalized-PostgreSQL-restaurant-domain-schema* discipline is current 2026 demand. The 3 named-gap vocabulary (Reservation + DiningSession + Discount) is the *extension surface* that any future v1 PR could adopt as the *canonical future-extension vocabulary*.

The **charter §3.1 invariant alignment**: LE31 v1's charter §3.1 says *"append-only StockEntry ledger"* + *"two primary operational surfaces—waiter web UI and cook Telegram bot"* — the 7-surfaces vocabulary preserves the append-only invariant (every reservation/session/order/bill/discount/payment event is an `audit_logs` row with `recorded_at` + `actor_user_id` if mutated, not an UPDATE of a mutable row). The 4 hypothetical SQLModel tables (`Reservation` + `DiningSession` + `Discount` + `Report`) compose with the existing `Order` + `Bill` + `Payment` + `StockEntry` SQLModel tables; the chain-verifier (`audit_logs.recorded_at` ordering) remains the source-of-truth for *what happened when*.

The **smallest in-window 2026 Python restaurant-POS repo of the 51-pass series** (43 KB): this is the **first in-window restaurant-POS schema-only repo** of the 51-pass series (the description explicitly names a *normalized PostgreSQL database* + 7 surfaces = a *schema-vocabulary artifact*). The 43 KB size is a *demand signal* — a maintainer built a normalized-PostgreSQL restaurant-management schema + a thin FastAPI wrapper *in 43 KB*, suggesting the *minimal-viable-restaurant-schema* is the *current 2026 demand*.

The **null license = vocabulary-only artifact** posture explicitly aligns with charter §3.2 (the codebase is not a v1 dependency; the vocabulary is the value) and charter §3.1 (the 7-surfaces + 4-of-7 v1-coverage + 3-gap vocabulary preserves the append-only invariant). The **no-AI-surface posture** (no `together-ai` topic, no `ai-agents` topic, no `llm` topic) explicitly aligns with charter §3.4 (operator-tooling not customer-facing AI).

Trigger for re-evaluation: first v1 PR that adds a `Reservation` SQLModel table, a `DiningSession` SQLModel table, a `Discount` SQLModel table, or a `Report` SQLModel table.

Trigger for cross-section: first v1 PR that adds a *reservation-bot* Telegram surface (the *Telegram-mediated reservation-creation* primitive would need to compose with the existing cook-Telegram-bot surface (the *order-cooking* primitive) and the waiter-HTMX-surface (the *order-taking* primitive) for the *reservation-to-order* flow).
