---
name: speckit-implement
description: Execute tasks in order, verifying each one before moving on
version: 1.0.0
metadata:
  hermes:
    tags: [development, spec-driven, implement, tdd]
    category: software-development
---

# Implement — Build

## When to Use

After `speckit-tasks` has produced an ordered task list. Last step before
`pre-merge-review`.

## Procedure

1. Work tasks in dependency order. Mark each one's status as you go so
   progress survives a context reset.
2. Prefer tests-first where the task involves logic worth protecting: write
   the test, watch it fail for the right reason, then make it pass.
3. For a bugfix specifically: the regression test must fail on the unfixed
   code. Write it, run it, watch it fail, apply the fix, run it again, watch
   it pass. A test that only ever passed proves nothing about the fix.
4. After each task, run its automated success criteria yourself — don't
   mark it done because the code looks right. Run the command, read the
   output.
5. Don't scope-creep. If you notice an unrelated improvement while
   implementing, note it — don't fold it into this change. Check the plan's
   "What we're NOT doing" section if unsure whether something's in scope.
6. When all tasks with automated criteria are done and verified, stop and
   report which manual success criteria (from the plan) still need a human
   to check. Do not self-certify those — that's the user's call.
7. Hand off to `pre-merge-review` before this merges anywhere.

## Pitfalls

- Declaring a task done because the diff looks plausible. Run it.
- Silently softening a test's assertion to make it pass — that's not a pass,
  that's removing the protection the test existed for.
- Three failed attempts at the same bug and reaching for a fourth patch
  instead of stepping back — that's a sign your model of the system is
  wrong, not that you need one more try.
- Marking manual verification items as done yourself. You can't observe a UI
  the way a human can — say "ready for manual verification" and stop.

## Verification

- [ ] Every task's automated criteria were actually run, not assumed.
- [ ] Any bugfix has a test that was observed failing before the fix and
      passing after.
- [ ] Manual verification items are reported to the user, not self-checked.
- [ ] Nothing outside the plan's scope got folded into this change.
