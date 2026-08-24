# smb-erp-pos-schema-separation-lsfusion — HANDOFF

> **Slice for the research agent.** This is a passive parking-lot
> observation of the in-window `lsfusion-solutions/mycompany`
> cross-section peer, not a feature build. The slice boundary is
> hard: zero source-file edits, zero schema changes, zero new config
> keys. Read this *and*
> `features/107-smb-erp-pos-schema-separation-lsfusion.md` before
> touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `107`
- Slug: `smb-erp-pos-schema-separation-lsfusion`
- Contract file: `features/107-smb-erp-pos-schema-separation-lsfusion.md`
- Bucket: **v2 owner-pains (parking-lot, future-schema-patterns)**
  — hard defer pending charter §3 single-tenant-posture review
- Linear parent: **HMM-139** (Brainstorm 2026-08-24 — daily, created in this cron)
- Linear sub-issue: **HMM-141** (create as a draft parking-lot artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct repo GET on
`lsfusion-solutions/mycompany`; ★317 mid-adoption; Apache-2.0
permissive license; JavaScript + lsFusion; 7-module ERP+POS surface
[inventory + invoicing + manufacturing + sales + projects + HR + POS];
pushed 2026-08-19T07:54:24Z).

**Confidence:** **high** for the pattern (a mature 7-module
single-tenant SMB ERP+POS at 317★ community traction validates that
single-tenant schema separation scales); **low** for the LE31-specific
build implication (charter §3 single-tenant posture is correct for v1
without modification; schema-patterns questions are a future-tense
concern).

**Decision: parking-lot; hard defer pending charter §3 review.** The
README read is the next research-side action. The "should LE31 v2
add per-business-context schema separation?" question is parked
pending charter approval.

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
features/107-smb-erp-pos-schema-separation-lsfusion.md   # NEW (this artifact)
specs/smb-erp-pos-schema-separation-lsfusion-HANDOFF.md # NEW (this file)
INDEX.md                                                    # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

- **Today**: verify that this `HANDOFF.md` exists + the
  `features/107-…md` contract file exists + the `INDEX.md` row was
  added + the `le31_daily_brainstorm_2026_08_24` Linear issue
  (HMM-139) was created with the parent body + the
  `le31_v1_core_mvp` Linear sub-issue (HMM-141) was created with the
  contract body and `Feature` label.
- **Daily (next 7 days)**: track `lsfusion-solutions/mycompany`
  star velocity via `GET
  https://api.github.com/repos/lsfusion-solutions/mycompany` (via
  `$HERMES_GITHUB_TOKEN`).
- **Daily (next 7 days)**: read the
  `lsfusion-solutions/mycompany` README + module documentation and
  confirm the 7-module schema-separation pattern (READ ONLY — no
  import).
- **Re-check threshold**: if stars ≥400 OR ≥2 independent
  permissive-license SMB ERP+POS peers converge on the same 7+
  module count, the slice is un-deferred and becomes a v2
  charter-question prompt.

## Linear sub-issue

- **Parent**: HMM-139 (Brainstorm 2026-08-24 — daily, project `le31
  Research`, status Done).
- **Sub-issue**: HMM-141 (Feature, project `le31 v1 — Core MVP`,
  status Backlog). Body has the full contract body; label `Feature`.

## Rollback path

**Fully reversible.** Delete
`features/107-smb-erp-pos-schema-separation-lsfusion.md` + this
`HANDOFF.md` + the `INDEX.md` row + the
`le31_daily_brainstorm_2026_08_24` parent issue + the
`le31_v1_core_mvp` sub-issue (HMM-141). Zero risk of code regression
(no code changed).

## Why this matters (for the research agent)

The 2026-08-24 brainstorm pass surfaces `lsfusion-solutions/mycompany`
as the only in-window ≥300★ permissive-license (Apache-2.0) mature SMB
ERP+POS reference documenting a 7-module schema-separation pattern.
The cross-section insight: **single-tenant SMB ERP+POS architecture
with per-business-context schema separation is the dominant open-source
SMB pattern at the 7-module level, and Apache-2.0 permissive licensing
makes the patterns study-able without contagion**. The artifact
validates LE31 charter §3 single-tenant posture without changing it
and records the 7-module pattern as a future reference for LE31 v2
if/when schema-patterns questions arise.

## Carry-over history

- **2026-08-24**: created from brainstorm 2026-08-24 Pick B.
- **Next pass (2026-08-25)**: down-stream daily-research pass should
  read `lsfusion-solutions/mycompany` README + module documentation
  and confirm the 7-module schema-separation pattern. Add
  `lsfusion-solutions/mycompany` to the daily-research watch list
  (5-repo watch) to track star velocity + push activity.

If the destination repo's research-side Hermes instance finds the
README read changes the gate verdict (e.g., the 7-module separation
turns out to be one lsFusion module per business area with no
explicit schema separation), the slice should be amended rather than
re-created.
