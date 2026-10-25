# Anatolii198-mesa-lite-mit-javascript-vanilla-js-no-dependencies-no-build-step-restaurant-analytics-dashboard-eight-svg-charts-v1-zero-dependency-analytics-surface-vocabulary — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/377-Anatolii198-mesa-lite-mit-javascript-vanilla-js-no-dependencies-no-build-step-restaurant-analytics-dashboard-eight-svg-charts-v1-zero-dependency-analytics-surface-vocabulary.md`
> before touching anything. **This is a WATCH-LIST / FRONTEND-CRITERIA
> slice, NOT a build slice.** There is no UI deliverable.
>
> **This slice does NOT authorise a client-side framework, a charting
> library, or an owner-facing dashboard.** It proposes **one acceptance
> criterion** about how any *future* owner- or waiter-facing view must
> render.

## Frozen identifiers (do not rename)

- Feature ID: `377`
- Slug: `Anatolii198-mesa-lite-mit-javascript-vanilla-js-no-dependencies-no-build-step-restaurant-analytics-dashboard-eight-svg-charts-v1-zero-dependency-analytics-surface-vocabulary`
- Contract file: `features/377-Anatolii198-mesa-lite-mit-javascript-vanilla-js-no-dependencies-no-build-step-restaurant-analytics-dashboard-eight-svg-charts-v1-zero-dependency-analytics-surface-vocabulary.md`
- Bucket: **v1 (owner-facing analytics surface vocabulary)** — defer
- Linear parent: **not created — Linear MCP write endpoint blocked (38th consecutive day), requestId `a4ff44223faad34e`**
- Linear sub-issue: **not created — same blocker**. Intended payload at `/opt/data/le31-daily-research-2026-10-25.linear-fallback.json`
- Source repo: GitHub `Anatolii198/mesa-lite` (MIT), ★0/⑂0, 255 KB, JavaScript, created 2026-10-18T10:12:36Z, pushed 2026-10-23T19:30:22Z
- Raw fetch: `/tmp/le31-daily-2026-10-25/pv/Anatolii198__mesa-lite.json`
- Report: `/opt/data/le31-daily-research-2026-10-25.md`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: inferred.** The artifact is real (direct
`/repos/` GET, HTTP 200, in-window by both `created_at` and
`pushed_at`, MIT licence verified, 10 topics including
`no-dependencies` and `svg-charts`). **But no LE31 owner has reported
pain about analytics, dashboards, or the frontend stack.** The
existence of an independently-built no-dependency dashboard is
evidence that the *shape* exists in the world — **not** evidence of
LE31 operator demand.

**Confidence: high** for the artifact's existence and shape. **Low**
for whether an owner-facing analytics surface is ever wanted by
LE31's owner — **that is an assumption, not a finding**, and the
contract says so.

**Decision: defer (vocabulary reference).** Check 1 (JTBD) **fails**:
no reported owner pain about analytics or dashboards. Checks **3** and
**5** also fail: the implementation shape is off-stack, and an owner
dashboard is a new owner-facing surface that §3.1 does not currently
include.

**Known rabbit hole:** reading *"no Chart.js, no frameworks, no build
step"* as a mandate to remove HTMX or to rewrite LE31's UI stack.
**It is neither.** LE31's §3.2 stack is fixed and the pick does not
propose changing it. The criterion's own wording ("no client-side
framework dependency") is **provisional** and is flagged as such in
the contract's Open Questions — **the owner decides whether HTMX is
inside or outside the line.**

