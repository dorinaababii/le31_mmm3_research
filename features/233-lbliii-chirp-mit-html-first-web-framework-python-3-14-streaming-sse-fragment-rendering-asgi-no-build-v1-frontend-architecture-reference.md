# Feature 233 — `lbliii-chirp-mit-html-first-web-framework-python-3-14-streaming-sse-fragment-rendering-asgi-no-build-v1-frontend-architecture-reference` (defer)

> **NEW observation (2026-09-26).** Documents in-window GitHub Search `htmx+no-build+language:python` query result: `lbliii/chirp` (**MIT ✓**, **9★/2⑂**, Python, **pushed 2026-09-05T14:00:41Z** (in-window by `pushed_at` — *21 days before fetch time*; mid-window), **created 2026-02-07T16:56:19Z** (~7-month-old repo with in-window `pushed_at`; **IN-WINDOW BY PUSH ONLY**; `created_at` is OUT-OF-WINDOW by ~6 months), **9471 KB** substantial repo, default_branch=`main`). Topics (verbatim from raw JSON, **11 topics**): `asgi`, `free-threading`, `html-over-the-wire`, `htmx`, `hypermedia`, `no-build`, `python`, `server-sent-events`, `sse`, `streaming`, `web-framework`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-26): *"⌁⌁ Chirp — HTML-first web framework for Python 3.14+ with streaming, SSE, and fragment rendering"*. **The only 2026-09-26 in-window v1 frontend-architecture-reference that pins all 11 of `asgi + free-threading + html-over-the-wire + htmx + hypermedia + no-build + python + server-sent-events + sse + streaming + web-framework` in the topic array** = **11/11 LE31-relevant topics** = **100% topic-overlap score = the only 100% topic-overlap of any 2026-09 candidate**; vs feature 226's 6/9 (67%), feature 224's 8/10 (80%), feature 225's 9/9 (100%, the only prior 100% topic-overlap score, filed on 2026-09-24). Bucket: **v1 frontend-architecture-reference (defer, parking-lot)** — watch-list entry, zero build time today. **HONEST DISCLOSURE**: this repo was surfaced as *adjacent-evidence* in features 54 + 210 (carry-over from 2026-08-10 + 2026-09-21 reports); **today's pick promotes it to a standalone v1 frontend-architecture-reference** because the 11/11 topic-overlap score is unique among 2026-09 candidates; the *Python 3.14+ free-threading* topic explicitly names the *PEP-703-free-threading* work that LE31 v1's Python 3.13 → 3.14+ upgrade decision may need to consider; the *streaming + SSE + fragment-rendering* triplet maps directly onto LE31 v1's *cook-ticket-streaming-from-cook-bot-to-waiter-web-UI* surface that feature 23 `sse-cook-channel` documents.

## Goal

Retain the **"HTML-first web framework for Python 3.14+ with streaming, SSE, and fragment rendering"** + **"asgi + free-threading + html-over-the-wire + htmx + hypermedia + no-build + python + server-sent-events + sse + streaming + web-framework"** undecuple-primitive as a persistent v1 frontend-architecture-reference for any future LE31 v1 maintainer asking the *HTML-first + streaming + SSE + fragment-rendering + ASGI + no-build* question (does LE31 v1 evolve the existing HTMX stack to add streaming + SSE + fragment-rendering? does LE31 v1 adopt Python 3.14+ free-threading? does LE31 v1 add an `hx-sse` HTMX attribute for server-streamed cook-ticket fragments?). The artifact is the persistent *HTML-first + streaming + SSE + fragment-rendering + ASGI + free-threading + no-build* vocabulary as a *named* v1 frontend-architecture reference. No code today (MIT license permits future code reuse; vocabulary-only artifact today; 9471 KB substantial-repo size makes source-code inspection feasible for the v1 maintainer).

## Scope

