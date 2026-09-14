# HANDOFF — Feature 174: `ilkinism-shiftwright-local-first-staff-rota-rule-explaining`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/174-ilkinism-shiftwright-local-first-staff-rota-rule-explaining.md` — defer/parking-lot (Pick B of Brainstorm 2026-09-14, parent research issue HMM-249).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Charter §3.1 (explicit state transitions) | ✓ | shiftwright *"names the exact rule that rules each person out of an uncovered shift"* is the §3.1 explicit-state-transitions primitive applied to staff-scheduling; every rota decision is reproducible by inspecting the rule that fired |
| 2 | Charter §3.2 (permissive license) | ✓ | MIT |
| 3 | Charter §3.4 (no customer-facing AI) | ✓ | shiftwright is a deterministic rule-verification system; no AI integration in the description or topics |
| 4 | In-window by `pushed_at` | ✓ | pushed 2026-09-10T07:29:08Z (within 30-day window 2026-08-15..2026-09-14) |
| 5 | Ripgrep-verified unique vs features/ 1..172 | ✓ | no existing feature covers the *"names the exact rule that rules each person out of an uncovered shift"* rule-explaining-rota primitive |
| 6 | Cross-section with ≥1 existing feature | ✓ | features 7/12/17/23/51 |
| 7 | Defer verdict (parking-lot, no code change) | ✓ | 0★ + 5-day-old README-only repo (456 bytes, no code yet) + single-maintainer + brand-new → no code adoption; the *vocabulary extension* is the value |

**Gate verdict**: **defer (parking-lot)** — 7/7 gate checks pass, but the build verdict is `defer` because the code is not adoptable (single-maintainer + README-only 456-byte repo + brand-new 5-day-old). The *vocabulary extension* (the named *rule-explaining-rota* primitive) is the brainstorm value, not the code.

## Bucket

**v2** (staff-scheduling-as-explicit-rule-verification) — the *vocabulary* is the value, not the code. LE31 v1 is single-owner single-floor with shift-recap, not multi-staff rota; the shiftwright pattern is the v2-architecture reference for any future v2 surface that asks *"how does LE31 surface a 'why' explanation to the operator when the system rejects an assignment?"*

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that adds multi-cook prep-station routing, or first v2 PR that introduces owner-side prep-task assignment with rule-explanation), the implementation would introduce:
- A `StaffMember` table (`app/models/staff_member.py`): id, name, skills (JSONB array), availability_windows (JSONB), rest_period_hours, weekly_hour_cap.
- A `Shift` table (`app/models/shift.py`): id, date, station, required_skills (JSONB array), start_time, end_time.
- A `Rota` table (`app/models/rota.py`): id, week_start_date, status: draft|verified|published, generated_at, published_at.
- A `RotaAssignment` table (`app/models/rota_assignment.py`): id, rota_id, shift_id, staff_member_id, assigned_at, excluded_reason (the named rule that excluded the staff member).
- A `Rule` table (`app/models/rule.py`): id, name, family: rest|hours|availability|skills, expression (SQL or Python lambda), severity: hard|soft.
- A `app/rules/` package with the 4 rule families (rest, hours, availability, skills) as named-rule functions.

This is **NOT a v1 surface** — LE31 v1 is single-owner single-floor with shift-recap, not multi-staff rota. The HANDOFF is to evaluate whether the v2 multi-cook surface is the right product-wedge for the next v2 PR.

## Verification protocol

1. `git clone https://github.com/ilkinism/shiftwright` (NOT to be done today — defer; repo is 456 bytes README-only with no code yet).
2. `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN" "https://api.github.com/repos/ilkinism/shiftwright"` for star count, fork count, license, language, pushed_at, created_at, topics (parent-verified 2026-09-14).
3. `git diff --stat` (post-trigger-fires, NOT today) to verify the multi-cook surface changes are isolated to `app/models/staff_member.py`, `app/models/shift.py`, `app/models/rota.py`, `app/models/rota_assignment.py`, `app/models/rule.py`, `app/rules/`.
4. `pytest app/rules/ -v` (post-trigger-fires, NOT today) to verify the 4 rule families (rest, hours, availability, skills) pass the named-rule test suite.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v2 trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop the 5 tables (`StaffMember`, `Shift`, `Rota`, `RotaAssignment`, `Rule`); the `app/rules/` package is additive, not destructive.

## Mandatory LE31 skill list

When (and only when) the future v2 trigger fires, the coding agent MUST load these skills before starting:

- `development` (router for all coding work)
- `le31-v1-feature-pattern` (existing LE31 v1 feature implementation pattern — applies as the LE31 v2 surface extends the v1 schema)
- `le31-handoff-spec` (HANDOFF contract reader/writer)
- `le31-coding-agent-brief` (paste-in prompt from slice contract)
- `speckit-implement` (verify tasks in order)

## Bucket project

**`le31 Research`** (parent research issue HMM-249) — the sub-issue for this feature lives in `le31 Research` (where the parent research issue lives), NOT in `le31 v1 — Core MVP`. Reason: the project `le31 v2 owner-pains` (which the original SKILL.md expected) **does not exist** in this workspace; the verified workspace contains only `le31 v1 — Core MVP`, `le31 Workflow`, and `le31 Research`. Per the verified-2026-08-28 skill note: *"For a v2-bucket pick, attach the sub-issue to `le31 Research` (where the parent research issue lives) and say so in the report."*

## Why this is a `defer`

The shiftwright repo is 0★, 5-day-old, README-only (456 bytes, no code yet). The single-maintainer cadence + the brand-new 5-day-old README-only state make code adoption impractical. The *value* is the vocabulary extension — the phrase *"names the exact rule that rules each person out of an uncovered shift"* is the §3.1 explicit-state-transitions primitive applied to staff-scheduling, and the `local-first + no-dependencies + compliance + working-time + availability + skills` topic set is the LE31 phone-first operator posture applied to multi-cook prep-station routing. No build time today; the value is the persistent cross-section reference + the named *rule-explaining-rota* primitive for any future v2 PR that adds multi-cook prep-station routing or owner-side prep-task assignment with rule-explanation.
