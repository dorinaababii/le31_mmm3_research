# Feature 370 — `jdmacleod/kitchen-erp` self-hosted-household-kitchen-+-vendors-+-products-+-purchases-+-normalized-price-history-+-Decimal-money-+-append-only-facts (defer)

> **NEW observation (2026-10-24).** Documents in-window GitHub repo `jdmacleod/kitchen-erp` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★0/⑂0**, **8,283 KB**, **Python ✓ ON-STACK** (FastAPI + SQLAlchemy + PostgreSQL + Docker), created **2026-09-22 AND pushed 2026-10-23 = IN-WINDOW BY BOTH FIELDS**, `archived=false`, `fork=false`, 5 open issues, default_branch=`main`. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-24, not from search-result numbers. Description (verbatim from GitHub API): *"Self-hosted household kitchen system: vendors, products, purchases, and normalized price history. Decimal money, append-only facts, no required outbound calls."* Topics (verbatim): `cooklang, docker, fastapi, grocery, household, kitchen, ocr, postgis, postgresql, price-comparison, price-history, price-tracking, python, react, receipts, self-hosted, sqlalchemy, typescript`. Bucket: **v1 (exact-money + append-only-facts vocabulary)** — Pick A of Daily Research 2026-10-24. Build verdict: `defer` (parking-lot; **vocabulary reference only**).

## Goal

Retain the **"Decimal money, append-only facts, no required outbound calls"** triad as a persistent, externally-originated reference for LE31's own three hardest invariants — and, more narrowly, retain the observation that **an unrelated household-kitchen project states LE31's invariant set as its one-line house style.**

The triad maps, exactly:

| Their phrase | LE31 invariant | Charter |
|---|---|---|
| "Decimal money" | exact EUR, never binary floats | §3.6 / conventions *Money* |
| "append-only facts" | every stock change is a new `StockEntry`; never update or delete; current stock derived | §3.3 / §4.3 / conventions *Stock* |
| "no required outbound calls" | self-contained, no third-party service dependency in the core loop | §3.5 / conventions *Practicability* |

**No code today. The deliverable is the sentence, and the reminder that it was arrived at independently.**

## Scope

**In scope (defer artifact):**

- A written record of the triad above, with the source repo and its verbatim description attached.
- A written record of the **third phrase**, which is the one LE31 has *not* explicitly stated anywhere: LE31 says "self-contained" and "one VPS", but has never written *"no required outbound calls"* as a rule for its own core loop. That is a genuinely new phrasing of an existing constraint, and it is the phrasing this project uses.
- A decision record noting that this is the **first external project found that states all three of LE31's money/stock/independence invariants together in one sentence** — a second independent arrival at the same invariant set.

**Out of scope (defer artifact):**

- Any LE31 code, schema, or migration.
- Adopting the kitchen-erp codebase (its domain is a household pantry, not a restaurant floor).
- Vendor price history, purchase receipt OCR, Cooklang recipe parsing, price comparison, and PostGIS — all out of scope for LE31 v1, and three of them are new *roles* (§3.1 has two).
- Any price-tracking or cost-tracking feature. LE31 v1 records `method = cash | card`; it does not track what a dish *cost*.

## Description

`jdmacleod/kitchen-erp` is a self-hosted household kitchen system: vendors, products, purchases, and normalized price history. The transferable part is not the domain and not the code — it is the **one-line description**, which happens to be a compact statement of three invariants LE31 already holds:

1. **"Decimal money"** — a project with money in it (purchase prices, vendor costs) chose `Decimal` and said so *in its pitch*, not just in its code. LE31's §3.6 / conventions require exact EUR and forbid binary floats for the same reason. **The difference worth keeping:** LE31's money rule is currently written as a constraint in a charter and a conventions doc, where it is invisible to anyone reading the project. `kitchen-erp` puts the rule in the position where a reader meets the project first.
2. **"append-only facts"** — the same project, independently, chose an append-only fact model for its inventory movements. LE31's §3.3 says the same thing as "every prepared-item quantity change is a new `StockEntry`. Never update or delete ledger events. Current stock is derived from entries." **Two teams, one shape.** The additional nuance in their phrasing: *facts*, not *events* or *entries*. "Facts" connotes that history is immutable because it is true, not because a database constraint forbids mutation — a rationale LE31's charter does not give.
3. **"no required outbound calls"** — the phrase LE31 has never used. LE31's posture is described structurally ("single VPS + systemd unit is fine for v1", §3.2) rather than as a rule about outbound dependencies. Their phrasing turns an architectural accident into a stated requirement: *the system must not require calling anyone else*. That is exactly the property that makes LE31's Telegram cook surface viable — the cook's bot cannot depend on a third-party API being up. **This is the pick's genuinely new contribution: a constraint LE31 holds implicitly, stated in a form it could adopt verbatim.**

