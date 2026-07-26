---
name: speckit-plan
description: Turn an approved spec into a concrete implementation plan
version: 1.0.0
metadata:
  hermes:
    tags: [development, spec-driven, plan]
    category: software-development
---

# Plan — How

## When to Use

After `speckit-specify` has produced a spec (in Linear or `specs/NNN/spec.md`).
Read the spec fully before writing anything — do not plan from a paraphrase
you remember from the conversation.

## Procedure

1. Re-read the spec. If anything in it is ambiguous enough to change the
   plan depending on interpretation, ask the user now — resolving an
   ambiguity mid-implementation is far more expensive.
2. Decide the technical approach: module boundaries, interfaces, data model
   changes, which files/areas are touched. This is where framework and
   library choices belong — they were deliberately excluded from the spec.
3. Write a **"What we're NOT doing"** section, distinct from the spec's
   non-goals — this one is about implementation choices you're deliberately
   not making (e.g. "not adding a caching layer," "not migrating the old
   endpoint yet"). `pre-merge-review` checks the diff against this list.
4. For each phase of work the plan implies, write two kinds of success
   criteria:
   - **Automated** — a command that proves it (tests pass, build succeeds,
     a migration applies cleanly). Whoever implements this runs it
     themselves.
   - **Manual** — what a human needs to eyeball (the UI actually works, no
     regression in a neighboring flow). These get flagged for the user, not
     self-certified.
5. No placeholders. "Add appropriate error handling," "handle edge cases,"
   "similar to the above" are not plan items — they're a guess waiting to
   happen for whoever implements this. If you don't know the answer yet,
   that's an open question to resolve now, not a task to write down vaguely.
6. Save alongside the spec (same Linear project, or `specs/NNN/plan.md`).

## Pitfalls

- Planning around an assumption instead of asking. If the spec is silent on
  something the plan needs to decide, that's a question, not a place to
  guess.
- Skipping the "NOT doing" section — without it, scope creep during
  implementation has nothing to be checked against.
- Writing automated-only success criteria for something that clearly needs
  human eyes (visual UI, UX flow, anything the user will actually look at).

## Verification

- [ ] Every phase has both automated and manual success criteria.
- [ ] "What we're NOT doing" section exists and is specific.
- [ ] No open questions remain unresolved — either answered or explicitly
      deferred with the user's sign-off.
