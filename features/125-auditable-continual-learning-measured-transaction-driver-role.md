# Feature 125 — Auditable Continual Learning: measured-transaction + driver-role + cumulative-halt

> **NEW observation (2026-08-27).** Documents in-window OpenAlex preprints
> `W7202188416` "Auditable Continual Learning: Measured Transactions for
> Sequential Weight Edits" (2026-08-11) + companion `W7202172049`
> "Auditable continual learning: verification code and pre-registration
> record (FP-471 to FP-516) — seals, drivers, reports, gate policies,
> and the append-only ledger slice" (2026-08-11) + v2 `W7202186994`
> (2026-08-12). From the 2026-08-27 daily-brainstorm pass.
>
> Bucket: **v2 owner-pains (architecture reference)** — watch-list
> defer. Zero build time today.

> **This is a reference artifact, not a build request.** Nothing in
> LE31 v1 needs it, because v1's `StockEntry` ledger has no effectful
> downstream cascades from a commit.

## Goal

Retain the **measured-transaction + driver-role + cumulative-halt**
vocabulary as a design reference for the first LE31 v2 surface that
records an **effectful downstream cascade** from a `StockEntry` commit
(restock triggers, supplier orders, payment reconciliation cascades,
or anything that translates a ledger commit into a derived state
change).

The artifact is the persistent design reference. No code today.

## Scope

**In scope:**
- This contract file as the durable record of the primitives and
  their source.
- One INDEX.md row in the active-feature-pipeline table.
- A bounded read of the full pre-registration bundle (FP-471..FP-516)
  **at the point when** a v2 feature first proposes an effectful
  cascade from `StockEntry`.

**Out of scope (v1 and today):**
- Any code. No `driver` column, no `cumulative_halt` table, no
  `measured_against` reference, no schema change, no migration.
- Any change to the existing `StockEntry` ledger. v1 records prepared-
  item quantity changes with explicit `via` enum entries; that posture
  stands and this feature does not reopen it.
- Any new dependency. The primitives are vocabulary, not code.
- Any v2-AI work. The paper is set in ML weight edits; LE31's v1 ships
  no AI surface and this feature does not start one.

## Description

### Sources

