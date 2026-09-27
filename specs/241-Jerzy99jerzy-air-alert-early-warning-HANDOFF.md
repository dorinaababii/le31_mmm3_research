# HANDOFF — Feature 241: `Jerzy99jerzy-air-alert-early-warning-apache-2-0-base-rate-gate-shared-alarm-budget-association-4-alert-state-append-only-stdlib-only-v2-alert-budget-vocabulary-reference`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/241-Jerzy99jerzy-air-alert-early-warning-apache-2-0-base-rate-gate-shared-alarm-budget-association-4-alert-state-append-only-stdlib-only-v2-alert-budget-vocabulary-reference.md` — defer/parking-lot (Pick C of Brainstorm 2026-09-27, parent research issue will be recorded as linear: blocked with fallback JSON at `/opt/data/le31-brainstorm-2026-09-27.linear-fallback.json`).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Charter §3.1 (explicit state transitions) | ✓ | Pick C's *4-alert-state-machine + 2-timing-regimes* is the §3.1 primitive applied to alert-publication; every state-transition is operator-driven or rule-driven, not implicit |
| 2 | Charter §3.2 (permissive license) | ✓ | Apache-2.0 permissive; §3.2 STRICTLY-COMPATIBLE |
| 3 | Charter §3.4 (no customer-facing AI) | ✓ | Pick C has no AI surface; the *base-rate-gate* is a deterministic rule evaluation, not customer-facing AI; the *cross-border-early-warning* domain is OSINT, not restaurant |
| 4 | In-window by `pushed_at` only | ✓ | pushed 2026-09-24T21:32:00Z (in-window by `pushed_at`); created 2026-09-04T22:42:38Z (~23 days old, IN-WINDOW BY PUSH ONLY; `created_at` is OUT-OF-WINDOW by ~7 days before window-start) |
| 5 | Ripgrep-verified unique vs features/ 1..238 | ✓ | parent-verified via `grep -l -i 'air-alert\|Jerzy99' features/*.md` → 0 matches |
| 6 | Cross-section with ≥1 existing feature | ✓ | features 174 + 177 + 216 + 230 via the *operator-wakeup-on-event + deterministic-rule-only + stdlib-only* cluster |
| 7 | Defer verdict (parking-lot, no code change today) | ✓ | 0★ + 23-day-old repo + no observed LE31 v2 pain + the *base-rate-gate + shared-alarm-budget + association + stdlib-only* posture is a vocabulary reference, not a build-need today; **NOT picked today** because LE31 v1 has no operator-wakeup-on-event surface (charter §3.1) |

**Gate verdict**: **defer (parking-lot)** — 7/7 gate checks pass, but the build verdict is `defer` because the artifact is vocabulary-only (the *operator-wakeup-on-event* surface is a v2 future reference, not a v1 build-need today).

## Bucket

**v2 alert-budget + base-rate-gate vocabulary reference** — the *base-rate-gate + shared-alarm-budget + association + stdlib-only* posture is the value, not the code. The verbatim description (`Cross-border early warning from Ukrainian air-alert feeds. A base-rate gate a rule must clear before it may wake anyone: recall, a shared alarm budget, association. Two timing regimes, four alert state.`) is the vocabulary primitive; LE31 v2 has no *operator-wakeup-on-event* surface today.

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that proposes a *low-stock-alert* or *expiry-alert* or *supplier-delivery-due-alert* surface; first v2 PR that proposes a *limit-total-alarms-per-day* surface), the implementation would not require a code change for the existing LE31 v1 surface — the existing `Visit` 5-state-machine + `audit_logs` append-only-ledger already implements the §3.1 primitives. The HANDOFF is to evaluate whether the v2 *low-stock-alert + base-rate-gate + 4-alert-state-machine* surface is the right product-wedge for the next v2 PR.

**For v2 low-stock-alert + base-rate-gate + 4-alert-state-machine** (if approved):
1. Add an `alert_rule` table to the LE31 v2 schema (Alembic migration) with columns `alert_rule_id, rule_name, rule_expression, base_rate_threshold, alert_state, correlation_id`.
2. Add a `shared_alarm_budget` table to the LE31 v2 schema (Alembic migration) with columns `budget_id, budget_date, budget_total, budget_consumed, budget_remaining`.
3. Add a `signal_association` table to the LE31 v2 schema (Alembic migration) with columns `association_id, source_alert_id, target_alert_id, association_rule`.
4. Add a `4_alert_state_machine` table to the LE31 v2 schema (Alembic migration) with columns `alert_id, current_state, state_transitions[], state_history[]`.
5. Add a `source_provenance` table to the LE31 v2 schema (Alembic migration) with columns `provenance_id, source_url, source_timestamp, source_schema`.
6. Add a `base_rate_gate_evaluator` module at `app/alerts/base_rate_gate.py` that evaluates the *base-rate-gate* using deterministic rule evaluation (NOT ML/LLM model per charter §3.4 no-customer-facing-AI invariant).
7. Wire the *base-rate-gate-evaluator* to the existing FastAPI app via a FastAPI dependency.
8. Wire the *4-alert-state-machine* to the existing FastAPI app via a FastAPI state-machine handler.
9. New feature file at `features/NNN-low-stock-alert-base-rate-gate-v2.md` (NOT this defer artifact).

## Verification protocol

1. `git clone https://github.com/Jerzy99jerzy/air-alert-early-warning` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/Jerzy99jerzy/air-alert-early-warning/main/README.md` (parent-verified 2026-09-27; the README is the source of truth for the verbatim description + the 18 named topics).
3. `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN" "https://api.github.com/repos/Jerzy99jerzy/air-alert-early-warning"` for star count, fork count, license, language, pushed_at, created_at, topics (parent-verified 2026-09-27; Apache-2.0 ✓, 0★/0⑂, Python, pushed 2026-09-24T21:32:00Z, created 2026-09-04T22:42:38Z, 6091 KB, 18 topics, archived=False).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the base-rate-gate-evaluator + 4-alert-state-machine changes are isolated to the expected files.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v2 trigger fires and the implementation lands:
- For v2 low-stock-alert + base-rate-gate + 4-alert-state-machine: rollback = `alembic downgrade -1` to drop the 5 new tables (`alert_rule + shared_alarm_budget + signal_association + 4_alert_state_machine + source_provenance`); the *base_rate_gate_evaluator* module is additive, not destructive; the existing FastAPI app continues to work without the alert-publication surface.

## Mandatory LE31 skill list (load these first)

Before authoring or reviewing any code derived from this HANDOFF, load these skills in order:

1. `skills/le31-conventions/SKILL.md` — the seven-check feature gate, charter invariants, and conflict-resolution rules.
2. `skills/le31-v1-feature-pattern/SKILL.md` — the existing v1 feature template + style guide.
3. `skills/le31-daily-research/SKILL.md` — the daily-research cron contract + source-families pattern.
4. `skills/le31-handoff-spec/SKILL.md` — the slice-contract template + verification-protocol reference.
5. `skills/le31-coding-agent-brief/SKILL.md` — the paste-in prompt for the coding agent.

The coding agent must NOT author code without all 5 skills loaded.