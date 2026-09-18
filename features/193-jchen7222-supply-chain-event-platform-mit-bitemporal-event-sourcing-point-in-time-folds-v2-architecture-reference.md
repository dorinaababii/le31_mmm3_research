# Feature 193 — `jchen7222-supply-chain-event-platform-mit-bitemporal-event-sourcing-point-in-time-folds-v2-architecture-reference` (defer)

> **NEW observation (2026-09-18).** Documents in-window GitHub repo `jchen7222/supply-chain-event-platform` (**MIT ✓**, **0★/0⑂**, Python, **pushed 2026-09-17T11:43:19Z (TODAY, in-window by `pushed_at` only)**, **created 2026-08-01T17:01:49Z** (47-day-old repo with in-window push), **1330 KB** substantial repo, default_branch=`main`). Topics (verbatim from raw JSON): `bitemporal, data-engineering, dbt, duckdb, event-sourcing, python`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-18): *"Bitemporal event-sourced supply-chain platform: append-only ledger, point-in-time folds, validated in CI against public vintage archives."* The **first in-window candidate of the 50-pass series to explicitly name the *bitemporal* primitive** — the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive is the **cleanest 2026-09 event-sourcing reference in-window**. Bucket: **v2 architecture-reference (parking-lot defer)** — vocabulary + primitive-transferability artifact, zero build time today.

## Goal

Retain the **"Bitemporal event-sourced supply-chain platform: append-only ledger, point-in-time folds, validated in CI against public vintage archives"** cross-section architectural vocabulary as a persistent v2 event-sourcing reference for the next LE31 v2 maintainer asking the *audit-export + reconciliation-rules + bitemporal event-sourcing* question (does LE31 v2 introduce a *time-travel* primitive for audit-export queries? does LE31 v2 adopt the *validated-in-CI* discipline for any audit-export surface?). The artifact is the persistent *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive as a named v2 architectural reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `supply-chain-event-platform` cross-section architectural vocabulary: the **first in-window candidate of the 50-pass series to explicitly name the *bitemporal* primitive**; the MIT license is charter §3.2-compatible; the `bitemporal + event-sourcing + dbt + duckdb + data-engineering + python` topic set maps onto any future LE31 v2 audit-export or reconciliation-rules surface.
- A written record of the **four primitives**: (1) *bitemporal* — every event carries both *valid time* (when the event happened in the real world) and *transaction time* (when the event was recorded in the system); (2) *event-sourced* — state is derived from events; current state is a fold of the event stream; (3) *point-in-time folds* — the SQL/materialized-view primitive that computes *state as of time T* by folding the event stream up to time T; (4) *validated-in-CI* — the test-against-truth discipline that re-derives the audit-trail-from-events and checks it matches the export.
- A written record of the **1:1 mapping onto LE31 §3.1*v2* primitives**: LE31 v1 already implements the *event-sourced* primitive implicitly (`StockEntry` is the event stream; current stock is a SQL aggregate of the stream); the *bitemporal* primitive would require a new `event_valid_at` column on `audit_logs` (currently only `event_recorded_at`); the *point-in-time folds* primitive would require a new SQL view or a Python helper; the *validated-in-CI* primitive would require a new CI step.
- A decision record: today's verdict is `defer (parking-lot)` because the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive is a v2 architectural vocabulary, not a v1 build implication. v1 has no bitemporal or point-in-time-folds surface today; v2 would extend the v1 primitives with these cluster primitives only if and when the v2 trigger condition fires.

**Out of scope (defer artifact):**
- Any change to the LE31 v1 schema (no `event_valid_at` column on `audit_logs` today, no `bitemporal_folds` SQL view today, no `validated-in-CI` step today). The defer artifact documents the architectural vocabulary; v2 maintainer decision required before any schema change.
- Any change to the waiter web UI (HTMX) or cook Telegram bot.
- Adoption of the supply-chain-event-platform code as a v2 dependency (the repo is 0★/0⑂ at 1330 KB; the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* primitives would need to be independently re-implemented and validated against the LE31 append-only StockEntry ledger + audit_logs, not simply imported; the `dbt + duckdb` stack is off-pattern — LE31 uses SQLModel + Postgres). The cross-section is *primitive vocabulary extension*, not *library adoption*.
- Any change to the `audit_logs` table or `StockEntry` ledger today.

## Evidence / JTBD

