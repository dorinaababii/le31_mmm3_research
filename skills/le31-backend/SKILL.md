---
name: le31-backend
description: Use when implementing or reviewing LE31 FastAPI, SQLModel, aiogram, services, endpoints, Telegram flows, configuration, permissions, or backend integration. Keeps business rules centralized, state transitions explicit, and operations idempotent.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, backend, fastapi, sqlmodel, aiogram]
    related_skills: [le31-conventions, le31-data, le31-v1-feature-pattern]
---

# LE31 Backend

## Overview

The backend serves waiter web actions and cook Telegram actions over one set of domain rules. Routers and handlers translate input; services own business operations; models and database constraints protect persistence.

## When to Use

Use for FastAPI routes, aiogram handlers/FSM, SQLModel sessions, service logic, configuration, auth/allowlists, polling, health checks, and deployment behavior.

## Boundaries

Routers/handlers validate transport input, identify actor, call one domain operation, and map feedback. Services enforce transitions, permissions, calculations, idempotency, and transactions. Models/data layer define persistence and constraints. Do not duplicate stock, bill, order-state, or permission rules in API and bot.

## Operation Pattern

Define actor/permission, input units, state precondition, duplicate behavior, transaction boundary, emitted rows/events (especially `StockEntry`), visible success, and recoverable errors. Completion: the same domain operation behaves consistently from every surface.

## FastAPI

Use explicit request/response models; keep sessions request-scoped and transactions short; return stable actionable errors; make health checks meaningful; keep secrets in settings/environment; add dependencies only for demonstrated needs.

## aiogram

Use v3 and pin the working version. Restrict handlers before mutation. Keep FSM resumable and cancellable. Assume callbacks can be delivered twice. Acknowledge callbacks promptly, show resulting state, and use long polling until a webhook is explicitly required.

## Verification

Start the app and bot, call realistic endpoints, press Telegram callbacks when applicable, inspect persisted rows, and observe waiter/cook feedback. For a bugfix, demonstrate the failure before the fix and rerun it afterward.

## Common Pitfalls

1. Putting business logic in routers.
2. Writing stock outside the order-state transaction.
3. Assuming Telegram delivery is exactly once.
4. Returning success before persistence.
5. Logging tokens or unnecessary PII.
6. Claiming completion from `/docs` presence alone.

## Verification Checklist

- [ ] Actor, permission, precondition, idempotency, transaction, and effects are explicit.
- [ ] API and bot use the same domain rule.
- [ ] Invalid and duplicate actions are tested.
- [ ] Rows and user feedback were observed.
- [ ] Secrets and unnecessary PII are absent.