**In scope (defer artifact):**
- A written record of the **HTML-first web framework** discipline: the *HTML-first* posture (matches LE31 v1's existing `index.html` mock-up + FastAPI + HTMX pattern per charter §3.2 stack-invariant posture; the *HTML-first* primitive IS the *pure-HTML-rendering-with-minimal-client-JS* discipline that LE31 v1 already implements).
- A written record of the **Python 3.14+ free-threading** discipline: the *PEP-703-free-threading* primitive (LE31 v1 today uses Python 3.13 stable; the *Python 3.14+ free-threading* posture may inform LE31 v1's Python 3.13 → 3.14+ upgrade decision; carry-over from 09-14 observation).
- A written record of the **streaming + SSE + fragment rendering** discipline: the *server-streamed-events-as-fragment-render* primitive that LE31 v1's *cook-ticket-streaming* (cook sends via Telegram, waiter receives via web-SSE; charter §3.1's *explicit-state-transition* discipline applied to the *real-time-cook-status* surface) uses today; chirp's *streaming + SSE + fragment-rendering* triplet extends LE31 v1's existing HTMX stack with the *server-pushed-HTML-fragments* primitive.
- A written record of the **ASGI + no-build + htmx + hypermedia** discipline: the *ASGI-server-runtime + no-build-step + HTMX-as-over-the-wire-hypermedia* primitive that LE31 v1 already implements via FastAPI + uvicorn + HTMX (charter §3.2 stack-invariant posture).
- A written record of the **web-framework + html-over-the-wire + server-sent-events** discipline: the *web-framework-as-server-rendered-HTML-first + html-over-the-wire + SSE* vocabulary (the *web-framework-as-cook-ticket-streaming-server* discipline is the *cook-ticket-pushed-from-server-to-waiter* primitive that LE31 v1 implements via feature 23 `sse-cook-channel`).
- A cross-section reference with the prior htmx + SSE + streaming + fragment-rendering cluster: features 23 (`sse-cook-channel`) + 25 (`fastapi-frontend-dev-loop`) + 54 (`corner-mart POS reference` + `chirp` adjacent evidence) + 142 (`feldroy-air-fastapi-htmx-ai-write-framework`) + 206 (`djust-org/djust` Phoenix-LiveView-style reactive-SSR) + 210 (`duckframework/duck` server-side-reactive-web-no-frontend-framework + `chirp` adjacent evidence). The *transferable insight* is the **HTML-first + Python 3.14+ + streaming + SSE + fragment-rendering + ASGI + free-threading + no-build + web-framework + htmx + hypermedia + html-over-the-wire + server-sent-events** undecuple-primitive.
- A decision record: today's verdict is `defer (parking-lot)` because (a) LE31 v1's existing HTMX + FastAPI + uvicorn stack already implements the *HTML-first + no-build + ASGI + htmx + hypermedia + server-sent-events* subset; (b) the *Python 3.14+ free-threading* topic is a *forward-looking* primitive that LE31 v1 does not yet need; (c) the *streaming + fragment-rendering* primitive is an *extension* of the existing feature 23 `sse-cook-channel` surface, not a new v1 surface.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI beyond adding an `hx-sse` HTMX attribute (charter §3.2 stack-invariant posture: HTMX + FastAPI + uvicorn + SQLModel + aiogram v3 + Postgres is the v1 stack).
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Python 3.13 → 3.14+ upgrade (charter §3.2 stack-invariant posture: Python 3.13 in production; 3.14+ is a future v2 decision).
- Any v2 surface in v1.
- Any customer-facing AI surface (charter §3.4 explicit invariant).
- Any owner-facing AI surface.
- Adoption of chirp's source code as a v1 dependency (chirp uses Python 3.14+ free-threading which LE31 v1 does not yet target; the *HTML-first + streaming + SSE + fragment-rendering* primitives would need to be independently re-implemented and validated against LE31's existing FastAPI + uvicorn + HTMX stack, not simply imported). The cross-section is *primitive vocabulary extension + architecture-reference*, not *library adoption*.

## Description

`lbliii/chirp` is a 9471 KB Python repository that implements an *HTML-first web framework for Python 3.14+* with three explicit extension points: **streaming**, **SSE (Server-Sent Events)**, and **fragment rendering**. The framework's design philosophy is *pure-HTML-rendering with minimal client-side JavaScript* (the *html-over-the-wire* + *htmx + hypermedia* posture); the runtime is ASGI-based (the *asgi + web-framework + server-sent-events* posture); the deployment story is *no-build* (the *no-build + html-over-the-wire* posture). The 11-topic array (`asgi + free-threading + html-over-the-wire + htmx + hypermedia + no-build + python + server-sent-events + sse + streaming + web-framework`) is the most-complete v1 frontend-architecture vocabulary surface of the 58-pass series. The free-threading topic explicitly references the *PEP-703-free-threading* CPython 3.13t/3.14+ work; the SSE + streaming + fragment-rendering triplet is the *server-pushed-HTML-fragments* primitive that LE31 v1's *cook-ticket-streaming* surface uses today (feature 23 `sse-cook-channel`).

## Data model

N/A (defer artifact; vocabulary-only; no schema change). If a future v1 PR adopts the chirp *streaming + fragment-rendering* primitive for cook-ticket-streaming, the data-model impact would be a `text/event-stream` response type on the existing `cook_ticket_stream` FastAPI endpoint, not a new SQLModel table.

