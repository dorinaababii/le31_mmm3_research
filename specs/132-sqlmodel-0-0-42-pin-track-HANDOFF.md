# HANDOFF — 132-sqlmodel-0-0-42-pin-track

**Status**: defer (pin-bump candidate, no build today)
**Date**: 2026-08-29
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/132-sqlmodel-0-0-42-pin-track.md`
**LE31 feature gate verdict**: defer (charter §3.2 pin-decision invariant requires charter authorisation; no pin-bump window is open today)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a
dated, in-window pin-bump candidate (`sqlmodel 0.0.40 → 0.0.41 → 0.0.42`
released 2026-08-28) for the next time the LE31 owner opens a
charter-decided pin-bump window.

If the trigger condition (pin-bump window opens) is met, the
external coding agent should:

1. Bump `pyproject.toml` `sqlmodel` pin from `==0.0.39` to `==0.0.42`.
2. Run `uv sync` (or `pip install -e .`).
3. Run the v1 test suite.
4. Surface any `Field(min_items=…, max_items=…)` test failures to the
   owner (LE31 does not currently use these parameters; none
   expected) and pin to `0.0.40` as a safer floor.
5. Verify the `pydantic-core` `info.version` vs `releases[2.46.5]`
   discrepancy status (see Recommendations #6 in the parent report).

If the trigger condition is **not** met, do nothing. The defer
artifact can be safely ignored until the owner opens a pin-bump
window.

## Mandatory inputs

- **Active feature**: `features/132-sqlmodel-0-0-42-pin-track.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-08-29.md`
- **Raw fetches**: `/tmp/le31-daily-2026-08-29/pypi-sqlmodel.json` and `/tmp/le31-daily-2026-08-29/atom-tiangolo_sqlmodel.xml`
- **Prior pin-bump discipline**: `features/115-uvicorn-0-52-4-pin-bump-v10.md` (no quota-filling)
- **Charter §3.2 (pin-decision invariant)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the
  hard invariants (charter §3.2 pin-decision).
- `le31-v1-feature-pattern` — for the canonical contract shape.
- `le31-research` — for the source-of-truth discipline on PyPI/GitHub
  release verification.
- `development` — for the generic code-change workflow.

The agent must NOT load `le31-feature-pipeline` (this is a defer
artifact, not a build pipeline candidate).

## Frozen contract

The pin-bump candidate is:

- `sqlmodel`: `==0.0.39` → `==0.0.42`

The three releases on 2026-08-28 are:

| Version | Upload (PyPI) | Updated (GitHub) | Maintainer | Type |
|---|---|---|---|---|
| `0.0.40` | `2026-08-28T19:18:23Z` | `2026-08-28T19:18:08Z` | @YuriiMotov / @tiangolo | Docs + Internal |
| `0.0.41` | `2026-08-28T19:31:50Z` | `2026-08-28T19:31:33Z` | @YuriiMotov | Refactors (deprecate `min_items`/`max_items`) |
| `0.0.42` | `2026-08-28T19:42:01Z` | `2026-08-28T19:41:43Z` | @YuriiMotov | Features (Discriminator for Field) |

Two sources corroborate (PyPI JSON + GitHub releases.atom) at second
precision. No fabrication possible.

## Files to touch (when pin-bump window opens)

- `/opt/data/le31_mmm3_research_work/pyproject.toml` — single line
  change to bump `sqlmodel` pin.
- (No other files expected to require changes.)

## Verification protocol

When the pin-bump window opens:

1. Confirm the pin bump via `uv pip show sqlmodel` (or `pip show
   sqlmodel`) — must report `0.0.42`.
2. Run the v1 test suite — all tests must pass.
3. Run any LE31-specific manual smoke test on the `StockEntry`
   ledger (append, read, derived-current-stock computation).
4. Verify the `pydantic-core` `info.version` vs `releases[2.46.5]`
   discrepancy status before bumping `pydantic-core` if a
   pin-bump is to land on `pydantic-core` too.

## Rollback path

If the pin bump causes regressions:

1. Revert `pyproject.toml` pin from `==0.0.42` to `==0.0.40` (the
   safest floor — docs + internal only, no API change).
2. Re-run tests.
3. Surface to the owner.

Pin bump is fully reversible — single line change, no migration
required, no schema change.

## Sign-off gap

No build today. The defer artifact does not require sign-off from
the owner; it surfaces a dated, in-window pin candidate and waits
for the next pin-bump window.

If the owner opens a pin-bump window, the external coding agent
must mirror this contract back to the owner before implementing
and stop if it cannot.