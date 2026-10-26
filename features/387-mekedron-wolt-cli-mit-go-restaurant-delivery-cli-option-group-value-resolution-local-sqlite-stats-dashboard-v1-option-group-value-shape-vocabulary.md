# Feature 387 — `mekedron/wolt-cli`: the option group/value shape, independently arrived at from the client side — and one vocabulary point LE31 has not written down

> **NEW observation (2026-10-26).** In-window GitHub repo `mekedron/wolt-cli` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE in principle**, but **Go ✗ OFF-STACK** for LE31's Python 3.13 / FastAPI / SQLModel / Postgres stack), **★36/⑂7**, **12,086 KB**, created **2026-02-22T00:00:00Z** and pushed **2026-10-25T00:00:00Z** = **in-window by `pushed_at` ONLY** (created 7 months before the 2026-09-26..2026-10-26 window start — **this is not a fresh discovery**). All field values read from a **direct `/repos/` GET** by the parent on 2026-10-26, never from search-result numbers. Description (verbatim from GitHub API): *"Free & Open Source CLI for Wolt: discover venues, inspect menus and options, manage carts, and preview checkout from the terminal."*
>
> Bucket: **v1 (menu-data + price-provenance vocabulary)** — Pick C of Daily Brainstorm 2026-10-26. Build verdict: **`defer`** (parking-lot; **vocabulary reference only** — no code changes, no schema change).
>
> ⚠️ **This repo was ALSO seen in today's daily-research report** (2026-10-26) as a *local-first* example alongside `RM15-Refunders/StockLink`, and **was not picked** by that pass — the research pass filed `dc-tech-inc/dotnet-pos-integration` (382), `huryoungkil-ops/cafe-sales-alert` (383) and `ifedayofakayode/spice-route-restaurant-dashboard` (384). **No feature file exists for `wolt-cli` in the repo as of this writing** (`ls features/ | grep -i wolt` → 0 hits). This is a **first filing**, not a re-pick.

## Goal

Retain `mekedron/wolt-cli` for **two** transferable shapes, and turn each into one written sentence in LE31's own documentation:

1. **The option group/value shape** — the same gap feature 386 names, arrived at from the opposite end of the stack. Two independent authors, one shape.
2. **The price-provenance distinction** — the reference separates *"the price the venue lists"* from *"the price this cart will be charged"*, and LE31 has never written down whether its `unit_price` snapshot is one or the other.

## Scope

**In scope (v1 — documentation only):**
- One sentence in LE31's menu-data boundary recording the **option group/value** shape as the convergent external shape (cross-reference feature 386 — **do not re-argue the gap**).
- One sentence in LE31's pricing boundary recording the **listed-price vs charged-price** distinction as a question LE31 has not answered.

## Out of scope (v1)

- **Any schema change.** No `Option`/`OptionGroup`/`Modifier`/`Variant` model. No `Cart`/`CartItem` model. **LE31 has no cart** and this feature does not propose one.
- **No `MenuItem` or `OrderItem` field of any kind.**
- **No integration with Wolt or any delivery platform.** `wolt-cli` is an **unofficial community client** — its own README says *"It is not affiliated with Wolt. Use it at your own responsibility."* **LE31 is not a Wolt integration and this feature does not propose one.** The value is the *shape*, not the integration.
- **No local-SQLite dashboard.** The reference's "sync your own order history into SQLite and serve a dashboard at `127.0.0.1:5173`" is **not** a proposal for LE31. LE31 is server-authoritative over Postgres (§3.2).
- **No CLI, no terminal surface.** LE31's surfaces are a waiter web UI and a cook Telegram bot (§3.1).
- **No adoption of `wolt-cli`'s code.** MIT makes it legally adoptable; Go is off-stack, and the interesting part is a two-field naming convention, not an implementation.
- **No token handling, no auth, no scraping.** Not proposed, not relevant.

## Description

### What the source actually says

`wolt-cli`'s README, read raw by the parent on 2026-10-26, states in its feature list:

> *"venue details, menus (with `--query` / `--category`), hours, and item drilldown"*
> *"**option matrix inspection and option resolution by name** (`--option "Drink=Cola"`)"*

and, in the worked cart example:

```bash
# 4a) Add by item id with explicit option ids (most precise)
wolt cart add burger-king-finnoo <item-id> \
  --option "<drink-group-id>=<drink-value-id>" \
  --option "<side-group-id>=<side-value-id>" \
  --count 1

# 4b) Add by name with option values resolved by name (most ergonomic)
wolt cart add burger-king-finnoo --query "WHOPPER Meal" \
  --option "Drink=Coca-Cola Zero" \
  --option "Side=Fries L" \
  --count 1
```

