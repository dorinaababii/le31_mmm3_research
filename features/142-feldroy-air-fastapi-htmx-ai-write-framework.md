# Feature 142 — feldroy/air FastAPI+HTMX framework "designed for AI to write" (defer)

> **NEW observation (2026-09-04).** Documents in-window GitHub repo `feldroy/air` *The first web framework designed for AI to write — Built on Python, FastAPI, Pydantic, and HTMX*, MIT, **915★, 97 forks**, language Python, topics `['ai', 'fastapi', 'pydantic', 'python', 'starlette', 'web']`, **created 2015-12-11 (off-window by ~11 years), pushed 2026-09-03T22:49:43Z (in-window by push only)**, by Audrey Feldroy + Daniel Feldroy (Two Scoops of Django authors). **Strongest single in-window stack-peer of the 34-pass series**: exact FastAPI+HTMX+Pydantic stack match + pushed today + MIT permissive + named author with industry credibility. Bucket: **v1 stack utility (peer awareness, pin/track)** — watch-list defer. Zero build time today.

## Goal

Retain `feldroy/air` as a **structural-evidence peer** that LE31's chosen substrate (FastAPI+HTMX+Python) is being actively maintained by high-star maintainers in 2026, with the "designed for AI to write" framing directly relevant to any future v2-AI surface. The artifact is the persistent peer-awareness record. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the peer: stack match, star/fork counts, licence, in-window activity, author credibility.
- A decision record: today's verdict is `defer` because LE31 v1 does not need to *use* `air` (FastAPI + Jinja2 + HTMX integration is straightforward without a wrapper framework). The peer value is **structural evidence**, not *adoption*.
- A reference for the next time LE31 proposes a v2 surface that wants AI-codegen-target-friendly waiter/cook/owner UI screens: `air` is MIT-permissive (no licensing friction) and is purpose-built for that use case.
- A reference for the "designed for AI to write" framing: any future v2-AI surface that wants AI-generated UI should evaluate `air` against the alternative (custom FastAPI + HTMX integration).

**Out of scope (defer artifact):**
- Any code change to LE31 today.
- Any pin bump (LE31 is on FastAPI 0.141.0+; `air` is a wrapper, not a FastAPI replacement).
- Any documentation change to LE31's README or HANDOFF.md.
- Any charter §3.1 stack-change consideration (FastAPI is explicitly required; `air` does not change the stack — it adds a wrapper layer on top of FastAPI + Starlette + Pydantic, which LE31 already uses).

## Description

GitHub `feldroy/air` — *The first web framework designed for AI to write — Built on Python, FastAPI, Pydantic, and HTMX* — is a **wrapper framework** around FastAPI + Starlette + Pydantic + HTMX that aims to make AI codegen produce well-formed FastAPI code. The repo is authored by Audrey Feldroy + Daniel Feldroy (Two Scoops of Django), the most-cited Django tutorial authors in the Python web ecosystem.

The repo's **915★ / 97 forks** are the **highest in-window star count for any Python FastAPI+HTMX peer** of the 34-pass series. Combined with the **MIT permissive licence**, the **exact stack match** (FastAPI + Pydantic + Starlette + HTMX are all charter §3.1 components), and the **2026-09-03 push** (in-window by push only), this is **the strongest single structural-evidence peer for LE31's chosen stack**.

**Stack match matrix**:

| `air` component | LE31 charter §3.1 | Match? |
|---|---|---|
| FastAPI | FastAPI (required) | ✅ exact |
| Pydantic | via SQLModel | ✅ exact (SQLModel uses Pydantic under the hood) |
| Starlette | via FastAPI | ✅ exact (FastAPI uses Starlette under the hood) |
| HTMX | used in `index.html` mockups | ✅ exact |
| Python | Python 3.13 (required) | ✅ exact (Python 3.13 supported) |
| "designed for AI to write" | n/a | 🆕 LE31-relevant for future v2-AI surfaces |

**Cross-section insight for LE31**: the "designed for AI to write" framing is **directly LE31-relevant** for any future v2 surface that wants AI-generated waiter/cook/owner UI screens. Today LE31 v1 has no AI-generated UI; v1's UI is hand-written FastAPI + Jinja2 + HTMX. If a future v2 surface proposes AI-generated UI (e.g., a natural-language summary that becomes a Telegram send or a waiter recommendation card), `air` is purpose-built to make that codegen *target well*. The peer-validation of the *idea* (AI can write FastAPI code if the framework is shaped for it) is the durable takeaway; whether LE31 ever adopts `air` is a separate decision.

**Author credibility**: Audrey Feldroy + Daniel Feldroy are the authors of *Two Scoops of Django* (the most-cited Django best-practices book, multiple revisions over ~15 years), founders of Feldroy (a publishing imprint), and active in the Python web community. The credibility is real — `air` is not a random 915-star repo; it is a **named-author repo with industry credibility**.

**Licence**: MIT permissive — **zero licensing friction** for any LE31 v2 surface that wants to *use* `air` (adopt = wrap, not fork, so no copyleft concerns). Charter §3.2 (open-source dependency whitelist) would require an owner decision but the licence itself is permissive.

