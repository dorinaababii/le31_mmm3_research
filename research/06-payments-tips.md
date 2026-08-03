# Payments, Tips & Reconciliation

The user's specific ask: capture payment method (cash/card), amount paid,
and **derive tip = total_paid − items_consumed**. This is the cleanest
model for tip tracking and is what we should implement.

## What existing POS systems do

- **TastyIgniter** (PHP/Laravel): `payments` table with `method`, `amount`,
  `tip`, `card_last4`. Tip is a separate input field, not derived.
- **URY** (Frappe): tip is a separate Sales Invoice field; manual entry.
- **Flutter POS** (Dart): tip stored as its own field on the Bill.

Every major POS treats tip as a **manual entry**. The user's spec
("derive it from total paid minus consumed") is *simpler* and *more honest*
— there is no risk of waiter mis-keying the tip.

## Data model

```
Bill         (id, order_id, subtotal_items, subtotal_tax, total_paid,
             payment_method, paid_at, by_user)
Payment      (id, bill_id, amount, method, card_last4, ref)   -- multiple rows allowed (split tender)
DerivedTip   (bill_id, amount, formula_version)               -- computed on bill close
```

When `Bill.close()` is called:
```
tip = total_paid - subtotal_items - subtotal_tax
if tip < 0: raise "Underpaid"  -- or carry as credit
DerivedTip.create(bill_id=bill.id, amount=tip, formula_version='v1')
```

## Reconciliation

End of shift, the manager runs:
1. `expected_cash = opening_float + cash_sales + cash_tips − cash_refunds`
2. Count the till.
3. `variance = counted - expected` → log it.

Tip pool / distribution (split tips across staff) is **out of scope for v1**.
Just record the tip per bill; manual spreadsheet is fine until the team
gets bigger.

## Open-source references

No project implements "derived tip = total_paid − items" automatically. Most
expect manual entry. Implementing this is a small win and a clean differentiator.

See [../features/05-payment-tip-reconciliation.md](../features/05-payment-tip-reconciliation.md).