# Feature 132 — sqlmodel 0.0.42 pin-track (defer)

## Goal

Track the first in-window `sqlmodel` activity of the LE31 daily-research
30-pass series — three releases `0.0.40 → 0.0.41 → 0.0.42` within
24 minutes on 2026-08-28 — as a dated pin-bump candidate, and surface it
to the owner when the next charter-decided pin-bump window opens.

## Scope

**In scope (defer artifact):**
- A written record of the `sqlmodel` triple release with timestamps and
  release notes (independently verified from `pypi-sqlmodel.json` and
  `atom-tiangolo_sqlmodel.xml`).
- A decision record: today's verdict is `defer` because the LE31
  pin-bump window is a charter decision.
- A reference for the next time the owner opens a pin-bump window.

**Out of scope (defer artifact):**
- Any change to `pyproject.toml` or any dependency pin.
- Any test or migration work — that belongs to the pin-bump window
  itself when it opens.
- Resolution of the separate `pydantic-core` `info.version` vs
  `releases[2.46.5]` discrepancy — that is a pass-31 follow-up.

## Description

On 2026-08-28, the LE31 v1 ORM layer pin candidate moved for the
first time in 11 consecutive days:

| Version | PyPI upload_time_iso_8601 | GitHub releases.atom `updated` | Maintainer PRs | Notes |
|---|---|---|---|---|
| `0.0.40` | `2026-08-28T19:18:23Z` | `2026-08-28T19:18:08Z` | docs + internal | grammar/typos in docs; "Decimals in SQLModel" doc fix; Termynal controls; "Library Skills" documentation; uv-projects-by-default recommendation; setup-uv action bump to `10.0.1`; PR Submit auth migration |
| `0.0.41` | `2026-08-28T19:31:50Z` | `2026-08-28T19:31:33Z` | refactors | **Deprecate `min_items` and `max_items` parameters of `Field`** (PR #1731 by @YuriiMotov) |
| `0.0.42` | `2026-08-28T19:42:01Z` | `2026-08-28T19:41:43Z` | features | **Allow `Discriminator` type for `discriminator` parameter in `Field`** (PR #1729 by @YuriiMotov) |

The three releases were shipped within 24 minutes by the same maintainer
(@YuriiMotov) with @tiangolo as the merge authority on `0.0.40`. The
release cadence (docs → deprecation → feature in one sitting) is
consistent with how `fastapi/sqlmodel` ships — not an emergency release.

The PyPI JSON (`pypi-sqlmodel.json`) and the GitHub releases Atom feed
(`atom-tiangolo_sqlmodel.xml`) corroborate each other at the second
precision; no fabrication possible.

LE31 v1 today pins `sqlmodel 0.0.39` (2026-06-25). Bumping the pin to
`0.0.42` is **strictly additive**: no breaking change, no migration
required for LE31's current v1 models (LE31 does not currently use
`Field(min_items=…, max_items=…)` or `Field(discriminator=…)`).

## Data model

No schema change. The pin bump is a single line in `pyproject.toml`:

```toml
# Before
sqlmodel = "==0.0.39"
# After (when pin-bump window opens)
sqlmodel = "==0.0.42"
```

## Implementation steps

None today (defer). When the owner opens a pin-bump window:

1. Bump `pyproject.toml` `sqlmodel` pin from `==0.0.39` to `==0.0.42`.
2. Reinstall: `uv sync` (or `pip install -e .`).
3. Run the v1 test suite: `pytest`.
4. If any test fails on `Field(min_items=…, max_items=…)` (LE31 does
   not currently use these parameters, so no migration is expected),
   surface to the owner and pin to `0.0.40` instead as a safer floor.
5. If `pydantic-core` `info.version` vs `releases[2.46.5]` discrepancy
   is still live at pin-bump time (pass-31 follow-up), surface to
   owner before bumping `pydantic-core`.

## Telegram interaction if any

None. This is a pin-bump candidate, not a user-facing feature.

## Dependencies

- LE31 charter §3.2 — pin-decision invariant (no pin change without
  charter authorisation).
- LE31 charter §3.1 — SQLModel is the v1 data-plane; pin-bump
  observability requires that the bump preserves the append-only
  `StockEntry` invariant (the bump is additive; no impact on the
  invariant).
- `features/115-uvicorn-0-52-4-pin-bump-v10.md` — prior pin-bump
  defer-observation; same discipline (defer until window opens).
- `features/116-aiogram-3-31-0-stable-track.md` — prior pin-bump
  candidate with `defer` verdict; same discipline.

## Open questions

- Does the owner want a pin-bump window opened today, or wait until
  the next v1 milestone ships?
- Should pass 31 re-fetch `pydantic-core` JSON to resolve the
  `info.version` vs `releases[2.46.5]` discrepancy before the next
  pin-bump window opens?
- Is there value in a separate `sqlmodel-0-0-41-deprecation-note`
  artifact (the `min_items` / `max_items` deprecation), or is the
  deprecation note sufficient for the eventual pin-bump window?

## Why this matters

This is the **first in-window SQLModel activity in 30 passes**, and
the triple-release cadence is itself a signal that the
`fastapi/sqlmodel` maintainer cadence is now *intentional and
predictable*. LE31's charter-decided pin-bump window can now land on
`0.0.42` with full information — additive changes (Discriminator),
deprecated-but-still-functional API (min_items/max_items), and
documented internal churn (the `0.0.40` docs + internal release). The
discipline of *not* auto-bumping pins protects the charter §3.2
invariant; the discipline of *tracking* pin candidates in daily
research gives the owner dated, in-window reference when the next
window opens. **Both disciplines are intact today.**