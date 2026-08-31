# HANDOFF — 140-casedock-adhd-informed-solo-builder-workbench-htmx-design-posture

**Status**: defer (parking-lot, watch-list design reference, no build today)
**Date**: 2026-08-30
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/140-casedock-adhd-informed-solo-builder-workbench-htmx-design-posture.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no v2 surface where the solo owner is asked to triage or focus; the value of casedock today is *design posture*, not *implementation*. Stack mismatch: casedock is Django 6, not FastAPI. Apache-2.0 licence permits design-idea adoption only.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the casedock repo (GitHub `gerpaick/casedock`, Apache-2.0, 2★, 6.6 MB, Python Django 6 + HTMX, **pushed today 2026-08-30T06:25:10Z**) as a dated, in-window design-posture reference for the next time LE31 proposes a v2 surface where the solo owner is asked to triage, focus, or review.

If the trigger condition (LE31 first proposes a v2 surface for owner-facing review/recap AND that surface asks the owner to triage or focus) is met, the external coding agent should:

1. Load this artifact and the casedock README (parent-fetched 2026-08-30).
2. Load the companion feature 130 (DHH-restaurant paper) and feature 84 (Reckon low-effort decision-journal watch) — casedock is the *implementation primitive* sibling of those features.
3. Load the companion feature 134 (ECHO Auditable Memory Plane) — casedock Case is the *bounded-working-object dual* of ECHO's structured records.
4. Re-run the LE31 feature gate with the casedock README in hand.
5. **Decide whether the surface is a workbench** (casedock-style bounded active set) **or a recap feed** (LE31 v1 owner-recap style chronological feed). The two have different shapes.
6. **If workbench: define the bounded working object** for LE31's owner surface. The most likely Case shapes are `Visit`, `Bill`, `Shift`, or `Reconciliation`.
7. **If workbench: implement the triage state machine**. casedock's states are `do_now / convert_to_case / set_aside / waiting / archive`. For LE31's owner surface, the equivalent states are `pending / reviewed / resolved / escalated / archived`. The "decided once" invariant is the load-bearing one.
8. **If workbench: respect the focus bound**. casedock's "1 main + 2 secondary per day" is aggressive; LE31's owner may need 5–10 active items without folding. The principle (bounded active set) is the load-bearing one; the exact bound is open.
9. **Add an explicit *no AI in the triage step* guardrail** — the casedock posture is *explicitly anti-AI* ("the first thing you see is an action, not information" — AI suggestions are information, not action).
10. **Decide whether the surface is a Telegram surface** (LE31 v1 chat-based) **or a web surface** (LE31 v1 has `index.html` mockups). casedock is a web surface; the Telegram equivalent is a different problem.
11. **Pilot on one decision type first**. Do not triage all of the owner's decisions at once.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/140-casedock-adhd-informed-solo-builder-workbench-htmx-design-posture.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-08-30.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-08-30/gh/restaurant-language_python-stars_%3E1-archived_false-created_2026-07-31..2026-08-30.json` (the in-window ≥1★ Python repo listing where casedock is NOT present — casedock surfaced via the `htmx+language:python` axis at `/tmp/le31-brainstorm-2026-08-30/gh/htmx-language_python-stars_%3E1-archived_false-created_2026-07-31..2026-08-30.json`).
- **Companion artifacts**:
  - `features/84-reckon-low-effort-decision-journal-watch.md` (Reckon PH launch — sibling JTBD validation)
  - `features/130-dhh-kitchen-accessible-operator-ux-visual-replayable.md` (DHH-restaurant paper — sibling cross-section)
  - `features/134-echo-auditable-memory-plane-stockentry-audit.md` (ECHO — bounded working object dual)
- **casedock README**: `https://raw.githubusercontent.com/gerpaick/casedock/main/README.md` (parent-fetched 2026-08-30)
- **Charter §3.1 (append-only ledger)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.4 (no customer-facing AI)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.4.4 (the non-technical owner)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 append-only, §3.4 observable evidence, §3.4.4 the non-technical owner).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification.

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The design posture surfaced by this defer is:

- **ADHD-informed design principles**: *"remove decisions instead of adding them; the first thing you see is an action, not information"* + *"no red badges, overdue indicators, or streaks"* + *"no time estimation, no gamification"* + *"the board never shows more than ~7–10 active cases without folding"*.
- **Core loop**: Capture → Triage (decided once: do_now / convert_to_case / set_aside / waiting / archive) → Case (bounded working object: spec / decisions / execution items / private notes / source links) → Focus (1 main + 2 secondary per day).
- **Anti-AI posture**: casedock has no AI integration; the triage step is operator-only; no AI suggestions shown in the triage step.

