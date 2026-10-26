# Feature 386 — `mighty840/kitchenasty`: menu-item **options** as a first-class concept — the third gap in LE31's `MenuItem` model

> **NEW observation (2026-10-26).** In-window GitHub repo `mighty840/kitchenasty` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE in principle**, but **TypeScript/React/Express/Socket.IO/Prisma ✗ OFF-STACK** for LE31's Python 3.13 / FastAPI / SQLModel / Postgres stack), **★58/⑂29**, **27,508 KB**, created **2026-02-18T00:00:00Z** and pushed **2026-10-05T00:00:00Z** = **in-window by `pushed_at` ONLY** (created 7 months before the 2026-09-26..2026-10-26 window start — **this is not a fresh discovery**). All field values read from a **direct `/repos/` GET** by the parent on 2026-10-26, never from search-result numbers. Description (verbatim from GitHub API): *"A self-hosted restaurant online ordering, table reservation, and management system. KitchenAsty enables restaurants, cafes, and takeaways to accept online orders for delivery and pickup, manage menus, handle table reservations, and run operations from a single admin panel"*.
>
> Bucket: **v1 (menu-data vocabulary)** — Pick B of Daily Brainstorm 2026-10-26. Build verdict: **`defer`** (parking-lot; **vocabulary reference only** — no code changes, no schema change).

## Goal

Retain `mighty840/kitchenasty` as a **second independent external arrival at the same menu-data gap**, and turn it into **one sentence in LE31's own documentation**.

The gap: **LE31's `MenuItem` model cannot express an option.** Not a size, not a doneness, not a side, not an "with / without". A tiramisu in LE31 is exactly one thing with exactly one price. In every restaurant LE31 targets, it is at least two things with two prices, and the price is **decided at order time**.

## Scope

**In scope (v1 — documentation only):**
- One sentence in LE31's menu-data boundary: LE31's `MenuItem` describes **a product**, and LE31 does **not yet** describe **a product's variants**. A line on an order is currently `MenuItem × qty` at a single `unit_price`.
- One sentence recording **which** gap this is and **which** it is not — see "Adjacent evidence" below, because this gap has two confusingly similar neighbours and confusing them would waste the next pass's time.

## Out of scope (v1)

