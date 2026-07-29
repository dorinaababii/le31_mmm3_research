# Feature 14 — Split Bills (Multi-Tender Payment)

> **Priority**: P1 · **Effort**: M for ledger, L with terminals (5–20 days) · **Source**: owner-pains research — **#2 most-requested feature** ("Three friends want to pay with three cards").
> **One-line**: One visit, multiple payments — by item, by equal split, or by guest.

## Goal

Let a party pay in any combination they want: by item ("I had the schnitzel,
you had the burger"), equally ("split 4 ways"), by guest assignment, or any
mix of those — without the waiter doing math or restarting the bill.

## Scope

**In scope (v1 — manual entry):**
- One `Visit` can have multiple `Bill` rows (or one `Bill` with multiple `Payment` rows).
- Pay-by-item: waiter assigns items to payers; system computes each payer's total.
- Pay-equal: split total among N payers.
- Pay-by-guest: waiter (or guest) labels items `for guest 1/2/3/4`; system rolls up.
- Multiple payment methods per bill: e.g. €40 cash + €100 card.
- Tip derived per payment row (so split tips work too).

**Out of scope (v1):**
- Live card terminals (we accept `cash | card` only — actual card processing is "manager keys it in later" or "customer's own tap-to-pay").
- Pay-at-table QR (each guest scans and pays their share).
- Saved customer payment methods.

## Description

The bill close screen grows a "Split" button. Three modes:

**Mode 1 — by item:**
```
Visit total: €140
  Marie   : Schnitzel (14) + Wine (10)        = €24
  Paul    : Burger (12) + Fries (4) + Coke (3) = €19
  Sarah   : Salad (9) + Tiramisu (6)           = €15
  ─── unassigned: €82 (3 mains + shared bottle wine)
```
Waiter assigns the rest to one of the three (or splits equally).

**Mode 2 — equal:**
```
Visit total: €140
  4 guests → €35 each
  Marie: pays €35 cash
  Paul:  pays €35 card
  Sarah: pays €35 card
  John:  pays €35 cash + €0 tip (rounding)
```

**Mode 3 — by guest (manual labels):**
```
Each line item has a 'for guest N' tag (set when ordered).
System rolls up per-guest totals.
```

In all modes, the result is N `Payment` rows attached to the `Bill`. Each row
has `amount`, `method`, and the derived tip from that payment (`tip = paid - share - tax_share`).

## Data model

```
Bill            (existing — one per visit)
Payment         (new — multiple per bill)
  id              PK
  bill_id         FK
  amount          Decimal
  method          Enum (cash | card | other)
  card_last4      TEXT NULL
  by_user_id      FK (waiter who keyed it)
  at              DATETIME

PaymentLineItem     (new — pay-by-item mapping)
  payment_id      FK
  order_item_id   FK
  amount          Decimal  (the order_item's share of this payment)
```

## Implementation

1. **New table** `Payment` + `PaymentLineItem`.
2. **Replace single-payment flow** in feature 05 with multi-payment flow.
3. **Bill router** `POST /api/bills/{id}/payments` — accepts list of payments,
   validates `sum(payments) >= total_due`, writes Payment + PaymentLineItem rows.
4. **Derived tip per payment** — same formula: `tip = paid − items_share − tax_share`.
5. **UI** — `index.html` bill close panel gets a "Split" toggle.

## Open questions

- Should we let guests pay via a QR code at the table (their phone, not the waiter)? (Punted to v2 with Stripe Terminal.)
- Tax split: equal per payer, or proportional to items? (Default: proportional.)
- Rounding: when €140 splits 4 ways, €35 each, no remainder. When €141 splits 4 → €35.25 each — does the last payer pay the extra cent? (Standard: first 3 pay €35, last pays €36.)

## Why this matters

Per the owner-pains research, this is **#2 of 12 most-requested features**
with "very common" frequency. Every group of 3+ has the moment where someone
says "let's split" and the waiter sighs.

The good news: the data model is simple (~2 new tables), and we already have
the derived tip formula from feature 05. The hard part is the UX — making
the "Split" panel usable on a phone in a noisy room.