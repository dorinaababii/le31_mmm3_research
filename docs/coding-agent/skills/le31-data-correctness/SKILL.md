---
name: le31-data-correctness
description: Use whenever changing or reviewing the SQLModel models, the Postgres schema, the migration strategy, the append-only ledger enforcement, money columns, VAT/tax columns, time/timestamp columns, or customer-data columns. Encodes correctness invariants the coding agent must preserve.
version: 1.0.0
author: Hermes Agent (research side)
license: MIT
metadata:
  hermes:
    tags: [le31, data, sqlmodel, postgres, ledger, gdpr, vat, money, timezone]
    related_skills: [le31-conventions-coder, le31-arch-patterns, le31-quality-gates]
---

# LE31 Data Correctness

## Overview

Schema, columns, and money/time invariants that the coding agent must preserve. If a change conflicts with this skill, the skill wins unless the owner revokes it explicitly.

## Standards anchor

- **Money**: Fowler Money pattern + Husobee (2016). Never float.
- **Timestamps**: RFC 3339 + IANA tzdb. Always TZ-aware, persisted in UTC, rendered in Europe/Paris.
- **VAT**: EU VAT Directive framework, France reduced rates. Store rate + base + tax per line.
- **Append-only**: NIST SP 800-92 + double-entry + Whittaker event-sourcing blog. Enforced in production at the database boundary.
- **Customer data**: GDPR Art. 5(1)(c) data minimisation + Art. 25 by design. CNIL is the French regulator.

## Stock ledger correctness

- Column `qty_delta` is `INTEGER`, signed.
- `reason` is a `CHECK`-constrained enum: `prep`, `order`, `waste`, `manual_adjust`.
- `source` is a `CHECK`-constrained enum: `bot`, `ui`, `import`.
- `actor` references the operator who triggered the action; not optional.
- `created_at` is `TIMESTAMPTZ`, default `now()` at UTC.
- No `current_stock` view column is stored. Current stock is `SUM(qty_delta)` filtered by item, never a column updated in place.
- Production Postgres revokes UPDATE and DELETE on `stock_entry` from the application role; the role may INSERT and SELECT only.
- Corrections are compensating rows, never in-place edits. A test asserts that an attempt to UPDATE raises.

## Money correctness

- Authoritative money values are `INTEGER` (cents) or `Decimal` (configured at boot). Never `float` or `DOUBLE PRECISION`.
- Currency is EUR unless the owner changes the single-currency decision.
- VAT: store `rate_bps` (basis points: 100 bps = 1%), `base_cents`, `tax_cents` per line. `tax_cents = round(base_cents * rate_bps / 10000)` for HALF-EVEN rounding.
- Totals derive from line rows; no stored total without an explicit consistency mechanism.
- Receipts store explicit `subtotal_cents`, `tax_cents`, `tip_cents`, `total_cents`. Tip is derived, never entered manually.

## Time and timezone

- Every timestamp column is `TIMESTAMPTZ` (`timestamp with time zone` in Postgres).
- Application code uses `datetime.now(tz=ZoneInfo("Europe/Paris"))` for business events. UTC for storage; conversion is explicit.
- Business-day boundaries (e.g. "today's revenue") compute via `AT TIME ZONE 'Europe/Paris'`.
- DST awareness: trust the tzdb; never hardcode offsets.

## Privacy and data minimisation (GDPR Art. 5 + Art. 25)

Columns that collect or store any of the following require an approved feature contract and must be listed in the table:

- customer name
- customer phone number
- customer email
- customer profile identifier
- payment card data (PAN, CVV, expiry)

V1 guest data is limited to counts (`party_size`, `adults`, `children`). Identity is not stored.

CI / pre-commit gate:

```sql
SELECT table_name, column_name FROM information_schema.columns
WHERE table_schema = 'public'
  AND (column_name ILIKE '%phone%' OR column_name ILIKE '%email%' OR
       column_name ILIKE '%name%' OR column_name ILIKE '%pan%');
```

Any row returned without an approved-feature annotation blocks the merge.

## Migrations

- A migration is a forward file and a rollback file with matching names.
- Forward applies with `alembic upgrade head`; rollback is `alembic downgrade -1`.
- A migration that touches the append-only ledger requires a database-role update script in the same change.
- Pre-commit smoke test on a clean Postgres: forward → app boots → rollback → forward → app boots.

## Idempotency key

Every state-changing endpoint accepts an `idempotency_key` (header or JSON field) and rejects duplicate keys within a 24-hour window by returning the original result.

## Common pitfalls

1. Casting a stored `TIMESTAMP WITHOUT TIME ZONE` to "Europe/Paris" at read time and treating it as truth.
2. `SELECT SUM(...)::money` and then `float(money)` somewhere upstream.
3. Storing `total_cents` derived from `line_total` that already disagrees with the line.
4. Letting an `idempotency_key` be reused after a 200 response for a different payload.
5. Adding a customer data column without an approved feature.

## Verification checklist

- [ ] Ledger UPDATE/DELETE revoked at the DB level for the app role in production migrations.
- [ ] No `float` in money arithmetic.
- [ ] Every `TIMESTAMP` is `TIMESTAMPTZ`.
- [ ] VAT columns store rate + base + tax per line, with documented rounding.
- [ ] Privacy gate green.
- [ ] Migrations replay forward/back/forward with the app booting.
- [ ] Idempotency keys tested for duplicate POST and conflicting replay.
