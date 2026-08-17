# telegram-agent-control-plane-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/78-telegram-agent-control-plane-watch.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `78`
- Slug: `telegram-agent-control-plane-watch`
- Contract file: `features/78-telegram-agent-control-plane-watch.md`
- Bucket: **v2-AI (watch-list)** — defer; LE31 already ships the surface (features 58/61/63/68)
- Linear parent: `Brainstorm 2026-08-17 — daily` (HMM-94, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list record)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (GitHub `topic:telegram-bot` cluster — `Mftrferdinand/Zeline` 64★ 2026-08-17T06:11:36Z + `H4fizWasabie/mino-agent` 14★ 2026-08-17T06:37:56Z + `viggomeesters/arr-orchestrator` 0★ 2026-08-17T06:27:12Z + `motu001/dsh-phone-bridge` 0★ 2026-08-17T05:04:33Z + `BosTheCoder/claude-concierge` 1★ 2026-08-17T06:16:46Z + `Nicotinamide/dsh-plugin-tg-bridge` 0★ 2026-08-17T04:10:15Z — 6 repos in 48h, all Python/Go/JS, all converging on chat-driven operational control).

**Confidence:** **medium** for the pattern convergence (the cluster is real and the timestamps are within 48h); **low** for LE31-specific pain (no observed pain at the LE31 owner-pain level; LE31 already ships the surface).

**Decision: defer (watch-list).** The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. Circuit breaker: delete this file + the corresponding `INDEX.md` row; no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules; even though this is v2-AI, the slicing discipline inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-17).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/78-telegram-agent-control-plane-watch.md   # NEW (this artifact)
specs/telegram-agent-control-plane-watch-HANDOFF.md # NEW (this file)
INDEX.md                                             # EDIT: append one row to "Active feature pipeline" table
```

Zero source files touched. Zero migrations. Zero new config keys. Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/78-telegram-agent-control-plane-watch.md` and confirm it matches the brainstorm report's "78-telegram-agent-control-plane-watch" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-17), pick slug (`telegram-agent-control-plane-watch`), feature path (`features/78-telegram-agent-control-plane-watch.md`), and Linear sub-issue ID.
3. **On a future daily-research pass**: re-query the GitHub `topic:telegram-bot` cluster and confirm the 6 in-window peers (Zeline, mino-agent, arr-orchestrator, dsh-phone-bridge, claude-concierge, dsh-plugin-tg-bridge) sustain or grow. If any crosses ≥10★ sustained for 7+ days, the watch re-activates (re-evaluate the gate).

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID `fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature` (label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 78 — telegram-agent-control-plane-watch`.
- Body: the contract from `features/78-telegram-agent-control-plane-watch.md` (or a short summary + the file path).
- Parent: `Brainstorm 2026-08-17 — daily` (HMM-94, the Linear index issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/78-telegram-agent-control-plane-watch.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other code changes to revert. No data migration to revert.

## Why this matters (for the coding agent)

The LE31 cook-bot operational-control surface is **the LE31 v2-AI differentiator** (PROJECT_CHARTER.md + features 58/61/63/68). The 6-repo in-window cluster confirms that the surface is at a 2026-08 convergence inflection point in the broader GitHub ecosystem. If the pattern is mainstream, LE31's strategic posture is validated; if it stays niche, LE31 can reallocate the v2-AI budget to other surfaces.

**Risk of NOT tracking**: the pattern may consolidate in 2026-H2; if the watch-list is not in place when that happens, LE31 either re-derives the same conclusions (wasted cycles) or misses the consolidation (strategic risk).

**Risk of over-tracking**: the pattern is observed at the repo level only; the watch-list is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the watch-list under "defer until either observed pain or peer-velocity re-activates it." Re-evaluate when one of the 6 peers crosses ≥10★ sustained for 7+ days.
