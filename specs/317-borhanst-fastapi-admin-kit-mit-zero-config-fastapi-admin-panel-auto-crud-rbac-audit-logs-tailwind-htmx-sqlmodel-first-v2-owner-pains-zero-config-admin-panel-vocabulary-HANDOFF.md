# HANDOFF — 317-borhanst-fastapi-admin-kit-mit-zero-config-fastapi-admin-panel-auto-crud-rbac-audit-logs-tailwind-htmx-sqlmodel-first

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-10-20
**Active feature path**: `/opt/data/le31_mmm3_research/features/317-borhanst-fastapi-admin-kit-mit-zero-config-fastapi-admin-panel-auto-crud-rbac-audit-logs-tailwind-htmx-sqlmodel-first-v2-owner-pains-zero-config-admin-panel-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v2 owner-pains roadmap is unspecified; the peer value is *zero-config-FastAPI-admin-panel-with-auto-CRUD-+-RBAC-+-audit-logs-+-Tailwind/HTMX-+-SQLModel-first vocabulary for a future v2 owner-pains PR that adds a zero-config-admin-panel surface*, not *adoption*.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the `borhanst/fastapi-admin-kit` GitHub repo (MIT, **★10 / 0⑂ = the highest topic-overlap v2 owner-pains pick of the 81-pass research series on `fastapi + python + sqlalchemy + sqlmodel + admin-panel + dashboard + fastapi-admin + fastapi-dashboard = 8/8 topics LE31-relevant = 100% topic-overlap score`**, language Python ✓ ON-STACK, **pushed 2026-10-16T11:34:49Z AND created 2026-07-02T13:10:24Z = IN-WINDOW BY BOTH FIELDS**, by `borhanst`) as a dated, in-window **structural-evidence peer** for LE31's v2 owner-pains zero-config-FastAPI-admin-panel-with-auto-CRUD-+-RBAC-+-audit-logs-+-Tailwind/HTMX-+-SQLModel-first substrate.

If the trigger condition (LE31 first proposes a v2 owner-pains surface that wants *zero-config-FastAPI-admin-panel-with-auto-CRUD-+-RBAC-+-audit-logs-+-Tailwind/HTMX-+-SQLModel-first* primitives, OR a future v2 owner-pains owner decision questions whether the zero-config-admin-panel-+-RBAC-+-audit-logs-+-Tailwind/HTMX-+-SQLModel-first approach is healthy in 2026) is met, the external coding agent should:

1. Load this artifact and the parent daily-research report (`/opt/data/le31-daily-research-2026-10-20.md`).
2. Load the `fastapi-admin-kit` repo: `https://github.com/borhanst/fastapi-admin-kit` — README + the auto-CRUD generator + the RBAC guard + the audit-log decorator if available.
3. Load the companion features 19 (`LE31-original-v1-waiter-UI-watch`) + 297 (`yevheniidehtiar/hyper-admin` Pydantic-native FastAPI admin + HTMX) + 325 (`AlexisLD-DEV/qramen` QR-code-table-ordering-PWA) + 329 (`nimaxin/adminsite` SQLAlchemy 2.0 admin for FastAPI/Starlette/Litestar) + 331 (`caravanacloud/conference-website` FastAPI + Tailwind v2) + 343 (`warpusTOM/StockWise_Group6_BT-204` offline-first-inventory-+-POS-vocabulary) — these are the persistent *v2 owner-pains admin + FastAPI + HTMX + SQLAlchemy + SQLModel* sister-cluster.
4. Re-run the LE31 feature gate with `fastapi-admin-kit`'s README in hand.
5. **Decide whether the proposed v2 owner-pains surface benefits from `fastapi-admin-kit`'s zero-config-+-auto-CRUD-+-RBAC-+-audit-logs-+-Tailwind/HTMX-+-SQLModel-first framing**. If the v2 owner-pains surface wants *zero-config-admin-panel-+-RBAC-+-audit-logs-+-Tailwind/HTMX-+-SQLModel-first*, `fastapi-admin-kit` is purpose-built for that use case. If the v2 owner-pains surface only wants a single-table-explicit-CRUD, `fastapi-admin-kit` adds the *zero-config + auto-CRUD + RBAC + audit-logs* primitives which may be over-engineering.
6. **If `fastapi-admin-kit` is proposed for adoption**: verify the underlying auto-CRUD generator respects the LE31 v1 SQLModel schema (LE31 uses SQLModel on Postgres; `fastapi-admin-kit` supports SQLModel/SQLAlchemy per the topics), add to a side-branch `requirements-fastapi-admin-kit.txt` (do not pin to main yet), and build a single-table prototype: register one existing SQLModel table (e.g., `MenuItem`) with the admin panel; verify that the auto-CRUD generates 4 routes (list + detail + edit + create) with RBAC gates + audit-log records on every action. Compare against the LE31 v1 *manual-handling-of-every-data-management-action* discipline. If the zero-config-+-auto-CRUD-+-RBAC-+-audit-logs discipline is meaningfully stronger, propose a v2 owner-pains surface adoption; if not, document the comparison and defer.
7. **If `fastapi-admin-kit` is not adopted**: document the comparison and defer. No charter §3.1 change is needed because the *zero-config + auto-CRUD + RBAC + audit-logs + Tailwind/HTMX + SQLModel-first* posture is a v2 owner-pains surface, not a stack change.
8. **Pilot on one table first**. Do not adopt `fastapi-admin-kit` project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/317-borhanst-fastapi-admin-kit-mit-zero-config-fastapi-admin-panel-auto-crud-rbac-audit-logs-tailwind-htmx-sqlmodel-first-v2-owner-pains-zero-config-admin-panel-vocabulary.md`
- **Parent daily-research report**: `/opt/data/le31-daily-research-2026-10-20.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-20/github_search/g4.json` (parent-verified raw JSON has `full_name=borhanst/fastapi-admin-kit` + `stargazers_count=10` + `forks_count=0` + `license.spdx_id=MIT` + `pushed_at=2026-10-16T11:34:49Z` + `created_at=2026-07-02T13:10:24Z` + `description="Zero-config FastAPI admin panel — auto-discovered CRUD, RBAC, audit logs, and a modern Tailwind/HTMX UI."` + `size=2674` + `topics=[admin-panel, dashboard, fastapi, fastapi-admin, fastapi-dashboard, python, sqlalchemy, sqlmodel]` = **8/8 topics LE31-relevant = 100% topic-overlap score**)
- **`fastapi-admin-kit` repo**: `https://github.com/borhanst/fastapi-admin-kit` (parent-fetched 2026-10-20 metadata)
- **Companion artifacts**:
  - `features/19-le31-original-v1-waiter-UI-watch.md` (LE31 v1 waiter UI surface)
  - `features/297-yevheniidehtiar-hyper-admin-Pydantic-native FastAPI admin.md` (Pydantic-native FastAPI admin)
  - `features/325-AlexisLD-DEV-qramen-QR-code-table-ordering-PWA.md` (QR-code-table-ordering-PWA)
  - `features/329-nimaxin-adminsite-SQLAlchemy-2.0-admin.md` (SQLAlchemy 2.0 admin for FastAPI/Starlette/Litestar)
  - `features/331-caravanacloud-conference-website-FastAPI-Tailwind.md` (FastAPI + Tailwind v2 application)
  - `features/343-warpusTOM-StockWise_Group6_BT-204-offline-first-inventory-+-POS-vocabulary.md` (offline-first-inventory-+-POS-vocabulary)
