# Handoff — Feature 279 — v1 small-business-protocol-vocabulary (defer)

> **Pick:** `Melvinanalytics/impacts-protokoll` — v1 cross-section reference for **file-based-protocol-for-SMEs + understand-work + simplify-processes + use-AI-and-data-science + business-process-management + knowledge-management + markdown + workflow-automation** primitive.
> **Status:** `defer (parking-lot, vocabulary reference)` — zero build time today; the artifact is vocabulary-only and persists as a future-cast reference for any future LE31 v1 surface that adopts the *file-based-protocol-for-SMEs + markdown + business-process-management + workflow-automation* primitives.
> **Source:** Daily Brainstorm 2026-10-05 (67th consecutive daily-brainstorm pass) → Pick B.
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/279-Melvinanalytics-impacts-protokoll-apache-2-0-file-based-protocol-smes-understand-work-simplify-processes-ai-data-science-v1-small-business-protocol-vocabulary.md`
> **Raw fetches:** `/tmp/le31-brainstorm-2026-10-05/verify_final_Melvinanalytics_impacts-protokoll.json` (parent-verified direct GitHub API GET, raw JSON, 8.2 KB)

---

## Seven-check gate verdict (LE31 charter §3.1 + §3.2 + §3.4)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✓ justified as a NEW pain | When a non-technical SME-owner wants to onboard to LE31's existing *waiter web UI + cook Telegram bot + owner daily-recap* without learning Python + FastAPI + SQLModel + Postgres, the owner wants a file-based-protocol-for-SMEs + markdown + business-process-management + workflow-automation surface, but struggles because the existing owner-dashboard is empty for non-technical SME-owners, so that the v1 surface-extension needs a *file-based-protocol-for-SMEs + markdown + business-process-management* discipline that adopts the *file-based-protocol + markdown-onboarding + business-process-management* primitives. **v1 expansion → NEW pain** |
| 2 | Viability | ✓ viable | Non-technical owner CAN understand (the *file-based-protocol-for-SMEs + markdown* primitive is operator-readable; the *understand-work + simplify-processes* posture IS the *owner-facing-clarity* charter §3.1 invariant); CAN recover (the *file-based-protocol + markdown + business-process-management* discipline is recoverable via Git); CAN maintain (the *file-based-protocol-for-SMEs + markdown + business-process-management* surface is documentation-only at v1; v1 surface would require FastAPI + SQLModel + Postgres expertise). **§3.1 owner-readable profile** |
| 3 | Strategic fit | ✓ aligned | Cross-section with feature 270 (Prism-Infoways/Tungsten MIT fastapi-admin-panel-filament-style-sqlmodel-sqlalchemy-jinja2-htmx-alpinejs v1 admin-panel-vocabulary-reference) + the daily-research 09-26 Pick C `violentzone/CarzinomaxERP` Apache-2.0 open-source-erp-fastapi-react-ai-data-entry-small-business-v1-small-business-ai-erp-vocabulary-reference. The *file-based-protocol-for-SMEs + markdown + business-process-management + workflow-automation* posture IS the canonical **v1 small-business-protocol-vocabulary** |
| 4 | Charter conflict | ✓ none hard | §3.1 STRICTLY-COMPATIBLE (Python + minimal-HTML posture; the *markdown-as-onboarding-format* posture IS the §3.1 *non-technical-SME-owner-readable* invariant applied to the *SME-protocol* dimension); §3.2 STRICTLY-COMPATIBLE (Apache-2.0 permissive + 0★/0⑨ community traction start); §3.4 NOT TRIGGERED (the *use-AI-and-data-science* posture is operator-server-calls, not customer-facing AI; the *file-based-protocol* surface is operator-tooling per charter §3.4 invariant); §3.7 N/A (no privacy primitive change). **No hard conflict** |
| 5 | Outcome, appetite, scope | ✓ alignable | v1 outcome (small-business-protocol-vocabulary). Max time worth spending = 0 minutes today (defer artifact); future v1 PR = 1-2 weeks for design + 2-3 weeks for *file-based-protocol-for-SMEs + markdown + business-process-management + workflow-automation* surface + 1 week for verification = 1-2 months total |
| 6 | Cost to operational value | ✓ marginal | Pain frequency = low (LE31 v1 has no v1 SME-protocol-onboarding surface today; no operator has asked for v1 SME-protocol-onboarding); money vocabulary = minimal; implementation cost = 1-2 months v1 PR. **MARGINAL VALUE at v1** |
| 7 | Circuit breaker and reversibility | ✓ reversible | Stop evidence = explicit owner/charter rejection of *file-based-protocol-for-SMEs + markdown + business-process-management + workflow-automation* adoption; review point = first v1 PR that proposes *file-based-protocol-for-SMEs + markdown + business-process-management + workflow-automation* surface; migration/rollback = trivial (vocabulary-only artifact, zero code shipped); retained data = N/A |

**Final decision: `defer (parking-lot, vocabulary reference)`.**

## Files to touch (future v1 PR trigger)

If a future v1 PR is triggered by the trigger condition below, the implementation would touch:

| File | Purpose | Notes |
|---|---|---|
| `app/models/sme_protocol.py` (NEW) | `SMEProtocol` SQLModel table | `protocol_id, protocol_name, protocol_markdown, protocol_owner_id, protocol_created_at, protocol_updated_at, protocol_status` |
| `app/models/sme_protocol_step.py` (NEW) | `SMEProtocolStep` SQLModel table | `step_id, step_name, step_markdown, step_protocol_id, step_order` for *workflow-automation + business-process-management* discipline |
| `app/models/sme_protocol_ai_data_science.py` (NEW) | `SMEProtocolAIDataScience` SQLModel table | `protocol_id, ai_data_science_payload_json, ai_usage_count, ai_last_used_at` for *use-AI-and-data-science* discipline |
| `app/api/sme_protocol.py` (NEW) | FastAPI route + endpoint | `/api/sme-protocol` (POST create, GET list, GET show, POST understand-work, POST simplify-processes) |
| `app/templates/sme_protocol.html` (NEW) | minimal-HTML/HTMX template | owner-facing surface for SME-protocol-onboarding |
| `app/static/css/sme-protocol.css` (NEW) | minimal CSS for markdown rendering | Optional: only if HTMX markdown rendering proves insufficient |
| `migrations/versions/<hash>_add_sme_protocol_tables.py` (NEW) | alembic migration | creates `sme_protocol + sme_protocol_step + sme_protocol_ai_data_science` tables |
| `tests/test_sme_protocol_api.py` (NEW) | pytest coverage | covers SMEProtocol CRUD + workflow-automation + business-process-management + use-AI-and-data-science |
| `tests/test_sme_protocol_markdown.py` (NEW) | pytest coverage | covers markdown-as-onboarding-format rendering |

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md` + `development` skill, the future v1 PR would:
1. Run `pytest tests/test_sme_protocol_api.py tests/test_sme_protocol_markdown.py -v` to confirm all tests pass.
2. Run `alembic upgrade head` to confirm migrations apply cleanly.
3. Run `python -c "from app.models.sme_protocol import SMEProtocol; print(SMEProtocol.__tablename__)"` to confirm SQLModel loads.
4. Manually verify via `curl http://localhost:8000/api/sme-protocol/status` that the FastAPI endpoint returns 200 with the expected schema.
5. Manually verify via the owner-dashboard that the *file-based-protocol-for-SMEs + markdown + business-process-management + workflow-automation* discipline works end-to-end (create protocol → add step → trigger workflow-automation → render markdown).
6. Run `mypy app/` + `ruff check app/` to confirm static analysis passes.
7. Confirm feature is in `Backlog` status + parent (this brainstorm parent) is in `Done` status in Linear.

