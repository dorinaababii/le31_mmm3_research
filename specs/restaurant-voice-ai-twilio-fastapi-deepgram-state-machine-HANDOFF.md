# restaurant-voice-ai-twilio-fastapi-deepgram-state-machine — HANDOFF

> **Slice for the research agent.** This is a passive parking-lot
> observation of the in-window `arushahmd/restaurant-voice-ai`
> cross-section peer, not a feature build. The slice boundary is
> hard: zero source-file edits, zero schema changes, zero new config
> keys. Read this *and*
> `features/113-restaurant-voice-ai-twilio-fastapi-deepgram-state-machine.md`
> before touching any code. Do not paste chat excerpts back into the
> build.

## Frozen identifiers (do not rename)

- Feature ID: `113`
- Slug: `restaurant-voice-ai-twilio-fastapi-deepgram-state-machine`
- Contract file: `features/113-restaurant-voice-ai-twilio-fastapi-deepgram-state-machine.md`
- Bucket: **v2 owner-pains (parking-lot, future-voice-cook-bot-architecture)**
  — hard defer pending charter §3 voice-input cook-bot review
- Linear parent: **HMM-147** (Brainstorm 2026-08-25 — daily, created in this cron)
- Linear sub-issue: **HMM-149** (create as a draft parking-lot artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct repo GET on
`arushahmd/restaurant-voice-ai`; ★1 low community traction;
MIT permissive license; Python; FastAPI + Twilio + Deepgram +
Redis + custom NLU + deterministic state-machine orchestration;
pushed 2026-08-19T17:09:21Z).

**Confidence:** **high** for the cross-section pattern (the
FastAPI + deterministic-state-machine voice-ordering architecture is
documented in the repo description); **low** for the LE31-specific
build implication (LE31 v1 doesn't ship a voice-input cook-bot
surface; no owner signal of "I want voice-input for the cook-bot"
today; the v2 extension is a future-tense concern; charter §3.5
AI non-customer-facing rule applies — voice-input must be gated on
deterministic state transitions, not free-form LLM calls).

**Decision: parking-lot; hard defer pending owner-pain signal or
charter §3 voice-input cook-bot review.** The README read is the
next research-side action. The "should LE31 v2 add voice-input to
the cook-bot surface (features 41 + 65 v2 extension)?" question is
parked pending charter approval.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job on 2026-08-25).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/113-restaurant-voice-ai-twilio-fastapi-deepgram-state-machine.md   # NEW (this artifact)
specs/restaurant-voice-ai-twilio-fastapi-deepgram-state-machine-HANDOFF.md  # NEW (this file)
INDEX.md                                                                     # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

- **Today**: verify that this `HANDOFF.md` exists + the
  `features/113-…md` contract file exists + the `INDEX.md` row was
  added + the `le31_daily_brainstorm_2026_08_25` Linear issue
  (HMM-147) was created with the parent body + the
  `le31_v1_core_mvp` Linear sub-issue (HMM-149) was created with the
  contract body and `Feature` label.
- **Daily (next 7 days)**: track `arushahmd/restaurant-voice-ai`
  star velocity via `GET
  https://api.github.com/repos/arushahmd/restaurant-voice-ai`
  (via `$HERMES_GITHUB_TOKEN`).
- **Daily (next 7 days)**: read the `restaurant-voice-ai` README +
  architecture documentation and confirm the deterministic-state-
  machine voice-ordering pattern (READ ONLY — no import, MIT means
  code-borrow is permitted but no borrow is needed today).
- **Re-check threshold**: if stars ≥50 OR ≥3 independent
  FastAPI + deterministic-state-machine voice-ordering peers, OR
  the LE31 owner signals an explicit "I want voice-input for the
  cook-bot" pain, the slice is un-deferred and becomes a v2
  charter-question prompt.

## Linear sub-issue

- **Parent**: HMM-147 (Brainstorm 2026-08-25 — daily, project `le31
  Research`, status Done).
- **Sub-issue**: HMM-149 (Feature, project `le31 v1 — Core MVP`,
  status Backlog). Body has the full contract body; label `Feature`.

## Rollback path

**Fully reversible.** Delete
`features/113-restaurant-voice-ai-twilio-fastapi-deepgram-state-machine.md`
+ this `HANDOFF.md` + the `INDEX.md` row + the
`le31_daily_brainstorm_2026_08_25` parent issue + the
`le31_v1_core_mvp` sub-issue (HMM-149). Zero risk of code regression
(no code changed).

## Why this matters (for the research agent)

The 2026-08-25 brainstorm pass surfaces
`arushahmd/restaurant-voice-ai` as the **only in-window FastAPI-
stack voice-ordering peer that explicitly names "deterministic
state-machine orchestration."** The cross-section insight informs
LE31 v2 owner-pains voice-input cook-bot surface (features 41 + 65
v2 extension) gated on deterministic-state-machine transitions, not
free-form LLM calls — preserving charter §3.1 + §3.5. MIT permissive
license means any spec or pattern is reusable without license
concerns for future v2 owner-pains extension. The artifact records
the deterministic-state-machine voice-ordering architecture for
future v2 iteration.

## Carry-over history

- **2026-08-25**: created from brainstorm 2026-08-25 Pick B.
- **Next pass (2026-08-26)**: down-stream daily-research pass should
  read `arushahmd/restaurant-voice-ai` README + architecture
  documentation and confirm the deterministic-state-machine
  voice-ordering pattern. Add `arushahmd/restaurant-voice-ai` to the
  daily-research watch list (5-repo watch) to track star velocity +
  push activity.

If the destination repo's research-side Hermes instance finds the
README read changes the gate verdict (e.g., the deterministic-
state-machine pattern turns out to be a thin wrapper around an LLM
call rather than a real state-machine), the slice should be amended
rather than re-created.