and, on the local stats feature:

> *"local stats dashboard (`wolt stats`) — fetches a pre-built bundle, syncs your order history into SQLite, serves the dashboard at `http://127.0.0.1:5173`, and opens the browser. No Node.js required at runtime."*

### Shape 1 — the option group/value pair (cross-reference feature 386)

The reference's option vocabulary is exactly two levels, and the naming makes the levels explicit:

| Level | Example from the source | What it is |
|---|---|---|
| **group** | `Drink`, `Side` | *which kind of choice this is* |
| **value** | `Coca-Cola Zero`, `Fries L` | *which choice within that kind* |

The resolution syntax (`Drink=Coca-Cola Zero`) and the id syntax (`<drink-group-id>=<drink-value-id>`) are **the same shape** — the ergonomic path and the precise path differ only in whether the identifiers are names or ids. **That is the transferable observation: an option choice is a (group, value) pair, not a bare string.**

This is the **same two-level shape** `mighty840/kitchenasty` expresses as *"Options … per item"* (feature 386) — arrived at by a different author, in a different language, on the opposite side of the stack (a full restaurant ERP vs. a terminal client for a third party's API), in the **same 30-day window**.

**LE31's own schema has no option concept at all**: `grep -rn -i "option|variant|modifier" backend/app/models.py` returns **no output**. `OrderItem` carries `qty` and one `unit_price` and nothing else. **Feature 386 owns that gap; this feature does not re-open it.**

### Shape 2 — listed price vs charged price (the part LE31 has not written down)

The reference separates two prices, and its own naming makes the separation visible:

- the **venue's** item list, with the price the venue publishes (read from the discovery feed);
- the **cart's** own projection — the reference calls it *"checkout projection (`checkout`, no order placement)"*, i.e. a **projection of what would be charged**, computed from the cart including its option choices, and explicitly **not** an order.

Two things are being said here that LE31 has never said:

1. **A cart total is a projection, not a fact.** It is derived from the cart's contents plus the chosen options. It is not the order, and the reference is careful to never place the order — *"Final order placement still happens in the official Wolt app/website."*
2. **The listed price and the charged price are different facts, and the difference is exactly the options.** The gap between them is the option set.

**How this lands on LE31.** LE31's `OrderItem.unit_price` is a snapshot of `MenuItem.unit_price` taken at order time. That is correct — prices move, and a historical order must keep the price it was sold at. **But LE31 has never written down *which* price `unit_price` is:** the *listed* price of the product, or the *charged* price for the product-as-ordered (which, once options exist, may differ).

**Why this matters more than it looks.** `DerivedTip` is computed as `total_paid − (subtotal_items + subtotal_tax)` — so **`subtotal_items` is derived from the order lines' `unit_price`.** If `unit_price` is the *listed* price and the customer chose a *more expensive* option, then the bill is arithmetically self-consistent but **describes a transaction that did not happen**, and the tip is derived from a wrong base. LE31's §3.6 treats money as exact; exact arithmetic over a wrong quantity is still wrong. **This is the money bug feature 386 names, seen from the price side.**

Note carefully: **this is not a defect in LE31 today** — because LE31 has no options, `unit_price` and "the price charged" are the same number by construction. **It is a latent definitional gap that becomes a defect the moment options exist.** Recording it now costs one sentence; discovering it after the first option lands costs a bill audit.

## Data model

**No change.** This is a documentation-only artifact.

For the record, and **explicitly not proposed here**, the two shapes the source points at:

```
OptionGroup        (id, name)              -- e.g. "Drink", "Side"
OptionValue        (id, group_id, name)    -- e.g. "Coca-Cola Zero", "Fries L"
OrderItemOption    -- the (group, value) pair chosen on an order line
```

and the price distinction:

```
MenuItem.unit_price       -- the LISTED price of the product
OrderItem.unit_price      -- the price actually charged for the ordered thing
                           -- equal to the listed price only while there are no options
```

**Neither is written into LE31's schema by this feature.** Feature 386 owns the option-shape question; this feature adds the **price-provenance** sentence, which is a genuinely different question.

## Implementation steps

1. **One sentence** recording the option group/value shape as the **convergent external shape**, with a pointer to feature 386 as the owner of that gap. **Do not re-argue it** — one reference, one line.
2. **One sentence** recording the listed-price vs charged-price distinction as a question LE31 has not answered, and pointing at `DerivedTip`'s dependence on `subtotal_items` as the reason it is not academic.
3. **Record the evidence class honestly**: the price distinction is **inferred** from an external artifact's CLI shape. **No owner has reported a pricing or options problem.** LE31's owner may sell a menu where every dish has one price, in which case none of this matters.

## Telegram interaction if any

**None.** No command, no output, no prompt.

## Dependencies

- **Feature 386** (`mighty840/kitchenasty` — the menu-item options vocabulary) — **the owner of the option gap.** Read it first; this feature is the second half of one idea, not a second idea.
- **Feature 10** (`10-allergen-tracking.md`) — unrelated to this feature; listed only because `wolt-cli`'s menus expose options and a real menu has both. **Not a dependency.**
- **Feature 14** (split tender) and **feature 05** — own payment splitting. **Not a dependency.**
- **`DerivedTip`** — the dependent record whose correctness this feature's second sentence is about. **Not a dependency** (nothing is being changed); the dependency is *conceptual* and is why the sentence is worth writing.

## Open questions

- **Is LE31's `unit_price` the listed price or the charged price?** **Currently indistinguishable** — and that is the point. The question becomes answerable only when options exist. **Recorded as a question, not answered.**
- **Does the owner sell any dish with a choice?** Unknown; feature 386 records the same unknown.
- **Should a cart exist in LE31?** The reference has a cart. **LE31 does not, and this feature does not propose one** — a cart is a §3.1 surface question and a §3.4 explicit-transition question, and neither is settled. **Recorded as out of scope, deliberately.**
- **Do LE31's future customers arrive through a delivery platform?** The reference's whole domain is "a consumer ordering from Wolt". LE31 is a venue-side system. **The overlap is the menu vocabulary, not the business.** Recorded so the next pass does not treat this as a delivery-platform integration opportunity.

## Why this matters

**Two independent authors, one shape, opposite ends of the stack, one window.** `kitchenasty` (feature 386) is a restaurant system that chose to model options per item; `wolt-cli` (this feature) is a terminal client that chose to resolve options as `group=value`. **Neither is LE31, neither is LE31's stack, and neither is talking to LE31.** They agree with each other about the shape of a menu choice, and LE31 has no such shape at all.

That convergence is the entire reason this is filed. **One author is a preference; two independent authors is a shape** — the same standard the series applied to `mesa-lite`'s three-authors-in-one-window no-dependency finding.

**But the more useful half of this pick is the price sentence, not the options sentence.** The options shape is already feature 386's. The price-provenance distinction is **new**, it is **LE31's own**, and it is the kind of thing that is cheap to write down and expensive to discover:

> LE31's `DerivedTip` is *derived* from `subtotal_items`, which is derived from `OrderItem.unit_price`. **A well-typed, exactly-computed money value, derived from a quantity whose meaning was never defined.** The moment a line can be "the product, plus a choice", that quantity has two defensible meanings and the code picks one **by accident** — because there was no sentence saying which.

**That is the third instance in three days of the same shape of finding** — LE31 has a correct-by-accident value that will stop being correct when a feature lands — and the reason this pass files it as a vocabulary reference rather than leaving it for whoever eventually builds options. **A boundary that is written down is a decision; a boundary that is merely absent is an accident.**

## Adjacent evidence

- **`kodlyft/xpos`** (MIT, ★51, **TypeScript/Vue on Frappe+ERPNext ✗ OFF-STACK**, in-window by push only) — the repo whose README line *"**Batch & serial tracking** – Select specific batch/serial numbers during sale or return"* triggered **feature 385**, today's first-party finding. It is **not** a pick of this pass. Recorded here because it and `wolt-cli` are the two restaurant-shaped MIT repos read in full today, and they name the two halves of the same operational reality: **which batch was consumed** (385) and **which variant was chosen** (386/387).
- **Today's daily-research pass** also saw `wolt-cli` and filed `RM15-Refunders/StockLink` and `dc-tech-inc/dotnet-pos-integration` instead. **No overlap in picks** — feature 382 (shortfall/idempotency) is a different question from feature 386/387 (menu shape) and from feature 385 (batch provenance).
- **`features/10-allergen-tracking.md`** — owns allergens. `kitchenasty` names allergens too; **that half is a duplicate and was not picked** (see feature 386's "Adjacent evidence").
- **`features/14` (split tender), `features/05`, `features/22`** — own payments and reservations. **Not re-picked.**
