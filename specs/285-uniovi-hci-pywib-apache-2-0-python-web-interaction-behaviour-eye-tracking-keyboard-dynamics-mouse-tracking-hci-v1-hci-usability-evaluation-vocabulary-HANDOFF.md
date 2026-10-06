# Handoff — Feature 285 — v1 HCI-usability-evaluation-vocabulary (defer)

> **Pick:** `uniovi-hci/pywib` — v1 cross-section reference for **Pywib-Python-Web-Interaction-Behaviour-library-for-analysing-metrics-from-users-interaction-with-web-pages + eye-tracking + hci + human-computer-interaction + keyboard-dynamics + mouse-tracking** primitive.
> **Status:** `defer (parking-lot, vocabulary reference)` — zero build time today; the artifact is vocabulary-only and persists as a future-cast reference for any future LE31 v1 surface that adopts the *Pywib + Python-Web-Interaction-Behaviour + eye-tracking + keyboard-dynamics + mouse-tracking* primitives.
> **Source:** Daily Brainstorm 2026-10-06 (68th consecutive daily-brainstorm pass) → Pick B.
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/285-uniovi-hci-pywib-apache-2-0-python-web-interaction-behaviour-eye-tracking-keyboard-dynamics-mouse-tracking-hci-v1-hci-usability-evaluation-vocabulary.md`
> **Raw fetches:** `/tmp/le31-brainstorm-2026-10-06/verify_uniovi-hci_pywib.json` (parent-verified direct GitHub API GET, raw JSON)

---

## Seven-check gate verdict (LE31 charter §3.1 + §3.2 + §3.4)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✓ justified as a NEW pain | When the LE31 owner wants to know how the waiter uses the waiter-web-UI (which buttons they click, which menus they spend time on, where their eyes linger, how their keyboard dynamics reveal hesitation), the owner wants a *Pywib + eye-tracking + keyboard-dynamics + mouse-tracking* telemetry surface, but struggles because the existing waiter-web-UI has *no web-page-telemetry + no eye-tracking + no keyboard-dynamics + no mouse-tracking*, so the v1 surface-extension needs a *Pywib + Python-Web-Interaction-Behaviour + eye-tracking + keyboard-dynamics + mouse-tracking* discipline. **v1 expansion → NEW pain** |
| 2 | Viability | ✓ viable | Non-technical owner CAN understand (the *Pywib + eye-tracking + keyboard-dynamics + mouse-tracking* primitive is operator-readable); CAN recover (the *web-page-telemetry + audit_logs* discipline is recoverable via Postgres backup); CAN maintain (the *Pywib + Python-Web-Interaction-Behaviour + eye-tracking + keyboard-dynamics + mouse-tracking* surface is documentation-only at v1; v1 surface would require FastAPI + SQLModel + Postgres + JavaScript-snippet + WebSocket expertise). **§3.1 owner-readable profile** |
| 3 | Strategic fit | ✓ aligned | Cross-section with feature 256 (jblattgerste/sus-analysis-toolkit MIT web-based-analysis-toolkit-system-usability-scale-calculation-plotting-interpretation-contextualised-reports-v1-hci-usability-evaluation-vocabulary-reference = *System-Usability-Scale-calculation-plotting-interpretation + contextualised-reports* quadruple-primitive) + 268 (escarletdesign/ux-laws-auditor MIT Cursor-Agent-Skill UX-auditor 20-HCI-psychology-laws-hick-fitts-jakob-miller-peak-end-v1-hci-usability-audit-vocabulary = *Cursor-Agent-Skill + UX-audit + 20-HCI-psychology-laws (Hick + Fitts + Jakob + Miller + Peak-end) + agent-skills + cursor-skills + hci + usability + ux* nonuple-primitive). The *Pywib + Python-Web-Interaction-Behaviour + eye-tracking + keyboard-dynamics + mouse-tracking* posture IS the canonical **v1 HCI-usability-evaluation-vocabulary** |
| 4 | Charter conflict | ✓ none hard | §3.1 STRICTLY-COMPATIBLE (Python + minimal-HTML posture; the *Pywib + Python-Web-Interaction-Behaviour + eye-tracking + keyboard-dynamics + mouse-tracking* posture IS the §3.1 *single-restaurant + single-owner + on-premise-deployment + HCI-research-grounded* invariant applied to the *waiter-web-UI-telemetry* dimension); §3.2 STRICTLY-COMPATIBLE (Apache-2.0 permissive + 3★/0⑨ community traction start); §3.4 NOT TRIGGERED (the *HCI-research-library* surface is operator-tooling + observable-evidence per charter §3.4 invariant; the *eye-tracking + keyboard-dynamics + mouse-tracking* primitives are deterministic telemetry primitives, not customer-facing AI; any future v1 surface adopting the *web-page-telemetry* vocabulary that exposes customer-facing eye-tracking requires explicit §3.4 review for privacy); §3.7 RIPGL_REVIEW REQUIRED (eye-tracking is borderline §3.7 privacy if the *waiter-eye-tracking* surface captures the waiter's gaze on a *customer-facing* page; the *waiter-web-UI* is operator-tooling, not customer-facing, so §3.7 is NOT triggered for the operator-side use; the §3.7 review is required only if the *web-page-telemetry* surface is extended to a *customer-facing* page). **No hard conflict** |
| 5 | Outcome, appetite, scope | ✓ alignable | v1 outcome (HCI-usability-evaluation-vocabulary). Max time worth spending = 0 minutes today (defer artifact); future v1 PR = 1-2 weeks for design + 2-3 weeks for *Pywib + eye-tracking + keyboard-dynamics + mouse-tracking* surface + 1 week for verification = 1-2 months total |
| 6 | Cost to operational value | ✓ marginal | Pain frequency = low (LE31 v1 has no v1 HCI-usability-evaluation surface today; no owner has asked for v1 HCI-usability-evaluation); money vocabulary = minimal; implementation cost = 1-2 months v1 PR. **MARGINAL VALUE at v1** |
| 7 | Circuit breaker and reversibility | ✓ reversible | Stop evidence = explicit owner/charter rejection of *Pywib + eye-tracking + keyboard-dynamics + mouse-tracking* adoption; review point = first v1 PR that proposes *Pywib + eye-tracking + keyboard-dynamics + mouse-tracking* surface; migration/rollback = trivial (vocabulary-only artifact, zero code shipped); retained data = N/A |

**Final decision: `defer (parking-lot, vocabulary reference)`.**

## Files to touch (future v1 PR trigger)

If a future v1 PR is triggered by the trigger condition below, the implementation would touch:

| File | Purpose | Notes |
|---|---|---|
| `app/models/web_page_telemetry.py` (NEW) | `WebPageTelemetry` SQLModel table | `telemetry_id, telemetry_kind, telemetry_payload_json, telemetry_at, telemetry_owner_id, telemetry_page_url` |
| `app/models/eye_tracking_event.py` (NEW) | `EyeTrackingEvent` SQLModel table | `event_id, event_kind, event_x, event_y, event_at, event_page_url` for *eye-tracking* discipline |
| `app/models/keyboard_dynamics_event.py` (NEW) | `KeyboardDynamicsEvent` SQLModel table | `event_id, event_key, event_press_at, event_release_at, event_page_url` for *keyboard-dynamics* discipline |
| `app/models/mouse_tracking_event.py` (NEW) | `MouseTrackingEvent` SQLModel table | `event_id, event_kind, event_x, event_y, event_at, event_page_url` for *mouse-tracking* discipline |
| `app/models/pywib_metric.py` (NEW) | `PywibMetric` SQLModel table | `metric_id, metric_kind, metric_value, metric_at, metric_page_url, metric_user_id` for *Pywib* discipline |
| `app/api/web_page_telemetry.py` (NEW) | FastAPI route + endpoint | `/api/web-page-telemetry` (POST create, GET list, GET show) |
| `app/templates/web_page_telemetry.html` (NEW) | minimal-HTML/HTMX template | owner-facing surface for web-page-telemetry with Pywib + eye-tracking + keyboard-dynamics + mouse-tracking |
| `app/static/js/web-page-telemetry-snippet.js` (NEW) | minimal JavaScript snippet | Pywib client-side JavaScript that captures eye-tracking + keyboard-dynamics + mouse-tracking events |
| `migrations/versions/<hash>_add_web_page_telemetry_tables.py` (NEW) | alembic migration | creates `web_page_telemetry + eye_tracking_event + keyboard_dynamics_event + mouse_tracking_event + pywib_metric` tables |
| `tests/test_web_page_telemetry_api.py` (NEW) | pytest coverage | covers WebPageTelemetry CRUD + Pywib + eye-tracking + keyboard-dynamics + mouse-tracking |

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md` + `development` skill, the future v1 PR would:
1. Run `pytest tests/test_web_page_telemetry_api.py -v` to confirm all tests pass.
2. Run `alembic upgrade head` to confirm migrations apply cleanly.
3. Run `python -c "from app.models.web_page_telemetry import WebPageTelemetry; print(WebPageTelemetry.__tablename__)"` to confirm SQLModel loads.
4. Manually verify via `curl http://localhost:8000/api/web-page-telemetry/status` that the FastAPI endpoint returns 200 with the expected schema.
5. Manually verify via the waiter-web-UI that the *Pywib + eye-tracking + keyboard-dynamics + mouse-tracking* discipline works end-to-end (load waiter-web-UI → verify JavaScript-snippet loads → click + move mouse → verify mouse-tracking event recorded → type on keyboard → verify keyboard-dynamics event recorded).
6. Run `mypy app/` + `ruff check app/` to confirm static analysis passes.
7. Confirm feature is in `Backlog` status + parent (this brainstorm parent) is in `Done` status in Linear.

