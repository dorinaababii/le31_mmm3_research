# five-primitives-Governing-AI-Agents-at-Runtime — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/126-five-primitives-Governing-AI-Agents-at-Runtime.md`
> before touching anything. **This is a WATCH-LIST / GOVERNANCE-
> PRIMITIVE-REFERENCE slice, NOT a build slice.** There is no code
> deliverable.
>
> **This slice does NOT authorise any v2-AI work.** Per the
> `le31-daily-research` hard rules, v2-AI work does not start unless
> the owner explicitly scopes it. This artifact defines how a
> hypothetical future feature would *govern non-staff actors*; it is
> not that feature, and it is not an argument that the feature should
> exist.

## Frozen identifiers (do not rename)

- Feature ID: `126`
- Slug: `five-primitives-Governing-AI-Agents-at-Runtime`
- Contract file: `features/126-five-primitives-Governing-AI-Agents-at-Runtime.md`
- Bucket: **v2 owner-pains (governance-primitive reference)** — defer
- Linear parent: **HMM-165** (Research 2026-08-28 — daily)
- Linear sub-issue: **HMM-166** (Feature)
- Source: arXiv `2608.26696v1` (2026-08-27, cs.MA)
- Raw fetch: `/tmp/le31-daily-2026-08-28/arxiv/arxiv_append-only%20ledger.xml`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: inferred.** arXiv `2608.26696v1` is a real,
dated, in-window primary source; the mechanism is well-specified in
the abstract. The *le * need is inferred from the v2 direction, not
reported. Confidence: **medium** for mechanism quality, **low** for
present LE31 urgency.

**Decision: defer (watch-list governance-primitive reference).** No
check fails. Blocked only on absence of present need (v1 has no
non-staff actor surface).

**Known rabbit hole:** mapping five paper primitives onto a
single-restaurant two-role surface where most will be no-ops. The
correct spend is a bounded read of the full paper at the point when a
v2 feature first proposes a non-staff actor.

**Circuit breaker:** if LE31 v2 scope is settled without any non-staff
actor surface, this expires unused. Acceptable outcome.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-research` — this pick came from the 2026-08-28 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.

If the destination repo does not ship these skills, request them
from the project owner before starting. **Do not invent LE31
conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/126-five-primitives-Governing-AI-Agents-at-Runtime.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No AI code is written.**

## What the coding agent must NOT do

- **Do not build any AI feature, assistant, or LLM call.** No model
  dependency of any kind.
- **Do not build a runtime-governance primitive implementation.** This
  is the specific scope creep the artifact exists to prevent.
- **Do not create a non-staff actor surface.** Charter §3.1 prohibits
  silent transitions, and this slice does not authorise new actors.
- **Do not amend charter §3.1.** This complements it; it does not
  rewrite it.
- **Do not read this artifact as a recommendation to build a
  non-staff actor surface.** "Keep v2 actors staff-only" is usually
  the better answer.

## Trigger for the next step

The first LE31 v2 feature proposal that records a non-staff actor
surface:

1. Read the full paper (`2608.26696v1`), not just the abstract.
2. Decide whether LE31 needs any of the five primitives, or whether
   the simpler answer is to keep v2 actors staff-only (e.g. the
   cook keys in the booking on the guest's behalf).
3. **Keeping v2 actors staff-only is usually the better answer and
   should be the default.**
4. If primitives are warranted, run `le31-conventions` on the
   concrete v2 feature independently.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/126-five-primitives-Governing-AI-Agents-at-Runtime.md`
      exists and was read back.
- [ ] arXiv ID, date, and category match the raw XML at
      `/tmp/le31-daily-2026-08-28/arxiv/arxiv_append-only%20ledger.xml`.
- [ ] The three-failure-modes quote (ephemeral principals + model-
      selected actions + discovered population) matches the raw
      abstract **exactly** — these are the load-bearing words and
      must not be paraphrased.
- [ ] Quoted passages are verbatim from the raw file.
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-166 exists with label `Feature` and parent HMM-165.
- [ ] No source file, schema, or test was modified. **No AI code
      exists.**

## Rollback path

Delete `features/126-five-primitives-Governing-AI-Agents-at-Runtime.md`,
delete `specs/five-primitives-Governing-AI-Agents-at-Runtime-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-166.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- Will LE31 ever ship a non-staff actor surface? If not, expire this.
- Which subset of the paper's five primitives survives the mapping
  to a single small restaurant? **Unknown — requires the full paper.**
- Does LE31's existing charter §3.1 explicit-transition posture
  already cover the operational side of governance? Likely partially
  — but the paper's framing is about *who may do what*, which §3.1
  only implicitly addresses.
- Does LE31's chat-id allowlist work correctly for the (current)
  staff-only actors? Yes, and there is no plan to change it.