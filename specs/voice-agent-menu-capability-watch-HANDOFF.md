# voice-agent-menu-capability-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/80-voice-agent-menu-capability-watch.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `80`
- Slug: `voice-agent-menu-capability-watch`
- Contract file: `features/80-voice-agent-menu-capability-watch.md`
- Bucket: **new (out-of-scope v1; v2-AI candidate)** — parking-lot; charter-out-of-scope
- Linear parent: `Brainstorm 2026-08-17 — daily` (HMM-94, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list record)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**inferred** (1 in-window 0★ repo `csloki-ab/voice-caller` 2026-08-17T02:50:39Z, no observed pain, no owner survey).

**Confidence:** **low** for the modality-crossing inflection (one repo is an observation, not a trend); **zero** for the LE31-specific pain.

**Decision: parking-lot (charter-out-of-scope, no observed pain).** The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. Circuit breaker: delete this file + the corresponding `INDEX.md` row; no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-17).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/80-voice-agent-menu-capability-watch.md   # NEW (this artifact)
specs/voice-agent-menu-capability-watch-HANDOFF.md # NEW (this file)
INDEX.md                                            # EDIT: append one row to "Active feature pipeline" table
```

Zero source files touched. Zero migrations. Zero new config keys. Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/80-voice-agent-menu-capability-watch.md` and confirm it matches the brainstorm report's "80-voice-agent-menu-capability-watch" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-17), pick slug (`voice-agent-menu-capability-watch`), feature path (`features/80-voice-agent-menu-capability-watch.md`), and Linear sub-issue ID.
3. **On a future daily-research pass**: re-query the GitHub `restaurant` cluster and confirm whether a future ≥10★ voice-restaurant repo validates the demand. If yes, the watch re-activates (re-evaluate the gate). If `csloki-ab/voice-caller` crosses ≥10★ sustained for 7+ days, the watch may upgrade.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID `fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature` (label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 80 — voice-agent-menu-capability-watch`.
- Body: the contract from `features/80-voice-agent-menu-capability-watch.md` (or a short summary + the file path).
- Parent: `Brainstorm 2026-08-17 — daily` (HMM-94, the Linear index issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/80-voice-agent-menu-capability-watch.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other code changes to revert. No data migration to revert.

## Why this matters (for the coding agent)

The 2026-08-17 observation of `csloki-ab/voice-caller` is the **first in-window data point** that AI menu-capability is crossing the modality boundary (text → voice). If 2026-08 is the inflection month, LE31's text-based cook bot may face a UX gap by 2027. The watch-list is parked because the LE31 stack does not yet import voice; if the inflection becomes a trend, the LE31 charter must be revised to include voice.

**Risk of NOT tracking**: if the inflection becomes a trend in 2026-H2 and the watch-list is not in place, LE31 either re-derives the same conclusions (wasted cycles) or misses the inflection (strategic risk).

**Risk of over-tracking**: the inflection is observed at the repo level only (1 repo, 0★); the watch-list is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the watch-list under "parking-lot — charter-out-of-scope, no observed pain." Re-evaluate when (a) a future ≥10★ voice-restaurant repo validates the demand, (b) the LE31 owner surveys surface voice pain, or (c) the charter is revised to include voice.
