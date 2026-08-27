# trace-integrity-cait-acceptance-criterion — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/122-trace-integrity-cait-acceptance-criterion.md` before
> touching anything. **This is a WATCH-LIST / GATE-CRITERION slice, NOT
> a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise any v2-AI work.** Per the
> `le31-daily-research` hard rules, v2-AI work does not start unless the
> owner explicitly scopes it. This artifact defines how a hypothetical
> future feature would be *accepted*; it is not that feature, and it is
> not an argument that the feature should exist.

## Frozen identifiers (do not rename)

- Feature ID: `122`
- Slug: `trace-integrity-cait-acceptance-criterion`
- Contract file: `features/122-trace-integrity-cait-acceptance-criterion.md`
- Bucket: **v2-AI (gate-criterion reference)** — defer
- Linear parent: **HMM-159** (Research 2026-08-27 — daily)
- Linear sub-issue: **HMM-161** (Feature)
- Source: arXiv `2608.26036v1` (2026-08-26, cs.AI)
- Raw fetch: `/tmp/le31-daily-2026-08-27/arxiv/arxiv_kitchen_display_system.xml`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: reported.** The paper supplies measured
numbers on a public benchmark (BIRD Mini-Dev): answer accuracy
20/22/24% against Trace Integrity Pass Rate 39/43/40% and CAIT
55/59.1/45.8%. The divergence between answer-correctness and
trace-validity is **measured, not asserted**, which is why confidence
sits above the usual single-paper level.

**Confidence: medium-high** for the measurement; **low** for present
LE31 urgency (LE31 ships no owner-facing assisted computation today).

**Decision: defer (watch-list gate-criterion reference).** No check
fails. This is the pick most likely to actually get used, because it
constrains how a future feature is *accepted* rather than proposing a
feature.

**Known rabbit hole:** scope creep into building a CAIT measurement
harness or evaluation framework. **Explicitly out of scope.** For a
single small restaurant, per-feature acceptance is the proportionate
response.

**Circuit breaker:** if LE31 never ships owner-facing assisted
computation, this expires unused. Acceptable outcome.

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
| `features/122-trace-integrity-cait-acceptance-criterion.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No AI code is written.**

## What the coding agent must NOT do

- **Do not build any AI feature, assistant, or LLM call.** No model
  dependency of any kind.
- **Do not build an evaluation harness, benchmark runner, or
  CAIT-measurement tooling.** This is the specific scope creep the
  artifact exists to prevent.
- **Do not create a customer-facing surface.** Charter §3.4 prohibits
  customer-facing AI; unchanged.
- **Do not amend charter §3.4.** This operationalises it; it does not
  rewrite it.
- **Do not read this artifact as a recommendation to build owner-facing
  assistance.** The §3.4 non-AI fallback remains the safer default.

## The seven acceptance properties (the actual deliverable content)

If a future v2 feature has an assistant report a derived number, that
feature's Definition of Done must require the recorded computation to
be:

1. **Explicit** — recorded, not implied.
2. **Executable** — the recorded query can actually be run.
3. **Schema-valid** — references real columns on real tables.
4. **Operator-faithful** — recorded operators are the ones that ran.
5. **Replayable** — re-runnable to the same answer.
6. **Answer-consistent** — displayed number equals what the recorded
   computation produces.
7. **Auditable** — the trace persists for later inspection.

**LE31 is unusually well-placed here:** derived values already come from
explicit deterministic queries over the append-only `StockEntry`
ledger, so satisfying these is largely *recording what already
happens*. Replayability is nearly free — re-running over immutable
entries gives the same answer by construction.

## Trigger for the next step

The first LE31 v2 feature proposal where an assistant reports a derived
number to the owner or staff.

When that happens:

1. Apply the seven properties as explicit acceptance criteria in that
   feature's Definition of Done.
2. Require the number to be traceable to a recorded, re-runnable query
   over the `StockEntry` ledger.
3. Require the non-AI fallback charter §3.4 already mandates.
4. **First ask whether assistance is warranted at all** — "show the
   owner the deterministic number and skip the assistant" may be
   strictly better for a single restaurant.
5. Run `le31-conventions` on that feature independently.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/122-trace-integrity-cait-acceptance-criterion.md`
      exists and was read back.
- [ ] arXiv ID, date, and category match the raw XML at
      `/tmp/le31-daily-2026-08-27/arxiv/arxiv_kitchen_display_system.xml`.
- [ ] The three-method table (20/22/24%, 39/43/40%, 55/59.1/45.8%) matches
      the raw abstract **exactly** — these are the load-bearing numbers
      and must not be rounded, reordered, or reconstructed from memory.
- [ ] Quoted passages are verbatim from the raw file.
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-161 exists with label `Feature` and parent HMM-159.
- [ ] No source file, schema, or test was modified. **No AI code
      exists.**

## Rollback path

Delete `features/122-trace-integrity-cait-acceptance-criterion.md`,
delete `specs/trace-integrity-cait-acceptance-criterion-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-161.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- Will LE31 ever ship owner-facing assisted computation? If not, expire
  this.
- Which of the seven properties are load-bearing for a single small
  restaurant, and which are ceremony? **Replayable** and
  **answer-consistent** look essential; formal **auditability** may be
  over-engineering when the owner is the only stakeholder. **Owner
  decision, not an agent guess.**
- Does the existing `StockEntry` ledger already give replayability for
  the queries LE31 would need? Likely yes by construction, but
  unverified — no such query exists yet.
- Is the §3.4 non-AI fallback sufficient on its own? This question
  should be settled before building assistance at all.
