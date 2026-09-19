# Feature 202 — `fjcloudaiconsulting-ziftbook-apache-appointment-booking-fastapi-nextjs-postgresql-multi-tenant-saas-small-business-cloudflare-workers-i18n` (defer)

> **NEW observation (2026-09-19).** Documents in-window GitHub repo `fjcloudaiconsulting/ziftbook` (**Apache-2.0 ✓** (`spdx_id: 'Apache-2.0'` in raw JSON), **0★/0⑂**, Python, **pushed 2026-09-18T05:22:39Z** (yesterday, in-window by `pushed_at` only), **created 2026-09-12T17:09:08Z** (7-day-old fresh repo, in-window by `created_at` — *both* fields in-window, **7-day-old fresh repo = the freshest in-window candidate today**), **808 KB substantial repo**, default_branch=`main`). Topics (verbatim from raw JSON): `appointment-booking, booking, cloudflare-workers, fastapi, i18n, multi-tenant, nextjs, postgresql, python, saas, salon, scheduling, small-business, typescript`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-19, truncated at the GitHub API 200-char cap): *"Appointment booking for small service businesses. Clients book in three taps with no account, and owners manage their calendar, confirmations, deposits and cancellations. Available in English, Dutch a…"* The **Apache-2.0 small-business SaaS operator-tooling primitive** + the **multi-tenant + i18n + cloudflare-workers + fastapi + postgresql + nextjs + saas + small-business** octuple primitive: this is the **ONLY strictly-adoptable pick of today's 3** (Apache-2.0 = §3.2 STRICTLY-COMPATIBLE for both vocabulary AND code adoption); the **small-business + no-account + multi-tenant + i18n** quadruple is the *operator-tooling* surface pattern. The `cloudflare-workers` topic is the **edge-deployment primitive** (Cloudflare Workers = a serverless edge compute platform with a free tier; LE31 v1 currently does not deploy to Cloudflare). The `i18n` topic is the **internationalization primitive** (LE31 v1 currently does not have an i18n surface — *vocabulary future-extension*). The `multi-tenant` topic is the **multi-tenancy primitive** (LE31 v1 is single-tenant; *multi-tenant* = the future v2 SaaS variant that LE31 v1 explicitly does not target today). The `fastapi + postgresql + nextjs` topic triple is the **LE31 v1 backend+frontend stack mirror** (the TypeScript + Next.js frontend is *off-pattern* for LE31 v1's HTMX-server-side-rendering posture, but the *FastAPI + PostgreSQL* backend primitive IS on-pattern). The `small-business + saas` topic pair is the **small-business SaaS operator-tooling surface** (LE31 v1 is exactly a small-business SaaS; charter §3.2 explicitly targets the *self-hosted small-business operator-tooling* posture). The `salon` topic is the *salon/appointment-booking vertical* (NOT restaurant; *cross-section with restaurant* via the *small-business + appointment-booking* primitive). No AI surface so charter §3.4 is not applicable. Bucket: **v1 architecture-reference (Apache-2.0 small-business SaaS operator-tooling primitive, parking-lot defer)** — vocabulary + multi-tenant + i18n + cloudflare-workers + Apache-2.0 strictly-adoptable primitive documentation, zero build time today.

## Goal

