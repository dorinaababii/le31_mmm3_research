# Feature 129 — LEDGER claim-to-evidence trace graph audit

> **NEW observation (2026-08-28).** Documents in-window arXiv paper
> `2608.18398` "LEDGER: Claim-to-Evidence Trace Graphs for Auditing
> LLM Agents" (2026-08-19) from the 2026-08-28 brainstorm pass.
> Bucket: **v2 owner-pains (architecture reference)** — watch-list
> defer. Zero build time today.
>
> **The paper names the gap in LE31's `audit_logs` precisely.** LE31
> has complete row-level visibility of every mutation and *no typed
> edge* from a derived number back to the rows and checks that
> produced it. The paper's own diagnosis — visibility alone still
> forces reviewers to reconstruct which actions matter for a
> conclusion — is a statement of LE31's condition, not an analogy.

## Goal

Retain the **claim-to-evidence trace graph** discipline as a design
reference for the first LE31 v2 feature that surfaces a derived
figure the owner is likely to challenge. The paper answers: *given a
complete execution log, how do you make "why is this conclusion what
it is?" mechanically answerable instead of a human reconstruction
job?* The answer is typed semantic edges from claims to the
artifacts and checks that support them, layered over the raw records
rather than replacing them.

## Scope

**In scope:**
- This contract file as the durable record of the paper and the
  three primitives it names (Evidence Nodes, Workflow Nodes, typed
  semantic edges over preserved Trace Records).
- One INDEX.md row in the active-feature-pipeline table.
- A bounded read of the full paper (not just the abstract) **at the
  point when** a v2 feature first surfaces a derived figure whose
  provenance an owner could reasonably dispute.

**Out of scope (v1 and today):**
- Any code. No evidence-node table, no edge table, no schema
  change, no migration, no API surface.
- Any change to `audit_logs` or `StockEntry`. The append-only
  posture is correct and stays correct; this is strictly additive
  and only *if* built.
- Any edge-type taxonomy design. The paper's taxonomy is drawn from
  LLM-agent workflows (tool calls, file edits, validation checks)
  and is **not** transferable as-is; LE31's taxonomy would have to
  be designed from LE31's own operations. That design work is
  explicitly deferred.
- Any LLM or agent runtime. The paper's subject is auditing LLM
  agents; LE31 borrows only the graph structure, not the agent
  context. Charter §3.4 is untouched.
- Any new dependency.

## Description

### Source

- **arXiv ID**: `2608.18398`
- **OpenAlex ID**: `W7203892911`
- **Published**: 2026-08-19 (in-window)
- **DOI**: `10.48550/arxiv.2608.18398`
- **Source**: arXiv (Cornell University), via OpenAlex
- **URL**: https://arxiv.org/abs/2608.18398
- **Raw fetch**: `/tmp/le31-brainstorm-2026-08-28/openalex_append-only20ledger20audit.json`
- **Abstract provenance**: reconstructed by the parent agent from
  `abstract_inverted_index` in the raw JSON. **Not** taken from the
  subagent summary, which was found to have interpolated invented
  text into other abstracts in this same pass (see the report's
  Blocker 1).

### Verbatim observations from the abstract

The paper states the productivity shift that motivates it:

> "As agents do more work faster, the productivity bottleneck
> shifts from producing outputs to auditing whether those outputs
> are correct and trustworthy."

And then names the specific insufficiency of plain observability —
this is the sentence that maps onto LE31:

> "Agent observability systems make fine-grained execution events
> visible, but visibility alone still leaves reviewers to
> reconstruct which actions, artifacts, and validation steps matter
> for a particular conclusion."

The proposed structure:

> "We introduce LEDGER - Layered Evidence and Decision Graphs for
> Execution Review, a tracing and review system that builds layered
> trace graphs over observed agent sessions. LEDGER preserves Trace
> Records while grouping them into Evidence Nodes and Workflow
> Nodes, representing artifacts as evidence anchors, and adding
> typed semantic edges that connect claims to supporting actions,
> artifacts, and checks."

And the evaluated outcome:

