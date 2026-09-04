# HANDOFF — 143-volfpeter-fasthx-htmx-fastapi-declarative-ssr

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-09-04
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/143-volfpeter-fasthx-htmx-fastapi-declarative-ssr.md`
**LE31 feature gate verdict**: defer (LE31 v1's waiter web UI is already FastAPI + Jinja2 + HTMX integration done by hand; `fasthx` is a wrapper utility that is not required. The peer value is *structural evidence of FastAPI+HTMX rendering activity in 2026*, not *adoption*.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the `volfpeter/fasthx` GitHub repo (730★, 22 forks, MIT, Python, declarative FastAPI+HTMX utility, **pushed 2026-08-27T13:49:53Z (in-window by push only; created 2024-01-24)**, by `volfpeter`) + its two same-author siblings (`volfpeter/htmy` 401★ async pure-Python rendering engine pushed 2026-09-02; `volfpeter/holm` 132★ Next.js-style hypermedia on FastAPI pushed 2026-09-03) as a dated, in-window **structural-evidence peer family** for the FastAPI+HTMX rendering pattern.

If the trigger condition (LE31 first proposes a v2 surface that wants declarative HTMX-on-FastAPI integration, OR a future owner decision questions whether the FastAPI+HTMX rendering pattern is healthy in 2026) is met, the external coding agent should:

1. Load this artifact and the parent brainstorm report (`/opt/data/le31-brainstorm-2026-09-04.md`).
2. Load the `fasthx` repo: `https://github.com/volfpeter/fasthx` — README + `docs/` if available.
3. Load the same-author siblings: `https://github.com/volfpeter/htmy` and `https://github.com/volfpeter/holm`.
4. Load the companion feature 142 (`feldroy/air`) — both are FastAPI+HTMX peers surfaced on the same brainstorm pass.
5. Re-run the LE31 feature gate with `fasthx`'s README in hand.
6. **Decide whether the proposed v2 surface benefits from `fasthx`'s declarative `HX-Trigger` + `(component, response)` pattern**. If the v2 surface has many HTMX routes with `HX-Trigger` interactions (e.g., a detailed owner-facing history surface), the declarative style reduces boilerplate. If the v2 surface has only a few routes, hand-written integration is fine.
7. **If `fasthx` is proposed for adoption**: pin to a specific version, add to `requirements-fasthx.txt` (do not pin to v1 yet), and refactor one existing route to use `fasthx`'s pattern. Compare against the hand-written equivalent. If the refactor is meaningfully smaller across multiple routes, propose a v2-wide adoption; if not, document the comparison and defer.
8. **If `fasthx` is not adopted**: document the comparison and defer. No charter §3.1 change is needed because `fasthx` is a utility on top of FastAPI + Jinja2 + HTMX, all of which are already charter §3.1 components.
9. **Pilot on one route first**. Do not adopt `fasthx` project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/143-volfpeter-fasthx-htmx-fastapi-declarative-ssr.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-09-04.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-09-04/gh/htmx-languagepython-stars3E1-archivedfalse.json` (where `volfpeter/fasthx` is listed at `pushed_at=2026-08-27T13:49:53Z`, 730★, MIT, Python) + same file for `volfpeter/htmy` (401★) + `volfpeter/holm` (132★).
- **`fasthx` repo**: `https://github.com/volfpeter/fasthx` (parent-fetched 2026-09-04 metadata).
- **Same-author siblings**:
  - `volfpeter/htmy` — `https://github.com/volfpeter/htmy` (401★, pushed 2026-09-02T14:28:57Z, MIT, Python)
  - `volfpeter/holm` — `https://github.com/volfpeter/holm` (132★, pushed 2026-09-03T09:29:24Z, MIT, Python)
- **Companion artifacts**:
  - `features/142-feldroy-air-fastapi-htmx-ai-write-framework.md` (same-pass FastAPI+HTMX peer)
  - `features/23-sse-cook-channel.md` (FastAPI SSE — same substrate)
  - `features/16-htmx-admin.md` (defer — HTMX-on-server-rendering)
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.2 (open-source dependency whitelist)**: would need an owner decision before any `fasthx` adoption.

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.4 observable evidence, §3.4.4 the non-technical owner).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The peer-awareness surfaced by this defer is:

- **Repo family**: `volfpeter/fasthx` (utility) + `volfpeter/htmy` (engine) + `volfpeter/holm` (framework)
- **Stars / forks / licence / language**: 730★/22 forks / 401★/9 forks / 132★/3 forks, all MIT, all Python
- **Created / pushed**: 2024-01-24 / 2026-08-27 (fasthx), 2024-09-? / 2026-09-02 (htmy), 2024-09-? / 2026-09-03 (holm) — **all in-window by push only**
- **Author**: `volfpeter` (volker peter), Hungarian Python developer
- **Stack match**: FastAPI ✅ / Jinja2 ✅ / HTMX ✅ / Python 3.13 ✅ (all three repos)

LE31 v1 doesn't need this peer for code today. The defer artifact does **not** propose a `fasthx` adoption. It surfaces the *peer family* for future use.

## Rollback path

This is a documentation-only artifact. There is no code to roll back. If the LE31 owner decides the peer-awareness is not worth carrying, the file can be deleted with no operational impact.

## Verification protocol reference

For the LE31 seven-check feature gate, see `skills/le31-conventions/SKILL.md` §"Feature gate". For GitHub repo verification, see `skills/le31-research/SKILL.md` (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON; the 2026-08-28 subagent fabrication incident is the reference failure mode).