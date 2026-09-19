# 202 — fjcloudaiconsulting/ziftbook Apache-2.0 small-business SaaS + multi-tenant + i18n + cloudflare-workers + no-account + 3-tap HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 Apache-2.0 small-business SaaS deployment-topology question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/202-fjcloudaiconsulting-ziftbook-apache-appointment-booking-fastapi-nextjs-postgresql-multi-tenant-saas-small-business-cloudflare-workers-i18n.md` (defer artifact; **no code today**).

Bucket: **v1 architecture-reference (Apache-2.0 small-business SaaS operator-tooling primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintainer asks *'if v1 introduces a multi-tenant SQLModel relationship, an i18n FastAPI template surface, or a Cloudflare Workers deployment, what is the Apache-2.0 small-business SaaS deployment-topology discipline that preserves the existing v1 single-tenant + on-premise + French-only charter §3.1 invariants?'*, the maintainer wants *evidence that another independent 2026 Python repo at 808 KB with Apache-2.0 + both fields in-window + 7-day-old fresh repo + small-business + multi-tenant + i18n + cloudflare-workers + fastapi + postgresql + salon/appointment-booking is shipping the *small-business + no-account + 3-tap* vocabulary as the canonical 2026 small-business SaaS operator-tooling surface*, but struggles because *v1 has no documented multi-tenant + i18n + cloudflare-workers primitive in the charter*, so that *v1 can introduce the multi-tenant + i18n + edge-deployment extensions with the explicit Apache-2.0 small-business SaaS vocabulary rather than inventing a new one*." **PASS** (zero-pain today; v1 has no multi-tenant + i18n + cloudflare-workers trigger; the JTBD is primitive vocabulary extension + Apache-2.0 strictly-adoptable posture + multi-tenant + i18n + cloudflare-workers future-extension documentation, not a build-need). |
| 2 | **Viability** | Owner can read 808 KB repo description + 14 topic tags + Apache-2.0 license + multi-tenant + i18n + cloudflare-workers vocabulary? Yes. No code change required. **PASS** (informational only; vocabulary + deployment-topology-reference artifact). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 today. Confidence: high for the multi-tenant + i18n + cloudflare-workers + Apache-2.0 small-business SaaS vocabulary (Apache-2.0 + Python + 808 KB substantial + 7-day-old fresh repo + both fields in-window + explicit multi-tenant + i18n + cloudflare-workers topic set + small-business + saas topic set); medium-high for *adoption* in the *vocabulary + deployment-topology* sense (Apache-2.0 explicitly enables *import-and-extend* of the multi-tenant + i18n + cloudflare-workers deployment-topology, but the salon/appointment-booking business-logic is off-domain). Stack: FastAPI + PostgreSQL backend = on-pattern for v1 primitives; Next.js + TypeScript frontend = off-pattern for v1 (LE31 v1 uses HTMX not Next.js); Apache-2.0 license = on-pattern for code adoption (§3.2 STRICTLY-COMPATIBLE); salon/appointment-booking business-logic = off-pattern for LE31 (LE31 is restaurant-POS, not salon-booking). Practicability of adoption: high for vocabulary + deployment-topology reference; low for code (off-domain business-logic). **PASS** (posture validation only; adoption is v1 question). |
| 4 | **Conflict** | None. The Apache-2.0 small-business SaaS octuple (small-business + saas + multi-tenant + i18n + cloudflare-workers + fastapi + postgresql + nextjs) maps onto LE31's existing 3-of-8 (small-business + saas + fastapi + postgresql match directly; multi-tenant + i18n + cloudflare-workers are future-extension vocabulary; nextjs is off-pattern for v1's HTMX posture). Charter §3.2 explicitly targets the *self-hosted small-business operator-tooling* posture (ziftbook is a *direct match* for this invariant). Charter §3.1 explicitly says single-tenant + on-premise + French-only (multi-tenant + i18n + cloudflare-workers are OFF-PATTERN for v1 but ON-PATTERN for v2 future-extension). §3.4 (no AI surface). Charter §3.1 + §3.2 + §3.4 explicitly aligned (with multi-tenant + i18n + cloudflare-workers as future-extension vocabulary, not v1 changes). **PASS**. |
| 5 | **Outcome, appetite, scope** | v1 architecture-reference (Apache-2.0 small-business SaaS + multi-tenant + i18n + cloudflare-workers + no-account + 3-tap booking vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 808 KB repo + 14 topic tags + Apache-2.0 license posture + multi-tenant + i18n + cloudflare-workers vocabulary (1 hour). **Cost-to-value ratio: high** (808 KB is substantial + Apache-2.0 enables *vocabulary + deployment-topology* adoption; only the *multi-tenant + i18n + cloudflare-workers + no-account + 3-tap* vocabulary + the 7-day-old fresh-repo signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/202-fjcloudaiconsulting-ziftbook-apache-appointment-booking-fastapi-nextjs-postgresql-multi-tenant-saas-small-business-cloudflare-workers-i18n-HANDOFF.md` and `features/202-fjcloudaiconsulting-ziftbook-apache-appointment-booking-fastapi-nextjs-postgresql-multi-tenant-saas-small-business-cloudflare-workers-i18n.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + Apache-2.0 strictly-adoptable posture + multi-tenant + i18n + cloudflare-workers future-extension documentation for the next v1 deployment-topology moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a multi-tenant SQLModel relationship, an i18n FastAPI template surface, or a Cloudflare Workers deployment):

- `app/models/tenant.py` — possibly add (the SQLModel table for the multi-tenant primitive; depends on the v1 change).
- `app/models/order.py` + `app/models/bill.py` + `app/models/payment.py` + `app/models/stock_entry.py` + `app/models/audit_log.py` — possibly modify to add `tenant_id` FK to `tenant` SQLModel table (the multi-tenant primitive; depends on the v1 change).
- `app/middleware/tenant_isolation.py` — possibly add (the FastAPI middleware that filters all queries by the current-request's `tenant_id`; depends on the v1 change).
- `app/i18n/strings.json` + `app/i18n/loader.py` — possibly add (the i18n string-table + i18n-aware Jinja2 template loader; depends on the v1 change).
- `app/deploy/cloudflare_workers.py` — possibly add (the Cloudflare Workers adapter; depends on the v1 change).
- `tests/test_multi_tenant_isolation.py` — possibly add (the integration test for the multi-tenant primitive; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/202-fjcloudaiconsulting-ziftbook-apache-appointment-booking-fastapi-nextjs-postgresql-multi-tenant-saas-small-business-cloudflare-workers-i18n.md` exists and is read back by the parent.
- [ ] `specs/202-fjcloudaiconsulting-ziftbook-apache-appointment-booking-fastapi-nextjs-postgresql-multi-tenant-saas-small-business-cloudflare-workers-i18n-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `ziftbook` description is quoted verbatim (808 KB repo).
- [ ] The 0★/0⑂ + Apache-2.0 §3.2 STRICTLY-COMPATIBLE + Python + 808 KB substantial + 7-day-old fresh repo + both fields in-window + small-business + multi-tenant + i18n + cloudflare-workers + fastapi + postgresql + nextjs + saas + salon + appointment-booking + booking + scheduling topic set + no-account + 3-tap booking vocabulary is documented.
- [ ] The charter §3.1 single-tenant + on-premise + French-only alignment + the multi-tenant + i18n + cloudflare-workers future-extension vocabulary is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds a multi-tenant SQLModel relationship, an i18n FastAPI template surface, or a Cloudflare Workers deployment lands):**
- [ ] The PR is read back by the parent.
- [ ] The `ziftbook` Apache-2.0 small-business SaaS + multi-tenant + i18n + cloudflare-workers + no-account + 3-tap vocabulary is evaluated against the PR's changes: does the change address the *multi-tenant + i18n + cloudflare-workers future-extension triple* discipline? Does the change preserve the *small-business + saas + Apache-2.0 octuple* posture? Does the change preserve the *charter §3.1 single-tenant + on-premise + French-only* invariant (if the change is v1) or *acknowledge the v2 multi-tenant + i18n + cloudflare-workers future-extension* (if the change is v2)?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the `app/models/tenant.py` SQLModel table; remove the `tenant_id` FK from `app/models/order.py` + `app/models/bill.py` + `app/models/payment.py` + `app/models/stock_entry.py` + `app/models/audit_log.py`; remove the `app/middleware/tenant_isolation.py` FastAPI middleware; remove the `app/i18n/strings.json` + `app/i18n/loader.py` i18n files; remove the `app/deploy/cloudflare_workers.py` Cloudflare Workers adapter; restore the original schemas.
- Migration cost: depends on the v1 change; the multi-tenant + i18n + cloudflare-workers vocabulary is *additive architecture* (the `Tenant` SQLModel table is *added on top of* the existing v1 surfaces; the `tenant_id` FK on existing tables is *additive*; the FastAPI middleware is *new* middleware; the i18n files are *new* files; the Cloudflare Workers adapter is *new* deploy code; no v1 surface is *removed*).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `Order` + `Bill` + `Payment` + `StockEntry` tables retain all rows; the new `Tenant` SQLModel table is *new* data, not a schema change; the verification log is a *new* document, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:

1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.
