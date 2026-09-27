# HANDOFF — Feature 240: `huoyunpili-xiaomaipu-apache-2-0-fish-shop-backend-order-workbench-payment-arrangement-supplier-coordination-local-video-evidence-per-order-profit-accounting-django-self-hosted-v1-smb-order-management-per-order-profit-reference`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/240-huoyunpili-xiaomaipu-apache-2-0-fish-shop-backend-order-workbench-payment-arrangement-supplier-coordination-local-video-evidence-per-order-profit-accounting-django-self-hosted-v1-smb-order-management-per-order-profit-reference.md` — defer/parking-lot (Pick B of Brainstorm 2026-09-27, parent research issue will be recorded as linear: blocked with fallback JSON at `/opt/data/le31-brainstorm-2026-09-27.linear-fallback.json`).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Charter §3.1 (explicit state transitions) | ✓ | Pick B's *order-state-changes* are operator-driven via the *order-workbench*; the *local-video-evidence* is the *evidence-on-write* primitive; no implicit state change |
| 2 | Charter §3.2 (permissive license) | ✓ | Apache-2.0 permissive; §3.2 STRICTLY-COMPATIBLE |
| 3 | Charter §3.4 (no customer-facing AI) | ✓ | Pick B has no AI surface; the *per-order-profit-accounting* is a deterministic arithmetic calculation, not customer-facing AI |
| 4 | In-window by `created_at` AND `pushed_at` | ✓ | created 2026-09-17T16:03:51Z + pushed 2026-09-23T03:23:46Z; IN-WINDOW BY BOTH FIELDS |
| 5 | Ripgrep-verified unique vs features/ 1..238 | ✓ | parent-verified via `grep -l -i 'huoyunpili\|xiaomaipu' features/*.md` → 0 matches |
| 6 | Cross-section with ≥1 existing feature | ✓ | features 39 + 57 + 74 + 75 + 82 + 205 via the *owner-side-profit-accounting + per-order-audit-trail* cluster |
| 7 | Defer verdict (parking-lot, no code change today) | ✓ | 0★ + 10-day-old repo + first in-window push today + no observed LE31 pain + the *per-order-profit-accounting + local-video-evidence + supplier-coordination-delivery* posture is a vocabulary reference, not a build-need today |

**Gate verdict**: **defer (parking-lot)** — 7/7 gate checks pass, but the build verdict is `defer` because the artifact is vocabulary-only (the *per-order-EUR-profit + local-video-evidence* posture is a v1/v2 future reference, not a v1 build-need today).

## Bucket

**v1 SMB-order-management-with-per-order-profit reference** — the *per-order-profit-accounting + local-video-evidence + supplier-coordination-delivery* posture is the value, not the code. The verbatim Chinese description (订单工作台、回款安排、供货商协作发货与本地视频留证、售后追款、逐单利润核算) is the vocabulary primitive; LE31 v1's `payment-tip-reconciliation` (feature 05) tracks *tip-amount + tip-attribution* but does NOT implement *per-order-EUR-profit-attribution* with *evidence-on-write*.

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that proposes a *per-order-EUR-profit-attribution* surface; first v1 PR that proposes a *supplier-delivery-evidence* surface), the implementation would not require a code change for the existing LE31 v1 surface — the existing `payment-tip-reconciliation` (feature 05) already implements the *tip-amount + tip-attribution* discipline. The HANDOFF is to evaluate whether the v1 *per-order-EUR-profit-attribution* surface or the v1 *supplier-delivery-evidence* surface is the right product-wedge for the next v1 PR.

**For v1 per-order-EUR-profit-attribution** (if approved):
1. Add a `per_order_profit` table to the LE31 v1 schema (Alembic migration) with columns `order_profit_id, visit_id, order_eur_revenue, order_eur_cogs, order_eur_fixed_cost_allocation, order_eur_profit, profit_calculated_at`. Use `Numeric(10, 2)` (Postgres `decimal`) for all EUR columns per charter §3.5 *never-use-binary-floats* invariant.
2. Add a `per_order_profit_calculator` module at `app/profit/calculator.py` that computes the per-order-EUR-profit from the order's revenue + cogs + fixed-cost-allocation.
3. Wire the per-order-profit-calculator to the existing FastAPI app via a FastAPI dependency.
4. Add a *profit-status* endpoint to the existing FastAPI app at `GET /api/v1/orders/{order_id}/profit` that returns the per-order-EUR-profit breakdown.
5. Update the existing waiter-web-UI to display the per-order-EUR-profit in the order-detail view.
6. No new feature file needed; this is an incremental enhancement to the existing `payment-tip-reconciliation` (feature 05) surface.

**For v1 supplier-delivery-evidence** (if approved):
1. Add a `local_video_evidence` table to the LE31 v1 schema (Alembic migration) with columns `video_id, delivery_id, video_file_path, video_recorded_at, video_duration_seconds, supplier_name, delivery_status`. Apply charter §3.7 *store only data needed for restaurant operations* + *videos of supplier-deliveries only, not customer-behavior* scope.
2. Add a `local_video_recorder` module at `app/evidence/video_recorder.py` that records a video of the supplier-delivery and saves it to a configured local-storage path.
3. Wire the local-video-recorder to the existing aiogram-bot (cook-bot per charter §3.1) via an aiogram handler that triggers the recording when the cook confirms a supplier-delivery-receipt.
4. New feature file at `features/NNN-supplier-delivery-evidence-v1.md` (NOT this defer artifact).

## Verification protocol

1. `git clone https://github.com/huoyunpili/xiaomaipu` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/huoyunpili/xiaomaipu/main/README.md` (parent-verified 2026-09-27; the README is the source of truth for the verbatim Chinese description + the 7 named topics).
3. `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN" "https://api.github.com/repos/huoyunpili/xiaomaipu"` for star count, fork count, license, language, pushed_at, created_at, topics (parent-verified 2026-09-27; Apache-2.0 ✓, 0★/0⑂, Python, pushed 2026-09-23T03:23:46Z, created 2026-09-17T16:03:51Z, 14754 KB, 7 topics, archived=False).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the per-order-profit-calculator + local-video-recorder changes are isolated to the expected files.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v1 trigger fires and the implementation lands:
- For v1 per-order-EUR-profit-attribution: rollback = `alembic downgrade -1` to drop the `per_order_profit` table; the *per_order_profit_calculator* module is additive, not destructive; the existing `payment-tip-reconciliation` (feature 05) continues to work without the per-order-profit-attribution surface.
- For v1 supplier-delivery-evidence: rollback = `alembic downgrade -1` to drop the `local_video_evidence` table; the *local_video_recorder* module is additive, not destructive; the existing supplier-orders (feature 16) continues to work without the supplier-delivery-evidence surface.

## Mandatory LE31 skill list (load these first)

Before authoring or reviewing any code derived from this HANDOFF, load these skills in order:

1. `skills/le31-conventions/SKILL.md` — the seven-check feature gate, charter invariants, and conflict-resolution rules.
2. `skills/le31-v1-feature-pattern/SKILL.md` — the existing v1 feature template + style guide.
3. `skills/le31-daily-research/SKILL.md` — the daily-research cron contract + source-families pattern.
4. `skills/le31-handoff-spec/SKILL.md` — the slice-contract template + verification-protocol reference.
5. `skills/le31-coding-agent-brief/SKILL.md` — the paste-in prompt for the coding agent.

The coding agent must NOT author code without all 5 skills loaded.