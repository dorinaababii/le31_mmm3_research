# Feature 395 — `Pantry Signal`: stock is three quantities, not one — on hand, reserved, and available

> **Pick B of Daily Research 2026-10-28 (90th pass).** Documents in-window GitHub repo `fortikday/pantry-signal` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★0/⑂0 — no traction evidence in either direction**, **1,255 KB**, **Python ✓ ON-STACK**, created **2026-10-22T10:51:24Z AND pushed 2026-10-22T11:41:42Z = IN-WINDOW BY BOTH FIELDS**, 0 topics, `default_branch=main`, `archived=false`, `fork=false`, 0 open issues). All field values read from a **direct `/repos/` GET** by the parent on 2026-10-28 (`/tmp/le31-daily-2026-10-28/gh/pv/fortikday__pantry-signal.json`), **not from search-result numbers**. Description (verbatim): *"Local restaurant prototype: independent kitchen orders, recipe-based stock estimates, delivery batches, and waste tracking. Python, MIT licensed."*
>
> **The README was read in full** (parent, 2026-10-28, `/tmp/le31-daily-2026-10-28/gh/readmes/fortikday__pantry-signal.md`, 151 lines). Four claims are recorded below, verbatim: the three-quantity stock model (*"**On hand** … **Reserved** … **Available**"*); the honesty about estimates (*"This is an estimate and **can become negative when records are incomplete**"*); the replay guarantee (*"**Replaying an event cannot deduct stock again.**"*); and the request-identity guarantee (*"An order request ID also protects against duplicate order submission."*).
>
> Bucket: **v1**. Verdict: **`defer`** (vocabulary only). **0 build time.**

## Goal

Record in LE31's vocabulary the distinction between **three** stock quantities — what is **on hand**, what is **reserved** against a queued order, and what is therefore **available** to promise to a new order — a distinction LE31 cannot currently express, because LE31 keeps a **single** number.

The concrete outcome: **one document stating that a stock figure is not one number, and naming which three numbers LE31 would need and why one column cannot hold them.**

## Scope

**In scope (v1, defer):**

- **One document** recording the three-quantity model with the verbatim quotes, the source URL, and the LE31-side vocabulary each one names.
- **One explicit statement of the relationship to feature 374** — this is a **refinement** of 374's question, not a replacement, and the two are orthogonal.
- **One explicit statement that this feature does NOT own the negative-balance question** — that belongs to feature 394 (Pick A of the same pass), which records it as an unmade charter decision.

**Explicitly NOT in scope:**

- **Any `Batch` column, model, or migration.** `Batch.qty_remaining` is **feature 374's** subject (stored-vs-derived), and this feature changes nothing about it.
- **Any `Reserved` / `Available` / `OnHand` model.** This feature names the concepts; it does not build them.
- **Any recipe, ingredient, BOM, or waste model.** LE31 has **no recipe or ingredient concept at all** (`grep -rn -i "recipe|ingredient|bom" backend/app/` → **no output**), and this feature does not introduce one. `Pantry Signal`'s recipe arithmetic is out of LE31 v1 scope.
- **Any change to `backend/app/`.** Zero lines of application code change.
- **Any adoption of `Pantry Signal`'s two-service architecture.** See "Description" — the architecture is **explicitly rejected**, only the vocabulary transfers.
- **Any change to the FastAPI / SQLModel / Postgres pins.**
- **Any delivery, delivery-batch, or waste-tracking feature.** All out of v1 scope.

## Description

### What `Pantry Signal` actually is

A **local, two-service restaurant prototype**: an order service (port 8770, `local/orders.sqlite3`) and a separate inventory service (port 8771, `local/inventory.sqlite3`). *"The runtime has no external packages."* It runs a **Table 7** walkthrough: load fictional ingredient batches, order a Caesar salad with chicken and shrimp, watch the kitchen ticket appear, let the inventory service reserve the recipe quantities, then start preparing so the reservation becomes recorded usage and the chicken goes from 5,000 g to 4,600 g on hand with no reservation left.

