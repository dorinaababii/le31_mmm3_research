# Feature 59 — Recap Replay Evidence Card

> **Priority**: P2 · **Effort**: S (≤2 days) · **Source**: brainstorm
> 2026-08-12 (cross-section pick B) · **Bucket**: v2 owner-pains.
> **One-line**: a replay + diff + evidence-card layer over
> `39-owner-daily-recap-telegram` — the owner sees a 1-line diff vs
> yesterday on each section and can tap any number to see the exact
> `StockEntry` / `VoidRationale` row, *without* an LLM call.

## Goal

LE31 ships `39-owner-daily-recap-telegram` and is shipping
`57-owner-recap-persona-voice` (today's "moments that mattered"
preamble). Both add *content* to the nightly recap push. This pick
adds the *replay* half instead — the owner can re-open any past recap,
see what changed since last time, and tap a single line to land on the
exact existing ledger row.

The look is:

```
🌙 Tonight (2026-08-12) compared to 2026-08-11
  Covers:       42  (was 38, +4)
  Voids:         3  (was 5, −2)
  Top mover:   lamb ragu  (was osso buco, swap)
  Prep on-time: 11/12    (was 10/12, +1)
  Stockouts:    lamb (21:30)
  ↳ 1. /why 1  ▸ lamb 86ed after running out  ▸ tap=StockEntry #10351
  ↳ 2. /why 2  ▸ focaccia comp for the birthday table  ▸ tap=VoidRationale #392
```

Each numbered line has a one-tap `/why <n>` reply that returns the
matching evidence card — a deterministic projection of one or two rows
from the existing append-only ledger. No model call. No LLM copy. The
moments block in feature 57 (warm persona) is *opt-in* and only
appears if the deployment sets `OWNER_RECAP_PERSONA='warm'`. The
replay block is *always on*.

## Scope

**In scope (v2 owner-pains, S effort):**

- A new module `backend/app/services/recap_replay.py` (NEW) with
  three pure functions:
  - `diff_sections(today: OwnerRecap, yesterday: OwnerRecap) ->
    list[DiffRow]` — one row per section, with `was=X, is=Y, delta=Z`.
  - `pick_moment_targets(today: OwnerRecap) -> list[MomentTarget]`
    — numeric-indexed targets for the owner (1..N), each
    pointing at one StockEntry/VoidRationale row id.
  - `evidence_card(target: MomentTarget) -> str` — the markdown
    evidence card body. Pure projection, no LLM.
- Extend `backend/app/services/recap.py` (where feature 39 + 57 live)
  to call `diff_sections()` and `pick_moment_targets()`, then prepend
  the diff line + the moment list to the existing body. ≤15 lines of
  PR.
- One new owner-only Telegram command: `/why <recap_moment_index>`
  (same handler spec as feature 57; falls back to feature 55
  `evidence-review-surface` if feature 57 not yet shipped).
- `backend/tests/test_recap_replay.py` (NEW) — deterministic,
  asserts same input → same output across 3 fixtures.
- `backend/README.md` — note the new `/why <N>` alias and that the
  replay block is always-on (no persona config).

**Out of scope (v2 owner-pains):**

- **LLM copy.** Deterministic, period. LLM-summarised replays are
  explicitly out of scope for this slice and are a v3 follow-up.
- **Persona / warm voice.** Feature 57 owns that; this slice is its
  *companion*, not its replacement.
- **Multi-day replays.** v1 is yesterday ↔ today; multi-day is a v3
  follow-up (`/replay <N>`).
- **Operator-side ledger search.** `/why` is index-keyed only at
  v1; full-text search is feature 55 (already shipped).

## Description

`Lulzx/memo` (1★, pushed 2026-07-27, Python) is the cleanest
external anchor — *"Permanent memory for agents. One log file, one
projection, 150 lines of Python."* The LE31 version of this is:
*one append-only ledger, one projection, ≤200 lines of Python.* The
existing `StockEntry` + `VoidRationale` + `AuditLog` tables are the
log; the recap body is the projection; this slice adds the *diff
projection* and the *moment targets*.

`RobbieRao/hci-paper-writing` (3★, pushed 2026-08-12, *traces claims
to evidence before red-teaming*) provides the HCI evidence-card
pattern in research-paper shape — but the actual UX is just one
inline `/why <N>` reply.

The OpenAlex `kama muta` (W7172434674, 2026-08-03) and `chatbot
emotion SR` (W7172493963, 2026-08-05) literature supports the *moments
that mattered* surface; this slice uses the literature to bound the
moment list (≤3 per recap, deterministic) without anthropomorphising
the bot.

## Data model

No schema change. Reuses:

- `OwnerRecap` (feature 39) — `body_markdown` is extended at write
  time by `diff_sections()` and `pick_moment_targets()`.
- `StockEntry` — moment target source.
- `VoidRationale` (features 37/47) — moment target source.
- `OwnerRecap.previous_id` (NEW reference, no migration) — to look
  up the previous recap on write. Implementation note: this is a
  computed column (last `OwnerRecap` row before this one), not a
  real FK. Stored as a JSON field on the markdown extension if
  needed.

## Implementation steps

1. Add `backend/app/services/recap_replay.py` (NEW) —
   `diff_sections`, `pick_moment_targets`, `evidence_card`. ≤200
   lines.
2. Extend `backend/app/services/recap.py` to call them
   (≤15-line PR).
3. Add the `/why <recap_moment_index>` handler in
   `backend/app/bot/cook_bot.py` (1 line, behind
   `OWNER_RECAP_REPLAY_ENABLED=1` flag, default OFF in v1; flip
   ON once owner has approved one fixture push).
4. Add `backend/tests/test_recap_replay.py` (3 fixtures).
5. Update `backend/README.md`.

## Telegram interaction if any

- New owner-only command: `/why <recap_moment_index>` — returns
  the evidence card body for that numbered target.
- Existing recap push (no separate Telegram interaction) gains the
  diff line and the numbered moment list *prepended* to the body.

No new buttons, no new flows. The `/why` reply keys into the existing
recap body markdown — same UX pattern as feature 55's `/explain` and
feature 57's `/why`.

## Dependencies

- **Feature 39** `owner-daily-recap-telegram` — pre-existing.
- **Feature 55** `evidence-review-surface` (cross-section pick A
  of 2026-08-11) — for the `/why` evidence-card shape (delegation
  target).
- **Feature 57** `owner-recap-persona-voice` (cross-section pick C
  of 2026-08-11) — *companion*, not a dependency. If 57 ships
  first, the recaps gain the warm preamble; this slice adds the
  replay block. If this slice ships first, the recaps gain replay
  only.

No new pip dependencies. No schema change.

## Why this matters

This is the smallest of today's three picks in shipping cost (S
effort, ≤2 days) and the cheapest in *user-visible* cost — the owner
sees a diff and a tap-to-row, no new flow. The literature supports
it (Lulzx/memo, RobbieRao/hci-paper-writing, OpenAlex W7172434674).

It is also the *easiest* one to roll back: feature flag the diff
block, ship ON, ship OFF in a single env-set.

## Open questions

- Diff granularity: today's `was / is / delta` is per section. Should
  it also be per *top-mover* item? Recommendation: per section at v1,
  per item in v3.
- Bound `pick_moment_targets` to 3? Recommendation: yes, ≤3 per
  recap (deterministic).
- Should this slice ship *before* or *after* feature 57? Recommendation:
  after — feature 57 sets the style guide; this slice respects it.

## Evidence (recorded)

- **Cross-section anchor 1**: `Lulzx/memo` (1★, pushed 2026-07-27,
  Python, MIT). Read at
  `/tmp/le31-brainstorm-2026-08-12/gh_topic_append-only.json`.
- **Cross-section anchor 2**: `RobbieRao/hci-paper-writing` (3★,
  pushed 2026-08-12, Python).
- **Cross-section anchor 3**: `ahmadAlMezaal/ledger` (0★, pushed
  2026-07-21, Python, MIT) — domain-agnostic append-only event store
  on plain PostgreSQL.
- **Literature anchor**: OpenAlex `Warmth in the chest, light in
  the past: kama muta in the design of digital cultural heritage`
  (W7172434674, 2026-08-03).
- **Literature bound**: OpenAlex `Would you rely on an eerie agent?
  A systematic review of the impact of the uncanny valley effect on
  trust in human-agent interaction` (W4417084818, 2026-07-22).

## Distinct from existing features

- **vs. feature 39** (`owner-daily-recap-telegram`): 39 is the count
  recap. This is the replay/diff/replay-tap layer on top of 39.
- **vs. feature 57** (`owner-recap-persona-voice`): 57 adds the warm
  preamble moments block with deterministic picking. This slice adds
  the diff block and the `/why <N>` evidence-card reply. They are
  complementary, not duplicates.
- **vs. feature 55** (`evidence-review-surface`): 55 is the general
  audit surface. This slice delegates to 55 for the actual evidence
  card body (or ships a tiny inline body if 55 hasn't shipped yet).
- **vs. feature 47** (`decision-rationale-mixin`): 47 is the
  per-decision rationale. This slice uses 47's `VoidRationale` table
  for void moments, but does not modify the rationale schema.
