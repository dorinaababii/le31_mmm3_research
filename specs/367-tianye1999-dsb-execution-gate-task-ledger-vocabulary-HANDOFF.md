# HANDOFF — Feature 364: `tianye1999-dsb-execution-gate-task-ledger-vocabulary`

**Upstream source repo: [`tianye1999/dsb`](https://github.com/tianye1999/dsb)** — see `features/364-tianye1999-dsb-execution-gate-task-ledger-vocabulary.md` for the full evidence record.

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/364-tianye1999-dsb-execution-gate-task-ledger-vocabulary.md` — defer/parking-lot (Pick A of Daily Brainstorm 2026-10-23).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 surface lets a system act on the owner's behalf, the owner wants *an explicit gate plus a durable record*, but struggles because *LE31's §3.1 explicit-action rule was designed for a human operator and has never been stress-tested against software that proposes actions*, so that *the ledger proves what was approved versus what ran*. **No observed JTBD today — LE31 has no agentic surface.** |
| 2 | Viability | ✓ | **Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE (code-shape adoptable)**, ★1⑂0, 7,295 KB, Python on-stack. **Traction caveat recorded in the feature: ★1⑂0 is no evidence in either direction — a repo created and pushed the same day as the pass.** The pick is about the shape, not the project. |
| 3 | Practicability and confidence | ✓ | The upstream stack (Android / DeepSeek / virtual display / scrcpy) is entirely off-stack, so no code is adoptable; the *vocabulary* is fully portable. No new packages, no schema migration, no infrastructure. Evidence strength: high for the vocabulary (named in the project's own description), low for present urgency. |
| 4 | Conflict | ✓ | Does not violate any invariant — the execution gate *is* §3.1, the task ledger *is* §3.3. **⚠️ But the pick is blocked by an unmade decision: LE31 has no AI surface at all (§3.4 permits AI assisting staff, never customer-facing), so there is nothing to gate.** This is the **third** pass to surface that decision (features 352, 354, 364). |
| 5 | Outcome + appetite + scope | ✓ | Maps to the v2-AI defer outcome. Maximum time worth spending: 45 min documentation. **Today: 0 build time.** |
| 6 | Cost to operational value | ✓ | The value is naming the gate/ledger/**log-split** before LE31 has any automated actor. Roughly 45 min of documentation; no build. |
| 7 | Circuit breaker + reversibility | ✓ | No code; no rollback needed. Revert by `git rm`. |

**Gate verdict: `defer` (parking-lot)** — 7/7 checks pass. `defer` because LE31 has no AI surface to gate, and adopting any of this presupposes an owner decision that has now been deferred three times.

## Bucket

**v2-AI (execution-gate + task-ledger + audit-log vocabulary)** — Pick A of Daily Brainstorm 2026-10-23. Note: **`le31 v2-AI` does NOT exist in the Linear workspace.** Confirmed this pass via `list_projects` — only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), `le31 Research` (P-HMM-1) exist. Per `le31-feature-pipeline/SKILL.md` line 33 this sub-issue attaches to **`le31 Research` P-HMM-1**.

## Files to touch

**None today.** Documentation-only.

If the owner ever decides LE31 gets an AI surface, the expected files are:

- `backend/models/task_ledger.py` — new **ProposedTask** model (intent, gate-required, never auto-executed).
- `backend/models/execution_log.py` — new **ExecutionLog** model (what ran; may diverge from approval — this divergence is the point).
- `backend/services/gate_service.py` — the gate itself: refuses to proceed without an explicit approval record. **No implicit path may reach an execution write.**
- `backend/services/task_ledger_service.py` — append-only writes for both models.
- `backend/alembic/versions/` — migration adding both tables.
- `bot/handlers/gate_handlers.py` — cook-Telegram inline Approve/Reject buttons (§3.1-conformant explicit action, needs no new client).
- `tests/test_gate_service.py` — **the load-bearing test: assert that no code path writes an ExecutionLog without a prior Approval.** This test is the feature.

## Verification protocol reference

Per `le31-conventions`: "Declaring done from a diff or passing tests alone" is a pitfall. When this feature is ever built, the gate must be exercised as **observable behaviour** — attempt an agent action with no approval, and observe the refusal, in the running system, not just in a unit test.

## Rollback path

`git rm features/364-*.md specs/367-*-HANDOFF.md`. Documentation-only, no migration, no data. Fully reversible.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate
- `le31-backend` — FastAPI/SQLModel patterns
- `le31-data` — append-only ledger rules (StockEntry: never update or delete)
- `le31-frontend` / `le31-telegram` surface patterns
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for invariants

## Open questions carried into any future build

1. **Does LE31 get any AI surface at all?** Unmade. Third time surfaced.
2. Should the ledger/log split be adopted for `StockEntry` even with no AI? **Do not do this speculatively** — no current pain.
3. Features 352 vs 354 retrieval-strategy conflict (vector-first vs keyword/file-based) — **still unresolved**, untouched by this feature.