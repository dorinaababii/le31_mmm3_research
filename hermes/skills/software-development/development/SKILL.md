---
name: development
description: Router for all coding work - decides process and next skill
version: 1.0.0
metadata:
  hermes:
    tags: [development, workflow, spec-driven, router]
    category: software-development
---

# The Development Process

The router for all coding work. It decides **how much process** a change
needs and **which skill runs next**. It owns almost no content of its own —
every step below is a skill in this same pack, and this file is the map.

## When to Use

Invoke this first, before writing or editing any code — a bug fix, a
refactor, a one-line change, a new feature. It is the entry point, not an
optional step. See `SOUL.md` for why: skipping straight to code is where a
misunderstanding of the system turns into thousands of bad lines instead of
one bad line of plan.

## Procedure

### 1. Triage — right-size the process

| The work | Lane |
|---|---|
| A **non-code** edit — comment/doc typo, formatting, a config value with no behavior change | Just do it. Not a spec-worthy change. |
| One coherent change, one area, you can see the whole thing | **Solo pipeline** — specify → plan → tasks → implement, you do it. |
| Several independent slices, or wide/cross-cutting change | **Fleet pipeline** — same pipeline, but delegate slices to subagents (`skill_manage`-spawned subagents or Hermes' parallel session support) once tasks are broken down. |
| Nobody knows what "done" looks like yet | **Stop.** Ask clarifying questions before planning. Do not plan an unclear thing. |

The dial is on research, not on the pipeline. You may skip deep research when
the change is genuinely well-understood. You may not skip specify → plan →
tasks → implement for anything touching code — even a one-line change gets a
short spec.

### 2. The pipeline

```
  /speckit-specify ──► /speckit-plan ──► /speckit-tasks
                                                │
                                                ▼
  merged ◄── pre-merge-review ◄── /speckit-implement
```

| Phase | Skill | Owns |
|---|---|---|
| Specify | `speckit-specify` | **What & why.** Technology-agnostic. |
| Plan | `speckit-plan` | **How.** Module boundaries, interfaces. |
| Break down | `speckit-tasks` | Dependency-ordered units of work. |
| Build | `speckit-implement` | The code. Tests first where practical. |
| Gate | `pre-merge-review` | An agent that is **not the author** signs off. |
| Land | (manual/CI) | Merge, then apply any pending migrations. |

Each phase is a separate skill invocation (`/speckit-specify`, etc.) — stack
them or run them one at a time, whichever fits the platform you're in.

### 3. Where artifacts live

If this project's `AGENTS.md` names a Linear project, store specs/plans/tasks
there (requires the Linear MCP server — see the pack's `README.md` for setup).
If no Linear project is named, use a local `specs/NNN-feature-name/` directory
in the project root with `spec.md`, `plan.md`, `tasks.md`. Check the project's
`AGENTS.md` before starting — don't guess which one applies.

### 4. The non-negotiables

Full list lives in `SOUL.md` (loaded globally, so it's always in context) —
this is the short version specific to code:

1. Every code change goes through specify → plan → tasks → implement.
2. Never skip or weaken a check to get green.
3. Product code merges on green checks *and* an independent review.
4. Apply pending migrations immediately after merge — don't wait to be asked.
5. Verify before claiming done — see "Done means observed" in `SOUL.md`.

## Pitfalls

- Treating "the task looks small" as license to skip specify/plan. Size the
  *depth* of research to the task, not whether the pipeline runs at all.
- Writing a plan with placeholder tasks ("handle edge cases," "add tests for
  the above") — whoever executes them will guess. Resolve every open
  question before finalizing a plan.
- Declaring a phase done because the code compiles or the summary sounds
  right, without actually running the thing.
- Skipping `pre-merge-review` because CI is green — green CI proves the
  suite passes, not that the suite asserts the right things.

## Verification

Before calling any coding task complete, confirm:
- [ ] A spec and plan exist for the change (or the change was non-code and
      genuinely didn't need one).
- [ ] The implementation was actually run/tested, not just read back.
- [ ] `pre-merge-review` returned a pass (or the change was docs/config/test
      only and skipped it deliberately).
- [ ] Any migrations in the merged diff were applied and verified.
