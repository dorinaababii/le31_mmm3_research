# Feature 180 — `satisfecho-pos-v3-renewed-momentum-watch`

**Bucket:** v1 watch-list (defer, parking-lot)
**Filed:** 2026-09-15 by the LE31 daily-research cron
**Source:** Daily Research 2026-09-15, Pick B
**Gate:** PASS (v1 watch-list)

## Goal

Document the renewed-momentum data point on `satisfecho/pos` (the highest in-window Python POS peer at 43★ / 15 forks, AGPL-3.0 ⚠) and capture it as a **watch-list continue** filing that can be cross-referenced from features 40 + 42 (which were filed pre-AGPL-discovery).

## Scope

1. **This is a watch-list continue pick, NOT a build candidate.** No code is written, no contract is sliced, no spec is built.
2. The watch-list entry is renewed today because of the **+2★/24h + +3 forks/24h + NEW PUSH after 7-day push-idle** combo — the strongest single-day movimento on this repo in the 47-pass series.
3. The AGPL-3.0 license **still blocks LE31 v1 import** per charter §3.2 (carried over from 2026-08-19).
4. The pick is **pure structural-evidence observation** — the maintainer is shipping code, the stars/forks are flowing, but LE31 cannot adopt the code.

## Out of scope

1. Any code adoption from `satisfecho/pos`. The AGPL-3.0 license **explicitly blocks** LE31 v1 import per charter §3.2.
2. Any mirror / fork of `satisfecho/pos` for internal use. The AGPL-3.0 obligation to publish source under the same license applies to any derivative work.
3. Any AI integration. Charter §3.4 not triggered.
4. Any new v1 surface. This is a v2 owner-pains watch-list entry (technically the repo addresses the restaurant-POS JTBD but LE31 v1 is Telegram + htmx + FastAPI, not Django; the cross-section is structural, not direct).

## Description

`Satisfecho/pos` is the **highest in-window Python POS peer** in the LE31 watch-list. Today's direct-GET (verified by parent against `/tmp/le31-daily-2026-09-15/gh_repo_satisfecho_pos.json`):

- **Stars: 43** (was 41 on 09-14 — +2★/24h)
- **Forks: 15** (was 12 on 09-14 — +3 forks/24h, **largest single-day fork delta** observed)
- **`pushed_at`: 2026-09-15T06:32:52Z** (= NEW PUSH INSIDE THE FETCH WINDOW, 24h before today's 06:31:32Z fetch)
- **`updated_at`: 2026-09-14T12:06:14Z** (metadata-only movement)
- **License: AGPL-3.0 ⚠** (still blocks LE31 v1 import per charter §3.2)
- **Language: Python (Django)**
- **Size: 340+ KB**
- **Description:** *"Restaurant POS and ordering — self-hosted, multi-tenant, real-time. Menu, tables, reservations, Stri..."*
- **Stars/fork ratio: 2.87** (vs 3.42 on 09-14 = slight inflow toward forks; consistent with sustained JTBD pull being absorbed as a *template*, not just a destination).

The **NEW PUSH after 7-day push-idle** is the most concrete maintainer-active signal since the August-burst (2026-08-19..21 = 5 pushes in 30h, then long quiescence). Today's push is the **first maintainer-active code push since 2026-09-07** (the previous push was the "maintainer-signal" push from 2026-08-19).

Cross-reference: **features 40 + 42 were filed pre-AGPL-discovery (before 2026-08-19) and never updated to flag the AGPL-block**; this pick (feature 180) is the **first filing to carry the AGPL-block + renewed-momentum combo in a single doc**. Recommend updating features 40 + 42 to cross-reference feature 180 on the next pass that opens them for edit.

## Data model

**No data model change.** Watch-list entry only.

## Implementation

1. **No implementation today.** This is a watch-list continue pick; the discipline is "document the data point and move on."
2. **Recommended follow-up actions (next-pass TODO, not blocking today):**
   - Open features 40 + 42 and append a line: *"Cross-reference: see feature 180 for the post-AGPL-discovery renewed-momentum data point (2026-09-15 NEW PUSH + +2★/24h + +3 forks/24h)."*
   - Direct-GET `satisfecho/pos` again in 3 days (2026-09-18) to confirm whether the 2026-09-15 NEW PUSH was a one-off or the start of a renewed maintainer-active cycle.
3. **No code, no commit.** This pick is a documentation entry only.

## Telegram interaction

None. This is a backend watch-list entry; no Telegram-side change.

## Dependencies

1. **`Satisfecho/pos` direct-GET watch** — the repo data point is verified by the parent against the raw GitHub JSON in `/tmp/le31-daily-2026-09-15/gh_repo_satisfecho_pos.json`. The next-pass follow-up direct-GET (3-day rule) requires the GitHub API + Bearer auth from `/opt/data/.env`.
2. **No LE31 stack changes.** The watch is observation-only.

## Open questions

1. **Should the watch-list stay open indefinitely, or should it close after a sustained-quiet period?** The current rule is "open while maintainer-active (push in last 30 days) OR sustained star/fork inflow (≥5★ in last 30 days)". Today both criteria are satisfied (push TODAY + 5★/30-day inflow). Recommend keep-open with 3-day follow-up to confirm.
2. **Should the AGPL-block be retroactively applied to features 40 + 42 + the multiple watch-list filings between 2026-08-19 and today?** Yes, but not blocking; a one-line append to each feature is sufficient. Recommend doing this in the next pass.
3. **Does LE31 have any contingency plan if the maintainer switches the license to MIT/Apache-2.0?** No. The watch is conditional on the maintainer's license choice; if the license flips to permissive, a follow-up pick should be filed to *evaluate* the import, not assume it.

## Why this matters

`Satisfecho/pos` is the **best structural-evidence data point in the LE31 watch-list for the *restaurant-POS JTBD pull*** — even with the AGPL-block, the data is valuable because:
- **Sustained JTBD pull** (43★ + 15 forks + renewed maintainer activity) confirms that *someone* is actively building in this space, which validates the LE31 charter's restaurant-tech focus.
- **Django + multi-tenant + real-time + menu + tables + reservations + Stripe** is the *complete feature surface* of a restaurant POS; LE31's Telegram + htmx + FastAPI surface is intentionally minimal (single-restaurant, no multi-tenant, no Stripe), but the data confirms that the *underlying JTBD* (a self-hosted restaurant operations platform) is real.
- **The AGPL-block demonstrates charter §3.2's value** — without the §3.2 privacy/license discipline, LE31 would be tempted to mirror the repo and inherit the AGPL obligation; with §3.2 in place, the watch-list discipline prevents that mistake.

The renewed-momentum data point (today's NEW PUSH + +2★/24h + +3 forks/24h) is the **single most actionable observation of the 47-pass series for the watch-list as a whole** — it tells us that *the maintainer is shipping code*, the *JTBD pull is being absorbed as a template (forks > stars growth)*, and the *AGPL-block is the right call*. This is exactly the kind of evidence the watch-list is designed to capture.
