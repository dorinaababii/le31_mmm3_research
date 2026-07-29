---
name: le31-conventions-coder
description: Use before writing any code in the LE31 coding-agent repository. Enforces the LE31 hard invariants (append-only stock, exact-money, Europe/Paris, explicit state transitions, no customer-facing AI, stack discipline) and runs the seven-check feature gate.
version: 1.0.0
author: Hermes Agent (research side)
license: MIT
metadata:
  hermes:
    tags: [le31, conventions, invariants, gate]
    related_skills: [le31-arch-patterns, le31-data-correctness, development]
---

# LE31 Conventions — Coding Agent

## Overview

The single source of "what is non-negotiable" while coding LE31 features. If a coding decision contradicts anything in this skill, stop and surface the conflict. Do not silently "improve" the stack.

## Standards anchor

This skill is defensible against published sources:

- **Money must not be float.** (IEEE 754 — `0.1` is not representable in binary.) Use integer minor units (`cents`) or `Decimal`. Source: Martin Fowler, *Patterns of Enterprise Application Architecture* — Money pattern (2003); Husobee (2016) `husobee.github.io/.../never-use-floats-for-currency.html`.
- **Timestamps must be timezone-aware.** Use Python `datetime` with `tzinfo=Europe/Paris`. Persist in UTC, render in Europe/Paris. Source: IETF RFC 3339 §5.6 + IANA tzdb.
- **Append-only stock and money events.** No UPDATE/DELETE on posted rows. Source: double-entry bookkeeping principle + Daniel Whittaker, "Is a Provable Audit Log Possible? With Event Sourcing It Is" (2014) + NIST SP 800-92.
- **Operators are non-technical.** Tailor UX. Source: Nielsen 10 heuristics (1994, last reviewed 2024); GOV.UK Service Standard.

## Hard invariants (refuse to break)

- Stack: Python 3.13, FastAPI, SQLModel, Postgres (SQLite for dev only), aiogram v3. Adding a dependency requires a checkpoint commit and a written justification.
- No customer-facing AI. All AI is owner- or operator-facing only.
- Operational state transitions are explicit user actions. Never silent auto-progress.
- Money is integer cents or `Decimal`. Never float for authoritative totals.
- Persist timezone-aware instants; render business dates in `Europe/Paris`.
- Customer data limited to what GDPR Art. 5(1)(c) data-minimisation permits. No PAN, no contact data, no identity unless an approved feature explicitly requires it.
- Single-currency EUR until the owner revokes it.
- Closed orders and bills are immutable. Corrections are compensating events.
- Reproducible: any state derivable from rows must be derivable, not stored beside them.

## Seven-check feature gate

Before writing any feature, produce a one-line answer to each. If the answer to any is `unknown`, the feature cannot start.

1. **Raison d'être** — which restaurant pain is served? (link to v1-XX / v2-XX / v2-AI-XX or justify as new)
2. **Owner operability** — can a non-technical operator run, recover, and explain this?
3. **Stack & data fit** — fits the fixed stack without new dependencies, schema, or permissions?
4. **Conflict** — does it violate any invariant, non-goal, or privacy boundary?
5. **Scope** — v1 / v2 / v2-AI? If new, justify.
6. **Cost-vs-value** — implementation + training + maintenance cost vs. pain avoided?
7. **Circuit breaker** — what evidence stops the work; can the feature be disabled safely; is there a migration cost?

Decision: `build`, `experiment`, `defer`, or `reject`. State the failing checks before proceeding.

## Mandatory reading order (before any code)

1. `docs/PROJECT_CHARTER.md`
2. `docs/features/<id>-<name>.md`
3. `hermes/skills/le31/le31-conventions-coder/SKILL.md` (this skill)
4. `hermes/skills/le31/le31-arch-patterns/SKILL.md`
5. `hermes/skills/le31/le31-data-correctness/SKILL.md`
6. Add only the LE31 skills named in the active handoff or feature file.
7. The active handoff contract `*-HANDOFF.md`.

Then stop and confirm the read before coding.

## Common pitfalls

1. New Python dependency without a checkpoint commit + justification.
2. `float` in money arithmetic.
3. Joining tables on timestamps as text without TZ awareness.
4. Editing posted ledger rows in place.
5. Optimistically closing orders or auto-sending to the kitchen.
6. Storing customer name/phone/email/PAN by default.
7. Calling a feature "done" without an end-to-end observation.

## Verification checklist

- [ ] Feature gate answered, including circuit breaker.
- [ ] All hard invariants still hold after the change.
- [ ] All mandatory LE31 skills loaded before coding.
- [ ] No silent contract change.
- [ ] Commit, push, and a Linear/equivalent status update recorded.
