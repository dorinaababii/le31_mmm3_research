# Feature 153 — sausageos-production-erp-append-only-stock-fefo-versioned-recipes (defer)

> **NEW observation (2026-09-08).** Documents in-window GitHub repo `patseluk-lang/sausageos` (MIT, **0★/0⑂**, Python, **pushed 2026-09-07T13:47:05Z**, in-window by push only, 182 B description). Description (verbatim): *"Production ERP where stock is an append-only ledger: versioned recipes, FEFO, costing from the lots actually consumed, batch recall. Django + DRF."* Topics: `erp`, `manufacturing`, `htmx`, `postgresql`, `traceability`, `docker`, `celery`, `pytest`. **The most LE31-aligned primitive of the 40-pass series**: the manufacturing-stock discipline (raw materials → WIP → finished goods, all as append-only ledger entries) maps **1:1** onto LE31 charter §3.1 (every prepared-item quantity change is a new `StockEntry`). Bucket: **v1 architecture-reference** — watch-list defer. Zero build time today.

## Goal

Retain the **"stock is an append-only ledger: versioned recipes, FEFO, costing from the lots actually consumed, batch recall"** production-ERP primitive set as a persistent cross-section reference for the LE31 v1 architecture review. The artifact is the persistent cross-section reference + a candidate *named pattern set* for the prepped-item stock + recipe + costing surfaces. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the sausageos production-ERP primitive set: *append-only stock ledger* + *versioned recipes* + *FEFO (First-Expired-First-Out)* + *costing from lots actually consumed* + *batch recall*.
- A written record of the **1:1 mapping onto LE31 v1 architecture**: the manufacturing-stock discipline (raw materials → WIP → finished goods) is the *production-ERP analog* of LE31's prepped-item stock (ingredients → prepared items → served items).
- A written record of the **batch recall** primitive (the manufacturing equivalent of LE31's `Bill` derivation — a derived view of `StockEntry` that can be reconstructed from the ledger).
- A decision record: today's verdict is `defer` because the LE31 v1 codebase already implements *append-only stock* implicitly via `StockEntry`; the *manufacturing-grade primitives* (FEFO, lot-based costing, batch recall) are valuable as *named patterns* for the next v1 architecture-review moment, not as immediate code changes.
- A cross-section reference with prior picks: features 121, 122, 125, 127, 129, 133, 134, 135, 137, 138, 139, 141, 145, 146, 147, 148, 149 = the 17-pick append-only-ledger cluster from 2026-09-07.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any change to the prepped-item / recipe / menu data model.
- Any new FEFO discipline (the LE31 v1 prepped-item stock does not have a FEFO discipline today; introducing FEFO would require a new `expires_at` field on `StockEntry` and a new ordering discipline — an *owner decision* per charter §3.2).
- Any new lot-based costing (the LE31 v1 money discipline is *exact EUR values* per charter §3.1, but the *costing-from-lots-actually-consumed* is a *future v2 surface* that requires a link between `StockEntry` and `Bill` line items).
- Any new batch recall (the LE31 v1 menu does not have a batch recall surface today; introducing one would require a *menu-level* `recall_id` field and a new operational transition).
- Adoption of the sausageos code (the repo is a 182 B README + a Django + DRF codebase; the stack is Django, not FastAPI → no code adoption is possible).

## Evidence / JTBD

When a future LE31 maintainer reads the prepped-item stock code, the owner wants *to verify the manufacturing-grade primitives (FEFO, lot-based costing, batch recall) are surfaced*, but struggles because *the current primitives are implicit in the `StockEntry` writes*, so that *the next maintainer can verify the production-ERP-aligned primitives are present*.

- **Evidence class**: observed (the sausageos README names the four production-ERP primitives — *versioned recipes, FEFO, costing from lots actually consumed, batch recall* — and LE31 v1's `StockEntry` discipline implements three of the four implicitly: append-only is implemented, versioned-recipes is partially implemented via `MenuItem.version`, FEFO is not implemented, lot-based costing is not implemented, batch recall is not implemented).
- **Confidence**: high for the architectural match (the four sub-primitives — *append-only stock ledger / versioned recipes / FEFO / lot-based costing / batch recall* — map onto LE31's `StockEntry`, `MenuItem`, missing-FEFO, missing-lot-costing, missing-batch-recall).
- **Real observed LE31 JTBD**: zero-pain today; the codebase is small enough that the primitives are implicit.
- **The value is naming, not direct demand**: when the prepped-item stock *is* reviewed (e.g. before a v2 surface lands that adds FEFO or lot-based costing), the sausageos primitive set is a ready-made *named* production-ERP pattern.

## Description

GitHub `patseluk-lang/sausageos` (MIT, 0★/0⑂, Python, pushed 2026-09-07T13:47:05Z, in-window by push only, 182 B description). Description (verbatim): *"Production ERP where stock is an append-only ledger: versioned recipes, FEFO, costing from the lots actually consumed, batch recall. Django + DRF."*

The architectural pattern has one core principle and four sub-primitives:

1. **"Stock is an append-only ledger"** — every stock movement (raw material received, WIP started, finished good completed, finished good shipped, finished good recalled) is a new ledger row. Current stock is **derived** from the ledger, never stored as a mutable cache.
2. **Versioned recipes** — a recipe is not a single document; it is a *versioned sequence* of documents (recipe v1, recipe v2, ...). Each production run uses a *specific version* of the recipe. The version is part of the production-run record.
3. **FEFO (First-Expired-First-Out)** — when consuming stock, the lot with the *earliest expiration date* is consumed first. This is the *opposite* of FIFO (First-In-First-Out) for non-perishable goods, and is the *right discipline* for perishables (raw materials, WIP, finished goods with shelf life).
4. **Costing from the lots actually consumed** — when computing the cost of a finished good, the cost is derived from the *actual lots that were consumed* (not a moving average or standard cost). This makes the cost *exact* and *traceable* back to the supplier invoices.
5. **Batch recall** — when a finished-good batch is recalled (e.g. contamination), the recall is a *forward derivation* from the ledger: which customers received items from this batch? which ingredients from which suppliers went into this batch? The recall surface is *derived* from the ledger, not a separate database.

**The 1:1 mapping onto LE31 v1 architecture:**

| Sausageos primitive | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| append-only stock ledger | `StockEntry` table (every prepared-item quantity change is a new row) | §3.1 (Never update or delete ledger events) | **Implemented in v1** |
| versioned recipes | `MenuItem.version` field (partial) | §3.1 (every prepared-item quantity change is a new `StockEntry`) | **Partially implemented in v1** — `MenuItem` has versioning but not the *production-run → recipe-version* link |
| FEFO (First-Expired-First-Out) | **NOT IMPLEMENTED in v1** — the prepped-item stock has no `expires_at` discipline | (future v2 surface) | **Not implemented** — would require a new `expires_at` field on `StockEntry` + a new ordering discipline |
| costing from lots actually consumed | **NOT IMPLEMENTED in v1** — the money discipline is *exact EUR values* per `Bill`, but the *cost-from-lots* link between `StockEntry` and `Bill` line items is not built | §3.1 (never use binary floats; preserve exact EUR values) | **Not implemented** — would require a new `Bill_line_item → StockEntry` link table |
| batch recall | **NOT IMPLEMENTED in v1** — there is no menu-level `recall_id` field | (future v2 surface) | **Not implemented** — would require a new `recall_id` field on `MenuItem` + a new operational transition |

**The "stock is an append-only ledger" core principle:**

The sausageos pattern's *core* is identical to LE31 charter §3.1: *every prepared-item quantity change is a new `StockEntry`; never update or delete ledger events; current stock is derived from entries*. The four sub-primitives are *additive* on top of this core: they specify *how to organize the ledger entries* (versioned recipes, FEFO ordering, lot-based costing, batch recall) but the *append-only discipline* is the same.

**What sausageos does NOT transfer:**

- The repo is a 182 B README + a Django + DRF codebase; the stack is **Django, not FastAPI** → no code adoption is possible.
- The author is a *new maintainer* (created 2026-09-04, in-window push 2026-09-07; 0★/0⑂ traction). The 4-day-old repo is *not* production-traction evidence.
- The "FEFO + lot-based costing + batch recall" sub-primitives are *future v2 surfaces*, not v1. Introducing them today would be a *v1 surface expansion* that requires an owner decision per charter §3.2.
- The stack includes `celery` (background tasks) and `htmx` (server-rendered HTML) — both are *transferable disciplines* (HTMX is the same web-surface philosophy as LE31's waiter web UI; Celery is a *future v2* background-task surface), but neither is a direct v1 code change.

**Cross-section with prior picks:**

- **Feature 121 ledger-commitment-field-tier-minimization** — the *what is committed* axis. Sausageos's *append-only stock ledger* is the commit primitive; feature 121's *canonical digest* is the commitment that makes the commit verifiable.
- **Feature 122 trace-integrity-cait-acceptance-criterion** — the *what is queried* axis. Sausageos's *batch recall* is a *forward derivation* (which customers received items from this batch?); feature 122 supplies the query-time measurement.
- **Feature 125 auditable-continual-learning-three-axis** — the *commit-time gate* axis. Sausageos's *versioned recipes* are the *commit-time gate* for production runs (each run commits to a specific recipe version).
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** — the *operational mode of ledger-based control*. Sausageos's *append-only stock* is the ledger; feature 127's *proposal-then-action* is the action the ledger authorizes.
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** — the *explanation-time* axis. Sausageos's *batch recall* is the *explanation-time* primitive (which lots → which customers?); feature 129's *graph* is the *typed edges* that make the explanation queryable.
- **Feature 133 hansard-runtime-witnessing** — the *who witnessed* axis. Sausageos's *versioned recipes* are the *who witnessed the recipe at production time* witness; feature 133 supplies the runtime witness.
- **Feature 134 echo-record-shape** — the *record shape* axis. Sausageos's *append-only stock ledger* is the *commit*; feature 134 is the *record shape* of the commit.
- **Feature 135 dreamledger-execution-settled-credit-ledger** — the *credit ledger* dual. Sausageos's *costing from lots actually consumed* is the *state ledger* for cost; feature 135 is the *credit ledger* for AI agent actions.
- **Feature 137 natural-language-policies-executable-obligations** — the *policy compilation* axis. Sausageos's *versioned recipes* are *compiled policies* (each recipe version is a policy); feature 137's obligations would be *compiled into* the recipe version.
- **Feature 138 institutional-continuity-infrastructure-formal-model** — the *formal model* of institutional continuity. Sausageos is the *informal* statement of feature 138's 9-node model (source → admitted meaning → warranted control → runtime authority → exact action → consequence → independent observation → reconciliation → examination).
- **Feature 139 stale-constraints-budgeted-verification-failures** — the *stale-constraint* problem. Sausageos's *FEFO* is the *what the verification might miss* (a stale expiration date in a non-FEFO discipline is a stale constraint); feature 139's verification budget is the resource.
- **Feature 141 krineia-five-invariants** — the *proof/record distinction*. Sausageos's *append-only stock ledger* is the *record*; feature 141's invariants are the *proof*.
- **Feature 145 garde-fous-frozen-mandate-append-only-agent-loop** — the *frozen mandate* primitive. Sausageos's *versioned recipes* are the *frozen mandate* (the recipe version is frozen at production-run start); the mandate is what the production-run holds fixed.
- **Feature 146 slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section** — the *JTBD framing*. Sausageos is the *production-ERP JTBD*; feature 146 is the *bookkeeping JTBD*. Both are operator-pain-driven.
- **Feature 147 reliability-lives-in-institution-not-cognition-2609-03192v1** — the *experimental test* of the architecture. Sausageos is the *informal* statement; feature 147 is the *experimental* test (preregistered refutations of the five properties).
- **Feature 148 coxswain-graphs-harness-owns-consequence-architecture-pattern** — the *one harness owns every consequence* pattern. Sausageos's *append-only stock ledger* is the *commit*; feature 148's *one harness* is the *one place where consequence is owned*.
- **Feature 149 personal-agent-blueprint-telegram-chokepoint-architecture-pattern** — the *authorization chokepoint* pattern. Sausageos's *versioned recipes* are the *what authorizes a production run* (the recipe version is the mandate); feature 149's *chokepoint* is the *enforcement of the authorization*.

The 18 picks (this one + 17 prior) form the **deepest single-vocabulary cluster in the 40-pass series** for the *append-only-ledger + production-ERP primitives* architectural pattern. **All 18 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only. The four sub-primitives that are *not* implemented in v1 (FEFO, lot-based costing, batch recall) are *future v2 surfaces* and would require:

- FEFO: a new `expires_at` field on `StockEntry` + a new ordering discipline on consumption queries.
- Lot-based costing: a new `Bill_line_item → StockEntry` link table + a new derivation query for cost.
- Batch recall: a new `recall_id` field on `MenuItem` + a new operational transition (`MenuItem.recall(actor, reason)`).

None of these are v1; all are v2 surfaces that would require an *owner decision* per charter §3.2.

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the sausageos production-ERP primitive set to `specs/2026-09-08-sausageos-production-erp-append-only-stock-fefo-versioned-recipes-HANDOFF.md`** as a named pattern set for the LE31 v1 codebase — already done in the HANDOFF.md.
2. **Wait for the first v1 surface that touches prepped-item stock** — trigger conditions: (a) first v1 PR that adds an `expires_at` field to `StockEntry`; (b) first v1 PR that adds a `Bill_line_item → StockEntry` link; (c) first v1 PR that adds a `recall_id` field to `MenuItem`; (d) first v1 PR that adds a *production-run* surface (which would link `MenuItem` to a `StockEntry` sequence).
3. **On trigger, evaluate the change against the sausageos primitive set** — does the change preserve *append-only stock ledger*? Does the change introduce FEFO discipline? Does the change add lot-based costing? Does the change add batch recall? The pattern set is the *what to verify*, not the *what to implement*.
4. **Future v2 surface (NOT v1)**: the four sub-primitives (FEFO, lot-based costing, batch recall, versioned recipes) are candidate v2 surfaces. Owner decision required: which sub-primitives, if any, should be added in v2? Each is a separate owner decision per charter §3.2.

## Telegram interaction if any

**None today.** The defer artifact is documentation only; no operator surface changes.

The **future v2 surface** (if the owner decides to add FEFO discipline) would: (a) add an `expires_at` field to `StockEntry`; (b) modify the cook Telegram bot's consumption query to order by `expires_at` ASC; (c) surface the FEFO ordering in the cook's view of the prepped-item queue. This is a *v2 surface*, not v1.

## Dependencies

- **GitHub access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.
- **Future v2 surface dependencies** (if FEFO / lot-based costing / batch recall are added): schema changes on `StockEntry`, `Bill`, `MenuItem`; new derivation queries; possible new operational transitions. All future; no v1 dependency.

## Open questions

1. **Which of the four sub-primitives (FEFO, lot-based costing, batch recall, versioned recipes) should be added in v2?** Owner decision required. Each is a separate charter §3.2 decision. The most operationally valuable is probably **FEFO** (perishables discipline) + **batch recall** (food-safety); the most technically valuable is probably **lot-based costing** (cost traceability). The cost in v1 today is *none of these* (the v1 prepped-item stock has a simple "current quantity" derivation, which is sufficient for a small restaurant's pre-FEFO operation).
2. **Is the sausageos 4-day-old 0★/0⑂ repo a credible production-traction data point?** Charter §3.2: stars are popularity proxy, not gate. The *primitive set* is the value, not the maintainer's track record. The 182 B description is tight; the topic tags are credible (`erp`, `manufacturing`, `htmx`, `postgresql`, `traceability` — all real production-ERP primitives). **The primitive set is transferable; the codebase is not adoptable**.
3. **Is the sausageos Django stack a blocking factor?** Stack mismatch (Django vs FastAPI) is the primary reason for the *no code adoption* decision. The *pattern* is portable; the *code* is not. If LE31 ever needs the sausageos primitives in code, they would be *re-implemented* on the LE31 stack (FastAPI + SQLModel + Postgres), not imported from sausageos.
4. **Should the LE31 v1 prepped-item stock add an `expires_at` field today?** Charter §3.2: only data needed for restaurant operations. The owner of a small restaurant knows when the prepped item will expire (the cook knows); the owner does not need the system to track expiration *automatically* (the cook is the system). Recommend: no, defer to v2 if/when the owner asks for FEFO discipline.

## Why this matters

**Sausageos is the most LE31-aligned primitive of the 40-pass series.** The four sub-primitives (append-only stock ledger, versioned recipes, FEFO, lot-based costing, batch recall) are the *production-ERP analog* of LE31's prepped-item stock. The 182 B README is the tightest single-paragraph production-ERP statement of the series; the 4-day-old 0★ repo is a new maintainer's first attempt at the pattern.

**The cluster (18 picks, this one + 17 prior) is the persistent cross-section reference for the next v1 architecture-review moment.** All 18 are `defer`; no code change today. The cluster is the *what the LE31 architecture is*, named across 18 different sources, and ready to be referenced when the first v2 surface lands (FEFO, lot-based costing, batch recall, or versioned recipes).

**The most operationally valuable future v2 surface is FEFO**: introducing an `expires_at` field on `StockEntry` + a FEFO ordering discipline on consumption queries would close the *perishables gap* (today, the cook tracks expiration manually; FEFO would surface the FEFO ordering in the cook's view of the prepped-item queue). Owner decision required; not v1.