# Feature 19 — Menu Engineering & Item Profitability

> **Priority**: P2 · **Effort**: S (2–3 days) · **Source**: AI/ML research,
> ranked **#1 of 8** by the subagent for "ship first for a small restaurant".
> **One-line**: Classify every dish as Star / Plowhorse / Puzzle / Dog using
> the Kasavana-Smith menu engineering matrix, so the chef knows what to promote,
> reprice, or remove.

## Why this matters

The classic **Kasavana-Smith menu engineering matrix** (1982, still the
industry standard) plots dishes on two axes:
- **Popularity** (sales volume) — X axis
- **Profitability** (margin per dish) — Y axis

This divides the menu into 4 quadrants:

| | High popularity | Low popularity |
|---|---|---|
| **High profitability** | ⭐ **Star** — promote, feature | 🧩 **Puzzle** — raise price or push harder |
| **Low profitability** | 🐎 **Plowhorse** — re-engineer (raise price, lower cost) | 🐕 **Dog** — remove or replace |

Most small restaurants never do this analysis — they just have a menu
and gut feel. Adding it surfaces 5–20% margin improvements on common items.

The AI/ML research flagged this as the **cheapest, highest-ROI** AI/ML
feature for a single restaurant because:
1. Pure analytics on data we already have (orders + new recipe-cost table).
2. No training needed — just SQL + a matrix view.
3. Insight is concrete and actionable ("raise Schnitzel price by €1" vs. "do better ML").

## Goal

A manager dashboard view + Telegram bot command showing each dish's
classification + recommended action.

## Scope

**In scope (v1 of this feature):**
- Compute sales volume per dish per period (week/month/quarter).
- Compute dish profitability = `unit_price − recipe_cost`.
- Kasavana-Smith classification (4 quadrants).
- Manager dashboard tile: "X Stars, Y Plowhorses, Z Puzzles, W Dogs".
- Telegram `/menu_engineering` command showing the matrix.
- Recommended action per quadrant (auto-generated text).

**Out of scope:**
- ML-based price elasticity estimation.
- A/B testing of price changes (see feature on A/B testing — not yet specced).
- Competitor price scraping.

## Description

Each dish has:
- `unit_price` (already in `menu_item`)
- `recipe_cost` (new — sum of `Ingredient.cost_per_unit × Recipe.qty`)

We compute:
- `gross_margin = unit_price − recipe_cost`
- `margin_pct = gross_margin / unit_price`
- `popularity = Σ(qty_sold) over period`

For each dish:
- `profitability_rank = pct_rank(margin_pct over all dishes)`
- `popularity_rank = pct_rank(popularity over all dishes)`

Classification:
- `Star`     if profitability_rank ≥ 0.5 AND popularity_rank ≥ 0.5
- `Plowhorse` if profitability_rank <  0.5 AND popularity_rank ≥ 0.5
- `Puzzle`    if profitability_rank ≥ 0.5 AND popularity_rank <  0.5
- `Dog`       otherwise

Recommended action per quadrant:
- Star:     "Feature on menu, train staff to upsell."
- Plowhorse: "Re-engineer — raise price €X or reduce ingredient cost."
- Puzzle:    "Reposition on menu or raise awareness."
- Dog:      "Consider removing or replacing."

## Data model

```
Ingredient      (existing from feature 10)
  cost_per_unit Decimal

Recipe          (existing from feature 10)

MenuEngineering
  id              PK
  menu_item_id    FK
  period_start    DATE
  period_end      DATE
  units_sold      INT
  gross_margin    Decimal  (per dish)
  margin_pct      Decimal
  popularity_rank Decimal  (0–1)
  profitability_rank Decimal (0–1)
  classification  Enum (star | plowhorse | puzzle | dog)
  computed_at     DATETIME
```

A materialized view (Postgres) or a daily-recomputed table (SQLite) works.

## Implementation

1. **Add `Ingredient.cost_per_unit`** (already in feature 10 spec).
2. **Add `MenuEngineering` table**.
3. **Daily job** (`backend/app/services/menu_engineering.py`): SQL aggregation
   → write `MenuEngineering` rows.
4. **API endpoint**: `GET /api/reports/menu_engineering?period=last_30_days`.
5. **Manager dashboard tile** on Reports view (`index.html`).
6. **Telegram command** in `cook_bot.py`: `/menu_engineering` returns a
   formatted summary with action items.

## Telegram interaction

```
Manager: /menu_engineering
Bot:     Menu engineering for last 30 days:

         ⭐ STARS (high margin + popular)
           Schnitzel   €14 / cost €4.50  → margin 68%  ×142 sold
           Burger      €12 / cost €4.20  → margin 65%  ×98 sold
           Coke        €3  / cost €0.40  → margin 87%  ×210 sold

         🐎 PLOWHORSES (popular but low margin — re-engineer!)
           Caesar Salad €9 / cost €5.80  → margin 36%  ×67 sold
             → Suggestion: raise price to €10.50, or replace anchovies
               with cheaper capers (saves €0.80/dish).

         🧩 PUZZLES (high margin, low popularity — promote more!)
           Tiramisu    €6  / cost €1.40  → margin 77%  ×31 sold
             → Suggestion: move to "chef's recommendation" card on menu.

         🐕 DOGS (low margin + low popularity — consider removing)
           Espresso    €2.50 / cost €1.20 → margin 52% ×8 sold
             → Marginal — keep if it's a customer expectation, else drop.

         Total potential margin improvement if all Plowhorses re-engineered:
         +€145 / month.
```

## Dependencies

- [10-allergen-tracking.md](10-allergen-tracking.md) — provides `Ingredient.cost_per_unit` and `Recipe`.
- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — provides `OrderItem` sales volume.

## Open questions

- Period for ranking — 30 days, 90 days, or rolling year? (Default: 30 days;
  longer = more stable but slower to react to menu changes.)
- Should we adjust for trend (rising vs falling popularity)? (v2 — using Prophet predictions.)
- Should the cook see competitor prices? (Out of scope; would need scraping.)

## Why this matters

The AI/ML research ranked this **#1 of 8 features to ship first** because:
- 2-3 days to ship
- Uses data we already have + a small new `cost_per_unit` field
- Surfaces 5-20% margin improvements
- Zero new external services, zero privacy risk, zero model training
- Pays for itself in weeks

Per the AI/ML research note: *"Zero privacy risk (own data). Real cost:
getting the chef to maintain recipe costs accurately."*

## Recommended next step

Build this **right after feature 10 (allergens)** because both depend on
the same `Ingredient` + `Recipe` tables. The combo unlocks profitability
analysis with almost no extra work.