# Feature 57 — Owner Recap Persona Voice

> **Priority**: P2 · **Effort**: S (≤2 days) · **Source**: brainstorm
> 2026-08-11 (cross-section pick C) · **Bucket**: v2 owner-pains
> **One-line**: a voiced, affect-aware owner daily recap that adds 1–2
> "moments that mattered" in a warm plain-voice layer over the existing
> count-format owner recap (feature 39), grounded in the kama muta /
> chatbot-emotion academic literature.

## Goal

LE31 ships **39-owner-daily-recap-telegram**, an end-of-day push with
counts: covers, voids-with-reasons, top movers, prep adherence.
Numbers-only is honest but flat. The owner (per the most-cited
follow-up question in HMM-40 evidence) actually wants to remember the
**moments** of last night — *the lamb 86ed at 21:30, the birthday
table's focaccia comp, the 4-topping that turned into a 6-topping with
the kids next door*. Today those moments are in the ledger but the
recap skips them.

Cross-section anchors:

- OpenAlex `Warmth in the chest, light in the past: kama muta in
  digital cultural heritage design` (W7172434674) — affect-driven
  design for cultural-heritage UX; transferable to a corner-mart /
  family-kitchen owner recap.
- OpenAlex `Emotion in consumer–chatbot interactions: a systematic
  review` (W7172493963) — empirical SR on emotional tone in chatbot
  UX.
- OpenAlex `Hakka Kitchen: Engagement with Culinary Cultural Heritage
  Through Immersive Game Play` (W7172068431) — culinary cultural
  heritage as a design anchor.

Bound: OpenAlex `Would you rely on an eerie agent? A systematic review
of the uncanny valley effect on trust in human-agent interaction`
(W4417084818) — keep the voice plain. Don't anthropomorphise the bot.
Don't give it a personality name. Don't write in first-person
emotional voice. Keep it as an *owner-facing design choice about
which moments to surface*, not a synthetic persona.

## Scope

**In scope (v2 owner-pains):**

- A new module `backend/app/services/recap_moments.py` (NEW) with one
  function `pick_moments(visited_rows, top_n=2) -> list[Moment]`.
  `Moment` is a small dataclass: `(at, one_liner, evidence_link_ids)`.
  Ranking heuristic (deterministic, no LLM call in v1):
  1. One 86 of a high-revenue item after 20:00 (forced pick).
  2. One comp for a named reason (forced pick).
  3. The remaining `top_n - 2` slots pick from: longest prep skip
     justification, highest-spend single line, largest void batch.
- Extend the existing feature-39 `OwnerRecap` push (in
  `backend/app/services/recap.py`) to call `pick_moments()` and prepend
  a 2-section "moments" block to the markdown before the existing 4
  count sections. The format:
  ```
  🌙 Tonight (2026-08-10)
    • 21:30 — Lamb 86ed after running out (cook-2)
    • 21:55 — Focaccia comp for the birthday table (cook-2)

  (then the existing count sections)
  ```
- A new bot command `/why <recap_moment_index>` — owner-only. Bot
  replies with the per-moment evidence card (delegated to feature 55).
- One new constant `OWNER_RECAP_PERSONA = "plain"` in
  `backend/app/config.py` — at v1 this is fixed; the v2 cut supports
  `OWNER_RECAP_PERSONA in ('plain', 'warm')` with a per-deployment
  choice. `warm` adds a single line of human-feel copy at the top
  ("Today had a few good ones, the regulars were out in force.") and
  **does not** anthropomorphise; the bot remains plain.

**Out of scope (v2 owner-pains):**

- **LLM-generated copy** — the `pick_moments()` function is a
  deterministic heuristic; no LLM call. LLM-summarised moments are a v3
  follow-up.
- **Persona names** — no "Kimi" / "Cashier" / "Sous" etc. Plain voice.
- **Per-owner persona profiles** — one `OWNER_RECAP_PERSONA` per
  deployment, not per owner. v3.
- **Daily streak / engagement metrics** — out.
- **Voice audio versions of the recap** — out; the v3 follow-up could
  ship TTS, but that's not the v1 path.

## Description

The owner receives a feature-39 `OwnerRecap` every evening at 23:30
Europe/Paris. With this feature, the same push gains a small
"moments" preamble in plain voice: the 1-2 things from the evening that
the owner would remember if they were there. The rest of the recap is
unchanged. The moments are picked by a deterministic heuristic from the
existing data — no LLM call, no extra model, just a rank-by-rule
function.

The plain-voice bound is enforced by a style guide in
`backend/app/services/recap_moments.py`:

- No first-person emotional voice (no "we had a great night", no "we
  felt the room").
- No persona name. The bot remains plain text.
- No back-patting or sales-copy language.
- Keep lines ≤12 words.

This is a **capability**, not a blocker: the owner's chat will say
"21:30 — Lamb 86ed after running out (cook-2)", not "oh dear, lamb
ran out at 21:30, what a night".

## Data model

No schema change. Reuses:

- `OwnerRecap` (feature 39) — `body_markdown` is extended at write
  time.
- `VoidRationale` (feature 37/47) — moment source.
- `CookChannel` event log (feature 23) — moment source.
- `PrepTask` (where present; falls back gracefully if absent) —
  moment source.

## Implementation steps

1. Add `backend/app/services/recap_moments.py` (NEW) — implements
   `pick_moments()` per the deterministic heuristic.
2. Add `OWNER_RECAP_PERSONA` to `backend/app/config.py`.
3. Patch `backend/app/services/recap.py` to call `pick_moments()` and
   prepend the moments block to the body markdown (1-line PR).
4. Add `/why <recap_moment_index>` command handler in
   `backend/app/bot/cook_bot_explain.py` (or piggyback on the handler
   added for feature 55).
5. Add `backend/tests/test_recap_moments.py` — deterministic, asserts
   the same input → same output.
6. Update `backend/README.md` with the persona config knob and the new
   `/why` command.

## Telegram interaction if any

- One new owner-only command: `/why <recap_moment_index>` — returns the
  per-moment evidence card. Mirrors feature 55's `/explain`.
- The existing feature-39 push (no separate Telegram interaction) gains
  a moments preamble.

## Dependencies

- **Feature 39** `owner-daily-recap-telegram` — pre-existing.
- **Feature 55** `evidence-review-surface` (cross-section pick A of
  today's brainstorm) — for the `/why` per-moment evidence card.

No new pip dependencies.

## Open questions

- Does the moments block sit *above* the count sections (today) or
  *below* (less prominent)? Recommendation: above — the moments are
  the narrative; counts are the audit.
- Should moments be tappable inline buttons, or are they index-only
  (use `/why <N>` from the reply)? Recommendation: index-only at v1;
  inline buttons are a v3 follow-up.
- `OWNER_RECAP_PERSONA` defaults to `'plain'`; `warm` requires a
  per-deployment config knob. The first deploy picks plain; an opt-in
  second deploy picks warm.

## Why this matters

The owner is the only audience that reads feature 39 every day. The
recap is the LE31 owner's primary surface with the system. Adding
"moments" gives the owner a reason to read every single push — and
gives feature 39 a narrative value beyond counts.

This is the **smallest** of today's three picks in shipping cost
(≤2 days, S effort), but moves the most-read feature to a new tier.
The literature supports it strongly (W7172434674 in particular); the
uncanny-valley bound (W4417084818) keeps it from going off the rails.
