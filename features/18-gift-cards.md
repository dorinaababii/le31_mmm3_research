# Feature 18 — Gift Cards & Store Credit

> **Priority**: P2 · **Effort**: M (5–8 days) · **Source**: owner-pains research
> — #11 feature with "common" frequency: "Gift cards should bring cash in now
> and repeat visits later. Store credit must survive refunds and be impossible
> for staff to 'lose' or duplicate."
> **One-line**: Issue gift cards and store credit via an append-only ledger;
> redeem at bill close with one scan.

## Goal

Let the restaurant sell gift cards (physical + digital) and issue store credit
(for refunds, comps). All balances computed from an append-only ledger —
impossible for staff to "lose" or duplicate.

## Scope

**In scope (v1 of this feature):**
- Issue a gift card: pick amount, optional recipient name + message, generate
  QR/code, optionally email.
- Redemption: at bill close, scan/type code → system applies balance, reduces
  the bill total due.
- Partial redemption (€20 card, €14 bill → card balance becomes €6).
- Refund-as-store-credit: when a bill is refunded, the customer can choose
  store credit instead of cash.
- Manager view: list of outstanding gift cards + total liability.

**Out of scope:**
- Multi-channel redemption (gift card works only at this restaurant).
- Loyalty points (separate; requires customer identity).
- Gift card marketplace / resale.
- Physical card printing (we issue QR/digital only; print-on-paper is a v2 add).

## Description

**Issuance** — manager runs `/giftcard 50 "Marie Dupont" "Happy birthday"` in
Telegram (or via the manager UI). Bot generates a 16-char code + QR. Manager
emails the code to Marie (or prints a physical QR for in-store sale).

**Redemption** — at bill close, waiter enters the code in the bill panel.
System validates:
- Card exists.
- Not expired.
- Has sufficient balance.

Reduces bill total due. Creates a `StoredValueTransaction` row with
`amount=-<redeemed>` (negative because it's leaving the card).

**Refund → store credit** — manager refunds a bill. System offers "cash to
customer" or "store credit". On credit, creates a new card with the refund
amount, owned by the same (anonymous) customer.

## Data model

```
GiftCard
  id              PK
  code            TEXT UNIQUE  (16-char, URL-safe, non-guessable)
  initial_cents   INT
  issued_at       DATETIME
  issued_by       FK (manager)
  recipient_name  TEXT NULL
  recipient_msg   TEXT NULL
  expires_at      DATETIME NULL
  status          Enum (active | depleted | expired | revoked)

StoredValueTransaction   -- append-only ledger
  id              PK
  gift_card_id    FK
  amount_cents    INT  (positive = added, negative = redeemed)
  reason          Enum (issuance | redemption | refund_credit | revoke | expiry)
  ref_bill_id     FK NULL
  by_user_id      FK
  at              DATETIME

  -- current balance = SUM(amount_cents) for gift_card_id
  -- never UPDATE or DELETE rows
```

## Implementation

1. **Add 2 tables** — `GiftCard`, `StoredValueTransaction`.
2. **Issuance** — manager UI + Telegram command; generates secure random code.
3. **Redemption** — extend the bill close flow with a "Gift card" field;
   validates + writes `StoredValueTransaction` rows in a single transaction.
4. **Manager view** — `/api/reports/giftcards` returns outstanding cards + total liability.
5. **Email delivery** (optional) — SendGrid / Mailgun integration.

## Telegram interaction

```
Manager: /giftcard 50 "Marie Dupont" "Joyeux anniversaire!"
Bot:     Gift card issued:

          Code: GFT-7K2M-9P4X-L8N3
          Balance: €50.00
          Recipient: Marie Dupont
          Message: Joyeux anniversaire!
          Expires: never

         [Email to customer] [Print QR] [Done]
```

```
Waiter (at bill close):
         Total: €42
         Gift card: GFT-7K2M-9P4X-L8N3 → balance €50, applied €42
         Remaining to pay: €0
         Tip on €0 paid: €0 (derived from total_paid − items)

Bot confirmation:
         Gift card GFT-7K2M-9P4X-L8N3: €42 redeemed. New balance: €8.
```

```
Manager: /giftcards
Bot:     Outstanding gift cards (5):

         Code                Balance  Issued         Expires
         GFT-7K2M-9P4X-L8N3  €8       3 days ago    never
         GFT-3X9P-2K7M-5L8W  €100     1 week ago    never
         ...

         Total liability: €246
```

## Why an append-only ledger matters

The owner-pains research called out: "store credit must survive refunds and
be impossible for staff to 'lose' or duplicate."

With the same append-only pattern as our `StockEntry` ledger:
- Balance = `SUM(amount_cents)` — never stored, always computed.
- Refunds, corrections, expirations are new rows — never mutations.
- Audit trail is automatic — every change has a `reason`, `by_user`, `at`.

This is the same pattern as a bank ledger. It works.

## Dependencies

- [05-payment-tip-reconciliation.md](05-payment-tip-reconciliation.md) — bill close flow.

## Open questions

- Do gift cards expire? (Default: no. Optional per card.)
- Can a gift card be re-loaded? (v2 feature; not v1.)
- Multi-restaurant gift cards (chain)? (Out of scope.)
- Physical card printing? (v2; v1 is QR/digital only.)

## Why this matters

Gift cards are pure upside: cash in now, redeem later. Industry average
redemption rate is ~70%, meaning 30% of gift card value is **never redeemed**
— that's free margin for the restaurant. They also pull in new guests
(recipients) who might not otherwise have visited.