The **domain shift is severe and is recorded plainly**: a household pantry is not a restaurant floor. Vendors → suppliers is a third role, not a second. Purchases → receipts is a third entity, not a prepared-batch entry. Price history → food cost is a cost-accounting feature LE31 v1 explicitly does not have. **None of that code is adoptable; only the sentence is.**

## Data model

None shipped. The vocabulary implies: **Vendor** (supplier, third role — §3.1 conflict), **Product** (purchased good, distinct from `MenuItem`/`Batch`), **Purchase** (a money event — would need `Decimal` EUR + explicit tax handling per §3.6), **PriceObservation** (append-only fact, derived price history). LE31's own `StockEntry` remains the only ledger; this pick contributes **no table** and proposes no change to `backend/app/models.py`.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (all must hold):** (1) the owner asks for food-cost or supplier-price visibility; (2) a §3.1 decision adds the supplier role explicitly; (3) a v1 PR proposes any money-bearing write path, at which point the §3.6 exact-`Decimal` rule must be cited in the PR description.

## Telegram interaction if any

None today. Long-horizon note: if supplier-facing flows ever arrive, the cook bot is the wrong surface (suppliers are not staff) — but the **"no required outbound calls"** property is precisely what keeps the *cook* bot dependent only on LE31 itself. If a notification channel ever needs to reach a supplier, that outbound dependency must be explicitly optional, or it breaches this pick's third rule.

## Dependencies

None. No new packages, no schema migration, no infrastructure. (The upstream project uses FastAPI + SQLAlchemy + PostgreSQL, which is on-stack — but nothing is being adopted.)

## Open questions

1. **Should LE31's own architecture notes quote this triad?** This feature's recommendation says yes — as external prior art for §3.3 + §3.5 + §3.6. **Unmade owner decision.**
2. **Is "no required outbound calls" a rule LE31 wants stated explicitly?** It is currently implicit in the single-VPS posture. Making it explicit would change what a future feature may propose.
3. **Does LE31 ever want supplier/purchase data?** §3.2 excludes online ordering and payment gateways; §3.1 names two roles. A supplier role is unmade and has been left unmade across 86 passes.

## Why this matters

Because it is **the cheapest available evidence that LE31's money and stock rules are the right rules** — and LE31 has never had evidence of that kind from outside itself. Every prior invariant confirmation has been internal: LE31 decided, LE31 wrote it down, LE31 obeyed it. This pass found a household-pantry project in a different country, for a different domain, with a different stack in places, whose author independently wrote *"Decimal money, append-only facts, no required outbound calls"* as the description of the project.

**That is prior art.** It does not prove LE31's rules are correct — a household pantry is not a restaurant, and the failure modes differ. But it does establish that the combination is a *natural* way to describe a money-and-stock system, which is exactly the property a charter invariant should have. If LE31's invariants had looked arbitrary to an outside builder, that builder would have chosen something else.

The narrow deliverable: **quote the sentence.** It costs one line in an architecture note and it converts three charter constraints from "rules we wrote" into "rules with prior art."

## Cross-section

Features 15 (`inventory-variance`), 259 (`CtrlAltDevelop/ledger-service` — double-entry + append-only + idempotent), 290 (`AlvaroVerona/prime-cost` — restaurant P&L / food-cost), 331 (`joshnivek/sudo-hotel-night-audit-automation` — exact money), 297 (`jonalemndi2/ALdia` — inventory + immutable audit trail). The price/cost dimension is already covered by features 290 and 331; what is **new** here is the explicit "no required outbound calls" phrasing. GitHub `jdmacleod/kitchen-erp` is unique vs features 1–369 (verified by ripgrep against `features/`, `specs/` and `INDEX.md`). Fully reversible — documentation-only artifact.
