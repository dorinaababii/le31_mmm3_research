---
name: le31-arch-patterns
description: Use when designing or reviewing the structure of new LE31 features — endpoints, services, handlers, models, FSM states, and the append-only money/stock event flow. Defines the architectural patterns the coding agent must follow.
version: 1.0.0
author: Hermes Agent (research side)
license: MIT
metadata:
  hermes:
    tags: [le31, architecture, patterns, fsm, ledger]
    related_skills: [le31-conventions-coder, le31-data-correctness, le31-backend]
---

# LE31 Architecture Patterns

## Overview

Architecture rules for the coding agent. These are the patterns the system must follow across every feature. Diverging requires a written justification in the commit and the handoff.

## Standards anchor

- **Append-only event stores** as audit backbone. NIST SP 800-92 (Guide to Computer Security Log Management) treats logs as sensitive artefacts requiring tamper protection and retention discipline. Pair with double-entry accounting's "equal-and-opposite entries" so every event is reconfirmable from rows. Source: NIST SP 800-92; double-entry bookkeeping principle.
- **Explicit state machines** instead of silent mutations. NIST SP 800-218 v1.1 PW.4–PW.6 require identified, reviewable flows; silent transitions break PW.7 (code review).
- **Domain operation pattern**: every UI handler calls exactly one service-layer operation. No business logic in router/handler code.

## Layered architecture

```
routers / aiogram handlers
        │  (validate, identify actor, map result)
        ▼
services                  ← exactly one operation per action
        │
        ▼
data layer (SQLModel, SQL constraints, append-only enforcers)
```

- **Routers / handlers**: input validation, actor identification, single service call, response mapping. No business rules.
- **Services**: state transitions, permissions, calculations, idempotency, transactions, event emission.
- **Data layer**: persistence shape + DB constraints, including append-only enforcement.

Same domain operation must behave identically from every UI surface.

## Event-driven backbone

The stock and money flows are append-only event stores. Every change is one event. Corrections are compensating events with explicit cause.

```
post event → DB CHECK: no UPDATE/DELETE possible
build views (current stock, today's revenue, …) by summing or joining events
```

Event payload minimum:

```
id, occurred_at (TZ-aware UTC), event_type, source, actor, item_ref, qty_delta, money_delta, reason, correlation_id
```

## Finite state machine pattern

Every domain object exposes a small, named FSM. Transitions are explicit user actions.

```
DRAFT → SENT → IN_PROGRESS → READY → SERVED → CLOSED
                         ↘ CANCELED
```

- Names are constants, not free text.
- Every transition is callable by exactly one service operation.
- Invalid transitions return a stable, named error (e.g. `INVALID_TRANSITION`).
- Concurrent duplicates are handled idempotently.

## Domain operation contract

Every service operation names:

- actor identity and required permission
- input schema and units
- state precondition
- duplicate behaviour (idempotent or reject)
- transaction boundary
- emitted events (StockEntry / MoneyEvent) and side effects
- success result and recoverable errors

Completion: the same operation behaves identically from every UI surface.

## Concrete patterns

### Money pattern

```python
@total.ordering
class Money:
    cents: int
    currency: str = "EUR"

    def __add__(self, other): ...
    def __mul__(self, n): ...       # integer multipliers only
    def display(self) -> str: ...    # "12,50 €" — derived for UI
```

Never `float`. Always `int cents` for storage and arithmetic, formatted for display only.

### Stock event

```python
class StockEntry(BaseModel, table=True):
    id: UUID
    item_id: int
    qty_delta: int                  # signed
    reason: Literal["prep", "order", "waste", "manual_adjust"]
    source: Literal["bot", "ui", "import"]
    actor: int
    created_at: datetime            # TZ-aware UTC
```

Current stock is `SUM(qty_delta)` filtered by active item, never stored beside the ledger.

### FSM transition

```python
def mark_ready(self, *, actor):
    self._assert_can("mark_ready", actor)
    self.status = "READY"
    self._emit_event(OrderEvent(type="ready", at=now_paris(), actor=actor))
```

`status` exists only to index; truth lives in the event log.

## Anti-patterns (refuse)

- Storing `current_stock` beside the ledger.
- Calculating totals in browser JavaScript.
- `current_total_paid` and `expected_total` diverging silently.
- Hiding FSM transitions inside generic CRUD.
- Auto-progressing orders when timers expire.

## Verification checklist

- [ ] Every action is implemented by exactly one service operation.
- [ ] Domain FSM states, transitions, and preconditions are explicit.
- [ ] Stock and money changes go through append-only events.
- [ ] Money arithmetic uses integer cents or `Decimal` only.
- [ ] No `current_*` field duplicates a derivation that the event store can answer.
