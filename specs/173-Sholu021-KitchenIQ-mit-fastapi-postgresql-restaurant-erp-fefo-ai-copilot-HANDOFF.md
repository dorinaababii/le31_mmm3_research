# HANDOFF — Feature 173: `Sholu021-KitchenIQ-mit-fastapi-postgresql-restaurant-erp-fefo-ai-copilot`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/173-Sholu021-KitchenIQ-mit-fastapi-postgresql-restaurant-erp-fefo-ai-copilot.md` — defer/parking-lot (Pick A of Brainstorm 2026-09-14, parent research issue HMM-249).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Charter §3.1 (explicit state transitions) | ✓ | KitchenIQ `Inventory Ledger + FEFO + Batch Management + Expiry Tracking` is the §3.1 explicit-state-transitions primitive applied to inventory with batch-level granularity; LE31 v1 already implements this in `StockEntry` for single-batch-per-item |
| 2 | Charter §3.2 (permissive license) | ✓ | MIT |
| 3 | Charter §3.4 (no customer-facing AI) | ✓ | KitchenIQ AI is owner/manager-side (`AI Copilot + AI Insights + Demand Forecasting + Automatic Reordering`); no guest-facing AI in the README; no waiter ordering, no menu recommendation for guests — §3.4-compatible (owner/staff-assist AI allowed; customer-facing AI forbidden) |
| 4 | In-window by `pushed_at` | ✓ | pushed 2026-09-14T06:55:15Z (within 30-day window 2026-08-15..2026-09-14) |
| 5 | Ripgrep-verified unique vs features/ 1..172 | ✓ | no existing feature covers the *FastAPI + SQLAlchemy 2.0 + PostgreSQL + Alembic + Inventory Ledger + FEFO + Approval Workflow + owner-side AI Copilot* stack-shape |
| 6 | Cross-section with ≥1 existing feature | ✓ | features 3/5/7/16/19/26/28/61/165 |
| 7 | Defer verdict (parking-lot, no code change) | ✓ | 0★ + 89-day-old repo + first in-window push today + single-maintainer + Next.js frontend vs LE31 minimal-HTML frontend + no code adoption → no code today; the *stack-shape validation* is the value |

**Gate verdict**: **defer (parking-lot)** — 7/7 gate checks pass, but the build verdict is `defer` because the code is not adoptable (single-maintainer + brand-new in-window push + Next.js frontend stack mismatch + no code adoption opportunity).

## Bucket

**v1** (operator-surface inspiration) — the *stack-shape* is the value, not the code. The verbatim tech-stack (FastAPI + SQLAlchemy 2.0 + PostgreSQL + Alembic + APScheduler + JWT Auth) is **byte-for-byte the LE31 stack** plus a frontend-framework (Next.js + React, which LE31 v1 does not use).

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds a FEFO/batch-level tracking surface, or first v2 PR that introduces an owner-side AI Copilot surface), the implementation would not require a code change for the existing LE31 v1 surface — the existing `StockEntry` schema already implements the append-only discipline. The HANDOFF is to evaluate whether the v1 FEFO/batch-level tracking surface or the v2 owner-side AI Copilot surface is the right product-wedge for the next v1/v2 PR.

**For v1 FEFO/batch-level tracking** (if approved):
1. Add a `batch_id` column to the `StockEntry` table (Alembic migration).
2. Add a `FEFO` helper function in `app/stock/fefo.py` that returns the oldest-batch-first inventory for a given `MenuItem`.
3. Update feature 3 (`kitchen-stock-tracker`) + feature 26 (`reorder-point-on-stockentry`) + feature 28 (`shelf-threshold-receiving-bot`) + feature 34 (`stockout-prep-board-snapshot`) to use the FEFO helper.
4. No new feature file needed; this is an incremental enhancement to the existing append-only `StockEntry` schema.

**For v2 owner-side AI Copilot** (if approved):
1. Add an `ai_copilot` module to the v2 surface at `app/ai/copilot.py`.
2. Wire it to the OpenAI API (or a self-hosted model) with the LE31 `audit_logs` + `StockEntry` as context.
3. Enforce the **§3.4 owner-side-AI primitive**: every AI suggestion must be reviewable by the owner before any state mutation; the AI is a *summariser*, not an *actor*.
4. New feature file at `features/NNN-ai-copilot-owner-side-OwnerAIDailyRecap.md` (NOT this defer artifact).

## Verification protocol

1. `git clone https://github.com/Sholu021/KitchenIQ` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/Sholu021/KitchenIQ/main/README.md` (parent-verified 2026-09-14; the README is the source of truth for the verbatim tech-stack + feature list).
3. `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN" "https://api.github.com/repos/Sholu021/KitchenIQ"` for star count, fork count, license, language, pushed_at, created_at, topics (parent-verified 2026-09-14).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the FEFO helper + the AI Copilot module changes are isolated to the expected files.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v1/v2 trigger fires and the implementation lands:
- For v1 FEFO: rollback = `alembic downgrade -1` to drop the `batch_id` column; the `FEFO` helper is a no-op when `batch_id IS NULL`, so the existing single-batch-per-item behavior is preserved.
- For v2 AI Copilot: rollback = remove the `app/ai/copilot.py` module; the AI integration is additive, not destructive.

## Mandatory LE31 skill list

When (and only when) the future v1/v2 trigger fires, the coding agent MUST load these skills before starting:

- `development` (router for all coding work)
- `le31-v1-feature-pattern` (existing LE31 v1 feature implementation pattern)
- `le31-handoff-spec` (HANDOFF contract reader/writer)
- `le31-coding-agent-brief` (paste-in prompt from slice contract)
- `speckit-implement` (verify tasks in order)

## Bucket project

**`le31 Research`** (parent research issue HMM-249) — the sub-issue for this feature lives in `le31 Research` (where the parent research issue lives), NOT in `le31 v1 — Core MVP`. Reason: the project `le31 v2 owner-pains` (which the original SKILL.md expected) **does not exist** in this workspace; the verified workspace contains only `le31 v1 — Core MVP`, `le31 Workflow`, and `le31 Research`. Per the verified-2026-08-28 skill note: *"For a v2-bucket pick, attach the sub-issue to `le31 Research` (where the parent research issue lives) and say so in the report."*

(Note: this pick is bucket=v1, not v2, but the parent research issue lives in `le31 Research` so the sub-issue is co-located there. If the future v1 trigger fires and the FEFO/batch-level tracking surface lands, the implementation PR targets `le31 v1 — Core MVP`; the feature research sub-issue stays in `le31 Research`.)

## Why this is a `defer`

The KitchenIQ repo is 0★, 89-day-old, with first in-window push today. The single-maintainer cadence + the Next.js/React frontend stack mismatch + the OpenAI integration (LE31 v1 has no AI charter scope) make code adoption impractical. The *value* is the stack-shape validation — the verbatim FastAPI + SQLAlchemy 2.0 + PostgreSQL + Alembic + Inventory Ledger + FEFO + Approval Workflow + AI Copilot tech-stack is the LE31 stack plus a frontend-framework, and the demand-signal is independent confirmation that this stack-shape is the right one for the restaurant domain. No build time today; the value is the persistent cross-section reference + the named *stack-shape match* primitive for any future v1 PR that adds FEFO/batch-level tracking or any future v2 PR that introduces owner-side AI Copilot.
