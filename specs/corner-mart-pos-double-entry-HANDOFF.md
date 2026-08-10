# corner-mart-pos-double-entry — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/54-corner-mart-pos-double-entry.md` before touching any code. This is a
> **parking-lot** slice — no build, no commit, no follow-up. The
> artifact exists so when the operator does report feature 39
> (`owner-daily-recap-telegram`) or feature 45 (`print-fallback-floor-sheet`)
> as inadequate, the path is documented and the reference fork is on file.

## Frozen identifiers (do not rename)

- Feature ID: `54`
- Slug: `corner-mart-pos-double-entry`
- Contract file: `features/54-corner-mart-pos-double-entry.md`
- Bucket: parking-lot (no build)
- Linear parent: HMM-57 (Brainstorm 2026-08-10 — daily)
- Linear sub-issue: HMM-60 (created, status Backlog, label `Feature`, project `le31 v1 — Core MVP`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "LE31 gate verdict per idea" → Pick C.
**Decision: parking-lot.** No failed checks; the gate is **deferred** until the operator reports feature 39 or feature 45 as inadequate, or asks for a clean third-party reference for the owner-facing reports surface.

Evidence precondition: **inferred** (the htmx+SQLite+double-entry pattern works for a single-store POS; today's `channyeintun/corner-mart-pos` is *the* Go reference). Confidence: **medium** for the pattern's general applicability, **low** for the LE31-specific JTBD.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

**None.** This is a parking-lot entry. The "files the slice touches" section is empty because no code is written, no migration is created, no endpoint is added.

If/when the parking-lot entry is promoted to a real feature (see "Promotion criteria" below), the files would be:
- A Python re-implementation of the `corner-mart-pos` Go binary (single-binary + no-build + pyinstaller).
- A FastAPI server-rendered reports surface using htmx + SQLite (the existing `index.html` mock-up is the starting point).
- A double-entry accounting module on top of the existing `Order` and `Payment` tables (the existing tip-reconciliation logic in feature 05 is the starting point).
- An Alembic migration adding the `journal_entries` table (if a separate table is preferred over extending the existing `Order` table).

## Endpoints and contracts added

**None.** This is a parking-lot entry. No new HTTP endpoints, no new SQLModel tables, no new bot commands.

## Verification protocol (end-to-end acceptance path)

**None.** This is a parking-lot entry. There is no end-to-end acceptance path because no code is written.

If/when the parking-lot entry is promoted to a real feature, the verification protocol would be:
1. Confirm the operator has reported feature 39 or 45 as inadequate.
2. Confirm the team has reviewed the LE31 charter and confirmed that the change does not violate any invariants.
3. Run `pytest backend/tests/test_corner_mart_port.py` (the new test suite for the Python re-implementation) — must pass all cases.
4. Run `pyinstaller --onefile backend/app/main.py` — must produce a single binary that runs without Docker on the operator's laptop.
5. Confirm the binary's `localhost:8080/reports` surface renders the owner's daily recap (replacing or supplementing the existing feature 39 Telegram message).
6. Confirm the binary's `localhost:8080/floor-sheet` surface renders the printable floor sheet (replacing or supplementing the existing feature 45).

## Rollback / feature-removal path

- **No rollback needed.** No code was written; there is nothing to roll back.
- If the parking-lot entry is promoted and the resulting feature is later rejected, the rollback path would be: `rm -rf the-new-feature-dir`, revert the migration, revert the routes, revert the binary build step.

## What remains safe if removed

- **Everything.** Removing a parking-lot entry is removing a documentation artifact; no code, no migration, no endpoint, no test. The LE31 codebase is unaffected.

## Promotion criteria (for moving from parking-lot to a real feature)

The parking-lot entry is promoted to a real feature when **all** of the following are true:

1. The operator reports feature 39 (`owner-daily-recap-telegram`) or feature 45 (`print-fallback-floor-sheet`) as inadequate (e.g. "the recap is too verbose", "the floor sheet doesn't include the prep board", "I want a printable PDF, not an HTML page").
2. The operator explicitly asks for a clean third-party reference (or the developer judges that a clean rewrite is the right path).
3. The team has the bandwidth for a 3-day Python re-implementation of the Go reference (the stack-mismatch is real; a port is required).
4. The team has reviewed the LE31 charter and confirmed that the change does not violate any invariants (no stack change without an explicit charter decision).

Until all four conditions are met, the parking-lot entry stays on file as a *reference*, not a *plan*.

If/when promoted, the resulting feature would have its own Feature ID (54 → promoted to e.g. 55), its own contract file, its own HANDOFF, its own Linear sub-issue, and its own implementation. The parking-lot entry would be marked "promoted" in the INDEX and removed from the parking-lot bucket.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-57)
back to the research-side Hermes before implementing. If they
conflict, **stop and ask** — do not silently rename.

Because this is a parking-lot entry, the implementation is intentionally absent. The sign-off gap applies only if/when the entry is promoted; until then, the gap is moot.
