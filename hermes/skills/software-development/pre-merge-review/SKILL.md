---
name: pre-merge-review
description: Require independent non-author review before merging code
version: 1.0.0
metadata:
  hermes:
    tags: [development, review, merge-gate]
    category: software-development
---

# Pre-Merge Review — The Gate

## When to Use

Before merging any change that touches product code, after
`speckit-implement` is finished and all automated success criteria pass.
Docs, config, test-only, and formatting-only changes skip this and merge on
green checks alone.

## Procedure

1. Confirm scope: does this diff touch actual application logic (not just
   docs/config/tests)? If not, this skill doesn't apply — merge on green
   checks.
2. Get a review from someone or something that is **not** the author of the
   change:
   - If a second model/agent is available (a different Hermes session, a
     different provider), hand it the diff and the plan's "What we're NOT
     doing" section, and ask it to review for: correctness against the spec,
     scope creep against the "NOT doing" list, and anything the automated
     tests wouldn't catch.
   - If no second agent is available, this is a hard stop: ask the user to
     review, or wait for one to become available. Do not self-review and
     call it done — an absent review is a `NEEDS-FIX`, not a pass.
3. The reviewer reports a verdict: `SHIP-OK` or `NEEDS-FIX` (with specifics).
   An ambiguous or missing verdict is treated as `NEEDS-FIX` — fail closed.
4. On `NEEDS-FIX`, address the findings and re-run this skill. Do not merge
   around it.
5. On `SHIP-OK`, merge. Then check the merged diff for any migration files —
   if found, apply them immediately (don't wait to be asked) and verify the
   resulting schema matches what the migration intended.

## Pitfalls

- Treating "CI is green" as equivalent to "reviewed." Green CI proves the
  suite runs and passes — it doesn't prove the suite (or the reviewer)
  checked the right things.
- Self-reviewing because no second agent was readily available, instead of
  stopping and asking. An absent review is not the same as a passing one.
- Merging on a vague or partial verdict ("looks mostly fine") instead of
  treating it as `NEEDS-FIX` until it's unambiguous.

## Verification

- [ ] The reviewer was not the author of the change.
- [ ] A verdict was actually returned — `SHIP-OK` or `NEEDS-FIX` — not
      inferred or assumed.
- [ ] Any migrations in the merged diff were applied and the resulting
      schema was checked, not just assumed to have worked.