## Implementation steps

N/A (defer artifact; zero build time today). If a future v1 PR adopts the chirp *streaming + fragment-rendering* primitive, the implementation steps would be:
1. Add `hx-sse` HTMX attribute to the waiter's cook-status fragment in `index.html`.
2. Add `text/event-stream` response type to the existing `cook_ticket_stream` FastAPI endpoint.
3. Replace the existing *polling-based* cook-status update with a *server-streamed-event-based* update.
4. Test end-to-end: cook sends ticket via Telegram bot → waiter receives server-streamed fragment update on web UI without manual refresh.

## Telegram interaction

N/A (defer artifact; no Telegram surface change). The chirp *streaming + SSE + fragment-rendering* primitive extends the *waiter-web-UI* surface, not the cook-bot surface; the cook-bot's `aiogram v3` Telegram-send flow is unchanged.

## Dependencies

**Existing LE31 v1 dependencies (unchanged):** Python 3.13, FastAPI, SQLModel, aiogram v3, uvicorn, Postgres.
**No new dependencies** required for the chirp *streaming + fragment-rendering* primitive beyond HTMX's `hx-sse` attribute (already in LE31 v1's HTMX stack).

## Open questions

- **Open question 1 (may kill any future PR)**: does LE31 v1 actually need the *streaming + SSE + fragment-rendering* primitive beyond the existing *polling-based* cook-status update? Today's polling-based update is functional; the *streaming + SSE + fragment-rendering* primitive is a *nice-to-have* for low-latency cook-status updates, not a *must-have*. LE31 v1's *poll-every-N-seconds* pattern is acceptable for restaurant ops (a 5-second poll latency on cook-status is not a real-world problem for restaurant ops).
- **Open question 2 (may kill any future PR)**: does LE31 v1 adopt Python 3.14+ free-threading? LE31 v1 today uses Python 3.13 stable; the *PEP-703-free-threading* work is opt-in in 3.13t and default-off in 3.14+. The free-threading primitive may inform a future v1 Python upgrade decision but is not a v1 build trigger.
- **Open question 3 (architecture reference only)**: does LE31 v1 adopt chirp's source code as a v1 dependency, or independently re-implement the *streaming + SSE + fragment-rendering* primitive against LE31's existing FastAPI + uvicorn + HTMX stack? Recommendation: independently re-implement (chirp uses Python 3.14+ free-threading which LE31 v1 does not yet target; the *streaming + SSE + fragment-rendering* primitive is small enough to re-implement in <100 LOC).

## Why this matters

The **HTML-first + Python 3.14+ + streaming + SSE + fragment-rendering + ASGI + free-threading + no-build + web-framework + htmx + hypermedia + html-over-the-wire + server-sent-events** undecuple-primitive is the **closest v1 frontend-architecture vocabulary to LE31 v1's existing HTMX stack of the 58-pass series**. The 11/11 topic-overlap score is unique among 2026-09 GitHub Search candidates. The *streaming + SSE + fragment-rendering* triplet is the *server-pushed-HTML-fragments* primitive that LE31 v1's *cook-ticket-streaming* surface already partially implements via feature 23 `sse-cook-channel` (chirp's primitive is the *named framework-level support* for the primitive that LE31 v1 implements ad-hoc). The *Python 3.14+ free-threading* primitive may inform a future v1 Python 3.13 → 3.14+ upgrade decision (carry-over from 09-14 observation). The *ASGI + no-build + htmx + hypermedia + html-over-the-wire* sextuple is the *pure-HTML-rendering + no-build-step + HTMX-as-over-the-wire-hypermedia* posture that LE31 v1's existing `index.html` mock-up + FastAPI + uvicorn + HTMX stack already implements (today's pick documents the *named architectural vocabulary* for the pattern that LE31 v1 already implements). The chirp pattern is the *future-extension-vocabulary* for LE31 v1's frontend-architecture-evolution; the *3rd-encounter-promotion* discipline (carry-over from 09-15 + 09-21 + 09-23 + 09-24) ensures that *repeatedly-surfaced* candidates with strong topic-overlap scores are promoted from *adjacent-evidence* to *standalone-vocabulary-reference* once the topic-overlap score crosses the 100% threshold.

**Fully reversible** (vocabulary-only artifact). Trigger condition = first v1 PR that adopts the chirp *streaming + SSE + fragment-rendering* primitive for cook-ticket-streaming (e.g. a `hx-sse` HTMX attribute on the cook-status fragment + a `text/event-stream` FastAPI endpoint + a Python 3.14+ free-threading evaluation PR for uvicorn ASGI server).
