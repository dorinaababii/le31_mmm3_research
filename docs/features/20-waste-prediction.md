# Feature 20 — Food Waste Prediction & Reduction

> **Priority**: P2 · **Effort**: M (5–7 days software-only; 30+ days if adding CV) ·
> **Source**: AI/ML research, ranked **#2 of 8** for "ship first for a small restaurant".
> **One-line**: Predict tonight's likely leftovers, then nudge the cook to
> run a discount special or staff-meal portion.

## Why this matters

Food cost is typically **28–35%** of revenue for a small restaurant.
Of that, **5–15%** is waste (prepped but unsold, then thrown away).
Cutting waste by half can mean **€500–2000/month** recovered margin
for a small restaurant.

The AI/ML subagent flagged this as the **highest-ROI AI feature** because:
- We already have the killer feature (prepared-item ledger — feature 03).
- Soft ML on per-item features gives 70% of the value of expensive CV.
- The hard part isn't the prediction — it's getting the cook to **act** on it.

## Goal

Predict at, say, 8pm which prepared items are likely to go unsold by closing
time. Surface this as a Telegram nudge with a one-tap action: "Run a 40% off
special" or "Mark as staff meal".

## Scope

**In scope (v1 of this feature):**
- Per-item "expected unsold at close" estimate based on:
  - Current `qty_remaining` (from `Batch`)
  - Historical sell-through rate (from `StockEntry` ledger)
  - Day of week, hour of day
  - Weather (optional — Open-Meteo, free)
- Model: simple per-item baseline (`avg_sell_through_rate`) + Prophet / XGBoost
  enhancement for items with ≥30 days history.
- Telegram alert at chosen hour (default 20:00) listing likely-waste items.
- Inline buttons:
  - `[Run X% off special]` — temporarily discount the menu item, log to a markdown note.
  - `[Mark as staff meal]` — post `StockEntry(reason='waste', qty_delta=-N)`, tag `staff_meal`.
  - `[Ignore]` — log a false positive; helps the model learn.

**Out of scope:**
- Computer vision over scraping bin (separate feature; needs camera hardware).
- ML-based dynamic pricing (deferred).
- Cross-item substitution suggestions ("run a burger special because Schnitzel will spoil").

## Description

The killer feature (feature 03) already records every `StockEntry` so we know
exactly how many of each prepped item was made and how many sold. With a few
weeks of history we can compute per-item `sell_through_rate`:

```
sell_through_rate[item, day_of_week, hour] =
    qty_sold[item, dow, hour] / qty_prepared[item, dow, hour]
```

Average across history for that (item, dow, hour) bucket.

At trigger time, for each active batch:
```
expected_unsold = qty_remaining * (1 - sell_through_rate[item, dow, hour])
if expected_unsold ≥ threshold (e.g. 30% of qty_start):
    alert cook
```

## Data model

No new schema — uses existing `Batch`, `StockEntry`, `MenuItem`. Add one
optional table to track cook responses (so the model can learn):

```
WastePredictionLog
  id              PK
  menu_item_id    FK
  batch_id        FK
  predicted_at    DATETIME
  trigger_hour    INT  (e.g. 20)
  predicted_unsold INT
  cook_action     Enum (special | staff_meal | ignored | other)
  action_at       DATETIME
  final_unsold    INT  (filled in at EOD)
```

## Implementation

1. **Background job** (`backend/app/services/waste_predict.py`): runs at
   configurable hour (default 20:00), computes predictions, sends Telegram
   alerts for items above threshold.
2. **Model v1** — simple per-item + dow + hour averages from `StockEntry`.
3. **Model v2** — Prophet per item with day-of-week + hour features (after
   60+ days of history).
4. **Inline buttons** in aiogram callback query handler.
5. **Manager dashboard tile** showing weekly waste cost + trend.

## Telegram interaction

```
Bot (20:00): ⚠ Likely waste tonight — chef, decide:

       Tiramisu:  6 portions remaining, 70% likely unsold
       Caesar Salad: 4 portions remaining, 50% likely unsold
       Schnitzel:  8 portions remaining, 25% likely unsold (under threshold)

       Actions for Tiramisu:
       [Run 40% off special (until 22:00)]
       [Mark as staff meal (5 portions)]
       [Ignore — false positive]

       Actions for Caesar Salad:
       [Run 30% off special]
       [Mark as staff meal]
       [Ignore]
```

Cook taps "Run 40% off special" for Tiramisu → system updates the menu display
with the temporary price, logs the action, sends a Telegram message to
waiters: "Tiramisu is 40% off until 22:00 — suggest to guests!"

## Library options

| Library | Stars | Use |
|---|---|---|
| **facebook/prophet** | 20.3k | Per-item time series with day-of-week, holiday regressors |
| **dmlc/xgboost** | 28.6k | Lag features + categorical (item, dow, hour, weather) |
| **Nixtla/statsforecast** | 4k | Fast AutoARIMA / Theta / ETS — lower effort than Prophet |
| **sktime** | 9.9k | Sklearn-compatible time series |

**Recommended start**: simple averages (1 day). **Recommended upgrade**: Prophet per item (3 days).

## Why this works without CV

The AI/ML research's strongest insight: *"the prepared-item ledger gives 80%
of the value"* of CV-based waste tracking. A camera over the scraping bin
catches what *was* thrown away, but our ledger already predicts what *will*
be thrown away — earlier, with cheaper data, in time to act.

CV adds value mostly when:
- Portion sizes vary a lot (we already track `qty` precisely).
- Waste happens *during* prep (we track `StockEntry(reason='waste')`).
- You want to differentiate "spoiled in kitchen" from "returned by guest"
  (we'd need either a tagging step or CV).

## Dependencies

- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — the ledger is the data source.
- [07-demand-estimation.md](07-demand-estimation.md) / [17-demand-forecasting-ml.md](17-demand-forecasting-ml.md)
  — predictions complement rather than duplicate demand forecasts.

## Open questions

- Should the discount special be visible to waiters immediately? (Yes — they need to know what to push.)
- Should we send reminders until the cook acts? (Default: yes, every 10 min for 30 min.)
- Do we need explicit "staff meal" tracking or just a `StockEntry(reason='staff_meal')`? (Default: explicit reason in enum.)
- Should we expose this to waiters proactively ("offer Tiramisu at €3.50 to guests waiting")? (v2.)

## Why this matters

The AI/ML research ranked this **#2 of 8** to ship first because:
- 5-7 days software-only (CV is overkill for a single restaurant).
- Uses our existing killer feature as direct input.
- Pays back via 5-10% food-cost reduction.
- Per the research: *"the hard part isn't the prediction — it's getting
  the cook to act on it"*. The inline-button UX addresses that.

Per the AI/ML note: *"ROI is concrete — 5–10% food-cost reduction pays
for a SaaS license alone."*