- **Charter §3.1 (Python 3.13 + FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.3 (append-only ledger)**: `fastapi-admin-kit`'s *audit-logs* IS canonical §3.3 *append-only-evidence-as-audit-trail* invariant applied to the *operator-action + role-action* dimension.
- **Charter §3.4 (chokepoint + human-gate + boundary-guard + router + non-AI-fallback + observable-evidence)**: `fastapi-admin-kit`'s *RBAC + audit-logs* IS canonical §3.4 *chokepoint-governed + human-gate + observable-evidence* charter invariant applied to the *operator-action + role-action* dimension.

## Mandatory LE31 skill list

The external coding agent must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.3 append-only ledger, §3.4 chokepoint + human-gate + non-AI-fallback, §3.7 privacy-first).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build; note: this is a v2 owner-pains pick, not a v1 pick, so the v1 pattern is informative but not directly applicable).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner (and note: `le31 v2 owner-pains` project does NOT exist per `le31-feature-pipeline/SKILL.md` line 33; sub-issue would be attached to `le31 Research` P-HMM-1 as parent).

## Verification protocol reference

- **Read-back protocol**: parent-re-parse the raw `/tmp/le31-daily-2026-10-20/github_search/g4.json` JSON to confirm `full_name=borhanst/fastapi-admin-kit` + `stargazers_count=10` + `forks_count=0` + `license.spdx_id=MIT` + `pushed_at=2026-10-16T11:34:49Z` + `created_at=2026-07-02T13:10:24Z` + `description` = `"Zero-config FastAPI admin panel — auto-discovered CRUD, RBAC, audit logs, and a modern Tailwind/HTMX UI."` + `size=2674` + `topics=[admin-panel, dashboard, fastapi, fastapi-admin, fastapi-dashboard, python, sqlalchemy, sqlmodel]` = **8/8 topics LE31-relevant = 100% topic-overlap score**.
- **GitHub canonical read**: GET `https://api.github.com/repos/borhanst/fastapi-admin-kit` (HTTP 200; parent-verified 2026-10-20).
- **Anti-fabrication canary**: `grep -lF 'borhanst/fastapi-admin-kit'` across `/opt/data/le31_mmm3_research/features/*.md` = 0 matches outside this feature file (parent-verified).
- **Distinct-from-features**: ripgrep-verified `borhanst`, `fastapi-admin-kit` against features 1–316 = only this feature 317.

## Rollback path

This defer artifact is fully reversible:
- **Delete the feature file**: `rm /opt/data/le31_mmm3_research/features/317-borhanst-fastapi-admin-kit-...md`.
- **Delete the HANDOFF**: `rm /opt/data/le31_mmm3_research/specs/317-borhanst-fastapi-admin-kit-...-HANDOFF.md`.
- **No code change was made today**, so no rollback of code is required.
- **No database migration was made today**, so no rollback of schema is required.
- **No pin change was made today** (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1).