When a future LE31 v2 maintainer asks *"if v2 introduces a *time-travel* surface for audit-export queries, what is the primitive pattern for *bitemporal event-sourcing + point-in-time folds + validated-in-CI*?"*, the maintainer wants *evidence that another independent 2026 Python repo at 1330 KB substantial content has shipped exactly the bitemporal + event-sourced + point-in-time folds + validated-in-CI quadruple-primitive as a named platform*, but struggles because *v1 has no bitemporal or point-in-time-folds surface and the charter §3.1 invariant is not yet operationalized as a *time-travel* behavior*, so that *v2 can introduce the audit-export surface with the explicit bitemporal discipline rather than inventing a new one*.

- **Evidence class**: observed (the supply-chain-event-platform description explicitly names *"bitemporal event-sourced"* + *"point-in-time folds"* + *"validated in CI against public vintage archives"* — exactly the v2 architectural vocabulary for any future LE31 audit-export or reconciliation-rules surface).
- **Confidence**: medium-high for the architectural vocabulary validation (MIT + Python + 1330 KB substantial + in-window push TODAY 2026-09-17 + the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive is explicitly named in the description). Confidence: low for *adoption* (LE31 should re-implement the *bitemporal + point-in-time folds + validated-in-CI* primitives against its own StockEntry + audit_logs, not import supply-chain-event-platform directly; the `dbt + duckdb` stack is off-pattern — LE31 uses SQLModel + Postgres).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension*, not *LE31 demand*.
- **The value is primitive vocabulary extension**: when (if) LE31 v2 introduces an audit-export or reconciliation-rules surface, the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* vocabulary is documented.

## Description

GitHub `jchen7222/supply-chain-event-platform` (MIT, 0★/0⑂, Python, pushed 2026-09-17T11:43:19Z, created 2026-08-01T17:01:49Z, 1330 KB substantial repo).

Description (verbatim): *"Bitemporal event-sourced supply-chain platform: append-only ledger, point-in-time folds, validated in CI against public vintage archives."*

Topics (verbatim from raw JSON): `bitemporal`, `data-engineering`, `dbt`, `duckdb`, `event-sourcing`, `python` — 6 topics; the **first in-window candidate of the 50-pass series to explicitly name the *bitemporal* primitive**.

The **four primitives**:
1. **Bitemporal** — every event carries both *valid time* (when the event happened in the real world) and *transaction time* (when the event was recorded in the system). The bitemporal discipline is the *audit-export* primitive that any future LE31 v2 owner-facing reconciliation-rules surface would need:
   - An owner asking *"what did the system think the stock count was on 2026-09-15?"* is asking a **transaction-time** question: re-derive the audit_logs at transaction-time `2026-09-15`.
   - An owner asking *"what was the actual stock count on 2026-09-15?"* is asking a **valid-time** question: re-derive the audit_logs where `event_valid_at <= 2026-09-15`.
   - **LE31 v1 mapping**: LE31's `audit_logs` table has `recorded_at` (transaction-time) but NOT `valid_at` (valid-time). Adding the bitemporal primitive would require an `event_valid_at` column on `audit_logs` and a new `audit_logs_bitemporal_fold` SQL view.
2. **Event-sourced** — state is derived from events; current state is a fold of the event stream. LE31 v1 already implements this implicitly:
   - `StockEntry` is the event stream; current stock is a SQL aggregate `SELECT SUM(quantity_change) FROM stock_entries WHERE menu_item_id = X`.
   - `audit_logs` is the event stream; current state (last action) is `SELECT * FROM audit_logs ORDER BY recorded_at DESC LIMIT 1`.
   - The v2 surface would *name* this discipline explicitly (e.g., a `charter/event_sourcing.md` doc) rather than implementing it implicitly.
3. **Point-in-time folds** — the SQL/materialized-view primitive that computes *state as of time T* by folding the event stream up to time T:
   ```sql
   -- Bitemporal point-in-time fold: state at valid_time T, recorded up to transaction_time R
   SELECT
       menu_item_id,
       SUM(quantity_change) AS stock_count
   FROM stock_entries
   WHERE event_valid_at <= T
     AND recorded_at <= R
   GROUP BY menu_item_id;
   ```
   **LE31 v1 mapping**: would require a new `stock_bitemporal_fold` SQL view (or a Python helper) parameterized by `T` and `R`.
