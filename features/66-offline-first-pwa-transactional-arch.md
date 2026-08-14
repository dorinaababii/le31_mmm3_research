# Feature 66 — Offline-First PWA Transactional Architecture (EXPERIMENT)

> **Priority**: P2 · **Effort**: S (≤2 days) · **Source**: brainstorm
> 2026-08-14 (cross-section pick C, **EXPERIMENT**) · **Bucket**:
> **v2 owner-pains (resilience experiment)** — same bucket as
> feature 53 (`zentra-offline-first-fb-pattern`) and feature 49
> (`postledger-tamper-evident-hash`). Distinct from both because
> the new pick is a **design doc + smallest-experiment** artifact,
> not code.
> **One-line**: adopt the **offline-first progressive-web-app
> transactional architecture** design pattern from Nugraha et al.
> (2026-08-10, diamond-OA) as the reference architecture for LE31's
> cook-side and waiter-side operational surfaces, and ship a single
> design doc (`docs/offline-first-architecture.md`) that documents
> the pattern, maps the existing LE31 surfaces to the pattern's
> components, and identifies the **smallest next experiment**.

## Status: EXPERIMENT (today)

This file is **not a build candidate**. It is a **design-doc
experiment**: the slice ships one Markdown file and zero code.
The slice boundary is hard:

1. The doc exists at `docs/offline-first-architecture.md`.
2. The doc maps the existing LE31 surfaces (cook Telegram bot,
   waiter web UI, append-only `StockEntry` ledger, hash-chained
   decision ledger) to the Nugraha et al. pattern's components
   (local cache + sync queue + idempotency keys + reconciliation).
3. The doc identifies the **smallest next experiment** (likely
   transactional idempotency keys for the cook bot photo upload
   flow from feature 65) as a separate future pick, not a
   current slice.

If the experiment validates, a follow-up pick wires the
transactional PWA shape into the cook bot and the waiter web UI.
That follow-up is **not** this slice.

## Goal

The charter invariant §Stock says *every prepared-item quantity
change is a new `StockEntry`*. The charter invariant §State says
*operational transitions are explicit user actions. Do not
silently send, serve, close, or reconcile an order.*