- **Any schema change.** No `Option`, `OptionGroup`, `Modifier`, `Variant` or `MenuItemOption` model is added by this feature. **The column does not exist and this feature does not add it.**
- **No `MenuItem` field of any kind is added or changed.** (Including allergens — see "Adjacent evidence"; feature 10 already owns that and the allergen half of this pick's source is therefore **recorded as a duplicate, not picked**.)
- **No waiter's UI, no order-taking change, no Telegram command, no pricing change.**
- **No adoption of `kitchenasty`'s code.** MIT makes it legally adoptable; it is a different stack, a different product surface (customer-facing online ordering with delivery/pickup, not a table service), and its option model is tied to its storefront. **The transferable content is the vocabulary, not the markup or the schema.**
- **No customer-facing ordering surface.** Feature 11 (`11-customer-qr-menu.md`) owns that and it is not re-picked.
- **No reservation feature.** Feature 22 and the reservation work own that; `kitchenasty` has reservations, and that half of its README is **not** what this pick is about.
- **No `Socket.IO`/WebSocket adoption.** §3.2 defers WebSockets; feature 375 builds on the polling model. `kitchenasty`'s "real-time WebSocket updates" is **explicitly not** a proposal to change LE31's transport.

## Description

### What the source actually says

`kitchenasty`'s README, read raw by the parent on 2026-10-26, states under **Menu & Kitchen**:

> *"Category management with nesting and menu item CRUD"*
> *"**Options, allergens, and mealtime tagging per item**"*
> *"Image uploads (JPEG/PNG/WebP/GIF, 5 MB max) with preview"*
> *"Stock tracking with automatic availability updates"*

and under **Ordering & Payments**:

> *"Online ordering with delivery/pickup, scheduling, and guest checkout"*
> *"Stripe payment integration with webhooks, plus cash-on-delivery"*

and under **Features → Kitchen display** (line 65):

> *"**Kitchen display — live Kanban board with one-click status progression**"*

### The gap in LE31's own schema, as observed

`backend/app/models.py`, read by the parent on 2026-10-26:

```python
class MenuItem(SQLModel, table=True):
    __tablename__ = "menu_item"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    category: str
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    unit: str = "piece"
    is_prepared: bool = True
    photo_url: str | None = None
```

**There is no option concept.** `grep -rn -i "option|variant|modifier" backend/app/models.py` returns **no output at all** — not a field, not a comment, not a stub.

And on the order line:

```python
class OrderItem(SQLModel, table=True):
    ...
    qty: int = 1
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
```

`OrderItem` records a quantity and **one** price. `unit_price` is a *snapshot* of `MenuItem.unit_price` at order time (correctly — prices move), but there is **nowhere to record which variant was chosen**, because there is no variant.

### Why this is a real gap and not a nitpick

**The price is decided at order time in every restaurant LE31 targets.** "Tiramisu", "8", "€6" is not a sufficient order line. "Tiramisu", "1", "€6" + "size: large" + "no walnuts" is. The moment LE31 serves a restaurant with a menu where any dish has a choice, the order line has to carry the choice — and today it has nowhere to put it.

**The tempting wrong answer is `notes`.** `OrderItem.notes` is a free-text field. Writing `"large, no walnuts"` into it would *appear* to work and would be **wrong in a specific, damaging way**: the price would still be `MenuItem.unit_price`, so the bill would be arithmetically correct but **semantically wrong** — the customer ordered the large one and was charged the small price, or the reverse. **This is a money bug with no error message.** LE31's §3.6 treats money as exact (`Decimal`, never float); a *recorded* price that does not match the *ordered* thing is a different failure that exact arithmetic cannot catch.

**This is why the gap must be named before it is filled.** The dangerous version of this feature is not "no options" — it is "options smuggled into `notes`", which is invisible, unreportable, and produces a wrong number that the owner trusts.

### Why *kitchenasty* and not a bigger, more famous restaurant system

`kitchenasty` is small (**★58**) and off-stack. It is picked anyway for a specific reason: **it is a restaurant-native system that chose to model options, allergens and mealtime tagging *per item* — all three in one line.** That line is the finding. It shows that a small self-hosted restaurant system treats "per-item metadata" as the default shape for a menu, while LE31's `MenuItem` carries only a name, a category, a price, a unit, a prepared flag and a photo.

**The scope of the vocabulary is deliberately tiny.** One sentence, not a schema. The next pass — or the owner — may well decide options are a v2 feature, a v1.5 feature, or never. **This feature records the gap; it does not fill it and does not schedule it.**

## Data model

**No change.** This is a documentation-only artifact.

For the record, and **explicitly not proposed here**, the shape the two sources point at is:

```
MenuItem
  └── OptionGroup          (e.g. "Size", "Side", "Add-ons")
        └── OptionValue    (e.g. "Large", "Fries", "Extra shot")
```

with the chosen value(s) recorded **on the order line**, alongside the price they imply. **Two independent sources converge on this exact two-level shape** — `kitchenasty` (options per item) and `mekedron/wolt-cli` (see feature 387: `--option "Drink=Coca-Cola Zero"`, `--option "Side=Fries L"` — a **group**, an `=`, and a **value**). **That convergence is why this is filed as a shape and not as one author's taste.** But the shape is **not** written into LE31's schema by this feature.

## Implementation steps

1. **One sentence, in LE31's own menu-data boundary.** The substance: *LE31's `MenuItem` describes a product; a product's variants are not described, and an order line is currently `MenuItem × qty` at a single price. Choosing a variant is a future decision, not an implicit use of `notes`.*
2. **One sentence naming what this gap is NOT**, because it has two confusingly similar neighbours (see "Adjacent evidence").
3. **Record the evidence class honestly**: this is an **inferred** gap, from an external artifact, with **no reported owner pain**. LE31's owner has never said "customers want more sizes". **The gap is observable in the schema; the need for it is not established.**

## Telegram interaction if any

**None.** No command, no output, no prompt.

## Dependencies

- **Feature 387** (`mekedron/wolt-cli` — the option-group/value shape) — the **second** independent arrival at the same gap. Read both; they are one idea from two directions.
- **Feature 10** (`10-allergen-tracking.md`) — owns allergens. **The allergen half of this pick's source is a duplicate of feature 10 and is therefore recorded as a duplicate, not picked.**
- **Feature 380** (`boethius68/KitchenLink` — allergen declaration vocabulary) — the first external arrival at the allergen gap; also a duplicate of feature 10's subject.
- **Feature 11** (`11-customer-qr-menu.md`) — owns the customer-facing menu. An option model is a **prerequisite** of a customer-facing menu that can show variant prices; noted here so the next pass does not treat this as a customer-menu detail.

## Open questions

- **Does LE31's owner sell any dish with a choice?** **Unknown, and not askable from the repo.** This is the single question that decides whether options are a v1 gap, a v2 feature, or a non-issue. **Recorded as unknown, not as "yes".**
- **If options are wanted, is the price per-option or per-item-with-surcharge?** Two different models (an option *has* a price vs an option *adjusts* the price). `wolt-cli`'s resolution model and `kitchenasty`'s per-item tags do not settle it. **Do not guess.**
- **Is a "notes" value ever allowed to carry a price-affecting choice?** **The recommendation is no**, and the reason is in "Description" — a free-text choice with a single recorded price is a silent money bug. But this is an owner decision and is recorded as such.
- **Does "mealtime tagging" (also in the source line) matter?** A dish served only at lunch is a menu-availability concept, not an option concept. **Out of scope for this feature**; recorded so a later pass does not conflate the two.

## Why this matters

**Not because options are needed — because the gap is invisible until it is expensive.**

LE31's `MenuItem` and `OrderItem` look complete. They have a price, a unit, a prepared flag, a photo URL. A reader checking "is the menu model done?" says yes. **The absence of options is only visible if you ask the operational question** — *can this restaurant sell a dish that has a size?* — and LE31's schema has no answer to it.

**And the gap has a dangerous wrong answer available.** `OrderItem.notes` exists. So the path of least resistance when the first restaurant asks for a size is `notes = "large"`. That path produces a system that *looks* like it supports sizes, charges the wrong price, and reports nothing. **Naming the gap is what prevents that.** A gap with a written name gets designed; a gap without one gets a `notes` hack.

**The two-arrival convergence is what makes this worth a contract at all.** One author modelling options is a preference. **Two independent authors — a self-hosted restaurant ERP and a restaurant-delivery CLI — both choosing a two-level group/value shape, in the same 30-day window, from opposite ends of the stack (a full restaurant system and a terminal client for someone else's API), is a shape.** That is the same evidentiary standard the series has used since `mesa-lite`'s three-authors-in-one-window finding.

**A boundary that is written down is a decision; a boundary that is merely absent is an accident.** This feature writes one sentence. That is the whole deliverable.

## Adjacent evidence

**This gap has two confusingly similar neighbours, and conflating them would waste the next pass's time:**

1. **The option gap (this feature).** *Which variant of a product was ordered, and what did it cost.* LE31's `MenuItem` and `OrderItem` have no concept of it.
2. **The allergen gap (NOT this feature).** *What is in the dish.* LE31's `MenuItem` has no allergen field — **but `features/10-allergen-tracking.md` already specifies this in full**: 14 EUFIC allergens, per-item and per-ingredient metadata, OR-based propagation, dietary tags, a `/allergens <item>` Telegram command, and a waiter-UI badge. `kitchenasty` names allergens in the same breath as options, and `boethius68/KitchenLink` (feature 380) names all 14 EU allergens. **Two independent arrivals — and LE31 had already specified the gap before either arrived.** **The allergen half of this pick's source is therefore a genuine duplicate and is recorded as such, not picked.**
3. **The category-nesting gap (NOT this feature).** *"Category management with nesting"* — `MenuItem.category` is a plain `str`. Nesting categories is a menu-structure question, not an option question. **Recorded, not picked.**

**Three separate "menu item needs more on it" findings in three days, one of which LE31 had already specified.** That is the shape of the current window: LE31's menu model is not wrong, it is **small**, and the window keeps naming the next three things it does not carry.
