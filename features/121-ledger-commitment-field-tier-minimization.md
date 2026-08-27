# Feature 121 — Ledger commitment with field-tier minimization

> **NEW observation (2026-08-27).** Documents in-window arXiv paper
> `2608.25474v1` "Separating Disclosure from Authorization: Field-Tier
> Minimization for Agent Action Mediation" (2026-08-26, cs.CR) from the
> 2026-08-27 daily research pass. The paper describes a mechanism for
> evolving privacy minimization over an append-only ledger **without
> invalidating history** — a concrete answer to a real LE31 v2 problem.
> Bucket: **v2 owner-pains (architecture reference)** — watch-list
> defer. Zero build time today.
>
> **This is a reference artifact, not a build request.** Nothing in
> LE31 v1 needs it, because v1 stores only counts.

## Goal

Retain the **ledger-commitment-before-minimization** mechanism as a
design constraint for the first LE31 v2 surface that records an
identifying field. The mechanism answers: *how do you change what an
append-only ledger discloses, later, without rewriting or invalidating
entries it already committed?*

The artifact is the persistent design reference. No code today.

## Scope

**In scope:**
- This contract file as the durable record of the mechanism and its
  source.
- One INDEX.md row in the active-feature-pipeline table.
- A bounded read of the full paper (not just the abstract) **at the
  point when** a v2 feature first proposes recording an identifying
  field.

**Out of scope (v1 and today):**
- Any code. No canonical-digest implementation, no tier table, no
  schema change, no migration.
- Any change to the existing `StockEntry` ledger. v1 records prepared-
  item quantity changes, which carry no identifying fields.
- Any change to the v1 privacy boundary. Charter §3.2 keeps v1 guest
  demographics as counts, not identity or contact data — that decision
  stands and this feature does not reopen it.
- Any new dependency.

## Description

### Source

- **arXiv ID**: `2608.25474v1`
- **Published**: 2026-08-26 (in-window)
- **Primary category**: cs.CR
- **Title**: "Separating Disclosure from Authorization: Field-Tier
  Minimization for Agent Action Mediation"
- **URL**: https://arxiv.org/abs/2608.25474
- **Raw fetch**: `/tmp/le31-daily-2026-08-27/arxiv/arxiv_append-only_ledger.xml`

### Verbatim observations from the abstract

The paper opens by naming the exact tension an audited append-only
ledger lives with:

> "A system that authorizes an action must see enough of it to decide,
> and a system that attests to its decision must record enough to be
> audited. Both pressures push raw action parameters — recipients,
> payment memos, record identifiers — into an append-only ledger that
> cannot delete them."

Its mechanism classifies **each parameter field**, not each action
class, into three tiers: fields a policy may legitimately match on
(cross raw); fields that are policy-relevant but identifying (cross
only as projections, e.g. an email domain or a templated route shape);
and fields with no legitimate policy use (never leave the workload).

The load-bearing property:

> "the ledger's commitment is a canonical digest of the full,
> unminimized parameters, computed **before** minimization runs. The
> commitment is therefore independent of the tier table: reclassifying
> a field changes what is disclosed without invalidating a historical
> entry, reopening a hash, or altering what an offline verifier
> checks."

The paper also generates the tier table, policy schema, and wire schema
from **one per-action declaration**, so the deciding party and the
recording party cannot hold different rules.

### Why this matters to LE31

LE31's charter §3.1 makes the `StockEntry` ledger append-only: every
prepared-item quantity change is a new entry, entries are never updated
or deleted, and current stock is derived. Charter §3.2 keeps v1 data
minimal — guest demographics are counts, not identity.

Those two rules are comfortable together **only while LE31 records
nothing identifying**. The moment a v2 surface records a supplier
contact, a staff identifier, or a delivery detail, LE31 inherits the
paper's tension: the ledger cannot delete what it recorded, but the
privacy posture may need to change later.

The naive resolutions are both bad:

1. **Mutate or purge historical entries** to reflect a new privacy
   rule — directly violates charter §3.1 and destroys auditability.
2. **Freeze the privacy posture forever** at whatever was decided when
   the first identifying field shipped — makes the ledger a permanent
   hostage to an early guess.

The paper's construction avoids both: commit a canonical digest of the
*full* parameters before minimization, so the commitment is stable
while the disclosure policy is free to change. Reclassifying a field
later changes what is *shown*, not what was *committed*, and an offline
verifier is unaffected.

**This is worth having written down before it is needed**, because the
decision it constrains (what to commit, and when, relative to
minimization) is made at the moment the first identifying field is
added — and is expensive to reverse afterwards.

### Honest assessment of strength

