# peer-architecture-comparison — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/31-peer-ledger-compare.md` before touching any code. Do not
> paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `31`
- Slug: `peer-architecture-comparison` (with feature slug `peer-ledger-compare`)
- Contract file: `features/31-peer-ledger-compare.md`
- Research artefact: `research/13-peer-architecture-comparison.md`
- Bucket: v1 (research artefact + ≤ 1 nullable column on `MenuItem`/`Batch`)
- Linear parent: HMM-28 (Research 2026-08-05 — daily)
- Linear sub-issue: HMM-30, `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "LE31 gate verdict". **Decision: build.** No
failed checks.

Evidence precondition: **observed** (two production peers in window with
full READMEs: `illustraton916/vanhamylly-api`, `nkieu-config/branchbrew-cafe-erp`).
Confidence: **medium-high**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).
6. `le31-research` (so the agent understands the `research/` folder's
   format and how peer-architecture-comparison fits alongside the existing
   `research/00..12` files).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
research/13-peer-architecture-comparison.md       # NEW — the comparison doc
backend/app/models.py                            # OPTIONAL — ≤ 1 nullable column on MenuItem or Batch
backend/README.md                                # OPTIONAL — note any new column if added
```

No new tables. No Alembic migration (charter §3.2 — `init_db()` for v1).
At most one nullable column; default is no column change.

## Endpoints and contracts added

None. This slice produces a research artefact and possibly one nullable
column. No new endpoints, no new bot commands, no new schema tables.

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all six mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Read the three peer sources**:
   - `https://github.com/illustraton916/vanhamylly-api` — README
     "Architecture" and "Money" sections; confirm "integer cents only,
     server-calculated totals" claim.
   - `https://github.com/nkieu-config/branchbrew-cafe-erp` — README
     intro and "Why I built this" sections; confirm "double-entry general
     journal, 150 orders/sec" claim.
   - `https://github.com/TidalBeast37/restaurant-inventory-rop` —
     README; confirm "current-stock table, not append-only ledger" claim.
3. **Read LE31's own pattern**:
   - `features/03-kitchen-stock-tracker.md` — the `StockEntry` pattern.
   - `features/26-reorder-point-on-stockentry.md` — the ROP layer that
     sits on top of `StockEntry`.
   - Charter §4.3 — the killer pattern in canonical form.
4. **Write the comparison doc** at `research/13-peer-architecture-comparison.md`
   with three sections:
   - Section 1: peer ledger patterns observed (≤ 3 paragraphs, one per peer).
   - Section 2: LE31's current `StockEntry` pattern restated (≤ 1 paragraph).
   - Section 3: verdict + optional column extension if warranted (default
     verdict: "stay narrow"; optional extension: `MenuItem.last_reorder_at
     TIMESTAMPTZ NULL` if the ROP comparison motivates it).
5. **Optional column check**: if section 3 motivates a column, confirm it
   is nullable, default `NULL`, and the existing `init_db()` pattern can
   add it (see feature 25, 26, 27 for prior art on nullable columns).
6. **Append-only invariant check**: confirm no `StockEntry` UPDATE or
   DELETE is introduced. The narrow pattern is unchanged.
7. **Commit + push**: branch is `main`. Commit message:
   `Add research/13-peer-architecture-comparison.md (Pick B 2026-08-05)`.
   If the optional column is added, a second commit:
   `Feature 31: <column-name> on <table> (Pick B 2026-08-05)`.

## Rollback / feature-removal path

- Delete `research/13-peer-architecture-comparison.md`.
- If a column was added, drop it from `backend/app/models.py` and
  `init_db()`.
- No data migration, no data retention — the doc is a Markdown file;
  the optional column is nullable, so existing rows keep their NULL
  default.

## What remains safe if removed

- No customer data, no historical state.
- The append-only `StockEntry` ledger is unaffected.
- The explicit-state rule is unaffected (no `OrderItem` transition is
  automated by this slice).
- Reading the peers' READMEs does not alter any LE31 state.

## Sign-off gap

External coding agent must mirror the six frozen identifiers (Feature ID,
slug, contract file path, bucket, Linear parent HMM-28, Linear sub-issue
HMM-30) back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** — do
not silently rename.
