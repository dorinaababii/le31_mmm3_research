# skill-state-scalable-long-horizon-agent-skills — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/128-skill-state-scalable-long-horizon-agent-skills.md`
> before touching anything. **This is a WATCH-LIST / ARCHITECTURE-
> REFERENCE slice, NOT a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise any v2-AI work.** Per the
> `le31-daily-research` hard rules, v2-AI work does not start unless
> the owner explicitly scopes it. This artifact *constrains how a
> future v2 skill would store long-horizon data*; it is not that
> skill, and it is not an argument that the skill should exist.

## Frozen identifiers (do not rename)

- Feature ID: `128`
- Slug: `skill-state-scalable-long-horizon-agent-skills`
- Contract file: `features/128-skill-state-scalable-long-horizon-agent-skills.md`
- Bucket: **v2 owner-pains (architecture reference)** — defer
- Linear parent: **HMM-165** (Research 2026-08-28 — daily)
- Linear sub-issue: **HMM-168** (Feature)
- Source: arXiv `2608.26263v1` (2026-08-26, cs.CL/AI)
- Raw fetch: `/tmp/le31-daily-2026-08-28/arxiv/arxiv_append-only%20ledger.xml`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: inferred.** arXiv `2608.26263v1` is a real,
dated, in-window primary source; the diagnosis (latency degradation
+ context-poisoning failures from append-only conversation history)
is well-specified in the abstract. The *le * need is inferred from
the v2 direction, not reported. Confidence: **medium** for mechanism
quality, **low-medium** for present LE31 urgency, **medium** for the
value of the counter-argument.

**Decision: defer (watch-list architecture reference).** No check
fails. The strongest reason to file is that the paper *argues
against* the naive extension of LE31's existing append-only posture
to chat history — and naive extension is the most likely future
mistake.

**Known rabbit hole:** treating the paper's structured-state
approach as universally applicable. The paper is right for chat
history; it is *not* right for state transitions, where append-only
remains correct. Mixing the two would silently produce either bloated
storage or under-determined audit trails.

**Circuit breaker:** if LE31 v2 ships without any multi-turn dialogue
surface, this remains an unused reference. Acceptable outcome.

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
| `features/128-skill-state-scalable-long-horizon-agent-skills.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No AI code is written.**

## What the coding agent must NOT do

- **Do not build any AI feature, assistant, or LLM call.** No model
  dependency of any kind.
- **Do not build a SKILL.state runtime or any structured-state
  implementation.** This is the specific scope creep the artifact
  exists to prevent.
- **Do not extend the charter §3.1 append-only posture to chat
  history.** This artifact's load-bearing recommendation is that
  the discipline applies to state transitions and *not* to free-form
  dialogue.
- **Do not read this artifact as a recommendation to build a long-
  horizon v2 skill.** "Keep v2 skills short-horizon" is usually the
  better answer.
- **Do not edit the cook-bot's existing aiogram FSM.** v1's
  interactions are short-horizon and the FSM is sufficient.

## The discipline distinction (the actual deliverable content)

Charter §3.1 mandates append-only for `StockEntry` and other state-
transition ledgers. **This is correct and stays correct.** The
discipline applies to:

- state transitions (sell an item, prep a batch, close a bill)
- audit trails (what happened, in what order, by whom)
- derived state computation (current stock from sum of entries)

The discipline does **not** apply to:

- free-form chat history (cook-bot conversation log)
- long-horizon session state (multi-shift continuous operation)
- any data structure where latency degradation and context-poisoning
  are failure modes

The two domains share the data-structure name ("log of events") and
are easy to confuse. They differ in *what* is being logged, *why* it
is being logged, *what* reads it, and *how long* it lives.

**The load-bearing check for any future v2 feature**: confirm that
the charter §3.1 append-only posture is being applied to **state
transitions**, not to **chat history**. If the feature proposes
appending free-form dialogue to an append-only log, the discipline is
being misapplied and the paper's structured-state pattern is the
correct alternative.

## Trigger for the next step

The first LE31 v2 skill that interacts with multi-turn cook-bot or
waiter-UI dialogue.

When triggered:

1. Read the full paper (`2608.26263v1`), not just the abstract.
2. Decide whether the skill needs structured state (likely yes for
   long-horizon; likely no for short-horizon).
3. Run `le31-conventions` on the concrete v2 skill independently.
4. **Confirm that the charter §3.1 append-only posture is being
   applied to state transitions, not to chat history.** This is the
   load-bearing check.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/128-skill-state-scalable-long-horizon-agent-skills.md`
      exists and was read back.
- [ ] arXiv ID, date, and category match the raw XML at
      `/tmp/le31-daily-2026-08-28/arxiv/arxiv_append-only%20ledger.xml`.
- [ ] The diagnosis quote ("continually appending observations,
      actions, and intermediate reasoning traces to an ever-growing
      conversation history, causing latency degradation and
      context-poisoning failures over long horizons") matches the
      raw abstract **exactly** — these are the load-bearing words
      and must not be paraphrased.
- [ ] Quoted passages are verbatim from the raw file.
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-168 exists with label `Feature` and parent HMM-165.
- [ ] No source file, schema, or test was modified. **No AI code
      exists.**

## Rollback path

Delete `features/128-skill-state-scalable-long-horizon-agent-skills.md`,
delete `specs/skill-state-scalable-long-horizon-agent-skills-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-168.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- Will LE31 v2 ever ship a long-horizon multi-turn surface? If the
  answer is no, this artifact is unnecessary and should expire.
- Does the paper's structured-state approach survive schema
  evolution? **Unknown — the abstract does not say.**
- Is the trade-off (append-only auditability vs structured-state
  scalability) sharp or graded? Could a hybrid (append-only
  transitions + structured-state between transitions) work?
  **This is the load-bearing design question; unresolved today.**
- How long is "long horizon" for LE31? A single service shift is
  ~6–10 hours; a multi-shift rolling operation could be ~24 hours
  per day. The paper's targets are multi-day sessions; LE31's likely
  horizons are 1–3 orders of magnitude shorter. **The relevance
  scales with the horizon.**