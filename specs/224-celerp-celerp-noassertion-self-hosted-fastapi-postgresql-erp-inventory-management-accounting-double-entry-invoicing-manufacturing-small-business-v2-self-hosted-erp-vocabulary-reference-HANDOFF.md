# 224 — celerp/celerp v2-self-hosted-erp-vocabulary-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 self-hosted-ERP-horizontal-expansion question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/224-celerp-celerp-noassertion-self-hosted-fastapi-postgresql-erp-inventory-management-accounting-double-entry-invoicing-manufacturing-small-business-v2-self-hosted-erp-vocabulary-reference.md` (defer artifact; **no code today**).

Bucket: **v2 self-hosted-ERP-vocabulary-reference (self-hosted + FastAPI + PostgreSQL + ERP + inventory-management + accounting + double-entry + invoicing + manufacturing + small-business, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a self-hosted-ERP-horizontal-expansion surface (expansion from a single-restaurant-vertical product to a small-business-ERP-horizontal product that supports multiple vertical-business-types, or expansion to a standalone-self-hosted-ERP product, or expansion to a standalone-double-entry-accounting product), what is the *self-hosted + FastAPI + PostgreSQL + ERP + inventory-management + accounting + double-entry + invoicing + manufacturing + small-business* vocabulary that preserves the existing v1 single-restaurant-vertical posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 20843 KB with 31★/8⑂ + NOASSERTION license + 10 topics + in-window-by-both-fields + +8★/24h star-inflow is shipping the *self-hosted + FastAPI + PostgreSQL + ERP + double-entry + invoicing + manufacturing + small-business* primitive as the v2 self-hosted-ERP-horizontal-expansion discipline*, but struggles because *v1 has no documented self-hosted-ERP-horizontal-expansion primitive in the charter*, so that *v2 can introduce the self-hosted-ERP + double-entry-accounting + inventory-management + manufacturing + invoicing vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no self-hosted-ERP-horizontal-expansion trigger; the JTBD is primitive vocabulary extension + self-hosted-FastAPI-ERP + double-entry + manufacturing + invoicing + small-business documentation, not a build-need; **cross-section JTBD value is HIGH** — the only 2026-09-24 GitHub Search candidate that pins all of `fastapi + postgresql + erp + double-entry-accounting + manufacturing` simultaneously + the +8★/24h star-inflow signal). |
| 2 | **Viability** | Maintainer can read 20843 KB repo description + 10-topic vocabulary + self-hosted + FastAPI + PostgreSQL + ERP + double-entry + manufacturing + invoicing + small-business decuple? Yes. No code change required. **PASS** (informational only; code adoption blocked by NOASSERTION §3.2). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *self-hosted-FastAPI-ERP + double-entry + manufacturing + invoicing* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the NOASSERTION code; LE31 v1 has no self-hosted-ERP-horizontal-expansion surface today). Confidence: medium-high for the *self-hosted-FastAPI-ERP + double-entry + manufacturing + invoicing* vocabulary (31★/8⑂ + 10 topics including all 8 LE31-relevant primitives + in-window-by-both-fields + +8★/24h star-inflow + description verbatim + NOASSERTION license = §3.2 BLOCKER for code adoption but vocabulary + architecture-reference adoption is permitted; the *self-hosted + FastAPI + PostgreSQL* stack matches LE31 v1's stack exactly; the *ERP + inventory-management + accounting + double-entry-accounting + invoicing* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the integrated-business-process-management dimension*; the *small-business + manufacturing* discipline IS the *single-tenant + production-process-tracking* posture). Practicability of adoption: vocabulary + architecture-reference adoption only; code would require author re-license negotiation. **PASS** (posture validation only; adoption is v2 question contingent on author re-license). |
| 4 | **Conflict** | None. The *self-hosted + FastAPI + PostgreSQL + ERP + inventory-management + accounting + double-entry-accounting + invoicing + manufacturing + small-business* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the integrated-business-process-management dimension* (every business-process state transition is an explicit SQLModel row; no silent transition; the *StockEntry-append-only* pattern IS the *inventory-management* primitive; the *double-entry-accounting* discipline IS the *every-transaction-has-two-legs* pattern). Charter §3.1 alignment (the *self-hosted + single-tenant + on-premise* posture IS the *explicit-state-transition + single-restaurant-vertical* discipline applied to the *integrated-business-process-management* dimension); §3.2 BLOCKER for code adoption (NOASSERTION; vocabulary-only artifact; description hints "MIT modules" but the GitHub-level `spdx_id` is NOASSERTION; the description is informational but the license is the spdx_id field); §3.4 not triggered (no AI surface; the *self-hosted-ERP* discipline is integrated-business-process-management, not customer-facing AI). **PASS** (vocabulary-adoption-yes, code-adoption-no). |
| 5 | **Outcome, appetite, scope** | v2 self-hosted-ERP-vocabulary-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 20843 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours with caveat: 20843 KB substantial-repo size makes inspection immediately productive if author grants re-license). **Cost-to-value ratio: high** (the *self-hosted-FastAPI-ERP + double-entry + manufacturing + invoicing + small-business* decuple + the in-window-by-both-fields signal + the +8★/24h star-inflow + the 8/10 topic-overlap score need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/224-celerp-celerp-noassertion-self-hosted-fastapi-postgresql-erp-inventory-management-accounting-double-entry-invoicing-manufacturing-small-business-v2-self-hosted-erp-vocabulary-reference-HANDOFF.md` and `features/224-celerp-celerp-noassertion-self-hosted-fastapi-postgresql-erp-inventory-management-accounting-double-entry-invoicing-manufacturing-small-business-v2-self-hosted-erp-vocabulary-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + self-hosted-FastAPI-ERP + double-entry + manufacturing + invoicing + small-business documentation for the next v2 self-hosted-ERP-horizontal-expansion review moment; **cross-section JTBD value is HIGH** — the only 2026-09-24 GitHub Search candidate that pins all of `fastapi + postgresql + erp + double-entry-accounting + manufacturing` simultaneously + the +8★/24h star-inflow signal; **code adoption blocked by NOASSERTION §3.2 — vocabulary + architecture-reference adoption only**).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a self-hosted-ERP-horizontal-expansion surface to the LE31 v2 operator surface, an ERP-module surface, an inventory-management surface, a double-entry-accounting surface, an invoicing surface, or a manufacturing surface):