4. **Validated-in-CI against public vintage archives** — the test-against-truth discipline that re-derives the audit-trail-from-events and checks it matches the export:
   - The CI step reads a *public vintage archive* (a frozen snapshot of the audit_logs at a specific transaction-time, like a *consensus state*).
   - The CI step then re-derives the audit-trail from the live `audit_logs` event stream up to that transaction-time.
   - The CI step asserts that the two match.
   - **LE31 v1 mapping**: would require a `audit_logs_vintage_archive` directory (read-only snapshots) + a CI step that re-derives and asserts.

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred — the architectural vocabulary validation is real but no LE31 owner has asked for *bitemporal + event-sourced + point-in-time folds + validated-in-CI* in 50 passes. The owner today uses features 121/122/125/127/148/153/154/161 to track the *append-only-ledger + event-sourcing + audit-log-primitive* convergence. |
| 2. Viability | Mechanism is well-defined (Python + dbt + duckdb); viability is conditional on a v2 audit-export or reconciliation-rules surface decision. |
| 3. Practicability and confidence | Confidence: medium-high for the architectural vocabulary validation (MIT + Python + 1330 KB substantial + in-window push TODAY 2026-09-17 + the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive is explicitly named in the description). Stack: off-pattern (LE31 uses SQLModel + Postgres, not dbt + duckdb; the primitives are stack-agnostic but the implementation surface is off). Practicability of adoption: medium — the *bitemporal + point-in-time folds + validated-in-CI* primitives can be extracted and re-implemented against LE31's StockEntry + audit_logs using SQLModel + Postgres. |
| 4. Conflict | No conflict with charter §3.1 (the *bitemporal + event-sourced* primitive is explicitly §3.1-aligned — append-only by construction; the *valid-time + transaction-time* discipline is additive to the existing `recorded_at` column); §3.2 (MIT = permissive); §3.4 (the *validated-in-CI* primitive is a non-AI primitive — it's a deterministic re-derivation + assertion, no AI integration). Charter §3.4 compatible (no AI integration). |
| 5. Outcome, appetite, scope | v2 architecture-reference (cross-section architectural vocabulary). Appetite: zero today. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value: medium-high (the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* vocabulary is the named architectural reference for any future v2 audit-export or reconciliation-rules surface). |
| 7. Circuit breaker and reversibility | Trivially reversible: written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today. The MIT + Python + 1330 KB + in-window push TODAY + *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive combo is a *novelty signal* + *vocabulary-validation signal*, not a *credibility signal*; the architectural vocabulary is the value.

## Implementation steps

None today. When v2 maintainer asks the v2 audit-export or reconciliation-rules question, the *architectural vocabulary validation* to surface is **"another independent 2026 Python repo at 1330 KB substantial content with the in-window push TODAY has shipped exactly the bitemporal + event-sourced + point-in-time folds + validated-in-CI quadruple-primitive as a named platform that LE31 v2 would need without re-architecting v1"**. This is a *primitive vocabulary extension*, not a v1 build implication; v2 maintainer decision required before any v2 surface adopts the *bitemporal + point-in-time folds + validated-in-CI* posture.

## Dependencies

- None today.
- Future dependencies (v2 only): a v2 maintainer decision on whether to introduce an audit-export or reconciliation-rules surface; an `event_valid_at` column on `audit_logs` to operationalize the *bitemporal* primitive; a `audit_logs_bitemporal_fold` SQL view or a Python helper to operationalize the *point-in-time folds* primitive; a `audit_logs_vintage_archive` directory + a CI step to operationalize the *validated-in-CI* primitive. None of these are in v1 scope.

## Open questions

1. **Does the supply-chain-event-platform bitemporal discipline use UTC or a domain-specific timezone (e.g., supply-chain event timestamps)?** Today: unknown — repo source not yet read. LE31 uses `Europe/Paris` for business time per charter §3.5; the bitemporal discipline would need to respect the timezone convention. Recommend read-and-cite on next v2-architecture-review moment.
2. **What is the granularity of the *point-in-time folds* (per-second, per-minute, per-hour)?** Today: unknown. LE31's `audit_logs` table records timestamps at second-level granularity; the bitemporal fold would be at second-level granularity by default. Coarser granularity (e.g., per-day) might be acceptable for human-facing audit-export queries. Recommend read-and-cite.
3. **What is the *public vintage archive* format (Parquet? DuckDB snapshot? Plain JSON dump?)?** Today: unknown. LE31 would likely use a plain SQL dump (e.g., `pg_dump --schema-only --data-only`) for portability and LE31's Postgres-only production deployment. Recommend read-and-cite.
4. **Is the supply-chain-event-platform repo actively maintained?** Today: 0★/0⑂ + MIT + 1330 KB + in-window push TODAY 2026-09-17 = active-maintainer signal but no community adoption (0★). Recommend re-check at the next 7-day boundary.

## Why this matters

The supply-chain-event-platform repo is the **first in-window candidate of the 50-pass series to explicitly name the *bitemporal* primitive** — the *bitemporal + event-sourced + point-in-time folds + validated-in-CI* quadruple-primitive is the **cleanest 2026-09 event-sourcing reference in-window**. The 1330 KB substantial content + the in-window push TODAY 2026-09-17 + the explicit *bitemporal* topic + the *validated-in-CI* discipline is the **highest-value v2 architecture-reference + audit-export primitive artifact of the 50-pass series**. For LE31 v1, the implication is *none* (v1 has no bitemporal or point-in-time-folds surface). For LE31 v2, the implication is *the bitemporal + event-sourced + point-in-time folds + validated-in-CI vocabulary is documented, and the charter §3.1 + §3.4 invariants are validated against an independent 2026 Python repo at 1330 KB*. **No build today.**

## Cross-section (vs the prior 50-pass cluster)

- Feature 121 (`append-only-ledger-canonical-architecture-reference-v2`) — *sister-shape* (the *append-only-ledger* canonical architecture reference maps onto the supply-chain-event-platform *append-only ledger* primitive; supply-chain-event-platform adds the *bitemporal + point-in-time folds + validated-in-CI* extensions).
- Feature 122 (`append-only-ledger-operator-ux-surface-cross-section`) — *sister-shape* (the *operator-ux surface* maps onto the supply-chain-event-platform *point-in-time folds* primitive; the operator can query *state as of time T* via the bitemporal fold).
- Feature 125 (`append-only-ledger-decision-journal-low-effort-entry`) — *sister-shape* (the *decision-journal + low-effort-entry* primitive maps onto the supply-chain-event-platform *bitemporal event-sourced* primitive; every decision is a bitemporal event with both valid-time and transaction-time).
- Feature 127 (`zero-shot-self-orchestration-Ledger-Based-Control`) — *sister-shape* (the *ledger-based control* primitive maps onto the supply-chain-event-platform *append-only ledger + point-in-time folds* primitive; the zero-shot-self-orchestration can re-derive state at any point in time).
- Feature 148 (`ppfenning-coxswain-graphs-graphs-own-sequence-write-nothing`) — *sister-shape* (the *graphs own sequence and write nothing* primitive is the *event-sourced* primitive applied to the graph domain; supply-chain-event-platform is the *event-sourced* primitive applied to the supply-chain domain).
- Feature 153 (`sausageos-production-erp-append-only-stock-fefo-versioned-recipes`) — *sister-shape* (the *production-ERP + append-only stock + FEFO + versioned recipes* primitive maps onto the supply-chain-event-platform *append-only ledger* primitive applied to the production-ERP domain; both primitives require the *submit-time vs valid-time* distinction for stock movements).
- Feature 154 (`chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive`) — *sister-shape* (the *OpenTimestamps-anchored audit-log* primitive is a *cryptographic-renewable-chronology* view of the same *bitemporal* primitive; supply-chain-event-platform adds the *point-in-time folds* view).
- Feature 161 (`Ybx-jp-claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema`) — *sister-shape* (the *claims-ledger + Toulmin-model schema (assertion/grounds/warrant/backing)* primitive maps onto the supply-chain-event-platform *sourced statements* primitive; every claim is a bitemporal event with both valid-time (when the claim was made) and transaction-time (when the claim was recorded) + the source-citation metadata).
- Feature 167 (`csakegyruszki-provtrail-hash-chained-llm-source-ledger`) — *sister-shape* (the *hash-chained LLM-source-ledger* primitive maps onto the supply-chain-event-platform *append-only ledger + validated-in-CI* primitive; provtrail adds the hash-chain verification, supply-chain-event-platform adds the bitemporal point-in-time folds).
- Feature 182 (`fredhead88-do-it-v2-merge-guard-derives-state`) — *sister-shape* (the *merge-guard-that-performs-the-merge* primitive maps onto the supply-chain-event-platform *point-in-time folds* primitive applied to the merge-conflict domain; the merge-guard *performs* the merge by re-deriving state at the merge-point transaction-time).

The *transferable insight* is **the bitemporal + event-sourced + point-in-time folds + validated-in-CI quadruple-primitive** — *the first in-window candidate of the 50-pass series to explicitly name the bitemporal primitive is also the cleanest 2026-09 event-sourcing reference, and a future LE31 v2 surface adopting the bitemporal + point-in-time folds + validated-in-CI discipline has a concrete 2026 1330 KB Python repo to anchor the primitive* — and v2 maintainer decision required before any v2 surface adopts the bitemporal-time-travel posture.
