# Feature 350 — `giammbo-incident-commander-apache-2-0-self-hosted-incident-management-one-click-declaration-configurable-lifecycle-timeline-postmortems-fastapi-htmx-python-v2-owner-pains-operator-utility-vocabulary` (defer)

> **Pick A of Daily Research 2026-10-21.** Documents in-window GitHub repo `giammbo/incident-commander` (**Apache-2.0 ✓ §3.2 permissive**, **★5/⑂1**, **1558 KB modest**, **Python ✓ ON-STACK** + **FastAPI ✓ ON-STACK** + **HTMX ✓ ON-STACK**, **pushed 2026-10-20T13:19:22Z** = in-window by `pushed_at`, **created 2026-04-30T03:14:02Z** = ~5.5-month-old repo with in-window push, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-21): *"Open-source, self-hosted incident management: one-click declaration, configurable lifecycle & timeline, postmortems (auto-generated post-incident review)."* Topics (verbatim, parent-verified, **6 topics = 100% LE31-relevant topic-overlap score of the 82-pass series**): `devops, fastapi, htmx, incident-management, incident-response, on-call`. Bucket: **v2 owner-pains** (parking-lot, vocabulary reference only). Build verdict: `defer`.

## Goal

Retain the **one-click-declaration + configurable-lifecycle + timeline + auto-generated-postmortems + self-hosted + FastAPI + HTMX** vocabulary as a persistent cross-section reference for the LE31 *operator-fire-mode* dimension, documenting the primitive an independent maintainer shipped in 2026 on the exact LE31 v1 backend stack. The artifact is a vocabulary reference + a demand signal for a future LE31 v2 owner-pains *incident-declaration* surface. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **one-click-declaration + configurable-lifecycle + timeline + auto-generated-postmortems** 4-tuple-primitive: declaring an operational incident is a single click, the incident then walks a *configurable* (not hard-coded) lifecycle, a timeline records every transition, and a postmortem review document is auto-generated afterwards. **The transferable primitive is *operator-fire-mode-as-first-class-state*:** when something goes wrong on the floor, the operator must be able to declare it in one action and everything after that is a recorded, replayable lifecycle.
- A written record of the **Apache-2.0 + Python + FastAPI + HTMX + self-hosted** stack-shape: this is the **first `incident-management` + `on-call` + `incident-response` vocabulary on the exact LE31 v1 stack (Python 3.13 + FastAPI + HTMX) of the 82-pass series**; the *self-hosted + docker* posture IS the charter §3.5 *self-hosted + on-premise-deployment* invariant applied to the *operator-utility* dimension.
- A written record of the *deterministic lifecycle* posture: `configurable lifecycle` means the state machine is data-driven (a config file, not code branches) — this is the charter §3.4 *deterministic kernel + explicit state transitions* invariant applied to the *incident-state* dimension. Sister-shape to features 108 (telegram-chat-history), 121 (ledger-commitment-field-tier), 122 (trace-integrity), 129 (ledger-claim-to-evidence) — the *explicit-lifecycle-as-config* posture is new; the others are *commitment/tier/trace* postures.
- A decision record: today's verdict is `defer` because (1) LE31 v1 has no incident-management surface and charter §3.5 scopes a *single restaurant*, not an on-call rotation; (2) the *demand-signal* (an independent maintainer shipped this on-stack in 2026) is the value, not the code-adoption opportunity; (3) no owner has raised "I need to file an incident" in 82 passes.

**Out of scope:**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any on-call rotation, escalation, paging, or notification-routing feature.
- Any auto-generated postmortem-document generator in LE31 v1.
- Adoption of the incident-commander codebase (Apache-2.0 permits it, but the domain is wrong — see Scope).

## Out of scope

- See the explicit out-of-scope list above. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v2 owner-pains surface proposes *"a one-click incident declaration with a configurable lifecycle, a replayable timeline, and an auto-generated postmortem, on the existing waiter-HTMX / cook-Telegram surfaces"*, the owner wants *a primitive that proves this shape is buildable on the exact LE31 stack in 2026*, but struggles because *LE31 has no documented incident-management surface and no owner has ever asked for one*, so that *the v2 surface can be defended with "an independent Apache-2.0 maintainer shipped exactly this on FastAPI + HTMX + Python + self-hosted in 2026"*.

