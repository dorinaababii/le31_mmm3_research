# Feature 174 — `ilkinism-shiftwright-local-first-staff-rota-rule-explaining` (defer)

> **NEW observation (2026-09-14).** Documents in-window GitHub repo `ilkinism/shiftwright` (**MIT**, **0★/0⑂**, Python, **pushed 2026-09-10T07:29:08Z**, in-window by `pushed_at` only, 456 bytes — README-only, no code yet, **created 2026-09-10T07:29:03Z** — 5-second-old repo at creation, brand-new single-maintainer repo). Description (verbatim from GitHub API, parent-verified direct-GET 2026-09-14): *"A week you can publish, checked before you send it. A local staff rota builder that verifies rest, hours, availability and skills — and names the exact rule that rules each person out of an uncovered shift."* Topics (verbatim from raw JSON, parent-verified): `compliance, local-first, no-dependencies, python, rota, scheduling, small-business, staff, working-time`. Bucket: **v2 (staff-scheduling-as-explicit-rule-verification; v2 surface, not v1 — LE31 v1 is single-owner single-floor with shift-recap, not multi-staff rota)** — pick B of Brainstorm 2026-09-14 (parent research issue HMM-249). Build verdict: `defer` (parking-lot). Zero build time today. The 5-second-old README-only repo is the demand-signal, not the code.

## Goal

Retain the **`"names the exact rule that rules each person out of an uncovered shift"`** primitive as a persistent cross-section reference for the LE31 v2 *staff-scheduling-as-explicit-rule-verification* surface, and document the **vocabulary extension** that an independent maintainer arrived at in 2026 — every rota decision is reproducible by inspecting the rule that fired, not by re-running an opaque ML model. The artifact is the persistent cross-section reference + the named *rule-explaining-rota* primitive. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **`"names the exact rule that rules each person out"`** primitive: every rota decision surfaces the specific rule that excluded or qualified the staff member. This is the **§3.1 explicit-state-transitions primitive applied to staff-scheduling**: every decision is reproducible by inspecting the rule that fired, not by re-running an opaque ML model. The operator-facing surface is *"why is cook X not assigned to this shift?" → answer: "rule Y fired because Z."*
- A written record of the **`compliance + working-time`** topic tag set: the rota is verified against working-time regulations (rest-period minimums, weekly-hour caps, availability windows) before the operator publishes it. This is the **operator-trust anchor**: the operator doesn't have to verify by hand that the rota is compliant — the system surfaces every rule that was checked.
- A written record of the **`local-first + no-dependencies + small-business`** topic tag set: the rota is computed on the local machine, with no cloud sync, no SaaS dependency. This is the **LE31 phone-first operator posture** applied to staff-scheduling — the operator owns the rota data, and the rota computation runs on the operator's hardware.
- A written record of the **`availability + skills`** rule set: the rota is verified against staff availability AND against the specific skills required for the shift (e.g., "this shift requires grill experience; cook X has grill experience; cook Y does not"). This is the **explicit-skill-rule primitive** — every rule is named, every rule is auditable.
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (5-second-old README-only repo); (2) LE31 v1 has no multi-staff rota surface (v1 is single-owner single-floor with shift-recap); (3) the *rule-explaining-rota* primitive is the brainstorm value, not the code.

**Out of scope (defer artifact):**
- Any change to LE31 v1's waiter web UI or cook Telegram bot (charter §3.1: explicit state transitions; v1 surfaces are sufficient for v1 ops).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Any change to LE31 v1's owner-side surfaces (owner-daily-recap-telegram, owner-recap-persona-voice, owner-no-account-live-floor-link).
- Adoption of the shiftwright codebase (single maintainer, README-only repo with no code yet).
- Cross-pollination with charter §3.4 (shiftwright is a deterministic rule-verification system; no AI integration in the description or topics).

## Evidence / JTBD

When a future LE31 v2 surface proposes "the multi-staff scheduling surface" (e.g., a v2 surface that introduces prep-station routing across multiple cooks, or a v2 surface that introduces owner-side prep-task assignment), the owner wants *a primitive that proves the demand for an explicit-rule-verification staff-scheduling surface exists in 2026*, but struggles because *LE31 has no documented evidence that "names the exact rule that rules each person out of an uncovered shift" is a real demand signal*, so that *the v2 surface can be defended with "this is what an independent maintainer shipped in 2026 with the rule-explaining-rota primitive."*