**Circuit breaker:** if the criterion is never added to the feature
template and no future view is ever proposed, this remains an unused
reference. **Acceptable outcome.**

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-research` — this pick came from the 2026-10-25 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.
5. `le31-handoff-spec` — the frozen-contract discipline this slice follows.
6. `le31-frontend` — the existing UI conventions, **if and only if** a
   view is ever actually being built (not for this defer slice).

If the destination repo does not ship these skills, request them
from the project owner before starting. **Do not invent LE31
conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/377-…-v1-zero-dependency-analytics-surface-vocabulary.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No template, CSS, chart, or component is
written. No dependency is added or removed.**

## What the coding agent must NOT do

- **Do not add a client-side framework** (React, Vue, Svelte, Alpine,
  or a bundler) **and do not remove one that already exists.** This
  slice records an observation; it does not authorise a stack change.
- **Do not add a charting library** (Chart.js, Recharts, D3, ECharts,
  …). If a chart is ever needed, the criterion requires an explicit
  statement of why hand-written or server-rendered SVG was not enough.
- **Do not build an owner-facing dashboard.** LE31's §3.1 surfaces are
  the waiter web UI and the cook Telegram bot. An owner reporting
  surface is **not** in scope today and this pick does not propose one.
- **Do not adopt `mesa-lite`'s markup, template, or SVG chart code.** It
  is MIT and legally adoptable, but it is a **static HTML template with
  no backend**; LE31's views are server-rendered by FastAPI with data
  from Postgres. **The transferable content is the principle, not the
  markup.**
- **Do not port or vendor the SVG chart implementations.**
- **Do not edit the charter, `le31-conventions`, or `le31-frontend`.**
  This artifact *proposes* a criterion; it does not *make* it. **Owner
  decision**, per the 2026-10-24 precedent.
- **Do not apply the criterion to the Telegram bot surface.** The
  criterion is about the **web** surface only — the bot's entire client
  is Telegram's own, so there is no HTML, no CSS, no chart, and no
  build step to have. This asymmetry is explicit in the contract and
  must not be flattened.

## The proposed criterion (the actual deliverable content)

If and when the LE31 feature template is next materially re-edited,
the waiter/owner-facing section should add:

> *When an owner-facing view is added to LE31, it must render with no
> build step and no client-side framework dependency — server-rendered
> HTML plus hand-written CSS, with charts drawn as inline SVG.*

**The honest caveat, carried forward from the contract:** this
criterion **largely describes a decision LE31 has already made** —
LE31's waiter UI is already server-rendered HTML with minimal HTMX.
So the pick's value is narrower than a new rule: it is **an outside
party reaching the same conclusion independently, for the same
reason** (the dependency tree is the cost). A charter decision that
has never faced an outside alternative is one nobody has tested.

**The in-window cluster is the second half of the finding.** One
author choosing no dependencies is a preference. **Three authors in
one 7-day window choosing no dependencies** — a LAN-only ordering
board (single file, 39 KB; feature 376), a restaurant dashboard (no
build step, 255 KB; this pick), and a material-request system (vanilla
JS + Firebase, offline-first; feature 378) — is a **coherent
engineering economy**, and it is one LE31 does not share. LE31's
answer to that economy is "we have a dependency tree and we chose it",
and that answer stands. **The criterion's job is to make the
alternative explicit at the moment a view is proposed**, not to
pretend the alternative does not exist.

## Trigger for the next step

The next time **any one** of these is true:

1. A PR adds an owner-facing or waiter-facing view.
2. A proposal to introduce a client-side framework or a bundler appears.
3. A proposal to add a charting dependency appears.

When triggered:

1. Read the contract in full, plus the `le31-frontend` skill for LE31's
   actual UI conventions.
2. **Confirm the criterion's wording with the owner** — specifically
   whether HTMX is inside or outside the "no client-side framework
   dependency" line. **The wording in this slice is provisional.**
3. The PR must state whether the criterion is met, or explicitly why
   not. **"It was faster" is not a stated reason.**

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/377-…-v1-zero-dependency-analytics-surface-vocabulary.md`
      exists and was read back.
- [ ] The repo's licence, star/fork counts, size, language, topics,
      `created_at`, `pushed_at`, `archived`, `fork` and `default_branch`
      match the raw JSON at
      `/tmp/le31-daily-2026-10-25/pv/Anatolii198__mesa-lite.json`.
- [ ] The description quoted in the contract is **verbatim** from the
      raw file — including the GitHub API's own **160-character
      truncation** (`*"…Dark and light th…"`), which must be reproduced
      as truncated, **not silently completed**.
- [ ] The topic list `['admin-dashboard','analytics','charts','dark-mode','dashboard','html-template','no-dependencies','restaurant','svg-charts','vanilla-js']`
      matches the raw file exactly (10 topics).
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] **No source file, template, CSS, chart, dependency, schema, or
      test was modified.** No framework was added or removed. No
      dashboard was built. No charter or skill edit was made.

## Rollback path

Delete
`features/377-Anatolii198-mesa-lite-mit-javascript-vanilla-js-no-dependencies-no-build-step-restaurant-analytics-dashboard-eight-svg-charts-v1-zero-dependency-analytics-surface-vocabulary.md`,
delete
`specs/Anatolii198-mesa-lite-mit-javascript-vanilla-js-no-dependencies-no-build-step-restaurant-analytics-dashboard-eight-svg-charts-v1-zero-dependency-analytics-surface-vocabulary-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and delete the (uncreated) Linear
sub-issue if it ever exists.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- **Is this criterion redundant?** LE31's waiter UI is *already*
  server-rendered HTML with minimal HTMX, so the criterion may restate
  existing behaviour. **The owner should decide whether a criterion
  that restates existing behaviour belongs in the feature template at
  all.** If not, this pick's value is only the external corroboration.
- **Where should the criterion live** — the `le31-frontend` skill, the
  feature template, or the charter? **Owner decision.**
- **What about charts specifically?** "No charting library" is a
  stronger claim than "no framework" — a charting library is a
  dependency, but frameworks like HTMX are also dependencies, and
  LE31 already accepts those. **The proposed wording is provisional
  and the owner must settle the HTMX question.**
- **Does the restaurant-operator-dashboard use case ever apply to
  LE31?** A "day's takings" view is an obvious v2 candidate, but
  **that is an assumption, not a finding**, and it is recorded as such
  in the contract.