When the network drops during a Friday-night rush, today's
design has only one half: the waiter-side replay queue (feature
53, `zentra-offline-first-fb-pattern`) buffers orders locally on
the waiter's tablet and flushes to the cook bot when the
connection returns. The cook-side surface (Telegram bot on the
cook's mobile data) is **more** resilient than the waiter side
(Telegram runs over the cook's mobile data, not the restaurant's
wifi) but is not designed for offline-first — the cook can still
issue actions that hit the server, and the server's response
comes back over the same mobile data.

Nugraha, Somantri, Rofiqi (2026-08-10). *Implementation of an
Offline-First Progressive Web App Architecture for Transactional
System Resilience.* bit-Tech 9(1):4044. doi:10.32877/bt.v9i1.4044.
Diamond-OA, free to read. **The single strongest academic anchor
for the offline-first operational-surface pattern** in this pass.

The paper documents a four-component pattern:
1. **Local cache** — every operational surface has a local
   write-ahead log that survives network drops.
2. **Sync queue** — the local cache flushes to the server when
   the network returns; the queue is durable across restarts.
3. **Idempotency keys** — every write carries a client-generated
   unique id; the server uses the id to deduplicate retries.
4. **Reconciliation** — when the server's view diverges from the
   local cache (e.g. a cook writes stock and a waiter closes an
   order at the same time), the server emits a reconciliation
   event that the local cache surfaces to the operator.

LE31 today has **partial** implementation: feature 53 ships
the sync queue for the waiter side; the append-only `StockEntry`
ledger (feature 03 + 49) ships the server-side hash chain; the
cook bot (feature 04) ships the cook surface. The Nugraha et al.
pattern is the **unified reference** that ties these together.

The slice ships **zero code**; the slice ships **one design doc**
that maps the existing surfaces to the pattern and identifies
the smallest next experiment. The design doc is **not** a
research paper; it is a 1-page engineering reference that a
future v3 coding agent can read in 5 minutes instead of
rediscovering the pattern from feature 53 alone.

## Scope

**In scope (v2 owner-pains S effort, ≤2 days, EXPERIMENT):**

- New `docs/offline-first-architecture.md` (≤500 words).
  Contents (per the le31-conventions evidence-first pattern):
  1. The Nugraha et al. pattern summary (≤100 words; cite the
     paper + DOI).
  2. The mapping table:
     | Nugraha component | LE31 surface today | Gap |
     |---|---|---|
     | Local cache | feature 53's IndexedDB replay queue (waiter side); absent on cook side | cook side |
     | Sync queue | feature 53's flush-on-reconnect (waiter side); Telegram bot's request/response on cook side | cook-side sync queue |
     | Idempotency keys | absent | **smallest next experiment** |
     | Reconciliation | absent; manual via feature 39 daily-recap | reconciliation event surface |
  3. The smallest next experiment paragraph: identify the
     **transactional idempotency key** as the next concrete
     slice, scoped to the cook bot photo upload flow from
     feature 65 (the natural place where "same photo uploaded
     twice during a network retry" becomes a real-world problem).
- One new entry in `INDEX.md` "Active feature pipeline" table:
  the row for pick 66.
- Zero source files touched; zero migrations; zero new
  config keys.

**Out of scope (v2 EXPERIMENT v1):**

- The actual idempotency-key implementation. That is the
  follow-up pick the doc identifies; not this slice.
- The actual reconciliation event surface. Same.
- The cook-side local cache. Same.
- Multi-device cook-side sync. The cook bot runs on one phone
  today; multi-device is a v3 concern.

## Description

`Nugraha, Somantri, Rofiqi (2026-08-10)` is the **academic
anchor**. The paper documents a production-ready pattern for
**transactional resilience** in offline-first PWA architecture;
the bit-Tech journal is a peer-reviewed venue (ISSN 2622-271X
/ 2622-2728). The diamond-OA status means the paper is free to
read and free to cite; no paywall, no embargo.

The **cross-validation anchors** are:

- `gaganjainse/ClinicLedger` (Kotlin, 1★, 2026-07-15) —
  *offline-first voice-assisted clinic ledger*. Different
  language (Kotlin) and different surface (clinic, not restaurant),
  but the **offline-first + ledger-as-source-of-truth + single
  small business** pattern overlap is tight.
- `Sreenivas-Sadhu-Prabhakara/shelftrack` (HTML PWA, MIT,
  2026-07-15 + 2026-08-14) — *Photo-first stock list for a tiny
  shop. 100% offline, nothing leaves your device.* The PWA
  pattern is the same shape; the LE31 application is the cook
  bot photo upload (feature 65) landing in the existing
  `StockEntry` ledger.
- `studionomadid/Zentra` (Kotlin + Jetpack Compose, carry-over
  from feature 53) — *Offline-first POS app for small F&B
  businesses. Keep selling, even without internet.* Validates
  the offline-first pattern as a 2026 production primitive
  for small-F&B.
- `vul-os/beepbite` (Go + React, 1★, carry-over from feature 42) —
  tags include `offline-first` and `multi-currency`. Corroborates
  the offline-first pattern in a different stack.

The **HN `SquadCue` and `Parley` Show HNs** (carry-over from
2026-08-11/12/13 daily-research) both use Telegram/Slack for
human approval with a local-first data model — direct
corroboration for the LE31 cook bot's existing Telegram surface
as a 2026 pattern.

The **OpenAlex `offline-first-evidence`** query (48 in-window
results) returned the Nugraha paper as the single strongest
academic hit; the other 47 are generic software-engineering
papers with no offline-first transactional architecture content.

## Data model

No new SQLModel table. No Alembic migration. The artefact is a
single Markdown design doc.

```
docs/
├── offline-first-architecture.md        # NEW (this slice)
```

The doc is data, not code; it lives in the existing `docs/`
directory and follows the same Markdown conventions as
`HANDOFF.md` and `PROJECT_CHARTER.md`.

## Implementation steps

1. Create `docs/offline-first-architecture.md` (≤500 words)
   with the three sections above (pattern summary + mapping
   table + smallest next experiment paragraph).
2. Add one row to `INDEX.md` "Active feature pipeline" table
   for pick 66 (date, pick, bucket, feature path, Linear ID,
   handoff).
3. Validate: run `wc -w docs/offline-first-architecture.md`
   — the doc must be ≤500 words.
4. No tests; no migrations; no config changes.

## Telegram interaction if any

None in this slice. The doc is documentation; no operational
surface changes.

## Dependencies

- **Feature 03** (`kitchen-stock-tracker`) — the `StockEntry`
  ledger that the pattern maps to.
- **Feature 04** (`menu-photo-bot`) — the cook Telegram bot
  surface that the pattern maps to.
- **Feature 49** (`postledger-tamper-evident-hash`) — the
  hash-chained audit trail that the pattern maps to.
- **Feature 53** (`zentra-offline-first-fb-pattern`) — the
  waiter-side replay queue that the pattern composes with.
- **Feature 65** (`cook-photo-stock-list-pwa`) — the cook-side
  photo upload flow that the smallest-next-experiment paragraph
  identifies as the natural place to ship transactional
  idempotency keys.
- **No new pip dependency**.

## Open questions

- Is the Nugraha et al. paper's pattern production-ready for
  LE31's scale (single small restaurant, ≤50 covers/night)?
  Recommendation: yes for the pattern's *components* (local
  cache + sync queue + idempotency keys + reconciliation);
  the implementation can be lightweight and ship in
  feature-sized slices.
- Should the design doc live in `docs/` or in
  `research/`? Recommendation: `docs/` (engineering reference,
  not research). Revisit if the doc grows past 500 words.
- Should the smallest-next-experiment paragraph name a
  specific feature pick? Recommendation: yes, name the
  idempotency-key slice scoped to feature 65's cook bot
  photo upload flow; that gives the future v3 coding agent
  a concrete starting point.

## Why this matters

The charter invariant §Stock says *every prepared-item quantity
change is a new `StockEntry`*. The charter invariant §State says
*operational transitions are explicit user actions. Do not
silently send, serve, close, or reconcile an order.*

When the network drops during a Friday-night rush, the cook and
waiter want the operational surface to keep a coherent local view
that reconciles when the network returns. Today's design has
only one half (waiter-side replay, feature 53) and no documented
pattern reference for the cook side.

The Nugraha et al. paper is a **vetted academic reference** for
exactly the pattern LE31 needs. The diamond-OA status means the
paper is free to read and free to cite; the bit-Tech journal
peer-review process means the pattern is not a 2026 fad but a
peer-reviewed contribution to the software-engineering literature.

The slice ships **zero code**; the slice ships **one design doc**
that gives LE31 a documented pattern reference for the offline-first
operational-surface design. A future v3 coding agent can read one
doc and one paper instead of rediscovering the pattern from
feature 53 alone.

This is an **experiment**, not a build. The slice boundary is
hard: one Markdown file + one INDEX.md row. If the experiment
validates, a follow-up pick wires the transactional idempotency
key into the cook bot photo upload flow from feature 65.

## Evidence (recorded)

- **Academic anchor 1**: Nugraha, Somantri, Rofiqi
  (2026-08-10). *Implementation of an Offline-First Progressive
  Web App Architecture for Transactional System Resilience.*
  bit-Tech 9(1):4044. doi:10.32877/bt.v9i1.4044. Diamond-OA,
  free to read. Read at
  `/tmp/le31-brainstorm-2026-08-14/oa_offline_first_evidence.json`.
- **Cross-section anchor 2**: `gaganjainse/ClinicLedger`
  (Kotlin, 1★, 2026-07-15). *Offline-first voice-assisted
  clinic ledger for Indian practitioners.* Read at
  `/tmp/le31-brainstorm-2026-08-14/gh_topic_local_first.json` +
  `gh_topic_offline_first.json`.
- **Cross-section anchor 3**: `Sreenivas-Sadhu-Prabhakara/shelftrack`
  (HTML PWA, MIT, 2026-07-15 + 2026-08-14). *Photo-first stock
  list for a tiny shop. 100% offline, nothing leaves your device.*
  Read at `/tmp/le31-brainstorm-2026-08-14/gh_topic_small_business.json`.
- **Carry-over anchor**: `studionomadid/Zentra` (Kotlin + Compose,
  feature 53 anchor). Read at
  `/tmp/le31-brainstorm-2026-08-14/gh_topic_offline_first.json`.
- **Carry-over anchor**: HN Show HN `SquadCue` (1pt, 2026-08-11)
  + `Parley` (9pt, 2026-08-11). Telegram/Slack-as-approval-channel
  pattern. Read at
  `/tmp/le31-brainstorm-2026-08-14/hn_offline-first-pos.json`.
- **In-repo dependency**: features 03 + 04 + 49 + 53 + 65; the
  pattern composes them into a unified reference.
