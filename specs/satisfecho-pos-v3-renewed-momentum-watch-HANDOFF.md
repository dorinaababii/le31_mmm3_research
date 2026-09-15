# Spec 180 — `satisfecho-pos-v3-renewed-momentum-watch` (HANDOFF)

**Source feature:** `features/180-satisfecho-pos-v3-renewed-momentum-watch.md`
**Parent research issue:** HMM-241
**Linear sub-issue:** HMM-243
**Filed:** 2026-09-15 by the LE31 daily-research cron

---

## Active feature path

- **Repo:** `dorinaababii/le31_mmm3_research.git` (working dir: `/opt/data/le31_mmm3_research_work/`)
- **Feature spec file:** `features/180-satisfecho-pos-v3-renewed-momentum-watch.md`
- **This HANDOFF file:** `specs/satisfecho-pos-v3-renewed-momentum-watch-HANDOFF.md`

## Seven-check gate verdict

| # | Check | Status |
|---|---|---|
| 1 | Goal stated | PASS (document the renewed-momentum data point; cross-reference features 40 + 42) |
| 2 | Evidence / JTBD stated | PASS (43★ + 15 forks + NEW PUSH today + AGPL-block retained) |
| 3 | Scope + Out-of-scope stated | PASS (watch-list continue; no code; no v1 surface) |
| 4 | User flow described | N/A (no user-visible flow; observation-only) |
| 5 | Data model described | PASS (no data model change; watch-list only) |
| 6 | Dependencies + failure-recovery + DoD | PASS (no implementation; no rollback needed; DoD = filing committed + Linear sub-issue created) |
| 7 | Open questions listed | PASS (watch-list close criteria; AGPL-block retro-application; license-flip contingency) |

**Gate verdict:** PASS — v1 watch-list continue (defer, parking-lot).

## Files to touch

1. **`features/180-satisfecho-pos-v3-renewed-momentum-watch.md`** — already written (this is the only file created by this pick).
2. **`specs/satisfecho-pos-v3-renewed-momentum-watch-HANDOFF.md`** — already written (this file).

**No other files touched.** This is a documentation-only pick.

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md`, this pick is a **watch-list continue** (not a build), so the verification protocol is **just the existence of the two files + the cross-references**:

1. **Confirm `features/180-satisfecho-pos-v3-renewed-momentum-watch.md` exists** in `/opt/data/le31_mmm3_research_work/features/`. Verified by parent: written.
2. **Confirm `specs/satisfecho-pos-v3-renewed-momentum-watch-HANDOFF.md` exists** in `/opt/data/le31_mmm3_research_work/specs/`. Verified by parent: written.
3. **Confirm the Linear sub-issue (HMM-243) is created** with the Feature label and attached to the correct project (recommend `le31 Research` since this is a watch-list continue, not a v1 build — per `le31-feature-pipeline/SKILL.md` v2-bucket picks go to `le31 Research` because `le31 v1 — Core MVP` would falsely imply a v1 build commitment).
4. **Confirm the next-pass follow-up direct-GET** is queued (recommended: 2026-09-18, 3 days from today, to confirm whether the NEW PUSH was a one-off or the start of a renewed maintainer-active cycle).

No pre-merge review required — this is a documentation-only pick, not a code change.

## Rollback path

**No rollback needed.** This is a documentation-only pick; the two files can be deleted without affecting the LE31 stack. If the operator wishes to "un-file" this pick (e.g., because the maintainer simultaneously reverted the NEW PUSH or the license flipped):

1. Delete `features/180-satisfecho-pos-v3-renewed-momentum-watch.md`.
2. Delete `specs/satisfecho-pos-v3-renewed-momentum-watch-HANDOFF.md`.
3. Archive the Linear sub-issue HMM-243.
4. Append a row to `/opt/data/INDEX.md` documenting the close-out.

No git revert needed (the two files are committed once but deleting them is a clean follow-up commit).

## Mandatory LE31 skill list

The coding agent does **NOT** need to load the LE31 skill list for this pick — there is no implementation. The skills relevant to *creating* this pick (already done by the parent cron) are:

1. `le31-daily-research` — the parent applied this skill to identify the pick.
2. `le31-feature-pipeline` — the parent applied this skill to write the feature contract + HANDOFF.
3. `le31-v1-feature-pattern` — the parent applied this skill to enforce the canonical v1 feature contract shape (Goal / Scope / Out of scope / Description / Data model / Implementation / Telegram interaction / Dependencies / Open questions / Why this matters).

For the **next-pass follow-up direct-GET** (3-day rule, recommended 2026-09-18):

1. `le31-daily-research` — the next cron will re-fetch the GitHub watchlist anyway.
2. `raw-api-web-research` — for the GitHub direct-repo GET call pattern.
3. `le31-research-workflow` — for the watch-list continue vs. close decision discipline.

## Notes for the operator

- **The pick is parked, not built.** The Linear sub-issue HMM-243 will sit in `Backlog` with the "watch-list continue" verdict until either (a) the maintainer flips the license to permissive, (b) the maintainer's activity stalls again for 30+ days, or (c) an LE31 owner raises a question that this pick is the reference for.
- **The AGPL-block is the load-bearing constraint.** Do NOT propose a code-derivative of `satisfecho/pos` at any point; the AGPL-3.0 obligation to publish source under the same license applies to any derivative work, and that would force LE31 to publish its entire codebase under AGPL-3.0 (charter §3.2 incompatibility).
- **The 3-day follow-up direct-GET is the right cadence.** If the follow-up confirms the NEW PUSH was the start of a renewed cycle (more pushes within the next 7 days), the watch-list can stay open; if not, file a close-out pick with the "maintainer returned to quiescence" reason.

## Notes for the next-pass follow-up direct-GET

When the next cron fetches `satisfecho/pos` (recommended 2026-09-18 or the next daily-research pass that includes GitHub watchlist GETs), compare against today's baseline:

- `pushed_at` 2026-09-15T06:32:52Z → next value? If still 2026-09-15 (no new push), the NEW PUSH was a one-off; recommend the watch-list stay open but flag as "low-confidence renewed-momentum claim".
- `stargazers_count` 43 → next value? If +2 or more, the inflow is sustained; if flat, the momentum claim weakens.
- `forks_count` 15 → next value? If +2 or more, the fork-velocity signal is sustained; if flat or negative, the momentum claim weakens.
- `updated_at` 2026-09-14T12:06:14Z → next value? If advanced, the maintainer is active; if held, no metadata movement.

The matrix of next-pass data points determines whether the watch-list stays at "active renewed momentum" or rolls back to "sustained-quiescence-after-August-burst" (which is the prior steady state).
