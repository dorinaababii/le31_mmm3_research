# Feature 10 — Allergen & Dietary Tracking

> **Priority**: P1 · **Effort**: S–M (3–7 days) · **Source**: owner-pains
> research — "I cannot safely answer 'does this contain nuts?' from memory."
> **One-line**: Per-dish allergen + dietary tags that propagate from ingredients
> and filter the customer-facing menu.

## Goal

Every menu item carries structured metadata about what allergens and dietary
properties it has. The cook can answer allergen questions confidently during
a rush. The customer-facing menu (when we add it) can filter by dietary need.

## Scope

**In scope (v1 of this feature):**
- 14 EUFIC-standard allergens (cereals, crustaceans, eggs, fish, peanuts,
  soybeans, milk, nuts, celery, mustard, sesame, sulphites, lupin, molluscs).
- Dietary tags: vegan, vegetarian, halal, kosher, gluten-free, lactose-free,
  spicy (mild/medium/hot).
- Per-menu-item metadata; per-ingredient metadata; auto-derivation.
- Substitutions table ("if no lactose → use oat milk").
- Cook gets a `/allergens <item>` Telegram command.
- Waiter UI badge on each menu item ("V" "GF" "contains nuts").

**Out of scope:**
- Full nutritional info (calories, macros) — needs a separate database.
- Customer-facing allergen quiz / form.
- Per-shift allergen briefings (folded into [feature 12 — pre-shift briefings](12-pre-shift-briefing.md)).

## Description

Each `MenuItem` is composed of `Ingredients`. Each `Ingredient` carries
allergen flags + dietary tags. Allergens propagate:
- If dish contains `flour` (cereal) → dish is flagged `contains_cereal`.
- If dish contains `butter` (milk) → dish is flagged `contains_milk`.
- Aggregation is OR-based: any ingredient with the flag → dish has the flag.

Dietary tags are subtler:
- Dish is `vegan` only if all ingredients are `vegan`.
- Dish is `vegetarian` if all ingredients are at least `vegetarian`.
- Dish is `gluten_free` if no ingredient contains gluten (cereals).

## Data model

```
Ingredient
  id              PK
  name            TEXT  ('flour', 'butter', 'chicken breast', ...)
  unit            TEXT  ('g', 'ml', 'piece')
  cost_per_unit   Decimal
  allergens       TEXT[]  (or comma-separated: 'cereal,milk')  -- OR'd from canonical 14
  dietary_tags    TEXT[]  ('vegan', 'vegetarian', 'gluten_free')
  is_raw          BOOL    -- true if stockable (flour); false if prepared

Recipe
  id              PK
  menu_item_id    FK
  ingredient_id   FK
  qty             Decimal
  unit            TEXT

Allergen                -- canonical list (lookup table)
  code          TEXT     ('cereal', 'crustacean', 'egg', ...)
  display_name  TEXT     ('Cereals containing gluten', ...)

DietaryTag              -- canonical list (lookup table)
  code          TEXT     ('vegan', 'vegetarian', ...)
  display_name  TEXT

Substitution
  id              PK
  ingredient_id   FK
  alt_ingredient_id FK
  notes          TEXT
```

## Implementation

1. **Seed allergens + dietary tags** from EUFIC list (one-time SQL insert).
2. **Seed common ingredients** as part of bootstrap (flour, butter, eggs, …).
3. **Recipe management** in the manager UI: pick menu item → add ingredients with qty.
4. **Auto-derivation trigger**: when a recipe row is added/removed, recompute
   the parent menu item's allergen / dietary tags (in a SQL view or
   computed field).
5. **`/allergens <item>` bot command**: returns the list with friendly names.
6. **Menu UI badges** on `index.html` (extend the menu view).

## Telegram interaction

```
Cook: /allergens schnitzel
Bot:  Schnitzel contains:
        🌾 Cereals (flour, breadcrumbs)
        🥛 Milk (butter, cream)
      Substitutions available:
        → gluten-free breadcrumbs
        → oat milk (lactose-free)
```

```
Cook: /allergens caesar_salad
Bot:  Caesar Salad contains:
        🌾 Cereals (croutons)
        🥚 Eggs (mayo, dressing)
        🐟 Fish (anchovies)
        🥛 Milk (parmesan)
      ⚠ Cannot be made vegan as currently composed.
```

## Dependencies

- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — Recipe → Batch story
  builds on the stock ledger for ingredient deduction.
- [11-customer-qr-menu.md](11-customer-qr-menu.md) (later) — needs allergen filters.

## Open questions

- Should we add the EUFIC list of 14 allergens verbatim, or pick a regional subset?
- Should dietary tags require **all** ingredients to match (strict) or **most**?
- Should the cook see warnings when an item becomes allergen-free after a
  substitution? (E.g. "you substituted oat milk → dish is now lactose-free".)

## Why this matters

- **Safety** — wrong allergen answers create legal liability.
- **Trust** — vegan/celiac guests become repeat customers when they can trust the menu.
- **Operational** — current waiters answer from memory; this makes them honest.

In the owner-pains research, allergens ranked #5 most-requested feature with
"very common" frequency and "high consequence" severity.