> "Through data-analysis and coding examples, we show how the
> resulting traces expose workflow decisions, artifact lineage,
> repair steps, validation coverage, and claim-support paths for
> evidence-centered audit."

### The three transferable primitives

1. **Layering, not replacement.** LEDGER "preserves Trace Records
   while grouping them" — the raw log stays authoritative and the
   graph sits over it. This is the property that makes the pattern
   compatible with charter §3.1: `audit_logs` and `StockEntry` rows
   would remain exactly as they are.
2. **Artifacts as evidence anchors.** A produced thing (a file, a
   report, a number) is a first-class node that other claims point
   at, rather than an untracked side effect.
3. **Typed semantic edges.** The edge carries a *type* — this claim
   is *supported-by* that check, this figure is *derived-from* those
   rows. Untyped adjacency (which is what timestamp ordering gives
   you) is what forces human reconstruction.

### Why this matters to LE31

Charter §3.1 mandates that every mutation writes an `audit_logs`
row. That gives LE31 **complete visibility** and it is the right
foundation. What it does not give is **structure over that
visibility**.

Concretely: when the owner asks "why is this month's stock variance
figure what it is?", answering today means a human reading
`StockEntry` and `audit_logs` rows in timestamp order and
reconstructing which ones fed the computation and which checks ran.
The rows are all there. The *edges* are not. The paper's framing is
that this reconstruction burden is the actual cost, and that the
fix is structural rather than more logging.

This completes a three-axis picture LE31 has been assembling:

| Axis | When it acts | Feature |
|---|---|---|
| Commit-time measured gate | before a write lands | 125 |
| Query-time acceptance criterion | when output is accepted | 122 |
| **Explanation-time traceability** | **when a conclusion is questioned** | **this one** |

The cost asymmetry is the argument for filing now rather than later:
designing evidence edges in from the start is cheap; retrofitting
them onto an audit log that was never designed to carry them means
backfilling provenance that may no longer be recoverable.

### Honest assessment of strength

- **Single source, and a preprint.** One arXiv paper, no in-window
  corroboration. Confidence **medium-high for mechanism quality**
  (the structure is clearly specified and the diagnosis is precise),
  **low for present LE31 urgency**.
- **Domain gap is real.** The paper audits LLM agents doing
  long-horizon technical work. LE31 has no agent, and charter §3.4
  forbids customer-facing AI. **Only the graph structure transfers.**
  The evaluation (data-analysis and coding workflows) says nothing
  about restaurant operations.
- **No LE31 pain has been observed.** No owner has asked "why is
  this number what it is?" in any prior pass. v1's derived figures
  are simple enough to trace by eye. The need is anticipated, not
  reported — stated plainly rather than dressed up as demand.
- **The expensive part is not in the paper.** LE31's edge-type
  taxonomy would have to be designed from scratch. The paper
  supplies the shape and none of the content.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 30 `append-only-audit-redirect` | Routes writes through one function so they cannot bypass the ledger | Write-path enforcement; this is read-path explanation |
| 49 `postledger-tamper-evident-hash` | Per-row cryptographic proof of no tampering | Proves rows *unchanged*; this explains how rows *combine* |
| 61 `holdfast-approval-ledger` | Approval events as immutable rows | Records approvals; this types the edges between them |
| 81 `append-only-immutable-audit-check` | Audit invariant check | Verifies the invariant; this structures what sits on top |
| 111 `arxiv-scroll-append-only-event-log-context-arch` | Append-only event log context architecture | Storage architecture; this is provenance graph over storage |
| 122 `trace-integrity-cait-acceptance-criterion` | Trace Integrity + CAIT rate | **Query-time acceptance**; this is explanation-time traceability |
| 125 `auditable-continual-learning-...-driver-role` | Measured transaction, driver role, cumulative halt | **Commit-time gate**; this is post-hoc explanation |
| 128 `skill-state-scalable-long-horizon-agent-skills` | Structured state vs append-only for chat | Chat-history data structure; this is audit provenance |

