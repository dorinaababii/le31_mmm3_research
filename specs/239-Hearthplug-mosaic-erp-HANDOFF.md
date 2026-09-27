# HANDOFF — Feature 239: `Hearthplug-mosaic-erp-mit-free-open-source-retail-erp-small-shops-customized-plain-english-interview-self-hosted-accounting-odoo-alternative-tally-alternative-v1-small-shop-pos-inventory-erp-reference`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/239-Hearthplug-mosaic-erp-mit-free-open-source-retail-erp-small-shops-customized-plain-english-interview-self-hosted-accounting-odoo-alternative-tally-alternative-v1-small-shop-pos-inventory-erp-reference.md` — defer/parking-lot (Pick A of Brainstorm 2026-09-27, parent research issue will be recorded as linear: blocked with fallback JSON at `/opt/data/le31-brainstorm-2026-09-27.linear-fallback.json`).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Charter §3.1 (explicit state transitions) | ✓ | Pick A's *plain-English-interview-as-configuration-mechanism* posture is operator-driven configuration; the *small-shop-ERP + odoo-alternative + tally-alternative* posture is a vocabulary reference, not a code change |
| 2 | Charter §3.2 (permissive license) | ✓ | MIT permissive; §3.2 STRICTLY-COMPATIBLE |
| 3 | Charter §3.4 (no customer-facing AI) | ✓ | Pick A has no AI surface; the *plain-English-interview* is deterministic operator-driven configuration, not customer-facing AI |
| 4 | In-window by `created_at` AND `pushed_at` | ✓ | created 2026-09-17T12:59:38Z + pushed 2026-09-27T03:13:49Z = TODAY push; IN-WINDOW BY BOTH FIELDS |
| 5 | Ripgrep-verified unique vs features/ 1..238 | ✓ | parent-verified via `grep -l -i 'hearthplug\|mosaic-erp' features/*.md` → 0 matches |
| 6 | Cross-section with ≥1 existing feature | ✓ | features 158 + 195 + 201 + 205 + 218 + 221 + 224 + 225 + 238 via the *small-business-ERP + inventory-management* cluster |
| 7 | Defer verdict (parking-lot, no code change today) | ✓ | 0★ + 10-day-old repo + first in-window push today + no observed LE31 pain + the *odoo-alternative + tally-alternative + plain-English-interview* posture is a vocabulary reference, not a build-need today |

**Gate verdict**: **defer (parking-lot)** — 7/7 gate checks pass, but the build verdict is `defer` because the artifact is vocabulary-only (the *small-shop-ERP-horizontal-expansion* is a v2 future reference, not a v1 build-need today).

## Bucket

**v1 small-shop-POS-inventory-ERP reference** — the *small-shop-ERP + odoo-alternative + tally-alternative + plain-English-interview* posture is the value, not the code. The verbatim description (`Free open-source retail ERP for small shops. Customized ERP. No custom developer required - set up by a plain-English interview.`) is the vocabulary primitive; LE31 v1 is a single-restaurant-vertical product, not a small-shop-ERP-horizontal product.

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that proposes an *operator-driven-configuration-mechanism* for the waiter-web-UI surface; first v2 PR that proposes a *multi-shop-support* surface), the implementation would not require a code change for the existing LE31 v1 surface — the existing `StockEntry` schema already implements the append-only discipline. The HANDOFF is to evaluate whether the v1 *operator-driven-configuration-mechanism* surface or the v2 *multi-shop-support* surface is the right product-wedge for the next v1/v2 PR.

**For v1 operator-driven-configuration-mechanism** (if approved):
1. Add a `plain_english_interview` table to the LE31 v1 schema (Alembic migration) with columns `interview_id, shop_id, question, answer, captured_at`.
2. Add a `plain_english_parser` module at `app/config/plain_english.py` that parses free-form English operator input into structured configuration directives.
3. Update the existing waiter-web-UI to expose a *plain-English-interview* configuration surface.
4. No new feature file needed; this is an incremental enhancement to the existing waiter-web-UI.

**For v2 multi-shop-support** (if approved):
1. Add a `shop` table to the LE31 v1 schema (Alembic migration) with columns `shop_id, shop_name, shop_type, accounting_currency, plain_english_config`.
2. Add a `multi_shop_router` module at `app/shops/router.py` that routes operator-requests to the correct shop based on shop-id.
3. Wire the multi-shop-router to the existing FastAPI app via a FastAPI dependency.
4. New feature file at `features/NNN-multi-shop-support-v2.md` (NOT this defer artifact).

## Verification protocol

1. `git clone https://github.com/Hearthplug/mosaic-erp` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/Hearthplug/mosaic-erp/main/README.md` (parent-verified 2026-09-27; the README is the source of truth for the verbatim description + the 10 named topics).
3. `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN" "https://api.github.com/repos/Hearthplug/mosaic-erp"` for star count, fork count, license, language, pushed_at, created_at, topics (parent-verified 2026-09-27; MIT ✓, 0★/0⑂, Python, pushed 2026-09-27T03:13:49Z = TODAY, created 2026-09-17T12:59:38Z, 6366 KB, 10 topics, archived=False).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the plain-English-interview + multi-shop-router changes are isolated to the expected files.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v1/v2 trigger fires and the implementation lands:
- For v1 plain-English-interview: rollback = `alembic downgrade -1` to drop the `plain_english_interview` table; the *plain_english_parser* module is additive, not destructive; the existing waiter-web-UI continues to work without the plain-English-interview surface.
- For v2 multi-shop-support: rollback = `alembic downgrade -1` to drop the `shop` table; the *multi_shop_router* module is additive, not destructive; the existing single-shop-vertical FastAPI app continues to work without the multi-shop-router.

## Mandatory LE31 skill list (load these first)

Before authoring or reviewing any code derived from this HANDOFF, load these skills in order:

1. `skills/le31-conventions/SKILL.md` — the seven-check feature gate, charter invariants, and conflict-resolution rules.
2. `skills/le31-v1-feature-pattern/SKILL.md` — the existing v1 feature template + style guide.
3. `skills/le31-daily-research/SKILL.md` — the daily-research cron contract + source-families pattern.
4. `skills/le31-handoff-spec/SKILL.md` — the slice-contract template + verification-protocol reference.
5. `skills/le31-coding-agent-brief/SKILL.md` — the paste-in prompt for the coding agent.

The coding agent must NOT author code without all 5 skills loaded.