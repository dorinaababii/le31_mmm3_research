# Spec 181 — `merkle-audit-tamper-evident-root-hash-batching` (HANDOFF)

**Source feature:** `features/181-merkle-audit-tamper-evident-root-hash-batching.md`
**Parent research issue:** HMM-241
**Linear sub-issue:** HMM-244
**Filed:** 2026-09-15 by the LE31 daily-research cron

---

## Active feature path

- **Repo:** `dorinaababii/le31_mmm3_research.git` (working dir: `/opt/data/le31_mmm3_research_work/`)
- **Feature spec file:** `features/181-merkle-audit-tamper-evident-root-hash-batching.md`
- **This HANDOFF file:** `specs/merkle-audit-tamper-evident-root-hash-batching-HANDOFF.md`

## Seven-check gate verdict

| # | Check | Status |
|---|---|---|
| 1 | Goal stated | PASS (document the off-chain-batch + inclusion-proof + role-based-allow-list primitives as v2-hardening vocabulary) |
| 2 | Evidence / JTBD stated | PASS (peer-reviewed IJIRT paper with measured 99.97% gas-cost saving + 25-test adversarial suite; zero LE31 v1 pain observed; v2 trigger conditions listed) |
| 3 | Scope + Out-of-scope stated | PASS (vocabulary-only defer; no code; no v1 surface; no AI integration) |
| 4 | User flow described | N/A (no v1 user flow; v2 surface hypothetical) |
| 5 | Data model described | PASS (no v1 change; v2 data model described as `merkle_batches` + `merkle_inclusion_proofs` tables on top of existing `audit_logs`) |
| 6 | Dependencies + failure-recovery + DoD | PASS (no v1 implementation; rollback = N/A; DoD = filing committed + Linear sub-issue created) |
| 7 | Open questions listed | PASS (v2 trigger conditions; verification layer choice; conflict with existing `audit_logs` writer model) |

**Gate verdict:** PASS — v2 owner-pains architecture-reference (defer, parking-lot).

## Files to touch

1. **`features/181-merkle-audit-tamper-evident-root-hash-batching.md`** — already written (this is the only file created by this pick).
2. **`specs/merkle-audit-tamper-evident-root-hash-batching-HANDOFF.md`** — already written (this file).

