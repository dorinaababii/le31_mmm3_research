# HANDOFF — 323-movsarusumov172-crypto-KitchenQ

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-10-15
**Active feature path**: `/opt/data/le31_mmm3_research/features/323-movsarusumov172-crypto-KitchenQ-mit-realtime-restaurant-ordering-waiter-kitchen-hall-screens-websocket-stoplist-table-bills-daily-report-fastapi-sqlite-python-v1-tiny-fastapi-websocket-crossover-restaurant-stack-shape-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v1 does not need to *use* `movsarusumov172-crypto/KitchenQ`; the LE31 v1 surface has features 02 (waiter order-taking) + 09 (kitchen delay visibility) + 23 (sse-cook-channel) + 03 (kitchen stock tracker) for the relevant operator surfaces, but no *real-time-3-operator-screens-over-WebSocket + per-table-stop-list + running-table-bill* surface today; the peer value is *v1 cross-section vocabulary for a future v1 PR that adds a real-time-floor-view surface*, not *adoption*.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the `movsarusumov172-crypto/KitchenQ` GitHub repo (MIT, **0★ / 0⑂**, **43 KB tiny**, language Python ✓ ON-STACK + FastAPI + SQLite + WebSocket + vanilla-JS, **pushed 2026-10-11T17:00:26Z AND created 2026-10-11T17:00:20Z = IN-WINDOW BY BOTH FIELDS**, by `movsarusumov172-crypto`) as a dated, in-window **structural-evidence peer** for LE31's potential v1 *real-time-floor-view + per-table-stop-list + running-table-bill + daily-report* surface.

If the trigger condition (LE31 first proposes a v1 surface that wants *real-time-3-operator-screens-over-WebSocket* OR *per-table-stop-list-propagation-in-real-time* OR *running-table-bill-via-WebSocket* OR *daily-report-via-WebSocket*-at-midnight primitives, OR a future owner decision questions whether feature 02 `order-taking` + feature 23 `sse-cook-channel` should be extended to cover the *real-time-floor-view* dimension with WebSocket) is met, the external coding agent should:

1. Load this artifact and the parent daily-brainstorm report (`/opt/data/le31-brainstorm-2026-10-15.md`).
2. Load the `KitchenQ` repo: `https://github.com/movsarusumov172-crypto/KitchenQ` — README + `KitchenQ/` source if available.
3. Load the companion features 02 (waiter order-taking) + 03 (kitchen stock tracker) + 09 (kitchen delay visibility) + 23 (sse-cook-channel) — all currently use polling or SSE; the *real-time-3-operator-screens-over-WebSocket* shape would extend these.
4. Re-run the LE31 feature gate with `KitchenQ`'s README in hand.
5. **Decide whether the proposed v1 surface benefits from `KitchenQ`'s WebSocket-3-operator-screens framing**. If the v1 surface wants *real-time-floor-view* or *per-table-stop-list-propagation-in-real-time*, `KitchenQ` is purpose-built for that use case (small). If the v1 surface only wants to extend the existing feature 02 waiter-tip-capture, `KitchenQ` adds no value.
6. **If `KitchenQ` is proposed for adoption**: pin to a specific version, add to `requirements-kitchenq.txt` (do not pin to v1 yet), and add a single test WebSocket-push call against a single `Visit` from the LE31 owner-side. Compare against the existing LE31 polling-HTML approach. If the test WebSocket-push adds sub-second-latency-waiter-floor-view, propose a v1 extension to feature 02; if not, document the comparison and defer.
7. **If `KitchenQ` is not adopted**: document the comparison and defer. No charter §3.1 change is needed because `KitchenQ` is a 43-KB real-time-WebSocket library, not a stack change.
8. **Pilot on one real-Visit first**. Do not adopt `KitchenQ` project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/323-movsarusumov172-crypto-KitchenQ-...md`
- **Parent daily-brainstorm report**: `/opt/data/le31-brainstorm-2026-10-15.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-15/gh_topic_restaurant_python.json` (where `KitchenQ` is listed; parent-verified raw JSON has `stargazers_count=0`, `forks_count=0`, `license.spdx_id=MIT`, `pushed_at=2026-10-11T17:00:26Z`, `created_at=2026-10-11T17:00:20Z`, `description="Real-time restaurant ordering: waiter, kitchen and hall screens over WebSocket with a stop-list, table bills and a daily report."`, `size=43`, `topics=[fastapi, python, realtime, restaurant, sqlite, vanilla-js, websocket]`)
- **`KitchenQ` repo**: `https://github.com/movsarusumov172-crypto/KitchenQ` (parent-fetched 2026-10-15 metadata; verify-via-direct-GitHub-API-GET at `/tmp/le31-brainstorm-2026-10-15/verify/ghverify__parent_movsarusumov172-crypto_KitchenQ.json`)
- **Companion artifacts**:
  - `features/02-order-taking.md` (the existing v1 waiter-side ordering surface that `KitchenQ` would extend with WebSocket)
  - `features/03-kitchen-stock-tracker.md` (the stop-list-item event already implemented as a `StockEntry` schema)
  - `features/09-kitchen-delay-visibility.md` (the existing cook-side Telegram bot that `KitchenQ` would extend with a kitchen-screen Web app)
  - `features/22-MhlG67-grid-table-manager-...md` (the prior v1 cross-section reference that uses WebSocket-over-HTTP for live-floor-updates — sister-shape)
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.6 money-invariants + integer-minor-units + per-order-attribution).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Verification protocol reference

- **Read-back protocol**: parent-re-parse the raw `/tmp/le31-brainstorm-2026-10-15/gh_topic_restaurant_python.json` JSON to confirm `full_name=movsarusumov172-crypto/KitchenQ` + `stargazers_count=0` + `forks_count=0` + `license.spdx_id=MIT` + `pushed_at=2026-10-11T17:00:26Z` + `created_at=2026-10-11T17:00:20Z` + `description = "Real-time restaurant ordering: waiter, kitchen and hall screens over WebSocket with a stop-list, table bills and a daily report."` + `size=43` + `topics=[fastapi, python, realtime, restaurant, sqlite, vanilla-js, websocket]`.
- **GitHub canonical read**: GET `https://api.github.com/repos/movsarusumov172-crypto/KitchenQ` (HTTP 200; parent-verified 2026-10-15; raw JSON at `/tmp/le31-brainstorm-2026-10-15/verify/ghverify__parent_movsarusumov172-crypto_KitchenQ.json`).
- **Anti-fabrication canary**: `grep -lF 'movsarusumov172-crypto/KitchenQ'` across `/opt/data/le31_mmm3_research/features/*.md` = 0 matches outside this feature file (parent-verified).
- **Distinct-from-features**: ripgrep-verified `KitchenQ` against features 1–322 = only this feature 323.

## Rollback path

This defer artifact is fully reversible:
- **Delete the feature file**: `rm /opt/data/le31_mmm3_research/features/323-movsarusumov172-crypto-KitchenQ-...md`.
- **Delete the HANDOFF**: `rm /opt/data/le31_mmm3_research/specs/323-movsarusumov172-crypto-KitchenQ-...-HANDOFF.md`.
- **No code change was made today**, so no rollback of code is required.
- **No database migration was made today**, so no rollback of schema is required.
- **No pin change was made today** (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1).