- **Evidence class**: observed (the shiftwright description + topics name the primitive explicitly: `compliance, local-first, no-dependencies, python, rota, scheduling, small-business, staff, working-time`).
- **Confidence**: medium for the demand signal (the description is direct; the topic tags are LE31-aligned; the 5-second-old README-only repo is the *demand signal*, not the *adoption signal*); low for transferability (LE31's stack is FastAPI+SSE+Postgres+aiogram, shiftwright is local-first-Python; LE31 v1 has no multi-staff rota surface at all).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-owner single-floor with shift-recap; no multi-staff scheduling); the value is the *vocabulary extension* — when the first v2 PR that adds any "the system suggested X, the cook did Y, the owner wants to see why" surface lands, the shiftwright *named-rule-explanation* primitive is the operator-trust anchor.
- **The value is vocabulary, not direct demand**: when the first v2 PR that adds prep-station routing across multiple cooks (if/when the owner approves the v2 multi-cook surface) lands, the shiftwright pattern is a ready-made *named primitive* and the `compliance + working-time + local-first + no-dependencies + availability + skills` vocabulary slots into features 7 (`demand-estimation`) + 12 (`pre-shift-briefing`) + 17 (`demand-forecasting-ml`) + 23 (`sse-cook-channel`) + 51 (`realtime-cook-cook-watch`).

## Description

GitHub `ilkinism/shiftwright` (MIT, 0★/0⑂, Python, pushed 2026-09-10T07:29:08Z, created 2026-09-10T07:29:03Z, 456 bytes README-only). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-14): *"A week you can publish, checked before you send it. A local staff rota builder that verifies rest, hours, availability and skills — and names the exact rule that rules each person out of an uncovered shift."*

The architectural primitive has one core principle and four sub-primitives that map 1:1 onto the LE31 v2 *staff-scheduling-as-explicit-rule-verification* surface:

1. **"A week you can publish, checked before you send it"** — the rota is verified *before* the operator commits it. This is the §3.1 explicit-state-transitions primitive applied to staff-scheduling: every decision is checked against named rules, and the check happens at commit-time, not at runtime. Sister-shape to feature 12 (`pre-shift-briefing`) + feature 51 (`realtime-cook-coach-watch`).
2. **"Verifies rest, hours, availability and skills"** — the four named rule families are: (a) `rest` = minimum rest period between shifts (e.g., 11 hours); (b) `hours` = weekly/monthly hour caps (e.g., 48 hours/week); (c) `availability` = the staff member's declared availability windows; (d) `skills` = the specific skills required for the shift (e.g., grill, pastry, station-routing). Each rule family is explicit, named, and auditable. Sister-shape to feature 7 (`demand-estimation`) + feature 17 (`demand-forecasting-ml`).
3. **"Names the exact rule that rules each person out of an uncovered shift"** — the operator-facing surface is the *rule-explainer*: when a staff member is not assigned to an uncovered shift, the system names the specific rule that fired (e.g., "cook X is ruled out of shift S by rule R: 'cook X worked shift T 8 hours before shift S, violating the 11-hour rest-period rule'"). This is the **operator-trust anchor**: the operator doesn't have to verify by hand — the system surfaces every rule that was checked. Sister-shape to feature 68 (`cook-assistant-deterministic-gate`) + feature 123 (`deterministic-operator-output-golden-test`) + feature 130 (`dhh-kitchen-accessible-operator-ux-visual-replayable`).
4. **"Local-first + no-dependencies"** — the rota is computed on the local machine, with no cloud sync, no SaaS dependency, no third-party API. This is the **LE31 phone-first operator posture** applied to staff-scheduling: the operator owns the rota data, and the rota computation runs on the operator's hardware. Sister-shape to feature 67 (`solo-operator-shift-journal-pwa`) + feature 32 (`solo-operator-floor-pin`).

**The 1:1 mapping onto LE31 v2 surface:**

