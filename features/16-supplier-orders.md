# Feature 16 — Supplier Purchase Orders & Receiving

> **Priority**: P2 · **Effort**: M (5–10 days) · **Source**: natural extension
> of feature 15 (inventory variance) + owner-pains research on inventory pain.
> **One-line**: Cook orders ingredients from suppliers, marks received → stock
> goes up automatically via the existing append-only ledger.

## Goal

Close the inventory loop: orders go out, deliveries come in, stock goes up —
all tracked through the same `StockEntry` ledger that already powers sales.

## Scope

**In scope (v1 of this feature):**
- `Supplier` entity (name, contact, delivery days, default items).
- `PurchaseOrder` + `PurchaseLine` (draft → ordered → partial → received).
- Cook creates a PO via Telegram bot (`/order flour 5kg butter 2kg milk 10L`).
- On delivery, cook marks "received"; bot prompts for actual received qty
  (often less than ordered); discrepancy is logged.
- Receiving creates `StockEntry(reason='purchase', qty_delta=+actual_qty)`
  rows on the appropriate batches or ingredient stocks.
- Suggested reorder point per ingredient: when stock ≤ par level, bot suggests PO.

**Out of scope:**
- Real supplier integrations (EDI, API, email-to-PO automation).
- Multiple delivery addresses (one restaurant).
- Cross-dock / back-haul logistics.
- Price negotiation / RFQ workflow.

## Description

The cook realizes at 4pm that tomorrow they'll run out of flour. They tap
`/order` in Telegram:
```
Cook: /order flour 5kg butter 2kg milk 10L eggs 60pc
Bot:  Creating draft PO for:
        flour  — 5 kg   (current stock: 1.2 kg)
        butter — 2 kg   (current stock: 0.4 kg)
        milk   — 10 L   (current stock: 3 L)
        eggs   — 60 pc  (current stock: 12 pc)
       Supplier: Default (Local bakery)?
       [Yes — send order] [Edit quantities] [Cancel]
```

Cook taps "Yes". Bot records the PO and (if configured) sends an email to the
supplier. When delivery arrives, cook taps `/receive 12` (PO #12):
```
Bot: PO #12 from Local bakery:
        flour  — ordered 5 kg   → received? [___]
        butter — ordered 2 kg   → received? [___]
        milk   — ordered 10 L   → received? [___]
        eggs   — ordered 60 pc  → received? [___]
```
Cook types `5 2 9 60` (milk was short by 1L).
Bot: 
```
Received:
  flour  5 kg → +5 kg to stock
  butter 2 kg → +2 kg to stock
  milk   9 L  → +9 L to stock (1 L short — flag to supplier?)
  eggs   60 pc → +60 pc to stock

[Send discrepancy email] [Mark PO complete]
```

## Data model

```
Supplier
  id              PK
  name            TEXT
  contact_name    TEXT NULL
  contact_phone   TEXT NULL
  contact_email   TEXT NULL
  delivery_days   TEXT[] (e.g. ['mon','wed','fri'])
  notes           TEXT NULL

PurchaseOrder
  id              PK
  supplier_id     FK
  ordered_at      DATETIME
  expected_at     DATETIME NULL
  received_at     DATETIME NULL
  status          Enum (draft | ordered | partial | received | cancelled)
  total_cents     INT
  notes           TEXT NULL

PurchaseLine
  id              PK
  purchase_order_id FK
  ingredient_id   FK
  qty_ordered     Decimal
  qty_received    Decimal NULL
  unit_cost       Decimal NULL  (filled in on receive)
```

## Telegram interaction

```
Cook: /stock_check
Bot:  Items below par level:

         flour  — 1.2 kg (par: 5 kg)  → suggest PO
         butter — 0.4 kg (par: 1 kg)  → suggest PO
         milk   — 3 L (par: 10 L)    → suggest PO
         eggs   — 12 pc (par: 60 pc) → suggest PO

       [Create PO for all 4] [Pick individual]
```

```
Manager: /suppliers
Bot:     Suppliers:
         1. Local bakery — Mon/Wed/Fri — flour, butter, eggs
         2. Dairy direct — Tue/Thu — milk, cream, cheese
         3. Wine merchant — Fri — wines
         [+ Add supplier]
```

## Implementation

1. **Add 3 tables** — Supplier, PurchaseOrder, PurchaseLine.
2. **Add Telegram commands** — `/order`, `/receive <po_id>`, `/stock_check`, `/suppliers`.
3. **Auto-par-level alerts** — APScheduler job runs nightly, checks each
   ingredient's current stock, suggests PO if below par.
4. **Receiving** — on confirm, batch of `StockEntry(reason='purchase', +qty)` rows
   on the right ingredient batches (or implicit ingredient stocks if no batch).
5. **Optional: email PO to supplier** — via SendGrid / Mailgun, plain text.

## Dependencies

- [15-inventory-variance.md](15-inventory-variance.md) — variance report consumes these POs.
- [10-allergen-tracking.md](10-allergen-tracking.md) — `Ingredient` table is the unit.

## Open questions

- Do we track ingredient batches (per-delivery batches) or just quantities? (v1: quantities;
  batches can come in v2 with FIFO expiry.)
- Should the PO be sent via email automatically, or just stored locally? (Default: stored + manual send.)
- Should we support multiple suppliers per ingredient (price comparison)? (v2.)
- Multi-location ordering (one PO for two restaurants)? (Out of scope for v1.)

## Why this matters

Closing the purchase-to-stock loop means the variance report (feature 15)
becomes **trustworthy** — without POs, "variance" is uninterpretable because
you don't know what *should* be on the shelf.

Per the owner-pains research, supplier / receiving is one of the most
overlooked gaps in small-restaurant software — most POS systems track
**sales** but not **purchases**, leaving the owner blind to leakages.