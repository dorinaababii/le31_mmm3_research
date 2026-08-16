# segment-seam-ledger-rotation — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/73-segment-seam-ledger-rotation.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `73`
- Slug: `segment-seam-ledger-rotation`
- Contract file: `features/73-segment-seam-ledger-rotation.md`
- Bucket: **v2 utility (watch-list)** — defer; feature 49 prerequisite not yet shipped
- Linear parent: `Brainstorm 2026-08-16 — daily` (TBD; created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list record)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (GitHub `topic:append-only` cluster — `nradawg/segment-seam-chain` pushed 2026-08-15T21:45:59Z + `nradawg/skew-ratchet-clock` pushed 2026-08-15T21:22:06Z, both 0★, MIT, same author same day; cluster-shipping rate of 5+ repos in a 24-hour window for the same broad topic).

**Confidence:** **medium** for the JTBD shape (the pattern is well-established in the broader ecosystem), **low** for the LE31-specific pain (no observed pain at the LE31 owner level; feature 49 not yet shipped).

**Decision: defer (watch-list).** The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. Circuit breaker: delete this file + the corresponding `INDEX.md` row; no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules; even though this is v2 utility, the slicing discipline inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-16).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/73-segment-seam-ledger-rotation.md   # NEW (this artifact)
specs/segment-seam-ledger-rotation-HANDOFF.md # NEW (this file)
INDEX.md                                       # EDIT: append one row to "Active feature pipeline" table
```

Zero source files touched. Zero migrations. Zero new config keys. Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/73-segment-seam-ledger-rotation.md` and confirm it matches the brainstorm report's "73-segment-seam-ledger-rotation" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-16), pick slug (`segment-seam-ledger-rotation`), feature path (`features/73-segment-seam-ledger-rotation.md`), and Linear sub-issue ID.
3. **On a future daily-research pass**: re-query the GitHub `topic:append-only` cluster and confirm the same-author same-day push pattern persists. If the cluster continues to ship segment-rotation + monotonic-clock primitives, the watch re-activates (re-evaluate the gate).

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID `fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature` (label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 73 — segment-seam ledger rotation`.
- Body: the contract from `features/73-segment-seam-ledger-rotation.md` (or a short summary + the file path).
- Parent: `Brainstorm 2026-08-16 — daily` (the Linear index issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/73-segment-seam-ledger-rotation.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other code changes to revert. No data migration to revert.

## Why this matters (for the coding agent)

The append-only `StockEntry` ledger is **the LE31 differentiator** (PROJECT_CHARTER.md + 16+ feature files reference it). Feature 49 covers the per-row tamper-evidence; this feature would cover the rotation boundary. **The pair is the production-grade append-only ledger pattern** that the LE31 charter implicitly assumes but does not yet ship.

**Risk of NOT tracking**: the rotation-threshold problem will surface after feature 49 is in production for 6-12 months. If the watch-list is not already in place when that happens, the build will be rushed. The watch exists to ensure the pattern is already-evaluated when the trigger condition arrives.

**Risk of over-tracking**: feature 49 is not yet shipped. The watch-list artifact is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the watch-list under "defer until feature 49 ships to production and the rotation threshold is observable." Re-evaluate when feature 49 lands.