| shiftwright primitive | LE31 v2 equivalent | Charter section | Status |
|---|---|---|---|
| Local-first + no-dependencies | Phone-first operator web UI + local SSE channel | §3.1, §3.2 ✓ | **Implemented (v1)** |
| Verifies rest, hours, availability, skills | (LE31 v1 has no multi-staff rota) | v2 | **Not implemented** — v2 surface |
| Names the exact rule that ruled each person out | (LE31 v1 has no rule-explainer) | v2 | **Not implemented** — v2 surface |
| A week you can publish, checked before you send it | (LE31 v1 has no pre-publish verification) | v2 | **Not implemented** — v2 surface |
| Compliance + working-time verification | (LE31 v1 has no compliance layer) | v2 | **Not implemented** — v2 surface |
| Small-business | Single-restaurant | §3.1 ✓ | **Implemented (v1)** |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that adds multi-cook prep-station routing), the implementation would introduce:
- A `StaffMember` table (id, name, skills, availability_windows, rest_period_hours, weekly_hour_cap).
- A `Shift` table (id, date, station, required_skills, start_time, end_time).
- A `Rota` table (id, week_start_date, status: draft|verified|published, generated_at, published_at).
- A `RotaAssignment` table (id, rota_id, shift_id, staff_member_id, assigned_at, excluded_reason — the named rule that excluded the staff member).
- A `Rule` table (id, name, family: rest|hours|availability|skills, expression: SQL or Python lambda, severity: hard|soft).

This is **NOT a v1 surface** — LE31 v1 is single-owner single-floor with shift-recap, not multi-staff rota. The HANDOFF is to evaluate whether the v2 multi-cook surface is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v2 trigger fires:
1. Add the 5 tables (`StaffMember`, `Shift`, `Rota`, `RotaAssignment`, `Rule`) via Alembic migrations.
2. Implement the 4 rule families (rest, hours, availability, skills) as named-rule functions in `app/rules/`.
3. Wire the rule-explainer surface to the operator UI: when a staff member is not assigned to a shift, the system surfaces the specific rule that fired.
4. New feature file at `features/NNN-multi-cook-prep-station-routing-with-rule-explainer.md` (NOT this defer artifact).

## Telegram interaction if any

None today. The defer artifact is documentation only.

If the future v2 multi-cook surface is approved, the cook-side Telegram bot could surface the rule-explanation: when cook X sees "you are not assigned to shift S", the Telegram bot could reply with "rule R: 'you worked shift T 8 hours before shift S, violating the 11-hour rest-period rule'." Sister-shape to feature 51 (`realtime-cook-coach-watch`) + feature 68 (`cook-assistant-deterministic-gate`).

## Dependencies

- None today (defer artifact is documentation only).
- If the v2 multi-cook surface is approved: Alembic migration framework (already in LE31 stack); the existing `audit_logs` table can record every rule-evaluation (every RotaAssignment row is an append-only entry).

## Open questions

- Does the owner approve a v2 multi-cook prep-station routing surface? (Currently no — v1 is single-owner single-floor with shift-recap; multi-cook is a v2 surface.)
- Does the owner approve a v2 rule-explanation Telegram delivery for cook-side rejections? (Currently no — v1 Telegram delivery is for the cook-channel + owner-recap, not for rule-explanations.)
- Is the v2 rule-explanation surface owner-side (owner sees the rule-explanation in their dashboard) or cook-side (cook sees the rule-explanation in their Telegram bot)? (Currently unspecified — the v2 surface design is open.)

## Why this matters

The shiftwright repo is the **vocabulary-extension reference** for the v2 question *"how does LE31 surface a 'why' explanation to the operator when the system rejects an assignment?"* The phrase *"names the exact rule that rules each person out of an uncovered shift"* is the §3.1 explicit-state-transitions primitive applied to staff-scheduling: every decision is reproducible by inspecting the rule that fired, not by re-running an opaque ML model. This is the **operator-trust anchor** for any future v2 surface that asks the operator to trust a system-generated decision — the operator can always inspect the rule. The `local-first + no-dependencies` topic set is the LE31 phone-first operator posture applied to staff-scheduling; the operator owns the rota data. No code today; the value is the vocabulary extension + the named *rule-explaining-rota* primitive for the future v2 multi-cook surface.
