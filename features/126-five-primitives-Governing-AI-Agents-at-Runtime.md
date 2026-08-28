# Feature 126 — Five Primitives for Governing Autonomous AI Agents at Runtime

> **NEW observation (2026-08-28).** Documents in-window arXiv paper
> `2608.26696v1` "Five Primitives for Governing Autonomous AI Agents at
> Runtime" (2026-08-27, cs.MA) from the 2026-08-28 daily research pass.
> Bucket: **v2 owner-pains (governance-primitive reference)** — watch-
> list defer. Zero build time today.

## Goal

Retain the **five-runtime-governance-primitives** framing as a design
constraint for the first LE31 v2 surface that records a non-staff
actor (a guest, a delivery driver, an automated booking source). The
paper answers: *what control primitives does a system need when the
actors are ephemeral, model-selected, and discovered rather than
enrolled?* LE31 v1 does not need this — its only actors are the cook
and manager, both long-lived, both statically allowlisted. The artifact
exists so the answer is on file before the question is asked.

## Scope

**In scope:**
- This contract file as the durable record of the mechanism.
- One INDEX.md row in the active-feature-pipeline table.
- A bounded read of the full paper (not just the abstract) **at the
  point when** a v2 feature first proposes a non-staff actor surface.

**Out of scope (v1 and today):**
- Any code. No primitive implementation, no middleware, no schema
  change, no migration.
- Any change to the existing chat-id allowlist for staff. v1 actors
  are static and the allowlist is appropriate for them.
- Any change to the v1 privacy boundary. Charter §3.2 keeps v1 guest
  demographics as counts, not identity or contact data — that decision
  stands and this feature does not reopen it.
- Any new dependency.

## Description

### Source

- **arXiv ID**: `2608.26696v1`
- **Published**: 2026-08-27 (in-window)
- **Primary category**: cs.MA
- **Title**: "Five Primitives for Governing Autonomous AI Agents at Runtime"
- **URL**: https://arxiv.org/abs/2608.26696
- **Raw fetch**: `/tmp/le31-daily-2026-08-28/arxiv/arxiv_append-only%20ledger.xml`

### Verbatim observations from the abstract

The paper diagnoses that enterprise deployments of autonomous AI
agents inherit a control model built for human users and long-lived
services, and the fit fails in three specific ways:

> "agent principals are ephemeral, appearing and vanishing faster
> than provisioning; their actions are selected by a model rather
> than programmed, so the set of things they may attempt is not
> known in advance; and the population is discovered" rather than
> enrolled.

The paper proposes five runtime governance primitives as the response
to these three failure modes.

### Why this matters to LE31

LE31's charter §3.1 makes every operational transition an *explicit
user action* — "do not silently send, serve, close, or reconcile an
order." In v1 the actors that can perform these actions are the cook
and the manager, both long-lived, both enrolled via the chat-id
allowlist, and both with model-fixed action sets (cook: set up menu,
mark sold-out, request leftover, view forecast; manager: view reports,
close shift). v1 therefore does **not** hit any of the three failure
modes the paper names.

The moment v2 records a non-staff actor — a guest placing an order
via a Telegram Mini App, a delivery driver confirming pickup, an
automated booking source — LE31 inherits all three failure modes at
once. The non-staff actor is ephemeral (the booking might last one
evening), model-selected (an LLM-issued booking might pick actions the
system has never seen), and discovered (the system didn't enroll
them; they appeared via a Telegram Mini App deep link).

The naive response is to extend the chat-id allowlist pattern to
cover these new actors. That is exactly the failure mode the paper
names: allowlists are for *long-lived enrolled principals* and break
for *ephemeral discovered principals*. Without the primitives, the
v2 surface would either (a) leak control to unknown actors, or (b)
require explicit per-actor enrollment, which is operationally
untenable for a single small restaurant.

### Honest assessment of strength

- **Single source.** One paper, no independent implementation
  reviewed, no second in-window source corroborating the primitives.
- **No LE31 pain observed.** v1 has no non-staff actor surface, and
  no owner has reported a governance problem. The need is **inferred
  from the v2 direction**, not reported.
- **Mapping is non-trivial.** The paper's five primitives are framed
  for *autonomous AI agents at enterprise scale*; LE31's setting is a
  single small restaurant with two human roles. Most of the five will
  be no-ops at LE31's scale; only a subset (probably action class,
  declared actor, decision reason) will translate cleanly.
