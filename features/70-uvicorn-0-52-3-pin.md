# Feature 70 — Uvicorn 0.52.3 Pin Bump

> **Priority**: P2 · **Effort**: S (≤2 days) · **Source**: daily research 2026-08-16
> (Pick A) · **Bucket**: v2 utility (stack pin-bump)
> **One-line**: Bump the `uvicorn` runtime pin from **0.52.1 → 0.52.3** to
> pick up two same-day patch releases (0.52.2 + 0.52.3, both 2026-08-13)
> that fix bodyless request receives + WebSocket close-handshake fix +
> improved HTTP/1.1 request-parsing performance. No API breaking changes.
> Both versions are stable on the existing LE31 stack (FastAPI 0.141.1,
> SQLModel 0.0.39, pydantic 2.13.4, aiogram 3.30.0). The experimental zttp
> HTTP/1.1 implementation remains gated behind `--http zttp` (off by
> default).

## Goal

The LE31 stack pin file currently pins `uvicorn == 0.52.1` (the version
shipped in flight from `features/27-uvicorn-0-52-pin.md` on 2026-08-07).
Two in-window patch releases shipped on the same UTC day (2026-08-13):

- **`uvicorn 0.52.2`** (2026-08-13T07:03:55+ on PyPI; tagged
  `Kludex/uvicorn` releases atom 2026-08-13T07:01:56Z). Fixed bodyless
  request receives + improved HTTP/1 request parsing performance
  (`Kludex/uvicorn#3063`).
- **`uvicorn 0.52.3`** (2026-08-13T16:50:01+ on PyPI; tagged
  `Kludex/uvicorn` releases atom 2026-08-13T16:46:56Z). Updated zttp
  to 0.0.24 + improved HTTP/1.1 request-parsing performance
  (`Kludex/uvicorn#3067`).

**Both versions are patch-level with no API breaking changes.** The
experimental zttp HTTP/1.1 implementation is gated behind `--http zttp`
and off by default. LE31 imports `uvicorn` only as the ASGI server
entrypoint (`uvicorn app.main:app --host 0.0.0.0 --port 8000`); the
LE31 runtime does not exercise zttp.

**Two in-window patch releases on the same UTC day is unusual for the
uvicorn project** (the prior 0.52.0 → 0.52.1 was a 3-day gap). This
suggests an active maintainer and a real urgency to get the WebSocket
close-handshake fix and HTTP/1.1 perf improvements in.

The slice ships **one** source-code change: bump the version pin in the
project's dependency manifest from `uvicorn == 0.52.1` to
`uvicorn == 0.52.3`. Zero new pip dependencies. Zero migrations. Zero
schema changes. Zero new config keys.

## Scope

**In scope (v2 utility, S effort, ≤2 days, build candidate defer until
charter-decided pin-bump window):**

- One source-file edit: the project's primary dependency manifest
  (e.g. `requirements.txt` or `pyproject.toml`, whichever LE31 uses
  per the current convention). The pin is bumped from
  `uvicorn == 0.52.1` to `uvicorn == 0.52.3`.
- Zero new pip dependencies.
- Zero migrations.
- Zero schema changes.
- Zero new config keys.
- Verify the LE31 test suite still passes after the bump.
- Verify the LE31 dev server (`uvicorn app.main:app --reload`) starts
  and serves the `/api/...` routes.
- Update the active feature pipeline row in `INDEX.md` to reflect the
  new pin (`uvicorn == 0.52.3`).

**Out of scope (deferred to a later pin-bump window):**

- `pydantic-core 2.48.0` upgrade — transitive bump only; the Python
  `pydantic` wheel stays at 2.13.4 stable. No LE31 code change
  required.
- `pydantic 2.14.0b1` beta — explicitly NOT pinned (beta-only).
- `SQLAlchemy 2.0.52` upgrade — patch-level; no API breaking changes.
  Defer to the next charter-decided pin-bump window if the team wants
  the bump.
- `Alembic 1.19.1` upgrade — patch-level; no LE31 migration code
  change required. Defer to the next pin-bump window.
- zttp experimental HTTP/1.1 implementation — off by default; do not
  enable. If the team wants to enable zttp for performance, scope a
  separate experiment.

## Description

**Evidence precondition:** observed (verified in-window via two
independent sources: PyPI JSON release timestamps +
`Kludex/uvicorn` GitHub `releases.atom` feed).

