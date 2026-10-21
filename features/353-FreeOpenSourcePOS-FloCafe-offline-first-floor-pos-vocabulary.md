# Feature 353 — `FreeOpenSourcePOS-FloCafe-offline-first-floor-pos-vocabulary` (defer)

> **NEW observation (2026-10-21).** Documents in-window GitHub repo `FreeOpenSourcePOS/FloCafe` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★148/⑂63 = the strongest-traction pick of the 83-pass brainstorm series** (previous series high was ★5), **28,192 KB moderate**, **TypeScript/Electron OFF-STACK for LE31's Python stack**, **pushed 2026-10-21T07:01:24Z (today) = IN-WINDOW BY PUSH**, created 2026-05-07T07:51:42Z = ~5.5-month-old repo with an in-window push, `archived=false`, `fork=false`, 56 open issues, default_branch=`main`). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-21): *"Free, open-source, offline-first Point of Sale for cafes, restaurants, and food businesses."* Topics (verbatim, parent-verified, **20 topics**): `billing-software, cafe-management, cafe-pos, electron, food-ordering, free-pos, inventory-management, kitchen-display, kitchen-display-system, offline-first, open-source, point-of-sale, pos, pos-system, receipt-printer, restaurant-management, restaurant-pos, restaurant-software, self-hosted, thermal-printer`. Bucket: **v1 (offline-first-floor-POS + kitchen-display + receipt/thermal-printer + inventory + billing + self-hosted vocabulary)** — Pick A of Daily Brainstorm 2026-10-21. Build verdict: `defer` (parking-lot; **vocabulary reference only**; MIT permits code-shape reuse but no v1 surface currently demands it).

## Goal

Retain the **offline-first POS + kitchen-display + thermal receipt printing + inventory + billing + self-hosted** vocabulary as a persistent cross-section reference for the LE31 v1 *floor-data-model* wedge, and document the primitive that an independent maintainer shipped and has been actively pushing daily in 2026 (20-topic array + the *offline-first* posture + the *kitchen-display* posture + the *thermal-printer* posture + the *self-hosted* posture IS the canonical §3.1 + §3.4 + §3.5 *hands-busy phone-first + deterministic kernel + single-binary-install-on-Italian-desktop-laptop + self-hosted* charter invariant applied to the *LE31-v1-floor-data-model* dimension) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **offline-first + kitchen-display + receipt/thermal-printer + inventory + billing + self-hosted** 6-tuple-primitive: a cafe POS that keeps working when the network does not, drives a kitchen display, prints receipts on a thermal printer, tracks inventory, does billing, and is self-hosted. The transferable primitive is **offline-first as the default posture, not a fallback mode** — the POS is designed so the network being down is not an exceptional state.
- A written record of the **20-topic, 100% LE31-relevant** stack shape: this is the **widest-topic restaurant-POS vocabulary of the 83-pass brainstorm series**; the *offline-first + self-hosted* posture IS the canonical §3.5 *single-binary-install-on-Italian-desktop-laptop + self-hosted* invariant; the *kitchen-display + kitchen-display-system* posture is the canonical §3.1 *operator-surface-degrades-to-a-shared-screen* invariant; the *thermal-printer + receipt-printer* posture is the canonical §3.4 *deterministic-kernel + hardware-as-first-class-output* invariant.
- A written record of the **dual-surface pairing**: this repo (desktop/Electron kitchen display) is deliberately paired with Pick C (`Haroon-World/RestaurantPOS_Android`, Python/Kivy + Bluetooth ESC/POS) — the SAME order→kitchen→print flow rendered to two different hardware surfaces over one offline-first kernel. Sister-shape to features 302 (`mhmd2042/cafe-pos`), 323 (`movsarusumov172-crypto/KitchenQ`), 304 (`drwjkirkpatrick-web/the-pass`), 347 (`mdaedalus/tableflow`), 348 (`ninondev/stove`), 349 (`gfs-invoice-breakdown`).
- A decision record: today's verdict is `defer` because (1) LE31 v1 today is HTMX-waiter + aiogram-cook-bot + append-only StockEntry and has **no kitchen-display surface at all**; (2) the *offline-first* posture implies a sync-conflict story that LE31 v1 has not designed; (3) the demand-signal is the value, not the code.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Adoption of the FloCafe codebase (TypeScript/Electron is off-stack for LE31's Python 3.13 / FastAPI / SQLModel charter).
- Any sync-conflict-resolution design. That is a separate future spec, not a vocabulary note.
- Cross-section candidate for v1 if LE31 ever adds a kitchen-display surface (charter §3.1 + §3.4 + §3.5 review required).

## Out of scope

- See "Scope" above. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v1 surface proposes "a kitchen display the cook can read at a glance", the owner wants *proof the shape is real and actively maintained*, but struggles because *LE31 has no documented evidence that an offline-first kitchen-display POS with thermal printing is a live 2026 shape rather than a hobby project*.

