# pipecat-voice-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/48-pipecat-voice-watch.md` before touching any code. This is
> a **parking-lot** slice — no build, no commit, no follow-up. The
> artifact exists so when the operator does report feature 38 as a
> problem, the path is documented.

## Frozen identifiers (do not rename)

- Feature ID: `48`
- Slug: `pipecat-voice-watch`
- Contract file: `features/48-pipecat-voice-watch.md`
- Bucket: parking-lot (no build)
- Linear parent: HMM-50 (Brainstorm 2026-08-08 — daily)
- Linear sub-issue: HMM-53 (created, status Backlog, label `Feature`, project `le31 v1 — Core MVP`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: parking-lot.** No failed checks; the gate is **deferred** until the operator reports feature 38's choppy pattern as a problem.

Evidence precondition: **observed** (1 in-window GitHub repo —
`pipecat-ai/pipecat` 13991★, pushed 2026-08-08T04:00:13Z — documents
the voice-agent stack has matured). Confidence: **high** for the
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
`features/48-pipecat-voice-watch.md` is the deliverable.

## Endpoints and contracts added

**No new endpoints.** No new bot commands. No new schema.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above.
2. **Verify**: open `features/48-pipecat-voice-watch.md` and confirm
   the contract is complete (Goal, Scope, Out of scope, Description,
   Evidence/JTBD, Why this matters).
3. **Verify**: search the codebase for any commit referencing
   `pipecat` or `voice-agent` — expect **zero** matches (no build
   happened).
4. **Regression**: confirm feature 38 (`cook-voice-note-to-stockentry`)
   is still in Backlog, untouched, and operational.

## Rollback / feature-removal path

- Delete `features/48-pipecat-voice-watch.md`.
- Delete `specs/pipecat-voice-watch-HANDOFF.md`.
- Archive Linear sub-issue HMM-53.
- No code changes; no migration; no data retention.

## What remains safe if removed

- Feature 38 is unaffected.
- The bot still works.
- The append-only `StockEntry` ledger is unaffected.
- The privacy invariant is preserved.

## When to revisit

- The operator reports feature 38's choppy pattern as a problem
  ("the choppy pattern is annoying because I want to interrupt mid-note",
  or "the choppy pattern misses overlapping voices during service rush").
- A future brainstorm surfaces a stronger voice-agent evidence
  (e.g. a 20000+★ voice-OSS project, or a peer restaurant-POS that
  ships real-time voice).
- v3 planning cycle considers the voice modal a v3 priority.

Until any of those fires, this is a paper artifact.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-50)
back to the research-side Hermes before "implementing". If they
conflict, **stop and ask** — do not silently rename. (And note that
"implementing" here means "no implementation, just acknowledging the
paper artifact exists.")
