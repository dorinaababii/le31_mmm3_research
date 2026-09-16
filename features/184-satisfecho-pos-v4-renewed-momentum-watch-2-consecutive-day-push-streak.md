# Feature 184 — `satisfecho-pos-v4-renewed-momentum-watch-2-consecutive-day-push-streak` (defer)

> **NEW observation (2026-09-16).** 4th filing of GitHub repo `satisfecho/pos` (AGPL-3.0 ⚠, **44★/14⑂**, Python (Django) + TypeScript, **99942 KB = ~98 MB substantial repo**, **`pushed_at` 2026-09-16T05:09:07Z = 2nd-consecutive-day NEW PUSH** (was 2026-09-15T06:32:52Z yesterday), `updated_at` 2026-09-15T20:52:00Z = metadata-only movement). Description (verbatim): *"Restaurant POS and ordering — self-hosted, multi-tenant, real-time. Menu, tables, reservations, Stripe+Revolut payment, kitchen display, reports."* Today's filing documents **+1★/24h AND −1⑂/24h AND 2nd-consecutive-day NEW PUSH** = **strongest sustained-active maintainer development signal on this repo in the 48-pass series**. Bucket: **v1 watch-list (defer, parking-lot)** — watch-list defer. AGPL-3.0 still **BLOCKS** LE31 v1 import per charter §3.2 (carried over from 2026-08-19). Charter §3.4 not triggered (no AI integration). Zero build time today. Distinct from features 40, 42 (pre-AGPL-discovery) and feature 180 (single-day NEW PUSH).

## Goal

