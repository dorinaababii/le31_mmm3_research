# HANDOFF — Feature 318: `JeanHoccart-bretzel-mit-full-stack-python-web-framework-server-driven-ui-typed-state-100-components-zero-npm-v1-no-javascript-server-driven-ui-python-framework-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

> **Note on filename**: the HANDOFF filename uses the full slug per the v1 feature contract shape (see `features/318-…-vocabulary.md`).

## Active feature path

`features/318-JeanHoccart-bretzel-mit-full-stack-python-web-framework-server-driven-ui-typed-state-100-components-zero-npm-v1-no-javascript-server-driven-ui-python-framework-vocabulary.md` — defer/parking-lot (Pick B of Daily Research 2026-10-15).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface needs a no-JavaScript server-driven UI Python framework on a FastAPI + HTMX substrate with reactive updates, *the developer wants* a ready-made Python framework with typed-state + 100+ UI-components + zero npm + server-driven-UI + SSE, *but struggles because* today's FastAPI+HTMX projects require hand-rolled state management or ad-hoc Jinja2 templates, *so that* the surface ships in 1-day of integration work instead of 1-week. |
| 2 | Viability | ✓ | Single-developer v1 surface; no specialist help needed; vocabulary-only artifact; REVERSIBLE (pure observation, zero code today). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + FastAPI ✓ ON-STACK + HTMX ✓ ON-STACK + SSE ✓ ON-STACK + reactive ✓ ON-STACK + server-driven-UI ✓ ON-STACK + no-JavaScript ✓ ON-STACK + TailwindCSS ✓ ON-STACK. The 8/8 LE31-stack-match + 12 topics (fastapi + full-stack + htmx + no-javascript + python + python-web-framework + reactive + server-driven-ui + sse + tailwindcss + ui-components + web-framework) = the most topic-rich no-JavaScript-server-driven-UI framework candidate of the 76-pass series. 3★/4⑂ = 1.33 forks-per-star = strongest fork-to-star ratio of any in-window 2026 Python web-framework candidate. Rabbit hole: the *typed-state + 100+-components + zero-npm* primitives are not yet adopted by LE31 v1; the *no-JavaScript-server-driven-UI-Python-framework* primitive is a v1 polish surface. Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *no-JavaScript + server-driven-UI + reactive + SSE* primitives are §3.1 + §3.4-aligned (Python+FastAPI+HTMX+SSE+reactive+server-driven-UI+TailwindCSS + append-only-audit-log + on-premise-deployment + non-AI-fallback). No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (no-JavaScript-server-driven-UI framework on waiter web UI). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + Pydantic schemas + HTMX waiter-web-UI) already implement the *FastAPI + HTMX + Python + no-JavaScript* discipline; the *typed-state + 100+-components + zero-npm + SSE + reactive + server-driven-UI + TailwindCSS* primitives are NEW = the reference is *naming + extending*, not just *naming*. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (the *no-JavaScript-server-driven-UI-Python-framework* primitive is a v1 polish surface; v1 charter is waiter-web-UI + cook-Telegram-bot + owner-daily-recap + append-only-StockEntry; the *no-JavaScript-server-driven-UI* primitive is not in v1 charter).

## Bucket

**v1** (no-JavaScript-server-driven-UI-Python-framework-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the duodecuple-primitive set (full-stack-Python-web-framework + server-driven-UI + typed-state + 100+-components + zero-npm + FastAPI + HTMX + no-JavaScript + reactive + SSE + TailwindCSS + UI-components + web-framework).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *no-JavaScript-server-driven-UI-Python-framework* discipline on the waiter web UI lands, the files to touch are:
- `backend/alembic/versions/` — add migration for `ServerDrivenState`, `ServerDrivenComponent`, `ServerDrivenSubscription` tables.
- `backend/server_driven_state_manager.py` — new file with `ServerDrivenStateManager` class.
- `backend/server_driven_component_renderer.py` — new file with `ServerDrivenComponentRenderer` class.
- `backend/server_driven_sse_broadcaster.py` — new file with `ServerDrivenSSEBroadcaster` class.
- `backend/main.py` — add `/api/server-driven-ui` FastAPI endpoint set.
- `frontend/templates/server-driven-ui.html` — new minimal-HTML/HTMX template with the no-JavaScript server-driven UI framework.

## Verification protocol reference

When the first v1 PR that adopts the *no-JavaScript-server-driven-UI-Python-framework* discipline lands, the verification protocol is:
1. Run `pytest tests/test_server_driven_state_manager.py` and verify the `ServerDrivenStateManager` produces a valid server-side typed-state.
2. Run `pytest tests/integration/test_server_driven_component_renderer.py` and verify the renderer produces valid HTML.
3. Run `uvicorn backend.main:app` and curl `/api/server-driven-ui` to verify the endpoint returns the state + component set as JSON.
4. Open `frontend/templates/server-driven-ui.html` in a browser and verify the no-JavaScript server-driven UI renders as a navigable UI with reactive SSE updates.

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *no-JavaScript-server-driven-UI-Python-framework* discipline lands, the rollback path is:
1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the three tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:
- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-v1-feature-pattern/SKILL.md` — for the v1 feature contract shape and slicing rules.
- `skills/le31-research/SKILL.md` — for the research workflow and report shape.
- `skills/le31-feature-pipeline/SKILL.md` — for the feature pipeline (lease to coding agent).
- `skills/le31-handoff-spec/SKILL.md` — for the handoff spec (this file).
- `skills/le31-coding-agent-brief/SKILL.md` — for the paste-in brief.
- `skills/le31-backend/SKILL.md` — for the backend conventions (if applicable).
- `skills/le31-frontend/SKILL.md` — for the frontend conventions (if applicable).
- `skills/le31-data/SKILL.md` — for the data conventions (if applicable).
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

This defer artifact is documentation only. It becomes a build trigger when the **first v1 PR that adopts the no-JavaScript server-driven UI framework on the waiter web UI** lands. At that point:
1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which ServerDrivenState (table-state? menu-state? order-state?), which ServerDrivenComponent (button? form? card?), which ServerDrivenSubscription (per-user? per-role? per-section?), and which existing v1 surface to inherit the Pydantic schemas from.
3. Adopt the *no-JavaScript-server-driven-UI* discipline on the existing v1 minimal-HTML/HTMX waiter-web-UI surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v1 code is shipped.