LE31 v1 doesn't have a v2 surface that needs this primitive today. The defer artifact does **not** propose a `Case` entity or a `Triage` state machine. It surfaces the *design posture* for future use.

When the defer is promoted to build, the future v2 surface would:

- Introduce a `Case` entity (analogous to `StockEntry` but for the decision layer).
- Introduce a `Triage` state machine: `pending / reviewed / resolved / escalated / archived` — each item gets decided exactly once.
- Adopt the "decided items leave your head" principle: triage-decided items do not appear again.
- Respect the focus bound (likely 5–10 active items, not casedock's 1+2).
- Add an explicit *no AI in the triage step* guardrail.
- Be a web surface (casedock is web; Telegram equivalent is a different problem).

## Files to touch (when defer is promoted to build)

None today. When the defer is promoted:

- `backend/app/models/` — possibly add a `Case` table or a `Triage` state machine. *Not before the defer is promoted.*
- New module (e.g., `backend/app/services/owner_workbench.py`) for the workbench surface. *Not before the defer is promoted.*
- `frontend/index.html` — possibly add a workbench page. *Not before the defer is promoted.*
- `features/<NN>-<new-slug>.md` — the build-time feature contract, derived from this defer artifact and the trigger conditions.

## Rollback path

Fully reversible. Filing as a defer artifact does not change any schema, any code, any surface. If the trigger condition is never met, this artifact can be archived without consequence. If the trigger condition is met and the build is rejected, the defer artifact remains in the watch-list for re-evaluation.

**Close trigger**: this parking-lot defer should be closed (and the artifact archived) when:
- LE31 first proposes a v2 surface where the owner is asked to triage or focus (then promote to build), OR
- 6 months pass without the trigger condition being met (then archive without consequence).

## Open questions carried forward

- **Is LE31 v2 an owner-workbench or an owner-recap?** The two have different shapes. The decision determines whether this primitive is relevant.
- **What is the bounded working object for LE31's owner?** Most likely: `Visit`, `Bill`, `Shift`, `Reconciliation`.
- **Is the "decide once" invariant compatible with v1?** LE31 v1's `audit_logs` are append-only (no edits, no deletes). The "decided once" invariant is *additive* over `audit_logs`: every triage decision is a new `audit_logs` row.
- **What is the focus bound for LE31's owner?** casedock's "1 main + 2 secondary per day" is aggressive. LE31's owner may need 5–10 active items without folding.
- **Is the casedock posture compatible with charter §3.4?** Yes by construction (no AI integration in casedock), but the *guardrail* must be written into the contract: *"the triage step is operator-only; no AI suggestion is shown in the triage step"*.

## Verification protocol reference

When the defer is promoted to build:

1. Re-run `le31-conventions`'s seven-check feature gate with the casedock README in hand.
2. Decide: workbench or recap feed?
3. If workbench: define the bounded working object.
4. If workbench: implement the triage state machine (RED: trigger a state transition without operator decision; GREEN: trigger it with operator decision).
5. If workbench: test the focus bound (RED: show 100 active items; verify the surface folds to ≤10; GREEN: show 1 active item; verify the surface doesn't over-fold).
6. If workbench: test the no-AI-in-triage guardrail (RED: introduce an AI suggestion in the triage step; verify it is rejected; GREEN: introduce it elsewhere; verify it is allowed).
7. If workbench: pilot on one decision type first.

## Companion artifacts (cross-references)

- Feature 84 (Reckon low-effort decision-journal watch) — sibling JTBD validation (PH launch, no code).
- Feature 130 (DHH-restaurant paper) — sibling cross-section: *"workstation prompts + self-paced rehearsal"*.
- Feature 134 (ECHO Auditable Memory Plane) — bounded working object dual: ECHO = structured records; casedock Case = bounded working object that *uses* structured records.

## Why this matters (one-line)

The casedock repo is the **first implementation primitive** for the "low-effort UX for solo operators" cross-section that feature 84 only validated at the JTBD level — its **Case + Decide Once** design pattern, plus its **explicit anti-AI design principles** ("no gamification", "no streaks", "the board never shows more than ~7–10 active cases"), is the most directly transferable v2 surface primitive for any future LE31 owner-facing review/recap surface, and the Apache-2.0 licence permits design-idea adoption without attribution gymnastics.
