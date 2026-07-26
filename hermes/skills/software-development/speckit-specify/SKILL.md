---
name: speckit-specify
description: Capture what/why for a feature before any code or plan
version: 1.0.0
metadata:
  hermes:
    tags: [development, spec-driven, specify]
    category: software-development
---

# Specify — What & Why

## When to Use

First step of the `development` pipeline for anything that touches code.
Run after the `development` router has decided this needs the full pipeline,
before `speckit-plan`.

## Procedure

1. Restate the request as a problem statement: what's broken or missing, for
   whom, and why it matters. If you can't state this in 2-3 sentences, ask
   the user before going further — an unclear spec produces a wrong plan.
2. Write the spec in **technology-agnostic** terms. No framework names, no
   file paths, no implementation detail — that belongs in the plan phase.
   A spec that says "use Postgres" instead of "persist orders durably" has
   leaked an implementation decision too early.
3. Include, at minimum:
   - **Problem** — what's wrong today.
   - **Goal** — what "fixed" looks like, in observable terms.
   - **Non-goals** — what this explicitly does NOT cover. This section is
     what the reviewer checks scope-creep against later — don't skip it.
   - **Open questions** — anything genuinely ambiguous. Resolve what you can
     by asking the user now; leave the rest only if truly optional.
4. Save it:
   - If the project's `AGENTS.md` names a Linear project, create a spec issue
     there.
   - Otherwise, write `specs/NNN-feature-name/spec.md` in the project root
     (NNN = next unused 3-digit number).

## Pitfalls

- Sneaking a "how" into the "what." If a sentence names a library or a file,
  cut it — it belongs in the plan.
- Skipping non-goals. Without them, `pre-merge-review` has no scope boundary
  to check extras against, and scope creep sails through.
- Writing a spec nobody could disagree with. If a spec is so vague that any
  implementation would satisfy it, it isn't specifying anything.

## Verification

- [ ] A person unfamiliar with the request could read the spec and know what
      "done" looks like.
- [ ] Non-goals section exists and says something concrete.
- [ ] No implementation details (frameworks, file paths, library names) leaked
      into the spec.