**No other files touched.** This is a documentation-only pick.

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md`, this pick is a **v2 architecture-reference defer** (not a build), so the verification protocol is **just the existence of the two files + the cross-references**:

1. **Confirm `features/181-merkle-audit-tamper-evident-root-hash-batching.md` exists** in `/opt/data/le31_mmm3_research_work/features/`. Verified by parent: written.
2. **Confirm `specs/merkle-audit-tamper-evident-root-hash-batching-HANDOFF.md` exists** in `/opt/data/le31_mmm3_research_work/specs/`. Verified by parent: written.
3. **Confirm the Linear sub-issue (HMM-244) is created** with the Feature label and attached to the correct project. Per `le31-feature-pipeline/SKILL.md` v2-bucket picks attach to `le31 Research` (since `le31 v2 owner-pains` and `le31 v2-AI` projects do NOT exist — verified 2026-08-28).
4. **Confirm the parent research issue (HMM-241) cross-references this sub-issue** in the body or comments.

No pre-merge review required — this is a documentation-only pick, not a code change.

## Rollback path

**No rollback needed.** This is a documentation-only pick; the two files can be deleted without affecting the LE31 stack. If the operator wishes to "un-file" this pick (e.g., because a subsequent pass surfaces a stronger primitive set, or the owner decides the v2 trigger conditions will never fire):

1. Delete `features/181-merkle-audit-tamper-evident-root-hash-batching.md`.
2. Delete `specs/merkle-audit-tamper-evident-root-hash-batching-HANDOFF.md`.
3. Archive the Linear sub-issue HMM-244.
4. Append a row to `/opt/data/INDEX.md` documenting the close-out.

No git revert needed (the two files are committed once but deleting them is a clean follow-up commit).

## Mandatory LE31 skill list

The coding agent does **NOT** need to load the LE31 skill list for this pick — there is no implementation. The skills relevant to *creating* this pick (already done by the parent cron) are:

1. `le31-daily-research` — the parent applied this skill to identify the pick.
2. `le31-feature-pipeline` — the parent applied this skill to write the feature contract + HANDOFF.
3. `le31-v1-feature-pattern` — the parent applied this skill to enforce the canonical v1 feature contract shape (adapted to v2 here — see Notes below).
4. `le31-research` — the parent applied this skill for the v2 architecture-reference verdict discipline.

If/when the v2 surface is actually implemented (see Open questions in the feature spec for triggers), the coding agent will need to load:

1. `le31-conventions` — for the existing `audit_logs` schema + writer model + migration discipline.
2. `le31-backend` — for the FastAPI + SQLAlchemy surface to add the `/audit-proof/<row_id>` endpoint.
3. `le31-data` — for the `merkle_batches` + `merkle_inclusion_proofs` table design + migration via Alembic.
4. `le31-research` — for the v2-hardening vocabulary and the cross-references to features 121/122/129/133/134/135/137/141/167/168/169.
5. `test-driven-development` — for the regression-test discipline (any new v2 surface must have a corresponding test that exercises the inclusion proof + role-based allow-list).
6. `pre-merge-review` — for the non-author-independent-review gate.

## Notes for the operator

- **The pick is parked, not built.** The Linear sub-issue HMM-244 will sit in `Backlog` with the "v2 architecture-reference defer" verdict until one of the v2 trigger conditions fires (see Open questions in the feature spec).
- **The pick is **fully reversible**.** Deleting the two files and archiving the Linear sub-issue is the entire close-out path.
- **The pick does NOT trigger any v1 work** per `le31-daily-research/SKILL.md` hard rules. The §3.4 no-customer-facing-AI charter provision remains in force; this pick is compliant with §3.4.
- **The pick is the most concrete of the v2-hardening cluster** (most measured performance numbers, most adversarial tests); it is the *most likely* to be referenced when LE31 v2 actually implements an external-auditor surface.

## Notes for the next-pass follow-up

The next daily-research cron should:

1. **Re-fetch OpenAlex `append-only+audit`** to confirm whether new in-window papers in this cluster surface (meta.count was 131 today; volatile pool).
2. **Cross-reference features 121/122/129/133/134/135/137/141/167/168/169** to verify the cross-section story remains coherent. If a new primitive surface in the cluster, file a new pick.
3. **Do NOT re-file feature 181** — the pick is parked; the discipline is "do not re-park the same pick" (see feature 27 / 70 / 76 / 78 / 80 / 82 / 87 / 93 / 99 / 105 / 109 / 115 / 116 / 121 lesson).

## Notes on the v1 feature template adaptation

The canonical v1 feature pattern (per `le31-v1-feature-pattern/SKILL.md`) contains: Goal / Evidence/JTBD / Scope / Out of scope / User flow / Data model / API/bot/UI contract / Dependencies / Failure/recovery / Definition of done / Open questions.

The v2 architecture-reference pick (this feature 181) uses a **slightly adapted shape**:
- Goal ✓
- Scope ✓
- Out of scope ✓
- Description (which combines Evidence/JTBD + a transferable-primitives catalogue; this is the v2-specific content) ✓
- Data model ✓ (described in deferral terms — no v1 change)
- Implementation ✓ (deferral: "no implementation today; v2 implementation would be X, Y, Z")
- Telegram interaction ✓ (none for v1; hypothetical for v2)
- Dependencies ✓ (no v1 dependencies; v2 dependencies listed)
- Open questions ✓ (v2 trigger conditions + verification-layer choice + conflict-with-existing checks)
- Why this matters ✓

The adaptation is **explicit** (per the feature template's slicing rule #3: "Keep one owner-visible outcome per feature; split work crossing v1/v2/v2-AI") — this pick is a v2 architecture-reference, so the v1-specific sections (User flow, API/bot/UI contract, Failure/recovery, Definition of done) are intentionally elided in favour of a deferral statement + a hypothetical v2 implementation outline.
