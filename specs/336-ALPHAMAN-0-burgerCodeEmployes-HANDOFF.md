# HANDOFF — 336-ALPHAMAN-0-burgerCodeEmployes

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today) — **v1 in-domain FastAPI+SQLite+Pydantic+restaurant+employee-management+shift-scheduling+tips+small-business vocabulary only; the `burgerCodeEmployes` codebase is fully compatible (MIT permissive) but NOT adopted because LE31 v1 has no employee-management + shift-recording + tip-distribution surface; a future v1 PR that wants an employee-management + shift-recording + tip-distribution surface would adopt the 9-pentagram-primitive from scratch**

**Date**: 2026-10-17
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/336-ALPHAMAN-0-burgerCodeEmployes-mit-fastapi-sqlite-pydantic-restaurant-employee-management-shift-scheduling-tips-small-business-rest-api-v1-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no employee-management + shift-recording + tip-distribution surface today; the v1 charter has *no employee-management + shift-recording + tip-distribution* surface; the 9-pentagram-primitive vocabulary is the transferable item; sister-shape to features 05 (`payment-tip-reconciliation`) + 39 (`owner-daily-recap-telegram`) + 165 (`ladle-restaurant-prep-forecasting-food-cost-leak-detection`)).

## Trigger policy

This is a **defer artifact (parking-lot, in-domain FastAPI+restaurant+employee-management+shift-scheduling+tips+small-business vocabulary only)** — a watch-list entry. It does not start a build. It surfaces the `ALPHAMAN-0/burgerCodeEmployes` GitHub repo (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★ / 0⑂**, **5 KB tiny = smallest in-window brainstorm-vocabulary pick of the 79-pass series**, **Python ✓ ON-STACK + FastAPI + SQLite + Pydantic + restaurant + employee-management + shift-scheduling + small-business + rest-api + tips**, **pushed 2026-09-20T11:24:42Z AND created 2026-09-20T11:24:31Z = IN-WINDOW BY BOTH FIELDS**) as a dated, in-window **in-domain FastAPI+restaurant+employee-management+shift-scheduling+tips+small-business vocabulary peer** for LE31's potential v1 *employee-management + shift-recording + tip-distribution* surface.

If the trigger condition (LE31 first proposes a v1 surface that wants *employee-management* OR *shift-recording* OR *tip-distribution* OR a future owner decision questions whether the v1 charter should be extended to support an employee-management + shift-recording + tip-distribution surface) is met, the external coding agent should:

1. Load this artifact and the parent daily-brainstorm report (`/opt/data/le31-brainstorm-2026-10-17.md`).
2. Load the `burgerCodeEmployes` repo: `https://github.com/ALPHAMAN-0/burgerCodeEmployes` — README + FastAPI + SQLite + Pydantic + restaurant + employee-management + shift-scheduling + small-business + rest-api + tips; **the codebase is fully compatible (MIT permissive) but NOT adopted today because v1 has no employee-management + shift-recording + tip-distribution surface**.
3. Load the companion features 05 (`payment-tip-reconciliation` — owner-side payment-tip reconciliation) + 39 (`owner-daily-recap-telegram` — owner daily-recap) + 165 (`ladle-restaurant-prep-forecasting-food-cost-leak-detection` — restaurant prep-forecasting); the **v1 employee-management + shift-recording + tip-distribution + weekly-reports** cluster is the LE31 v1 precedent for the `burgerCodeEmployes` vocabulary.
4. **Adopt the vocabulary-shape (FastAPI+SQLite+Pydantic+restaurant+employee-management+shift-scheduling+tips+small-business+rest-api), when the v1 surface opens**. The transferable items are: (a) *employee-management*; (b) *shift-scheduling + shift-recording*; (c) *tips + weekly-reports*; (d) *FastAPI+SQLite+Pydantic ON-STACK posture*; (e) *small-business + single-tenant + rest-api* discipline. Each is a *pattern* in LE31's v1 charter, not a *code dependency*.
5. Re-run the LE31 feature gate with the adoption in mind. **Critical charter checks before any adoption**:
   - §3.1 ✓ (FastAPI + Python + Pydantic + SQLite + rest-api ✓; SQLite is OFF-§3.1 for production but ON-§3.1 for development per charter — a future v1 PR would adopt Postgres + SQLModel + Alembic for production per charter §3.1)
   - §3.2 ✓ (MIT permissive; LE31 v1 §3.2 *permissive-license-only* invariant)
   - §3.6 partial (tips + weekly-reports primitives require EUR-money + Decimal-money invariant review; shift-scheduling requires timezone-aware-instants + Europe/Paris business-dates review)
   - §3.7 partial (employee-management + shift-recording primitives require minimal-PII-only review per charter §3.7 — employee name + role + hourly-rate are PII)
