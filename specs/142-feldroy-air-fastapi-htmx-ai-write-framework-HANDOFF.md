# HANDOFF — 142-feldroy-air-fastapi-htmx-ai-write-framework

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-09-04
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/142-feldroy-air-fastapi-htmx-ai-write-framework.md`
**LE31 feature gate verdict**: defer (LE31 v1 does not need to *use* `air`; FastAPI + Jinja2 + HTMX integration is straightforward without a wrapper framework. The peer value is *structural evidence of substrate activity in 2026*, not *adoption*.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the `feldroy/air` GitHub repo (915★, 97 forks, MIT, Python, FastAPI+Pydantic+HTMX+Starlette, **pushed 2026-09-03T22:49:43Z (in-window by push only; created 2015-12-11)**, by Audrey Feldroy + Daniel Feldroy of *Two Scoops of Django*) as a dated, in-window **structural-evidence peer** for LE31's chosen stack.

If the trigger condition (LE31 first proposes a v2 surface that wants AI-codegen-target-friendly waiter/cook/owner UI screens, OR a future owner decision questions whether the FastAPI+HTMX substrate is healthy in 2026) is met, the external coding agent should:

1. Load this artifact and the parent brainstorm report (`/opt/data/le31-brainstorm-2026-09-04.md`).
2. Load the `air` repo: `https://github.com/feldroy/air` — README + `docs/` if available.
3. Load the companion feature 143 (`volfpeter/fasthx`) — both are FastAPI+HTMX peers surfaced on the same brainstorm pass.
4. Re-run the LE31 feature gate with `air`'s README in hand.
5. **Decide whether the proposed v2 surface benefits from `air`'s "designed for AI to write" framing**. If the v2 surface has AI-generated UI (e.g., a natural-language summary becomes a Telegram send or a waiter recommendation card), `air` is purpose-built for that use case. If the v2 surface is hand-written UI (as v1 is today), `air` adds no value.
6. **If `air` is proposed for adoption**: pin to a specific version, add to `requirements-air.txt` (do not pin to v1 yet), and refactor one existing route to use `air`'s pattern. Compare against the hand-written equivalent. If the refactor is meaningfully smaller, propose a v2-wide adoption; if not, document the comparison and defer.
7. **If `air` is not adopted**: document the comparison and defer. No charter §3.1 change is needed because `air` is a wrapper, not a stack change.
8. **Pilot on one route first**. Do not adopt `air` project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/142-feldroy-air-fastapi-htmx-ai-write-framework.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-09-04.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-09-04/gh/htmx-languagepython-stars3E1-archivedfalse.json` (where `feldroy/air` is listed at `pushed_at=2026-09-03T22:49:43Z`, 915★, MIT, Python).
- **`air` repo**: `https://github.com/feldroy/air` (parent-fetched 2026-09-04 metadata).
- **Companion artifacts**:
  - `features/143-volfpeter-fasthx-htmx-fastapi-declarative-ssr.md` (same-pass FastAPI+HTMX peer)
  - `features/23-sse-cook-channel.md` (FastAPI SSE — same substrate)
  - `features/16-htmx-admin.md` (defer — HTMX-on-server-rendering)
  - `features/106-rafood-api-fastapi-sqlmodel-context-arch.md` (FastAPI+SQLModel context arch — different peer)
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.2 (open-source dependency whitelist)**: would need an owner decision before any `air` adoption.

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.4 observable evidence, §3.4.4 the non-technical owner).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The peer-awareness surfaced by this defer is:

- **Repo**: `feldroy/air` — *The first web framework designed for AI to write — Built on Python, FastAPI, Pydantic, and HTMX*
- **Stars / forks / licence / language**: 915★ / 97 forks / MIT / Python
- **Created / pushed**: 2015-12-11 (off-window by ~11 years) / **2026-09-03T22:49:43Z (in-window by push only)**
- **Author**: Audrey Feldroy + Daniel Feldroy (Two Scoops of Django)
- **Stack match**: FastAPI ✅ / Pydantic ✅ (via SQLModel) / Starlette ✅ (via FastAPI) / HTMX ✅ / Python 3.13 ✅

LE31 v1 doesn't need this peer for code today. The defer artifact does **not** propose an `air` adoption. It surfaces the *peer* for future use.

## Rollback path

This is a documentation-only artifact. There is no code to roll back. If the LE31 owner decides the peer-awareness is not worth carrying, the file can be deleted with no operational impact.

## Verification protocol reference

For the LE31 seven-check feature gate, see `skills/le31-conventions/SKILL.md` §"Feature gate". For GitHub repo verification, see `skills/le31-research/SKILL.md` (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON; the 2026-08-28 subagent fabrication incident is the reference failure mode — subagent reported `pronto` as 42★/15f when raw JSON said 43★/17f, and omitted an AGPL-3.0 licence that is a charter §3.2 blocker).