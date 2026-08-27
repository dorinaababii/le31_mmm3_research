# Feature 122 — Trace Integrity + CAIT as an acceptance criterion

> **NEW observation (2026-08-27).** Documents in-window arXiv paper
> `2608.26036v1` "Trace Integrity for LLM Data Agents: A Vision for
> Auditable Structured Reasoning in Real-World Systems" (2026-08-26,
> cs.AI) from the 2026-08-27 daily research pass. The paper supplies a
> **measured** acceptance criterion for owner-facing assisted
> computation, operationalising charter §3.4's "observable evidence"
> requirement. Bucket: **v2-AI (gate-criterion reference)** —
> watch-list defer.
>
> **This artifact does NOT start any v2-AI work.** Per
> `le31-daily-research` hard rules, no v2-AI Linear issue is opened
> unless explicitly scoped as v2-AI by the owner. This is a *criterion
> for accepting* a future feature, not a feature.

## Goal

Adopt **Trace Integrity** and the **CAIT (Correct Answer / Invalid
Trace) Rate** as the acceptance vocabulary for any future LE31
owner-facing assisted computation, so that "the number looked right" is
never sufficient evidence for shipping.

The artifact is the persistent criterion record. No code today.

## Scope

**In scope:**
- This contract file as the durable record of the criterion and its
  source.
- One INDEX.md row in the active-feature-pipeline table.
- Use of the vocabulary (execution contract, Trace Integrity, CAIT
  rate) **when** the first v2 owner-facing assisted number is
  specified.

**Out of scope (v1 and today):**
- Any AI feature. No assistant, no LLM call, no model dependency.
- Any evaluation harness, benchmark runner, or CAIT-measurement
  tooling. Building one would be the classic scope creep this artifact
  is meant to prevent.
- Any change to charter §3.4. This *operationalises* it; it does not
  amend it.
- Any customer-facing surface. Charter §3.4 prohibits customer-facing
  AI and that is unchanged.
- Any new dependency.

## Description

### Source

- **arXiv ID**: `2608.26036v1`
- **Published**: 2026-08-26 (in-window)
- **Primary category**: cs.AI
- **Title**: "Trace Integrity for LLM Data Agents: A Vision for
  Auditable Structured Reasoning in Real-World Systems"
- **URL**: https://arxiv.org/abs/2608.26036
- **Raw fetch**: `/tmp/le31-daily-2026-08-27/arxiv/arxiv_kitchen_display_system.xml`
  (surfaced incidentally in the `kitchen display system` query pool)

### Verbatim observations from the abstract

The premise:

> "Answer accuracy is an insufficient reliability signal for LLM data
> agents. In structured-data tasks, a benchmark-correct answer can be
> produced by an invalid trace."

**Trace Integrity** is defined as a deployment reliability criterion
evaluating whether the computation recorded behind an answer is:

> "explicit, executable, schema-valid, operator-faithful, replayable,
> answer-consistent, and auditable."

The named failure mode is the **Structure Gap**:

> "natural-language reasoning and free-form rationales do not reliably
> specify the operator-level programs required by real-world systems."

The mechanism is **execution contracts** — "structured artifacts that
bind user intent to schema elements, operator plans, assumptions,
executable queries, verification status, and final-answer linkage."

The measurement is the **CAIT (Correct Answer / Invalid Trace) Rate**,
which "measures how often answer-only evaluation counts computationally
unsupported outputs as successes."

### The measured numbers (why this is stronger than a typical single paper)

On BIRD Mini-Dev, across three methods (Direct SQL, Operation Summary +
SQL, Contract-First SQL):

| Method | Answer accuracy | Trace Integrity Pass Rate | CAIT Rate |
|---|---|---|---|
| Direct SQL | 20% | 39% | 55% |
| Operation Summary + SQL | 22% | 43% | 59.1% |
| Contract-First SQL | 24% | 40% | 45.8% |

The finding is that **answer accuracy, trace validity, and silent-
failure risk are three distinct axes** — and that roughly half of the
answers scored "correct" were computationally unsupported.

This matters for confidence assessment: the divergence is **measured
on a public benchmark**, not asserted. Most single papers in this
series offer a mechanism; this one offers a number that makes the risk
concrete.

### Why this matters to LE31

Charter §3.4: *AI may assist owner/staff, with observable evidence and
a non-AI fallback.* "Observable evidence" is the right requirement, but
as written it is not testable — it does not say what counts as
evidence, or how you would know it was absent.

Trace Integrity makes it testable. If LE31 ever ships a v2 surface
where an assistant reports a stock discrepancy, a margin, or a
reconciliation total, the acceptance bar becomes:

1. **Explicit** — the computation is recorded, not implied.
2. **Executable** — the recorded query can actually be run.
3. **Schema-valid** — it references real columns on real tables.
4. **Operator-faithful** — the recorded operators are the ones that
   ran.
5. **Replayable** — the owner (or a maintainer) can re-run it and get
   the same answer.
6. **Answer-consistent** — the displayed number equals what the
   recorded computation produces.
7. **Auditable** — the trace persists for later inspection.

**LE31 is unusually well-placed to satisfy this**, because derived
values already come from explicit deterministic queries over the
append-only `StockEntry` ledger. An execution contract for LE31 would
largely be *recording what already happens*, rather than retrofitting
explainability onto an opaque process. The ledger provides the
replayability for free — a re-run over immutable entries gives the same
answer by construction.

