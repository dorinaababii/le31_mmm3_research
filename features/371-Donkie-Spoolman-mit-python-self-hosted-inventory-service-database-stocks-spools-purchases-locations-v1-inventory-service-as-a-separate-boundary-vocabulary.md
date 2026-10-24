# Feature 371 — `Donkie/Spoolman` self-hosted-Python-inventory-service-+-database-+-stocks-+-purchases-+-locations (defer)

> **NEW observation (2026-10-24).** Documents in-window GitHub repo `Donkie/Spoolman` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★2932/⑂308**, **8,827 KB**, **Python ✓ ON-STACK**, created **2023-04-01 AND pushed 2026-10-23T08:09:14Z = IN-WINDOW BY PUSH** (a 3.5-year-old repo with an in-window push), `archived=false`, `fork=false`, **171 open issues**, default_branch=`master`. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-24, not from search-result numbers. Description (verbatim from GitHub API): *"Keep track of your inventory of 3D-printer filament spools."* Topics (verbatim): `3d-printing, database, inventory, service`. Bucket: **v1 (inventory-service-as-a-separate-boundary vocabulary)** — Pick B of Daily Research 2026-10-24. Build verdict: `defer` (parking-lot; **vocabulary reference only**).

## Goal

Retain the **inventory-as-a-separate-self-hosted-service-with-its-own-database** shape as a persistent reference, and record the observation that a mature, genuinely-tractioned Python project (★2932, 171 open issues, 3.5 years of continuous work) has converged on running inventory as a **standalone process with its own database** rather than as a module inside a larger application.

No code today. The value is the **counterfactual**: it shows what LE31's stock ledger would look like if it were ever split out into its own service.

## Scope

**In scope (defer artifact):**

- A written record of the **service-boundary shape**: inventory data living behind its own database, served by its own long-running process, with the host application talking to it over an interface rather than sharing tables.
- A written record of the **scale reference**: ★2932/⑂308 with 171 open issues is the only genuinely-tractioned in-window inventory project, and it is a *service*, not a feature.
- A decision record noting that **LE31's own §4.3 stock ledger already implies this boundary** (stock is a derived projection over append-only entries, which is a service-shaped concern), but LE31 has never externalised it.

**Out of scope (defer artifact):**

- Any LE31 code, schema, or migration.
- Adopting the Spoolman codebase (its domain is 3D-printer filament: spools, locations, purchase prices — the vocabulary of a *material store*, not a kitchen).
- Splitting LE31's stock ledger into a separate service. §3.1 says one restaurant; a second service is a §3.5 deployment decision that no one has asked for.
- Any multi-location, multi-warehouse, or transfer-between-locations feature. §3.2 excludes multi-location explicitly.

## Description

`Donkie/Spoolman` tracks inventory of 3D-printer filament spools. Its relevance is **not the domain** — filament spools are consumable stock with purchase prices, batch identity, and a location, which is superficially close to LE31's prepared batches and is actually a different problem. Its relevance is the **architecture**:

1. **A separate service, not a module.** The repo ships as a standalone inventory *service* with its own database. The host application does not read its tables; it asks it. This is the shape LE31's `StockEntry` ledger is *already* — a self-contained, derivable concern — but has never been *run* as.
2. **One persistence concept, cleanly separated.** Locations, stock items, and purchases are the whole model. There is no ad-hoc "quantity on hand" column anywhere; on-hand is derived from movements. **That is §4.3 exactly.**
3. **A real operational footprint.** 171 open issues against a ★2932 project is a project with genuine users and genuine support load. Recorded plainly: **this is the cost side of the shape.** Running an inventory service means triaging 171 issues' worth of surface area, and LE31's §3.2 explicitly chooses "single VPS + systemd unit" over Docker for v1. A service boundary has a price.

**The domain shift is severe and recorded plainly.** Filament is not food: it has no expiry, no FEFO, no prep-batch, no kitchen. §4.3's `StockEntry` reasons (`initial`, `sale`, `sold_out`, `waste`, `restock`) have **no counterpart** in a filament store — there is no "sold_out" because filament is never sold per unit in service. **Do not read this repo as a model of LE31's stock semantics.** What it models is the *deployment* shape and the *derivation* discipline, and only those.

