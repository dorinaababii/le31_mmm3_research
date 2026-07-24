# Recommended Stack & Architecture

## TL;DR

Build a thin Python app, not a fork.

| Layer | Choice | Why |
|---|---|---|
| HTTP API | **FastAPI** | async, type-hinted, auto OpenAPI docs |
| Database | **PostgreSQL** | mature, supports the Batch + StockEntry ledger pattern |
| Telegram bot | **aiogram** | MIT, FSM, clean async API |
| Menu OCR | **RapidOCR** + small LLM call | lightweight, ~3s end-to-end |
| UI mock-up | **index.html** (vanilla, served by FastAPI) | per user spec |
| Auth | PIN-code per role | simpler than full user/pass for a small restaurant |
| Deployment | single VPS, Docker Compose | smallest moving parts |

## High-level architecture

```
                                 ┌──────────────────┐
                                 │   PostgreSQL     │
                                 │  (ledger, batch) │
                                 └─────────▲────────┘
                                          │
                       ┌──────────────────┼──────────────────┐
                       │                  │                  │
                ┌──────┴──────┐   ┌───────┴───────┐  ┌───────┴────────┐
                │   FastAPI   │   │   aiogram     │  │   index.html   │
                │  (waiters,  │   │   (cook,      │  │   (waiter UI   │
                │   manager)  │   │    manager)   │  │    mock-up)    │
                └──────▲──────┘   └───────────────┘  └────────────────┘
                       │
                       │
                  HTTP + JSON
                       │
                  (tablets / laptops at tables)
```

## Key tables (DDL sketch)

```sql
-- Menu & stock
CREATE TABLE menu_item (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT,
  unit_price NUMERIC(10,2) NOT NULL,
  unit TEXT,                     -- 'piece', 'glass', 'plate'
  is_prepared BOOLEAN DEFAULT TRUE,
  photo_url TEXT
);

CREATE TABLE batch (
  id SERIAL PRIMARY KEY,
  menu_item_id INT REFERENCES menu_item(id),
  qty_start INT NOT NULL,
  qty_remaining INT NOT NULL,
  prepared_at TIMESTAMPTZ DEFAULT NOW(),
  expires_at TIMESTAMPTZ,
  photo_url TEXT,
  notes TEXT
);

CREATE TABLE stock_entry (
  id BIGSERIAL PRIMARY KEY,
  batch_id INT REFERENCES batch(id),
  qty_delta INT NOT NULL,        -- positive = added, negative = consumed
  reason TEXT,                   -- 'sale', 'waste', 'restock', 'initial'
  ref_order_item_id BIGINT,
  by_user_id INT,
  at TIMESTAMPTZ DEFAULT NOW()
);
-- current stock = SUM(qty_delta) per batch_id; never delete rows.

-- Operations
CREATE TABLE table_ (              -- 'table' is a reserved word; underscored
  id SERIAL PRIMARY KEY,
  label TEXT,                      -- 'T1', 'T2'...
  seats INT
);

CREATE TABLE visit (
  id SERIAL PRIMARY KEY,
  table_id INT REFERENCES table_(id),
  server_id INT REFERENCES app_user(id),
  opened_at TIMESTAMPTZ DEFAULT NOW(),
  closed_at TIMESTAMPTZ,
  party_size INT,
  adults INT,
  children INT
  -- gender fields intentionally omitted in v1 (privacy)
);

CREATE TABLE order_item (
  id BIGSERIAL PRIMARY KEY,
  visit_id INT REFERENCES visit(id),
  menu_item_id INT REFERENCES menu_item(id),
  qty INT NOT NULL DEFAULT 1,
  unit_price NUMERIC(10,2) NOT NULL,
  course TEXT,                    -- 'appetizer', 'main', 'dessert'
  status TEXT DEFAULT 'new',      -- new|preparing|ready|served|cancelled
  notes TEXT
);

CREATE TABLE bill (
  id SERIAL PRIMARY KEY,
  visit_id INT REFERENCES visit(id) UNIQUE,
  subtotal_items NUMERIC(10,2),
  subtotal_tax NUMERIC(10,2),
  total_paid NUMERIC(10,2),
  payment_method TEXT,            -- 'cash' | 'card'
  paid_at TIMESTAMPTZ,
  closed_by INT
);

CREATE TABLE derived_tip (
  bill_id INT PRIMARY KEY REFERENCES bill(id),
  amount NUMERIC(10,2),
  formula_version TEXT            -- 'v1'
);

CREATE TABLE app_user (
  id SERIAL PRIMARY KEY,
  name TEXT,
  pin_hash TEXT,                  -- bcrypt
  role TEXT                       -- 'server' | 'cook' | 'manager'
);
```

## REST endpoints (sketch)

```
GET   /api/tables                  → list tables + status
POST  /api/visits                  → seat party at table (captures party_size, adults, children)
POST  /api/visits/{id}/items       → add order item
PATCH /api/visits/{id}/items/{iid} → update item status (kitchen bumps)
POST  /api/visits/{id}/close       → generate bill, capture total_paid + payment_method
GET   /api/reports/today           → manager dashboard
GET   /api/menu                    → today's available menu
GET   /api/menu/{id}               → menu item details
POST  /api/menu/from-image         → (Telegram bot only) ingest menu photo
```

## Telegram bot flows

**Cook — `/start_today`:**
1. Bot: "Send me a photo of today's menu"
2. Cook sends photo → bot runs OCR + LLM → returns list of `{name, qty, price}` items
3. Bot shows inline keyboard "Confirm?" → cook confirms → batches created
4. Cook sets per-item quantities via numbered replies or buttons

**Cook — `/sold_out <item>`:**
- Marks the batch as depleted; menu auto-updates for waiters

**Cook — `/eod`:**
- Lists: sold, leftover, waste (manual entries)
- Suggests tomorrow's prep: `round(sold_avg_last_14_days * 1.1)`

**Waiter — `/my_tables`:**
- Shows tables I'm serving with current bill preview

## v1 / v2 split

**v1 (this index.html + minimal real app):**
- Table management, seating, party size
- Order entry (waiter selects from menu)
- Send to kitchen (kitchen sees on Telegram)
- Bill close + tip derivation
- Telegram bot for daily menu photo + OCR

**v2 (after we have data):**
- Demand forecast (last N days)
- Per-server tip pooling
- Customer loyalty / repeat visit tracking
- Multi-location

## Open questions for the user (before we code)

1. **Language** — what language for the menu items? (Affects OCR choice: PaddleOCR if CN, RapidOCR for European languages.)
2. **Currency** — single currency or multi? Affects schema.
3. **Tax** — flat or per-category? Affects `subtotal_tax` calculation.
4. **Hardware** — waiters on tablets? phones? desktop? Affects UI choices.
5. **Single restaurant or chain?** — affects multi-tenancy decisions.

See [../features/01-table-management.md](../features/01-table-management.md) for the first feature spec.