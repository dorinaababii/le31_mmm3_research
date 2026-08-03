---
name: le31-feature-pipeline
description: Use after le31-daily-research (or any feature proposal that passed the gate). Turns the proposal into ready-to-build artefacts: feature contract, draft Linear issue, slice handoff contract, then commits and pushes to main.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, features, pipeline, linear, github]
    related_skills: [le31-daily-research, le31-conventions, le31-v1-feature-pattern, le31-handoff-spec, le31-coding-agent-brief]
---

# LE31 Feature Pipeline

## Overview

Takes a passed-gate feature pick and produces the deliverables the coding agent needs to build it, persisted in the right places.

## When to Use

- Daily after `le31-daily-research`.
- Manual after any research that produces a feature proposal.

## Procedure

1. Receive the three picks from `le31-daily-research`.
2. For each pick:
   - Decide the bucket: v1 / v2 / v2-AI / new.
   - If new, justify the bucket in the contract.
3. Write `features/NN-<slug>.md` using the existing v1 feature template:
   Goal / Scope / Out of scope / Description / Data model / Implementation steps / Telegram interaction if any / Dependencies / Open questions / Why this matters.
4. Create or draft a Linear sub-issue in the matching project (`le31 v1 — Core MVP`, `le31 v2 owner-pains`, or `le31 v2-AI`) with the contract body and label `Feature`.
5. Write a `*-HANDOFF.md` slice contract for the coding agent under `specs/` that includes:
   - the active feature path
   - the seven-check gate verdict
   - the files to touch
   - verification protocol reference
   - rollback path
   - the mandatory LE31 skill list
6. Commit and push to the branch named in the skill config (default: main).
7. Add a row to `/opt/data/INDEX.md` "active feature pipeline" table with date, pick, feature path, Linear ID.

## Hard rules

- The coding-agent-brief skill produces the paste-in prompt automatically from the slice contract; do not paste chat excerpts.
- The contract must be sufficient for the coding agent to start without asking.
- If the pick fails the gate, do not write a contract; report rejection instead.

## Verification checklist

- [ ] Feature contract file written.
- [ ] Linear sub-issue created with matching label and project.
- [ ] Slice handoff file under specs/.
- [ ] Commit and push confirmed.
- [ ] /opt/data/INDEX.md pipeline row added.