## Rollback path

The defer artifact is vocabulary-only, zero code shipped, so no rollback is needed today. If a future v1 PR ships and the *file-based-protocol-for-SMEs + markdown + business-process-management + workflow-automation* discipline is rejected by the owner/charter:
1. Run `alembic downgrade -1` to drop the `sme_protocol + sme_protocol_step + sme_protocol_ai_data_science` tables.
2. Delete `app/models/sme_protocol.py` + `app/models/sme_protocol_step.py` + `app/models/sme_protocol_ai_data_science.py` + `app/api/sme_protocol.py` + `app/templates/sme_protocol.html` + `app/static/css/sme-protocol.css` + the alembic migration + the pytest files.
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

**v1** (attached to `le31 v1 — Core MVP` P-HMM-3 per the verified workspace project list of 2026-10-05; the `le31 v2 owner-pains` and `le31 v2-AI` projects do NOT exist per `le31-feature-pipeline/SKILL.md` line 33).

## Trigger condition

First v1 PR that adds a `sme_protocol` SQLModel table + a `/api/sme-protocol` FastAPI endpoint + a `sme-protocol.html` minimal-HTML/HTMX template; OR first v1 PR that adopts the *file-based-protocol-for-SMEs + understand-work + simplify-processes + use-AI-and-data-science + business-process-management + knowledge-management + markdown + workflow-automation* discipline on the existing owner-dashboard.

## Charter compatibility

§3.1 + §3.2 STRICTLY-COMPATIBLE; §3.4 NOT TRIGGERED (the *use-AI-and-data-science* posture is operator-server-calls, not customer-facing AI).

## Companion artifacts

- Feature file: `/opt/data/le31_mmm3_research_work/features/279-Melvinanalytics-impacts-protokoll-apache-2-0-file-based-protocol-smes-understand-work-simplify-processes-ai-data-science-v1-small-business-protocol-vocabulary.md`
- Spec file: `/opt/data/le31_mmm3_research_work/specs/279-Melvinanalytics-impacts-protokoll-apache-2-0-file-based-protocol-smes-understand-work-simplify-processes-ai-data-science-v1-small-business-protocol-vocabulary-HANDOFF.md`
- Linear sub-issue: BLOCKED (workspace plan-limit error: *\"You've exceeded the free issue limit for this workspace\"* — **16th consecutive day**; verified today via 2 write-probes with requestId `a45aac5e0a9ad368`; parent fallback at `/opt/data/le31-brainstorm-2026-10-05.linear-fallback.json`)
- Report: `/opt/data/le31-brainstorm-2026-10-05.md`
- Raw fetches: `/tmp/le31-brainstorm-2026-10-05/verify_final_Melvinanalytics_impacts-protokoll.json` (parent-verified direct GitHub API GET, raw JSON, 8.2 KB)