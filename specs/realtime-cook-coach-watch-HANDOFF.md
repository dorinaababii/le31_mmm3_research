# realtime-cook-coach-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/51-realtime-cook-coach-watch.md` before touching any code. This is a
> **parking-lot** slice — no build, no commit, no follow-up. The
> artifact exists so when the operator does report feature 38 as a
> problem, the path is documented.

## Frozen identifiers (do not rename)

- Feature ID: `51`
- Slug: `realtime-cook-coach-watch`
- Contract file: `features/51-realtime-cook-coach-watch.md`
- Bucket: parking-lot (no build)
- Linear parent: HMM-52 (Brainstorm 2026-08-09 — daily) [predicted; will be confirmed on issue creation]
- Linear sub-issue: HMM-55 (created, status Backlog, label `Feature`, project `le31 v1 — Core MVP`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "LE31 gate verdict per idea" → Pick C.
**Decision: parking-lot.** No failed checks; the gate is **deferred** until the operator reports feature 38's choppy pattern as a problem or asks for a real-time conversational Q&A on the live ledger.

Evidence precondition: **observed** (1 in-window GitHub repo —
`pathorsAI/parley` 13★, pushed 2026-08-09T06:30:31Z — documents the
real-time-mid-task-AI-coach category trend). Confidence: **high** for the
category trend, **low** for "we need to migrate today".

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

**No files.** This is a paper artifact. The feature file
`features/51-realtime-cook-coach-watch.md` is the deliverable.

## Endpoints and contracts added

**No new endpoints.** No new bot commands. No new schema.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above.
2. **Verify**: open `features/51-realtime-cook-coach-watch.md` and confirm
   the contract is complete (Goal, Scope, Out of scope, Description,
   Evidence/JTBD, Why this matters).
3. **Verify**: search the codebase for any commit referencing
   `pathorsAI/parley` or `realtime-cook-coach` — expect **zero**
   matches (no build happened).
4. **Regression**: confirm feature 38 (`cook-voice-note-to-stockentry`)
   is still in Backlog, untouched, and operational.
5. **Regression**: confirm feature 48 (`pipecat-voice-watch`) is still
   in Backlog as a *parallel* watch (the *infrastructure* side of the
   same category trend) and is not modified by this slice.

## Rollback / feature-removal path

- Delete `features/51-realtime-cook-coach-watch.md`.
- Delete `specs/realtime-cook-coach-watch-HANDOFF.md`.
- Archive Linear sub-issue HMM-55.
- No code changes; no migration; no data retention.

## What remains safe if removed

- Feature 38 is unaffected.
- Feature 48 is unaffected.
- The append-only `StockEntry` ledger is unaffected.
- The privacy invariant is preserved.
- The bot still works.

## When to revisit

- The operator reports feature 38's choppy pattern as a problem
  ("the choppy pattern is annoying because I want to interrupt mid-note",
  or "the choppy pattern misses overlapping voices during service rush",
  or "I want to ask the bot how much ricotta I have left without typing").
- A future brainstorm surfaces a stronger real-time-cook-coach evidence
  (e.g. a 50★+ cook-voice-coach project, or a peer restaurant-POS that
  ships real-time conversational Q&A on the live ledger).
- v3 planning cycle considers the real-time conversational modal a v3 priority.

Until any of those fires, this is a paper artifact.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-52)
back to the research-side Hermes before "implementing". If they
conflict, **stop and ask** — do not silently rename. (And note that
"implementing" here means "no implementation, just acknowledging the
paper artifact exists.")
