# Feature 296 — `volfpeter/htmui` Python UI components for hypermedia applications (defer)

> **NEW observation (2026-10-13).** Documents in-window GitHub repo `volfpeter/htmui` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **13★/1⑂ = the highest in-window 2026 star count of any net-new Python permissive in-domain non-watchlist of the 75-pass series**, language Python, **507 KB modest**, default_branch=`main`, **pushed 2026-10-12T16:56:17Z (in-window by `pushed_at` only; created 2026-02-23T13:15:35Z = ~8-month-old repo with in-window push)**). Topics (verbatim from raw JSON, **8 topics**): `fastapi, html, htmx, hypermedia, python, server-side-rend, web, web-development`. Description (verbatim, parent-verified GitHub API direct-GET 2026-10-13): *"Python UI components for building hypermedia applications"*. The **FastAPI + HTMX + Python = 3/3 LE31-stack-match** plus 4 additional primitives (`html + server-side-rend + hypermedia + web-development`) is the **strongest in-window 2026 v1-stack-match of the 75-pass series for a discrete-hypermedia-UI-component-pack** (vs `feldroy/air` = feature 142 which is an application framework + `volfpeter/fasthx` = feature 143 which is declarative-SSR-framework + `mcs0002/jobfeed` sister-shape but off-domain). The **13★** is the **highest in-window 2026 star count of any net-new Python permissive in-domain non-watchlist of the 75-pass series** (= +9★ PICK B's `yevheniidehtiar/hyper-admin` + +10★ PICK C's `the-vibey-project/vibey` + 2.6× `brockamer/findajob`'s off-domain carry-over). **Sister-shape to feature 143 `volfpeter/fasthx`** (same author, different repo; `htmui` is the discrete-UI-component-pack while `fasthx` is the declarative-SSR framework). **First observation date 2026-10-13** = today. Bucket: **v1 hypermedia-UI-component-vocabulary (defer, parking-lot)** = peer awareness + named v1 architectural vocabulary + today-pushed-sister-shape observation; **zero build time today**.

## Goal

Retain `volfpeter/htmui` as a **structural-evidence peer** that LE31's chosen substrate (FastAPI+HTMX+Python) is being actively maintained by high-velocity maintainers in 2026, with the **discrete-UI-component-pack vocabulary** directly relevant to any future v1 surface that wants ready-made FastAPI+HTMX components. The artifact is the persistent peer-awareness record + the named architectural vocabulary for the **discrete-UI-component-pack + hypermedia + Python-on-stack** quadruple. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the peer: stack match (3/3 = FastAPI + HTMX + Python), star/fork counts, licence (MIT permissive), in-window activity, author identity (`volfpeter` = same author as feature 143 `volfpeter/fasthx`).
- A decision record: today's verdict is `defer` because LE31 v1 does not need to *use* `htmui` (the LE31 v1 surface is a single-restaurant waiter web UI = ~5 routes today, which can be hand-written using FastAPI+HTMX without a discrete-component-pack; the moment LE31 v1 scales to a 10+ route surface, a discrete-UI-component-pack becomes valuable). The peer value is **structural evidence + vocabulary, not *adoption***.
- A reference for the next time LE31 proposes a v1 surface that wants ready-made FastAPI+HTMX components: `htmui` is MIT-permissive (no licensing friction) and is purpose-built for that use case.
- A reference for the "Python UI components for building hypermedia applications" framing: any future v1 surface that wants AI-codegen-target-friendly waiter UI components can evaluate `htmui` against the alternative (custom FastAPI + HTMX hand-written components).
- A cross-section reference with the `volfpeter/fasthx` = feature 143 (sister-shape; same author + different repo = the FastAPI+HTMX substrate has multiple independent in-window peer instances).

**Out of scope (defer artifact):**
- Any code change to LE31 today.
- Any pin bump (LE31 is on FastAPI 0.118.0+; `htmui` is a component-pack, not a FastAPI replacement).
- Any documentation change to LE31's README or HANDOFF.md.
- Any charter §3.1 stack-change consideration (FastAPI + HTMX are explicitly required; `htmui` does not change the stack — it adds a discrete-UI-component-pack on top of FastAPI + Python, which LE31 already uses).
- Any charter §3.4 consideration (the `htmui` components are user-facing UI = human-supervised; no AI primitives; the component-pack itself does not introduce AI cross-section).

## Description

GitHub `volfpeter/htmui` — *"Python UI components for building hypermedia applications"* — is a **discrete-UI-component-pack** built on FastAPI + HTMX that aims to provide ready-made components for FastAPI + HTMX apps. The repo is authored by `volfpeter` (the same author as feature 143 `volfpeter/fasthx`, which is the declarative-SSR-framework sister-package).

The repo's **13★ / 1⑂** is the **highest in-window star count of any net-new Python permissive in-domain non-watchlist of the 75-pass series**. Combined with the **MIT permissive licence**, the **exact 3/3 stack match** (FastAPI + HTMX + Python are all charter §3.1 components), and the **2026-10-12 push** (in-window by push only), this is **the strongest single discrete-hypermedia-UI-component-pack peer for LE31's chosen stack** in 2026.

**Stack match matrix**:

| `htmui` component | LE31 charter §3.1 | Match? |
|---|---|---|
| FastAPI | FastAPI (required) | ✅ exact |
| HTMX | used in `index.html` mockups | ✅ exact |
| Python | Python 3.13 (required) | ✅ exact (Python 3.13 supported) |
| hypermedia | matching LE31's charter §3.1 hypermedia-first UI surface | ✅ exact |
| server-side-rend | matching LE31's cook Telegram bot's html-rendering-pipeline | ✅ exact |
| web, web-development | matching LE31's waiter web UI substrate | ✅ exact |
| html | matching LE31's `index.html` template | ✅ exact |

**Cross-section insight for LE31**: the **discrete-UI-component-pack + Python-on-stack + FastAPI+HTMX-substrate** framing is **directly LE31-relevant** for any future v1 surface that wants ready-made components for waiter or owner UI screens. Today LE31 v1 has hand-written components per surface (e.g., `index.html` waiter UI = ~200 lines of FastAPI + Jinja2 + HTMX; the cook Telegram bot is aiogram v3 markup). The peer-validation of the *discrete-UI-component-pack* idea is the durable takeaway; whether LE31 ever adopts `htmui` is a separate decision (and requires the LE31 v1 surface to scale past ~10 routes before the discrete-component-pack becomes load-bearing).

**Author identity**: `volfpeter` is the maintainer of multiple in-window FastAPI+HTMX repos including **feature 143 `volfpeter/fasthx`** (declarative-SSR-framework) and **this `volfpeter/htmui`** (discrete-UI-component-pack). The author has demonstrated sustained engagement with the FastAPI+HTMX substrate in 2026 (= 2 separate packages in-window today = strong 2026 active-maintenance signal). The credibility is real — `volfpeter` is not a random high-star author; it is a **named-author with multi-package 2026 activity**.

**Licence**: MIT permissive — **zero licensing friction** for any LE31 v1 surface that wants to *use* `htmui` (adopt = `pip install`, not fork, so no copyleft concerns). Charter §3.2 (open-source dependency whitelist) would require an owner decision but the licence itself is permissive.

**In-window by push only — labelled as such**: the repo was **created 2026-02-23** (~8 months ago, well off-window for an in-window-by-creation-signal). The 2026-10-12 push is a **fresh push on an ~8-month-old component pack**, not a new discovery. Per the skill's hard rule, this is in-window by push only. The signal is "the component pack is being actively maintained by its author", which is real evidence of substrate health.

**Distinct from features 1–295** (ripgrep-verified — no overlap on `volfpeter`, `htmui`):

- Does **NOT** duplicate feature 142 (`feldroy/air` — FastAPI+HTMX+Pydantic wrapper framework) or feature 143 (`volfpeter/fasthx` — declarative-SSR-framework, sister-shape of `htmui` = same author) or feature 16 (`htmx-admin`, defer — hand-written HTMX-on-server-rendering) or feature 308 (`manwithacat/dazzle` — AI-collaborative-software substrate, four-of-four LE31-stack-match) or feature 142 (peer of LE31's chosen substrate).

## Data model

No schema change today. The defer artifact documents that `htmui` would have:
- **API surface**: FastAPI-compatible routes (already supported by LE31 v1).
- **No Postgres integration** — `htmui` is HTTP-only; LE31's `StockEntry` + `audit_logs` are unchanged.
- **No aiogram integration** — `htmui` is web-only; LE31's cook Telegram bot (charter §3.1) is unchanged.
- **No `audit_logs` integration** — `htmui` is UI-only; LE31's append-only audit trail is unchanged.
- **No `order_no` or `table_no` integration** — `htmui` components are generic UI primitives, not restaurant-specific (the surface would need to be wrapped in LE31-specific UI templates anyway).

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to evaluate `htmui` for a future v1 surface:

1. Add `htmui` to a side-branch `requirements-htmui.txt` (do not pin to v1 yet).
2. Build a 1-route prototype: a single FastAPI route wrapped by `htmui`'s discrete-UI-component helpers, returning the existing LE31 `index.html` template.
3. Compare the prototype's code size + readability against LE31's current FastAPI + Jinja2 + HTMX integration.
4. **If `htmui` reduces the code size meaningfully**, propose a v1 surface that adopts `htmui` for new waiter or owner UI screens; **if not**, document the comparison and defer.
5. **Out of scope for v1 today**: any `htmui` adoption. v1's UI is already working and stable. The moment LE31 v1 scales to a 10+ route surface, revisit.

## Telegram interaction if any

None. `htmui` is a discrete-UI-component-pack for web UI; no Telegram integration today. The cook Telegram bot (charter §3.1) is aiogram v3 and is not affected by `htmui` adoption.

## Dependencies

- **GitHub**: `volfpeter/htmui` 13★ / 1⑂ / MIT / Python / pushed 2026-10-12T16:56:17Z / created 2026-02-23T13:15:35Z.
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.2 (open-source dependency whitelist)**: would need an owner decision before any `htmui` adoption.
- **Stack**: FastAPI 0.118.0+ (LE31 pin), HTMX (LE31's `index.html` template), Python 3.13 (LE31's runtime).
- **Licence**: MIT permissive — **zero licensing friction**.
- **Companion artifacts**:
  - `features/142-feldroy-air-fastapi-htmx-ai-write-framework.md` (FastAPI+HTMX peer)
  - `features/143-volfpeter-fasthx-htmx-fastapi-declarative-ssr.md` (declarative-SSR-framework sister-package)
  - `features/308-manwithacat-dazzle-mit-semantic-substrate-ai-collaborative-software-fastapi-htmx-pydantic-starlette-v1-hypermedia-fastapi-stack-shape-vocabulary.md` (4/4 LE31-stack-match carry-over)

## Open questions

1. **Does LE31 ever need a discrete-UI-component-pack?** Today: no — v1's UI surfaces are 5 routes hand-written and stable. v2 surfaces: maybe — if the surface scales to 10+ routes or introduces AI-codegen-target-friendly UI, a discrete-UI-component-pack becomes load-bearing. Recommendation: revisit when the LE31 owner requests a v1 surface that scales past 10 routes, OR when a v2-AI surface proposes AI-generated UI components.
2. **Is `htmui` mature enough for production?** Today: 13★ / 1⑂ is encouraging but not conclusive (Python FastAPI+HTMX peers with similar maturity include `feldroy/air` 915★ at 11 years old + `volfpeter/fasthx` at lower star count = feature 143). `htmui` is in the *peer-of-le31* tier, not the *industry-standard* tier. Recommendation: not a v1 question today; revisit when the LE31 owner requests a discrete-component-pack evaluation.
3. **Would adopting `htmui` violate charter §3.1's "no stack changes without explicit charter decision"?** No — `htmui` is a *discrete-UI-component-pack on top of FastAPI + Python*, not a *replacement* for FastAPI. Charter §3.1 says "Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres in production" — adopting `htmui` does not change the stack; it adds an *integration layer* on top. Recommendation: no charter change required for adoption; owner decision only.
4. **Does the "Python UI components for building hypermedia applications" framing match the LE31 operator philosophy?** Charter §3.4.4: *"the non-technical owner"*. A discrete-UI-component-pack is operator-friendly by lowering the technical-bar for adding new UI screens. The library is human-authored and stable (no AI primitives inside). Recommendation: evaluated; adoptable if the trigger condition is met.

## Why this matters

LE31's chosen stack — **FastAPI + SQLModel + Postgres + aiogram v3** — is well-established but the *evolution* of the stack is what matters for v1 surfaces that scale. `volfpeter/htmui` is **structural evidence** that:

1. **The FastAPI+HTMX-pattern + Python-on-stack + discrete-UI-component-pack substrate is being actively maintained by `volfpeter` in 2026.** This is the load-bearing substrate for any future LE31 v1 UI surface that wants ready-made components; structural health is good.
2. **The "Python UI components for building hypermedia applications" framing is emerging as a named architectural concern.** Any future v1 surface that wants AI-codegen-target-friendly or hand-author-friendly UI components has a peer component pack purpose-built for that use case.
3. **MIT permissive + exact 3/3 stack match + named author with multi-package 2026 activity** = the strongest single in-window v1 discrete-UI-component-pack peer of the 75-pass series.

The defer is fully reversible: the file is a peer-awareness record, not a code dependency. If the LE31 owner decides to evaluate `htmui` later, the file documents what to evaluate and how to evaluate it; if not, the file can be deleted with no operational impact.