- **Single source.** One paper, no independent implementation
  reviewed, no second in-window source corroborating it.
- **No LE31 pain observed.** No owner has reported a privacy-
  minimization problem, because v1 has no identifying fields. The
  need is **inferred from the v2 direction**, not reported.
- **The hard part is canonicalisation.** Producing a stable byte
  representation of a record across schema evolution is where such
  schemes usually fail in practice. The paper's abstract does not
  resolve this; the full text would need reading before any
  implementation.
- Confidence: **medium** for mechanism quality, **low** for present
  LE31 urgency.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 111 `arxiv-scroll-append-only-event-log-context-arch` | arXiv Scroll: append-only Event Log + eviction index | Scroll is about *retrieval* over an event log; this is about *privacy minimization* over a committed ledger |
| 108 `telegram-chat-history-fuzzy-search-stockentry-audit` | Telegram fuzzy-search indexing for audit trail | Search/indexing surface; not commitment or minimization |
| 112 `twff-deterministic-process-logging-human-ai-collab` | open-standard deterministic process logging | Logging standard alignment; no field-tier or digest mechanism |
| 118 `textile-erp-whatsapp-conversation-first-audit-erp` | ERP mirroring charter §3.1 phrasing | Charter validation; no minimization mechanism |
| 49 / 81 / 30 (audit-trail cluster) | LE31 audit-trail primitives | This constrains *how* those primitives commit data if identifying fields are ever added |

Ripgrep-clean against features 1–120 by slug and by arXiv ID.

## Data model

**None today.** Zero tables, zero columns, zero rows, zero migrations.

If and when a v2 feature records an identifying field, the mechanism
would imply (not yet decided, not yet designed):

- a commitment column on the relevant ledger row, holding a canonical
  digest of the full pre-minimization parameters;
- a tier declaration per recorded action, generated from one source so
  policy and wire schema cannot diverge;
- **no change** to existing `StockEntry` rows, which carry no
  identifying fields and therefore need no minimization.

These are sketches for a future decision, deliberately not specified
here.

## Implementation

1. **No implementation today.** The deliverable is this contract file.
2. **Trigger for the next step**: the first LE31 v2 feature proposal
   that records an identifying field (supplier contact, staff
   identifier, delivery detail, or similar).
3. **When triggered:**
   - Read the full paper, not just the abstract, with specific
     attention to how it canonicalises parameters across schema
     change.
   - Decide whether LE31 needs a commitment digest at all, or whether
     not recording the identifying field is the cheaper answer. **Not
     recording it is usually the better answer and should be the
     default.**
   - If a commitment is warranted, run `le31-conventions` again on the
     concrete v2 feature — this artifact does not pre-authorise
     anything.
4. **If no v2 identifying-field surface appears**, this artifact
   expires. That is an acceptable outcome.

## Telegram interaction

None. No cook-bot or waiter-UI surface is touched. The mechanism, if
ever adopted, is invisible to operators by design.

## Dependencies

- None today.
- Conceptually related to features 30 / 49 / 81 (audit-trail cluster)
  and 111 (append-only event log). None is a hard prerequisite —
  this artifact stands alone as a reference.

## Open questions

- Will LE31 v2 ever record an identifying field? If the answer is no,
  this artifact is unnecessary and should expire.
- Does the paper's canonicalisation approach survive schema evolution
  in a SQLModel/Postgres setting? **Unknown — the abstract does not
  say, and the full text has not been read.** This is the main
  technical risk.
- Is a commitment digest even proportionate for a single small
  restaurant? A hash-committed ledger with an offline verifier may be
  heavier than the setting warrants; the alternative (record less) is
  simpler and aligns with charter §3.2.
- Who would ever run the offline verifier? For LE31 there is no
  adversarial auditor — the owner is the only stakeholder. This
  weakens the case for the full construction and should be resolved
  before any implementation.

## Why this matters

LE31 has already committed to an append-only ledger. That decision is
right, and features 30 / 49 / 81 / 108 / 111 / 112 / 118 show it is
being independently validated from several directions. But an
append-only ledger has one genuinely hard consequence that LE31 has not
yet had to face: **it cannot forget.** While v1 records only counts,
this costs nothing. The first time v2 records something identifying,
the privacy posture becomes permanent unless the commitment was
designed to be independent of the disclosure policy.

This paper describes exactly that separation, with dated primary-source
provenance. Filing it costs one file. Re-deriving it later, after the
first identifying field has already shipped with the wrong commitment
design, would cost a migration over a ledger that by charter cannot be
rewritten.

The recommendation is **defer, not build** — and if v2 never records an
identifying field, the correct outcome is that this artifact quietly
expires unused.
