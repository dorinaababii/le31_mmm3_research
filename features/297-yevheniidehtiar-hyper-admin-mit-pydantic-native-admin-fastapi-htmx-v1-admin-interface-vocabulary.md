# Feature 297 — `yevheniidehtiar/hyper-admin` Pydantic-native admin for FastAPI + HTMX (defer)

> **NEW observation (2026-10-13).** Documents in-window GitHub repo `yevheniidehtiar/hyper-admin` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **5★/2⑂**, language Python, **4464 KB modest**, default_branch=`main`, **pushed 2026-10-11T20:23:58Z (in-window by `pushed_at` only; created 2025-08-22T19:51:14Z = ~14-month-old repo with in-window push)**). Topics = NONE listed (description-only metadata). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-13): *"A modern, Pydantic-native admin interface for FastAPI, powered by HTMX"*. The **FastAPI + HTMX + Pydantic-native = 3/3 LE31-stack-match** is the **strongest in-window 2026 LE31-stack-match of the 75-pass series for an admin-interface-pack** (vs `feldroy/air` = feature 142 which is FastAPI+HTMX+ai-write-framework not admin-specific; vs `glebdi-ai/hxadmin` which is FastAPI+SQLAlchemy+Jinja2+htmx+Jinja2-templates not Pydantic-native; vs `alina-geissler/recipe-drawer` off-domain). The **5★ / 2⑂** is the **2nd-highest in-window 2026 star count of any net-new Python permissive v1-admin-interface candidate** (= was 0★ on 10-12's 3 picks; the +1★ from 10-12 = first star movement for this repo). **First observation date 2026-10-13** = today. Bucket: **v1 admin-interface-vocabulary (defer, parking-lot)** = peer awareness + named v1 architectural vocabulary; **zero build time today**.

## Goal

Retain `yevheniidehtiar/hyper-admin` as a **structural-evidence peer** that LE31's chosen validation layer (Pydantic) + the FastAPI+HTMX substrate are being actively maintained by an admin-interface-author in 2026, with the **Pydantic-native + FastAPI + HTMX triple** directly relevant to any future v1 surface that wants a ready-made admin-interface inheriting Pydantic schemas. The artifact is the persistent peer-awareness record + the named architectural vocabulary for the **Pydantic-native + admin-interface + FastAPI + HTMX** quadruple. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the peer: stack match (3/3 = FastAPI + HTMX + Pydantic-native), star/fork counts, licence (MIT permissive), in-window activity, author identity (`yevheniidehtiar` = independent author with sustained 2026 engagement).
- A decision record: today's verdict is `defer` because LE31 v1 does not need to *use* `hyper-admin` (LE31 v1 owner screen is a small subset of the waiter UI today, not a standalone admin). The peer value is **structural evidence + vocabulary, not *adoption***.
- A reference for the next time LE31 proposes a v1 surface that wants a ready-made admin interface: `hyper-admin` is MIT-permissive (no licensing friction) and is Pydantic-native (LE31's SQLModel uses Pydantic under the hood = natural schema-inheritance).
- A reference for the "A modern, Pydantic-native admin interface for FastAPI, powered by HTMX" framing: any future v1 owner-screen surface can evaluate `hyper-admin` against the alternative (custom FastAPI + Jinja2 + HTMX admin-template).
- A cross-section reference with the **FastAPI+HTMX peer cluster** = features 142 + 143 + 308 + 296 (this one = feature 297) + `mcs0002/jobfeed` sister-shape but off-domain.

**Out of scope (defer artifact):**
- Any code change to LE31 today.
- Any pin bump (LE31 is on FastAPI 0.118.0+; SQLModel uses Pydantic for schemas; `hyper-admin` is a UI-component-pack, not a Pydantic replacement).
- Any documentation change to LE31's README or HANDOFF.md.
- Any charter §3.1 stack-change consideration (Pydantic is the validation layer behind SQLModel; `hyper-admin` does not change the stack — it adds a Pydantic-native admin interface on top of FastAPI + HTMX, which LE31 already uses).

## Description

GitHub `yevheniidehtiar/hyper-admin` — *"A modern, Pydantic-native admin interface for FastAPI, powered by HTMX"* — is a **Pydantic-native admin-interface** built on FastAPI + HTMX that provides a ready-made admin-interface for FastAPI apps that inherit Pydantic schemas. The repo is authored by `yevheniidehtiar` (independent maintainer with 2026 active engagement).

The repo's **5★ / 2⑂** is the **2nd-highest in-window star count of any net-new Python permissive v1-admin-interface candidate of the 75-pass series** (was 0★ on 10-12's 3 picks). Combined with the **MIT permissive licence**, the **exact 3/3 stack match** (FastAPI + HTMX + Pydantic-native are all charter §3.1 components via SQLModel's Pydantic underpinnings), and the **2026-10-11 push** (in-window by push only), this is **the strongest single Pydantic-native + FastAPI + HTMX admin-interface peer for LE31's chosen stack** in 2026.

**Stack match matrix**:

| `hyper-admin` component | LE31 charter §3.1 | Match? |
|---|---|---|
| FastAPI | FastAPI (required) | ✅ exact |
| HTMX | used in `index.html` mockups | ✅ exact |
| Pydantic-native | SQLModel uses Pydantic under the hood | ✅ exact (schema-inheritance via Pydantic) |
| admin-interface | matches a future owner-screen surface | ✅ semantic-match |

**Cross-section insight for LE31**: the **Pydantic-native + admin-interface + FastAPI+HTMX substrate** framing is **directly LE31-relevant** for any future v1 surface that wants a Pydantic-schema-inherited admin-interface for an owner-screen. Today LE31 v1's owner-screen is a subset of the waiter UI (e.g., feature 03 menu-management). The peer-validation of the *Pydantic-native + admin-interface* idea is the durable takeaway; whether LE31 ever adopts `hyper-admin` is a separate decision.

**Pydantic-native specifically**: LE31's `SQLModel` uses Pydantic v2 as the validation/schema layer. The "Pydantic-native" adjective means `hyper-admin` reads Pydantic schemas directly from FastAPI routes (no separate schema definition). This is the strongest Pydantic-native v1-admin-interface framing of the 75-pass series because every other in-window admin-candidate requires either a separate SQLAlchemy model import (e.g., `glebdi-ai/hxadmin`) or a hand-rolled CRUD template.

**Licence**: MIT permissive — **zero licensing friction** for any LE31 v1 surface that wants to *use* `hyper-admin` (adopt = `pip install`, not fork, so no copyleft concerns).

**In-window by push only — labelled as such**: the repo was **created 2025-08-22** (~14 months ago, off-window for an in-window-by-creation-signal). The 2026-10-11 push is a **fresh push on a ~14-month-old admin-interface**, not a new discovery.

**Distinct from features 1–295** (ripgrep-verified — no overlap on `yevheniidehtiar`, `hyper-admin`):

- Does **NOT** duplicate feature 142 (`feldroy/air` — FastAPI+HTMX+Pydantic wrapper framework, MIT 915★, different repo) or feature 296 (`volfpeter/htmui` — discrete-UI-component-pack, MIT 13★, same pass) or feature 297 (this = `hyper-admin`) or feature 308 (`manwithacat/dazzle` — AI-collaborative-software substrate, four-of-four LE31-stack-match).

## Data model

No schema change today. The defer artifact documents that `hyper-admin` would have:
- **API surface**: FastAPI-compatible admin routes (already supported by LE31 v1).
- **Pydantic-native**: reads Pydantic schemas from FastAPI routes (no schema duplication).
- **No Postgres integration** — `hyper-admin` reads from the FastAPI app's existing routes, not directly from Postgres; LE31's `StockEntry` + `audit_logs` are unchanged.
- **No aiogram integration** — `hyper-admin` is web-only; LE31's cook Telegram bot (charter §3.1) is unchanged.

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to evaluate `hyper-admin` for a future v1 surface:

1. Add `hyper-admin` to a side-branch `requirements-hyper-admin.txt` (do not pin to v1 yet).
2. Build a 1-route prototype: register a single FastAPI route with a Pydantic schema + let `hyper-admin` introspect.
3. Compare the prototype's code size + readability against LE31's current owner-screen implementation (which is part of the waiter UI today).
4. **If `hyper-admin` reduces the code size meaningfully**, propose a v1 surface that adopts `hyper-admin` for new owner-screens; **if not**, document the comparison and defer.
5. **Out of scope for v1 today**: any `hyper-admin` adoption. v1's UI is already working and stable.

## Telegram interaction if any

None. `hyper-admin` is a web-only admin-interface; no Telegram integration today. The cook Telegram bot (charter §3.1) is aiogram v3 and is not affected by `hyper-admin` adoption.

## Dependencies

- **GitHub**: `yevheniidehtiar/hyper-admin` 5★ / 2⑂ / MIT / Python / pushed 2026-10-11T20:23:58Z / created 2025-08-22T19:51:14Z.
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.2 (open-source dependency whitelist)**: would need an owner decision before any `hyper-admin` adoption.
- **Stack**: FastAPI 0.118.0+ (LE31 pin), HTMX (LE31's `index.html` template), Pydantic v2 (via SQLModel).
- **Licence**: MIT permissive — **zero licensing friction**.

## Open questions

1. **Does LE31 ever need a ready-made admin-interface?** Today: no — v1's owner-screen is a subset of the waiter UI (≤ 5 routes today). v2 surfaces: maybe — if the owner-screen scales to 10+ tables OR requires a separate owner-only auth-scope, a Pydantic-native admin-interface becomes load-bearing. Recommendation: revisit when the LE31 owner requests an owner-screen surface that scales past 10 tables.
2. **Is `hyper-admin` mature enough for production?** Today: 5★ / 2⑂ is encouraging but not conclusive (Python FastAPI+HTMX admin-interface peers with similar maturity include `musterhq/muster` at higher star count but off-domain). Recommendation: not a v1 question today.
3. **Would adopting `hyper-admin` violate charter §3.1's "no stack changes without explicit charter decision"?** No — `hyper-admin` is a *Pydantic-native admin-interface on top of FastAPI + Python*, not a *replacement* for FastAPI. Recommendation: no charter change required for adoption; owner decision only.

## Why this matters

LE31's chosen stack — **FastAPI + SQLModel + Postgres + aiogram v3** — is well-established. The Pydantic-via-SQLModel validation layer is the **load-bearing schema-lifecycle invariant** for any future v1 surface that wants CRUD operators auto-generated from Pydantic schemas. `yevheniidehtiar/hyper-admin` is **structural evidence** that:

1. **The Pydantic-native + FastAPI + HTMX + admin-interface substrate is being actively maintained by `yevheniidehtiar` in 2026.** This is the load-bearing substrate for any future LE31 v1 owner-screen surface that wants ready-made admin-interface; structural health is good.
2. **The "A modern, Pydantic-native admin interface for FastAPI, powered by HTMX" framing is emerging as a named architectural concern.** Any future v1 surface that wants Pydantic-schema-inherited admin-interface can evaluate `hyper-admin` against the alternative.
3. **MIT permissive + exact 3/3 stack match + Pydantic-native semantic-match** = the strongest single in-window 2026 v1 Pydantic-native admin-interface peer of the 75-pass series.

The defer is fully reversible: the file is a peer-awareness record, not a code dependency. If the LE31 owner decides to evaluate `hyper-admin` later, the file documents what to evaluate and how to evaluate it; if not, the file can be deleted with no operational impact.