Retain the **"Appointment booking for small service businesses. Clients book in three taps with no account, and owners manage their calendar, confirmations, deposits and cancellations. Available in English, Dutch a…"** cross-section architectural vocabulary + **small-business + no-account + multi-tenant + i18n** quadruple as the persistent v1 architecture reference for any future LE31 v1 maintainer asking the *Apache-2.0 small-business SaaS deployment* question (does LE31 v1 ever need to deploy to Cloudflare Workers, support i18n, or scale to multi-tenant?). The artifact is the persistent *Apache-2.0 small-business SaaS operator-tooling primitive* + the *multi-tenant + i18n + cloudflare-workers* future-extension triple as a *named* v1 architectural reference. The Apache-2.0 license makes this the **ONLY strictly-adoptable pick of today's 3** — the codebase can be referenced as a v1 *architecture-reference* (not a v1 dependency; LE31 has different domain logic) or as a v1 *deployment-topology-reference* (the Cloudflare Workers + i18n + multi-tenant triple). No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `ziftbook` cross-section vocabulary: the **ONLY Apache-2.0 strictly-adoptable pick of today's 3 picks** (Apache-2.0 = §3.2 STRICTLY-COMPATIBLE for both vocabulary AND code adoption); the **first in-window Apache-2.0 small-business + multi-tenant + i18n + cloudflare-workers + fastapi + postgresql Python repo of the 51-pass series**.
- A written record of the **Apache-2.0 small-business SaaS operator-tooling primitive**: the *small-business + SaaS + Apache-2.0 + multi-tenant + i18n + no-account* quintuple — the *operator-tooling* surface pattern. LE31 v1 is exactly a small-business SaaS (charter §3.2 explicitly targets the *self-hosted small-business operator-tooling* posture); `ziftbook` is the **only strictly-adoptable external 2026 evidence** that the *small-business + SaaS + Apache-2.0 + multi-tenant + i18n* discipline is current 2026 demand.
- A written record of the **multi-tenant + i18n + cloudflare-workers** future-extension triple: (a) `multi-tenant` = a *tenant-isolation discipline* in the SQLModel + alembic stack; (b) `i18n` = a *localization discipline* in the FastAPI template + Telegram bot surface; (c) `cloudflare-workers` = a *serverless edge-deployment discipline* (Cloudflare Workers = a serverless edge compute platform with a free tier; LE31 v1 currently deploys via FastAPI on a single VPS, NOT edge-deployment). LE31 v1 is **explicitly single-tenant + on-premise + French-only** in charter §3.1; the *multi-tenant + i18n + cloudflare-workers* triple is a **future-extension vocabulary** for LE31 v2.
- A written record of the **no-account + 3-tap booking** primitive: the *clients-book-in-three-taps-with-no-account* pattern = a *friction-free-client-booking* discipline. The phrase *no account* names the **anonymous-booking primitive** (clients book without creating an account; the booking record is keyed by phone-number or email, not by user-account). The phrase *three taps* names the **friction-minimization primitive** (3 user actions from landing-page to booking-confirmation: tap-time-slot + tap-confirm + tap-pay-or-deposit). LE31 v1 has no booking surface today but the *no-account + 3-tap* pattern is the *friction-minimization vocabulary* for any future v1 client-facing surface.
- A written record of the **Apache-2.0 license as the §3.2 strictly-compatible posture**: the codebase CAN be adopted as a library (Apache-2.0 = §3.2 STRICTLY-COMPATIBLE for *import-and-extend*); but the *salon/appointment-booking* domain is off-domain for LE31 (LE31 is restaurant-POS, not salon-booking), so the **vocabulary + deployment-topology** is the value, not the *salon-business-logic adoption*.
- A decision record: today's verdict is `defer (parking-lot)` because the *Apache-2.0 small-business SaaS + multi-tenant + i18n + cloudflare-workers* octuple is a v1 architecture reference, not a v1 build implication. v1 is single-tenant + on-premise + French-only today; the *multi-tenant + i18n + cloudflare-workers* triple documents the *future-extension vocabulary* for the next v1 maintainer.

**Out of scope (defer artifact):**
- Any change to the LE31 v1 schema (no `tenant_id` field on SQLModel tables today; no multi-tenant primitive; no i18n surface).
- Any change to the waiter web UI (HTMX) or cook Telegram bot.
- Adoption of the `ziftbook` code as a v1 dependency in the *business-logic* sense (the salon/appointment-booking domain is off-domain for LE31 restaurant-POS; the codebase cannot be directly adopted). The *Apache-2.0 license posture* explicitly enables *vocabulary reference + architecture-reference adoption* (the *multi-tenant + i18n + cloudflare-workers* triple IS on-pattern for any future v1 deployment-topology extension).
- Any change to the `audit_logs` table or `StockEntry` ledger today.
- Any new dependency on the `fjcloudaiconsulting` maintainer.

## Evidence / JTBD

When a future LE31 v1 maintainer asks *"if v1 introduces a multi-tenant SQLModel relationship, an i18n FastAPI template surface, or a Cloudflare Workers deployment, what is the Apache-2.0 small-business SaaS deployment-topology discipline that preserves the existing v1 single-tenant + on-premise + French-only charter §3.1 invariants?"*, the maintainer wants *evidence that another independent 2026 Python repo at 808 KB with Apache-2.0 + both fields in-window + 7-day-old fresh repo + small-business + multi-tenant + i18n + cloudflare-workers + fastapi + postgresql + salon/appointment-booking is shipping the *small-business + no-account + 3-tap* vocabulary as the canonical 2026 small-business SaaS operator-tooling surface*, but struggles because *v1 has no documented multi-tenant + i18n + cloudflare-workers primitive in the charter*, so that *v1 can introduce the multi-tenant + i18n + edge-deployment extensions with the explicit Apache-2.0 small-business SaaS vocabulary rather than inventing a new one*.

