# visual-table-layout-v2 — HANDOFF

> **Slice for the coding agent.** Read this *and* `features/24-visual-table-layout-v2.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `24`
- Slug: `visual-table-layout-v2`
- Contract file: `features/24-visual-table-layout-v2.md`
- Bucket: v1 polish (extends feature 01; no new model, no new endpoint)
- Linear parent: HMM-16 (Research 2026-08-03 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Decision: **build**. All seven checks answered in the contract file under
"LE31 gate verdict". No failed checks. Evidence precondition: **observed**
(LE31 mock-up already ships a colored grid; competitor activity confirms
the pattern). Confidence: **high**.

Conflict surfaced and resolved: charter §3.2 forbids drag-and-drop table
*editor* in v1; runtime drag-to-reorder **without persistence** is in scope
because it is a display-only polish, not a layout-authoring admin tool.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` (project invariants).
2. `le31-v1-feature-pattern` (v1 contract shape).
3. `le31-handoff-spec` (frozen-contract discipline).
4. `le31-daily-research` (where this pick came from).

## Files the slice touches

```
backend/app/config.py                    # NEW SECTIONS constant
backend/app/routers/tables.py             # extend /api/tables response with sections[]
index.html                               # rewrite the floor grid; add waiter badge; add drag JS
```

No new tables. No new columns. No migration.

## Endpoints and contracts added

- `GET /api/tables` — response gains a sibling `sections: ["main","patio","bar"]`
  field. Each `Table` already carries `section`; no schema change.

## Verification protocol (end-to-end acceptance path)

1. Load all four mandatory LE31 skills.
2. Mirror the five frozen identifiers back to research-side Hermes before
   implementing.
3. Run `uvicorn app.main:app --reload`; open `/docs` and confirm `/api/tables`
   response now includes `sections`.
4. Open `/` on a tablet-sized viewport — confirm section dividers render.
5. Seat a party with a known `server_id` — confirm the waiter-badge
   initials appear on that table card.
6. Drag a table card to a new spot within its section — confirm the move
   is reflected locally; reload — confirm the layout resets to the
   server-derived order (no persistence regression).
7. Tap a free table — confirm the existing seat-party modal still opens
   (regression for feature 01).
8. Visual: confirm colors (green / yellow / orange / red / gray) still
   match the state machine in feature 01.

## Rollback / feature-removal path

- Revert `index.html` to the previous single-grid version.
- Revert `/api/tables` to the prior response shape (drop the `sections`
  field; drop the `SECTIONS` constant).
- No data migration, no data retention.

## What remains safe if removed

- Tables still load in the original order.
- The seat-party flow is unchanged.
- No customer data, no historical state.

## Sign-off gap

External coding agent must mirror the five frozen identifiers (Feature ID,
slug, contract file path, bucket, Linear parent HMM-16) back to the
research-side Hermes before implementing. If any conflict, **stop and ask**.