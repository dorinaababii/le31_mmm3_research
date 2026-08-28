# zero-shot-self-orchestration-Ledger-Based-Control — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/127-zero-shot-self-orchestration-Ledger-Based-Control.md`
> before touching anything. **This is a WATCH-LIST / ARCHITECTURE-
> REFERENCE slice, NOT a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise any v2-AI work.** Per the
> `le31-daily-research` hard rules, v2-AI work does not start unless
> the owner explicitly scopes it. This artifact validates an existing
> charter §3.1 decision and recommends a documentation-level name
> change; it is not that change, and it is not an argument that v2-AI
> should exist.

## Frozen identifiers (do not rename)

- Feature ID: `127`
- Slug: `zero-shot-self-orchestration-Ledger-Based-Control`
- Contract file: `features/127-zero-shot-self-orchestration-Ledger-Based-Control.md`
- Bucket: **v2 owner-pains (architecture reference)** — defer
- Linear parent: **HMM-165** (Research 2026-08-28 — daily)
- Linear sub-issue: **HMM-167** (Feature)
- Source: arXiv `2608.26480v1` (2026-08-27, cs.CL/AI)
- Raw fetch: `/tmp/le31-daily-2026-08-28/arxiv/arxiv_append-only%20ledger.xml`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: reported.** The paper supplies empirical
isolation of the ledger effect from confounds (token budgets, tool
calls, prompts). The finding that the ledger is the load-bearing
component is **measured, not asserted** — which is why confidence in
the mechanism sits above the usual single-paper level.

**Confidence: medium-high** for the mechanism, **medium** for
transferability (multi-agent coding ≠ single-restaurant ops), **high**
for the terminology recommendation.

**Decision: defer (watch-list architecture reference).** No check
fails. The pick validates an existing decision and recommends a
documentation-level name change. The artifact stands as the in-window
academic reference.

**Known rabbit hole:** treating the paper's quantitative findings as
load-bearing for LE31. The *mechanism* transfers; the *numbers* do
not. The recommendation is for the *name*, not the *numbers*.

**Circuit breaker:** if LE31 v2 ships and the charter is never re-
edited, this remains an unused reference. Acceptable outcome.

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
| `features/127-zero-shot-self-orchestration-Ledger-Based-Control.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No AI code is written.**

## What the coding agent must NOT do

- **Do not build any AI feature, assistant, or LLM call.** No model
  dependency of any kind.
- **Do not edit the charter or `le31-conventions` skill.** This
  artifact *recommends* a future documentation change; it does not
  *make* the change. Charter edits are infrequent and deliberate.
- **Do not rename `StockEntry` or any existing model.** The discipline
  stands; only the *documentation name* might change.
- **Do not treat this as a v2 build trigger.** It is not.

## The terminology recommendation (the actual deliverable content)

If and when the charter or `le31-conventions` is next materially re-
edited, the relevant section should rename:

- **"append-only ledger invariant"** → **"Ledger-Based Control"**

The change is **functional**, not descriptive:
- *Descriptive* name ("append-only") describes the data structure.
- *Functional* name ("Ledger-Based Control") describes what the data
  structure *does* — it controls what the cook's menu can offer, what
  bills can be closed, what shifts can reconcile.

A future v2 contributor who reads "Ledger-Based Control" sees
immediately that the ledger is not just *recording* state but
*controlling* it. The question "why can't we just compute it
differently?" reframes to "what depends on the control?" — and the
answer is immediate.

The change is a **one-line edit** in a documentation file. The
benefit (more accurate framing for future contributors) is real but
speculative. **The change should be made deliberately, not as part
of this artifact's delivery.**

## Trigger for the next step

The next time the `le31-conventions` skill or the project charter is
materially re-edited.

When triggered:

1. Read the full paper (`2608.26480v1`), not just the abstract.
2. Confirm the proposed terminology change ("append-only ledger
   invariant" → "Ledger-Based Control") is still preferred.
3. Make the edit in one place, with a citation to arXiv
   `2608.26480v1` as the external anchor.
4. **Do not** make the change without the owner's approval; charter
   edits are not autonomous.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/127-zero-shot-self-orchestration-Ledger-Based-Control.md`
      exists and was read back.
- [ ] arXiv ID, date, and category match the raw XML at
      `/tmp/le31-daily-2026-08-28/arxiv/arxiv_append-only%20ledger.xml`.
- [ ] The confound-isolation quote (pipelines change token budgets,
      tool calls, and prompts simultaneously) matches the raw
      abstract **exactly** — this is the load-bearing framing and
      must not be paraphrased.
- [ ] Quoted passages are verbatim from the raw file.
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-167 exists with label `Feature` and parent HMM-165.
- [ ] No source file, schema, or test was modified. **No AI code
      exists.** **No charter edit was made.**

## Rollback path

Delete `features/127-zero-shot-self-orchestration-Ledger-Based-Control.md`,
delete `specs/zero-shot-self-orchestration-Ledger-Based-Control-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-167.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- Should the charter's §3.1 wording actually be renamed? **Owner
  decision, not an agent guess.**
- Is the terminology change worth the churn? Cost is low (one line);
  benefit is speculative but real.
- Does the paper's quantitative evidence transfer at all to LE31's
  setting? Probably not in detail; the mechanism transfers but the
  numbers do not. **The recommendation is for the *name*, not the
  *numbers*.**
- Is "Ledger-Based Control" the right name, or is there a better
  one? Owner choice. Alternatives: "stock-derived state", "ledger-
  controlled state".