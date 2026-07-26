---
name: speckit-tasks
description: Break an approved plan into dependency-ordered tasks
version: 1.0.0
metadata:
  hermes:
    tags: [development, spec-driven, tasks]
    category: software-development
---

# Tasks — Break Down

## When to Use

After `speckit-plan` has produced a plan. Before `speckit-implement`.

## Procedure

1. Read the full plan. Break it into units of work small enough that each
   one has a clear, checkable "done" — a task like "build the feature" is
   too big; "add the `orders` table migration" is right-sized.
2. Order tasks by dependency, not by convenience. If task 5 needs the schema
   from task 2, task 2 comes first regardless of what's more interesting to
   build.
3. Each task inherits its automated/manual success criteria from the plan
   phase it belongs to — don't invent new criteria at this stage, just scope
   them to the task.
4. Group tasks into phases/milestones if the plan is large enough to warrant
   it (e.g. "Phase 1: schema," "Phase 2: API," "Phase 3: UI").
5. Save as a task list alongside the spec/plan (Linear issues under the
   feature label, or `specs/NNN/tasks.md`).

## Pitfalls

- Tasks that are really "go figure out how to do X" — that's still planning
  work, and it means the plan phase wasn't actually finished. Push it back.
- Ordering by file instead of by dependency — grouping "all the frontend
  tasks" together when one of them actually depends on a not-yet-built API
  from a later "backend" task.

## Verification

- [ ] Every task has a single, checkable definition of done.
- [ ] Dependency order is correct — no task requires something that comes
      later in the list.
- [ ] Nothing in the plan was left out of the task list.