**The traction caveat, stated plainly:** ★2932/⑂308 is real traction — but it is traction for *3D-printer filament inventory*, **not for restaurant software and not for LE31's problem.** A star count is not a demand signal. LE31's restaurant domain has no traction evidence anywhere in this window (see the report).

## Data model

None shipped. The shape implies a service owning: **Location** (where stock sits), **StockItem** (a thing that can be consumed), **Purchase** (money in, stock in), **Movement/Entry** (append-only, signed delta). LE31's own `StockEntry` already *is* the movement table, and `batch.qty_remaining` already *is* the derived projection — the only genuinely new element would be the **service boundary**, i.e. `backend/services/stock_service.py` becoming a network boundary rather than a module call. **Not proposed.**

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (all must hold):** (1) the stock ledger needs to be consumed by something outside the LE31 process (e.g. a second surface or an external tool); (2) a §3.5 deployment decision authorises a second long-running process; (3) the issue tracker and the deployment story are both acceptable to the owner — **the 171-issue footprint in this reference is the honest cost of the shape.**

## Telegram interaction if any

None today. Long-horizon note: if the stock ledger ever becomes a service, the **cook's Telegram bot is the surface most likely to need it** (sold-out alerts, waste entries). The cost is that the bot now depends on a second process being up. Under §3.5 that dependency must be optional — a degraded bot that cannot reach the stock service must still accept orders. **This is the concrete reason the "no required outbound calls" phrasing in feature 370 matters: it is the rule that would forbid making the stock service a hard dependency of the cook bot.**

## Dependencies

None. No new packages, no schema migration, no infrastructure.

## Open questions

1. **Would LE31 ever split the stock ledger into its own service?** Unmade. Nothing has asked for it. Recorded because this pick shows both the shape *and* its price (171 issues).
2. **Does the cook bot degrade gracefully if a stock service is unreachable?** Unanswerable today (no such service). If feature 370's "no required outbound calls" rule is adopted, this becomes a design constraint to write down.
3. **What is the real cost of the derived-projection discipline at LE31's scale?** Unknown. LE31 has one restaurant, one kitchen, and perhaps a few hundred entries a day — far below the scale at which a separate service pays for itself. **Recorded as an explicit reason this is a defer, not a build.**

## Why this matters

Because it is the pass's **honest counterfactual**, and because the cost is the interesting half.

Most of the LE31 research series surfaces shapes LE31 could adopt. This one surfaces a shape LE31 could adopt *and the bill for it*. A ★2932 self-hosted inventory service with 171 open issues is what happens when a small domain (spools) is served by a dedicated process — and LE31's domain (one restaurant, one kitchen, one waiter, one cook) is **three orders of magnitude smaller**. Running a service for LE31's stock ledger would cost the owner maintenance attention that LE31's v1 scope explicitly minimises ("one-click local dev setup", "single VPS + systemd unit", "no Docker required").

**The takeaway is the negative result, and negative results are worth filing.** The shape is not wrong for LE31; it is *too big* for LE31. That is a decision-support fact, not a feature. Recording it means that if a future pass proposes a stock service, this reference is already on file and the answer is known: *the shape works, and it does not pay here.*

The second reason it matters: Spoolman derives on-hand from movements and never stores it — **independently arriving at §4.3's derive-never-mutate rule from a completely different domain**, the second such external arrival in this pass (see feature 370). Two independent projects, one week, two different domains, same two rules: money is `Decimal`, stock is derived. That is now a *pattern* in the corpus, not a coincidence.

## Cross-section

Features 15 (`inventory-variance`), 153 (`sausageos-production-erp-append-only-stock-fefo-versioned-recipes`), 176 (`Sholu021/KitchenIQ` — FastAPI + PostgreSQL restaurant ERP with FEFO), 259 (`CtrlAltDevelop/ledger-service` — idempotent append-only service), 297 (`jonalemndi2/ALdia` — inventory + immutable audit trail), 370 (`jdmacleod/kitchen-erp` — "append-only facts" + "no required outbound calls"). The inventory-service shape is already covered by features 259 and 297; what is **new** here is the **traction + maintenance-cost reference** that makes the defer decision explicit rather than implicit. GitHub `Donkie/Spoolman` is unique vs features 1–369 (verified by ripgrep against `features/`, `specs/` and `INDEX.md`). Fully reversible — documentation-only artifact.