The CAIT concept is worth keeping even if nothing else from the paper
is used: it names the specific way an assisted-computation feature
fails silently, and gives it a rate that can be argued about.

### Honest assessment of strength

- **Single source**, no in-window corroboration. Confidence is raised
  above the usual single-paper level only by the public-benchmark
  numbers.
- **It is a "vision" paper** by its own subtitle. The criterion is
  well-specified; the tooling is not.
- **No LE31 pain observed.** LE31 ships no owner-facing assisted
  computation today, so this addresses a hypothetical.
- The benchmark is text-to-SQL over BIRD, not restaurant operations.
  The *criterion* transfers; the *numbers* do not.
- Confidence: **medium-high** for the measurement, **low** for
  present LE31 urgency.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 68 `cook-assistant-deterministic-gate` | deterministic gate for cook assistant | Gates *whether* the assistant may act; this defines *how you accept* its output |
| 112 `twff-deterministic-process-logging-human-ai-collab` | open-standard deterministic process logging | Logging format alignment; no acceptance criterion or failure-rate metric |
| 111 `arxiv-scroll-append-only-event-log-context-arch` | append-only event log for context | Storage architecture; not output validation |
| 92 `ai-agent-decision-ledger-cluster-watch` | AI decision-ledger cluster | Recording decisions; not validating computation behind an answer |
| 121 `ledger-commitment-field-tier-minimization` | privacy minimization over a committed ledger | Privacy/disclosure; this is computational validity |
| 104 `aldia-ai-agent-business-engine-cross-section` | AI business-engine inverse-validation | Charter posture; no acceptance criterion |

Ripgrep-clean against features 1–120 by slug and by arXiv ID.

## Data model

**None today.** Zero tables, zero columns, zero rows, zero migrations.

If a v2 assisted-computation feature is ever specified, an execution
contract would plausibly persist: intent, referenced schema elements,
operator plan, assumptions, the executable query, verification status,
and the link to the final displayed answer. **Deliberately not
specified here** — that belongs to the concrete feature's own spec,
which must run the gate on its own merits.

## Implementation

1. **No implementation today.** The deliverable is this contract file.
2. **Trigger for the next step**: the first LE31 v2 feature proposal
   where an assistant reports a derived number to the owner or staff.
3. **When triggered:**
   - Apply the seven Trace Integrity properties as explicit acceptance
     criteria in that feature's Definition of Done.
   - Require the displayed number to be traceable to a recorded,
     re-runnable query over the `StockEntry` ledger.
   - Require the non-AI fallback that charter §3.4 already mandates.
   - Run `le31-conventions` on that feature independently. **This
     artifact pre-authorises nothing.**
4. **Do not build a CAIT measurement harness.** For a single small
   restaurant, per-feature acceptance is the proportionate response;
   a benchmark harness is not.
5. **If LE31 never ships owner-facing assisted computation**, this
   artifact expires unused. That is an acceptable outcome.

## Telegram interaction

None today. If a future v2 cook-bot or owner surface reports an
assisted number, the criterion would require the bot to be able to show
the computation behind it on request, with a deterministic non-AI path
always available (charter §3.4).

## Dependencies

- None today.
- Conceptually related to feature 68 (`cook-assistant-deterministic-gate`)
  — that feature decides *whether* assistance may act; this decides
  *how its output is accepted*. Complementary, neither blocking.
- Related to features 30 / 49 / 81 (audit trail), which would supply
  the replayability substrate.

## Open questions

- Will LE31 ever ship owner-facing assisted computation? If not, this
  expires.
- Which of the seven properties are load-bearing for a single small
  restaurant, and which are ceremony? **Replayable** and
  **answer-consistent** look essential; **auditable** in the formal
  sense may be over-engineering when the owner is the only
  stakeholder. This needs an owner decision, not an agent guess.
- Does the existing `StockEntry` ledger already provide replayability
  for the queries LE31 would need? Likely yes by construction, but
  unverified — no such query exists yet.
- Is the non-AI fallback (charter §3.4) sufficient on its own? For a
  single restaurant, "show the owner the deterministic number and skip
  the assistant" may be strictly better than any assisted path. **This
  question should be asked before building assistance at all**, and
  this artifact should not be read as an argument that assistance is
  desirable.

## Why this matters

The most likely way a future LE31 owner-assistance feature fails is not
a wrong answer — it is a **right-looking answer with no supporting
computation**, shipped because it matched the owner's expectation
during testing. This paper measures that failure at 45–59% on a public
benchmark, and names it.

Charter §3.4 already requires observable evidence. This artifact turns
that requirement from a principle into a checklist that a specific
feature can be held to, sourced from dated third-party work rather than
invented in-house.

Cost today: one file. Value: if assistance is ever specified, the
acceptance bar is already written, externally grounded, and not
negotiable downward under delivery pressure — which is precisely when
such bars usually get softened.

The recommendation is **defer**. Filing this artifact is explicitly
**not** a recommendation to build owner-facing assistance; charter
§3.4's non-AI fallback remains the safer default, and the "should LE31
ship assisted computation at all?" question is untouched by this
artifact.
