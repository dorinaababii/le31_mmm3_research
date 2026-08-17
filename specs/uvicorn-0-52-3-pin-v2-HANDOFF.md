# uvicorn-0-52-3-pin-v2 — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/76-uvicorn-0-52-3-pin.md` before touching any code. Do not
> paste chat excerpts back into the build. This is a **second-pass
> artifact** (feature 76) that re-confirms the `uvicorn 0.52.1 → 0.52.3`
> recommendation from feature 70 (2026-08-16) across the 17-pass
> observation window.

## Frozen identifiers (do not rename)

- Feature ID: `76`
- Slug: `uvicorn-0-52-3-pin-v2`
- Contract file: `features/76-uvicorn-0-52-3-pin.md`
- Bucket: **v2 utility (stack pin-bump)**
- Linear parent: `HMM-89` (Research 2026-08-17 — daily) — **TBD pending Linear issue creation**
- Linear sub-issue: **TBD** (create when the next charter-decided
  pin-bump window opens; see "Linear sub-issue" below)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (PyPI JSON release timestamps +
`Kludex/uvicorn` GitHub `releases.atom` feed — both confirm
`uvicorn 0.52.2` + `0.52.3` in window on 2026-08-13). 17-pass
observation (2026-08-03..2026-08-17) confirms the recommendation is
**unchanged**. Confidence: **high** for the pin-bump mechanics;
**medium** for an immediate bump (two releases same day suggests
urgency but neither is a CVE/security fix).

**Decision: build candidate (defer until charter-decided pin-bump
window).** The slice boundary is hard: one source-file edit (the pin
manifest), zero code changes, zero migrations, zero new dependencies.
Circuit breaker: revert the pin to `uvicorn == 0.52.1`; no other
code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2 utility, the slicing discipline
   inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror
   contract back).
4. `le31-daily-research` (this pick came from the daily research
   job on 2026-08-17).
5. `le31-feature-pipeline` (so the agent understands how this
   slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
<dependency-manifest>  # EDIT: bump uvicorn pin 0.52.1 -> 0.52.3
INDEX.md               # EDIT: update active feature pipeline row
```

The `<dependency-manifest>` is whichever the LE31 project uses
(`requirements.txt`, `pyproject.toml`, `Pipfile`, or `poetry.lock`).
The coding agent must read the repo's existing convention before
touching the manifest.

Zero source files touched (beyond the pin manifest). Zero migrations.
Zero new config keys. Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/76-uvicorn-0-52-3-pin.md` and confirm it
   matches the daily-research report's
   "uvicorn-0-52-3-pin-bump-v2" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature
   pipeline" table and confirm the date (2026-08-17), pick slug
   (`uvicorn-0-52-3-pin-bump-v2`), feature path
   (`features/76-uvicorn-0-52-3-pin.md`), and Linear sub-issue ID.
3. **After the pin bump lands:**
   - Run the LE31 test suite (`pytest` or equivalent) and confirm
     no regressions.
   - Start the LE31 dev server (`uvicorn app.main:app --reload`)
     and confirm the `/api/...` routes serve correctly.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID
`fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`
(label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 76 — uvicorn 0.52.3 pin bump v2`.
- Body: the contract from `features/76-uvicorn-0-52-3-pin.md`
  (or a short summary + the file path).
- Parent: `HMM-89` (Research 2026-08-17 — daily) — **TBD pending Linear issue creation**.
- Status: `Backlog`.

## Rollback path

Revert the pin to `uvicorn == 0.52.1`. Delete this HANDOFF.md and
the `features/76-uvicorn-0-52-3-pin.md` file. Remove the corresponding
row from `INDEX.md`. No other code changes to revert. No data
migration to revert.

## Why this matters (for the coding agent)

The `uvicorn 0.52.1 → 0.52.3` pin bump is the **only** in-window
stack change that affects a LE31 pin and the **only** one where the
diff is pure stability/perf (zttp 0.0.22 → 0.0.24 + WebSocket
close-handshake fix). Two in-window patch releases on the same UTC
day is unusual for the uvicorn project (the prior 0.52.0 → 0.52.1 was
a 3-day gap), suggesting an active maintainer and a real urgency to
get the WebSocket close-handshake fix and HTTP/1.1 perf improvements
in.

**As of 2026-08-17 (17-pass observation), the recommendation is
unchanged.** Across 2026-08-14 through 2026-08-17, no new uvicorn
releases have shipped. The two-release same-day pattern
(0.52.2 + 0.52.3, both 2026-08-13) is the **only** in-window stack
change.

**Risk of NOT bumping**: LE31 v1 is on `uvicorn == 0.52.1`; the
WebSocket close-handshake fix (0.52.2) and HTTP/1.1 request-parsing
perf improvements (0.52.3) are missed. Low-severity risk (no CVE, no
security fix); the fix is operational polish, not correctness.

**Risk of bumping**: the two same-day releases suggest urgency but
neither is a CVE/security fix; bumping mid-window may conflict with
other in-flight work. The defer-to-next-pin-bump-window recommendation
balances these risks.

**Net: defer to the next charter-decided pin-bump window.** Keep the
recommendation visible in the active pipeline; close the artifact
once the bump lands.