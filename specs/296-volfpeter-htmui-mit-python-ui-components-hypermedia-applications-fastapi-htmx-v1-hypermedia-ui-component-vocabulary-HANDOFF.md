# HANDOFF — 296-volfpeter-htmui-mit-python-ui-components-hypermedia-applications-fastapi-htmx

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-10-13
**Active feature path**: `/opt/data/le31_mmm3_research/features/296-volfpeter-htmui-mit-python-ui-components-hypermedia-applications-fastapi-htmx-v1-hypermedia-ui-component-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v1 does not need to *use* `volfpeter/htmui`; the LE31 v1 surface is a single-restaurant waiter web UI = ~5 routes today, which can be hand-written using FastAPI+HTMX without a discrete-component-pack. The peer value is *structural evidence of substrate activity in 2026 + named architectural vocabulary*, not *adoption*.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the `volfpeter/htmui` GitHub repo (MIT, **13★ / 1⑂** = the **highest in-window 2026 star count of any net-new Python permissive in-domain non-watchlist of the 75-pass series**, language Python, **pushed 2026-10-12T16:56:17Z (in-window by push only; created 2026-02-23 = ~8-month-old repo with in-window push)**, by `volfpeter` = same author as feature 143 `volfpeter/fasthx` = the sister-shape declarative-SSR-framework) as a dated, in-window **structural-evidence peer** for LE31's chosen v1 hypermedia-UI-component-pack substrate.

If the trigger condition (LE31 first proposes a v1 surface that wants ready-made FastAPI+HTMX discrete UI components, OR a future owner decision questions whether the FastAPI+HTMX+Python discrete-UI-component-pack substrate is healthy in 2026) is met, the external coding agent should:

1. Load this artifact and the parent daily-research report (`/opt/data/le31-daily-research-2026-10-13.md`).
2. Load the `htmui` repo: `https://github.com/volfpeter/htmui` — README + `docs/` if available.
3. Load the companion feature 143 (`volfpeter/fasthx`) — both are FastAPI+HTMX peers with the same author.
4. Re-run the LE31 feature gate with `htmui`'s README in hand.
5. **Decide whether the proposed v1 surface benefits from `htmui`'s discrete-UI-component-pack framing**. If the v1 surface has 10+ routes OR wants AI-codegen-target-friendly waiter UI components, `htmui` is purpose-built for that use case. If the v1 surface is ≤ 5 hand-written routes (as today), `htmui` adds no value.
6. **If `htmui` is proposed for adoption**: pin to a specific version, add to `requirements-htmui.txt` (do not pin to v1 yet), and refactor one existing route to use `htmui`'s discrete-UI-component-pack. Compare against the hand-written equivalent. If the refactor is meaningfully smaller, propose a v1-wide adoption; if not, document the comparison and defer.
7. **If `htmui` is not adopted**: document the comparison and defer. No charter §3.1 change is needed because `htmui` is a discrete-UI-component-pack, not a stack change.
8. **Pilot on one route first**. Do not adopt `htmui` project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/296-volfpeter-htmui-mit-python-ui-components-hypermedia-applications-fastapi-htmx-v1-hypermedia-ui-component-vocabulary.md`
- **Parent daily-research report**: `/opt/data/le31-daily-research-2026-10-13.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-13/gsearch_4.json` (where `volfpeter/htmui` is listed at `pushed_at=2026-10-12T16:56:17Z`, 13★, MIT, Python)
- **`htmui` repo**: `https://github.com/volfpeter/htmui` (parent-fetched 2026-10-13 metadata)
- **Companion artifacts**:
  - `features/142-feldroy-air-fastapi-htmx-ai-write-framework.md` (FastAPI+HTMX peer)
  - `features/143-volfpeter-fasthx-htmx-fastapi-declarative-ssr.md` (declarative-SSR-framework sister-package; same author)
  - `features/308-manwithacat-dazzle-mit-semantic-substrate-ai-collaborative-software-fastapi-htmx-pydantic-starlette-v1-hypermedia-fastapi-stack-shape-vocabulary.md` (4/4 LE31-stack-match carry-over from 10-12)
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.4 observable evidence, §3.4.4 the non-technical owner).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Verification protocol reference

- **Read-back protocol**: parent-re-parse the raw `/tmp/le31-daily-2026-10-13/gsearch_4.json` JSON to confirm `full_name=volfpeter/htmui` + `stargazers_count=13` + `forks_count=1` + `license.spdx_id=MIT` + `pushed_at=2026-10-12T16:56:17Z` + `created_at=2026-02-23T13:15:35Z` + `description="Python UI components for building hypermedia applications"` + `size=507` + `topics=[fastapi, html, htmx, hypermedia, python, server-side-rend, web, web-development]`.
- **GitHub canonical read**: GET `https://api.github.com/repos/volfpeter/htmui` (HTTP 200; parent-verified 2026-10-13).
- **Anti-fabrication canary**: `grep -lF 'volfpeter/htmui'` across `/opt/data/le31_mmm3_research/features/*.md` = 0 matches outside this feature file (parent-verified).
- **Distinct-from-features**: ripgrep-verified `volfpeter` against features 1–295 = only this feature 296 + carry-over feature 143.

## Rollback path

This defer artifact is fully reversible:
- **Delete the feature file**: `rm /opt/data/le31_mmm3_research/features/296-volfpeter-htmui-...md`.
- **Delete the HANDOFF**: `rm /opt/data/le31_mmm3_research/specs/296-volfpeter-htmui-...-HANDOFF.md`.
- **No code change was made today**, so no rollback of code is required.
- **No database migration was made today**, so no rollback of schema is required.
- **No pin change was made today** (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1).

## Frozen contract

The peer-awareness surfaced by this defer is:
- **Repo**: `volfpeter/htmui` — *"Python UI components for building hypermedia applications"*
- **Stars / forks / licence / language**: 13★ / 1⑂ / MIT / Python
- **Created / pushed**: 2026-02-23 (~8 months ago) / **2026-10-12T16:56:17Z (in-window by push only)**
- **Author**: `volfpeter` = same author as feature 143 `volfpeter/fasthx` (declarative-SSR-framework sister-package)
- **Topics (8)**: `fastapi, html, htmx, hypermedia, python, server-side-rend, web, web-development`
- **Stack match**: FastAPI ✅ / HTMX ✅ / Python 3.13 ✅ = **3/3 LE31-stack-match**
- **Bucket**: v1 hypermedia-UI-component-vocabulary
- **Verdict**: defer (parking-lot, watch-list, no build today)

LE31 v1 doesn't need this peer for code today. The defer artifact does **not** propose an `htmui` adoption. It surfaces the *peer* for future use.