- **Evidence class**: observed (the `ziftbook` description explicitly names *"Appointment booking for small service businesses. Clients book in three taps with no account, and owners manage their calendar, confirmations, deposits and cancellations"* + the topic set `multi-tenant + i18n + cloudflare-workers + fastapi + postgresql + nextjs + saas + small-business` = the *Apache-2.0 small-business SaaS operator-tooling primitive + multi-tenant + i18n + cloudflare-workers* triple).
- **Confidence**: high for the multi-tenant + i18n + cloudflare-workers vocabulary (Apache-2.0 + Python + 808 KB substantial + 7-day-old fresh repo + both fields in-window + explicit multi-tenant + i18n + cloudflare-workers topic set + small-business + saas topic set); medium-high for *adoption* in the *vocabulary + deployment-topology* sense (the Apache-2.0 license explicitly enables *import-and-extend* of the multi-tenant + i18n + cloudflare-workers deployment-topology, but the salon/appointment-booking business-logic is off-domain).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + Apache-2.0 strictly-adoptable posture documentation + multi-tenant + i18n + cloudflare-workers future-extension documentation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + Apache-2.0 strictly-adoptable posture + multi-tenant + i18n + cloudflare-workers future-extension documentation**: when (if) LE31 v1 introduces a multi-tenant SQLModel relationship, an i18n surface, or a Cloudflare Workers deployment, the *Apache-2.0 small-business SaaS + multi-tenant + i18n + cloudflare-workers* octuple vocabulary is documented.

## Description

GitHub `fjcloudaiconsulting/ziftbook` (Apache-2.0, 0★/0⑂, Python, pushed 2026-09-18T05:22:39Z, created 2026-09-12T17:09:08Z = *both fields in-window*, **7-day-old fresh repo**, 808 KB substantial repo).

Description (verbatim, parent-verified GitHub API direct-GET 2026-09-19, truncated at the 200-char GitHub API cap): *"Appointment booking for small service businesses. Clients book in three taps with no account, and owners manage their calendar, confirmations, deposits and cancellations. Available in English, Dutch a…"* (the `…` indicates truncation at the GitHub API 200-char cap; the full description likely extends beyond 200 chars with the i18n language list + maybe a tagline; the explicit description carries the *small-business + no-account + 3-tap* vocabulary; the truncated continuation is not load-bearing for the primitive).

Topics (verbatim from raw JSON): `appointment-booking, booking, cloudflare-workers, fastapi, i18n, multi-tenant, nextjs, postgresql, python, saas, salon, scheduling, small-business, typescript`.

