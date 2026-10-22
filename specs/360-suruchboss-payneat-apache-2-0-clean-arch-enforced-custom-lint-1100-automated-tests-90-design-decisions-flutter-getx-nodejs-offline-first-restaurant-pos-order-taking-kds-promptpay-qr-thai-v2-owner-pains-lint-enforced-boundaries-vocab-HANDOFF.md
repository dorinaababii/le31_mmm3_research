# HANDOFF — Feature 360 · Architecture boundaries as lint failures (build, v2 owner-pains)

**Date:** 2026-10-22 · **Feature:** `features/360-suruchboss-payneat-apache-2-0-...-lint-enforced-boundaries-vocab.md`
**Source:** [`SuruchBoss/PaynEat`](https://github.com/SuruchBoss/PaynEat) — Apache-2.0 ✓ §3.2 · ★5/⑂4 · Dart off-stack · created 2026-09-07, pushed 2026-10-21
**Linear:** not attached — write endpoint blocked (34th day), `requestId a4e6a0548d28d2de`

## Why this slice is next

Cheapest pick in the series. No migration, no new entity, no user surface, no runtime behaviour change — and it removes a recurring class of reviewer error. The unverified part is named below rather than glossed.

## Upstream references

| Ref | Detail |
|---|---|
| Repo | https://github.com/SuruchBoss/PaynEat |
| Licence | Apache-2.0 (verified via `GET /repos/SuruchBoss/PaynEat`, 2026-10-22) |
| Description | *"Restaurant POS built with Clean Architecture (enforced via custom lint), 1,100+ automated tests, and 90+ documented design decisions. Flutter/GetX + Node.js — order taking, kitchen display, real PromptPay QR, offline mode."* |
| Topics | 17, incl. `offline-first`, `point-of-sale`, `restaurant-management`, `sqlite`, `thai` |
| In-window | `pushed_at` **only** (2026-10-21); created 2026-09-07 |
| **Unverified claim** | *"1,100+ automated tests"* and *"90+ documented design decisions"* are **self-reported by the author and were NOT independently counted.** Do not cite these numbers as fact. |

**Adoption posture: vocabulary only.** Dart/Flutter/GetX is off-stack and not adopted. The transferable item is the *mechanism* — lint as the enforcer, with the error message naming the correct destination.

## Slice

1. **Verify open question 1 first:** does LE31 have a `domain/` layer today? If not, slice 1 is a directory move, not a lint rule.
2. Choose **one** harness: `ruff` + `flake8-tidy-imports`, or `import-linter`. **Not both.**
3. Rules 1–2 (domain purity): domain must not import FastAPI; domain must not import SQLModel or open a session.
4. Rules 3–4 (channel boundary): aiogram handlers hold no business logic; no Telegram types outside `channels/`.
5. **Every message names the allowed destination.** "Put transport types behind the adapter in `api/`" — not "import not allowed".
6. Wire into the existing check command.
7. **Run it and record what it finds before changing the rules.** A clean first run means the rules are wrong, not that the codebase is perfect.

## Acceptance

- `make lint-boundaries` (or the existing check) fails on a deliberately-introduced violating import.
- Each of the four rules has at least one verified triggering case in the test.
- Every message names its destination.
- The pre-existing violation count is recorded in the PR body.

## Risks

| Risk | Severity | Mitigation |
|---|---|---|
| LE31 has no `domain/` layer — this is a refactor, not a lint change | **high** | Check before starting; size the slice accordingly. |
| Rules fire on legitimate code → disabled within a week | high | Measure the violation count first. Tune the rules before enforcing. |
| Lint harness choice turns into a debate | low | Pick one, move on. The mechanism matters, the harness does not. |
| Two overlapping harnesses installed | low | Explicitly forbidden by step 2. |

## Reversibility

**Fully reversible.** Delete four lint rules and one config block. No data, no migration, no runtime effect.

## Rollback trigger

If the rules fire on legitimate code more than a handful of times in the first two weeks and the fix is consistently "disable the rule", the rules are miscalibrated — fix or remove them. A disabled-but-retained boundary rule is worse than none, because it teaches the team to ignore the output.