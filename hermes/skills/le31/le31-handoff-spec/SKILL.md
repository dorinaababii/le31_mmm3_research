---
name: le31-handoff-spec
description: Use when packaging an LE31 research or feature decision into a self-contained handoff so a different coding agent can build the agreed slice without needing the original conversation. Produces the trigger policy, mandatory inputs, frozen contract, verification protocol, handoff summary, and sign-off gap.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, handoff, contract, coding-agent]
    related_skills: [le31-conventions, le31-research, le31-v1-feature-pattern, development, speckit-specify]
---

# LE31 Handoff to External Coding Agent

## Overview

This skill packages an LE31 decision into a frozen build contract. A different coding agent will read this package instead of the original research chat. If the agent cannot act from the package alone, the package is incomplete.

## When to Use

- After research and the LE31 feature gate have accepted a new feature.
- Before handing work to a separate coding agent, contractor, or team.
- When a long-running research phase ends and implementation starts.
- Any time a different agent must inherit work without prior conversation.

Do not use for in-session implementation by the same Hermes instance. Do not use for feature contracts that have not yet cleared the feature gate.

## Required Inputs

Before producing a handoff, the package must include:

- LE31 feature gate verdict for this slice.
- The matching `docs/features/<id>-<name>.md` contract.
- Conflicting or resolved charter questions that affect the slice.
- The mandatory LE31 skill list the external agent must load.
- Trigger policy and disambiguation text for the external agent.
- Existing model, route, bot, or UI files the slice will touch.
- Verification protocol and end-to-end acceptance path.
- A linear task ID or equivalent durable identifier.

Completion: a stranger who has read only this package can implement and verify the feature.

## Required Outputs

Generate these artifacts:

1. **`<slug>-HANDOFF.md`** — the build contract for the coding agent.
2. **`<slug>-PROMPT.md`** — a copy-pasteable prompt that the `le31-coding-agent-brief` skill would produce.
3. **`<slug>-CONTEXT.json`** — machine-readable summary with feature ID, scope, required skills, evidence pointer, verification steps, and link back to the source artifact.

Always reference, do not duplicate, the persistent materials. Use stable paths only.

## Frozen Contract Discipline

Once the handoff is sent:

- Do not silently change the slice, scope, or verification path.
- Do not rename identifiers that the external agent now relies on.
- Surface any new evidence or change to the user, then patch the package and re-send.
- The external agent must mirror back the frozen contract before implementing and stop if it cannot.

## Verification Protocol

The external agent verifies:

- its read of the contract matches the recorded contract fields
- the slice does not require another skill, model, or migration outside the package
- the end-to-end acceptance path is executable in the configured environment
- the rollback or feature-removal path is present and reversible

## Common Pitfalls

1. Pasting a chat excerpt as a handoff instead of producing a structured contract.
2. Forgetting the mandatory skill list, so the external agent reinvents LE31 conventions.
3. Adding new product behavior between research and hand-off without re-running the feature gate.
4. Hiding charter conflicts instead of stating the chosen resolution.
5. Letting the external agent invent verification paths instead of using frozen ones.

## Verification Checklist

- [ ] Feature gate verdict is recorded.
- [ ] Feature contract, conflicting-charter resolutions, and pinpointed files are linked.
- [ ] Mandatory LE31 skill list is named.
- [ ] Verification protocol and rollback path are present.
- [ ] External agent loaded the same contract and confirmed the trigger policy.
- [ ] Status and Linear or equivalent reference match reality.