Retain the **2-consecutive-day NEW PUSH streak (09-15 + 09-16) + +1★/24h AND −1⑂/24h delta** as a persistent cross-section reference for the strongest sustained-active maintainer development signal in the 48-pass series. The artifact is the watch-list observation + the structural-evidence data point that LE31 v1's maintenance cycle can be measured against. AGPL-3.0 still **blocks** LE31 v1 import per charter §3.2; structural-evidence observation only. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **2-consecutive-day NEW PUSH streak** (09-15 + 09-16) — the first sustained-active maintainer development pattern since the August-burst quiesced on 2026-08-22.
- A written record of the **+1★ AND −1⑂ delta** — the **1st starred-up-while-forked-down delta** in this repo's history (43→44★, 15→14⑂). Two interpretations: (a) *organic-discovery of new users + retention-decline of inactive forks*; (b) *repo-cleanup event*. Recommend direct observation (not over-interpretation).
- A written record of the **size correction**: today confirmed 99942 KB = ~98 MB substantial repo (was 340+ KB on 09-15 = parent was using cached/stale size datum; today's direct-GET shows the actual size).
- A decision record: today's verdict is `defer` because AGPL-3.0 explicitly blocks LE31 v1 import per charter §3.2; the watch-list observation provides structural-evidence data only.
- A cross-section reference with prior satisfecho/pos filings: features 40, 42 (pre-AGPL-discovery), feature 180 (post-AGPL-discovery single-day NEW PUSH).

**Out of scope (defer artifact):**
- Any change to LE31 v1's waiter web UI or cook Telegram bot.
- Any change to LE31 v1's `audit_logs` schema or `StockEntry` invariant.
- Adoption of the satisfecho/pos codebase (AGPL-3.0 explicitly blocks).
- Cross-pollination with charter §3.4 AI surface (no AI integration in satisfecho/pos).
- Comparison with features 89 (devnest-hq/r-mgmt JS-not-Python) and 119 (Ritchalison/BalanceDesk NOASSERTION) — both are watch-list neighbors but have different blockers.

## Evidence / JTBD

When a future LE31 maintainer asks *"how often should LE31 v1 push code? what is the maintainer-activity calibration for a self-hosted multi-tenant restaurant POS in 2026?"*, the owner wants *a data point from a peer repo with the closest LE31-shape surface*, but struggles because *most watch-list POS repos are either JS-not-Python (feature 89) or AGPL-blocked (this pick) or NOASSERTION-license (feature 119)*, so that *the maintainer can calibrate LE31 v1's maintenance cycle against a peer with a *clean* LE31-shape surface, AGPL-block or not*.

- **Evidence class**: observed (the satisfecho/pos direct-GET data points + the 2-consecutive-day NEW PUSH streak are directly verifiable).
- **Confidence**: high for the streak observation; medium for the interpretation of the +1★ AND −1⑂ delta (two competing interpretations).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 doesn't exist yet; the v1 maintainer activity will be measured against peer repos once LE31 v1 ships.
- **The value is calibration, not direct demand**: when LE31 v1's maintenance cycle is reviewed, the satisfecho/pos 2-consecutive-day burst is a ready-made *peer calibration* data point.

## Description

GitHub `satisfecho/pos` (AGPL-3.0 ⚠, 44★/14⑂, Python (Django) + TypeScript, 99942 KB = ~98 MB substantial repo, `pushed_at` 2026-09-16T05:09:07Z = 2nd-consecutive-day NEW PUSH, `updated_at` 2026-09-15T20:52:00Z = metadata-only movement).

Description (verbatim): *"Restaurant POS and ordering — self-hosted, multi-tenant, real-time. Menu, tables, reservations, Stripe+Revolut payment, kitchen display, reports."*

Topics (verbatim): `[angular, docker, docker-compose, fastapi, kitchen-display-system, multi-tenant, open-source, point-of-sale, pos-system, postgresql, python, redis, restaurant-management, restaurant-management-system, restaurant-pos, saas, self-hosted, stripe, typescript, websocket]`

**Watch-list significance:**

### Observation: 2-consecutive-day NEW PUSH streak (09-15 + 09-16)

The repo pushed code on both 2026-09-15T06:32:52Z and 2026-09-16T05:09:07Z. This is the **strongest sustained-active maintainer development signal** on this repo in the 48-pass series:
- **5-push-in-30h burst** from 2026-08-19..2026-08-21 (August burst) → **24-day quiescence** (2026-08-22 to 2026-09-14) → **2-consecutive-day burst** on 09-15 + 09-16 (current cycle).
- The 2-consecutive-day burst is the **first sustained-active maintainer development pattern since the August burst quiesced on 2026-08-22**.
- Recommend follow-up direct-GET in 3 days (2026-09-19) to confirm whether the burst continues or quiesces.

### Observation: +1★ AND −1⑂ delta

The 24-hour delta is 43→44★ (star-floor growth) AND 15→14⑂ (fork-floor decay). This is the **1st starred-up-while-forked-down delta** in this repo's history. Two competing interpretations:
- (a) *organic-discovery of new users (stars up) + retention-decline of inactive forks (forks down)* — typical of a project gaining mainstream attention while losing hobbyist fork-cloners.
- (b) *repo-cleanup event* — the maintainer deleted inactive fork-references in the burst cycle (a `git push --prune` or equivalent).

Recommend **direct observation (not over-interpretation)** until the burst cycle completes.

### Observation: Size correction (340+ KB → 99942 KB = ~98 MB)

Today's direct-GET confirms the size is **99942 KB = ~98 MB** substantial repo. The 340+ KB datum in feature 180 was a parent-cached/stale size; today's direct-GET shows the actual size. The size growth from 09-15's 340+ KB to today's 99942 KB is *mostly* the size datum correction; the 2-consecutive-day NEW PUSH cycle may have added code but not 98 MB of code.

## Data model

**No v1 data model change.** This is a watch-list observation.

## Implementation steps

**None today.** Watch-list defer, structural-evidence observation only.

## Telegram interaction if any

**None today.** The repo is not LE31-relevant at the code level (AGPL blocks).

## Dependencies

- **Charter §3.1 invariant compatibility**: ✓ (no charter violation; this is an external observation).
- **§3.2 license compatibility**: ⚠ AGPL-3.0 explicitly **BLOCKS** LE31 v1 import.
- **§3.4 AI compatibility**: ✓ not triggered (no AI integration).
- **Stack compatibility**: ✓ not triggered (no adoption).

## Open questions

1. **Is the 2-consecutive-day burst the start of a sustained-active cycle or a one-off?** Recommend a follow-up direct-GET in 3 days (2026-09-19) to confirm whether the burst continues or quiesces.
2. **Why is the AGPL-3.0 license blocking adoption?** Per charter §3.2, AGPL is incompatible with LE31 v1's single-restaurant self-hosted model (the AGPL viral-copyleft would force LE31 users who fork the system to release their changes under AGPL, which is incompatible with the operator's ability to keep their menu prices private). This was documented in feature 40 (the pre-AGPL-discovery filing) and is not in question.
3. **What value is there in continuing to observe this repo?** Structural-evidence observation: the AGPL-block does not prevent LE31 from *learning* from satisfecho/pos's architecture. The strongest cross-section learning value today is the **2-consecutive-day NEW PUSH pattern** = a signal of active-maintainer development, which is exactly the property LE31 v1 should aim for in its own maintenance cycle.

## Why this matters

This pick **maintains the watch-list discipline** for the highest-stars Python POS peer in the productive query space. The AGPL-block prevents code adoption, but the watch-list observation provides:
1. **Maintainer-activity calibration** — LE31 v1's maintenance cycle can be measured against the satisfecho/pos burst/quiescence pattern.
2. **Architecture-evolution signal** — features in satisfecho/pos's NEW PUSH cycles (kitchen display, multi-tenant, self-hosted, Stripe+Revolut payment) are the closest direct LE31-stack-shape peers in the productive query space; tracking the burst cycles tells LE31 which features are landing in the maintained Python POS ecosystem.
3. **JTBD validation** — the sustained-active maintainer development pattern (after the August-burst quiescence) is itself a JTBD signal: there *is* sustained demand for a self-hosted multi-tenant restaurant POS, and satisfecho/pos is the closest LE31-shape peer filling that demand.

The pick is **fully reversible** (watch-list observation only) and **does not trigger any v1 work**.

Companion artifacts: features 40, 42 (pre-AGPL-discovery filings), feature 180 (post-AGPL-discovery single-day NEW PUSH), features 89 (devnest-hq/r-mgmt) and 119 (Ritchalison/BalanceDesk) — watch-list neighbors. Parent research issue HMM-259 (Research 2026-09-16 — daily).
