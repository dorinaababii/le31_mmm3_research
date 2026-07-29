---
name: le31-verification-protocol
description: Use immediately before claiming a feature is done in the LE31 coding-agent repository. Defines the exact sequence of observable behaviour to execute, with evidence to capture and known blockers.
version: 1.0.0
author: Hermes Agent (research side)
license: MIT
metadata:
  hermes:
    tags: [le31, verification, done, evidence, e2e]
    related_skills: [le31-quality-gates, le31-conventions-coder, le31-data-correctness]
---

# LE31 Verification Protocol

## Overview

A feature is "done" only after this protocol is run against the target environment and evidence is recorded. The protocol is ordered from cheap to expensive, with mandatory observations at every step.

## Standards anchor

- **NIST SP 800-218 SSDF PW.8** — test executable code in its target environment.
- **NIST SP 800-218 SSDF RV.1** — vulnerability response and recovery discipline.
- **NIST SP 800-92** — log management and retention as part of evidence.

## Sequence

### 1. Static gates

Run the gates from `le31-quality-gates`:

```bash
ruff check . && mypy --strict app/ && pip-audit --strict && bandit -r app/ -ll
gitleaks detect --no-banner
```

Expected: zero findings. Failure here stops the protocol.

### 2. Migrations against a clean database

```bash
make migrate-fresh
make migrate-rollback
make migrate-fresh
```

Expected: forward succeeds, rollback succeeds, second forward succeeds.

### 3. Append-only enforcement

```bash
psql "$DATABASE_URL" -c "UPDATE stock_entry SET qty_delta = 0 WHERE id = 1"
```

Expected: `ERROR: permission denied` or `ERROR: append-only constraint`.

### 4. End-to-end happy path with the actor roles

Run the slice's manual test script with cook, waiter, and owner roles, in that order. Capture: timing, observed responses, payload inspections.

Required evidence per slice:

- HTTP responses with status, headers, body
- aiogram callback log (whether the cook received the message)
- Database row inspections with literal SQL
- One screenshot per UI surface change

### 5. Failure paths

For each named failure path:

- duplicate callback delivered twice (must be idempotent or reject)
- bot command from an unauthorised chat_id (must reject)
- concurrent updates with two waiters editing the same visit (one wins, the other gets INVALID_TRANSITION)
- network drop after POST but before response (client retried safely)

### 6. Reconciliation

```sql
SELECT SUM(qty_delta) AS stock_ledger_total
FROM stock_entry
WHERE item_id = $1 AND created_at < date_trunc('day', now() AT TIME ZONE 'Europe/Paris');

SELECT SUM(quantity) AS derivation_total
FROM view_current_stock
WHERE item_id = $1;
```

Expected: identical values. A non-zero delta blocks the slice.

### 7. Privacy gates

```sql
SELECT column_name FROM information_schema.columns
WHERE table_schema = 'public' AND (
  column_name ILIKE '%phone%' OR
  column_name ILIKE '%email%' OR
  column_name ILIKE '%name%' OR
  column_name ILIKE '%pan%'
);
```

Expected: only columns from the explicit approved feature list.

### 8. Logging gates (OWASP A09)

For each operation, assert in tests that exactly one event row is emitted with `correlation_id`, `actor`, `occurred_at`, `surface`, and the value delta. Assert no PII in the payload schema.

### 9. Rollback rehearsal

Run the documented rollback/feature-removal path on a copy of production data. Confirm the system returns to the prior observable behaviour. Record command outputs.

### 10. Documented evidence

Save under `coding-agent/evidence/<slice-id>/`:

- `static-gates.txt`
- `e2e.log`
- `db-dump.sql` (anonymised if it contains customer data)
- `screenshots/*.png`
- `rollback.log`
- `disclosure.md`

## Known limits (honest)

- Screenshots verify appearance; only end-to-end observation verifies behaviour.
- Reconciliation depends on the view's correct implementation — test the view separately.
- OWASP coverage is not a substitute for an audit; A01 access-control policies still need policy review.

## Common pitfalls

1. Claiming done from "tests pass" without an end-to-end run.
2. Skipping failure paths.
3. Not reading back screenshots — trusting they captured the right state.
4. Letting synthetic seed data substitute for a real Postgres test.

## Verification checklist

- [ ] Static gates clean.
- [ ] Migrations replay.
- [ ] Append-only enforced at the DB level.
- [ ] Happy + failure paths observed in the target environment.
- [ ] Reconciliation matches to zero.
- [ ] Privacy columns vetted against the approved list.
- [ ] Logging emits correlation IDs and value deltas with no PII.
- [ ] Rollback rehearsed.
- [ ] Evidence artefacts archived under `coding-agent/evidence/<slice-id>/`.
