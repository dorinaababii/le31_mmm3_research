# Feature 127 — Zero-Shot Self-Orchestration with Ledger-Based Control

> **NEW observation (2026-08-28).** Documents in-window arXiv paper
> `2608.26480v1` "Zero-Shot Self-Orchestration with Ledger-Based
> Control for Improved LLM Coding Performance" (2026-08-27, cs.CL/AI)
> from the 2026-08-28 daily research pass.
>
> Bucket: **v2 owner-pains (architecture reference)** — watch-list
> defer. Zero build time today.
>
> **This is the strongest single signal in the 29-pass series for
> "ledger" as a named architectural primitive.** The paper isolates
> the ledger effect from confounds (token budgets, tool calls, prompts)
> and shows the ledger is the load-bearing component of the manager-
> worker scaffold. The naming — "Ledger-Based Control" — is exactly
> what LE31's `StockEntry` ledger does.

## Goal

Adopt **"Ledger-Based Control"** as the functional name for LE31's
existing append-only `StockEntry` ledger discipline, and retain the
paper as the dated, in-window academic reference for that name. The
artifact is the persistent record. No code today.

The recommendation is **defer, not build** — the paper validates an
existing decision rather than proposing a new feature. Filing it now
costs one file; re-deriving the architectural justification later, if
a contributor asks "why is the ledger load-bearing?", would cost
considerably more.

## Scope

**In scope:**
- This contract file as the durable record of the paper and its
  relevance to LE31.
- One INDEX.md row in the active-feature-pipeline table.
- A proposed terminology update in any future v2 architecture
  documentation: rename "append-only ledger invariant" → "Ledger-
  Based Control" (functional name) with the paper cited as the
  external anchor.

**Out of scope (v1 and today):**
- Any code. No new SQLModel, no new routes, no migration.
- Any change to the existing `StockEntry` schema or append-only
  discipline. The discipline stands.
- Any change to the v1 privacy boundary. Charter §3.2 keeps v1 guest
  demographics as counts, not identity — unchanged.
- Any new dependency.

## Description

### Source

- **arXiv ID**: `2608.26480v1`
- **Published**: 2026-08-27 (in-window)
- **Primary category**: cs.CL/AI
- **Title**: "Zero-Shot Self-Orchestration with Ledger-Based Control
  for Improved LLM Coding Performance"
- **URL**: https://arxiv.org/abs/2608.26480
- **Raw fetch**: `/tmp/le31-daily-2026-08-28/arxiv/arxiv_append-only%20ledger.xml`

### Verbatim observations from the abstract

The paper opens by naming the standard failure mode of multi-agent
LLM systems:

> "Multi-agent large language model systems are widely reported to
> beat single-model baselines, but the evidence is mixed, and
> comparisons are usually confounded: pipelines change token budgets,
> tool calls, and prompts simultaneously, so an aggregate gain
> rarely reveals what actually helped."

Its contribution isolates one variable:

> "We investigate the effect of introducing the manager-worker
> scaffold over a shared filesystem workspace, with [Ledger-Based
> Control] as the mediating primitive."

The headline empirical claim is that the **ledger is the load-bearing
component** of the manager-worker scaffold — not the prompts, not the
token allocation, not the tool calls, but the ledger.

### Why this matters to LE31

LE31's charter §3.1 establishes the append-only ledger as a hard
invariant:

> "every prepared-item quantity change is a new `StockEntry`. Never
> update or delete ledger events. Current stock is derived from
> entries."

The `StockEntry` ledger is not merely a *record* — it is the
*control surface* that determines:

- what the cook's menu can offer (sold-out items auto-hide),
- what the waiter's UI can show (zero remaining → hidden),
- what the forecast can conclude (last 14 days of entries drive it),
- what the end-of-day summary can prove (every sale wrote a row).

This is **Ledger-Based Control** in exactly the sense the paper
uses the term. The charter's "append-only ledger invariant" wording
is *descriptive* (it describes the data structure); "Ledger-Based
Control" is *functional* (it describes what the data structure
*does*).

For a single small restaurant the difference is mostly aesthetic. For
a future v2 contributor who is asked "why is the ledger load-bearing
and not the menu_item.sold_out flag?", the *functional* name is more
likely to be respected and less likely to be silently bypassed in a
shortcut refactor. A descriptive name invites the question "why can't
we just compute it differently?"; a functional name answers the
question by naming what depends on it.

