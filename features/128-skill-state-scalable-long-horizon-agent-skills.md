# Feature 128 — SKILL.state: Scalable Long-Horizon Agent Skills

> **NEW observation (2026-08-28).** Documents in-window arXiv paper
> `2608.26263v1` "SKILL.state: Scalable Long-Horizon Agent Skills"
> (2026-08-26, cs.CL/AI) from the 2026-08-28 daily research pass.
> Bucket: **v2 owner-pains (architecture reference)** — watch-list
> defer. Zero build time today.
>
> **The paper's diagnosis is the inverse of LE31's `StockEntry`
> discipline.** Same data structure (append-only); opposite value
> judgement (right for state transitions, wrong for free-form
> dialogue). Filing this prevents the most likely future mistake:
> the naive extension of LE31's append-only posture to chat history.

## Goal

Retain the **SKILL.state** discipline as a design constraint for the
first LE31 v2 skill that interacts with multi-turn cook-bot or
waiter-UI dialogue. The paper answers: *what data structure does a
long-horizon agent use to avoid conversation-history poisoning?* The
answer is *not* an append-only log; it is a structured state. This
artifact exists so LE31 does not extend its append-only ledger
discipline to chat history by default — which would be the wrong
choice.

## Scope

**In scope:**
- This contract file as the durable record of the paper and its
  negative-result implication for LE31 (i.e. *do not* extend the
  append-only posture to chat history).
- One INDEX.md row in the active-feature-pipeline table.
- A bounded read of the full paper (not just the abstract) **at the
  point when** a v2 skill first interacts with multi-turn dialogue.

**Out of scope (v1 and today):**
- Any code. No SKILL.state runtime, no skill-state implementation,
  no schema change, no migration.
- Any change to the existing `StockEntry` ledger. The append-only
  posture is correct for state transitions and stays correct.
- Any change to the cook-bot's current aiogram FSM. v1's multi-step
  cook-bot interactions (forecast, prep, eod-summary) are short-
  horizon enough that the append-only-everything default is not
  actively harmful.
- Any new dependency.

## Description

### Source

- **arXiv ID**: `2608.26263v1`
- **Published**: 2026-08-26 (in-window)
- **Primary category**: cs.CL/AI
- **Title**: "SKILL.state: Scalable Long-Horizon Agent Skills"
- **URL**: https://arxiv.org/abs/2608.26263
- **Raw fetch**: `/tmp/le31-daily-2026-08-28/arxiv/arxiv_append-only%20ledger.xml`

### Verbatim observations from the abstract

The paper diagnoses a specific failure mode of long-horizon agents:

> "Existing agent runtimes maintain execution by continually
> appending observations, actions, and intermediate reasoning
> traces to an ever-growing conversation history, causing latency
> degradation and context-poisoning failures over long horizons."

Its response is to replace the append-only conversation history with
**SKILL.state**, a runtime architecture that uses structured state.

The paper is about agent *skills* — the long-horizon procedural
patterns an agent runs — and the architecture is designed to make
those skills scalable. The data structure trade-off is the load-
bearing contribution.

### Why this matters to LE31

LE31's charter §3.1 mandates append-only for `StockEntry` and other
state-transition ledgers. This is **correct and stays correct**. The
discipline prevents silent state mutation, preserves auditability, and
is the foundation of LE31's competitive differentiation (charter §1).

But the *same discipline*, applied to *chat history* (cook-bot
conversation log, waiter-UI session log), would be **wrong** — and
the paper is exactly the argument why. Append-only chat history
grows without bound, causes latency degradation (every turn reads
more history), and is subject to context-poisoning (earlier bad
turns contaminate later reasoning). The paper's structured-state
response is the right pattern.

The two domains are easy to confuse because they share the data-
structure name ("log of events"). They differ in:
- **what** is being logged (state transitions vs free-form dialogue),
- **why** it is being logged (auditability vs debugging),
- **what** reads it (the system vs future reasoning),
- **how long** it lives (indefinitely for audit vs only as long as
  the session is relevant).

The naive future mistake is to extend LE31's "everything append-only"
posture to chat history because the charter *sounds* like it applies
to all logs. It does not. The paper is the in-window, peer-reviewed
counter-argument. Filing it costs one file; missing it costs a
context-poisoning failure mode in the first multi-turn v2 skill.

### Honest assessment of strength

- **Single source but diagnostically strong.** The paper names the
  failure mode concretely (latency degradation + context-poisoning
  failures over long horizons) and proposes a structured response.
  Confidence is medium for mechanism quality.
- **Domain match is partial.** LE31 is not currently a long-horizon
  agent at the scale the paper targets (multi-day coding sessions).
  LE31's longest single session is a single service shift (~6–10
  hours). The discipline is therefore more relevant for v2 (which
  may add multi-shift continuous operation) than for v1.
