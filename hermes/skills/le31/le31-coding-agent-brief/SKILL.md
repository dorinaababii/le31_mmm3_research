---
name: le31-coding-agent-brief
description: Use when generating a ready-to-paste prompt that packages an LE31 build slice for an external coding agent. Embeds the trigger sentence, read-first file list, hard constraints, verification protocol, mandatory LE31 skills to load, and stop conditions in one block.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, coding-agent, brief, prompt]
    related_skills: [le31-conventions, le31-handoff-spec, le31-v1-feature-pattern, le31-data, le31-backend, le31-frontend, le31-finance-analytics, development]
---

# LE31 Coding-Agent Brief

## Overview

A short, copy-pasteable instruction block that primes an external coding agent for one frozen LE31 slice. It references the handoff package, forces the agent to load the LE31 skills, and prescribes verification before completion.

## When to Use

- When handing a slice to Kimi, Claude Code, Cursor, or any external coding agent.
- When generating a session bootstrap for a fresh agent on a new surface.
- When the user requests a paste-in prompt for a third-party agent.

Do not use for research or planning-only requests.

## Procedure

### 1. Confirm package readiness

If `le31-handoff-spec` is not complete, finish it before producing the brief.

### 2. Assemble the trigger sentence

Open the brief with a single load-the-package directive naming the slice ID and the path to the handoff document.

### 3. List the mandatory inputs

Include only the stable paths the external agent must read before any code is written: charter, handoff doc, feature file, mandatory skills, and confirmation of the frozen contract fields.

### 4. Embed the hard constraints

Set explicit behavior for:

- read everything in the listed order, then stop and confirm before coding
- load the LE31 skills before any decision
- do not change stack or silently resolve charter contradictions
- implement only the contracted slice
- run the end-to-end acceptance path before claiming done
- commit, push, and report with the required evidence

### 5. Define the verification protocol

Spell out the commands, inspection steps, and observable user flow the agent must run and record. Include the explicit rollback or feature-removal path.

### 6. Set stop conditions

List the conditions under which the agent must pause and ask, including blocked reading, missing source-of-truth resolution, scope drift, charter contradictions, and persistent test failures.

### 7. Final closing sentence

End with a single line that asks for a mirror-back of the contract and a confirmation before any implementation begins.

## Brief Shape

```markdown
Load the LE31 build package before any code.

You are building slice <id> for the LE31 restaurant app.
Package: <repo-path>/<slug>-HANDOFF.md
Feature contract: <repo-path>/docs/features/<file>.md

Read first, in this order:
1. <repo-path>/docs/PROJECT_CHARTER.md
2. <repo-path>/docs/HANDOFF.md
3. <repo-path>/docs/features/<file>.md
4. <repo-path>/hermes/skills/le31/le31-conventions/SKILL.md
5. <repo-path>/hermes/skills/le31/le31-v1-feature-pattern/SKILL.md
6. Add only the LE31 skills named in <slug>-HANDOFF.md.
7. <repo-path>/<slug>-HANDOFF.md

Hard constraints:
- Do not change the stack or silently resolve charter contradictions.
- Implement only the contracted slice.
- Keep stock events append-only and money exact.
- Make operational state transitions explicit.
- No customer-facing AI surfaces.

Verify before declaring done:
- Reproduce the end-to-end acceptance path on the configured environment.
- Inspect the actual database rows after the change is applied.
- Confirm forbidden transitions and duplicate actions are safe.
- Run lint, type check, and tests available in this repo, then commit and push.

Stop and ask if:
- The read-first list is missing a needed file.
- Charter, feature file, or current code disagree and the resolution is not documented.
- The slice requires a new dependency, model, or migration outside the package.
- Verification fails twice on the same root cause.

Before coding, mirror back the slice ID, the required skills, the verification protocol, and the rollback path. Confirm or correct each, then begin.
```

## Common Pitfalls

1. Forgetting the load-the-package trigger at the top.
2. Referencing a chat excerpt or path inside this conversation rather than a stable repository path.
3. Listing skills to optionally load; the LE31 skills must load.
4. Omitting the stop conditions, so the agent invents scope or stack changes.
5. Ending the brief without a mirror-back request.

## Verification Checklist

- [ ] Handoff package is complete.
- [ ] Brief opens with load-the-package directive and stable paths.
- [ ] Read-first order and mandatory LE31 skills are explicit.
- [ ] Hard constraints, verification protocol, and stop conditions are present.
- [ ] Brief ends with mirror-back confirmation before implementation.
- [ ] Repository was read back, referenced paths exist, and skill names resolve.
