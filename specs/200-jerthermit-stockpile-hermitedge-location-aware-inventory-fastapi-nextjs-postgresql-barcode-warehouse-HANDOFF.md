# 200 — jerthermit/stockpile-hermitedge location-aware-inventory + 5-verbs + barcode-scanner + warehouse-management HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 stock-ledger-as-physical-place question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/200-jerthermit-stockpile-hermitedge-location-aware-inventory-fastapi-nextjs-postgresql-barcode-warehouse.md` (defer artifact; **no code today**).

Bucket: **v1 architecture-reference (stock-ledger-as-physical-place primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintainer asks *'if v1 introduces a barcode-scanner-equipped staff device, a physical-floor stock-location SQLModel field, or a warehouse-management surface, what is the stock-ledger-as-physical-place primitive that preserves the existing v1 StockEntry + audit_logs + cook-bot invariants?'*, the maintainer wants *evidence that another independent 2026 Python repo at 9792 KB with null license + both fields in-window + restaurant-inventory + barcode-scanner + warehouse-management topics is shipping the 5-verbs vocabulary (receive + store + move + sell + check) as the physical-floor inventory discipline*, but struggles because *v1 has no documented stock-ledger-as-physical-place primitive in the charter*, so that *v1 can introduce the physical-floor inventory vocabulary with the explicit 5-verbs rather than inventing a new one*." **PASS** (zero-pain today; v1 has no stock-ledger-as-physical-place trigger; the JTBD is primitive vocabulary extension + 5-verbs + barcode-scanner + warehouse-management documentation, not a build-need). |
| 2 | **Viability** | Owner can read 9792 KB repo description + 5-verbs vocabulary + barcode-scanner + warehouse-management topic set? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the stock-ledger-as-physical-place vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the TypeScript + Next.js frontend or the `together-ai` integration). Confidence: medium-high for the 5-verbs + stock-ledger-as-physical-place vocabulary (null + Python + 9792 KB substantial + both fields in-window + explicit 5-verbs description + staff-facing AI topic = §3.4-compatible). Stack: FastAPI + PostgreSQL backend = on-pattern for v1 primitives; TypeScript + Next.js frontend = off-pattern for v1 (LE31 v1 uses HTMX not Next.js); null license = off-pattern for code adoption (§3.2 BLOCKER); together-ai integration = off-pattern for code adoption (charter §3.4 — staff-facing AI-assist IS §3.4-compatible in principle but the specific `together-ai` provider is not on LE31's stack). Practicability of adoption: low for code; high for vocabulary + deployment-topology reference. **PASS** (posture validation only; adoption is v1 question). |
| 4 | **Conflict** | None. The 5-verbs vocabulary (receive + store + move + sell + check) maps onto LE31's existing 2-of-5 StockEntry verbs (receive → `StockEntry.entry_type='receive'`; sell → `Bill` consumption) + 3 hypothetical storage-location verbs (store + move + check); charter §3.1 alignment; §3.2 (null license = vocabulary-only); §3.4 (staff-facing AI-assist via `together-ai`, NOT customer-facing AI = §3.4-compatible). Charter §3.1 + §3.2 (vocabulary-only) + §3.4 explicitly aligned. **PASS**. |
| 5 | **Outcome, appetite, scope** | v1 architecture-reference (stock-ledger-as-physical-place + 5-verbs + barcode-scanner + warehouse-management vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 9792 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (9792 KB is substantial; only the *5-verbs + stock-ledger-as-physical-place + barcode-scanner + warehouse-management* vocabulary + the both-fields-in-window signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/200-jerthermit-stockpile-hermitedge-location-aware-inventory-fastapi-nextjs-postgresql-barcode-warehouse-HANDOFF.md` and `features/200-jerthermit-stockpile-hermitedge-location-aware-inventory-fastapi-nextjs-postgresql-barcode-warehouse.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + stock-ledger-as-physical-place + 5-verbs + barcode-scanner + warehouse-management documentation for the next v1 schema-extension moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a barcode-scanner integration, a physical-floor stock-location SQLModel field, or a warehouse-management surface):

- `app/models/storage_location.py` — possibly add (the SQLModel table for the physical storage location surface; depends on the v1 change).
- `app/models/stock_entry.py` — possibly add `storage_location_id` FK + `transferred_at` + `from_location_id` + `to_location_id` + `counted_at` + `counted_by_actor` + `physical_count` fields (the 5-verbs vocabulary extensions; depends on the v1 change).
- `app/api/barcode_scan.py` — possibly add (the FastAPI route that handles barcode-scanner input from a staff device; depends on the v1 change).
- `app/bot/cook.py` — possibly modify to add the *barcode-scanner-equipped cook flow* (the cook-bot surface when input comes from a scanned barcode, not a typed message; depends on the v1 change).
- `tests/test_warehouse_management.py` — possibly add (the integration test for the warehouse-management surface; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/200-jerthermit-stockpile-hermitedge-location-aware-inventory-fastapi-nextjs-postgresql-barcode-warehouse.md` exists and is read back by the parent.
- [ ] `specs/200-jerthermit-stockpile-hermitedge-location-aware-inventory-fastapi-nextjs-postgresql-barcode-warehouse-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `stockpile-hermitedge` description is quoted verbatim (9792 KB repo).
- [ ] The 0★/0⑂ + null-license (§3.2 BLOCKER for code adoption, vocabulary-only artifact) + Python + both-fields-in-window + restaurant-inventory + 5-verbs vocabulary (receive + store + move + sell + check) + barcode-scanner + warehouse-management + staff-facing AI (charter §3.4-compatible) is documented.
- [ ] The charter §3.1 alignment via explicit 5-verbs mapping (2-of-5 direct LE31 StockEntry-verb matches: receive → `StockEntry.entry_type='receive'`; sell → `Bill` consumption) + 3-of-5 hypothetical storage-location verbs (store + move + check) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds a barcode-scanner integration, a physical-floor stock-location SQLModel field, or a warehouse-management surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `stockpile-hermitedge` 5-verbs + stock-ledger-as-physical-place + barcode-scanner + warehouse-management vocabulary is evaluated against the PR's changes: does the change address the *5-verbs vocabulary (receive + store + move + sell + check)* discipline? Does the change preserve the *stock-ledger-as-physical-place* primitive? Does the change preserve the existing 2-of-5 v1 verbs (receive + sell)?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the `app/models/storage_location.py` SQLModel table; remove the `app/models/stock_entry.py` `storage_location_id` + `transferred_at` + `from_location_id` + `to_location_id` + `counted_at` + `counted_by_actor` + `physical_count` fields; remove the `app/api/barcode_scan.py` FastAPI route; restore the original `app/bot/cook.py` Telegram handler.
- Migration cost: depends on the v1 change; the stock-ledger-as-physical-place vocabulary is *additive architecture* (the storage-location fields are *added on top of* the existing StockEntry schema; the barcode-scan route is a *new* route; the cook-bot flow is *modified* to add the barcode-scanner-equipped variant).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `StockEntry` table retains all rows; the new `StorageLocation` SQLModel table is *new* data, not a schema change; the new barcode-scan route is *new* code, not a schema change; the verification log is a *new* document, not a schema change.

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