- **OpenAlex IDs**: `W7202188416` (primary, 2026-08-11), `W7202172049`
  (verification bundle, 2026-08-11), `W7202186994` (v2 update,
  2026-08-12), `W7172495412` (adjacent: "Measurement Drift During the
  MCP 2026 Transition", 2026-08-05).
- **Published**: 2026-08-11 (in-window)
- **URLs**:
  - https://openalex.org/W7202188416
  - https://openalex.org/W7202172049
  - https://openalex.org/W7202186994
- **Raw fetches**:
  `/tmp/le31-brainstorm-2026-08-27/oa_append-only-ledger-audit.json`

### Verbatim observations from the primary abstract

> *"Continual weight-level learning is usually treated as unsafe because
> its damage is unbounded and unaccounted. We ask whether a sequence of
> weight edits can be made transactional — each candidate measured
> against an explicit trusted base, admitted or rolled back by a
> mechanical rule, recorded in an append-only ledger — and whether the
> enforcement does any work."*

> *"the audited editor was the only method with a measured gate, a
> cumulative halt (which fired), and an append-only ledger."*

The verification bundle (`W7202172049`) abstract verbatim:

> *"Complete pre-registration and verification bundle for the auditable
> continual-learning program (FP-471 through FP-516): sealed designs
> committed before each run, the measurement drivers and editors, the
> primary result JSONs, the frozen gate-policy ladder, and the
> append-only ledger slice (4okY-4om8) containing every bank entry the
> papers cite — including retractions and corrections at full weight."*

### The three transferable primitives (extracted, generalised)

1. **measure-then-rollback at commit time** — every candidate commit
   is *measured against an explicit trusted base*, and a mechanical
   rule either *admits* or *rolls back* the commit before it reaches
   the append-only ledger. The transfer to LE31: today's charter §3.1
   already mandates explicit state transitions ("operational transitions
   are explicit user actions") but the *measured-against-trusted-base*
   framing is new vocabulary. The base in LE31's setting would be the
   prior `StockEntry` for the same `menu_item_id` — a single-row
   reference, less rich than the paper's model-checkpoint base, but the
   semantic is identical.

2. **driver role** — *"the measurement drivers and editors"* from the
   verification bundle. The driver is the named actor that translates a
   ledger commit into an effectful transition. **This is the missing
   architectural role in LE31.** Currently LE31's `actor_user_id` is a
   passive field on `StockEntry`; the *driver* notion would formalize
   *who/what applies a `StockEntry` commit to derived state* (current
   stock, per-item aggregates, future restock triggers, supplier
   orders, reconciliation totals). Charter §3.1 commits to explicit
   transitions attributable to a named actor; the driver is the
   architectural primitive that *names* the actor for cascades.

3. **cumulative halt** — a gate that fires once a measured threshold
   is crossed; the gate **prevents further commits** until reviewed.
   Distinct from feature 122 (Trace Integrity CAIT) which is a
   *query-time* acceptance criterion. The cumulative halt is a
   *commit-time* veto. LE31's v1 has no such gate; the closest
   analogue is the deterministic-gate primitive from feature 68
   (`cook-assistant-deterministic-gate`) which gates an assistant
   proposal *before* a `StockEntry` commit, but per-assistant not
   per-context.

### Why this matters to LE31

LE31's charter §3.1 makes the `StockEntry` ledger append-only: every
prepared-item quantity change is a new entry, entries are never updated
or deleted, and current stock is derived. Charter §3.2 keeps v1 data
minimal and §3.4 requires observable evidence for any AI assistance.

These rules are comfortable together for v1 because LE31 has **no
effectful downstream cascades** from `StockEntry`: today, a commit
only updates current-stock derived state, and the rest of the system
reads that derived state passively. The moment a v2 surface proposes
to **react** to a commit (auto-reorder, supplier email, payment
reconciliation, end-of-shift recap), the architectural primitives
from this paper become directly relevant:

- The *driver* role names who applied the cascade, so the cascade
  itself is attributable and reversible through the ledger.
- The *measure-then-rollback* discipline means the cascade is
  rejected at commit time if the measured base disagrees, rather
  than cascading an invalid state forward.
- The *cumulative halt* is the per-context gate that prevents a
  runaway cascade from committing further state until the operator
  reviews.

Filing the vocabulary now means the v2 boundary is well-named when
it arrives, rather than rediscovered under pressure.

### Honest assessment of strength

- **Single source cluster.** Three related OpenAlex preprints, all
  2026-08-11..12, abstracts read in full from raw JSON. No independent
  in-window corroborating source.
- **No LE31 pain observed.** No owner has reported a missing-driver-role
  or cumulative-halt problem, because v1's append-only ledger works
  fine for the current single-restaurant scope.
- **The primitives are abstract.** "Trusted base" in LE31's setting
  is the prior `StockEntry` for the same `menu_item_id` (a
  single-row reference, less rich than the paper's model-checkpoint
  base). The transfer works but adds less than the ML setting.
- **The paper is set in a v2-AI domain** (continual learning on
  Qwen2.5-3B-Instruct). LE31 v1 ships no AI surface. The primitives
  transfer because both settings have an append-only ledger and a need
  for measurable, attributable, haltable transactions, but the
  evidence base is AI-adjacent.
- Confidence: **medium** for primitive quality, **low** for present
  LE31 urgency.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 49 `postledger-tamper-evident-hash` | SHA-256 hash chain on `StockEntry` | Hash chain; no driver role or cumulative halt |
| 81 `append-only-immutable-audit-check` | `/audit-check` walk of the hash chain | Verification surface; no commit-time gate |
| 108 `telegram-chat-history-fuzzy-search-stockentry-audit` | Telegram fuzzy-search indexing for audit trail | Search/indexing surface; not commit-time primitives |
| 111 `arxiv-scroll-append-only-event-log-context-arch` | arXiv Scroll: append-only Event Log + eviction index | Retrieval over an event log; not commit-time primitives |
| 112 `twff-deterministic-process-logging-human-ai-collab` | Open-standard deterministic process logging | Logging standard alignment; no driver/measured-transaction/halt vocabulary |
| 121 `ledger-commitment-field-tier-minimization` | Field-tier minimisation with pre-commitment canonical digest | Privacy posture at commit time; no driver role or halt |
| 122 `trace-integrity-cait-acceptance-criterion` | Trace Integrity + CAIT rate as query-time acceptance criterion | Query-time acceptance; this is commit-time primitives |
| 68 `cook-assistant-deterministic-gate` | AssistantProposal → deterministic gate → StockEntry | Per-assistant gate; cumulative halt is per-context and *commit-time veto* |

Ripgrep-clean against features 1–124 by slug, by arXiv ID, by
OpenAlex ID, and by the candidate-phrase grep
(`measured.transaction|Measured Transaction|driver-as-translator|seals.+drivers.+gate|21881995|21881977|21805084|W7202188416|W7172495412|W7202172049`) — zero matches.

## Data model

**None today.** Zero tables, zero columns, zero rows, zero migrations.

If and when a v2 surface introduces effectful downstream cascades, the
primitives would imply (not yet decided, not yet designed):

- A `driver` column (or a `Driver` table) on the relevant `StockEntry`
  row, naming the actor that applies the entry to derived state;
- A `measured_against` column holding the trusted base reference
  (e.g., the prior `StockEntry` id for the same `menu_item_id`);
- A `cumulative_halt` table or flag carrying the per-context gate
  state (which contexts are halted, why, since when, who reviews);
- **No change** to existing `StockEntry` rows, which already carry the
  `via` enum and `actor_user_id` discipline charter §3.1 requires.

These are sketches for a future decision, deliberately not specified
here.

## Implementation

1. **No implementation today.** The deliverable is this contract file.
2. **Trigger for the next step**: the first LE31 v2 feature proposal
   that introduces an effectful downstream cascade from a `StockEntry`
   commit (restock trigger, supplier email, payment reconciliation
   cascade, end-of-shift auto-recap, etc.).
3. **When triggered:**
   - Read the full pre-registration bundle (FP-471..FP-516), not just
     the abstract, with specific attention to the gate-policy ladder
     and the seal / driver / report triplet.
   - Decide whether LE31 needs a *driver* role at all, or whether
     naming `actor_user_id` more explicitly is sufficient. **Often the
     simpler answer is right.**
   - Decide whether a *cumulative halt* is proportionate for the
     cascade in question, or whether a per-cascade revert is enough.
   - If either primitive is warranted, run `le31-conventions` on the
     concrete v2 feature — this artifact does not pre-authorise
     anything.
4. **If no v2 effectful-cascade surface appears**, this artifact
   expires. That is an acceptable outcome.

## Telegram interaction

None. No cook-bot or waiter-UI surface is touched. The primitives, if
ever adopted, are invisible to operators by design (the *driver*
appears only in audit trails; the *cumulative halt* surfaces as a
single rejection message at most).

## Dependencies

- None today.
- Conceptually related to features 30 / 49 / 81 / 108 / 111 / 112 /
  121 / 122 (audit-trail + append-only cluster) and 68
  (`cook-assistant-deterministic-gate`). None is a hard prerequisite —
  this artifact stands alone as a reference.
- If LE31 ever ships owner-facing assistance (charter §3.4), the
  *cumulative halt* primitive becomes directly relevant and should be
  re-read at that point.

## Open questions

- Will LE31 v2 ever introduce effectful downstream cascades from
  `StockEntry`? If no, expire this artifact.
- Is the *driver* role worth modeling as a separate primitive, or is
  expanding `actor_user_id`'s semantics sufficient? The paper's
  setting is ML (where the driver is distinct from the editor); LE31's
  setting may collapse the two into one named actor.
- What "trusted base" means in LE31's single-restaurant setting.
  Single-row reference (prior `StockEntry` for the same
  `menu_item_id`) is the obvious choice but adds little beyond
  `prev_hash`. The paper's value comes from a multi-row base (model
  checkpoint vs weight edit) which LE31 doesn't have.
- Is a *cumulative halt* proportionate for any plausible v2 cascade?
  The paper's halt is fired by an ML damage threshold; LE31's
  cascade-side analogue might be a per-supplier aggregate, a per-day
  aggregate, or a per-restaurant aggregate — each with different halt
  semantics.

## Why this matters

LE31 has already committed to an append-only ledger. That decision is
right, and features 30 / 49 / 81 / 108 / 111 / 112 / 118 / 121 / 122
show it is being independently validated from several directions. But
an append-only ledger has one consequence LE31 has not yet had to
face: **what happens when a commit causes a cascade?** Charter §3.1
covers the commit (explicit, attributable) and charter §3.4 covers
assistance (observable evidence, non-AI fallback), but neither
explicitly names who/what translates the commit into derived state,
nor what gate prevents a runaway cascade.

The 2026-08-11 Auditable Continual Learning pre-registration suite
supplies the vocabulary: **measured transaction + driver + cumulative
halt**. Three named primitives that, if adopted at the v2 boundary,
would make the cascade itself attributable and reversible.

Filing this costs one file. Re-deriving the vocabulary under the
pressure of a v2 cascade design would cost more, and would likely
miss the "measured against an explicit trusted base" framing which is
the paper's load-bearing property.

The recommendation is **defer, not build** — and if v2 never
introduces an effectful cascade, the correct outcome is that this
artifact quietly expires unused.