**There is no traction claim here and none is made.** ★0, 0 open issues, no topics, a two-day-old repository, and the README says so itself: *"**This is a demonstration, with fictional recipes and optional fictional deliveries.** It has no connection to a real restaurant, payment terminal, or live AI model."* It also reports its own test count honestly — *"The current version passed **147 automated checks**: 89 domain, 18 HTTP, and 40 front-end behavior tests on 22 October 2026"* — and states plainly: *"There is no claim of measured waste savings or proven business demand."*

### The three-quantity model — the reason this pick exists

The README's "Stock and dates" section is the whole substance of this pick:

> *"**On hand:** received grams minus recorded recipe usage and logged waste. This is an estimate and can become negative when records are incomplete.*
>
> ***Reserved:** ingredients required by queued orders not yet prepared or cancelled.*
>
> ***Available:** a conservative estimate using dated batches, on-hand balance, and reservations. Batches past their recorded date or without a date are excluded."*

**LE31 has none of these three.** Parent-verified on 2026-10-28:

```
$ grep -rn -i "reserved\|available\|on_hand\|on hand" backend/app/
backend/app/models.py:65:    __tablename__ = "table_"  # 'table' is a SQL reserved word
```

The single hit is the word *"reserved"* inside a **SQL comment** about the word `table` being a reserved SQL keyword. **There is no reserved-stock concept in LE31.** LE31's `Batch` has `qty_start` and `qty_remaining` — **one** number, which feature 374 argues should not even be stored.

**And the single number cannot express the difference.** If two orders are queued against the same batch of tiramisu, `qty_remaining` is a single value that does not distinguish *"8 tiramisu are physically in the fridge"* from *"4 are physically there and 4 are promised to a table that has already ordered them"*. The first is what the kitchen can sell; the second is what a new order can be promised. **A restaurant that treats them as the same number oversells**, and a restaurant that treats them as different needs **two** numbers where LE31 has **one**.

### Why this is a refinement of feature 374, not a replacement

Feature 374 (`le31-qty-remaining-derived-not-stored-…`) asks: *"should `qty_remaining` be **stored**?"* and argues it should be **derived** from the `StockEntry` ledger (§3.3).

This feature asks a **different and orthogonal** question: *"**how many** quantities are there?"* — and answers **at least three**.

The two questions point the same direction — toward **deriving** rather than storing — but answering only one leaves the other open:

- If LE31 derives `on_hand` from `StockEntry` and **stops there**, it has solved 374 and still cannot say what is *promisable*.
- If LE31 derives all three, it has solved both, and 374's argument applies to each.

**Both features must be read together.** 374 is not superseded, and this feature does not pre-empt it.

### The replay-safety half — a second, smaller claim

> *"The order service commits each kitchen change and its event together in `local/orders.sqlite3`. The inventory service reads those events over HTTP and updates `local/inventory.sqlite3`. **Each event is applied once in the same transaction as its saved cursor. Replaying an event cannot deduct stock again.**"*
>
> *"An order request ID also protects against duplicate order submission."*

LE31's `StockEntry` has `at: datetime` and **no monotonic event cursor** — parent-verified: `grep -rn -i "cursor\|replay\|offset\|sequence" backend/app/` → **no output**. LE31 is single-service, so it does not face the distributed-replay hazard that `Pantry Signal` is built to survive, and this feature makes **no claim that it does**. But the *property* — *"each event is applied once"* — is exactly the property LE31 would need to **assert** if it ever grows a second reader of the ledger (a reporting job, an export, a bot-side projection). **Recorded as a forward-looking vocabulary item**, not as a present gap.

### ⭐ The architecture is explicitly rejected

