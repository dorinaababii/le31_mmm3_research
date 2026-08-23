# Slice Handoff — `aldia-ai-agent-business-engine-cross-section`

> **Pick**: 104-aldia-ai-agent-business-engine-cross-section (defer, watch-list, charter-pending)
> **Source brainstorm**: 2026-08-23 (Pick C)
> **Generated**: 2026-08-23 by daily-brainstorm cron

## Active feature path

- `features/104-aldia-ai-agent-business-engine-cross-section.md`
- This `specs/aldia-ai-agent-business-engine-cross-section-HANDOFF.md`

## Seven-check gate verdict

**Decision: defer, watch-list, charter-pending.** The cross-section is inverse-validation of LE31 charter §3.4 (no customer-facing AI): ALdia assumes AI-agent-facing API; LE31 says human-staff-facing. The artifact flags the charter tension for the next charter review, without changing today's roadmap.

**Gate summary**:
1. **JTBD**: When the LE31 v2 team considers whether the audit-trail primitive should accept AI-agent calls (in addition to human staff calls), knowing that a commercially-viable peer exists informs the API-surface decision. Defer (charter §3.4 is the binding constraint today).
2. **Viability**: n/a (no new feature to operate). The pattern informs existing feature 49 + 81 v2 extension.
3. **Practicability + confidence**: medium (peer repo 1★ + Apache-2.0 + Python + immutable-audit; architecture straightforward). Low confidence in LE31-specific urgency (1★ + charter tension).
4. **Conflict**: **flagged** — inverse-validation of charter §3.4. Not a hard conflict (the audit-trail primitive is the same) but requires explicit charter confirmation before adoption.
5. **Outcome, appetite, scope**: v2-AI + v2 owner-pains watch-list. S effort. ≤1 day. Defer (charter-pending).
6. **Cost to operational value**: zero implementation cost; pure pattern-record artifact. High upside (v2-AI API surface) at zero downside IF charter §3.4 is revisited.
7. **Circuit breaker + reversibility**: fully reversible. Watch-list artifact; can be deleted without consequence.

## Files to touch

**ZERO files in LE31 source tree.** This is a research-only artifact.

If the slice is ever un-deferred (i.e., when the peer crosses ≥5★ OR 2+ independent repos converge on the AI-agent-facing audit-trail API pattern **AND** charter §3.4 is explicitly revisited), the slice will become an **input to feature 49 + 81 v2 extension**, which will touch:
- `backend/app/audit/agent_api.py` (new file) — AI-agent-facing audit-trail API endpoint (separate from the human-calls endpoint).
- `backend/app/audit/router.py` (modify) — add the agent_api router with caller-distinction metadata.
- `specs/feature-49-81-v2-agent-api.md` (new file) — v2 extension spec.

These files do **not exist today** and **will not be created by this slice**. **Charter review required first.**

## Verification protocol reference

- **Today**: verify that this `HANDOFF.md` exists + `features/104-aldia-ai-agent-business-engine-cross-section.md` exists + the `INDEX.md` row was added + the `le31_daily_brainstorm_2026_08_23` Linear issue (HMM-133) was created with the parent body + the `le31_v1_core_mvp` Linear sub-issue was created with the charter-pending flag in the body.
- **Daily (next 7 days)**: track `jonalemndi2/ALdia` star velocity via `GET https://api.github.com/repos/jonalemndi2/ALdia` (via `$HERMES_GITHUB_TOKEN`).
- **Charter review trigger**: the next charter review (per PROJECT_CHARTER.md review cadence) should consider whether the AI-agent-facing audit-trail API surface is acceptable as a **non-customer-facing** layer (i.e., the AI agent is the orchestrator, not the customer).
- **Re-check threshold**: if stars ≥5 OR ≥2 independent repos in the same `topic:small-business` cluster ship with the same AI-agent-facing audit-trail API pattern **AND** charter §3.4 is explicitly revisited, the slice is un-deferred.

## Rollback path

**Fully reversible.** Delete `features/104-aldia-ai-agent-business-engine-cross-section.md` + this `HANDOFF.md` + the `INDEX.md` row + the `le31_daily_brainstorm_2026_08_23` sub-issue + the `le31_v1_core_mvp` Linear sub-issue. Zero risk of code regression (no code changed). **Charter untouched** — the artifact flagged the tension but did not modify the charter.

## Mandatory LE31 skill list

Before resuming this slice, load:
- `le31-conventions` — verify no charter violation (especially §3.4 AI + §3.7 truth + §3.9 privacy).
- `le31-feature-pipeline` — verify the contract is up-to-date.
- `le31-v1-feature-pattern` — confirm the v1 contract template format.
- `le31-coding-agent-brief` — generate the paste-in prompt only if the slice is un-deferred AND charter §3.4 is revisited.

If any skill is updated during the lifetime of this slice, patch it via `skill_manage(action='patch')` and re-verify before proceeding.

## Charter tension flag (explicit)

This is the **first brainstorm pick** in the 23-pass series that explicitly flags a **charter tension** (rather than a hard charter violation). The artifact invites the next charter review to revisit §3.4 with the option of allowing AI-agent-facing audit-trail APIs as a non-customer-facing layer. The artifact does NOT modify the charter; the charter review is the appropriate escalation path.
