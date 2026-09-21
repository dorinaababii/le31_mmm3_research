# 210 — duckframework/duck server-side-reactive-web-no-frontend-framework-no-javascript-stack-HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 server-side-reactive-web + no-SPA + no-JS-build + WebSocket + HTTP/2 + reverse-proxy question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/210-duckframework-duck-server-side-reactive-web-no-frontend-framework-no-javascript-stack-http2-websocket-reverse-proxy.md` (defer artifact; **no code today**).

Bucket: **v2 no-build reactive-web (server-side-reactive-web + no-SPA + no-JS-build + WebSocket + HTTP/2 + reverse-proxy + reactive-ui + real-time primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a server-side-reactive-web surface, a WebSocket-stateful-connection primitive, an HTTP/2-multiplexed-websocket primitive, or a reverse-proxy-as-application-server primitive, what is the *server-side-reactive-web + no-SPA + no-JS-build + WebSocket + HTTP/2 + reverse-proxy + reactive-ui + real-time* vocabulary that preserves the existing v1 no-server-side-reactive-web + manual-refresh + form-submission posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 20529 KB with 46★/3⑂ + BSD-3-Clause permissive + in-window-by-push-only + 20 topics including reactive + reactive-ui + real-time + server-side + websocket + http2 + reverse-proxy is shipping the server-side-reactive-web + no-SPA + no-JS-build primitive as the v2 no-build reactive-web discipline*, but struggles because *v1 has no documented server-side-reactive-web primitive in the charter*, so that *v2 can introduce the server-side-reactive-web + no-SPA + no-JS-build + WebSocket + HTTP/2 + reverse-proxy vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no server-side-reactive-web trigger; the JTBD is primitive vocabulary extension + server-side-reactive-web + no-SPA + no-JS-build documentation, not a build-need). |
| 2 | **Viability** | Owner can read 20529 KB repo description + 20-topic vocabulary + server-side-reactive-web + no-SPA + no-JS-build + WebSocket + HTTP/2 + reverse-proxy + reactive-ui + real-time octuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v2 (the *server-side-reactive-web* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the duckframework/duck codebase; LE31 v1 has no server-side-reactive-web surface today). Confidence: medium for the *server-side-reactive-web + no-SPA + no-JS-build + WebSocket + HTTP/2 + reverse-proxy + reactive-ui + real-time* vocabulary (BSD-3-Clause + Python + 20529 KB substantial + in-window-by-push-only + 46★/3⑂ + 20 topics + explicit server-side-reactive-web + no-SPA + no-JS-build description + 7 LE31-relevant topics = §3.2 STRICTLY-COMPATIBLE + §3.4 not triggered). Stack: FastAPI + PostgreSQL backend = on-pattern for v2 primitives; WebSocket = on-pattern for v2; HTTP/2 = on-pattern for v2; reverse-proxy = off-pattern for v1 (LE31 v1's FastAPI + uvicorn does not include a reverse-proxy); BSD-3-Clause permissive = on-pattern for code adoption. Practicability of adoption: high for vocabulary + architecture-reference adoption (BSD-3-Clause §3.2 STRICTLY-COMPATIBLE); low for code reuse (LE31 would re-implement against its own stack, not import the duckframework/duck codebase). **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *server-side-reactive-web* discipline IS the *charter §3.1 explicit-state-transition discipline* applied to the server-driven-reactivity dimension (the state lives on the server; the client receives DOM-diffs). Charter §3.1 alignment (the *server-side-reactive-web* vocabulary is *explicit-state-transition* applied to the server-driven-reactivity dimension); §3.2 STRICTLY-COMPATIBLE (BSD-3-Clause permissive); §3.4 not triggered (no AI surface; the *server-side-reactive-web* pattern is *operator-tooling UI* territory). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 no-build reactive-web (server-side-reactive-web + no-SPA + no-JS-build + WebSocket + HTTP/2 + reverse-proxy + reactive-ui + real-time vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 20529 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (20529 KB is substantial; only the *server-side-reactive-web + no-SPA + no-JS-build + WebSocket + HTTP/2 + reverse-proxy + reactive-ui + real-time* vocabulary + the in-window-by-push-only signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/210-duckframework-duck-server-side-reactive-web-no-frontend-framework-no-javascript-stack-http2-websocket-reverse-proxy-HANDOFF.md` and `features/210-duckframework-duck-server-side-reactive-web-no-frontend-framework-no-javascript-stack-http2-websocket-reverse-proxy.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + server-side-reactive-web + no-SPA + no-JS-build documentation for the next v2 no-build-reactive-web-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a server-side-reactive-web surface to the LE31 v2 operator surface, a WebSocket-stateful-connection primitive to the LE31 v2 architecture, an HTTP/2-multiplexed-websocket primitive, or a reverse-proxy-as-application-server primitive):

- `app/web/reactive/` — possibly add (the server-side-reactive-web module; depends on the v2 change).
- `app/web/reactive/websocket.py` — possibly add (the WebSocket-stateful-connection primitive that pushes DOM-diffs to clients; depends on the v2 change).
- `app/web/reactive/http2.py` — possibly add (the HTTP/2-multiplexing primitive; depends on the v2 change).
- `app/web/reverse_proxy.py` — possibly add (the reverse-proxy-as-application-server primitive; depends on the v2 change).
- `app/web/reactive/state.py` — possibly add (the server-side-state primitive that tracks the source-of-truth state on the server; depends on the v2 change).
- `tests/test_reactive_websocket.py` + `tests/test_http2_multiplexing.py` + `tests/test_reverse_proxy.py` + `tests/test_reactive_state.py` — possibly add (the integration tests for the server-side-reactive-web + WebSocket-stateful-connection + HTTP/2-multiplexed-websocket + reverse-proxy-as-application-server primitives; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no server-side-reactive-web surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/210-duckframework-duck-server-side-reactive-web-no-frontend-framework-no-javascript-stack-http2-websocket-reverse-proxy.md` exists and is read back by the parent.
- [ ] `specs/210-duckframework-duck-server-side-reactive-web-no-frontend-framework-no-javascript-stack-http2-websocket-reverse-proxy-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `duckframework/duck` description is quoted verbatim (20529 KB repo).
- [ ] The 46★/3⑂ + BSD-3-Clause permissive license (§3.2 STRICTLY-COMPATIBLE for code adoption) + Python + in-window-by-push-only + 20 topics (reactive + reactive-ui + real-time + server-side + websocket + http2 + reverse-proxy = 7 LE31-relevant topics) is documented.
- [ ] The charter §3.1 alignment via *server-side-reactive-web = explicit-state-transition discipline applied to server-driven-reactivity* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (BSD-3-Clause permissive) is documented.
- [ ] The charter §3.4 not-triggered (no AI surface) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a server-side-reactive-web surface to the LE31 v2 operator surface, a WebSocket-stateful-connection primitive to the LE31 v2 architecture, an HTTP/2-multiplexed-websocket primitive, or a reverse-proxy-as-application-server primitive lands):**
- [ ] The PR is read back by the parent.
- [ ] The `duckframework/duck` *server-side-reactive-web + no-SPA + no-JS-build + WebSocket + HTTP/2 + reverse-proxy + reactive-ui + real-time* vocabulary is evaluated against the PR's changes: does the change address the *server-driven-reactivity* discipline? does the change preserve the *WebSocket-stateful-connection* primitive? does the change preserve the *HTTP/2-multiplexing* primitive? does the change preserve the *reverse-proxy-as-application-server* primitive? does the change preserve the *charter §3.1 explicit-state-transition* pattern?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the `app/web/reactive/` server-side-reactive-web module; remove the `app/web/reactive/websocket.py` WebSocket-stateful-connection primitive; remove the `app/web/reactive/http2.py` HTTP/2-multiplexing primitive; remove the `app/web/reverse_proxy.py` reverse-proxy-as-application-server primitive; remove the `app/web/reactive/state.py` server-side-state primitive; restore the original `app/main.py` FastAPI app.
- Migration cost: depends on the v2 change; the *server-side-reactive-web* vocabulary is *additive architecture* (the reactive module is *new* files; the WebSocket primitive is *new* code; the HTTP/2 primitive is *new* code; the reverse-proxy primitive is *new* code; the server-side-state primitive is *new* code, not a schema change).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `StockEntry` table retains all rows; the new `web_socket_session` table is *new* data, not a schema change; the new `web_socket_state` table is *new* data, not a schema change; the verification log is a *new* document, not a schema change.

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