- **Counter-argument is non-obvious.** The most likely future
  contributor who proposes a chat-history feature will *not* ask
  "should this be append-only?" — they will default to append-only
  because the charter says so. Having the counter-argument on file
  prevents the default from going unchallenged.
- Confidence: **medium** for mechanism quality, **low-medium** for
  present LE31 urgency, **medium** for the value of the counter-
  argument.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 30 `append-only-audit-redirect` | Audit redirect extension to `StockEntry` | Audit-trail extension; this is the *negative* counterpart for chat |
| 81 `append-only-immutable-audit-check` | Audit-trail primitive | Audit invariant; this argues the same invariant is *wrong* for chat |
| 102 `nightmux-stdlib-telegram-bridge` | stdlib-only Telegram-agent bridge (transport | Transport-layer cross-section; this is data-structure |
| 111 `arxiv-scroll-append-only-event-log-context-arch` | Scroll: append-only Event Log | Same family — structured-state-for-long-horizon |
| 112 `twff-deterministic-process-logging-human-ai-collab` | Deterministic process logging | Logging standard alignment; this is data-structure critique |
| 122 `trace-integrity-cait-acceptance-criterion` | Trace Integrity + CAIT rate | Query-time acceptance; this is storage-time data structure |
| 125 `auditable-continual-learning-measured-transaction-driver-role` | Auditable continual learning | ML weight-edit transactions; this is general chat history |

Ripgrep-clean against features 1–125 by slug and by arXiv ID.

## Data model

**None today.** Zero tables, zero columns, zero rows, zero migrations.

If and when a v2 skill needs long-horizon chat history, the
mechanism would imply (not yet decided, not yet designed):
- a structured skill-state object per active session (not an
  append-only log);
- an explicit eviction policy for stale state entries (not "keep
  everything");
- a checkpoint boundary at each state transition (the *transitions*
  remain append-only per charter §3.1; the *dialogue between*
  transitions is structured-state);
- **no change** to `StockEntry` rows, which are correct as
  append-only.

These are sketches for a future decision, deliberately not specified
here.

## Implementation

1. **No implementation today.** The deliverable is this contract file.
2. **Trigger for the next step**: the first LE31 v2 skill that
   interacts with multi-turn cook-bot or waiter-UI dialogue.
3. **When triggered**:
   - Read the full paper, not just the abstract.
   - Decide whether the skill needs structured state (likely yes
     for long-horizon; likely no for short-horizon).
   - Run `le31-conventions` on the concrete v2 skill — this artifact
     does not pre-authorise anything.
   - **Confirm that the charter §3.1 append-only posture is being
     applied to state transitions, not to chat history.** This is
     the load-bearing check.
4. **If no v2 multi-turn dialogue surface appears**, this artifact
   expires. That is an acceptable outcome.

## Telegram interaction

None today. The discipline, if ever adopted, would affect any v2
cook-bot or waiter-UI skill that interacts with multi-turn dialogue.
But v1's cook-bot interactions are short-horizon and the FSM +
message-history that aiogram provides is sufficient.

## Dependencies

- None today.
- Conceptually related to features 30 / 81 / 102 / 111 / 112 / 122
  / 125 (long-horizon / append-only / structured-state cluster).
  None is a hard prerequisite — this artifact stands alone as a
  reference and a counter-argument.

## Open questions

- Will LE31 v2 ever ship a long-horizon multi-turn surface? If the
  answer is no, this artifact is unnecessary and should expire.
- Does the paper's structured-state approach survive schema
  evolution? **Unknown — the abstract does not say, and the full
  text has not been read.**
- Is the trade-off (append-only auditability vs structured-state
  scalability) sharp or graded? Could a hybrid (append-only
  transitions + structured-state between transitions) work?
  **This is the load-bearing design question; unresolved today.**
- How long is "long horizon" for LE31? A single service shift is
  ~6–10 hours; a multi-shift rolling operation could be ~24 hours
  per day. The paper's targets are multi-day sessions; LE31's likely
  horizons are 1–3 orders of magnitude shorter. **The relevance
  scales with the horizon.**

## Why this matters

LE31 has committed to append-only state transitions, and that
commitment is correct and load-bearing. But the *commitment's
wording* in the charter — "every change is a new entry, never update
or delete" — sounds universal. It is not. Applied to chat history,
it would cause the exact failure mode the paper names: latency
degradation and context-poisoning over long horizons.

The most likely future mistake is the contributor who, when adding
the first multi-turn v2 skill, defaults to "everything append-only"
because the charter says so. They will not ask "should this be
append-only?" because the charter will appear to have already
answered. The paper is the in-window counter-argument.

Filing the observation costs one file. Re-deriving the
counter-argument under contributor pressure — when the default is
already in code and the bug surfaces in production — would cost a
redesign of the chat-history storage layer.

The recommendation is **defer, not build** — and if v2 never ships
a multi-turn dialogue surface, the correct outcome is that this
artifact quietly expires unused.