**In-window by push only — labelled as such**: the repo was **created 2015-12-11** (off-window by ~11 years). The 2026-09-03 push is a **fresh push on a long-established framework**, not a new discovery. Per the skill's hard rule, this is in-window by push only. The signal is "the framework is being actively maintained by its authors", which is real evidence of substrate health but is *not* evidence that `air` itself is a new LE31-actionable feature.

**Distinct from features 1–140** (ripgrep-verified — no overlap on `feldroy`, `audreyfeldroy`, `air.fastapi`, `Two Scoops of Django`):

- Does **NOT** duplicate feature 23 (`sse-cook-channel` — FastAPI SSE) or feature 16 (`htmx-admin`, defer) or feature 106 (`rafood-api-fastapi-sqlmodel-context-arch` — different peer, `RafaelEmery/rafood-api` 3★ off-window) or feature 132 (`sqlmodel-0-0-42-pin-track` — pin-bump, framework-agnostic) or feature 140 (`casedock` — Django+HTMX, different stack).

## Data model

No schema change today. The defer artifact documents that `air` would have:

- **API surface**: FastAPI-compatible routes (already supported by LE31 v1).
- **No Postgres integration** — `air` is HTTP-only; LE31's `StockEntry` + `audit_logs` are unchanged.
- **No aiogram integration** — `air` is web-only; LE31's cook Telegram bot (charter §3.1) is unchanged.

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to evaluate `air` for a future v2 surface:

1. Add `air` to a side-branch `requirements-air.txt` (do not pin to v1 yet).
2. Build a 1-route prototype: a single FastAPI route wrapped by `air`'s HTMX helpers, returning the existing LE31 `index.html` template.
3. Compare the prototype's code size + readability against LE31's current FastAPI + Jinja2 + HTMX integration.
4. **If `air` reduces the code size meaningfully**, propose a v2 surface that adopts `air` for new waiter/cook/owner UI screens; **if not**, document the comparison and defer.
5. **Out of scope for v1**: any `air` adoption. v1's UI is already working and stable.

## Telegram interaction if any

None. `air` is a web framework; no Telegram integration today. The cook Telegram bot (charter §3.1) is aiogram v3 and is not affected by `air` adoption.

## Dependencies

- **GitHub**: `feldroy/air` 915★ / 97 forks / MIT / Python / pushed 2026-09-03T22:49:43Z.
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.2 (open-source dependency whitelist)**: would need an owner decision before any `air` adoption.
- **Stack**: FastAPI 0.141.0+, Pydantic, Starlette, HTMX (all LE31 components).
- **Licence**: MIT permissive — **zero licensing friction**.

## Open questions

1. **Does LE31 ever want AI-generated UI?** Today: no — v1 UI is hand-written and stable. v2-AI surface: maybe — if a natural-language summary becomes a Telegram send or a waiter recommendation card, the *recipient of the UI* might be AI-shaped, but the *producer* of the UI is still human. Recommendation: revisit when the first v2-AI surface is proposed.
2. **Is `air` mature enough for production?** Today: 915★ / 97 forks is encouraging but not conclusive (Python FastAPI peers with similar maturity include `fastapi-users` 7k★, `sqlmodel` 16k★, `tiangolo/full-stack-fastapi-template` 35k★). `air` is in the *peer-of-le31* tier, not the *industry-standard* tier. Recommendation: not a v1 question; revisit when the LE31 owner requests a v2 surface that needs a FastAPI wrapper.
3. **Would adopting `air` violate charter §3.1's "no stack changes without explicit charter decision"?** No — `air` is a *wrapper around FastAPI*, not a *replacement* for FastAPI. Charter §3.1 says "Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres in production" — adopting `air` does not change the stack; it adds an *integration layer* on top. Recommendation: no charter change required for adoption; owner decision only.
4. **Does the "designed for AI to write" framing match the LE31 operator philosophy?** Charter §3.4.4: *"the non-technical owner"*. AI-written UI would be *operator-friendly by* (AI generates a screen that the non-technical owner sees) but *operator-acceptance unknown* (will the owner accept AI-generated screens, or want human-authored ones?). Recommendation: not evaluated; revisit when the first AI-generated UI is proposed.

## Why this matters

LE31's chosen stack — **FastAPI + SQLModel + Postgres + aiogram v3** — is well-established but the *evolution* of the stack is what matters for v2 surfaces. `feldroy/air` is **structural evidence** that:

1. **The FastAPI+HTMX pattern is being actively maintained by high-star maintainers in 2026.** This is the load-bearing substrate for LE31's waiter web UI; structural health is good.
2. **The "designed for AI to write" framing is emerging as a named architectural concern.** Any future v2-AI surface that wants AI-codegen-target-friendly UI has a peer framework purpose-built for that use case.
3. **MIT permissive + exact stack match + named author with industry credibility** = the strongest single in-window stack-peer of the 34-pass series.

The defer is fully reversible: the file is a peer-awareness record, not a code dependency. If the LE31 owner decides to evaluate `air` later, the file documents what to evaluate and how to evaluate it; if not, the file can be deleted with no operational impact.