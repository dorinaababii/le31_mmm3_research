# HANDOFF — 314-Samarty-1-payout-recon-mit-payment-processor-payout-reconciliation

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-10-13
**Active feature path**: `/opt/data/le31_mmm3_research/features/314-Samarty-1-payout-recon-mit-payment-processor-payout-reconciliation-pos-stripe-grabfood-foodpanda-bank-statement-duckdb-fastapi-v1-payment-processor-payout-reconciliation-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v1 does not need to *use* `Samarty-1/payout-recon`; the LE31 v1 surface has feature 05 `payment-tip-reconciliation` for the waiter-side tip capture, but no *fee-discrepancy-detection* or *bank-deposit-late-detection* surface today; the peer value is *operational vocabulary for a future v1 PR that surfaces payment-processor-payout-discrepancies*, not *adoption*.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the `Samarty-1/payout-recon` GitHub repo (MIT, **0★ / 0⑂**, **28 KB tiny**, language Python ✓ ON-STACK, **pushed 2026-10-10T13:15:51Z AND created 2026-10-10T13:15:45Z = IN-WINDOW BY BOTH FIELDS**, by `Samarty-1` = same author as feature 315 `Samarty-1/fairshift` = sister-pushed same-day-same-hour) as a dated, in-window **structural-evidence peer** for LE31's chosen v1 payment-processor-payout-reconciliation substrate.

If the trigger condition (LE31 first proposes a v1 surface that wants *fee-discrepancy-detection* or *bank-deposit-late-detection* or *double-charge-catching* primitives, OR a future owner decision questions whether feature 05 `payment-tip-reconciliation` should be extended to cover the 4-way-reconciliation dimension) is met, the external coding agent should:

1. Load this artifact and the parent daily-brainstorm report (`/opt/data/le31-brainstorm-2026-10-13.md`).
2. Load the `payout-recon` repo: `https://github.com/Samarty-1/payout-recon` — README + `payout_recon/` source if available.
3. Load the companion feature 293 (`quueli/yookassa-polling-payments`) — both are payment-processor-operations peers; quueli covers `yookassa` polling; payout-recon covers the 4-way reconciliation for Stripe+GrabFood/foodpanda.
4. Re-run the LE31 feature gate with `payout-recon`'s README in hand.
5. **Decide whether the proposed v1 surface benefits from `payout-recon`'s 4-way reconciliation framing**. If the v1 surface wants *fee-discrepancy-detection* or *bank-deposit-late-detection*, `payout-recon` is purpose-built for that use case. If the v1 surface only wants the existing feature 05 waiter-tip-capture, `payout-recon` adds no value.
6. **If `payout-recon` is proposed for adoption**: pin to a specific version, add to `requirements-payout-recon.txt` (do not pin to v1 yet), and add a single test reconciliation call against a single date from the LE31 owner-side `tips_daily` view. Compare against the hand-written equivalent. If the test reconciliation adds fee-discrepancy-detection, propose a v1 extension to feature 05; if not, document the comparison and defer.
7. **If `payout-recon` is not adopted**: document the comparison and defer. No charter §3.1 change is needed because `payout-recon` is a 4-way-reconciliation library, not a stack change.
8. **Pilot on one date first**. Do not adopt `payout-recon` project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/314-Samarty-1-payout-recon-mit-payment-processor-payout-reconciliation-pos-stripe-grabfood-foodpanda-bank-statement-duckdb-fastapi-v1-payment-processor-payout-reconciliation-vocabulary.md`
- **Parent daily-brainstorm report**: `/opt/data/le31-brainstorm-2026-10-13.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-13/gh_creative_topic_small_business_fastapi.json` (where `Samarty-1/payout-recon` is listed; parent-verified raw JSON has `stargazers_count=0`, `forks_count=0`, `license.spdx_id=MIT`, `pushed_at=2026-10-10T13:15:51Z`, `created_at=2026-10-10T13:15:45Z`, `description="Did every order get paid, at the fee you agreed, and did the money reach your bank? Reconciles POS, Stripe, GrabFood/foodpanda payouts and the bank statement (DuckDB, FastAPI)"`, `size=28`, `topics=[accounting, duckdb, fastapi, reconciliation, small-business, stripe]`)
- **`payout-recon` repo**: `https://github.com/Samarty-1/payout-recon` (parent-fetched 2026-10-13 metadata)
- **Companion artifacts**:
  - `features/293-quueli-yookassa-polling-payments-...md` (yookassa-specific payment-processor-operations sister-shape)
  - `features/05-payment-tip-reconciliation-...md` (the existing v1 `payment-tip-reconciliation` surface that `payout-recon` would extend)
  - `features/315-Samarty-1-fairshift-...md` (same-author same-day sister-shape for shift-rostering)
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.6 money-invariants + integer-minor-units + per-order-attribution).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Verification protocol reference

- **Read-back protocol**: parent-re-parse the raw `/tmp/le31-brainstorm-2026-10-13/gh_creative_topic_small_business_fastapi.json` JSON to confirm `full_name=Samarty-1/payout-recon` + `stargazers_count=0` + `forks_count=0` + `license.spdx_id=MIT` + `pushed_at=2026-10-10T13:15:51Z` + `created_at=2026-10-10T13:15:45Z` + `description` = `"Did every order get paid, at the fee you agreed, and did the money reach your bank? Reconciles POS, Stripe, GrabFood/foodpanda payouts and the bank statement (DuckDB, FastAPI)"` + `size=28` + `topics=[accounting, duckdb, fastapi, reconciliation, small-business, stripe]`.
- **GitHub canonical read**: GET `https://api.github.com/repos/Samarty-1/payout-recon` (HTTP 200; parent-verified 2026-10-13).
- **Anti-fabrication canary**: `grep -lF 'Samarty-1/payout-recon'` across `/opt/data/le31_mmm3_research/features/*.md` = 0 matches outside this feature file (parent-verified).
- **Distinct-from-features**: ripgrep-verified `payout-recon` against features 1–313 = only this feature 314 (plus the same-author-pair reference in feature 315).

## Rollback path

This defer artifact is fully reversible:
- **Delete the feature file**: `rm /opt/data/le31_mmm3_research/features/314-Samarty-1-payout-recon-...md`.
- **Delete the HANDOFF**: `rm /opt/data/le31_mmm3_research/specs/314-Samarty-1-payout-recon-...-HANDOFF.md`.
- **No code change was made today**, so no rollback of code is required.
- **No database migration was made today**, so no rollback of schema is required.
- **No pin change was made today** (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1).
