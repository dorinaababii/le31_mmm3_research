# Feature 314 — `volfpeter-htmui-mit-python-ui-components-hypermedia-applications-fastapi-htmx-v1-hypermedia-ui-component-vocabulary` (defer)

> **NEW observation (2026-10-15).** Documents 10-13 daily-research PICK A carry-over (was promised in 2026-10-13 report's INDEX-narrative truth but the actual feature file was never written; today's pass closes the INDEX-vs-on-disk gap). GitHub `volfpeter/htmui` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **13★/1⑂**, language Python ✓ ON-STACK, **pushed 2026-10-12T16:56:17Z**, **created 2026-02-23T13:15:35Z = 8-month-old repo with in-window push**, **507 KB modest**, `default_branch=main`, archived=`False`). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-15): *"Python UI components for building hypermedia applications."* Topics (verbatim, parent-verified, 8): `fastapi, html, htmx, hypermedia, python, server-side-rend, web, web-development`. Bucket: **v1 (hypermedia-UI-component-vocabulary)** — Pick A of Daily Research 2026-10-13 carry-over. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`Python-UI-components-for-building-hypermedia-applications + FastAPI + HTMX + Python`** quadruple-primitive as a persistent cross-section reference for the LE31 v1 *hypermedia-UI-component-pack* wedge, and document the **FastAPI + HTMX + Python + server-side-rendering + 8-topic topic-array** stack-shape validation that an independent maintainer (`volfpeter` — same author as feature 143 `volfpeter/fasthx`) arrived at in 2026. The artifact is a persistent cross-section reference + a stack-validation that the discrete-UI-component-pack layer on top of FastAPI+HTMX is a real shape in 2026. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`Python-UI-components-for-building-hypermedia-applications + FastAPI + HTMX + Python + server-side-rendering + 8-topic topic-array** quadruple-primitive.
- A written record of the **stack-shape validation**: `volfpeter/htmui` is the discrete-UI-component-pack primitive on top of FastAPI + HTMX = the same author's `volfpeter/fasthx` = feature 143 is the declarative-SSR-framework primitive. The two primitives together = the FastAPI + HTMX ecosystem is **two-layer** (framework + components).
- A written record of the **8-topic topic-array** = `fastapi + html + htmx + hypermedia + python + server-side-rend + web + web-development` = the most topic-rich FastAPI + HTMX + Python hypermedia-UI-component-pack of the 76-pass series.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of `volfpeter/htmui` codebase (single-author 13★ sister-shape to feature 143 `volfpeter/fasthx`; LE31 v1 has no UI-component-pack surface today; the *discrete UI component* primitive is a v1 polish surface).
- Cross-pollination with the v1 charter §3.4 customer-facing-AI posture (the *hypermedia-UI-component-pack* surface is operator-tooling, not customer-facing).

## Description

GitHub `volfpeter/htmui` (MIT, 13★/1⑂, Python, pushed 2026-10-12T16:56:17Z, created 2026-02-23T13:15:35Z = 8-month-old repo with in-window push, 507 KB modest, default_branch=`main`, archived=`False`).

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **Python UI components for building hypermedia applications** — the *discrete-UI-component-pack primitive* on top of FastAPI + HTMX.
2. **FastAPI + HTMX + Python** = **3/3 LE31-stack-match** = the strongest in-window 2026 v1 FastAPI+HTMX+Python hypermedia-UI-component-pack stack-match of the 76-pass series (vs `feldroy/air` = feature 142 = FastAPI+HTMX+ai-write-framework not component-pack-specific).
3. **8 topics including `fastapi + html + htmx + hypermedia + python + server-side-rend + web + web-development`** = the most topic-rich v1 FastAPI+HTMX+Python hypermedia-UI-component-pack of the 76-pass series.
4. **Sister-shape to feature 143** (`volfpeter/fasthx` = same author, different repo) — but `htmui` is the **discrete hypermedia-component-pack**, not the declarative-SSR framework.
5. **13★** = the **3rd-highest in-window 2026 star count of any net-new Python permissive in-domain non-watchlist of the 76-pass series** (after `brockamer/findajob` ★19 and `alltuner/vibetuner` ★14).

**The 1:1 mapping onto LE31 surface:**

| htmui-primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Python UI components | (LE31 v1 has hand-rolled Jinja2 templates) | §3.1 ✓ | **Not implemented** — v1 polish surface |
| FastAPI + HTMX + Python | (LE31 v1 uses FastAPI + HTMX + Python) | §3.1 ✓ | **Implemented (v1, partial)** — the *FastAPI + HTMX* is implemented; the *discrete-component-pack* primitive is **Not implemented** — v1 polish surface |
| hypermedia + server-side-rend | (LE31 v1 uses minimal-HTML/HTMX) | §3.1 ✓ | **Implemented (v1)** |
| Same author as feature 143 | (LE31 v1 has no UI-component-pack surface) | n/a | Sister-shape |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds a discrete-HTML-UI-component-pack to the waiter web UI), the implementation would add:

1. A new `UIComponent` SQLModel table (Alembic migration) with columns: `id` (UUID), `name` (str, unique), `category` (str), `template_html` (str), `htmx_attributes` (JSON), `requires_auth` (bool), `created_at`, `updated_at`.
2. A new `UIComponentInstance` SQLModel table (Alembic migration) with columns: `id` (UUID), `component_id` (UUID FK), `page_id` (UUID FK), `position_index` (int), `rendered_html` (str), `created_at`, `updated_at`.
3. A new `UIComponentSlot` SQLModel table (Alembic migration) with columns: `id` (UUID), `instance_id` (UUID FK), `slot_name` (str), `slot_value` (str), `created_at`.
5. An Alembic migration that adds the new tables.
6. A `UIComponentRegistry` service that loads the `UIComponent` set + builds the component lookup + worker-side render.
7. A `UIComponentRenderer` service that renders a `UIComponentInstance` to HTML with the current `UIComponentSlot` values + applies the HTMX attributes.
8. A `ui-component-template.html` minimal-HTML/HTMX template that renders the UIComponent pack.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires:

**For v1 hypermedia-UI-component-pack surface** (if approved):
1. Add new `UIComponent` SQLModel table (Alembic migration).
2. Add new `UIComponentInstance` SQLModel table (Alembic migration).
3. Add new `UIComponentSlot` SQLModel table (Alembic migration).
4. Add Alembic migration for the new tables.
5. Add a `UIComponentRegistry` service that loads the `UIComponent` set + builds the component lookup.
6. Add a `UIComponentRenderer` service that renders a `UIComponentInstance` to HTML.
7. Add a `ui-component-template.html` minimal-HTML/HTMX template that renders the UIComponent pack.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires, the v1 hypermedia-UI-component-pack surface would add **a v1 cook-Telegram-component primitive** (e.g., the cook Telegram bot subscribes to a UIComponent pack and receives formatted component messages). The cook-Telegram-component primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 53/66 (offline-first).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; `volfpeter/htmui` stack is Python + FastAPI + HTMX + server-side-rendering which is on-§3.1).
- **External**: None.
- **Internal**: §3.1 (Python+FastAPI+HTMX on-§3.1); §3.2 (MIT permissive on-§3.2); §3.4 (no customer-facing AI on-§3.4).
- **Trigger dependency**: future v1 PR that adds a discrete-HTML-UI-component-pack to the waiter web UI.

## Open questions

- **Q1**: When (if ever) will LE31 introduce a discrete-HTML-UI-component-pack? The v1 charter explicitly uses minimal-HTML/HTMX + hand-rolled Jinja2 templates; the UIComponent-pack primitive is a v1 polish surface.
- **Q2**: If the UIComponent-pack surface lands, will it use `volfpeter/htmui` or `feldroy/air` = feature 142 or hand-rolled? The `volfpeter/htmui` approach is a discrete-component-pack = the *adopt-the-upstream-component-pack* primitive; the *hand-rolled* approach is the *start-from-zero* primitive.
- **Q3**: Will the *hypermedia + server-side-rendering* posture align with LE31 v1's existing `audit_logs` schema? The *hypermedia + server-side-rendering* posture IS the *append-only-audit-trail + state-transition-via-server-side-action* invariant applied to the *UIComponent* dimension.

## Why this matters

The **`Python-UI-components-for-building-hypermedia-applications + FastAPI + HTMX + Python + server-side-rendering + 8-topic topic-array`** quadruple-primitive is the **strongest direct LE31 v1 FastAPI+HTMX+Python hypermedia-UI-component-pack stack-match of the 76-pass series** for three reasons:

1. **The 3/3 LE31-stack-match is the canonical FastAPI+HTMX+Python posture**: when LE31 v1 introduces a discrete-HTML-UI-component-pack surface (e.g., a v1 surface that lets the waiter drag-and-drop pre-built components into a waiter-web-UI page), the FastAPI+HTMX+Python substrate is the existing v1 stack.
2. **The 8-topic topic-array is the strongest FastAPI+HTMX+Python hypermedia-UI-component-pack topic-coverage of the 76-pass series**: the *hypermedia + server-side-rendering + web-development* triple-primitive is the canonical FastAPI+HTMX+Python UI-component-pack topic-coverage.
3. **The same-author-sister-shape-to-feature-143 confirmation is the strongest FastAPI+HTMX+Python UI-component-pack framework-validation of the 76-pass series**: `volfpeter` maintains both `fasthx` (feature 143) and `htmui` (this feature 314) = the FastAPI+HTMX+Python ecosystem has **two-layer** (framework + components) validation by the same author = strongest signal that the FastAPI+HTMX+Python UI-component-pack discipline is production-viable.

Sister-shape to features 142 (`feldroy/air` = FastAPI+HTMX+ai-write-framework) + 143 (`volfpeter/fasthx` = declarative-SSR-framework) + 308 (`manwithacat/dazzle` = hypermedia-FastAPI-stack-shape) + 315 (`yevheniidehtiar/hyper-admin` = admin-interface-vocabulary). The `volfpeter/htmui` pattern is the **strongest direct Python-UI-components-hypermedia-applications + FastAPI + HTMX + Python + server-side-rendering primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v1 PR that adds a discrete-HTML-UI-component-pack to the waiter web UI.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/142-feldroy-air-…md` — FastAPI+HTMX+ai-write-framework (sister-shape)
- `features/143-volfpeter-fasthx-…md` — declarative-SSR-framework (sister-shape same-author)
- `features/308-manwithacat-dazzle-…md` — hypermedia-FastAPI-stack-shape (sister-shape)
- `features/315-yevheniidehtiar-hyper-admin-…md` — admin-interface-vocabulary (sister-shape; PICK B 10-13 carry-over)

---

**Parent research issue**: [linear: blocked] (parent fallback at `/opt/data/le31-daily-research-2026-10-15.linear-fallback.json`). Original Daily Research issue: 2026-10-13 PICK A carry-over.