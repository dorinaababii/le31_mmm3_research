# Slice Contract — `br-collab-Project-Atreides-mit-doctrine-governed-type-safe-asset-class-agnostic-python-framework-institutional-post-trade-operations-custody-settlement-reconciliation-securities-lending-v1-institutional-reconciliation-architecture-reference` (defer, parking-lot, vocabulary reference)

> **Active feature path:** `features/250-br-collab-Project-Atreides-mit-doctrine-governed-type-safe-asset-class-agnostic-python-framework-institutional-post-trade-operations-custody-settlement-reconciliation-securities-lending-v1-institutional-reconciliation-architecture-reference.md`
> **Linear sub-issue:** [linear: blocked] (workspace plan-limit error: *"You've exceeded the free issue limit for this workspace"* — 10th consecutive day; intended project `le31 v1 — Core MVP` P-HMM-3; intended label `Feature`; parent fallback at `/opt/data/le31-daily-research-2026-09-29.linear-fallback.json`)
> **Status:** defer (parking-lot, vocabulary reference; zero build time today)
> **Bucket:** v1 (reconciliation-architecture-reference)
> **Trigger condition:** the first v1 PR that proposes a reconciliation surface, a nightly-reconciliation report, a variance-resolution surface, or a doctrine-governed business-rules layer.

## Seven-check gate verdict

| Gate item | Verdict | Evidence |
|---|---|---|
| 1. License (charter §3.2) | **PASS** — MIT ✓ STRICTLY-COMPATIBLE | parent-verified GitHub API direct-GET 2026-09-29: `license.spdx_id = "MIT"` |
| 2. Stack fit (charter §3.1 + Python) | **PASS** — Python + type-safe + reconciliation-first | description verbatim: *"Doctrine-governed, type-safe, asset-class-agnostic Python framework for institutional post-trade operations - custody, settlement, reconciliation, securities lending"* |
| 3. Customer-facing AI (charter §3.4) | **NOT TRIGGERED** — owner-facing reconciliation reports only | description contains no AI/LLM references; reconciliation surface is owner-facing only |
| 4. Stars (signal) | **PASS** — 1★ (modest signal) | parent-verified GitHub API direct-GET: `stargazers_count = 1`, `watchers_count = 1` |
| 5. In-window (≤7 days) | **PASS** — by `pushed_at` (2026-09-28T19:55:45Z) | parent-verified: `created_at = 2026-06-21T02:23:57Z` is OUT-OF-WINDOW but `pushed_at` is in-window |
| 6. LE31-shape-fit | **PASS** — type-safe + reconciliation-first vocabulary | the only in-window 2026 Python repo combining doctrine-governed + type-safe + asset-class-agnostic + reconciliation-first primitives |
| 7. No observed pain | **DEFER** — no LE31 owner pain (v1 has no reconciliation surface) | the artifact is vocabulary-only; trigger condition requires explicit owner/charter sign-off |
| **Final verdict** | **defer (parking-lot)** — vocabulary reference only | per le31-daily-research/SKILL.md hard rule "do not fabricate" + charter §3.1 invariant (v1 surface expansion requires explicit owner/charter sign-off) |

## Files to touch (when triggered)

If a future v1 PR is triggered by the trigger condition above, the implementation would touch:
1. `backend/app/models/custody_record.py` (new file) — SQLModel schema for the `custody_record` table
2. `backend/app/models/settlement_record.py` (new file) — SQLModel schema for the `settlement_record` table
3. `backend/app/models/reconciliation_record.py` (new file) — SQLModel schema for the `reconciliation_record` table
4. `backend/app/services/reconciliation.py` (new file) — reconciliation engine that derives the reconciliation report from `StockEntry` + `Order` + `OrderItem` schemas
5. `backend/app/services/doctrine.py` (new file) — doctrine-governed business rules layer
6. `backend/app/routers/reconciliation.py` (new file) — FastAPI router for the `/reconcile` + `/variance` + `/custody` endpoints
7. `backend/app/bots/cook_bot.py` (modify) — add `/reconcile` + `/variance` + `/custody` commands
8. `backend/app/services/audit_logs.py` (modify) — record every reconciliation run as an `audit_logs` entry
9. `tests/test_reconciliation.py` (new file) — pytest tests for the reconciliation engine
10. `tests/test_doctrine.py` (new file) — pytest tests for the doctrine-governed business rules layer
11. `docs/reconciliation.md` (new file) — owner documentation for the reconciliation surface

## Verification protocol reference

Per `verification-protocol/SKILL.md` (LE31 charter §3.5): every PR must pass:
1. `make test` — pytest full suite
2. `make lint` — ruff + mypy strict
3. `make type-check` — mypy --strict on all backend/app/**/*.py
4. `make smoke` — docker-compose up + curl health check
5. Manual: run `/reconcile last-24h` → verify reconciliation report is generated → verify variance is computed correctly → verify custody matches settlement within tolerance

## Rollback path

1. `git revert <commit-sha>` — single-commit revert
2. Drop the new tables (`custody_record`, `settlement_record`, `reconciliation_record`) — these are additive-only, no data loss
3. Remove the `/reconcile` + `/variance` + `/custody` commands from the cook-bot — `git revert <cook-bot-commit-sha>`
4. Remove the doctrine layer — `rm backend/app/services/doctrine.py`

## Mandatory LE31 skill list

When the coding agent starts work on this feature, the load MUST consult these skills in order:
1. `le31-conventions` — project conventions + git workflow
2. `le31-v1-feature-pattern` — v1 feature contract template
3. `le31-coding-agent-brief` — paste-in prompt template
4. `development` — full development pipeline (specify → plan → tasks → implement)
5. `speckit-implement` — task execution protocol
7. `pre-merge-review` — independent review before merge

## Notes on the trigger

LE31 v1 today does NOT have a reconciliation surface. The `StockEntry` ledger records prep-item quantities + manual adjustments but does NOT yet do formal reconciliation against supplier invoices or nightly POS-sales totals. The reconciliation surface would:
- Run a nightly reconciliation report (e.g., at 02:00 every day)
- Compare custody (what we have) vs settlement (what was sold) for each asset
- Compute the variance (custody_total - settlement_total)
- Record the variance + variance_reason in the `reconciliation_record` table
- Surface the variance to the owner via the cook-bot + the `/reconcile` + `/variance` + `/custody` commands
- Handle variance-resolution: if variance > threshold, alert the owner + record the alert in `audit_logs`

This is a substantial v1 surface expansion that requires explicit owner/charter sign-off per charter §3.1 invariant. The defer artifact documents the *vocabulary* so the next owner review can scope it properly.

## Out of scope reminder

The artifact is vocabulary-only. Do NOT:
- Implement the reconciliation surface today
- Add new dependencies (the LE31 v1 stack is sufficient; no new deps required for vocabulary-only)
- Modify any v1 SQLModel schema (the reconciliation surface would ADD new tables, not modify existing ones)
- Modify any v1 FastAPI router (the reconciliation surface would ADD a new router, not modify existing ones)
- Modify any v1 aiogram bot handler (the reconciliation surface would ADD new commands to the cook-bot, not modify existing commands)
- Modify the audit_logs table (the reconciliation surface would RECORD entries in audit_logs, not modify its structure)
- Modify the StockEntry table
- Introduce any customer-facing AI surface (charter §3.4 explicit invariant)
- Introduce any v2 horizontal-expansion surface (charter §3.1 + §3.2 invariant)

If any of the above is requested, escalate to the owner for explicit charter §3.1 sign-off before any code change.