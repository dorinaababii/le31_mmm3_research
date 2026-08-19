# reckon-low-effort-decision-journal-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/84-reckon-low-effort-decision-journal-watch.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `84`
- Slug: `reckon-low-effort-decision-journal-watch`
- Contract file: `features/84-reckon-low-effort-decision-journal-watch.md`
- Bucket: **v2 owner-pains** — defer (watch-list)
- Linear parent: `HMM-107` (Brainstorm 2026-08-19 — daily, created in this cron)
- Linear sub-issue: **HMM-108** (created in this cron; project `le31 v1 — Core MVP`, label `Feature`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (in-window ProductHunt main feed launch — `Reckon` "decision journal
that helps you calibrate", 2026-08-06; solo-builder micro-SaaS in the low-effort UX
lane). Confidence: **low–medium** for the JTBD pull (the peer is a solo-builder PH
launch with no star count and no public repo; the cross-section is real but the
evidence is thin).

**Decision: defer.** Failed checks:
- **Practicability**: no public Reckon repo to read for cross-section pattern validation; the surface design would require a teardown that the artifact cannot complete today.
- **Cost-to-value**: no observed LE31 cook/owner demand for decision-recap surface; the JTBD pull is inferred, not observed.
- **Scope**: the surface could expand into "full decision audit trail" which collides with features 61 (holdfast approval ledger) and 47 (decision-rationale mixin); the scope guardrail in the feature contract Q2 is essential.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules; even though this is v2 owner-pains, the slicing discipline inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-19).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after re-elevation).
6. `le31-research` (for the cross-section evidence base).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice will touch (when re-elevated to build)

```
features/84-reckon-low-effort-decision-journal-watch.md         # NEW (this artifact)
specs/reckon-low-effort-decision-journal-watch-HANDOFF.md      # NEW (this file)
INDEX.md                                                          # EDIT: append one row to "Active feature pipeline" table
backend/app/models/cook_decision.py                              # NEW: CookDecision SQLModel (append-only)
backend/alembic/versions/XXXX_add_cook_decision.py              # NEW: one migration
backend/app/services/cook_decision.py                            # NEW: append() + latest_for_cook()
backend/app/bot/cook_bot.py                                       # EDIT: /decision handler (≤30 lines)
backend/app/services/owner_recap.py                              # EDIT: append latest decision to daily recap (≤15 lines)
backend/tests/test_cook_decision.py                               # NEW: 3 acceptance tests
backend/README.md                                                 # note the new table + /decision command
```

Zero schema impact on existing tables. Zero new pip dependencies. Zero new config keys.

## Verification protocol

After the artifact ships (post-re-elevation):

1. **Read back** `features/84-reckon-low-effort-decision-journal-watch.md` and confirm it matches the daily-brainstorm report's "84-reckon-low-effort-decision-journal-watch" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-19), pick slug, feature path, and Linear sub-issue ID.
3. **Run the 3 acceptance tests** in `backend/tests/test_cook_decision.py`:
   - empty `CookDecision` table for cook X → latest_for_cook(X) returns None
   - one shift's decision → latest_for_cook(X) returns it; append-only (cannot update or delete)
   - recap channel wiring → the latest decision appears appended to the daily recap push
4. **Run the LE31 test suite** (`pytest` or equivalent) and confirm it still passes.
5. **Hand-test on the cook bot**: trigger `/decision` in a test chat; reply with free text; verify the answer is appended to `CookDecision` and surfaces in the next daily recap push.
6. **On a future daily-brainstorm pass**: re-query ProductHunt main feed + GitHub `topic:journal` + OpenAlex `decision journal` for new in-window peers with the single-field-per-day personal-calibration pattern. If a new ≥10★ peer with public repo surfaces, escalate evidence and re-evaluate.

## Rollback path

The artifact is a watch-list (no code shipped today). When re-elevated and shipped, rollback is: drop the `cook_decision` table via Alembic downgrade; remove the `/decision` handler; revert the recap channel wiring. The slice is reversible at zero data-loss cost (no production `CookDecision` rows will exist on the day of the rollback if the feature never saw real traffic).