The **Apache-2.0 small-business SaaS operator-tooling octuple** (one of the *4 themes* in today's 3 picks):

| `ziftbook` topic/feature | LE31 v1 surface | Match status |
|---|---|---|
| `small-business` (topic) | charter §3.2 self-hosted small-business operator-tooling | ✓ direct match |
| `saas` (topic) | charter §3.2 self-hosted SaaS posture | ✓ direct match |
| `multi-tenant` (topic) | (LE31 v1 is single-tenant today; no `tenant_id` field on SQLModel tables) | **★ FUTURE-EXTENSION: LE31 v1 has no multi-tenant primitive; the ziftbook primitive names the multi-tenant future-extension** |
| `i18n` (topic) | (LE31 v1 is French-only today via charter §3.1; no FastAPI i18n template surface) | **★ FUTURE-EXTENSION: LE31 v1 has no i18n primitive; the ziftbook primitive names the i18n future-extension** |
| `cloudflare-workers` (topic) | (LE31 v1 is on-premise VPS deployment today; no Cloudflare Workers edge-deployment) | **★ FUTURE-EXTENSION: LE31 v1 has no edge-deployment primitive; the ziftbook primitive names the edge-deployment future-extension** |
| `fastapi` (topic) | FastAPI 0.141.1 | ✓ direct match |
| `postgresql` (topic) | PostgreSQL via SQLModel 0.0.42 | ✓ direct match |
| `nextjs` + `typescript` (topic) | (LE31 v1 uses HTMX + minimal HTML, NOT Next.js + TypeScript) | **★ STACK-MISMATCH: LE31 v1 uses HTMX-server-side-rendering on FastAPI; the ziftbook stack uses Next.js + TypeScript server-side-rendering on FastAPI** |
| `salon` (topic — appointment-booking vertical) | (LE31 v1 is restaurant-POS, NOT salon-booking) | **★ DOMAIN-MISMATCH: ziftbook's salon-booking business-logic is off-domain; the *small-business + no-account + 3-tap* pattern is on-domain** |
| `appointment-booking` + `booking` + `scheduling` (topic — the 3 booking-disciplines) | (LE31 v1 has no booking surface today; *cross-section with future reservation surface* via feature 201's 7-surfaces vocabulary) | **★ CROSS-SECTION: ziftbook's appointment-booking patterns are the *external 2026 evidence* for any future v1 reservation-bot surface (cross-section with feature 201's `Reservation` SQLModel table + reservation-bot Telegram surface)** |

The **no-account + 3-tap booking primitive**: the *clients-book-in-three-taps-with-no-account* pattern = a *friction-free-client-booking* discipline. The phrase *no account* names the **anonymous-booking primitive** (clients book without creating an account; the booking record is keyed by phone-number or email, not by user-account). The phrase *three taps* names the **friction-minimization primitive** (3 user actions from landing-page to booking-confirmation: tap-time-slot + tap-confirm + tap-pay-or-deposit). LE31 v1 has no booking surface today but the *no-account + 3-tap* pattern is the *friction-minimization vocabulary* for any future v1 client-facing surface (e.g. a future reservation-bot).

The **Apache-2.0 license as the §3.2 strictly-compatible posture**: the codebase CAN be adopted as a library (Apache-2.0 = §3.2 STRICTLY-COMPATIBLE for *import-and-extend*); but the *salon/appointment-booking* domain is off-domain for LE31 (LE31 is restaurant-POS, not salon-booking), so the **vocabulary + deployment-topology** is the value, not the *salon-business-logic adoption*.

The **multi-tenant + i18n + cloudflare-workers future-extension triple**: (a) `multi-tenant` = a *tenant-isolation discipline* in the SQLModel + alembic stack; (b) `i18n` = a *localization discipline* in the FastAPI template + Telegram bot surface; (c) `cloudflare-workers` = a *serverless edge-deployment discipline*. LE31 v1 is **explicitly single-tenant + on-premise + French-only** in charter §3.1; the *multi-tenant + i18n + cloudflare-workers* triple is a **future-extension vocabulary** for LE31 v2.

## Data model

**No LE31 data model change today.** The defer artifact is documentation only. The multi-tenant future-extension primitive names the *tenant_id* field on SQLModel tables (a future v1 PR adds `tenant_id` FK to `tenant` SQLModel table on every existing table — `Order` + `Bill` + `Payment` + `StockEntry` + `audit_logs`) + a *tenant-isolation middleware* (a FastAPI middleware that filters all queries by the current-request's `tenant_id`). The i18n future-extension primitive names the *FastAPI i18n template surface* (a future v1 PR adds an i18n string-table + an i18n-aware Jinja2 template loader + a `{{ _('key') }}` template helper for translatable strings). The cloudflare-workers future-extension primitive names the *Cloudflare Workers adapter* (a future v1 PR moves the FastAPI app to a Cloudflare Workers-compatible runtime, e.g. via `pyodide` or `cloudflare-workers-python`).

## Implementation steps

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a multi-tenant SQLModel relationship, an i18n FastAPI template surface, or a Cloudflare Workers deployment):

- `app/models/tenant.py` — possibly add (the SQLModel table for the multi-tenant primitive; depends on the v1 change).
- `app/models/order.py` + `app/models/bill.py` + `app/models/payment.py` + `app/models/stock_entry.py` + `app/models/audit_log.py` — possibly modify to add `tenant_id` FK to `tenant` SQLModel table (the multi-tenant primitive; depends on the v1 change).
- `app/middleware/tenant_isolation.py` — possibly add (the FastAPI middleware that filters all queries by the current-request's `tenant_id`; depends on the v1 change).
- `app/i18n/strings.json` + `app/i18n/loader.py` — possibly add (the i18n string-table + i18n-aware Jinja2 template loader; depends on the v1 change).
- `app/deploy/cloudflare_workers.py` — possibly add (the Cloudflare Workers adapter; depends on the v1 change).
- `tests/test_multi_tenant_isolation.py` — possibly add (the integration test for the multi-tenant primitive; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Telegram interaction if any

None today. If a future v1 trigger fires (multi-tenant + i18n + reservation-bot), the Telegram interaction would be a *reservation-bot surface* in the *current-request's tenant_id* (a future v1 PR adds a Telegram bot that handles reservation creation + lookup via Telegram commands like `/reserve <table-id> <time> <party-size>`, scoped to the *current-request's tenant_id*); the cook-bot surface would persist for order-cooking flow; the new reservation-bot would be a *tenant-scoped separate* Telegram bot surface.

## Dependencies

- No new dependency today.
- If a future v1 trigger fires:
  - Schema: `Tenant` SQLModel table + `tenant_id` FK on every existing table + a tenant-isolation middleware.
  - i18n: an i18n string-table + an i18n-aware Jinja2 template loader + a `{{ _('key') }}` template helper for translatable strings.
  - Cloudflare Workers: a Cloudflare Workers adapter (e.g. via `pyodide` or `cloudflare-workers-python`).

## Open questions

- Should LE31 v1 ever introduce a `Tenant` SQLModel table (the *multi-tenant* primitive)?
- Should LE31 v1 ever introduce an i18n FastAPI template surface (the *i18n* primitive)?
- Should LE31 v1 ever migrate to Cloudflare Workers (the *edge-deployment* primitive)?
- Should LE31 v1 ever introduce a reservation-bot Telegram surface (the *booking-disciplines* primitive; cross-section with feature 201's `Reservation` SQLModel table)?
- If yes to any of the above: should the v1 PR cross-reference this feature 202 contract + HANDOFF as the named Apache-2.0 architecture reference?

## Why this matters

The *Apache-2.0 small-business SaaS + multi-tenant + i18n + cloudflare-workers* octuple is the **future-extension vocabulary** that any future LE31 v1 maintainer would adopt as the *canonical future-extension primitive*. LE31 v1 is **explicitly single-tenant + on-premise + French-only** in charter §3.1; the *multi-tenant + i18n + cloudflare-workers* triple is the **future-extension surface area** that LE31 v2 would inherit from v1 (charter §3.2 explicitly targets the *self-hosted small-business operator-tooling* posture; the Apache-2.0 license posture + the multi-tenant + i18n + edge-deployment primitives are the *natural v2 extensions* that preserve the v1 single-tenant + on-premise + French-only invariant).

The **charter §3.2 invariant alignment**: LE31 v1's charter §3.2 says *"self-hosted small-business operator-tooling posture"* — the *small-business + saas + Apache-2.0* triple directly aligns. The *multi-tenant + i18n + cloudflare-workers* future-extension triple is OFF-PATTERN for v1 (charter §3.1 explicitly says single-tenant + on-premise + French-only) but ON-PATTERN for v2 (charter §3.4 mentions v2 as the *operator-tooling extension*).

The **ONLY strictly-adoptable pick today** (Apache-2.0 = §3.2 STRICTLY-COMPATIBLE): this is the **first in-window Apache-2.0 small-business + multi-tenant + i18n + cloudflare-workers + fastapi + postgresql Python repo of the 51-pass series**. The Apache-2.0 license posture enables *architecture-reference adoption* (any future v1 PR that adds a multi-tenant + i18n + cloudflare-workers future-extension cross-references the `ziftbook` *vocabulary + deployment-topology* as the named reference). The *salon/appointment-booking* business-logic is OFF-DOMAIN (LE31 is restaurant-POS, not salon-booking), but the *small-business + no-account + 3-tap + multi-tenant + i18n + cloudflare-workers + Apache-2.0* octuple is ON-DOMAIN.

The **no-AI-surface posture** (no `together-ai` topic, no `ai-agents` topic, no `llm` topic in the topic set) explicitly aligns with charter §3.4 (operator-tooling not customer-facing AI).

Trigger for re-evaluation: first v1 PR that adds a `Tenant` SQLModel table, a `tenant_id` FK on existing tables, an i18n FastAPI template surface, a Cloudflare Workers deployment, or a reservation-bot Telegram surface (cross-section with feature 201).

Trigger for cross-section: first v1 PR that adds a *reservation-bot* Telegram surface (the *Telegram-mediated anonymous-booking primitive* would need to compose with the *no-account + 3-tap booking primitive* from `ziftbook` and with the *7-surfaces vocabulary* + `Reservation` SQLModel table from feature 201).
