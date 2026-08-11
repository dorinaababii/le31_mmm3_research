# owner-recap-persona-voice — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/57-owner-recap-persona-voice.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `57`
- Slug: `owner-recap-persona-voice`
- Contract file: `features/57-owner-recap-persona-voice.md`
- Bucket: v2 owner-pains (S effort — feature 39 extension)
- Linear parent: HMM-62 (Brainstorm 2026-08-11 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build.** No failed checks. (Confidence: high; literature:
W7172434674 + W7172493963 + W7172068431 in-window.)

Evidence precondition: **observed** (4 in-source anchors today:
W7172434674 kama muta paper; W7172493963 chatbot emotion SR;
W7172068431 Hakka Kitchen cultural heritage; W4417084818 uncanny-valley
SR — bound). Confidence: **high**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract
   back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/config.py                            # NEW: OWNER_RECAP_PERSONA = 'plain' | 'warm' (default 'plain')
backend/app/services/recap_moments.py            # NEW: pick_moments() deterministic heuristic + style guide
backend/app/services/recap.py                    # EDIT: extend the existing build_daily_recap() to prepend moments (1-line PR)
backend/app/bot/cook_bot_explain.py              # NEW: /why <recap_moment_index> handler (or piggyback on feature 55's module)
backend/app/bot/cook_bot.py                      # EDIT: register /why handler (1 line, behind OWNER_EVIDENCE_REVIEW_ENABLED flag)
backend/tests/test_recap_moments.py              # NEW: deterministic unit tests
backend/README.md                                # note the persona config knob + the new /why command
```

No new pip dependencies. No schema change.

## Endpoints and contracts added

No new HTTP routes. No new SQLModel tables. No new Alembic migration.
The `OwnerRecap.body_markdown` field (from feature 39) is **extended
at write time** — the existing column is unchanged.

The extension looks like:

```
🌙 Tonight (2026-08-10)
  • 21:30 — Lamb 86ed after running out (cook-2)
  • 21:55 — Focaccia comp for the birthday table (cook-2)

(existing 4-section body unchanged)
```

When `OWNER_RECAP_PERSONA='plain'`, the moments block is the only
addition. When `OWNER_RECAP_PERSONA='warm'`, a single line of human-feel
copy is added to the top of the moments block ("Today had a few good
ones, the regulars were out in force."). Both keep the bot plain —
no persona name, no first-person emotional voice, no anthropomorphising.

## Style guide (enforced by code review)

The `pick_moments()` function and the optional persona line adhere
strictly to the style guide encoded in the module's docstring and
test fixtures. The coding agent MUST:

- Never use first-person voice ("we had a great night").
- Never anthropomorphise ("the kitchen felt busy").
- Never give the bot a name.
- Keep each moment ≤12 words.
- Keep the optional warm line ≤18 words.

`OWNER_RECAP_PERSONA='warm'` adds ONE warm line (if the deployment
chooses it). It does not turn the bot into a persona.

## Endpoints and bot commands added

One new owner-only Telegram command on the existing `cook_bot.py`:

- `/why <recap_moment_index>` — returns the per-moment evidence card,
  delegating to feature 55's `EvidenceLink` table. Falls back to
  "No moment <N> in recap <R>" if not found.

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent MUST:

1. Unit-test `pick_moments()` deterministically: same input → same
   output across 3 fixtures.
2. Style-guide unit-test: assert no first-person voice, no persona
   names, line-length cap respected.
3. Bot test: `/why 1` returns the expected card for a fixture row;
   `/why 0` returns the "No moment 0" fallback.
4. Persona-knob test: `OWNER_RECAP_PERSONA='warm'` adds the warm line;
   `OWNER_RECAP_PERSONA='plain'` does not. Same bot output for both
   `plain` and `warm` apart from the single warm line.

After implementation, run the parent's verify-before-fixing protocol on
the slice branch.

## Rollback path

- This slice touches the existing feature-39 push, so rollback is
  "revert the PR". Feature-flag behind `OWNER_RECAP_PERSONA_VOICE_ENABLED=1`
  (default OFF in the first deploy), then flip ON once the owner has
  approved one fixture push.
- The optional `OWNER_RECAP_PERSONA='warm'` mode is per-deployment
  config; flipping back to `'plain'` is a single env-set.
- Reversible in <5 min: env-set + restart.

## What is explicitly NOT in this slice

- LLM-generated copy. Slice is purely deterministic.
- Per-owner persona profiles. One config knob per deployment.
- Voice audio recap. v3.
- Inline-tappable moments (button UI). v3.
