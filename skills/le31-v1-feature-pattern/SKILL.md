---
name: le31-v1-feature-pattern
description: Use when specifying, planning, implementing, or reviewing an LE31 v1 feature. Enforces the project’s feature-contract shape, thin end-to-end slices, explicit non-goals, dependencies, and observed waiter/cook/owner acceptance paths.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, v1, feature, acceptance]
    related_skills: [le31-conventions, development, speckit-specify]
---

# LE31 v1 Feature Pattern

## Overview

A v1 feature is a thin operational slice, not a backend endpoint in isolation. The contract connects a real restaurant pain to data, one or more user surfaces, and an observable acceptance path.

## When to Use

Use for v1 feature work and material changes to a v1 contract. Do not use to pull v2 or v2-AI work into v1.

## Canonical Contract

Every feature specification contains: Goal; Evidence/JTBD; Scope; Out of scope; User flow; Data model; API/bot/UI contract; Dependencies; Failure/recovery; Definition of done; Open questions.

Completion: the contract contains no unresolved blocker and a developer can derive a plan without inventing product behavior.

## Slicing Rules

- Build model → domain operation → interface → realistic verification as one coherent slice.
- Preserve explicit state changes. Name allowed and rejected transitions.
- Keep one owner-visible outcome per feature; split work crossing v1/v2/v2-AI.
- Reuse project primitives before adding abstractions.
- For stock effects, name the exact append-only `StockEntry` event and when it is written.
- For money effects, name the exact derivation and rounding rule.

## Implementation Handoff

The plan identifies files/interfaces, schema or migration impact, API/bot/UI surfaces, permissions/configuration, verification cases including duplicates and invalid transitions, and the feature-removal path. Tasks are dependency ordered and independently verifiable; no placeholder tasks.

## Definition of Done

Done means the specified user completes the flow on the intended surface, resulting rows and derived values are inspected, forbidden and duplicate actions are safe, promised feedback appears, the regression gap was demonstrated where applicable, docs/status match reality, and the change is committed and pushed.

## Common Pitfalls

1. Treating a router response as an end-to-end feature.
2. Omitting failure recovery because v1 is small.
3. Adding v2 convenience during v1 implementation.
4. Writing a StockEntry effect as an update to current stock.
5. Accepting “tests pass” without running the actual waiter/bot/UI path.

## Verification Checklist

- [ ] Goal, evidence, scope, non-goals, flow, data, contracts, dependencies, recovery, DoD, and questions are present.
- [ ] Scope belongs entirely to v1.
- [ ] State, stock, and money effects are explicit.
- [ ] End-to-end acceptance path was observed.
- [ ] Status, docs, commit, and push reflect the result.
