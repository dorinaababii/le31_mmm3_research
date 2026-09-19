# 201 — sahajasakhunala/DineDesk normalized-PostgreSQL-restaurant-domain-schema + 7-surfaces vocabulary + Reservation + DiningSession + Discount HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 normalized-PostgreSQL-restaurant-domain-schema question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/201-sahajasakhunala-DineDesk-full-stack-restaurant-normalized-postgresql-table-reservation-dining-session-order-kitchen-billing-discount-payment.md` (defer artifact; **no code today**).

Bucket: **v1 architecture-reference (normalized-PostgreSQL-restaurant-domain-schema primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintainer asks *'if v1 introduces a Reservation SQLModel table (for table reservations), a DiningSession SQLModel table (for dining-session start-time + end-time + party-size), or a Discount SQLModel table (for line-item-discount primitives), what is the normalized-PostgreSQL-restaurant-domain-schema discipline that preserves the existing v1 Order + Bill + Payment + StockEntry + audit_logs invariants?'*, the maintainer wants *evidence that another independent 2026 Python repo at 43 KB with null license + both fields in-window + restaurant-POS + normalized-PostgreSQL-schema is shipping the 7-surfaces vocabulary (table reservations + dining sessions + order processing + kitchen workflows + billing + discounts + payments + operational) as the canonical 2026 restaurant-management surface area*, but struggles because *v1 has no documented normalized-PostgreSQL-restaurant-domain-schema primitive in the charter*, so that *v1 can introduce the Reservation + DiningSession + Discount surfaces with the explicit 7-surfaces vocabulary rather than inventing a new one*." **PASS** (zero-pain today; v1 has no Reservation + DiningSession + Discount trigger; the JTBD is primitive vocabulary extension + 7-surfaces + normalized-PostgreSQL-schema documentation, not a build-need). |
| 2 | **Viability** | Owner can read 43 KB repo description + 7-surfaces vocabulary + normalized-PostgreSQL-schema discipline? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the 7-surfaces vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + alembic stack, not imported). Confidence: medium-high for the 7-surfaces + normalized-PostgreSQL-schema vocabulary (null + Python + 43 KB tiny + both fields in-window + explicit *normalized-PostgreSQL* + 7-surfaces description). Stack: on-pattern for v1 schema primitives (FastAPI + PostgreSQL = LE31 v1 backend stack); off-pattern for v1 code adoption (null license = §3.2 BLOCKER). Practicability of adoption: high for vocabulary + normalized-schema discipline; low for code. **PASS** (posture validation only; adoption is v1 question). |
| 4 | **Conflict** | None. The 7-surfaces vocabulary (table reservations + dining sessions + order processing + kitchen workflows + billing + discounts + payments + operational) maps onto LE31's existing 4-of-7 SQLModel-table families (`Order` + `Bill` + `Payment` + `StockEntry-kitchen-workflow`); 3 of 7 surfaces are named-gap vocabulary (`Reservation` + `DiningSession` + `Discount` not in v1 today); charter §3.1 alignment via 4-of-7 direct match; §3.2 (null license = vocabulary-only); §3.4 (no AI surface). Charter §3.1 + §3.2 (vocabulary-only) explicitly aligned. **PASS**. |
| 5 | **Outcome, appetite, scope** | v1 architecture-reference (normalized-PostgreSQL-restaurant-domain-schema + 7-surfaces + Reservation + DiningSession + Discount vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 43 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (43 KB tiny repo is already substantial for a schema-only artifact; only the *7-surfaces + normalized-PostgreSQL-schema + 3-gap vocabulary* + the both-fields-in-window signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/201-sahajasakhunala-DineDesk-full-stack-restaurant-normalized-postgresql-table-reservation-dining-session-order-kitchen-billing-discount-payment-HANDOFF.md` and `features/201-sahajasakhunala-DineDesk-full-stack-restaurant-normalized-postgresql-table-reservation-dining-session-order-kitchen-billing-discount-payment.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + normalized-PostgreSQL-restaurant-domain-schema + 7-surfaces + Reservation + DiningSession + Discount documentation for the next v1 schema-extension moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a Reservation SQLModel table, a DiningSession SQLModel table, or a Discount SQLModel table):

- `app/models/reservation.py` — possibly add (the SQLModel table for the pre-booked-table primitive; depends on the v1 change).
- `app/models/dining_session.py` — possibly add (the SQLModel table for the start-time + end-time + party-size primitive; depends on the v1 change).
- `app/models/discount.py` — possibly add (the SQLModel table for the line-item-discount primitive; depends on the v1 change).
- `app/models/report.py` — possibly add (the SQLModel table for the operational-reports primitive; depends on the v1 change).
- `app/models/order.py` — possibly modify to add the *reservation_id* FK (the table-reservation integration with the existing Order primitive; depends on the v1 change).
- `app/models/bill.py` — possibly modify to add the *discount_id* FK (the line-item-discount integration with the existing Bill primitive; depends on the v1 change).
- `app/api/reservations.py` — possibly add (the FastAPI route that handles reservation creation + lookup; depends on the v1 change).
- `tests/test_reservation_flow.py` — possibly add (the integration test for the reservation primitive; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/201-sahajasakhunala-DineDesk-full-stack-restaurant-normalized-postgresql-table-reservation-dining-session-order-kitchen-billing-discount-payment.md` exists and is read back by the parent.
- [ ] `specs/201-sahajasakhunala-DineDesk-full-stack-restaurant-normalized-postgresql-table-reservation-dining-session-order-kitchen-billing-discount-payment-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `DineDesk` description is quoted verbatim (43 KB tiny repo).
- [ ] The 0★/0⑂ + null-license (§3.2 BLOCKER for code adoption, vocabulary-only artifact) + Python + 43 KB both-fields-in-window + restaurant-POS + normalized-PostgreSQL-schema + 7-surfaces vocabulary (table reservations + dining sessions + order processing + kitchen workflows + billing + discounts + payments + operational) is documented.
- [ ] The charter §3.1 alignment via explicit 4-of-7 v1-coverage mapping (Order + Bill + Payment + StockEntry-kitchen-workflow) + 3-of-7 named-gap vocabulary (Reservation + DiningSession + Discount) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds a Reservation SQLModel table, a DiningSession SQLModel table, or a Discount SQLModel table lands):**
- [ ] The PR is read back by the parent.
- [ ] The `DineDesk` 7-surfaces + normalized-PostgreSQL-schema + Reservation + DiningSession + Discount vocabulary is evaluated against the PR's changes: does the change address the *7-surfaces vocabulary (table reservations + dining sessions + order processing + kitchen workflows + billing + discounts + payments + operational)* discipline? Does the change preserve the *normalized-PostgreSQL-schema* discipline (no duplicated data + relations via explicit foreign keys + PostgreSQL-native types)? Does the change preserve the existing 4-of-7 v1-coverage (Order + Bill + Payment + StockEntry)?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the `app/models/reservation.py` + `app/models/dining_session.py` + `app/models/discount.py` + `app/models/report.py` SQLModel tables; remove the `app/models/order.py` *reservation_id* FK; remove the `app/models/bill.py` *discount_id* FK; remove the `app/api/reservations.py` FastAPI route; restore the original `app/models/order.py` + `app/models/bill.py` schemas.
- Migration cost: depends on the v1 change; the 7-surfaces vocabulary is *additive architecture* (the Reservation + DiningSession + Discount + Report tables are *added on top of* the existing v1 surfaces; the Order + Bill schemas are *modified* to add the reservation_id + discount_id FKs).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `Order` + `Bill` + `Payment` + `StockEntry` tables retain all rows; the new `Reservation` + `DiningSession` + `Discount` + `Report` tables are *new* data, not a schema change; the verification log is a *new* document, not a schema change.

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
