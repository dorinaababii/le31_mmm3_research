# HANDOFF — Feature 314: `volfpeter-htmui-mit-python-ui-components-hypermedia-applications-fastapi-htmx-v1-hypermedia-ui-component-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

> **Note on filename**: the HANDOFF filename uses the full slug per the v1 feature contract shape (see `features/314-…-vocabulary.md`).

## Active feature path

`features/314-volfpeter-htmui-mit-python-ui-components-hypermedia-applications-fastapi-htmx-v1-hypermedia-ui-component-vocabulary.md` — defer/parking-lot (Pick A of Daily Research 2026-10-13 carry-over).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface needs a discrete hypermedia-UI-component-pack on a FastAPI + HTMX substrate, *the developer wants* ready-made UI-components they can drop into existing FastAPI views, *but struggles because* today's FastAPI+HTMX projects require hand-rolled component libraries or ad-hoc Jinja2 templates, *so that* the surface ships with less surface-area cost. |
| 2 | Viability | ✓ | Single-developer v1 surface; no specialist help needed; vocabulary-only artifact; REVERSIBLE (pure observation, zero code today). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + FastAPI ✓ ON-STACK + HTMX ✓ ON-STACK. The 8-topic topic-array = `fastapi + html + htmx + hypermedia + python + server-side-rend + web + web-development` = the most topic-rich FastAPI+HTMX+Python hypermedia-UI-component-pack topic-coverage of the 76-pass series. 13★ = 3rd-highest in-window 2026 star count of any net-new v1-admin-interface candidate of the 76-pass series. Rabbit hole: the 2-layer (framework + components) FastAPI+HTMX+Python ecosystem is not yet adopted by LE31 v1; the *discrete UI component* primitive is a v1 polish surface. Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *hypermedia + server-side-rendering* primitives are §3.1-aligned (FastAPI+HTMX+Python+server-side-rendering + append-only-audit-log). No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (discrete-HTML-UI-component-pack on waiter web UI). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry` + HTMX waiter-web-UI) already implement the *hypermedia + server-side-rendering* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (the discrete-HTML-UI-component-pack is a v1 polish surface; v1 charter is waiter-web-UI + cook-Telegram-bot + owner-daily-recap + append-only-StockEntry; the *discrete-UI-component-pack* primitive is not in v1 charter).

## Bucket

**v1** (hypermedia-UI-component-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 8-topic-array set (FastAPI + HTMX + Python + server-side-rendering + web-development + hypermedia + html + ui-components).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *discrete-HTML-UI-component-pack* discipline on the waiter web UI lands, the files to touch are:
- `backend/alembic/versions/` — add migration for `UIComponent`, `UIComponentInstance`, `UIComponentSlot` tables.
- `backend/ui_component.py` — new file with `UIComponentRegistry` class.
- `backend/ui_component_renderer.py` — new file with `UIComponentRenderer` class.
- `backend/main.py` — add `/api/ui-components` FastAPI endpoint set.
- `frontend/templates/ui-component-template.html` — new minimal-HTML/HTMX template with the discrete-component-pack UI.

## Verification protocol reference

When the first v1 PR that adopts the *discrete-HTML-UI-component-pack* discipline lands, the verification protocol is:
1. Run `pytest tests/test_ui_component.py` and verify the `UIComponentRegistry` produces a valid component lookup for the existing waiter-web-UI surfaces.
2. Run `pytest tests/integration/test_ui_component_renderer.py` and verify the renderer produces valid HTML.
3. Run `uvicorn backend.main:app` and curl `/api/ui-components` to verify the endpoint returns the component set as JSON.
4. Open `frontend/templates/ui-component-template.html` in a browser and verify the discrete-HTML-UI-component-pack renders as a navigable UI.

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *discrete-HTML-UI-component-pack* discipline lands, the rollback path is:
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

This defer artifact is documentation only. It becomes a build trigger when the **first v1 PR that adds a discrete-HTML-UI-component-pack to the LE31 single-restaurant Swiss kitchen waiter web UI** lands. At that point:
1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which UIComponent (button? form? menu-card? order-card?), which UIComponentInstance (per-page? per-section? per-user?), which UIComponentSlot (label? value? href?), and which existing v1 surface to inherit the Pydantic schemas from.
3. Adopt the *discrete-HTML-UI-component-pack* discipline on the existing v1 minimal-HTML/HTMX waiter-web-UI surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v1 code is shipped.