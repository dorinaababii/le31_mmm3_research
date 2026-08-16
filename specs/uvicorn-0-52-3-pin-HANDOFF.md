# uvicorn-0-52-3-pin — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/70-uvicorn-0-52-3-pin.md` before touching any code. Do not
> paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `70`
- Slug: `uvicorn-0-52-3-pin`
- Contract file: `features/70-uvicorn-0-52-3-pin.md`
- Bucket: **v2 utility (stack pin-bump)**
- Linear parent: `HMM-85` (Research 2026-08-16 — daily)
- Linear sub-issue: **TBD** (create when the next charter-decided
  pin-bump window opens; see "Linear sub-issue" below)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (PyPI JSON release timestamps +
`Kludex/uvicorn` GitHub `releases.atom` feed — both confirm
`uvicorn 0.52.2` + `0.52.3` in window on 2026-08-13). Confidence:
**high** for the pin-bump mechanics; **medium** for an immediate bump
(two releases same day suggests urgency but neither is a
CVE/security fix).

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
   job on 2026-08-16).
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
editing.

Zero migrations. Zero schema changes. Zero new config keys. Zero new
pip dependencies.

## Verification protocol

After the pin bump:

1. **Run the LE31 test suite** (per the project's existing test
   command). The suite must pass.
2. **Run the LE31 dev server** (`uvicorn app.main:app --reload
   --host 0.0.0.0 --port 8000`). The server must start successfully.
3. **Hit one `/api/...` route** (e.g. `GET /api/health` if it exists,
   or `GET /api/menu`). The route must return a valid response.
4. **Hit one WebSocket route if any** (LE31 may or may not have a
   WebSocket surface; if it does, verify the close-handshake fix
   is working per `Kludex/uvicorn#3063`).

The pin bump is verified when:

- The test suite passes.
- The dev server starts.
- The `/api/...` route returns a valid response.

If any of these fail, revert the pin to `uvicorn == 0.52.1` and
investigate.

## Linear sub-issue

When the next charter-decided pin-bump window opens:

- Create a Linear sub-issue in project `le31 v1 — Core MVP`
  (project ID `fdb233e0-044c-4425-8574-1b72c3787563`) with label
  `Feature` (label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).
- Title: `Feature 70 — uvicorn 0.52.3 pin bump`.
- Body: the contract from `features/70-uvicorn-0-52-3-pin.md` (or
  a short summary + the file path).
- Parent: `HMM-85` (Research 2026-08-16 — daily).
- Status: `Backlog`.

## Rollback path

Revert the `<dependency-manifest>` pin to `uvicorn == 0.52.1`. No
other code changes to revert. No data migration to revert (no
schema changes were made).

## Why this matters (for the coding agent)

The `uvicorn 0.52.2` + `0.52.3` patch releases are the **only**
in-window stack events that affect a LE31 pin and the only ones
where the diff is **pure stability/perf** (zttp 0.0.22 → 0.0.24 +
WebSocket close-handshake fix + HTTP/1.1 request-parsing perf).
Two patch releases on the same UTC day is unusual for the uvicorn
project (the prior 0.52.0 → 0.52.1 was a 3-day gap), suggesting an
active maintainer and a real urgency to get the WebSocket
close-handshake fix in.

**Risk of NOT bumping:** the LE31 server runs on a uvicorn version
that has known HTTP/1.1 parsing issues fixed in 0.52.2 + a known
WebSocket close-handshake bug fixed in 0.52.3. These are not CVEs
but they are real production stability fixes; staying on 0.52.1
means LE31 does not pick them up.

**Risk of bumping:** zero API breaking changes; both 0.52.2 and
0.52.3 are patch-level; the experimental zttp HTTP/1.1
implementation remains gated behind `--http zttp` and off by
default. The LE31 runtime does not exercise zttp. **The bump is
low-risk and high-stability.**
