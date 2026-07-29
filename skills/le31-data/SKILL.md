---
name: le31-data
description: Use when changing LE31 SQLModel models, Postgres schema, stock, order, payment, audit, migration, retention, or reporting data. Protects the append-only StockEntry ledger and reproducible business calculations.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, data, postgres, sqlmodel, ledger]
    related_skills: [le31-conventions, le31-backend, le31-finance-analytics]
---

# LE31 Data

## Overview

LE31 data must explain what happened in the restaurant. Prefer immutable events and derived views over quietly editable totals, while keeping the single-restaurant schema simple.

## When to Use

Use for models, constraints, indexes, migrations, queries, backups, reports, stock, orders, bills, shifts, and any feature that reads or writes operational history.

## Stock Ledger Invariant

- A quantity change inserts one `StockEntry`; it never mutates or deletes an existing entry.
- Each entry identifies item/batch, signed quantity delta, reason/source, actor, and timezone-aware creation instant as defined by the active schema.
- Current and historical stock are derived from qualifying entries.
- Corrections are compensating entries with an explicit correction reason.
- Generic CRUD for ledger rows is forbidden.
- Production Postgres must enforce append-only behavior at the database boundary.
- Zero-crossing and sold-out notification behavior must be idempotent under concurrent requests.

## Schema Change Procedure

Read the feature contract and models; state the invariant and historical-query requirement; design constraints/indexes/deletion behavior; resolve the charter’s migration contradiction before implementation; define forward/rollback behavior; test duplicates/concurrency/history; apply the schema and read it back. Completion: schema, model, and observed database behavior agree.

## Data Rules

- Persist timezone-aware instants; derive restaurant dates in `Europe/Paris`.
- Never store authoritative money as binary floating point. Follow the resolved explicit project decision for integer cents versus `Decimal`; the repository has conflicting historical guidance.
- Make state transitions explicit and reject invalid transitions.
- Keep PII out unless separately approved.
- Reports derive from source rows; forecasts preserve history and provenance.
- Verify backup/restore before production claims.

## Query Discipline

Index observed paths: active visit by table, today’s menu, stock by item/batch/time, open orders, closed bills by business date, and recent ledger entries. Avoid speculative indexes.

## Common Pitfalls

1. Adding mutable `qty_remaining` as truth beside the ledger.
2. Correcting events with UPDATE or DELETE.
3. Computing Paris “today” by slicing UTC text.
4. Mixing integer cents, Decimal, and float.
5. Relying only on application checks for critical invariants.
6. Calling a migration safe without applying it and reading back the result.

## Verification Checklist

- [ ] Source event and invariant are named.
- [ ] Append-only behavior is database-enforced.
- [ ] Constraints, indexes, deletion, and timezone semantics are explicit.
- [ ] Migration conflicts were resolved, not guessed.
- [ ] History, duplicate, and concurrent cases were tested.
- [ ] Actual schema and rows were inspected.