6. **Decide whether the proposed v1 surface benefits from the in-domain FastAPI+restaurant+employee-management+shift-scheduling+tips+small-business primitive**. If the v1 surface wants *employee-management* OR *shift-recording* OR *tip-distribution*, the `burgerCodeEmployes` vocabulary is purpose-built for that use case. If the v1 surface only wants to extend the existing v1 cook-Telegram-polling deployment, `burgerCodeEmployes` adds no value.
7. **If the in-domain FastAPI+restaurant+employee-management+shift-scheduling+tips+small-business vocabulary is proposed for adoption**: do NOT add `burgerCodeEmployes` to `requirements.txt`; instead, design a fresh v1 employee-management + shift-recording + tip-distribution system from scratch that captures the *FastAPI+SQLite+Pydantic+restaurant+employee-management+shift-scheduling+tips+small-business+rest-api + 5/5 LE31-on-stack posture + EUR-money-Decimal-money invariant + minimal-PII-only invariant + Europe/Paris-business-dates invariant + append-only-audit-logs invariant* primitives. Add to `requirements.txt` only the new dependencies (`fastapi` already pinned, `sqlmodel` already pinned, `pydantic` already pinned, `alembic` already pinned, `pytest` already in dev-deps; LE31 v1 dependency-whitelist is silent on `sqlite` for production but the v1 charter pins `Postgres + SQLModel` so a future v1 PR would use Postgres, not SQLite). Add a single test employee-management + shift-recording + tip-distribution call against the existing v1 cook-Telegram-polling deployment. Compare against the existing v1 owner-side `payment-tip-reconciliation` deployment. If the test employee-management + shift-recording + tip-distribution adds employee-side-value, propose a v1 extension; if not, document the comparison and defer.
8. **If the in-domain FastAPI+restaurant+employee-management+shift-scheduling+tips+small-business vocabulary is not adopted**: document the comparison and defer. No charter §3.1 + §3.2 + §3.6 + §3.7 change is needed.
9. **Pilot on one employee first**. Do not ship the employee-management + shift-recording + tip-distribution surface project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Files to touch

**No files** for this defer artifact today. A future v1 PR that adopts the vocabulary would create:

- New SQLModel tables: `Employee`, `Shift`, `Tip`, `WeeklyReport` (see `features/336` "Data model" section for the high-level shape)
- New FastAPI routes: `/employees` (POST + GET + PATCH), `/employees/{employee_id}/shifts` (POST + GET), `/employees/{employee_id}/tips` (POST + GET), `/reports/weekly` (GET)
- New Pydantic models: `EmployeeCreate`, `EmployeeUpdate`, `ShiftCreate`, `ShiftUpdate`, `TipCreate`, `WeeklyReport`
- New Alembic migration: `alembic revision --autogenerate -m "add_employee_management_tables"`
- New tests: `tests/test_employee_management.py` (employee CRUD + shift CRUD + tip CRUD + weekly-report aggregation test)

## Verification protocol reference

- **`le31-conventions` skill**: load before any v1 build; the §3.6 *EUR-money + Decimal-money + tax/tip-derivation* charter-invariant review is mandatory for the `Tip` table; the §3.7 *minimal-PII-only* charter-invariant review is mandatory for the `Employee` table
- **`le31-v1-feature-pattern` skill**: load for the v1 SQLModel-table + Alembic-migration + FastAPI-route patterns; the v1 employee-management + shift-recording + tip-distribution surface would adopt the v1 patterns
- **`le31-handoff-spec` skill**: load for the slice-contract template + the seven-check gate verdict; the slice contract for the v1 employee-management + shift-recording + tip-distribution surface would follow the same template
- **`le31-coding-agent-brief` skill**: load for the paste-in prompt; the v1 build prompt would follow the same template

## Rollback path

**Trivially reversible** (the defer artifact is a vocabulary-only artifact):

- The 9-pentagram-primitive is a documented vocabulary reference; no code is added; no SQLModel tables are added; no FastAPI routes are added; no Alembic migrations are added; no dev-deps are added; no production-deps are added
- The artifact can be deleted by `rm /opt/data/le31_mmm3_research_work/features/336-ALPHAMAN-0-burgerCodeEmployes-mit-fastapi-sqlite-pydantic-restaurant-employee-management-shift-scheduling-tips-small-business-rest-api-v1-vocabulary.md` + `rm /opt/data/le31_mmm3_research_work/specs/336-ALPHAMAN-0-burgerCodeEmployes-HANDOFF.md`
- The artifact does not affect any production deployment; the v1 dependency-whitelist is unchanged; the v1 SQLModel-table-set is unchanged; the v1 FastAPI-route-set is unchanged; the v1 Alembic-migration-set is unchanged; the v1 dev-deps are unchanged; the v1 production-deps are unchanged

## Mandatory LE31 skill list

The external coding agent **must** load these skills before any v1 build:

- `le31-conventions` — the §3.6 *EUR-money + Decimal-money + tax/tip-derivation* charter-invariant review is mandatory for the `Tip` table; the §3.7 *minimal-PII-only* charter-invariant review is mandatory for the `Employee` table
- `le31-feature-pipeline` — the v1 build follows the standard feature-pipeline; the v1 bucket project is `le31 v1 — Core MVP` per the 2026-08-28 verified workspace structure
- `le31-v1-feature-pattern` — the v1 employee-management + shift-recording + tip-distribution surface would adopt the v1 SQLModel-table + Alembic-migration + FastAPI-route patterns
- `le31-handoff-spec` — the v1 build follows the standard slice-contract template
- `le31-coding-agent-brief` — the v1 build follows the standard paste-in prompt template
- `le31-daily-research` — the v1 vocabulary references for the `burgerCodeEmployes` surface are tracked in the daily-research picks list (features 05/39/165 = the v1 employee-side + owner-side tip-reconciliation + weekly-recap cluster)