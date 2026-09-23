# 223 — psb684-sketch/athena v2-small-business-erp-horizontal-vocabulary-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 small-business-ERP-horizontal-expansion question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/223-psb684-sketch-athena-mit-erp-inventory-management-small-business-python-sqlite-business-automation-v2-small-business-erp-horizontal-vocabulary-reference.md` (defer artifact; **no code today**).

Bucket: **v2 small-business-ERP-horizontal-vocabulary-reference (ERP + inventory-management + small-business + Python + SQLite, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a small-business-ERP-horizontal-expansion surface (expansion from a single-restaurant-vertical product to a small-business-ERP-horizontal product that supports multiple vertical-business-types, or expansion to a standalone-inventory-management product, or expansion to a standalone-business-process-management product), what is the *ERP + inventory-management + small-business + Python + SQLite* vocabulary that preserves the existing v1 single-restaurant-vertical posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 426 KB with 1★/0⑂ + MIT permissive license + 6 topics + in-window-by-both-fields is shipping the *ERP + inventory-management + small-business + Python + SQLite* primitive as the v2 small-business-ERP-horizontal-expansion discipline*, but struggles because *v1 has no documented small-business-ERP-horizontal-expansion primitive in the charter*, so that *v2 can introduce the small-business-ERP + inventory-management + business-automation vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no small-business-ERP-horizontal-expansion trigger; the JTBD is primitive vocabulary extension + ERP + inventory-management + small-business + Python + SQLite documentation, not a build-need; **cross-section JTBD value is moderate** — the only of today's 3 picks that is in-window by BOTH `created_at` AND `pushed_at` = the freshest discovery of the 55-pass brainstorm series' cross-app-signals section). |
| 2 | **Viability** | Maintainer can read 426 KB repo description + 6-topic vocabulary + ERP + inventory-management + small-business + Python + SQLite sextuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *ERP + inventory-management + small-business + Python + SQLite* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the MIT-permissive code; LE31 v1 has no small-business-ERP-horizontal-expansion surface today). Confidence: medium for the *ERP + inventory-management + small-business + Python + SQLite* vocabulary (1★/0⑂ + MIT permissive license + 6 topics + in-window-by-both-fields + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *ERP + inventory-management* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the integrated-business-process-management dimension*; the *small-business + Python + SQLite* discipline IS the *single-tenant + embedded-database posture* applied to the deployment-formalization dimension). Stack: FastAPI + SQLModel + PostgreSQL backend = on-pattern for v1 primitives (matches v1 charter §3.2 baseline); ERP = off-pattern for v1 (LE31 v1 has no ERP surface); inventory-management = on-pattern for v1 (charter §3.2 baseline = StockEntry-append-only); small-business = on-pattern for v1 (LE31 v1 is one-small-restaurant = small-business); SQLite = on-pattern for v1 *development* (known-conflict per `le31-conventions/SKILL.md` lines 73-75); MIT permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *ERP + inventory-management + small-business + Python + SQLite* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the integrated-business-process-management dimension* (every business-process state transition is an explicit SQLModel row; no silent transition; the *StockEntry-append-only* pattern IS the *inventory-management* primitive). Charter §3.1 alignment (the *business-processes + inventory-modules* discipline IS the *explicit-state-transition* applied to the integrated-business-process-management dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive; SQLite is on-pattern for v1 development per known-conflict note); §3.4 not triggered (no AI surface; the ERP is inventory-management-business-process-management, not customer-facing AI). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 small-business-ERP-horizontal-vocabulary-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 426 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours with caveat: 426 KB modest-repo size limits inspection depth). **Cost-to-value ratio: moderate** (426 KB is modest; the *ERP + inventory-management + small-business + Python + SQLite* sextuple + the in-window-by-both-fields signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/223-psb684-sketch-athena-mit-erp-inventory-management-small-business-python-sqlite-business-automation-v2-small-business-erp-horizontal-vocabulary-reference-HANDOFF.md` and `features/223-psb684-sketch-athena-mit-erp-inventory-management-small-business-python-sqlite-business-automation-v2-small-business-erp-horizontal-vocabulary-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + ERP + inventory-management + small-business + Python + SQLite documentation for the next v2 small-business-ERP-horizontal-expansion review moment; **cross-section JTBD value is moderate, the only of today's 3 picks that is in-window by BOTH `created_at` AND `pushed_at`**).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a small-business-ERP-horizontal-expansion surface to the LE31 v2 operator surface, an ERP-module surface, an inventory-management surface, or a business-automation surface):

- `app/business_processes/` — possibly add (the ERP business-process module; depends on the v2 change).
- `app/business_processes/processes.py` — possibly add (the business-process execution handler; depends on the v2 change).
- `app/inventory_modules/` — possibly add (the inventory-module configuration surface; depends on the v2 change).
- `app/inventory_modules/config.py` — possibly add (the per-tenant inventory-module configuration handler; depends on the v2 change).
- `app/models/business_processes.py` — possibly add (the `business_processes` SQLModel table; depends on the v2 change).
- `app/models/inventory_modules.py` — possibly add (the `inventory_modules` SQLModel table; depends on the v2 change).
- `app/models/tenant_config.py` — possibly add (the `tenant_config` SQLModel table; depends on the v2 change).
- `tests/test_business_processes.py` + `tests/test_inventory_modules.py` + `tests/test_tenant_config.py` — possibly add (the integration tests for the ERP + inventory-management + tenant-config surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no small-business-ERP-horizontal-expansion surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/223-psb684-sketch-athena-mit-erp-inventory-management-small-business-python-sqlite-business-automation-v2-small-business-erp-horizontal-vocabulary-reference.md` exists and is read back by the parent.
- [ ] `specs/223-psb684-sketch-athena-mit-erp-inventory-management-small-business-python-sqlite-business-automation-v2-small-business-erp-horizontal-vocabulary-reference-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `psb684-sketch/athena` description is quoted verbatim (426 KB repo).
- [ ] The 1★/0⑂ + MIT permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption) + Python + in-window-by-both-fields + 6 topics + description *"ERP system pc ver"* is documented.
- [ ] The charter §3.1 alignment via *business-processes + inventory-modules = explicit-state-transition discipline applied to integrated-business-process-management* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (MIT permissive; SQLite is on-pattern for v1 development per known-conflict note) is documented.
- [ ] The charter §3.4 not-triggered (no AI surface) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a small-business-ERP-horizontal-expansion surface to the LE31 v2 operator surface, an ERP-module surface, an inventory-management surface, or a business-automation surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `psb684-sketch/athena` *ERP + inventory-management + small-business + Python + SQLite* vocabulary is evaluated against the PR's changes: does the change address the *small-business-ERP-horizontal-expansion* discipline? does the change preserve the *inventory-management* primitive? does the change preserve the *business-automation* primitive? does the change preserve the *charter §3.1 explicit-state-transition* pattern?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 trigger (if the v2 small-business-ERP-horizontal-expansion surface is adopted):**
- Disable path: feature flag `LE31_SMALL_BUSINESS_ERP_ENABLED = False` (default; gates all `app/business_processes/` + `app/inventory_modules/` routes); no data loss.
- Delete path: `rm -rf app/business_processes/ app/inventory_modules/` + `rm -rf app/models/business_processes.py app/models/inventory_modules.py app/models/tenant_config.py` + `rm -rf tests/test_business_processes.py tests/test_inventory_modules.py tests/test_tenant_config.py`; remove any small-business-ERP-specific dependencies from `requirements.txt`; no retained data; no safe-failure-mode concern.
- Migration/rollback cost: low (no schema change for `audit_logs` or `StockEntry`; new `business_processes` + `inventory_modules` + `tenant_config` tables are independent).

## 6. Mandatory LE31 skill list (per `le31-feature-pipeline/SKILL.md` step 5)

The following skills MUST be loaded by the coding agent before any v2 trigger fires:

- `le31-conventions` — for the seven-check feature gate + charter §3.1 + §3.2 + §3.4 invariants.
- `le31-verification-protocol` — for the verification protocol + the "done means observed, not asserted" principle.
- `le31-feature-pattern` — for the existing v1 feature pattern (FastAPI + SQLModel + aiogram v3 + Postgres; first-class prepared-item stock via append-only `StockEntry` ledger).
- `le31-handoff-spec` — for the slice contract format (this file is an example).
- `le31-coding-agent-brief` — for the paste-in prompt that the coding agent will use to start work.

The following skills MAY be loaded depending on the trigger:

- `le31-research` — if the v2 trigger requires additional cross-section vocabulary.
- `le31-v1-feature-pattern` — if the v2 trigger requires extending the v1 feature pattern.
- `le31-frontend` / `le31-backend` — if the v2 trigger requires frontend or backend changes.