- `app/erp_modules/` — possibly add (the self-hosted-ERP module directory; depends on the v2 change).
- `app/erp_modules/accounting.py` — possibly add (the double-entry-accounting handler; depends on the v2 change).
- `app/erp_modules/inventory.py` — possibly add (the inventory-management handler; depends on the v2 change).
- `app/erp_modules/invoicing.py` — possibly add (the invoicing handler; depends on the v2 change).
- `app/erp_modules/manufacturing.py` — possibly add (the manufacturing-process handler; depends on the v2 change).
- `app/models/erp_accounts.py` — possibly add (the `erp_accounts` SQLModel table; double-entry-accounting ledger; depends on the v2 change).
- `app/models/erp_invoices.py` — possibly add (the `erp_invoices` SQLModel table; depends on the v2 change).
- `app/models/erp_manufacturing.py` — possibly add (the `erp_manufacturing` SQLModel table; depends on the v2 change).
- `app/models/erp_inventory.py` — possibly add (the `erp_inventory` SQLModel table; depends on the v2 change).
- `tests/test_erp_modules.py` + `tests/test_erp_accounts.py` + `tests/test_erp_invoices.py` + `tests/test_erp_manufacturing.py` + `tests/test_erp_inventory.py` — possibly add (the integration tests for the self-hosted-ERP + double-entry-accounting + invoicing + manufacturing + inventory surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no self-hosted-ERP-horizontal-expansion surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

- **No code today**, so no verification protocol applies.
- **Future v2 verification protocol** (if the trigger condition fires + author re-license is granted):
  1. **License re-verification** — re-fetch `https://api.github.com/repos/celerp/celerp/license` to confirm `spdx_id` has changed from NOASSERTION to MIT-permissive (or to a per-module SPDX expression that includes MIT for the relevant modules).
  2. **Stack-shape verification** — confirm `celerp/celerp` source uses FastAPI + PostgreSQL + SQLAlchemy + double-entry-accounting primitives by inspecting `app/` or `src/` directory.
  3. **Inventory-management verification** — confirm `celerp/celerp` source has an `inventory` module with StockEntry-equivalent append-only ledger entries.
  4. **Invoicing verification** — confirm `celerp/celerp` source has an `invoicing` module with double-entry invoice-handling.
  5. **Manufacturing verification** — confirm `celerp/celerp` source has a `manufacturing` module with production-process tracking.
  6. **Integration test verification** — verify the adapted vocabulary primitives work against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack.
  7. **Telegram surface verification** (if a Telegram surface is added in v2) — verify the adapted vocabulary primitives send correct aiogram messages with no hallucinated text.
- **Anti-fabrication canary**: `grep -c 'LE31' <celerp-source-file>` must return 0 — the celerp source is independent of LE31 and any "verbatim" quotes must not mention LE31.

## 5. Rollback path

**Fully reversible.** The defer artifact is documentation only. Disable/delete path:
- `git rm specs/224-celerp-celerp-noassertion-self-hosted-fastapi-postgresql-erp-inventory-management-accounting-double-entry-invoicing-manufacturing-small-business-v2-self-hosted-erp-vocabulary-reference-HANDOFF.md`
- `git rm features/224-celerp-celerp-noassertion-self-hosted-fastapi-postgresql-erp-inventory-management-accounting-double-entry-invoicing-manufacturing-small-business-v2-self-hosted-erp-vocabulary-reference.md`
- No migration, no SQLModel schema rollback, no FastAPI route removal, no Telegram handler removal required.
- No retained data; no safe-failure-mode concern.

If a future v2 PR has already added a self-hosted-ERP surface based on this vocabulary reference, the rollback path includes:
- Remove the v2 surface code (depends on the v2 change).
- Remove the v2 SQLModel tables (depends on the v2 change).
- Remove the v2 FastAPI routes (depends on the v2 change).
- Remove the v2 Telegram handlers (depends on the v2 change).
- Re-run LE31 v2 test suite to confirm no regression.

## 6. Mandatory LE31 skill list

The coding agent **MUST** load and follow these skills before any future v2 implementation (none apply today):

- `le31-conventions` — the master skill for v2 development conventions; §3.1 explicit-state-transitions, §3.2 license-compatible-only, §3.4 no-customer-facing-AI.
- `le31-v1-feature-pattern` — the v1 feature template pattern that informs the v2 surface shape.
- `le31-handoff-spec` — the handoff spec that documents the slice contract.
- `le31-coding-agent-brief` — the coding-agent brief that produces the paste-in prompt from the slice contract.
- `le31-verification-protocol` — the verification protocol that defines what "done" means.
- `le31-feature-pipeline` — the feature pipeline that produces the deliverables.
- `le31-daily-research` — the daily research skill that produced this artifact.
- `le31-daily-brainstorm` — the daily brainstorm skill that produced this artifact.
- `le31-v2-feature-pattern` — the v2 feature template pattern (if it exists; otherwise this skill is not loaded).

**No skill loading required today.** The defer artifact is documentation only; the coding agent does not need to load any skill because there is no code change.

---

**Summary**: defer (parking-lot); v2 self-hosted-ERP-vocabulary-reference; no code today; NOASSERTION §3.2 BLOCKER for code adoption (vocabulary-only); cross-section JTBD value is HIGH (the only 2026-09-24 GitHub Search candidate that pins all of `fastapi + postgresql + erp + double-entry-accounting + manufacturing` simultaneously + +8★/24h star-inflow); 8/10 topic-overlap score; sister-shape to features 90/94 + 152 + 195 + 223.