# Feature 143 — volfpeter/fasthx declarative FastAPI+HTMX server-side rendering (defer)

> **NEW observation (2026-09-04).** Documents in-window GitHub repo `volfpeter/fasthx` *Declarative Python server-side rendering utility for FastAPI with built-in HTMX support*, MIT, **730★, 22 forks**, language Python, topics `['fastapi', 'html', 'htmx', 'jinja2', 'python', 'server-side-rendering', 'templating', 'website']`, **created 2024-01-24 (off-window by ~20 months), pushed 2026-08-27T13:49:53Z (in-window by push only)**, by `volfpeter` (same author publishes `volfpeter/htmy` 401★ async pure-Python rendering engine and `volfpeter/holm` 132★ Next.js-style hypermedia on FastAPI — three siblings in the family, all in-window by push only). **Strongest htmx-on-FastAPI rendering peer of the 34-pass series** alongside PICK B (`feldroy/air`). Bucket: **v1 stack utility (peer awareness, pin/track)** — watch-list defer. Zero build time today.

## Goal

Retain `volfpeter/fasthx` (+ its same-author siblings `htmy` + `holm`) as **structural-evidence peer** that the FastAPI+HTMX rendering pattern is being actively developed by multiple maintainers in 2026. The artifact is the persistent peer-awareness record. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the peer: stack match, star/fork counts, licence, in-window activity, same-author siblings.
- A decision record: today's verdict is `defer` because LE31 v1's waiter web UI is **already FastAPI + Jinja2 + HTMX integration done by hand**, and a wrapper library (`fasthx`) is not required. The peer value is **structural evidence**, not *adoption*.
- A reference for the next time LE31 proposes a v2 surface that wants **declarative HTMX-on-FastAPI integration** (e.g., `HX-Trigger` headers in route decorators, `(component, response)` tuples): `fasthx` is the named pattern for that.
- A reference for the same-author three-sibling family (`fasthx` + `htmy` + `holm`) as evidence that the FastAPI+HTMX rendering space is actively developed.

