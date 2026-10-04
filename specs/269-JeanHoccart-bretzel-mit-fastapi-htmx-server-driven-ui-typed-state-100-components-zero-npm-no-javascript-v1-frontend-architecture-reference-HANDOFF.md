# Pick A — `JeanHoccart/bretzel` — v1 frontend-architecture-reference — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/269-JeanHoccart-bretzel-mit-fastapi-htmx-server-driven-ui-typed-state-100-components-zero-npm-no-javascript-v1-frontend-architecture-reference.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v1 PR that adds a *server-driven-UI + typed-state* surface to the existing FastAPI + minimal-HTML/HTMX stack.
2. First v1 PR that adopts the *100+-components + zero-npm + no-javascript + SSE + Tailwind* library for waiter-ticket-display or cook-screen-display.
3. First v1 PR that introduces a *Component + ComponentInstance* SQLModel table for the 100+-components library.
4. First v1 PR that adds an SSE-streaming endpoint for live table-status / live order-status / live cook-queue-length.
5. First v1 PR that adopts the *Pydantic-as-typed-state* discipline for the entire *waiter-web-UI-state* dimension.
6. First v1 PR that adds a *Tailwind* utility-CSS dependency to `requirements.txt` or `package.json` (note: the *Tailwind* utility-CSS is OK; the *JS toolchain* is NOT OK; the *htmx* + *jinja2* are the on-LE31-stack primitives).

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v1 surface wants to **scale the existing minimal-HTML/HTMX templates to a 100+-component library without adopting a JS toolchain** (e.g., a v1 surface that wants to expose 100+ stateful UI components like live table-status, live order-status, live cook-queue-length with typed-state), the owner wants a known-good FastAPI+htmx+server-driven-UI+typed-state+100+-components+zero-npm+no-javascript+SSE+Tailwind blueprint, but LE31 today has no 100+-components library + no typed-state discipline + no SSE-streaming, so that any future v1 extension has a documented reference."* — PASS (links to features 23 + 25 + 54 + 142 + 206 + 210 + 233 + 256 + 269; justifies a new pain).
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the *server-driven-UI + typed-state* outputs on the existing minimal-HTML/HTMX waiter-web-UI. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 NOT triggered (no AI surface; the *100+-components* is deterministic HTML/HTMX rendering, not customer-facing AI); confidence **high** for vocabulary transferability, **low** for immediate LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling only; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v1** outcome (cross-section to features 23+25+54+142+206+210+233+256). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = medium (~200-500 lines of FastAPI + Jinja2 + HTMX + Tailwind + 100+-components-library code; 5-10 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/components/` (new directory) — 100+-components library (each component = a Jinja2 macro + a Pydantic typed-state model + a FastAPI endpoint that serves the component HTML + a Tailwind utility-CSS class set)
- `le31/app/models/component.py` (new) — `Component` + `ComponentInstance` SQLModel tables
- `le31/app/services/component.py` (new) — service layer for `render_component` + `register_component` + `update_component_state` + `sse_stream_component_state`
- `le31/app/hermes/hooks/component_rendering.py` (new) — Hermes Agent hook integration that records every component-state-update as an immutable row in `audit_logs` (operator-tooling only)
- `le31/app/api/v1/components.py` (new) — HTTP endpoints: `GET /api/components` + `POST /api/components` + `GET /api/components/<component_id>` + `GET /api/components/<component_id>/state` + `POST /api/components/<component_id>/state` + `GET /api/components/<component_id>/sse` (SSE streaming endpoint)
- `le31/app/waiter_ui/templates/components/` (new directory) — 100+-components Jinja2 templates (one per component: table-card, order-card, cook-queue-card, stock-card, etc.)
- `le31/app/waiter_ui/static/tailwind.css` (new) — Tailwind utility-CSS compiled output
- `le31/app/waiter_ui/templates/base.html` (modified) — add `htmx + alpinejs + tailwind` script + style tags
- `requirements.txt` (modified) — add `tailwindcss` (build-time only; the *Tailwind* utility-CSS is OK; the *JS toolchain* is NOT adopted)
- `skills/le31-conventions/SKILL.md` — append the *FastAPI + htmx + server-driven-UI + typed-state + 100+-components + zero-npm + no-javascript + SSE + Tailwind* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the 100+-components library** (remove the `le31/app/components/` directory)
- **Revert the Component + ComponentInstance tables** (remove the `le31/app/models/component.py` file + remove the import from `le31/app/models/__init__.py` + drop the tables on next alembic downgrade)
- **Revert the component service** (remove the `le31/app/services/component.py` file + remove the import from `le31/app/services/__init__.py`)
- **Revert the Hermes Agent hook** (remove the `le31/app/hermes/hooks/component_rendering.py` file + remove the hook registration from `le31/app/hermes/hooks/__init__.py`)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/components.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the 100+-components Jinja2 templates** (remove the `le31/app/waiter_ui/templates/components/` directory)
- **Revert the Tailwind utility-CSS** (remove the `le31/app/waiter_ui/static/tailwind.css` file + remove the `tailwindcss` dependency from `requirements.txt`)
- **Revert the base.html modifications** (remove the `htmx + alpinejs + tailwind` script + style tags)
- **No data loss** if the rollback happens BEFORE any component-row is written
- **Full data retention** if the rollback happens AFTER rows are written (the Component + ComponentInstance tables are dropped but the component-state-update rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked — workspace plan-limit error 15th consecutive day; parent fallback at `/opt/data/le31-daily-research-2026-10-04.linear-fallback.json`]