## Rollback path

The defer artifact is vocabulary-only, zero code shipped, so no rollback is needed today. If a future v1 PR ships and the *Pywib + Python-Web-Interaction-Behaviour + eye-tracking + keyboard-dynamics + mouse-tracking* discipline is rejected by the owner/charter:
1. Run `alembic downgrade -1` to drop the `web_page_telemetry + eye_tracking_event + keyboard_dynamics_event + mouse_tracking_event + pywib_metric` tables.
2. Delete `app/models/web_page_telemetry.py` + `app/models/eye_tracking_event.py` + `app/models/keyboard_dynamics_event.py` + `app/models/mouse_tracking_event.py` + `app/models/pywib_metric.py` + `app/api/web_page_telemetry.py` + `app/templates/web_page_telemetry.html` + `app/static/js/web-page-telemetry-snippet.js` + the alembic migration + the pytest files.
3. Re-run `alembic upgrade head` to confirm clean state.
4. Re-run `pytest -v` to confirm no regressions.

## Mandatory LE31 skill list

The future v1 PR author MUST load + apply these skills before any code is written:

| Skill | Why |
|---|---|
| `le31-conventions` | Repository-wide Python + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX conventions |
| `le31-v1-feature-pattern` | Existing v1 feature pattern (table management, cook-channel, stock-ledger) |
| `le31-handoff-spec` | Slice handoff format |
| `le31-coding-agent-brief` | Paste-in prompt generation from this slice contract |
| `systematic-debugging` | 4-phase root cause debugging if any test fails |
| `verify-before-fixing` | Verify diagnostic / CI / delegated subagent before fixing |
| `pre-merge-review` | Independent non-author review before merging |

