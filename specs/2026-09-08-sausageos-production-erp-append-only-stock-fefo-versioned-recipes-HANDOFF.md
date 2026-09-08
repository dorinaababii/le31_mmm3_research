# 2026-09-08 — `sausageos-production-erp-append-only-stock-fefo-versioned-recipes` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/153-sausageos-production-erp-append-only-stock-fefo-versioned-recipes.md` (defer artifact; **no code today**).

Bucket: **v1 architecture-reference**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 maintainer reads the prepped-item stock code, the owner wants *to verify the manufacturing-grade primitives (FEFO, lot-based costing, batch recall) are surfaced*, but struggles because *the current primitives are implicit in the `StockEntry` writes*, so that *the next maintainer can verify the production-ERP-aligned primitives are present*." **PASS** (zero-pain today; the codebase is small enough that the primitives are implicit; the JTBD is documentation-nicety, not build-need). |
| 2 | **Viability** | Owner can read 182 B? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence high for the architectural match (the four sub-primitives — *append-only stock ledger / versioned recipes / FEFO / lot-based costing / batch recall* — map onto LE31's `StockEntry`, `MenuItem`, missing-FEFO, missing-lot-costing, missing-batch-recall). Stack mismatch (Django, not FastAPI) → no code adoption is possible. **PASS**. |
| 4 | **Conflict** | None. The sausageos "append-only stock ledger" pattern *is* the LE31 §3.1 *current stock is derived from entries* invariant; "versioned recipes" *is* the LE31 §3.1 *every prepared-item quantity change is a new `StockEntry`* invariant (each production run commits to a specific recipe version). **PASS** (charter §3.1 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v1 architecture-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 182 B description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (182 B is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-08-sausageos-production-erp-append-only-stock-fefo-versioned-recipes-HANDOFF.md` and `features/153-sausageos-production-erp-append-only-stock-fefo-versioned-recipes.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v1 architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds an `expires_at` field to `StockEntry`, a `Bill_line_item → StockEntry` link, a `recall_id` field on `MenuItem`, or a *production-run* surface):

- `app/models/stock_entry.py` — possibly add an `expires_at` field (depends on the v1 change).
- `app/models/bill.py` — possibly add a `Bill_line_item → StockEntry` link (depends on the v1 change).
- `app/models/menu_item.py` — possibly add a `recall_id` field (depends on the v1 change).
- `app/state/transitions.py` — possibly add a *production-run* transition (depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/153-sausageos-production-erp-append-only-stock-fefo-versioned-recipes.md` exists and is read back by the parent.
- [ ] `specs/2026-09-08-sausageos-production-erp-append-only-stock-fefo-versioned-recipes-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The sausageos description is quoted verbatim (182 B repo).
- [ ] The 1:1 mapping onto LE31 v1 architecture is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds FEFO, lot-based costing, batch recall, or a production-run surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The sausageos primitive set is evaluated against the PR's changes: does the change preserve *append-only stock ledger*? Does the change introduce FEFO discipline? Does the change add lot-based costing? Does the change add batch recall?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `expires_at` / `Bill_line_item → StockEntry` / `recall_id` / production-run surface; restore the original `StockEntry` + `Bill` + `MenuItem` schema.
- Migration cost: depends on the v1 change; the sausageos pattern's *append-only* implies *no new migrations* (the new fields are additive on top of the existing append-only log).
- Retained data: the `StockEntry` table retains all rows (charter §3.1); the verification log is a *new* document, not a schema change.

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

## 7. Handoff summary

| Field | Value |
|---|---|
| Feature ID | 153 |
| Slug | `sausageos-production-erp-append-only-stock-fefo-versioned-recipes` |
| Bucket | v1 architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/stock_entry.py` (possibly) + `app/models/bill.py` (possibly) + `app/models/menu_item.py` (possibly) + `app/state/transitions.py` (possibly) |
| Trigger condition | First v1 PR that adds an `expires_at` field to `StockEntry`, a `Bill_line_item → StockEntry` link, a `recall_id` field on `MenuItem`, or a *production-run* surface |
| Verification protocol | Does the change preserve *append-only stock ledger*? Does it introduce FEFO discipline? Does it add lot-based costing? Does it add batch recall? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | (to be created) |
| Linear sub-issue | (to be created) |
| Lead source | GitHub `patseluk-lang/sausageos` (MIT, 0★, pushed 2026-09-07T13:47:05Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v1 trigger sign-off gap** (when the first v1 PR that adds FEFO, lot-based costing, batch recall, or a production-run surface lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the sausageos primitive set is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v1 surface that adds FEFO, lot-based costing, batch recall, or a production-run surface will append a row here with: PR number, the sausageos primitive set evaluated, the evaluation result, and the operator's sign-off.)*