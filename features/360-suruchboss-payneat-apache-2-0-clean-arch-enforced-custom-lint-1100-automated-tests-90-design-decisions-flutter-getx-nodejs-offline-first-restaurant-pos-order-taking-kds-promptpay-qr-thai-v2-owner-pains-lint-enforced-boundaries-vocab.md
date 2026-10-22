# Feature 360 — `suruchboss-payneat-apache-2-0-clean-arch-enforced-custom-lint-1100-automated-tests-90-design-decisions-flutter-getx-nodejs-offline-first-restaurant-pos-order-taking-kds-promptpay-qr-thai-v2-owner-pains-lint-enforced-boundaries-vocab` (build)

> **Pick B of Daily Brainstorm 2026-10-22 (pass 83).** Documents in-window GitHub repo `SuruchBoss/PaynEat` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**), **★5/⑂4**, **Dart/Flutter OFF-STACK** but the *discipline* is language-neutral and directly portable to LE31's Python 3.13 charter, **created 2026-09-07, pushed 2026-10-21** — in-window by `pushed_at` only; the repo is ~6 weeks old. 17 topics including `offline-first + point-of-sale + restaurant-management + sqlite + thai`. Bucket: **v2 owner-pains**. Verdict: **`build`**.

## Goal

Make the LE31 architecture boundary **mechanically enforced rather than reviewer-enforced**. The separation between domain logic, floor/channel, and adapters should fail the build when violated, not appear in a convention document that drifts the first time someone is in a hurry.

## Scope

**In scope:**

- One lint rule per load-bearing boundary. The candidate set, in priority order:
  1. **Domain must not import FastAPI.** Pure domain logic, no framework types.
  2. **Domain must not import SQLModel or open a session.** Persistence is an adapter concern.
  3. **aiogram handlers must not contain business logic** beyond routing and formatting.
  4. **No module may import a Telegram type** except under `channels/`.
- A single command (`make lint-boundaries` or a pre-commit hook) that runs them, wired into the existing check.
- The rule *messages* must say **where the dependency is allowed to live**, not merely that it is forbidden. A lint error that names the correct destination converts a blocker into a 10-second fix.

**Out of scope:**

- Adopting Dart/Flutter, GetX, or the repo's codebase. Off-stack; vocabulary only.
- A general-purpose architecture linter. Build the four rules LE31 needs, not a framework.
- Enforcing test coverage thresholds. The repo advertises 1,100+ tests; LE31 has no coverage gate and this contract does not add one — that is a separate decision, not a free rider.
- Documenting the 90 design decisions. Recorded as a signal about the repo, not adopted as a deliverable.

## Evidence / JTBD

**Gate check 1 (JTBD) passes, and unusually cleanly** — the job is one the *development process* has, not one the product has: *when a contributor adds a feature, they want the architecture boundary to hold automatically, but it currently holds only because reviewers remember to check, so violations get merged under review pressure and the layer boundary erodes silently.* This is a real job with a real current cost, and it is the **owner-pains** bucket in its most literal sense: LE31's owner (the person who also writes the code) is the one who pays when the boundary erodes.

- **Evidence class**: **observed claim about the repo's own process**. The description states *"Clean Architecture (enforced via custom lint), 1,100+ automated tests, and 90+ documented design decisions."* This is **self-reported by the repo author and was NOT independently verified** — the count of tests and decisions was not checked. The *technique* (lint as an enforcer) is the transferable item and does not depend on those counts being accurate.
- **Confidence**: **high** that lint-based boundary enforcement is a real and workable practice. **Medium** on the repo's execution quality at ★5. **Explicitly not claimed**: that 1,100 tests is accurate, or that the boundaries LE31 needs match theirs.
- **Traction**: ★5/⑂4 with a **1 fork per 1.25 stars** ratio — small but unusually fork-heavy, which for a project of this type suggests people actually forked it to use the pattern.

## Description

The conventional way to hold an architecture boundary is a written convention plus reviewer diligence. Both decay: the document goes stale, and the reviewer is human. `PaynEat`'s move is to make the boundary a **lint error**, so the machine checks what the reviewer forgets under pressure.

The transferable insight for LE31 has two halves, and the second half is the more valuable one:

1. The boundary is a lint rule, not a document.
2. **The lint message names the correct destination.** "Domain layer must not import FastAPI — put transport types behind the adapter in `api/`" is a 10-second fix. "Import not allowed" is a 30-minute investigation. A rule that blocks without directing is a rule that gets disabled.

## Data model

None. This contract changes no entities, no migrations, no runtime behaviour.

## Implementation steps

1. Pick the lint harness. LE31 is Python 3.13; `ruff` covers import-boundary rules via `flake8-tidy-imports` `ban-relative-imports`-style config, or `import-linter` if its contract DSL is preferred. **Choose one — do not run both.**
2. Encode rules 1 and 2 (domain purity) first. They are the two the checklist in `le31-conventions` treats as non-negotiable.
3. Encode rules 3 and 4 (channel boundary) second.
4. Write the messages with destinations.
5. Wire into the existing check command.
6. Run it. **Expect violations.** Record what it finds before deciding whether the rules are right — if the first run is clean, the rules are probably wrong.

## Telegram interaction

None. Explicitly none — this is a development-time contract and ships no user surface.

## Dependencies

- A Python lint harness already present in the repo (if not, `ruff` is the lightest addition).
- The existing LE31 layer convention, which this contract makes mechanical rather than aspirational.

## Open questions

1. **Does LE31 actually have a `domain/` layer today?** If not, rule 1 is unenforced because there is nothing to enforce against, and the first slice is a directory move rather than a lint rule. **Unverified — must be checked before implementation.**
2. **How much friction is right?** A boundary rule that fires often on legitimate code will be disabled within a week. Start by measuring.
3. **Should the rule be a warning initially?** Defensible for one release, but a warning that is never promoted is worse than no rule, because it trains the team to ignore the output.

## Why this matters

Every other `v2 owner-pains` pick in this series has proposed a *tool*. This one proposes a *constraint*, and constraints are cheaper to maintain: a lint rule either keeps firing or gets deleted, whereas a convention document quietly becomes fiction. It also directly reduces the cost of the passes that come after it, because the next contributor's first mistake is caught by the machine.

---

**Gate verdict: `build`.** Passes all three gate checks — real JTBD, permissive licence, small stack-native change. **No hard conflict, fully reversible** (delete four lint rules to undo it), and the downside if wrong is mild friction on legitimate code. The honest caveats: the repo's headline test-count claim is unverified, and open question 1 is unresolved — if LE31 has no `domain/` layer yet, this is partly a refactor rather than purely a lint change, which affects the size estimate. v2 owner-pains bucket. Attached to `le31 Research` P-HMM-1 in the fallback payload only — **not attached in Linear** (write endpoint blocked, 34th consecutive day).