- **Evidence class**: **observed** (the verbatim description names `one-click declaration`, `configurable lifecycle & timeline`, `postmortems (auto-generated post-incident review)`, `self-hosted`; the 6 topics confirm `incident-management`, `incident-response`, `on-call`, `devops`, `fastapi`, `htmx`).
- **Confidence**: **medium-high** for the vocabulary match (verbatim description + 6/6 relevant topics + full LE31 backend-stack match); **low** for present urgency (zero owner mentions in 82 passes).
- **Real observed LE31 JTBD**: **zero direct JTBD today.** The value is the vocabulary: when the first v2 owner-fire-mode surface is proposed, this is a ready-made *named primitive*.

## Description

GitHub `giammbo/incident-commander` (Apache-2.0 ✓ §3.2, ★5/⑂1, 1558 KB modest, Python ✓ ON-STACK + FastAPI ✓ ON-STACK + HTMX ✓ ON-STACK + devops + on-call + incident-management + incident-response, pushed 2026-10-20T13:19:22Z, created 2026-04-30T03:14:02Z, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-21): *"Open-source, self-hosted incident management: one-click declaration, configurable lifecycle & timeline, postmortems (auto-generated post-incident review)."*

The architectural primitive has sub-primitives that map 1:1 onto LE31's operational surface:

1. **One-click declaration** — declaring an incident is a single action, not a form. This IS the canonical §3.1 *hands-busy phone-first* invariant applied to the *operator-fire-mode* dimension: a waiter with covered hands must be able to declare "86 on the lamb" in one action.
2. **Configurable lifecycle** — the incident walks a lifecycle whose stages are *data-driven*, not code branches. This IS the canonical §3.4 *deterministic kernel + explicit state transition* invariant applied to the *incident-state* dimension (charter §3.1's "state: operational transitions are explicit user actions").
3. **Timeline** — every lifecycle transition is recorded with a timestamp. This IS the canonical §3.3 *append-only audit chain* invariant applied to the *incident-lifecycle* dimension; the timeline is a read projection over the append-only transition events.
4. **Auto-generated postmortems** — the review document is generated from the recorded timeline rather than written by hand. This IS the canonical §3.3 *current-state-is-derived-from-entries* invariant applied to the *postmortem-document* dimension — the document is a projection, not a source of truth.
5. **Self-hosted** — the system runs on-premise. This IS the canonical §3.5 *single-restaurant + self-hosted + on-premise-deployment* invariant.
6. **FastAPI + HTMX** — the full LE31 v1 backend + waiter-UI stack, no SPA, no build step. This IS the canonical §3.1 *fixed stack* invariant, verified on-stack for the first time in the 82-pass series for an incident-management-class utility.

The defer artifact retains the **6-tuple-primitive** (one-click-declaration + configurable-lifecycle + timeline + auto-generated-postmortems + self-hosted + FastAPI/HTMX-on-stack) as a persistent cross-section reference.

## Data model

N/A (defer artifact; vocabulary-only; no schema today).

When the first v2 owner-fire-mode PR adopts this discipline, the shape is:

```sql
-- An incident is a first-class, explicitly-declared operational state (charter §3.1).
CREATE TABLE incident (
    id BIGSERIAL PRIMARY KEY,
    declared_by TEXT NOT NULL,        -- actor_user_id / 'cook-bot' / 'waiter-web'
    declared_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    declared_surface TEXT NOT NULL,   -- 'cook-bot' / 'waiter-web'
    one_click_reason TEXT NOT NULL,   -- the single-action reason, e.g. '86 on lamb'
    lifecycle_config_key TEXT NOT NULL, -- FK to the DATA-DRIVEN lifecycle definition
    current_stage TEXT NOT NULL       -- current lifecycle stage (explicit, never silent)
);

-- Every lifecycle transition is an APPEND-ONLY event (charter §3.1: never update/delete).
CREATE TABLE incident_transition (
    id BIGSERIAL PRIMARY KEY,
    incident_id BIGINT NOT NULL REFERENCES incident(id),
    from_stage TEXT,
    to_stage TEXT NOT NULL,
    actor TEXT NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- The timeline is a DERIVED VIEW over the append-only transitions
-- (charter §3.1: current stock/state is derived from entries, never stored).
CREATE VIEW incident_timeline AS
    SELECT incident_id, from_stage, to_stage, actor, occurred_at
    FROM incident_transition
    ORDER BY occurred_at ASC;

-- The postmortem is a DERIVED DOCUMENT over the timeline (never hand-written source of truth).
CREATE VIEW incident_postmortem AS
    SELECT
        i.id AS incident_id,
        i.declared_at,
        i.one_click_reason,
        COUNT(t.id) AS transition_count,
        MIN(t.occurred_at) AS first_transition_at,
        MAX(t.occurred_at) AS last_transition_at,
        i.current_stage AS final_stage
    FROM incident i
    LEFT JOIN incident_transition t ON t.incident_id = i.id
    GROUP BY i.id, i.declared_at, i.one_click_reason, i.current_stage;
```

**Stock impact**: none. **Money impact**: none. **§3.1 invariants preserved**: `incident_transition` is append-only (never updated, never deleted); `incident_timeline` and `incident_postmortem` are views, not tables.

## Implementation steps

**None today.** The defer artifact is documentation only.

When the first v2 owner-fire-mode PR adopts this discipline:

1. Add `Incident` SQLModel table with `lifecycle_config_key` (data-driven lifecycle, no code branches).
2. Add `IncidentTransition` SQLModel table (append-only; no `update()`/`delete()` paths anywhere).
3. Add `incident_timeline` + `incident_postmortem` SQL views (derived; never persisted).
4. Add `/api/incidents` (POST one-click declaration) + `/api/incidents/{id}/transitions` (POST explicit stage change) FastAPI endpoints.
5. Add `incident.html` minimal-HTML/HTMX template (one-click declaration button + timeline view + postmortem export).
6. Add cook-bot aiogram v3 `/incident <reason>` one-click declaration handler (operator-fire-mode; hands-busy).
7. Add unit + integration tests asserting the append-only invariant (transition rows cannot be updated or deleted).

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

When the first v2 owner-fire-mode PR adopts this discipline, the cook-bot (aiogram v3) interaction would be:

- `/incident <reason>` — cook declares an incident in one action (hands-busy; §3.1 phone-first).
- The bot replies with the current lifecycle stage + a `/stage <name>` command to advance explicitly (§3.1: operational transitions are explicit user actions; no silent transitions).
- `/timeline` — bot renders the derived timeline view for the current incident.

**§3.4 note**: the cook bot is operator-facing, never customer-facing — no AI is involved in this surface at all; the declaration is a plain command, deterministic, no inference.

## Dependencies

- Python 3.13, FastAPI, SQLModel, Postgres (production) — all already LE31 v1 stack.
- aiogram v3 for the cook-bot handler.
- HTMX for the waiter-web surface.
- **Zero new pip dependencies** for the v1-shaped version. (The upstream repo's own dependency set was not inspected; the LE31 version is designed from the primitive, not from the code.)

## Open questions

- **Does the LE31 charter ever want an incident surface?** Today no — charter §3.5 scopes a single restaurant, and an *on-call* posture is a multi-tenant concept. **Decision pending.**
- **What is the LE31 v1 stance on auto-generated review documents?** The *derived-postmortem* posture (a view, not a hand-written document) maps cleanly onto §3.1's derived-state discipline, but the *content* of a postmortem for a single restaurant with two roles is unclear. **Decision pending.**
- **Who declares an incident?** The cook, the waiter, or the owner? The *one-click* posture implies it must be the person closest to the problem (the cook or waiter), which means the waiter-web and cook-bot surfaces both need a declaration affordance. **Decision pending.**

## Why this matters

This is the **first `incident-management` vocabulary on the exact LE31 v1 backend stack (Python + FastAPI + HTMX) of the 82-pass series**, and the **first 6/6-topic LE31-relevant topic-overlap score from an operator-utility-class repo in the 82-pass series**. The *one-click-declaration + configurable-lifecycle + timeline + auto-generated-postmortem* quadruple-primitive is directly portable to LE31's §3.1 explicit-state and §3.3 append-only-audit invariants, and the *timeline-is-a-view + postmortem-is-a-view* pairing is a clean illustration of "derived, never persisted" applied to a non-stock domain.

The reason it is filed at `defer` rather than promoted: **no owner has asked for it in 82 passes**, and LE31's charter §3.5 scopes a single restaurant rather than an on-call rotation. The value is that when an owner-fire-mode surface is finally proposed, this is a named, on-stack, permissively-licensed reference that has already been proven buildable — rather than a design argument starting from scratch.

Fully reversible: vocabulary-only artifact; deletion has zero runtime impact.