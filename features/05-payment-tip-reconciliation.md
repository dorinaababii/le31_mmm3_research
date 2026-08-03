# Feature 05 — Payment, Tip & Reconciliation

## Goal

Capture how a visit was paid, derive the tip automatically from `total_paid − items`,
and provide the manager a clean end-of-shift reconciliation report.

## Scope

**In scope (v1):**
- Single bill per visit; split tender (one cash + one card payment row).
- Payment methods: `cash`, `card` (card stores last 4 digits only — no full PAN).
- Derived tip: `tip = total_paid − subtotal_items − subtotal_tax`.
- End-of-shift cash reconciliation: opening float + cash sales + cash tips −
  counted cash = variance.
- Manager export to CSV.

**Out of scope (v1):**
- Online payment gateways (Stripe, SumUp, etc.).
- Tip pooling across staff (each waiter's tips tracked on their own visits).
- Discounts / promo codes.

## Description

When the waiter taps "Bill" on a visit, the system sums `OrderItem.unit_price × qty`
into `subtotal_items`, looks up tax (flat or per-category), shows the total, and
prompts for the amount paid. The waiter types `total_paid = 47.50 EUR, method = card`
(or split: `30 cash + 17.50 card`). On confirm, `Bill` is written and `DerivedTip`
is computed.

```
subtotal_items  = 39.00
subtotal_tax    =  3.90   (10 %)
total_due       = 42.90
total_paid      = 47.50
tip             =  4.60   ← derived
```

If `tip < 0`: refuse to close (underpayment). If `tip > 50%` of subtotal: ask
"are you sure?" (catch typos).

## Data model

```
Bill         (id, visit_id, subtotal_items, subtotal_tax, total_due,
             total_paid, payment_method, paid_at, closed_by)
Payment      (id, bill_id, amount, method, card_last4, ref, at)
DerivedTip   (bill_id, amount, formula_version)
Shift        (id, opened_at, closed_at, opening_float, counted_cash,
             variance, by_user)
```

## End-of-shift reconciliation

Manager (in app or via Telegram `/close_shift`):

1. Open shift → record `opening_float` (e.g. €100).
2. Throughout shift, all cash sales + cash tips accumulate.
3. Close shift → manager types `counted_cash`.
4. System computes:
   ```
   expected_cash = opening_float + SUM(payments WHERE method='cash') +
                   SUM(derived_tips WHERE bill.payments contain cash)
   variance = counted_cash - expected_cash
   ```
5. Variance logged; persistent record for audit.

## CSV export

Daily export columns:
```
date, bill_id, table, server, subtotal, tax, tip, payment_method, paid_at
```

Weekly manager view in the web UI: total sales, total tips, average tip %,
top 10 items sold, payment method mix.

## Dependencies

- [02-order-taking.md](02-order-taking.md) — provides `subtotal_items`.
- [../research/06-payments-tips.md](../research/06-payments-tips.md) —
  establishes the "derive tip = paid − consumed" approach.

## Open questions

- Tax rate — flat (e.g. 10%) or per-category (food 9% / alcohol 19%)?
- Discounts: handled in v1 or punted? (Recommended: punt.)
- "Service charge" (auto-added %): in scope for v1? (Common in EU restaurants;
  not common in US. Decide before coding.)

## Why derived tip is the right choice

- **No manual tip entry** → waiters can't mis-key, can't skim.
- **Auditable**: `tip = paid - items - tax` is provable from the data.
- **One source of truth**: a tip can't disagree with what was paid.