Ripgrep-clean against features 1–128 by slug, by arXiv ID
(`2608.18398`), by OpenAlex ID (`W7203892911`), and by concept terms
(`claim-to-evidence`, `trace graph`, `evidence anchor`, `artifact
lineage` — all zero matches).

## Data model

**None today.** Zero tables, zero columns, zero rows, zero
migrations.

If and when a v2 feature needs explanation-time traceability, the
mechanism would imply (not decided, not designed):

- an `EvidenceNode` concept anchoring a produced artifact or figure;
- a `WorkflowNode` concept grouping the rows belonging to one
  operational episode (a shift, a reconciliation, a stock count);
- a typed edge table (`supported_by`, `derived_from`,
  `checked_by`) referencing existing `audit_logs` / `StockEntry`
  primary keys;
- **no change** to `audit_logs` or `StockEntry` rows, which stay
  append-only and authoritative.

These are sketches for a future decision, deliberately not
specified here. The edge-type vocabulary is the load-bearing design
question and is **not** answered by the paper.

## Implementation

1. **No implementation today.** The deliverable is this contract
   file.
2. **Trigger for the next step**: the first LE31 v2 feature that
   surfaces a derived figure whose provenance an owner could
   reasonably dispute (candidates: inventory variance, supplier
   reconciliation totals, any forecast).
3. **When triggered**:
   - Read the full paper, not just the abstract.
   - Determine whether LE31's derived figures are complex enough
     that reconstruction is actually painful. **If they are not,
     stop here** — the honest answer may be that timestamp ordering
     is sufficient.
   - Design an LE31-specific edge-type taxonomy from LE31's own
     operations. Do not import the paper's.
   - Run `le31-conventions` on the concrete v2 feature. This
     artifact pre-authorises nothing.
   - Confirm the layering property holds: the graph is additive
     over `audit_logs`, never a replacement.
4. **If no v2 feature surfaces a disputable derived figure**, this
   artifact expires. That is an acceptable outcome.

## Telegram interaction

None today. If ever built, the plausible owner-facing surface is a
"show me why" affordance on a reported figure — but that is a v2
design question, not a commitment, and the cook surface would not
be involved at all.

## Dependencies

- None today.
- Conceptually related to features 30 / 49 / 61 / 81 / 111 / 122 /
  125 (audit-trail and provenance cluster). None is a hard
  prerequisite; this artifact stands alone as a reference.

## Open questions

- Are LE31's derived figures ever complex enough to justify an
  evidence graph? **Unknown, and this is the question that could
  kill the pick.** If a variance number is always traceable by
  reading twenty rows in order, the graph is pure overhead.
- What is LE31's edge-type taxonomy? **Unresolved and not derivable
  from the paper.** This is the load-bearing design question.
- Does the paper's layering survive schema evolution — can edges
  written against one `StockEntry` shape still resolve after a
  migration? **Unknown; the abstract does not say and the full text
  has not been read.**
- Who is the auditor? The paper assumes "human or automated"
  reviewers. LE31 has exactly one stakeholder: the owner. A
  structure designed for institutional audit may be over-built for
  a single person who can simply ask. **This mirrors the open
  question that constrains feature 121 and deserves the same
  scepticism.**
- Is this cheaper than the alternative of computing derived figures
  *deterministically from a named row set* and storing that row set
  with the figure? A much simpler pattern might get most of the
  value. **Not evaluated.**

## Why this matters

LE31's audit posture is strong on the write side and unstructured on
the read side. Every mutation is recorded; nothing records *what
combined into what*. The paper's contribution is naming that gap as
a structural problem rather than a logging shortfall, and giving the
missing pieces names: evidence anchors and typed edges over
preserved records.

Filing the observation costs one file. The alternative — discovering
at the v2 boundary that provenance edges are needed and that the
historical rows no longer carry enough information to backfill them
— costs a redesign plus a permanent gap in the record for everything
already written.

The recommendation is **defer, not build**. The need is anticipated
rather than observed, the edge taxonomy is unsolved, and the
simplest competing pattern (store the row set alongside the figure)
has not been ruled out. If v2 never surfaces a disputable derived
figure, the correct outcome is that this artifact quietly expires
unused.
