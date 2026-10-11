# HANDOFF — Feature 304: `DSHCorrectover-agent-second-fuse-mit-independent-fail-closed-second-fuse-ai-agents-runtime-guard-signed-receipts-append-only-ledger-incident-reports-v2-ai-fail-closed-second-fuse-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/304-DSHCorrectover-agent-second-fuse-mit-independent-fail-closed-second-fuse-ai-agents-runtime-guard-signed-receipts-append-only-ledger-incident-reports-v2-ai-fail-closed-second-fuse-vocabulary.md` — defer/parking-lot (Pick C of Daily Research 2026-10-11).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports* primitive, the owner wants *evidence that this fail-closed-second-fuse-vocabulary exists in 2026 with an independent-runtime-guard + incident-reporting surface*, but struggles because *LE31 has no documented v2-AI fail-closed-second-fuse-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the fail-closed-second-fuse framing + the incident-reports primitive"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports) without specialist help. The 0★/0⑂ with single-maintainer cadence + 84 KB tiny repo makes code adoption risky, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: **Python on-stack** (LE31 stack match). The **runtime-guard + signed-receipts + append-only-ledger + incident-reports** primitives are the v2-AI surface, not the v1 surface. Required data + permissions + infrastructure: Python runtime + cryptographic-signing utility + append-only-ledger + incident-reporting surface. Rabbit hole: 84 KB tiny repo is the smallest v2-AI pick of the 73-pass series and may not have full implementation. Evidence strength: medium for vocabulary (the verbatim description names the 5-primitive set); low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *fail-closed-second-fuse + runtime-guard* discipline IS the §3.4 *non-AI-fallback + safe-default* charter invariant applied to the *AI-agent-action* dimension (the second fuse is a deterministic rule-based guard that is independent of the AI model = non-AI-fallback). The *append-only-ledger* primitive is §3.1-aligned. The *signed-receipts + incident-reports* primitives are §3.4 *observable-evidence* charter invariant. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI outcome (fail-closed-second-fuse for AI-agent actions). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs`) already implement the append-only discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + 0★ + 84 KB tiny + no v2-AI surface in v1 charter).

## Bucket

**v2-AI** (fail-closed-second-fuse-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description names the 5-primitive quintuple set (`fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports`).

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that adds a v2-AI surface that requires fail-closed-second-fuse with runtime-guard + signed-receipts + append-only-ledger + incident-reports semantics):

1. `backend/alembic/versions/` — add Alembic migration that adds a `signature` column on the `audit_logs` table for v2-AI receipts.
2. `backend/app/audit/models.py` — add new `IncidentReport` SQLModel table with columns: `id` (UUID), `receipt_id` (UUID FK to `audit_logs`), `denied_action` (str), `denial_reason` (str), `denied_at` (timezone-aware datetime), `notified_operator_at` (timezone-aware datetime nullable), `operator_response` (str nullable).
3. `backend/app/audit/models.py` — add new `second_fuse_rule` SQLModel table with columns: `id` (UUID), `agent_id` (str), `action` (str), `rule` (JSON), `enabled` (bool), `created_at`, `updated_at`.
4. `backend/app/audit/models.py` — add new `second_fuse_decision` SQLModel table with columns: `id` (UUID), `action_id` (str), `decision` (enum: ALLOW / DENY), `reason` (str), `decided_at` (timezone-aware datetime), `signature` (str).
5. `backend/app/audit/second_fuse_runtime.py` — NEW: runtime guard that evaluates a rule against an action and returns ALLOW / DENY (the second fuse).
6. `backend/app/audit/incident_report.py` — NEW: structured incident report formatter.
7. `backend/app/audit/ed25519_sign.py` — NEW: ed25519 sign/verify utility (sister-shape to feature 302 step 7).
8. `backend/app/api/v2/second_fuse.py` — NEW: `GET /v2/second-fuse/decisions?agent=<>&action=<>&as_of=<>` search endpoint.
9. `backend/app/api/v2/second_fuse.py` — NEW: `POST /v2/second-fuse/decide` endpoint.
10. `backend/app/api/v2/incidents.py` — NEW: `POST /v2/incidents` endpoint.
11. `backend/app/api/v2/incidents.py` — NEW: `GET /v2/incidents?denied=<>&notified=<>&as_of=<>` query endpoint.
12. `backend/app/bot/notifications.py` — add Telegram notification hook that sends a Telegram message to the operator when an incident is recorded.

## Verification protocol

1. `git clone https://github.com/DSHCorrectover/agent-second-fuse` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/DSHCorrectover/agent-second-fuse/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set).
3. `curl -sS -H "Authorization: Bearer ***" "https://api.github.com/repos/DSHCorrectover/agent-second-fuse"` for star count, fork count, license, language, pushed_at, created_at, topics, description (parent-verified 2026-10-11).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the second-fuse + signed-receipts + incident-reports changes are isolated to the expected files.
5. Per `le31-conventions/SKILL.md`: load `le31-conventions`, `le31-research`, `le31-v1-feature-pattern`, `le31-handoff-spec` before any implementation.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v2-AI trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop the new tables + remove the `signature` column on `audit_logs` + remove the new API endpoints.
- No data loss if the rollback happens BEFORE any second-fuse-decision row is written.
- Full data retention if the rollback happens AFTER rows are written (the new tables are dropped but the original `audit_logs` rows are preserved per the *append-only* invariant).

## Mandatory LE31 skill list

Before any implementation, the coding agent must load:
1. `le31-conventions` — the global LE31 decision layer (charter invariants + feature gate).
2. `le31-research` — the research workflow.
3. `le31-v1-feature-pattern` — v1 feature-pattern enforcement (append-only StockEntry, etc.).
4. `le31-handoff-spec` — the handoff-spec requirements (frozen contract discipline, mandatory skill list, verification protocol).
5. `le31-feature-pipeline` — the feature-pipeline workflow (parent research issue, sub-issue creation, handoff file).

## Linear sub-issue reference

Sub-issue draft (deferred pending Linear MCP write endpoint recovery): `Research 2026-10-11 / Pick C — v2-AI fail-closed-second-fuse-vocabulary (DSHCorrectover/agent-second-fuse)`. Parent fallback JSON captures the intended sub-issue at `/opt/data/le31-daily-research-2026-10-11.linear-fallback.json`. Sub-issue project = `le31 Research` (P-HMM-1) per `le31-feature-pipeline/SKILL.md` line 33 since `le31 v2-AI` does not exist.

## Parent research issue

[linear: blocked — workspace plan-limit error 21st consecutive day; parent fallback at `/opt/data/le31-daily-research-2026-10-11.linear-fallback.json`]