# Feature 186 — `Sholu021-KitchenIQ-mit-fastapi-postgresql-restaurant-erp-fefo-ai-copilot` (defer)

> **NEW observation on 2026-09-17.** Documents in-window GitHub repo `Sholu021/KitchenIQ` (**MIT ✓**, **0★/0⑂**, Python, **pushed 2026-09-16T15:30:26Z**, in-window by push only, **859 KB** substantial repo). Description (verbatim from GitHub API): *"AI-powered ERP & Inventory Management System for Restaurants, Cafés, Bakeries & Cloud Kitchens."* Topics: `[erp, fastapi, food-tech, inventory-management, nextjs, openai, postgresql, python, react, restaurant, sqlalchemy]` — the **strongest direct LE31-stack-shape match** of any 2026-09-17 in-window repo: `fastapi + postgresql + sqlalchemy + python` = **4 of 4 LE31 backend stack primitives** matched. **CAVEATS**: (1) `nextjs` + `react` topics = frontend stack mismatch with LE31's HTMX approach; (2) `openai` topic + `AI-powered` marketing language + customer-facing restaurant-ERP context = **charter §3.4 ripgrep REQUIRED** before any adoption. Bucket: **v2 architecture-reference (defer, parking-lot)**. Zero build time today.

## Goal

Document `KitchenIQ` as a v2 architecture-reference observation: a real in-domain FastAPI+SQLAlchemy+Postgres restaurant ERP peer in 2026 — but NOT a build candidate today because of the frontend stack mismatch (NextJS+React vs LE31 HTMX) + the §3.4 AI surface that needs ripgrep verification. The artifact is a persistent cross-section reference for the FastAPI+SQLAlchemy+PostgreSQL restaurant-ERP stack-shape match, with two unresolved next-step questions for the coding agent.

## Scope

**In scope (defer artifact):**

- A written record of the **direct LE31-stack-shape match** (FastAPI + SQLAlchemy + PostgreSQL + Python = 4 of 4 LE31 backend stack primitives matched) — the strongest such match of any 2026-09-17 in-window repo.
- A written record of the **two caveats** (frontend stack mismatch + §3.4 ripgrep) that gate any future v2 reference usage.
- A decision record: today's verdict is `defer` because both caveats need resolution before any v2 reference usage.
- A cross-section reference with the in-domain fastapi+restaurant peer cluster: features 89, 106, 158.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot.
- Any change to LE31 v1's `audit_logs` or `StockEntry` schema.
- Adoption of the `KitchenIQ` codebase (caveats unresolved).
- Any v1 build implication.

## Evidence / JTBD

When a future LE31 v2 surface looks for an in-domain FastAPI+SQLAlchemy+Postgres restaurant ERP peer for architectural reference (without code adoption), the owner wants *evidence that such a peer exists in 2026*, but struggles because *most in-window FastAPI+restaurant repos are off-domain or AGPL-blocked or stack-mismatched (frontend is NextJS+React not HTMX)*, so the v2 surface can establish a credible architectural reference.

- **Evidence class**: observed (the `KitchenIQ` description + topics directly name FastAPI + PostgreSQL + SQLAlchemy + Python + restaurant).
- **Confidence**: high for the stack-shape match (the GitHub API topic set is direct).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 doesn't need a v2 architectural reference yet; the v2 surface that would *use* the reference doesn't exist.
- **The value is naming, not direct demand**: when the first v2 surface looks for an in-domain FastAPI+Postgres restaurant-ERP reference, `KitchenIQ` is a documented peer.

## Description

GitHub `Sholu021/KitchenIQ` (MIT, 0★/0⑂, Python, pushed 2026-09-16T15:30:26Z, created date TBD, 859 KB).

Description (verbatim): *"AI-powered ERP & Inventory Management System for Restaurants, Cafés, Bakeries & Cloud Kitchens."*

Topics (verbatim from GitHub API): `erp`, `fastapi`, `food-tech`, `inventory-management`, `nextjs`, `openai`, `postgresql`, `python`, `react`, `restaurant`, `sqlalchemy` — 11 topics; **the FastAPI+PostgreSQL+SQLAlchemy+Python stack-shape match is the strongest in 2026-09-17's in-window set**.

The two caveats:

1. **Frontend stack mismatch**: `nextjs` + `react` topics indicate the frontend is built with NextJS+React (LE31's chosen frontend approach is HTMX). Without reading the `app/` directory structure, we cannot tell whether the FastAPI backend is decoupled from the NextJS+React frontend (architectural reference possible) or tightly coupled (architectural reference not useful for LE31 because LE31 has its own HTMX frontend).
2. **§3.4 AI surface**: `openai` topic + `AI-powered` description + customer-facing restaurant-ERP context = charter §3.4 ripgrep REQUIRED. If the AI integration is internal/admin-only (e.g., a smart-inventory-recommendation dashboard for the owner), §3.4 permits (staff-tooling territory). If the AI integration is customer-facing (e.g., a customer-facing chatbot that takes orders), §3.4 forbids.

**The 1:1 mapping onto LE31 stack (today):**

| KitchenIQ topic | LE31 stack | Match status |
|---|---|---|
| `fastapi` | FastAPI (LE31 backend framework) | ✓ **EXACT** |
| `postgresql` | Postgres in production (charter §3.1) | ✓ **EXACT** |
| `sqlalchemy` | SQLModel (which uses SQLAlchemy core) | ✓ **EXACT** (via SQLModel → SQLAlchemy core) |
| `python` | Python 3.13 (charter §3.1) | ✓ **EXACT** |
| `erp` | (no direct LE31 counterpart — LE31 is a v1 single-restaurant ops system, not an ERP) | ⚠ **scope mismatch** (LE31 is a thin ops system, not a full ERP) |
| `restaurant` | (charter §3.1 = single small restaurant) | ✓ **EXACT** |
| `inventory-management` | `StockEntry` (charter §3.1) | ✓ **EXACT** |
| `nextjs` | (LE31 frontend is HTMX) | ❌ **STACK MISMATCH** |
| `react` | (LE31 frontend is HTMX) | ❌ **STACK MISMATCH** |
| `openai` | (charter §3.4 forbids customer-facing AI; allows staff-tooling AI) | ⚠ **§3.4 NEEDS RIPGREP** |
| `food-tech` | (charter §3.1 is small-restaurant-focused; food-tech is broader) | ⚠ **scope adjacency** (LE31 is narrow; food-tech is broad) |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 surface that needs an in-domain FastAPI+Postgres restaurant-ERP architectural reference), the coding agent's next-step work is:

1. **Read `app/` directory** to determine whether the FastAPI backend is decoupled from the NextJS+React frontend.
2. **Read the AI-touching code paths** to determine whether the `openai` integration is staff-tooling (charter §3.4 permits) or customer-facing (charter §3.4 forbids).

The answer to these two questions is the gate to any future v2 reference usage of `KitchenIQ`.

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v2 implementation would include (pending the two next-step questions being answered):

1. If the FastAPI backend is decoupled AND the AI integration is staff-tooling, the v2 surface can use `KitchenIQ` as an architectural reference (NOT for code adoption — only for vocabulary).
2. If either the FastAPI backend is tightly coupled OR the AI integration is customer-facing, the v2 surface should NOT use `KitchenIQ` as a reference (the reference fails the charter gate).

**No existing code change today.**

## Telegram interaction

**None today.** The defer artifact is documentation only.

Future v2: the cook Telegram bot would not change; the v2 surface that would *use* the `KitchenIQ` reference is hypothetical and not LE31-specific.

## Dependencies

1. Read access to the `KitchenIQ` GitHub repository (`Sholu021/KitchenIQ`).
2. File-inspection of the `app/` directory structure to determine backend/frontend coupling.
3. Ripgrep for `openai`, `customer-facing`, `chatbot` strings to verify §3.4 posture.

## Open questions

1. **Is the FastAPI backend decoupled from the NextJS+React frontend?** Inspect `app/` directory to determine. **Required for any future v2 reference usage.**
2. **Is the `openai` integration staff-tooling (charter §3.4 permits) or customer-facing (charter §3.4 forbids)?** Ripgrep the AI-touching code paths to determine. **Required for any future v2 reference usage.**
3. **Is `KitchenIQ` a v1 single-restaurant system (like LE31) or a multi-tenant SaaS?** The description says "AI-powered ERP" which suggests ERP-style (multi-module, multi-tenant). LE31 v1 is a thin ops system for a single small restaurant. The scope mismatch is acknowledged in the 2-step gate above but warrants a deeper scope-comparison.

## Why this matters

`KitchenIQ` is the **strongest direct LE31-stack-shape match** of any 2026-09-17 in-window repo (FastAPI + PostgreSQL + SQLAlchemy + Python = 4 of 4 LE31 backend stack primitives matched). The architectural reference is real, even if the caveats gate any adoption today. Documenting the match + the caveats gives future LE31 v2 surfaces a documented in-domain FastAPI+Postgres restaurant-ERP peer for vocabulary reference (NOT code adoption) — exactly the kind of cross-section signal that the LE31 v2 cluster has been collecting since 2026-08-28 (features 121/122/129/133/134/135/141/148/167/168/169/181/182).