# 206 — djust-org/djust phoenix-liveview-style-reactive-server-side-rendering + HTMX-alternative + WebSocket + Rust-performance HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 reactive-SSR + HTMX-alternative + WebSocket + Rust-performance question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/206-djust-org-djust-phoenix-liveview-style-reactive-server-side-rendering-django-rust-websocket-htmx-alternative.md` (defer artifact; **no code today**).

Bucket: **v1 UI-architecture-reference (reactive-SSR + HTMX-alternative + WebSocket + Rust-performance primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintainer asks *'if v1 introduces a reactive-SSR pattern, a WebSocket route to the waiter web UI, or a Rust-accelerated hot-path component to the FastAPI serving layer, what is the reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance primitive that preserves the existing v1 SSE-cook-channel + HTMX-server-side-rendering + pure-Python-FastAPI invariants?'*, the maintainer wants *evidence that another independent 2026 Python+Rust repo at 62089 KB with MIT license + in-window-by-push-only + 92★/7⑂ + 9 topics including htmx-alternative + liveview + reactive + real-time + rust + server-side-rendering + websocket is shipping the Phoenix LiveView-style reactive-SSR primitive as the v1 UI-architecture reference discipline*, but struggles because *v1 has no documented reactive-SSR primitive in the charter*, so that *v1 can introduce the reactive-SSR + stateful-connection + server-pushed-DOM-diffs vocabulary with the explicit HTMX-alternative positioning rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no reactive-SSR trigger; the JTBD is primitive vocabulary extension + reactive-SSR documentation, not a build-need). |
| 2 | **Viability** | Owner can read 62089 KB repo description + 9-topic vocabulary + reactive-SSR + HTMX-alternative + WebSocket + Rust-performance topic set? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the reactive-SSR vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the Django + Rust crate). Confidence: medium-high for the reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance vocabulary (MIT + Python + 62089 KB substantial + in-window-by-push-only + 92★/7⑂ + 9 topics + explicit LiveView-style description + htmx-alternative positioning = §3.2 STRICTLY-COMPATIBLE). Stack: FastAPI + PostgreSQL backend = on-pattern for v1 primitives; Django frontend = off-pattern for v1 (LE31 v1 uses FastAPI + HTMX, not Django + djust); Rust crate = off-pattern for v1 (LE31 v1 uses pure-Python FastAPI + uvicorn); MIT license = on-pattern for code adoption (LE31 could re-implement against its own stack). Practicability of adoption: high for vocabulary + architecture-reference adoption (MIT §3.2 STRICTLY-COMPATIBLE); medium for code reuse (LE31 would re-implement against its own stack, not import Django + Rust crate code). **PASS** (posture validation only; adoption is v1 question). |
| 4 | **Conflict** | None. The reactive-SSR primitive (stateful-connection + server-pushed-DOM-diffs) is an *extension* of the existing v1 SSE-cook-channel (feature 23) — not a replacement; the existing SSE cook channel serves the cook-bot's order-status alerts; the reactive-SSR pattern could supplement the SSE cook channel with a WebSocket channel for the waiter web UI. Charter §3.1 alignment (stateful-connection + server-pushed-DOM-diffs is *explicit-state-transitions* applied to UI state); §3.2 STRICTLY-COMPATIBLE (MIT license); §3.4 not applicable (UI pattern, not AI surface). **PASS**. |
| 5 | **Outcome, appetite, scope** | v1 UI-architecture-reference (reactive-SSR + HTMX-alternative + WebSocket + Rust-performance vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 62089 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (62089 KB is substantial; only the *reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance* vocabulary + the in-window-by-push-only signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/206-djust-org-djust-phoenix-liveview-style-reactive-server-side-rendering-django-rust-websocket-htmx-alternative-HANDOFF.md` and `features/206-djust-org-djust-phoenix-liveview-style-reactive-server-side-rendering-django-rust-websocket-htmx-alternative.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance documentation for the next v1 UI-architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a WebSocket route to the waiter web UI, a server-pushed-DOM-diff mechanism to the cook Telegram bot, or a Rust-accelerated hot-path component to the FastAPI serving layer):

- `app/api/websocket.py` — possibly add (the FastAPI WebSocket route that handles the *stateful-connection + server-pushed-DOM-diffs* pattern; depends on the v1 change).
- `app/api/sse_cook_channel.py` — possibly modify to add a WebSocket alternative (the SSE cook channel could be supplemented by a WebSocket channel; depends on the v1 change).
- `app/web/reactive.py` — possibly add (the reactive-SSR pattern implementation for the waiter web UI; depends on the v1 change).
- `app/bot/cook.py` — possibly modify to add the *server-pushed-DOM-diff mechanism* (the cook-bot surface when the server detects a new order status; depends on the v1 change).
- `tests/test_reactive_ssr.py` — possibly add (the integration test for the reactive-SSR pattern; depends on the v1 change).
- `Cargo.toml` + Rust crate — possibly add (the Rust-accelerated hot-path component; depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no Rust crate added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/206-djust-org-djust-phoenix-liveview-style-reactive-server-side-rendering-django-rust-websocket-htmx-alternative.md` exists and is read back by the parent.
- [ ] `specs/206-djust-org-djust-phoenix-liveview-style-reactive-server-side-rendering-django-rust-websocket-htmx-alternative-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `djust-org/djust` description is quoted verbatim (62089 KB repo).
- [ ] The 92★/7⑂ + MIT license (§3.2 STRICTLY-COMPATIBLE for code adoption) + Python + in-window-by-push-only + 9 topics (htmx-alternative + liveview + reactive + real-time + rust + server-side-rendering + websocket + django + pwa) is documented.
- [ ] The charter §3.1 alignment via *stateful-connection + server-pushed-DOM-diffs* (explicit-state-transitions applied to UI state) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds a WebSocket route to the waiter web UI, a server-pushed-DOM-diff mechanism to the cook Telegram bot, or a Rust-accelerated hot-path component to the FastAPI serving layer lands):**
- [ ] The PR is read back by the parent.
- [ ] The `djust-org/djust` reactive-SSR + HTMX-alternative + LiveView-style + WebSocket + Rust-performance vocabulary is evaluated against the PR's changes: does the change address the *stateful-connection + server-pushed-DOM-diffs* discipline? does the change preserve the *HTMX-alternative positioning*? does the change preserve the *LiveView-style + WebSocket + Rust-performance* triple?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the `app/api/websocket.py` FastAPI route; remove the `app/web/reactive.py` reactive-SSR pattern; remove the `Cargo.toml` + Rust crate; restore the original `app/bot/cook.py` Telegram handler.
- Migration cost: depends on the v1 change; the reactive-SSR vocabulary is *additive architecture* (the WebSocket route is *added alongside* the existing SSE cook channel; the reactive-SSR pattern is *added on top of* the existing HTMX-server-side-rendering posture; the Rust crate is *new* dependency, not a schema change).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `StockEntry` table retains all rows; the WebSocket route is *new* code, not a schema change; the reactive-SSR pattern is *new* code, not a schema change; the Rust crate is *new* code, not a schema change; the verification log is a *new* document, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:
1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.
