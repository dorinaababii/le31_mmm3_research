# Feature 07 — Demand Estimation (Prep Quantities)

## Goal

Each evening, the cook (or manager) gets a Telegram message:
*"Based on the last 14 days, I suggest you prep 22 Schnitzel, 18 Burger, 6 Tiramisu tomorrow."*

## Scope

**In scope (v1):**
- Per-item 14-day rolling average of sold quantity.
- Per-item leftover rate from yesterday.
- Suggestion = `max(0, round(avg_14d × 1.1))` — slight buffer.
- Item-specific adjustment factors (cook can override per item).
- Telegram bot command: `/forecast` or `/demand_forecast`.

**Out of scope (v1):**
- Day-of-week seasonality (would need 4+ weeks of data and is v2).
- Weather / event-aware forecasting (v3+).
- ML model — v1 uses simple averages; v2 can use Prophet or similar.

## Description

The cook records what was leftover at end of each day (feature 03 → EOD summary
already collects this). Each morning, the bot shows yesterday's results. Each
evening, `/forecast` runs and posts tomorrow's suggested prep quantities.

## Algorithm (v1 — simple)

```
For each item X sold in the last 14 days:
  avg_sold     = mean(sold_qty over last 14 days)
  waste_rate   = mean(leftover_qty / prepared_qty over last 14 days)
  buffer       = 1.1  # 10 % buffer for safety
  suggested    = round(avg_sold * buffer)
  message     += f"{X}: prepare ~{suggested} (avg {avg_sold}, waste {waste_rate*100:.0f}%)"
```

For items with <14 days of data, fall back to the cook's manual quantity
prompt that already exists in the menu photo bot.

## Data sources

- `stock_entry` (ledger) — sum by day for `reason='sale'`.
- `batch` — `qty_start` and `qty_remaining` give leftover at any time.

The derived metric `sold_per_day(item_id, date)` is computed nightly.

## Telegram interaction

```
Cook: /forecast
Bot: Here's my forecast for tomorrow:

  Schnitzel    22   (avg 19 sold/day, 8% waste)
  Burger       18   (avg 16 sold/day, 12% waste)
  Tiramisu      6   (avg 5 sold/day, 15% waste)

  [✓ Sounds good]
  [✎ Override...]
```

If cook overrides (e.g. "tomorrow is a holiday, prep more"), the override is
saved as `manual_override` and used for tomorrow's actual batch.

## Dependencies

- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — source of
  sales and leftover data.
- [04-menu-photo-bot.md](04-menu-photo-bot.md) — bot interface.

## Open questions

- Should the forecast adjust for the **next day of week**? (Big lift —
  needs 4+ weeks of data per day-of-week; defer to v2.)
- How to handle brand-new items with no history? Default to the cook's
  manual quantity.
- Should the forecast consider upcoming reservations? (Out of scope for v1.)

## Future (v2)

- Prophet / SARIMA model with weekly seasonality.
- Weather API integration.
- "Special event" flag the manager can set that bumps the forecast.