# ledger-claim-to-evidence-trace-graph-audit — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/129-ledger-claim-to-evidence-trace-graph-audit.md` before
> touching anything. **This is a WATCH-LIST / ARCHITECTURE-REFERENCE
> slice, NOT a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise any evidence-graph implementation.**
> It records vocabulary and structure for a decision that has not been
> made. The paper's subject is auditing LLM agents; LE31 has no agent
> and charter §3.4 is untouched. **Only the graph structure transfers.**

## Frozen identifiers (do not rename)

- Feature ID: `129`
- Slug: `ledger-claim-to-evidence-trace-graph-audit`
- Contract file: `features/129-ledger-claim-to-evidence-trace-graph-audit.md`
- Bucket: **v2 owner-pains (architecture reference)** — defer
- Linear parent: **HMM-169** (Brainstorm 2026-08-28 — daily)
- Linear sub-issue: **HMM-170** (Feature)
- Source: arXiv `2608.18398` / OpenAlex `W7203892911` (2026-08-19)
- DOI: `10.48550/arxiv.2608.18398`
- Raw fetch: `/tmp/le31-brainstorm-2026-08-28/openalex_append-only20ledger20audit.json`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: observed.** The paper exists, is in-window,
and its abstract was read in full. **Provenance note that matters:**
the abstract was reconstructed **by the parent agent** from
`abstract_inverted_index` in the raw JSON, *not* taken from the
subagent's summary — the subagent was found to have fabricated text
inside abstracts it labelled "verbatim" during this same pass (see
HMM-169 and the report's Blocker 1). Any future quotation must come
from the raw file or from arXiv directly.

**Confidence: medium-high** for mechanism quality (the structure is
clearly specified and the diagnosis is precise); **low** for present
LE31 urgency (no owner has ever asked "why is this number what it
is?").

**Decision: defer (watch-list architecture-reference).** No check
fails. Blocked solely on absence of present need.

**Known rabbit hole:** designing the edge-type taxonomy. The paper's
types come from LLM-agent workflows (tool call, file edit, validation
check) and are **not transferable**. LE31's taxonomy would have to be
designed from LE31's own operations, and that is the real cost. **Do
not attempt it in this slice.**

**Circuit breaker:** if LE31 v2 never surfaces a derived figure whose
provenance an owner disputes, this expires unused. Acceptable outcome.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-brainstorm` — this pick came from the 2026-08-28 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.

If the destination repo does not ship these skills, request them from
the project owner before starting. **Do not invent LE31 conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/129-ledger-claim-to-evidence-trace-graph-audit.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No table is created.**

## What the coding agent must NOT do

- **Do not create an evidence-node, workflow-node, or edge table.**
  No schema change of any kind.
- **Do not modify `audit_logs` or `StockEntry`.** The append-only
  posture is correct and stays correct. If this pattern is ever built
  it is strictly *additive over* those tables, never a replacement.
- **Do not design the edge-type taxonomy.** That is the load-bearing
  design question and it is deferred deliberately.
- **Do not add any LLM, agent runtime, or model dependency.** The
  paper audits LLM agents; LE31 borrows the graph shape only. Charter
  §3.4 is unchanged.
- **Do not treat this as a recommendation to build.** The need is
  anticipated, not reported.

## The three primitives (the actual deliverable content)

If a future v2 feature surfaces a disputable derived figure, these are
the structural ideas worth carrying over:

1. **Layering, not replacement** — the raw records stay authoritative
   and the graph sits over them. This is the property that keeps the
   pattern compatible with charter §3.1.
2. **Artifacts as evidence anchors** — a produced figure becomes a
   first-class node that claims point at, rather than an untracked
   side effect.
3. **Typed semantic edges** — the edge carries a type (`derived-from`,
   `supported-by`, `checked-by`). Untyped adjacency — which is all
   that timestamp ordering provides — is precisely what forces a human
   to reconstruct the chain.

**Where LE31 stands today:** charter §3.1 gives complete row-level
visibility (every mutation writes an `audit_logs` row) and **zero
typed edges**. Answering "why is this variance figure what it is?"
means a human reads rows in timestamp order and infers which fed the
computation. The rows are all there; the edges are not.

**Three-axis position:** feature 125 is the commit-time measured gate,
feature 122 is the query-time acceptance criterion, and this is the
**explanation-time** axis.

## Trigger for the next step

The first LE31 v2 feature that surfaces a derived figure whose
provenance an owner could reasonably dispute — candidates: inventory
variance, supplier reconciliation totals, any forecast.

When that happens:

1. Read the full paper, not just the abstract.
2. **First ask whether reconstruction is actually painful.** If a
   variance number is always traceable by reading twenty rows in
   order, an evidence graph is pure overhead. **Stopping here is a
   legitimate and likely outcome.**
3. **Evaluate the cheaper competing pattern before this one:** compute
   the derived figure deterministically from a *named row set* and
   store that row set alongside the figure. This may capture most of
   the value for a fraction of the cost. It has not been evaluated.
4. Design an LE31-specific edge-type taxonomy from LE31's own
   operations. Do not import the paper's.
5. Confirm the layering property holds — additive over `audit_logs`,
   never a replacement.
6. Run `le31-conventions` on that feature independently. This
   artifact pre-authorises nothing.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/129-ledger-claim-to-evidence-trace-graph-audit.md`
      exists and was read back.
- [ ] arXiv ID (`2608.18398`), OpenAlex ID (`W7203892911`), DOI, and
      publication date (2026-08-19) match the raw JSON at
      `/tmp/le31-brainstorm-2026-08-28/openalex_append-only20ledger20audit.json`.
- [ ] Quoted passages are verbatim from the **raw file**, reconstructed
      from `abstract_inverted_index` — **not** copied from the
      subagent's `_SUMMARY.md`, which is known-contaminated this pass.
- [ ] `grep -c 'LE31'` on the raw OpenAlex file returns `0` —
      confirming no LE31-specific language exists in the source and any
      such phrasing in a summary is fabricated.
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-170 exists with label `Feature` and parent HMM-169.
- [ ] No source file, schema, table, or test was modified.

## Rollback path

Delete `features/129-ledger-claim-to-evidence-trace-graph-audit.md`,
delete `specs/ledger-claim-to-evidence-trace-graph-audit-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-170.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- Are LE31's derived figures ever complex enough to justify an
  evidence graph? **This is the question that could kill the pick.**
- What is LE31's edge-type taxonomy? **Unresolved, and not derivable
  from the paper.**
- Does the layering survive schema evolution — can edges written
  against one `StockEntry` shape still resolve after a migration?
  **Unknown; full text unread.**
- Who is the auditor? The paper assumes "human or automated"
  reviewers. LE31 has exactly one stakeholder — the owner — who can
  simply ask. A structure built for institutional audit may be
  over-built for one person. **Same scepticism that constrains
  feature 121; owner decision, not an agent guess.**
- Is the simpler named-row-set pattern good enough? **Not evaluated,
  and it could shrink this to nothing.**
