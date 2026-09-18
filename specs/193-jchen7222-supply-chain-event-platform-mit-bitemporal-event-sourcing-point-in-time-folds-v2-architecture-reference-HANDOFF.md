# 193 — jchen7222/supply-chain-event-platform bitemporal + event-sourced + point-in-time folds HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 audit-export or reconciliation-rules surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/193-jchen7222-supply-chain-event-platform-mit-bitemporal-event-sourcing-point-in-time-folds-v2-architecture-reference.md` (defer artifact; **no code today**).

Bucket: **v2 architecture-reference (parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a time-travel surface for audit-export queries, what is the primitive pattern for bitemporal event-sourcing + point-in-time folds + validated-in-CI?'*, the maintainer wants *evidence that another independent 2026 Python repo at 1330 KB substantial content has shipped exactly the bitemporal + event-sourced + point-in-time folds + validated-in-CI quadruple-primitive as a named platform*, but struggles because *v1 has no bitemporal or point-in-time-folds surface and the charter §3.1 invariant is not yet operationalized as a time-travel behavior*, so that *v2 can introduce the audit-export surface with the explicit bitemporal discipline rather than inventing a new one*." **PASS** (zero-pain today; v1 has no bitemporal or point-in-time-folds surface; the JTBD is primitive vocabulary extension, not a build-need). |
| 2 | **Viability** | Owner can read 1330 KB repo description + 6 topics? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (Python is the LE31 v1 backend). Confidence: medium-high for the architectural vocabulary validation (MIT + Python + 1330 KB substantial + in-window push TODAY 2026-09-17 + the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive is explicitly named in the description). Stack: off-pattern (LE31 uses SQLModel + Postgres, not dbt + duckdb; the primitives are stack-agnostic but the implementation surface is off). Practicability of adoption: medium — the *bitemporal + point-in-time folds + validated-in-CI* primitives can be extracted and re-implemented against LE31's StockEntry + audit_logs using SQLModel + Postgres. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *bitemporal + event-sourced* primitive is explicitly §3.1-aligned (append-only by construction; the *valid-time + transaction-time* discipline is additive to the existing `recorded_at` column); §3.2 (MIT = permissive); §3.4 (the *validated-in-CI* primitive is a non-AI primitive — it's a deterministic re-derivation + assertion, no AI integration). Charter §3.4 compatible (no AI integration). **PASS** (charter §3.1 + §3.2 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 architecture-reference (cross-section architectural vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1330 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (1330 KB is already substantial; only the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* + description need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/193-jchen7222-supply-chain-event-platform-mit-bitemporal-event-sourcing-point-in-time-folds-v2-architecture-reference-HANDOFF.md` and `features/193-jchen7222-supply-chain-event-platform-mit-bitemporal-event-sourcing-point-in-time-folds-v2-architecture-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary for the next v2 audit-export or reconciliation-rules question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an `event_valid_at` column to `audit_logs`, a `audit_logs_bitemporal_fold` SQL view, a `audit_logs_vintage_archive` directory, or a `validated-in-CI` step):

- `app/audit_logs_extension.py` — possibly add an `event_valid_at` column to `audit_logs` (operationalizes the *bitemporal* primitive; depends on the v2 change).
- `app/views/audit_logs_bitemporal_fold.py` — possibly add a `audit_logs_bitemporal_fold` SQL view or a Python helper (operationalizes the *point-in-time folds* primitive; depends on the v2 change).
- `tests/test_audit_logs_vintage.py` — possibly add a CI step that re-derives the audit-trail-from-events and asserts it matches the vintage archive (operationalizes the *validated-in-CI* primitive; depends on the v2 change).
- `data/audit_logs_vintage_archive/` — possibly add a *public vintage archive* directory (frozen snapshots of `audit_logs` at specific transaction-times; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/193-jchen7222-supply-chain-event-platform-mit-bitemporal-event-sourcing-point-in-time-folds-v2-architecture-reference.md` exists and is read back by the parent.
- [ ] `specs/193-jchen7222-supply-chain-event-platform-mit-bitemporal-event-sourcing-point-in-time-folds-v2-architecture-reference-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `supply-chain-event-platform` description is quoted verbatim (1330 KB repo).
- [ ] The 0★/0⑂ + MIT + Python + in-window push TODAY 2026-09-17 + `bitemporal + event-sourcing + dbt + duckdb + data-engineering + python` topic set + *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive vocabulary is documented.
- [ ] The charter §3.1 alignment via *bitemporal + event-sourced* primitive + charter §3.4 alignment via *validated-in-CI* non-AI primitive is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an `event_valid_at` column to `audit_logs`, a `audit_logs_bitemporal_fold` SQL view, a `audit_logs_vintage_archive` directory, or a `validated-in-CI` step lands):**
- [ ] The PR is read back by the parent.
- [ ] The `supply-chain-event-platform` architectural-vocabulary set is evaluated against the PR's changes: does the change address the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive? Does the change preserve the *append-only* invariant? Does the change use `Europe/Paris` timezone per charter §3.5?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `event_valid_at` column on `audit_logs`; remove the new `audit_logs_bitemporal_fold` SQL view; remove the new `audit_logs_vintage_archive` directory; remove the new `validated-in-CI` step; restore the original `audit_logs` + `StockEntry` schemas.
- Migration cost: depends on the v2 change; the `supply-chain-event-platform` pattern's *bitemporal + event-sourced + point-in-time folds + validated-in-CI* implies *additive architecture* (the new bitemporal surface is additive on top of the existing v1 surfaces — FastAPI routes + aiogram handlers + `audit_logs` writer all live in one Python process today; the new bitemporal surface adds a discrete layer with the valid-time + transaction-time discipline).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the verification log is a *new* document, not a schema change.

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
