# Pick C — `Mfrostbutter/ageniusdesk-ce` — v2 owner-pains operator-console-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/274-Mfrostbutter-ageniusdesk-ce-mit-fastapi-control-plane-dashboard-observability-mcp-self-hosted-workflow-automation-v2-owner-pains-operator-console-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2 PR that adds a `MultiInstanceOperatorConsole` SQLModel table (`instance_id, instance_url, instance_status, last_healthcheck_at`).
2. First v2 PR that adds a `MultiInstanceOperatorService` Python service (`register_instance, deregister_instance, list_instances, get_instance_status`).
3. First v2 PR that adds a `MultiInstanceOperatorDashboard` Python service (`dashboard_summary, dashboard_alerts, dashboard_metrics`).
4. First v2 PR that adds an `/api/multi-instance/console` + `/api/multi-instance/<instance_id>` + `/api/multi-instance/<instance_id>/status` + `/api/multi-instance/<instance_id>/register` + `/api/multi-instance/<instance_id>/deregister` FastAPI endpoint set.
5. First v2 PR that adds a `multi_instance_console.html` minimal-HTML/HTMX template that renders *multi-instance-management + observability + control-plane + dashboard + ai-assisted-debugging + one-click-container-deployment*.
6. First v2 PR that adopts a *production-grade-observability* posture on the existing owner-dashboard (i.e., the existing FastAPI logging + aiogram logging + Postgres logging is replaced with a *production-grade-observability* stack like Prometheus + Grafana + OpenTelemetry).
7. First v2 PR that adopts an *ai-assisted-debugging-as-operator-tooling* posture on the existing operator-tooling surface (i.e., a v2 surface that uses Anthropic + OpenAI + Ollama + LLM for *ai-assisted-debugging* with explicit charter §3.4 review).

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v2 surface wants to add a **multi-instance-management + observability + control-plane + dashboard + ai-assisted-debugging + one-click-container-deployment** surface to the existing owner-dashboard + Hermes-driven agent pipeline (e.g., a v2 surface that lets the operator inspect multiple LE31 instances from a single owner-console with production-grade-observability + control-plane + ai-assisted-debugging + one-click-container-deployment), the operator wants a known-good FastAPI + control-plane + dashboard + observability + mcp + self-hosted + workflow-automation + error-tracking + ai-assisted-debugging + multi-instance-management + one-click-container-deployment blueprint, but LE31 today has a *single-restaurant* + *minimal-observability* + *no-control-plane* + *no-ai-assisted-debugging* + *no-one-click-container-deployment* owner-console surface, so that any future v2 extension has a documented reference."* — PASS (links to features 197 + 203 + 254 + 263 + 264; justifies a new v2 pain).
2. **Viability** — Operator does not need to understand the implementation; they only see the *multi-instance-management + observability + control-plane + dashboard + ai-assisted-debugging + one-click-container-deployment* surface on the existing minimal-HTML/HTMX owner-dashboard. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 RIPGL_REVIEW REQUIRED if any customer-facing surface is added (the *ai-assisted-debugging* surface is operator-tooling per charter §3.4 invariant; the *mcp + llm + anthropic + openai + ollama* posture IS the *operator-tooling + observable-evidence + non-AI-fallback* charter §3.4 invariant applied to the *multi-instance-console* dimension); confidence **high** for vocabulary transferability, **low** for immediate LE31 v2 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling + observable-evidence + non-AI-surface; §3.1 explicit-state-transitions preserved; the *n8n* cluster-context is OFF-domain for LE31 v1 today which uses aiogram-Telegram-bot instead of n8n. PASS.
5. **Outcome, appetite, and scope** — **v2 owner-pains** outcome (cross-section to features 197 + 203 + 254 + 263 + 264). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = high (~500-1000 lines of Python + SQLModel + FastAPI + Prometheus + Grafana + OpenTelemetry + optional-Anthropic-API + optional-Ollama-API + Docker + docker-compose code; 20-40 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/multi_instance_operator_console.py` (new) — `MultiInstanceOperatorConsole` SQLModel table
- `le31/app/services/multi_instance_operator.py` (new) — `MultiInstanceOperatorService` + `MultiInstanceOperatorDashboard` Python services
- `le31/app/services/multi_instance_observability.py` (new) — production-grade-observability service (Prometheus + Grafana + OpenTelemetry integration)
- `le31/app/services/multi_instance_ai_assisted_debugging.py` (new) — ai-assisted-debugging service with explicit charter §3.4 review (Anthropic + OpenAI + Ollama + LLM integration; **NO customer-facing AI per charter §3.4**; **operator-tooling + observable-evidence + non-AI-fallback** posture)
- `le31/app/services/multi_instance_container_deployment.py` (new) — one-click-container-deployment service (Docker + docker-compose integration)
- `le31/app/api/v1/multi_instance_operator.py` (new) — HTTP endpoints: `GET /api/multi-instance/console` + `GET /api/multi-instance/<instance_id>` + `GET /api/multi-instance/<instance_id>/status` + `POST /api/multi-instance/<instance_id>/register` + `POST /api/multi-instance/<instance_id>/deregister`
- `le31/app/owner_dashboard/templates/multi_instance_console.html` (new) — minimal-HTML/HTMX owner-dashboard template for multi-instance-console
- `le31/migrations/versions/<revision>_multi_instance_operator.py` (new) — Alembic migration for the new table
- `le31/app/observability/prometheus.yml` (new) — Prometheus configuration
- `le31/app/observability/grafana_dashboard.json` (new) — Grafana dashboard configuration

## Verification protocol reference

- Run `pytest le31/tests/test_multi_instance_operator.py -v` to verify the new table + endpoints + minimal-HTML/HTMX template
- Run `pytest le31/tests/test_multi_instance_observability.py -v` to verify the production-grade-observability surface
- Run `pytest le31/tests/test_multi_instance_ai_assisted_debugging.py -v` to verify the ai-assisted-debugging surface (operator-tooling + observable-evidence + non-AI-fallback posture)
- Run `pytest le31/tests/test_multi_instance_container_deployment.py -v` to verify the one-click-container-deployment surface
- Run `pytest le31/tests/test_charter_3_4_no_customer_facing_ai.py -v` to verify §3.4 no-customer-facing-AI invariant (the *ai-assisted-debugging* surface is operator-tooling only; **NO customer-facing AI**)
- Run `pytest le31/tests/test_charter_3_6_money_primitive.py -v` to verify §3.6 money-primitive invariant (the *multi-instance-console* is NOT a money-primitive)

## Rollback path

- Revert the SQLModel migration: `alembic downgrade -1`
- Delete the new files (`le31/app/models/multi_instance_operator_console.py` + `le31/app/services/multi_instance_operator.py` + `le31/app/services/multi_instance_observability.py` + `le31/app/services/multi_instance_ai_assisted_debugging.py` + `le31/app/services/multi_instance_container_deployment.py` + `le31/app/api/v1/multi_instance_operator.py` + `le31/app/owner_dashboard/templates/multi_instance_console.html` + `le31/migrations/versions/<revision>_multi_instance_operator.py` + `le31/app/observability/prometheus.yml` + `le31/app/observability/grafana_dashboard.json`)
- Stop the Prometheus + Grafana services
- Restart the FastAPI server

## Mandatory LE31 skill list

- `le31-conventions` (charter §3.1 + §3.2 + §3.3 + §3.4 + §3.6 + §3.7 invariants; seven-check feature gate)
- `le31-feature-pipeline` (vocabulary-to-build pipeline + parking-lot-vs-build decision)
- `le31-v1-feature-pattern` (existing v1 feature patterns + Hermes-Plugin architecture)
- `le31-data` (existing audit_logs + sqlmodel-extensions patterns)
- `le31-cook-bot-ux` (existing cook-Telegram-bot surface; the *multi-instance-console* is a separate HTTP surface, NOT a Telegram surface)
- `le31-quality-gates` (existing quality-gates + production-grade-observability patterns)