- **Evidence class**: observed (the verbatim description + 20 verbatim topics name the primitives explicitly, and the direct-GET star/fork/push counts were read from the repo endpoint, not from a search index).
- **Confidence**: medium-high for the vocabulary match; **high for traction relative to the series** (★148/⑂63 is ~30× the previous series high of ★5 — but see the caveat below); low for transferability (LE31 v1 has no kitchen-display surface today).
- **Traction caveat, recorded plainly**: ★148/⑂63 is real, parent-verified API data, but it is **not** evidence of restaurant-industry adoption. This repo's topic set is broad and generic, and no owner mention of FloCafe exists in 83 passes. Traction is a tie-breaker, not a demand signal.
- **Real observed LE31 JTBD**: zero direct JTBD today. The value is the named primitive, ready when the first v1 kitchen-display PR lands.

## Description

GitHub `FreeOpenSourcePOS/FloCafe` (MIT ✓ §3.2 STRICTLY-COMPATIBLE, ★148/⑂63, 28,192 KB, TypeScript/Electron, pushed 2026-10-21T07:01:24Z, created 2026-05-07T07:51:42Z, archived=false).

The architectural primitive has multiple sub-primitives that map onto the LE31 v1 surface:

1. **Offline-first as the default posture** — the network being down is not an exceptional state. IS the canonical §3.4 *deterministic kernel* invariant: business logic runs locally and does not depend on a remote call succeeding.
2. **Kitchen display** — a dedicated screen the cook reads, distinct from the waiter surface. IS the canonical §3.1 *two-role surface* invariant that LE31 v1 already has (waiter HTMX + cook aiogram), here expressed as *two screens on one local system* rather than *two clients of one server*.
3. **Thermal / receipt printing** — hardware as a first-class output. IS the canonical §3.4 *deterministic-kernel + hardware-as-first-class-output* invariant (and pairs with feature 348 `ninondev/stove` ESC/POS vocabulary).
4. **Inventory management as a first-class concern** — IS the canonical §3.3 *append-only derived-not-persisted* tension point: FloCafe pairs billing with inventory, whereas LE31 v1's StockEntry ledger is append-only with no mutable inventory row. This is the sharpest design question the pick raises.
5. **Billing** — a money surface. LE31 v1 has EUR pricing but no billing; adopting a billing vocabulary triggers a §3.7 review of what is guest data.
6. **Self-hosted + open-source** — IS the canonical §3.5 *self-hosted + single-install* invariant.

## Data model

None shipped. The vocabulary implies a shape worth recording: **Order** (the sole persisted entity, per feature 347's *order-as-sole-persisted-entity* primitive), with **table/garson** and **item** as lookup columns rather than separate CRUD surfaces, and **kitchen-display state** as a **projection over order state** rather than a separate persisted queue. The **inventory** concern is explicitly flagged as the open question: append-only StockEntry + a mutable inventory count is a reconciliation problem, not a modelling one.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (all must hold):** (1) a v1 PR proposes a kitchen-display or receipt-printing surface; (2) the charter §3.1/§3.4/§3.5 review is done for offline-first semantics; (3) the StockEntry-append-only vs inventory-count reconciliation question has an owner answer.

## Telegram interaction if any

None today. Note only: the *cook* role in LE31 v1 is already a Telegram bot (aiogram v3). FloCafe's kitchen display is a **screen**, not a chat. If LE31 ever needs a kitchen display, the interesting question is whether it is a second Telegram surface (HTMX page on the kitchen tablet), a second chat, or a thermal printer — that decision is unmade and belongs to a future spec, not this vocabulary note.

## Dependencies

- LE31 v1 charter §3.1 (two-role surface), §3.3 (append-only / derived-not-persisted), §3.4 (deterministic kernel, no inference in the business path), §3.5 (self-hosted, single install), §3.7 (guest data as counts not identity).
- Sister features: 302, 304, 323, 347, 348, 349, 350.
- Paired pick: feature 355 (`Haroon-World/RestaurantPOS_Android`) — the phone-surface sibling.

## Open questions

1. **Append-only StockEntry vs a mutable inventory count.** FloCafe has both billing and inventory; LE31 v1 has append-only StockEntry and no inventory row. Which is the source of truth? Unmade.
2. **Offline-first implies sync.** LE31 v1's Postgres is a single instance on a VPS. What is LE31's offline posture — read-only offline, or full offline-with-merge? Unmade and consequential.
3. **Kitchen display: screen, chat, or printer?** Unmade.
4. **Billing and §3.7.** Billing touches money and possibly guest identity. A §3.7 review is required before any billing surface.

## Why this matters

It is the **highest-traction restaurant-POS vocabulary of the 83-pass series** and the **widest-topic one (20/20 LE31-relevant)**. Its real contribution is the **dual-surface pairing**: combined with Pick C it documents that one order→kitchen→print flow can be written once and rendered to both a desktop kitchen display and a phone-as-Bluetooth-printer over an offline-first kernel. That is exactly LE31's degradation posture, expressed as a portable shape rather than two unrelated codebases. It also surfaces the sharpest unresolved v1 question in the POS domain — **append-only ledger vs mutable inventory** — which has been implicit across features 108, 225, 290, 298, 342, 343, 349 and is now worth naming explicitly.