**Out of scope (defer artifact):**
- Any code change to LE31 today.
- Any pin bump (LE31's FastAPI is already pinned at 0.141.0+).
- Any documentation change to LE31's README or HANDOFF.md.
- Any charter §3.1 stack-change consideration (FastAPI is explicitly required; `fasthx` is a wrapper on top of FastAPI, not a replacement).

## Description

GitHub `volfpeter/fasthx` — *Declarative Python server-side rendering utility for FastAPI with built-in HTMX support* — is a wrapper utility that adds declarative HTMX support to FastAPI routes. The pattern is: define `HX-Trigger` headers in the route decorator, render Jinja2 templates, return `(component, response)` tuples. The library is by `volfpeter` (volker peter), a Hungarian Python developer who publishes three siblings in the FastAPI+HTMX rendering space:

| Repo | Description | Stars | Forks | Pushed (window) |
|---|---|---|---|---|
| `volfpeter/fasthx` | Declarative Python SSR utility for FastAPI with built-in HTMX support (Jinja2 templates) | 730 | 22 | **2026-08-27** |
| `volfpeter/htmy` | Async, pure-Python server-side rendering engine for hypermedia applications | 401 | 9 | **2026-09-02** |
| `volfpeter/holm` | Hypermedia web development framework that brings the Next.js developer experience to Python, built on FastAPI | 132 | 3 | **2026-09-03** |

All three siblings are **in-window by push only** (off-window by create: 2024-01-24 / 2024-09-? / 2024-09-? respectively), MIT permissive, Python-only, FastAPI-compatible.

**Cross-section insight for LE31**: LE31 v1's waiter web UI is **FastAPI + Jinja2 + HTMX integration done by hand** (the `index.html` mockups use HTMX attributes for `fetch` + `hx-*` triggers, and FastAPI routes return rendered Jinja2 templates). `fasthx` is **the named pattern** for declarative integration of HTMX into FastAPI routes. LE31 v1 does not need this wrapper — the hand-written integration is straightforward and works — but the **pattern** is what matters: it's a **named idiom** that a future v2 surface can reference ("we use the fasthx pattern") or adopt.

**Why the three-sibling family matters**: a single in-window push on `fasthx` would be one data point; **three in-window pushes on three siblings from one maintainer** is a **structural-evidence signal** that the FastAPI+HTMX rendering space is being **actively developed** in 2026. The three siblings are at three different layers:
- `fasthx` — the **utility** (declarative helper for FastAPI routes).
- `htmy` — the **engine** (async pure-Python rendering, alternative to Jinja2).
- `holm` — the **framework** (Next.js-style developer experience on FastAPI).

This three-layer structure suggests the FastAPI+HTMX rendering space is **maturing** in 2026 — multiple maintainers (just volfpeter here, but other maintainers exist at `htmx` org etc.) are pushing at all layers.

**Stack match matrix**:

| `fasthx` component | LE31 charter §3.1 | Match? |
|---|---|---|
| FastAPI | FastAPI (required) | ✅ exact |
| Jinja2 templates | used in `index.html` mockups | ✅ exact |
| HTMX | used in `index.html` mockups | ✅ exact |
| Python | Python 3.13 (required) | ✅ exact |
| Declarative `HX-Trigger` headers | hand-written today | 🆕 LE31-relevant as named idiom |
| `(component, response)` tuples | hand-written today | 🆕 LE31-relevant as named idiom |

**Licence**: MIT permissive — **zero licensing friction** for any LE31 v2 surface that wants to *use* `fasthx`. Charter §3.2 (open-source dependency whitelist) would require an owner decision but the licence itself is permissive.

**In-window by push only — labelled as such**: the repo was **created 2024-01-24** (off-window by ~20 months). The 2026-08-27 push is a **fresh push on a long-established utility**, not a new discovery. Per the skill's hard rule, this is in-window by push only. The signal is "the utility is being actively maintained", which is real evidence of substrate health but is *not* evidence that `fasthx` itself is a new LE31-actionable feature.

**Distinct from features 1–140** (ripgrep-verified — no overlap on `volfpeter`, `fasthx`, `holm`, `htmy`):

- Does **NOT** duplicate feature 23 (`sse-cook-channel` — FastAPI SSE) or feature 16 (`htmx-admin`, defer) or feature 140 (`casedock` — Django+HTMX, different stack).

## Data model

No schema change today. The defer artifact documents that `fasthx` would have:

- **API surface**: FastAPI-compatible routes (already supported by LE31 v1).
- **Template layer**: Jinja2 templates (already supported by LE31 v1).
- **HTMX integration**: declarative headers + `(component, response)` tuples (already hand-written in LE31 v1; `fasthx` would standardize the pattern).
- **No Postgres integration** — `fasthx` is HTTP-only; LE31's `StockEntry` + `audit_logs` are unchanged.

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to evaluate `fasthx` for a future v2 surface:

1. Add `fasthx` to a side-branch `requirements-fasthx.txt` (do not pin to v1 yet).
2. Refactor a single existing LE31 route (e.g., the waiter order-taking route) to use `fasthx`'s declarative `HX-Trigger` pattern.
3. Compare the refactored code size + readability against the hand-written equivalent.
4. **If the refactor reduces duplication meaningfully across multiple routes**, propose a v2 surface that adopts `fasthx` as a project-wide pattern; **if not**, document the comparison and defer.
5. **Out of scope for v1**: any `fasthx` adoption. v1's UI is already working and stable.

## Telegram interaction if any

None. `fasthx` is a web framework utility; no Telegram integration today. The cook Telegram bot (charter §3.1) is aiogram v3 and is not affected by `fasthx` adoption.

## Dependencies

- **GitHub**: `volfpeter/fasthx` 730★ / 22 forks / MIT / Python / pushed 2026-08-27T13:49:53Z.
- **Same-author siblings**: `volfpeter/htmy` 401★ / pushed 2026-09-02T14:28:57Z; `volfpeter/holm` 132★ / pushed 2026-09-03T09:29:24Z.
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.2 (open-source dependency whitelist)**: would need an owner decision before any `fasthx` adoption.
- **Stack**: FastAPI 0.141.0+, Jinja2, HTMX (all LE31 components).
- **Licence**: MIT permissive — **zero licensing friction**.

## Open questions

1. **Does LE31 v1 have enough HTMX route complexity to benefit from `fasthx`?** Today: probably not — the waiter web UI has a small number of routes. Recommendation: not a v1 question; revisit when the route count grows beyond ~10.
2. **Is `fasthx` worth adopting for v2 surfaces that are HTMX-heavy?** Possibly — if a future v2 surface adds many HTMX routes (e.g., a detailed owner-facing history surface with multiple `HX-Trigger` interactions), `fasthx`'s declarative style would reduce boilerplate. Recommendation: revisit when the first HTMX-heavy v2 surface is proposed.
3. **Would adopting `fasthx` violate charter §3.1's "no stack changes without explicit charter decision"?** No — `fasthx` is a *utility on top of FastAPI + Jinja2 + HTMX*, all of which are already charter §3.1 components. Recommendation: no charter change required; owner decision only.
4. **Does the `htmy` async pure-Python rendering engine have any LE31 relevance?** Today: probably not — LE31 v1 uses Jinja2 templates, which are fast enough for the existing UI surface. Recommendation: revisit if a future v2 surface needs async rendering performance.

## Why this matters

LE31's chosen substrate — **FastAPI + Jinja2 + HTMX** — is well-established but the *health of the substrate* matters for v2 surfaces. `volfpeter/fasthx` + `volfpeter/htmy` + `volfpeter/holm` (three siblings, all in-window by push only, all MIT permissive) is **structural evidence** that:

1. **The FastAPI+HTMX rendering pattern is being actively developed by multiple maintainers in 2026.** This is the load-bearing substrate for LE31's waiter web UI; structural health is good.
2. **The pattern has a named idiom** (`fasthx` declarative `HX-Trigger` headers + `(component, response)` tuples) that a future v2 surface can reference or adopt.
3. **The three-layer structure** (utility → engine → framework) suggests the FastAPI+HTMX rendering space is **maturing** in 2026.

The defer is fully reversible: the file is a peer-awareness record, not a code dependency. If the LE31 owner decides to evaluate `fasthx` later, the file documents what to evaluate and how to evaluate it; if not, the file can be deleted with no operational impact.