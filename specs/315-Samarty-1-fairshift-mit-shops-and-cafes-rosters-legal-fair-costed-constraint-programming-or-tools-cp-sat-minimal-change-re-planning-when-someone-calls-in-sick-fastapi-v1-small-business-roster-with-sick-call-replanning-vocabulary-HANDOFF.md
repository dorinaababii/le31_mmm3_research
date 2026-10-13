# HANDOFF — 315-Samarty-1-fairshift-mit-shops-and-cafes-rosters-legal-fair-costed-constraint-programming

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-10-13
**Active feature path**: `/opt/data/le31_mmm3_research/features/315-Samarty-1-fairshift-mit-shops-and-cafes-rosters-legal-fair-costed-constraint-programming-or-tools-cp-sat-minimal-change-re-planning-when-someone-calls-in-sick-fastapi-v1-small-business-roster-with-sick-call-replanning-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v1 does not have a *chef-shift-staffing* surface today; the owner manually schedules cook shifts; the peer value is *constraint-programming-with-sick-call-replanning vocabulary for a future v1 PR that surfaces chef-shift-staffing + minimal-change-re-planning primitives*, not *adoption*.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the `Samarty-1/fairshift` GitHub repo (MIT, **0★ / 0⑂**, **31 KB tiny**, language Python ✓ ON-STACK, **pushed 2026-10-10T13:06:54Z AND created 2026-10-10T13:06:49Z = IN-WINDOW BY BOTH FIELDS**, by `Samarty-1` = same author as feature 314 `Samarty-1/payout-recon` = sister-pushed same-day-same-hour) as a dated, in-window **structural-evidence peer** for LE31's v1 small-business-roster-with-sick-call-replanning substrate.

If the trigger condition (LE31 first proposes a v1 surface that wants *chef-shift-staffing* or *chef-availability* or *chef-time-off-requests* primitives, OR the operator reports manual-shift-rostering-pain that costs minutes-to-hours every day, OR a future owner decision questions whether LE31 needs a *constraint-programming-with-sick-call-replanning* surface at all) is met, the external coding agent should:

1. Load this artifact and the parent daily-brainstorm report (`/opt/data/le31-brainstorm-2026-10-13.md`).
2. Load the `fairshift` repo: `https://github.com/Samarty-1/fairshift` — README + `fairshift/` source if available.
3. Load the companion feature 314 (`Samarty-1/payout-recon`) — same author + same day; the operator-pain-mapping discipline is universal across small-business-operations.
4. Add OR-Tools to a side-branch `requirements-ortools.txt` (LE31 v1 today has no OR-Tools dependency) — verify Python 3.13 compatibility before adding.
5. Re-run the LE31 feature gate with `fairshift`'s README in hand.
6. **Decide whether the proposed v1 surface benefits from `fairshift`'s constraint-programming-with-OR-Tools-CP-SAT framing**. If the v1 surface wants *chef-shift-staffing + sick-call-replanning*, `fairshift` is purpose-built for that use case. If the v1 surface only wants a manual-shift-practices interface, `fairshift` adds no value.
7. **If `fairshift` is proposed for adoption**: pin to a specific version, add to `requirements-fairshift.txt` (do not pin to v1 yet), and build a single-week prototype with LE31 chef-availability data. Compare against the owner-manual-shift-practices. If the constraint-programming-based roster improves on the manual practice with reasonable constraint solving time (target <1 second per LE31's "under a second" goal), propose a v1 surface; if not, document the comparison and defer.
8. **If `fairshift` is not adopted**: document the comparison and defer. No charter §3.1 change is needed because `fairshift` is a shift-rostering library, not a stack change (OR-Tools is an optional dependency, not a Postgres replacement).
9. **Pilot on one week first**. Do not adopt `fairshift` project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/315-Samarty-1-fairshift-mit-shops-and-cafes-rosters-legal-fair-costed-constraint-programming-or-tools-cp-sat-minimal-change-re-planning-when-someone-calls-in-sick-fastapi-v1-small-business-roster-with-sick-call-replanning-vocabulary.md`
- **Parent daily-brainstorm report**: `/opt/data/le31-brainstorm-2026-10-13.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-13/gh_creative_topic_small_business_fastapi.json` (where `Samarty-1/fairshift` is listed; parent-verified raw JSON has `stargazers_count=0`, `forks_count=0`, `license.spdx_id=MIT`, `pushed_at=2026-10-10T13:06:54Z`, `created_at=2026-10-10T13:06:49Z`, `description="Rosters for shops and cafés: legal, fair and costed in under a second, with minimal-change re-planning when someone calls in sick (OR-Tools CP-SAT, FastAPI)"`, `size=31`, `topics=[constraint-programming, fastapi, or-tools, rostering, scheduling, small-business]`)
- **`fairshift` repo**: `https://github.com/Samarty-1/fairshift` (parent-fetched 2026-10-13 metadata)
- **Companion artifacts**:
  - `features/314-Samarty-1-payout-recon-...md` (same-author same-day sister-shape for 4-way-payment-reconciliation)
  - `features/03-kitchen-stock-tracker-...md` (the existing v1 kitchen-stock-tracker surface — different concern, but both involve operator-driven solver-style planning)
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.5 (offline-first + operator-can-keep-working)**: `fairshift`'s *minimal-change-re-planning-when-someone-calls-in-sick* IS the canonical §3.5 *operator-can-keep-working-during-staff-shortage* invariant applied to the *shift-rescheduling* dimension.

## Mandatory LE31 skill list

The external coding agent must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.5 offline-first + operator-can-keep-working).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Verification protocol reference

- **Read-back protocol**: parent-re-parse the raw `/tmp/le31-brainstorm-2026-10-13/gh_creative_topic_small_business_fastapi.json` JSON to confirm `full_name=Samarty-1/fairshift` + `stargazers_count=0` + `forks_count=0` + `license.spdx_id=MIT` + `pushed_at=2026-10-10T13:06:54Z` + `created_at=2026-10-10T13:06:49Z` + `description` = `"Rosters for shops and cafés: legal, fair and costed in under a second, with minimal-change re-planning when someone calls in sick (OR-Tools CP-SAT, FastAPI)"` + `size=31` + `topics=[constraint-programming, fastapi, or-tools, rostering, scheduling, small-business]`.
- **GitHub canonical read**: GET `https://api.github.com/repos/Samarty-1/fairshift` (HTTP 200; parent-verified 2026-10-13).
- **Anti-fabrication canary**: `grep -lF 'Samarty-1/fairshift'` across `/opt/data/le31_mmm3_research/features/*.md` = 0 matches outside this feature file (parent-verified).
- **Distinct-from-features**: ripgrep-verified `fairshift` against features 1–313 = only this feature 315 (plus the same-author-pair reference in feature 314).

## Rollback path

This defer artifact is fully reversible:
- **Delete the feature file**: `rm /opt/data/le31_mmm3_research/features/315-Samarty-1-fairshift-...md`.
- **Delete the HANDOFF**: `rm /opt/data/le31_mmm3_research/specs/315-Samarty-1-fairshift-...-HANDOFF.md`.
- **No code change was made today**, so no rollback of code is required.
- **No database migration was made today**, so no rollback of schema is required.
- **No pin change was made today** (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1).