## Bucket

**v1** (attached to `le31 Research` P-HMM-1 per the verified workspace project list of 2026-10-06; the `le31 v1 — Core MVP` P-HMM-3 exists but per `le31-feature-pipeline/SKILL.md` line 33, the v1-bucket pick is attached to `le31 Research` as the parent of the sub-issue; the v1 surface-extension for web-page-telemetry is a vocabulary-only artifact, not a v1 build trigger).

## Trigger condition

First v1 PR that adds a `web_page_telemetry` SQLModel table + a `WebPageTelemetry` event table + a `/api/web-page-telemetry` FastAPI endpoint + a `web-page-telemetry.html` minimal-HTML/HTMX template with Pywib + eye-tracking + keyboard-dynamics + mouse-tracking; OR first v1 PR that adopts the *Pywib + Python-Web-Interaction-Behaviour + eye-tracking + keyboard-dynamics + mouse-tracking* discipline on the existing waiter-web-UI.

## Charter compatibility

§3.1 + §3.2 STRICTLY-COMPATIBLE; §3.4 NOT TRIGGERED (the *HCI-research-library* surface is operator-tooling + observable-evidence per charter §3.4 invariant; the *eye-tracking + keyboard-dynamics + mouse-tracking* primitives are deterministic telemetry primitives, not customer-facing AI); §3.7 RIPGL_REVIEW REQUIRED (eye-tracking is borderline §3.7 privacy if the *waiter-eye-tracking* surface captures the waiter's gaze on a *customer-facing* page; the *waiter-web-UI* is operator-tooling, not customer-facing, so §3.7 is NOT triggered for the operator-side use; the §3.7 review is required only if the *web-page-telemetry* surface is extended to a *customer-facing* page).

## Companion artifacts

- Feature file: `/opt/data/le31_mmm3_research_work/features/285-uniovi-hci-pywib-apache-2-0-python-web-interaction-behaviour-eye-tracking-keyboard-dynamics-mouse-tracking-hci-v1-hci-usability-evaluation-vocabulary.md`
- Spec file: `/opt/data/le31_mmm3_research_work/specs/285-uniovi-hci-pywib-apache-2-0-python-web-interaction-behaviour-eye-tracking-keyboard-dynamics-mouse-tracking-hci-v1-hci-usability-evaluation-vocabulary-HANDOFF.md`
- Linear sub-issue: BLOCKED (workspace plan-limit error: *"You've exceeded the free issue limit for this workspace"* — **17th consecutive day**; verified today via 1 write-probe with requestId TBD; parent fallback at `/opt/data/le31-brainstorm-2026-10-06.linear-fallback.json`)
- Report: `/opt/data/le31-brainstorm-2026-10-06.md`
- Raw fetches: `/tmp/le31-brainstorm-2026-10-06/verify_uniovi-hci_pywib.json` (parent-verified direct GitHub API GET, raw JSON)
