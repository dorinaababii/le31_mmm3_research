# qsr-edge-vision-order-accuracy-intel-openvino-apache — HANDOFF

> **Slice for the research agent.** This is a passive parking-lot
> observation of the in-window `intel-retail/order-accuracy`
> cross-section peer, not a feature build. The slice boundary is
> hard: zero source-file edits, zero schema changes, zero new config
> keys. Read this *and*
> `features/114-qsr-edge-vision-order-accuracy-intel-openvino-apache.md`
> before touching any code. Do not paste chat excerpts back into the
> build.

## Frozen identifiers (do not rename)

- Feature ID: `114`
- Slug: `qsr-edge-vision-order-accuracy-intel-openvino-apache`
- Contract file: `features/114-qsr-edge-vision-order-accuracy-intel-openvino-apache.md`
- Bucket: **v2 owner-pains (parking-lot, future-vision-surface-reference)**
  — hard defer pending charter §3 computer-vision surface review
- Linear parent: **HMM-147** (Brainstorm 2026-08-25 — daily, created in this cron)
- Linear sub-issue: **HMM-150** (create as a draft parking-lot artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct repo GET on
`intel-retail/order-accuracy`; ★2 / 15 forks; 1:7.5 star-to-fork
ratio signals real consumption; Apache-2.0 permissive license;
Python; Intel-authored QSR reference implementation for edge object
detection + order accuracy; GStreamer + OpenVINO + Intel hardware;
pushed **2026-08-25T05:00:26Z (today)**).

**Confidence:** **high** for the cross-section pattern (the
GStreamer + OpenVINO + edge deployment architecture is documented in
the repo description; Intel as authoring org is the vendor-grade
quality signal); **low** for the LE31-specific build implication
(LE31 v1 doesn't ship a computer-vision surface; no owner signal of
"I want plate-accuracy / kitchen-display visual verification" today;
the v2 extension is a future-tense concern; charter §3.5
AI non-customer-facing rule applies — vision must be gated on
deterministic stock-state transitions, not free-form LLM calls).

**Decision: parking-lot; hard defer pending owner-pain signal or
charter §3 computer-vision surface review.** The README read is the
next research-side action. The "should LE31 v2 add a computer-vision
surface (plate-accuracy, kitchen-display visual verification,
stock-shelf visual verification)?" question is parked pending
charter approval.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job on 2026-08-25).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/114-qsr-edge-vision-order-accuracy-intel-openvino-apache.md   # NEW (this artifact)
specs/qsr-edge-vision-order-accuracy-intel-openvino-apache-HANDOFF.md  # NEW (this file)
INDEX.md                                                              # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

- **Today**: verify that this `HANDOFF.md` exists + the
  `features/114-…md` contract file exists + the `INDEX.md` row was
  added + the `le31_daily_brainstorm_2026_08_25` Linear issue
  (HMM-147) was created with the parent body + the
  `le31_v1_core_mvp` Linear sub-issue (HMM-150) was created with the
  contract body and `Feature` label.
- **Daily (next 7 days)**: track `intel-retail/order-accuracy` star
  velocity via `GET
  https://api.github.com/repos/intel-retail/order-accuracy`
  (via `$HERMES_GITHUB_TOKEN`).
- **Daily (next 7 days)**: read the `intel-retail/order-accuracy`
  README + architecture documentation and confirm the GStreamer +
  OpenVINO + edge deployment pattern (READ ONLY — no import,
  Apache-2.0 means code-borrow is permitted but no borrow is needed
  today).
- **Re-check threshold**: if stars ≥100 OR ≥3 independent
  QSR edge-vision reference implementations, OR the LE31 owner
  signals an explicit "I want plate-accuracy / kitchen-display
  visual verification" pain, the slice is un-deferred and becomes a
  v2 charter-question prompt.

## Linear sub-issue

- **Parent**: HMM-147 (Brainstorm 2026-08-25 — daily, project `le31
  Research`, status Done).
- **Sub-issue**: HMM-150 (Feature, project `le31 v1 — Core MVP`,
  status Backlog). Body has the full contract body; label `Feature`.

## Rollback path

**Fully reversible.** Delete
`features/114-qsr-edge-vision-order-accuracy-intel-openvino-apache.md`
+ this `HANDOFF.md` + the `INDEX.md` row + the
`le31_daily_brainstorm_2026_08_25` parent issue + the
`le31_v1_core_mvp` sub-issue (HMM-150). Zero risk of code regression
(no code changed).

## Why this matters (for the research agent)

The 2026-08-25 brainstorm pass surfaces
`intel-retail/order-accuracy` as the **freshest in-window push
(today)** and the **only in-window Intel-authored QSR reference
implementation** for edge object detection + order accuracy. The
cross-section insight informs LE31 v2 owner-pains computer-vision
surface (plate-accuracy, kitchen-display visual verification,
stock-shelf visual verification) gated on deterministic
stock-state transitions, not free-form LLM calls — preserving
charter §3.1 + §3.5. Apache-2.0 permissive license means any spec
or pattern is reusable without license concerns for future v2
owner-pains extension. The artifact records the QSR edge-vision
architecture for future v2 iteration.

## Carry-over history

- **2026-08-25**: created from brainstorm 2026-08-25 Pick C.
- **Next pass (2026-08-26)**: down-stream daily-research pass should
  read `intel-retail/order-accuracy` README + architecture
  documentation and confirm the GStreamer + OpenVINO + edge
  deployment pattern. Add `intel-retail/order-accuracy` to the
  daily-research watch list (5-repo watch) to track star velocity +
  push activity + Intel-credibility signals.

If the destination repo's research-side Hermes instance finds the
README read changes the gate verdict (e.g., the GStreamer + OpenVINO
pipeline requires Intel-specific hardware that's incompatible with
LE31 v1 deployment context), the slice should be amended rather
than re-created.