`Pantry Signal` is a **two-service, event-over-HTTP, locally-hosted prototype**. LE31 is **one service** with one Postgres (§3.5's stack: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres in production).

Copying this architecture would mean introducing a service boundary, a cursor, and an HTTP hop between the order and the inventory — **for no v1 benefit**, and at a real cost in operational simplicity for a one-restaurant product whose entire premise is that the owner can run and understand it. **The transferable part is the vocabulary — three quantities — not the architecture.** This is recorded explicitly so the pick is not mistaken for an architecture recommendation.

### A genuine duplicate, explicitly NOT re-picked

**Feature 269** (`D-L-Narayana-stockline`, 2026-10-09) already records *"Atomic stock reservation, idempotent orders, optimistic locking, append-only ledger"* — i.e. the **reservation** half is already in LE31's tree as a vocabulary reference.

This pick is **not** a re-pick of that. What `Pantry Signal` adds, and what feature 269 does not contain, is the **three-way distinction** and the honest handling of the **estimate** quality flag (*"This is an estimate and can become negative when records are incomplete"*). Feature 269's reservation is a **write-side** concern (claiming stock atomically); `Pantry Signal`'s triad is a **read-side** concern (reporting three different facts about the same stock). **Both are needed, and they are not the same feature.**

### The recipe-dependency, stated honestly

`Pantry Signal`'s quantities are denominated in **grams of ingredients**, because it is a **recipe-driven** system: *"Sample chicken quantity: **400 g**"*, *"three lattes consume 54 g of coffee and 600 ml of milk"*.

**LE31 has no recipe or ingredient concept at all** — parent-verified: `grep -rn -i "recipe|ingredient\|bom" backend/app/` → **no output**; `MenuItem` has no recipe link. LE31's stock is denominated in **prepared-item units** (`Batch` = *"8 pieces of Tiramisu, prepared 09:00 today"*).

So the triad as `Pantry Signal` states it is **not directly portable**: it is expressed over ingredients, and LE31's model is over prepared items. **The concept transfers; the denominators do not.** This is the same structural caveat that put feature 390 (`Pantry`'s recipe-consumption snapshot) **behind feature 359** (recipe-linked depletion) — and it is recorded here for the same reason. **This feature is filed at `defer` precisely because it names a question whose implementation depends on a recipe model LE31 does not have.**

## Data model

**No data model change. This feature changes zero lines of `backend/app/models.py`.**

The *shape* it is recording — **explicitly not proposed as an implementation today**, and expressed in LE31's own denominators (prepared-item units, not grams):

```
For a given batch:
  on_hand    := SUM(StockEntry.qty_delta WHERE batch_id = X)          -- what physically exists
  reserved   := SUM(qty promised to queued, not-yet-prepared orders)   -- committed to an order
  available  := on_hand - reserved                                    -- what can be promised anew
```

**The open question this feature deliberately does not answer:** how `reserved` is *represented* in an append-only ledger where §3.3 forbids updating or deleting entries. A reservation is **not** a stock movement — it is a **claim on a future movement** — and the correct ledger representation of that is a separate question (a distinct `reason` value with a sign convention? a separate table? a derived join over `OrderItem`?). **Recorded as an open question, not decided here.** It is adjacent to, but not the same as, feature 394's negative-balance question.

## Implementation

**No implementation steps. This feature is a `defer` vocabulary artifact.**

