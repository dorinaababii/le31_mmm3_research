# Pick B — `Prism-Infoways/Tungsten` — v1 admin-panel-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/270-Prism-Infoways-Tungsten-mit-fastapi-admin-panel-filament-style-sqlmodel-sqlalchemy-jinja2-htmx-alpinejs-v1-admin-panel-vocabulary-reference.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v1 PR that adds a *Filament-style-admin-panel-for-FastAPI* surface to the existing FastAPI + SQLModel + minimal-HTML/HTMX stack.
2. First v1 PR that adopts the *describe-a-model-once-in-Python + list/create/edit/view-pages* discipline for the existing SQLModel tables (MenuItem + StockEntry + Order + CustomerVisit + Discount + StoredValueTransaction + audit_logs).
3. First v1 PR that adds a `tungsten-admin` pip dependency to `requirements.txt`.
4. First v1 PR that adds an `/admin/menu-items/` + `/admin/stock-entries/` + `/admin/orders/` + `/admin/customer-visits/` + `/admin/discounts/` + `/admin/stored-value-transactions/` + `/admin/audit-logs/` FastAPI route prefix set.
5. First v1 PR that introduces a *role-based-access-control* layer for the admin-panel (the *admin-panel* must respect the existing *role-based-access* posture per charter §3.7; the *role-based-access* IS the *audit-on-behalf-of-operator* charter §3.7 invariant).
6. First v1 PR that adds a *list-page* + *create-page* + *edit-page* + *view-page* for any existing SQLModel table (e.g., a `MenuItem` admin-page or a `StockEntry` admin-page).

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v1 surface wants to **expose the existing SQLModel tables (MenuItem + StockEntry + Order + CustomerVisit + Discount + StoredValueTransaction + audit_logs) as a CRUD UI without writing custom HTML for each surface** (e.g., a v1 surface that wants to give the owner a self-service admin-panel for menu-management + stock-management + order-management), the owner wants a known-good Filament-style+FastAPI+admin-panel+describe-a-model-once-in-Python+list/create/edit/view-pages+pip-install-tungsten-admin blueprint, but LE31 today has no admin-panel + no auto-generate-CRUD-UI-from-SQLModel, so that any future v1 extension has a documented reference."* — PASS (links to features 02 + 03 + 09 + 22 + 116 + 152 + 175 + 187 + 195 + 201 + 205 + 218 + 220 + 221 + 222 + 223 + 224 + 225 + 232 + 236 + 237 + 239 + 240 + 242 + 243 + 244 + 246 + 248 + 251 + 252 + 254 + 255 + 256 + 257 + 258 + 259 + 260 + 261 + 262 + 263 + 264 + 265 + 266 + 267 + 268 + 270; justifies a new pain).
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the *list/create/edit/view-pages* outputs on the existing minimal-HTML/HTMX admin-panel. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 NOT triggered (no AI surface; the *describe-a-model-once-in-Python* is deterministic Pydantic-validation, not LLM; the *list/create/edit/view-pages* is deterministic CRUD rendering, not customer-facing AI); confidence **high** for vocabulary transferability, **low** for immediate LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling only; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v1** outcome (cross-section to features 02+03+09+22+116+152+175+187+195+201+205+218+220+221+222+223+224+225+232+236+237+239+240+242+243+244+246+248+251+252+254+255+256+257+258+259+260+261+262+263+264+265+266+267+268). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = low-medium (~50-200 lines of FastAPI + Jinja2 + HTMX + AlpineJS + SQLModel + tungsten-admin code; 2-5 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/admin/` (new directory) — admin-panel package
- `le31/app/admin/__init__.py` (new) — admin-panel package init
- `le31/app/admin/auto_crud.py` (new) — auto-generate-CRU D-UI-from-SQLModel primitive (reads the existing SQLModel tables + auto-generates list-page + create-page + edit-page + view-page)
- `le31/app/admin/routes.py` (new) — HTTP routes: `/admin/<table-name>/` (list) + `/admin/<table-name>/new` (create) + `/admin/<table-name>/<id>` (view) + `/admin/<table-name>/<id>/edit` (edit) for each SQLModel table
- `le31/app/admin/templates/` (new directory) — Jinja2 templates for list-page + create-page + edit-page + view-page
- `le31/app/admin/static/admin.css` (new) — admin-panel CSS (Tailwind utility-CSS is OK)
- `le31/app/api/v1/admin.py` (new) — admin-panel HTTP endpoints: `GET /admin/menu-items/` + `POST /admin/menu-items/new` + `GET /admin/menu-items/<id>` + `GET /admin/menu-items/<id>/edit` + ... (one set per SQLModel table)
- `le31/app/hermes/hooks/admin_panel_access.py` (new) — Hermes Agent hook integration that records every admin-panel-CRUD-action as an immutable row in `audit_logs` (operator-tooling only; **role-based-access-required per charter §3.7**)
- `le31/app/owner_dashboard/templates/admin_base.html` (new) — admin-panel base template (extends `owner_dashboard/templates/base.html` with admin-specific nav)
- `requirements.txt` (modified) — add `tungsten-admin` (the *pip-install-tungsten-admin* IS the *pip-as-deployment* charter §3.1 invariant)
- `skills/le31-conventions/SKILL.md` — append the *Filament-style + FastAPI + admin-panel + describe-a-model-once-in-Python + list/create/edit/view-pages + pip-install-tungsten-admin* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the admin-panel package** (remove the `le31/app/admin/` directory)
- **Revert the auto-generate-CRUD-UI-from-SQLModel primitive** (revert `le31/app/admin/auto_crud.py`)
- **Revert the admin-panel routes** (revert `le31/app/admin/routes.py` + remove the import from `le31/app/admin/__init__.py`)
- **Revert the admin-panel templates** (remove the `le31/app/admin/templates/` directory)
- **Revert the admin-panel CSS** (remove the `le31/app/admin/static/admin.css` file)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/admin.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the Hermes Agent hook** (remove the `le31/app/hermes/hooks/admin_panel_access.py` file + remove the hook registration from `le31/app/hermes/hooks/__init__.py`)
- **Revert the admin-panel base template** (remove the `le31/app/owner_dashboard/templates/admin_base.html` file)
- **Revert the `tungsten-admin` dependency** (remove `tungsten-admin` from `requirements.txt`)
- **No data loss** if the rollback happens BEFORE any admin-panel-CRUD-action is performed
- **Full data retention** if the rollback happens AFTER actions are performed (the admin-panel-CRUD-action rows are preserved in `audit_logs` per the *append-only* invariant; the underlying SQLModel table rows are preserved by the existing SQLModel schema)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked — workspace plan-limit error 15th consecutive day; parent fallback at `/opt/data/le31-daily-research-2026-10-04.linear-fallback.json`]