- Confidence: **medium** for mechanism quality, **low** for present
  LE31 urgency.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 23 `sse-cook-channel` | SSE cook-channel surface | Cook is a staff actor; allowlist pattern is correct |
| 41 `telegram-msg-stock-update` | Cook updates stock via Telegram message | Staff actor; allowlist pattern is correct |
| 49 `audit-trail-cook-action-reason` | Cook records rationale on `StockEntry` | Staff actor; allowlist pattern is correct |
| 81 `append-only-immutable-audit-check` | Audit-trail primitive | Records what was done; this paper is about *who may do what* |
| 90 `pronto-cafe-telegram-reminders-cross-section` | WhatsApp+Telegram reminder cross-section | Cook-side, not guest-side |
| 104 `aldia-ai-agent-business-engine-cross-section` | AI-agent open-business engine | Adjacent — same failure-mode family but inverse-validation of charter §3.4 |

Ripgrep-clean against features 1–125 by slug and by arXiv ID.

## Data model

**None today.** Zero tables, zero columns, zero rows, zero migrations.

If and when a v2 feature records a non-staff actor, the mechanism
would imply (not yet decided, not yet designed):
- a runtime decision point at every state-touching entry, returning
  a primitive-shaped verdict;
- an audit trail of the decision reasons (charter §3.1 already
  requires explicit transitions; the primitives add structure to
  *why* the transition was allowed);
- **no change** to existing v1 staff allowlist, which works correctly
  for static long-lived actors.

These are sketches for a future decision, deliberately not specified
here.

## Implementation

1. **No implementation today.** The deliverable is this contract file.
2. **Trigger for the next step**: the first LE31 v2 feature proposal
   that records a non-staff actor (a guest placing an order via
   Telegram Mini App, a delivery driver confirming pickup, an
   automated booking source, or similar).
3. **When triggered**:
   - Read the full paper, not just the abstract.
   - Decide whether LE31 needs *any* of the five primitives, or
     whether the simpler answer is to keep v2 actors staff-only
     (e.g. the cook keys in the booking on the guest's behalf).
     **Keeping v2 actors staff-only is usually the better answer and
     should be the default.**
   - If primitives are warranted, run `le31-conventions` again on the
     concrete v2 feature — this artifact does not pre-authorise
     anything.
4. **If no v2 non-staff actor surface appears**, this artifact
   expires. That is an acceptable outcome.

## Telegram interaction

None today. The primitives, if ever adopted, would affect any v2 surface
that records a non-staff actor — and a Telegram Mini App would be the
most likely surface per the current threat model — but the cook-bot
itself is staff-only and unchanged.

## Dependencies

- None today.
- Conceptually related to features 49 / 81 / 30 (audit-trail cluster)
  and feature 104 (AI-agent cross-section). None is a hard
  prerequisite — this artifact stands alone as a reference.

## Open questions

- Will LE31 v2 ever record a non-staff actor? If the answer is no,
  this artifact is unnecessary and should expire.
- Which subset of the paper's five primitives survives the mapping
  to a single small restaurant? **The full set is over-engineered
  for LE31's setting; the question is which 1–2 primitives carry
  any weight.** Unknown — requires the full paper.
- Does LE31's existing charter §3.1 explicit-transition posture
  already cover the operational side of governance? Likely
  partially — but the paper's framing is about *who may do what*,
  which §3.1 only implicitly addresses.
- Does LE31's chat-id allowlist work correctly for the (current)
  staff-only actors? Yes, and there is no plan to change it.

## Why this matters

LE31 has committed to explicit operational transitions and a static
staff allowlist. Those commitments are correct for v1's setting. The
moment v2 introduces a non-staff actor, the commitments are no longer
sufficient on their own — they cover *what* happens, but not *who is
allowed to cause it*. The paper describes the governance primitives
that fill the *who* gap, with dated primary-source provenance.

Filing the observation costs one file. Re-deriving it later, after the
first non-staff actor has shipped with the wrong primitives, would
cost a security review and likely a redesign — and the redesign would
be more expensive than getting it right at the moment of first use.

The recommendation is **defer, not build** — and if v2 never records
a non-staff actor, the correct outcome is that this artifact quietly
expires unused.