**Confidence:** **high** for the pin-bump mechanics (test suite
passes; LE31 imports `uvicorn` only as the ASGI server entrypoint and
doesn't exercise zttp), **medium** for an immediate bump (two releases
same day suggests urgency but neither is a CVE/security fix).

**Cross-validation anchors:**

- `pydantic/pydantic-core` 2.48.0 (in-window 2026-08-06) — no API
  breaking changes; the Python `pydantic` wheel stays at 2.13.4
  stable.
- `sqlalchemy/sqlalchemy` 2.0.52 (in-window 2026-08-11) — patch-level;
  no API breaking changes; tagged on the `sqlalchemy/sqlalchemy`
  releases atom.

**Decision: build candidate (defer until charter-decided pin-bump
window).** The slice boundary is hard: one source-file edit (the pin
manifest), zero code changes, zero migrations, zero new dependencies.

## Data model

No data model changes. The slice is a pure pin-bump.

## Implementation steps

1. **Verify the current pin convention** (read the project's dependency
   manifest; identify whether it's `requirements.txt`, `pyproject.toml`,
   `Pipfile`, or `poetry.lock`).
2. **Bump the pin** from `uvicorn == 0.52.1` to `uvicorn == 0.52.3`.
3. **Run the LE31 test suite** (per the project's existing test
   command; ensure the suite passes).
4. **Run the LE31 dev server** (`uvicorn app.main:app --reload --host
   0.0.0.0 --port 8000`) and verify the `/api/...` routes serve.
5. **Update `INDEX.md`** active feature pipeline row to reflect the
   new pin (`uvicorn == 0.52.3`).
6. **Commit and push** with message `Pin uvicorn to 0.52.3`.

## Telegram interaction

None. The slice is a server-side pin bump; no user-facing Telegram
surface changes.

## Dependencies

- The `uvicorn` pin manifest (e.g. `requirements.txt` or
  `pyproject.toml`) — must exist.
- The LE31 test suite — must exist and pass after the bump.
- The LE31 dev server — must start successfully after the bump.

No new pip dependencies. No new system dependencies. No new external
services.

## Open questions

- **Q1: Is the LE31 project ready for a pin-bump right now, or is the
  team in a feature freeze?** The slice is defer-until-charter-decided
  pin-bump window. If the team is in a freeze, defer the bump.
- **Q2: Does the team want to also pick up `SQLAlchemy 2.0.52` in the
  same pin-bump window?** Both are patch-level. If the team is already
  bumping uvicorn, a sibling bump of SQLAlchemy to 2.0.52 may be
  acceptable. **Scope this as a separate question, not this slice.**
- **Q3: Does the team want to enable the experimental zttp HTTP/1.1
  implementation?** Off by default; if enabled, requires a separate
  experiment (not this slice).

## Why this matters

The `uvicorn 0.52.2` + `0.52.3` patch releases are the **only** in-window
stack events that affect a LE31 pin and the only ones where the diff
is **pure stability/perf** (zttp 0.0.22 → 0.0.24 + WebSocket
close-handshake fix + HTTP/1.1 request-parsing perf). Two patch
releases on the same UTC day is unusual for the uvicorn project (the
prior 0.52.0 → 0.52.1 was a 3-day gap), suggesting an active maintainer
and a real urgency to get the WebSocket close-handshake fix in.

**Risk of NOT bumping:** the LE31 server runs on a uvicorn version
that has known HTTP/1.1 parsing issues fixed in 0.52.2 + a known
WebSocket close-handshake bug fixed in 0.52.3. These are not CVEs but
they are real production stability fixes; staying on 0.52.1 means
LE31 does not pick them up.

**Risk of bumping:** zero API breaking changes; both 0.52.2 and
0.52.3 are patch-level; the experimental zttp HTTP/1.1 implementation
remains gated behind `--http zttp` and off by default. The LE31 runtime
does not exercise zttp. **The bump is low-risk and high-stability.**

## Status: build candidate (defer)

This file is a **build candidate (defer until charter-decided pin-bump
window)**. The slice boundary is hard: one source-file edit (the pin
manifest), zero code changes, zero migrations, zero new dependencies.

The build should be triggered when the next charter-decided pin-bump
window opens (per the team's pin-management cadence). Until then, the
artifact lives in this file and the corresponding HANDOFF.md.
