# rafood-api-fastapi-sqlmodel-context-arch — HANDOFF

> **Slice for the research agent.** This is a passive parking-lot
> observation of the in-window `RafaelEmery/rafood-api` cross-section
> peer, not a feature build. The slice boundary is hard: zero
> source-file edits, zero schema changes, zero new config keys. Read
> this *and* `features/106-rafood-api-fastapi-sqlmodel-context-arch.md`
> before touching any code. Do not paste chat excerpts back into the
> build.

## Frozen identifiers (do not rename)

- Feature ID: `106`
- Slug: `rafood-api-fastapi-sqlmodel-context-arch`
- Contract file: `features/106-rafood-api-fastapi-sqlmodel-context-arch.md`
- Bucket: **v2 owner-pains (parking-lot, future-context-decomposition)**
  — hard defer pending charter §3 surface-expansion review
- Linear parent: **HMM-139** (Brainstorm 2026-08-24 — daily, created in this cron)
- Linear sub-issue: **HMM-140** (create as a draft parking-lot artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct repo GET on
`RafaelEmery/rafood-api`; ★3; Python; FastAPI + SQLModel + Alembic +
Postgres + K8s + 5-context DDD separation documented in README;
pushed 2026-08-23T22:28:04Z).

**Confidence:** **high** for the pattern (the 5-context DDD separation
is documented in the README explicitly); **low** for the LE31-specific
build implication (charter §3 single-tenant posture is correct for v1;
multi-context decomposition is a charter-level question deferred to
v2).

**Decision: parking-lot; hard defer pending charter §3 review.** The
README read is the next research-side action. The "should LE31 v2
decompose into multiple bounded contexts?" question is parked pending
charter approval.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job on 2026-08-24).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/106-rafood-api-fastapi-sqlmodel-context-arch.md   # NEW (this artifact)
specs/rafood-api-fastapi-sqlmodel-context-arch-HANDOFF.md # NEW (this file)
INDEX.md                                                    # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

- **Today**: verify that this `HANDOFF.md` exists + the
  `features/106-…md` contract file exists + the `INDEX.md` row was
  added + the `le31_daily_brainstorm_2026_08_24` Linear issue
  (HMM-139) was created with the parent body + the
  `le31_v1_core_mvp` Linear sub-issue (HMM-140) was created with the
  contract body and `Feature` label.
- **Daily (next 7 days)**: track `RafaelEmery/rafood-api` star
  velocity via `GET https://api.github.com/repos/RafaelEmery/rafood-api`
  (via `$HERMES_GITHUB_TOKEN`).
- **Daily (next 7 days)**: read the `RafaelEmery/rafood-api` README +
  ADRs + ER model and confirm the 5-context separation pattern
  (READ ONLY — no import).
- **Re-check threshold**: if stars ≥25 OR ≥2 independent
  FastAPI+SQLModel peers converge on the same 5→7 context count, the
  slice is un-deferred and becomes a v2 charter-question prompt.

## Linear sub-issue

- **Parent**: HMM-139 (Brainstorm 2026-08-24 — daily, project `le31
  Research`, status Done).
- **Sub-issue**: HMM-140 (Feature, project `le31 v1 — Core MVP`,
  status Backlog). Body has the full contract body; label `Feature`.

## Rollback path

**Fully reversible.** Delete
`features/106-rafood-api-fastapi-sqlmodel-context-arch.md` + this
`HANDOFF.md` + the `INDEX.md` row + the `le31_daily_brainstorm_2026_08_24`
parent issue + the `le31_v1_core_mvp` sub-issue (HMM-140). Zero risk
of code regression (no code changed).

## Why this matters (for the research agent)

The 2026-08-24 brainstorm pass surfaces `RafaelEmery/rafood-api` as
the only in-window FastAPI + SQLModel + Alembic + Postgres + K8s
peer that documents a 5-context DDD separation. The cross-section
insight informs LE31 v2 multi-context decomposition if/when it
becomes necessary (e.g., splitting `StockEntry` writes from menu
reads from owner-recap reads). The pattern is informational; LE31 v1
single-tenant posture (charter §3) is correct without it. The
artifact records the 5-context pattern for future v2-AI iteration.

## Carry-over history

- **2026-08-24**: created from brainstorm 2026-08-24 Pick A.
- **Next pass (2026-08-25)**: down-stream daily-research pass should
  read `RafaelEmery/rafood-api` README + ADRs + ER model and confirm
  the 5-context separation. Add `RafaelEmery/rafood-api` to the
  daily-research watch list (5-repo watch) to track star velocity +
  push activity.

If the destination repo's research-side Hermes instance finds the
README read changes the gate verdict (e.g., the 5-context separation
turns out to be documentation-only with no module boundaries), the
slice should be amended rather than re-created.
