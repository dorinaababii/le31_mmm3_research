---
name: le31-conventions
description: Use when proposing, researching, specifying, planning, implementing, or reviewing any LE31 change. Applies the project invariants and the evidence-first seven-check feature gate before work proceeds.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, restaurant, conventions, feature-gate]
    related_skills: [development, speckit-specify, le31-research]
---

# LE31 Conventions

## Overview

This is the global LE31 decision layer. Use the generic `development` pipeline for code; use this skill to keep every decision aligned with the restaurant, owner, architecture, and data invariants.

## When to Use

Use for every LE31 feature proposal, research question, specification, plan, implementation, review, or operational change. Do not use as a substitute for the generic coding workflow.

## Source-of-truth order

1. Current explicit user decision.
2. `docs/PROJECT_CHARTER.md` and the matching `docs/features/*.md` contract.
3. Current repository behavior and tests.
4. Linear for task status and durable decisions.
5. Research reports for evidence, never as automatic product requirements.

When sources conflict, stop and expose the exact conflict. Do not silently pick the newest-looking or easiest rule.

## Hard invariants

- Product: one small restaurant and two primary operational surfaces—waiter web UI and cook Telegram bot.
- Stack: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres in production. A stack change requires an explicit charter decision.
- Stock: every prepared-item quantity change is a new `StockEntry`. Never update or delete ledger events. Current stock is derived from entries.
- State: operational transitions are explicit user actions. Do not silently send, serve, close, or reconcile an order.
- AI: no customer-facing AI. AI may assist owner/staff, with observable evidence and a non-AI fallback.
- Money: never use binary floats. Preserve exact EUR values and explicit tax/tip derivations.
- Business time: persist timezone-aware instants and render business dates in `Europe/Paris`.
- Privacy: store only data needed for restaurant operations; v1 guest demographics are counts, not identity or contact data.
- Truth: GitHub is source of truth for files and code; Linear for work and decisions; `/opt/data` for local reports. Never fabricate research results or execution output.

## Feature gate

Run this before agreeing to a new feature or material scope change. Produce a short answer for each item; do not manufacture numerical precision.

### Evidence precondition

Classify the pain as **observed**, **reported**, **inferred**, or **assumed**. Record the evidence and confidence (`high`, `medium`, `low`). An assumed pain becomes a small experiment, not a full feature.

### Seven checks

1. **Raison d'être / JTBD** — Write: “When ___, the owner/waiter/cook wants to ___, but struggles because ___, so that ___ improves.” Link it to an existing feature or justify a new pain.
2. **Viability** — Can the non-technical owner and staff understand, operate, recover, and maintain it without hidden administration or recurring specialist help?
3. **Practicability and confidence** — Does it fit the fixed stack? Are required data, permissions, integrations, infrastructure, and AI capability available? Name rabbit holes and evidence strength.
4. **Conflict** — Does it violate any invariant, decided non-goal, data rule, privacy boundary, or explicit state transition? A hard conflict blocks the proposal until redesigned or explicitly overridden.
5. **Outcome, appetite, and scope** — Which v1/v2/v2-AI outcome does it serve? Set the maximum time worth spending. Keep time fixed and cut scope if the solution grows.
6. **Cost to operational value** — Compare pain frequency/severity and money/time/error avoided against implementation, training, and maintenance cost. Use ICE/RICE concepts only as vocabulary, not fake arithmetic.
7. **Circuit breaker and reversibility** — Define stop evidence, review point, disable/delete path, migration/rollback cost, retained data, and what remains safe if removed. Run a pre-mortem for high-risk or irreversible work.

Decision: **build**, **experiment**, **defer**, or **reject**. State the failed or uncertain checks before proceeding.

## Workflow

- Product behavior: `development` → specify → plan → tasks → implement → independent review.
- Research: load `le31-research`; persist evidence before making recommendations.
- UI: show or update an `index.html` mock-up before backend behavior when the interaction is new or materially changed.
- Progress: commit and push coherent artifacts as they are completed; do not wait until the whole initiative ends.
- Scope: build exactly the accepted outcome. Unrequested abstractions and features are defects.

## Known conflicts to surface

The charter currently contains historical inconsistencies, including integer-cents versus `Decimal`, Postgres-only versus SQLite development, migration strategy, and some v1 deployment details. Treat the matching feature spec plus current explicit user decision as required resolution; never encode both interpretations in code.

## Common Pitfalls

1. Using RICE or MoSCoW as the build gate. They rank candidates after evidence and feasibility; they do not replace this gate.
2. Treating research novelty as user demand. A paper or release is evidence about possibility, not evidence of restaurant pain.
3. Calling an automatic transition “convenient.” Explicit operational state is a deliberate safety principle.
4. Declaring done from a diff or passing tests alone. Exercise the waiter/cook/owner behavior that changed.

## Verification Checklist

- [ ] Evidence and confidence recorded.
- [ ] All seven checks answered.
- [ ] Decision is build, experiment, defer, or reject.
- [ ] No unresolved source-of-truth conflict was guessed through.
- [ ] Observable behavior was exercised before claiming completion.
