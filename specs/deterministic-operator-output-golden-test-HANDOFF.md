# deterministic-operator-output-golden-test — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/123-deterministic-operator-output-golden-test.md` before
> touching anything. **This is a PARKING-LOT / TECHNIQUE-REFERENCE
> slice, NOT a build slice.** There is no code deliverable today.
>
> **This is the weakest of the three picks from 2026-08-27.** The source
> repo is 1★ / 0 forks and is cited for its idea, not its adoption. Do
> not inflate it.

## Frozen identifiers (do not rename)

- Feature ID: `123`
- Slug: `deterministic-operator-output-golden-test`
- Contract file: `features/123-deterministic-operator-output-golden-test.md`
- Bucket: **v2 utility (technique reference)** — defer / parking-lot
- Linear parent: **HMM-159** (Research 2026-08-27 — daily)
- Linear sub-issue: **HMM-162** (Feature)
- Source: `nicholasrossi0530/escpos-render` — 1★, 0 forks, MIT, Go,
  pushed 2026-08-24T18:39:38Z
- Raw fetch: `/tmp/le31-daily-2026-08-27/gh_search/gh_pos_go.json`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: observed** (the repo exists and states its
purpose). **The star count is explicitly NOT the evidence** — per the
standing pitfall, stars are not restaurant need, and 1★ / 0 forks is no
demand signal at all. The evidence is that the *technique* is
well-defined and transferable.

**Confidence: low-medium.** Genuinely the weakest of the three picks
from this pass.

**Decision: defer (parking-lot technique reference).** No check fails,
but present value is contingent on LE31 having rendered operator output
complex enough to regress — which today it may not.

**Known rabbit hole:** brittle golden tests that fail on every cosmetic
change, get reflexively `--update`-ed or disabled, and end up asserting
nothing. **A brittle golden test is worse than no golden test**, because
it trains people to bypass a failing check.

**Circuit breaker:** if cook-bot rendering stays simple, or if LE31 CI
already has a test that would catch a rendering regression, this expires
unused.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-research` — this pick came from the 2026-08-27 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.

If the destination repo does not ship these skills, request them from
the project owner before starting. **Do not invent LE31 conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/123-deterministic-operator-output-golden-test.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added.**

## What the coding agent must NOT do

- **Do not add ESC/POS or thermal-printer support.** LE31's cook surface
  is a Telegram bot (charter §3.1). Physical receipt printing is not in
  v1 and is not proposed here.
- **Do not add a Go dependency and do not vendor the referenced repo.**
  LE31 is Python 3.13. The repo is a reference, never a dependency.
- **Do not snapshot whitespace, emoji choice, or decorative
  separators.** That is the brittleness that kills the technique.
- **Do not snapshot entire message bodies verbatim** if that makes the
  test fail on cosmetic edits.
- **NEVER weaken or delete a golden test to make CI green.** If one
  fails: either the rendering regressed (fix the rendering) or the
  change was intended (read the diff, review it, update deliberately).
  Reflexive `--update` makes the whole technique worthless.

## The technique, for when it is triggered

The LE31 analogue of a "virtual printer" is the **Telegram send
payload**:

1. Ensure cook-bot payload construction is a **pure function** — order
   state in, message payload out, no I/O.
2. Snapshot the payload (text, entities, `reply_markup`) for a small set
   of representative orders. **No Telegram API call.**
3. Commit the snapshots; diff in CI.
4. **Scope assertions to semantically load-bearing content** — item
   names, quantities, modifiers, totals, button actions — and *not* to
   formatting cosmetics.

## Trigger for the next step

The next material change to cook-bot ticket rendering, or the
introduction of an owner recap/summary output.

**Best sequenced alongside a rendering change**, not as standalone work,
so golden files are written against a deliberately-reviewed rendering
rather than retrofitted onto one nobody re-examined.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only today:

- [ ] `features/123-deterministic-operator-output-golden-test.md` exists
      and was read back.
- [ ] Repo name, star count (**1★**), fork count (**0**), license
      (**MIT**), language (**Go**), and `pushed_at`
      (**2026-08-24T18:39:38Z**) match the raw JSON at
      `/tmp/le31-daily-2026-08-27/gh_search/gh_pos_go.json`.
- [ ] The repo description is quoted **verbatim**, not paraphrased.
- [ ] The contract states plainly that 1★ is not a demand signal.
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-162 exists with label `Feature` and parent HMM-159.
- [ ] No source file or test was modified.

**If this slice is ever actually built**, verification becomes
behavioural: change the rendering deliberately, watch the golden test
**fail**, then accept the new golden file. A golden test that has only
ever passed proves nothing.

## Rollback path

Delete `features/123-deterministic-operator-output-golden-test.md`,
delete `specs/deterministic-operator-output-golden-test-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-162.

**Rollback cost: zero.** No schema, no behaviour, no dependency.

If the technique is later implemented and then removed, rollback is
deleting the golden files and the test — also zero risk, since it is
test infrastructure that touches no state, stock, money, or privacy.

## Open questions carried into the slice

- Is LE31's cook-bot rendering complex enough today to justify this?
  **Probably not yet** — the main reason for parking-lot rather than
  build.
- Is cook-bot payload construction currently a pure function, or
  interleaved with sending? If interleaved, a small refactor is needed
  first, which changes the cost calculus.
- What assertion granularity avoids brittleness without being too weak
  to catch real regressions? Probably a structured projection of the
  payload — **undecided**.
- Should the waiter web UI get the same treatment, or is that better
  served by ordinary integration tests?
- **Does LE31 CI already have a test that would catch a cook-bot
  rendering regression? Unverified in this pass.** If yes, this artifact
  adds little and should expire.