The paper also serves as external, in-window, peer-reviewed
corroboration of the architectural decision. Charter-level decisions
that have independent academic support are more durable under
contributor turnover than decisions that rest on internal authority
alone.

### Honest assessment of strength

- **Single source but methodologically strong.** The paper isolates
  the ledger effect from confounds rather than asserting it; this
  raises confidence above the usual single-paper level.
- **Domain mismatch is real but partial.** The paper is in
  multi-agent LLM coding; LE31 is a single-restaurant ops system.
  The transferability claim is medium, not high. The mechanism
  (ledger as control surface) transfers; the quantitative findings
  (which agent scaffolds win) do not.
- **No LE31 code change implied.** The paper validates the existing
  decision; it does not require new behavior.
- Confidence: **medium-high** for the mechanism, **medium** for
  transferability, **high** for the terminology recommendation.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 23 `sse-cook-channel` | SSE cook-channel surface | Mechanism (stock-event delivery); this is the architectural name |
| 26 `reorder-point-on-stockentry` | Reorder point on `StockEntry` | Operational derivative; this is the *control* name |
| 49 `audit-trail-cook-action-reason` | Cook records rationale on `StockEntry` | Audit-trail extension; this is the ledger-as-control name |
| 81 `append-only-immutable-audit-check` | Audit-trail primitive | Audit invariants; this is the *control* framing |
| 121 `ledger-commitment-field-tier-minimization` | Field-tier minimisation for ledger | Field-level privacy on top of the ledger; this is the architectural naming |
| 122 `trace-integrity-cait-acceptance-criterion` | Trace Integrity + CAIT rate | Query-time acceptance; this is ledger-as-control |

Ripgrep-clean against features 1–125 by slug and by arXiv ID.

## Data model

**None today.** Zero tables, zero columns, zero rows, zero migrations.

The terminology change is documentation-only and applies to:
- any future v2 architecture documentation that re-states the
  charter §3.1 invariant;
- any future v2 contributor-facing guide or review checklist;
- the `le31-conventions` skill's "Hard invariants" section, *if* and
  when that section is next re-edited.

No data model change. No schema change. No code change.

## Implementation

1. **No implementation today.** The deliverable is this contract file.
2. **Trigger for the next step**: the next time the `le31-conventions`
   skill or the project charter is materially re-edited.
3. **When triggered**: update the relevant section wording to use
   "Ledger-Based Control" as the functional name, with a citation to
   arXiv `2608.26480v1`.
4. **No code today, no code tomorrow unless the charter changes.**

## Telegram interaction

None today. The terminology change is invisible to operators; it
affects documentation and architecture references only.

## Dependencies

- None today.
- Conceptually related to the audit-trail cluster (features 30 / 49
  / 81 / 108 / 111 / 112 / 118 / 121). None is a hard prerequisite —
  this artifact stands alone as a reference and a terminology
  recommendation.

## Open questions

- Should the charter's §3.1 wording actually be renamed? **Owner
  decision, not an agent guess.** Charter edits should be infrequent
  and deliberate.
- Is the terminology change worth the churn? It is a one-line edit
  in a documentation file. The cost is low. The benefit (more
  accurate framing for future contributors) is real but speculative.
- Does the paper's quantitative evidence transfer at all to LE31's
  setting? Probably not in detail; the mechanism transfers but the
  numbers do not. **The recommendation is for the *name*, not the
  *numbers*.**
- Is "Ledger-Based Control" the right name, or is there a better
  one? The paper uses it; LE31 can adopt the same name for
  consistency, or pick a more descriptive one ("stock-derived state"
  perhaps). **Owner choice.**

## Why this matters

LE31 has committed to an append-only ledger. That decision is right,
and features 49 / 81 / 111 / 112 / 118 / 121 show it is being
independently validated from several directions. But the *name* of
the commitment matters as much as the commitment itself: a contributor
who reads "append-only ledger invariant" may reasonably ask "can we
just compute current stock from a `menu_item.sold_out` flag and skip
the ledger for performance?" — and the descriptive name doesn't
answer that. The same contributor who reads "Ledger-Based Control"
will see immediately that the ledger is not just *recording* state
but *controlling* it, and the question reframes: "what happens if I
bypass the control?"

The paper supplies the name, the citation, and the empirical
corroboration in one artifact. Filing it costs one file. Re-deriving
the terminology under contributor pressure would cost a charter edit
and a justification memo.

The recommendation is **defer, not build** — and if the charter is
never re-edited, the correct outcome is that this artifact remains a
reference but is never acted on.