For reference only, what a future implementer would need to decide (recorded so the shape is not lost, **not** as this feature's scope):

- **The denominators**: LE31's triad would be over **prepared-item units**, not ingredients — so it depends on the recipe model (feature 359) that LE31 does not have.
- **The ledger representation of a reservation** under §3.3's append-only rule.
- **The derivation site**: a query or a view over `StockEntry`, not a stored column — consistent with feature 374's direction.
- **The quality flag**: how the surface distinguishes *"available"* from *"available as an estimate"*, which `Pantry Signal` handles by marking quantities as a *"last estimate"* with *"muted numbers and a warning beside them"*. LE31 has no equivalent flag today.

## Telegram interaction

**None. No bot, no command, no surface change.**

Rationale: the triad is a **read-side reporting** concept. LE31's two operational surfaces are the waiter web UI and the cook Telegram bot. A future owner-facing "how much is actually sellable" view would be a **new surface**, and §3.1 names exactly two surfaces — so **adding one requires its own charter decision and its own gate run from scratch**. This feature does not create it, and it is **not** bundled with one.

The **cook bot** *could* eventually consume the "available" figure (a cook asking what can still be promised), but that is a separate proposal. **Recorded, not picked.**

## Dependencies

- **Feature 374** (`le31-qty-remaining-derived-not-stored-charter-4-3-vs-schema-contradiction-first-party-…`) — **read first**. It owns whether `qty_remaining` is stored or derived. This feature is a **refinement of the same area, not a replacement** — both point toward deriving, and 374 must not be re-answered here.
- **Feature 359** (recipe-linked depletion) — **the hard dependency**. `Pantry Signal`'s quantities are denominated in ingredients; LE31's are denominated in prepared-item units. Until a recipe/ingredient model exists, LE31's triad can only be stated abstractly.
- **Feature 385** (`le31-order-item-batch-provenance-first-party-…`) — batch provenance. It owns *"which batch did this sale hit"*, which is the **write-side** counterpart of the triad's read-side.
- **Feature 394** (Pick A of the same pass) — owns the **negative-balance question**. `Pantry Signal` is one of the two artifacts in conflict; this feature **references** it and **does not re-answer** it.
- **Feature 269** (`D-L-Narayana-stockline`) — the reservation vocabulary, already in the tree. **Not re-picked.**
- **Feature 15** (`inventory-variance`), **feature 03** (`kitchen-stock-tracker`) — adjacent stock surfaces.
- **Charter §3.3** (stock is derived from entries; entries are never updated or deleted), **§3.1** (two named surfaces), **§3.2** (fixed stack; no recipes/ingredients in v1 scope).
- **`skills/le31-conventions/SKILL.md`** — the seven-check gate.

## Open questions

1. **⭐ How is `reserved` represented in an append-only ledger?** A reservation is a **claim on a future movement**, not a movement. §3.3 forbids updating or deleting entries. A distinct `StockReason` with a sign convention? A separate table? A derived join over `OrderItem`? **Undecided.**
2. **Can the triad exist at all before there are recipes?** LE31's stock is over prepared items; `Pantry Signal`'s is over ingredients. **Is a prepared-item-level triad meaningful without recipes** (e.g. "8 tiramisu, 3 reserved to table 4, 5 available")? Probably yes — but that is LE31's own formulation, not the artifact's, and it should be recorded as LE31's, not borrowed.
3. **What is the quality flag?** `Pantry Signal` marks quantities as a *"last estimate"* when its background sync is stale, and warns before comparing a physical count. LE31 has no staleness concept for derived stock. **Undecided.**
4. **Does `reserved` need to be visible to the waiter at all**, or is it only an owner-facing concept? (A surface-count question, §3.1.)
5. **Should a physical count be a `StockEntry` or a comparison artifact?** `Pantry Signal` answers: *"Record a measured stock count to compare it with the estimate at that moment. The count saves an unexplained difference; **it does not change the stock ledger**."* That is a clean rule and a candidate §3.3 clarification — **recorded, not adopted.**

## Why this matters

**Because a single number cannot answer the question a restaurant actually asks.**

The owner's question is not *"how many do I have?"* — it is *"how many can I still promise?"* Those are different numbers the moment a single order is queued, and LE31 currently has **no way to express the difference at all**. A restaurant that sells a dish against `qty_remaining` alone will, on a busy evening, promise the last portion to two tables.

**The cost profile is favourable and the timing is good:**

- **Cheap now:** one vocabulary decision, and — once a recipe model exists — a derived view rather than a stored column.
- **Expensive after:** if the first selling path ships against a single `qty_remaining` and the reservation concept is added later, then **every historical sale** is ambiguous about whether it consumed reserved or unreserved stock, and the ledger — which is append-only, so the ambiguity is permanent — would have to be *interpreted* rather than *read*. LE31's own `StockEntry` already carries `ref_order_item_id` (line 124), so the order line is reachable from the ledger; but **whether the order was reserved at all is not**, and that is a fact about time that cannot be recovered later.

**And the artifact is honest in a way that makes it useful as a reference.** It does not claim waste savings or proven demand; it says its numbers are estimates that *"can become negative when records are incomplete"*; and it says its architecture is a local prototype that *"does not manage opening dates, storage temperatures, preparation yields, or prepared subrecipes."* **A reference that states its own limits is worth citing; one that claims more than it has is not.**

## Evidence

- **Evidence class:** **reported**, confidence **medium** for the shape, **low** for LE31's need. ★0, no traction, self-described demonstration with fictional data.
- **Raw artefacts:** `/tmp/le31-daily-2026-10-28/gh/pv/fortikday__pantry-signal.json`, `/tmp/le31-daily-2026-10-28/gh/readmes/fortikday__pantry-signal.md`.
- **Report:** `/opt/data/le31-daily-research-2026-10-28.md`.
- **Parent verification scripts:** `/opt/data/le31-verify-2026-10-28/rederive.py`, `rank.py`.
