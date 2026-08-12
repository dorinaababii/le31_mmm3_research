# recap-replay-evidence-card — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/59-recap-replay-evidence-card.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `59`
- Slug: `recap-replay-evidence-card`
- Contract file: `features/59-recap-replay-evidence-card.md`
- Bucket: v2 owner-pains (S effort — feature 39 extension)
- Linear parent: HMM-66 (Brainstorm 2026-08-12 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (4 in-source anchors today: `Lulzx/memo` pushed
2026-07-27; `RobbieRao/hci-paper-writing` pushed 2026-08-12;
`ahmadAlMezaal/ledger` pushed 2026-07-21; OpenAlex W7172434674 +
W7172493963 in-window). Confidence: **high**.

**Decision: build (v2 owner-pains, S effort, ≤2 days).** No failed
checks. The slice is deterministic, reuses existing tables, has no
LLM call, and respects the style guide of feature 57.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; the slicing discipline inherits even at v2 owner-pains).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract
   back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/services/recap_replay.py             # NEW: diff_sections(), pick_moment_targets(), evidence_card() — ≤200 lines
backend/app/services/recap.py                    # EDIT: call the three new functions in build_daily_recap(); ≤15-line PR
backend/app/bot/cook_bot.py                      # EDIT: register /why <recap_moment_index> handler (1 line, behind OWNER_RECAP_REPLAY_ENABLED flag)
backend/tests/test_recap_replay.py               # NEW: 3 deterministic fixtures
backend/README.md                                # note the persona config knob + the new /why command
```

No new pip dependencies. No new SQLModel tables. No new Alembic
migration. The `OwnerRecap.body_markdown` field is extended **at
write time** by the slice's projection.

## Endpoints and contracts added

No new HTTP routes. No new SQLModel tables. No new Alembic migration.
The `OwnerRecap.body_markdown` field (from feature 39) is **extended
at write time** — the existing column is unchanged.

The extension looks like:

```
🌙 Tonight (2026-08-12) compared to 2026-08-11
  Covers:       42  (was 38, +4)
  Voids:         3  (was 5, −2)
  Top mover:   lamb ragu  (was osso buco, swap)
  Prep on-time: 11/12    (was 10/12, +1)
  Stockouts:    lamb (21:30)
  ↳ 1. /why 1  ▸ lamb 86ed after running out  ▸ tap=StockEntry #10351
  ↳ 2. /why 2  ▸ focaccia comp for the birthday table  ▸ tap=VoidRationale #392

(existing 4-section body unchanged)
```

The block is **always-on** at v1. There is **no** `OWNER_RECAP_REPLAY`
persona config (in contrast to feature 57's `OWNER_RECAP_PERSONA`).
The replay is not a voice choice; it is a deterministic projection.

## Endpoints and bot commands added

One new owner-only Telegram command on the existing `cook_bot.py`:

- `/why <recap_moment_index>` — returns the per-moment evidence card,
  delegating to feature 55's `EvidenceLink` table. Falls back to an
  inline body if feature 55 hasn't shipped yet. Falls back to
  *"No moment <N> in recap <R>"* if the index is out of range.

The handler is registered behind `OWNER_RECAP_REPLAY_ENABLED=1`
(default OFF in the first deploy; flip ON once the owner has
approved one fixture push).

## Style guide (enforced by code review)

The `diff_sections()`, `pick_moment_targets()`, and `evidence_card()`
functions and the diff block adhere strictly to the style guide of
feature 57 plus an extra no-voice rule:

- No first-person voice (no "we had a great night").
- No persona name. The bot remains plain text.
- No anthropomorphising ("the kitchen felt busy").
- No warm voice. The replay block is plain, even when
  `OWNER_RECAP_PERSONA='warm'` is set on feature 57.
- Each numbered line ≤12 words.
- The delta line (`(was X, is Y, delta Z)`) is the only voice the
  replay block uses — neutral, factual.

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent MUST:

1. Unit-test `diff_sections()` deterministically: same input →
   same output across 3 fixtures (no-change, single-section change,
   multi-section change).
2. Unit-test `pick_moment_targets()` deterministically: same input
   → same output (3 fixtures, each producing 0..3 targets).
3. Unit-test `evidence_card()` deterministically: every target must
   produce a one-line body that fits ≤80 chars and ends with the
   stock/void/audit id.
4. Bot test: `/why 1` returns the expected card for a fixture row;
   `/why 0` returns the "No moment 0" fallback; `/why` with no
   index returns a one-line usage.
5. Style-guide test: assert no first-person voice, no persona
   names, line-length cap respected, no warm copy.
6. Integration test: ship one fixture push, assert the recap
   contains both the diff block and the existing 4-section body
   in correct order.

After implementation, run the parent's verify-before-fixing protocol
on the slice branch.

## Rollback path

- This slice touches the existing feature-39 push, so rollback is
  *"revert the PR"*.
- Feature-flag behind `OWNER_RECAP_REPLAY_ENABLED=1` (default OFF in
  the first deploy), then flip ON once the owner has approved one
  fixture push.
- The diff block is purely additive to `body_markdown`; removing it
  reverts the recap to feature 39's exact output.
- Reversible in <5 min: env-set + restart.

## What is explicitly NOT in this slice

- **LLM-generated copy.** Slice is purely deterministic.
- **Per-owner persona profiles.** One config knob per deployment.
- **Voice audio recap.** v3.
- **Inline-tappable moments (button UI).** v3.
- **Multi-day replays.** v1 is yesterday ↔ today; multi-day is a v3
  follow-up (`/replay <N>`).
- **Style-guide changes.** This slice respects feature 57's style
  guide; it does not add to it.

## Charter conformance

- Charter invariant: *"Truth: GitHub is source of truth for files
  and code."* ✓ — the slice is identical-input, deterministic.
- Stock invariant: This slice does *not* write a `StockEntry` row;
  it *projects* existing rows. ✓
- State invariant: No automatic transitions. ✓
- Money invariant: N/A.
- AI invariant: No AI call. The slice is deterministic projection. ✓
