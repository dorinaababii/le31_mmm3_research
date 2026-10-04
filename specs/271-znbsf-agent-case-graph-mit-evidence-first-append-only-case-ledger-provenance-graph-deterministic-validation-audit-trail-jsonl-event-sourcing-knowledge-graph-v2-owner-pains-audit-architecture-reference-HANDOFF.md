# Pick C — `znbsf/agent-case-graph` — v2 owner-pains audit-architecture — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/271-znbsf-agent-case-graph-mit-evidence-first-append-only-case-ledger-provenance-graph-deterministic-validation-audit-trail-jsonl-event-sourcing-knowledge-graph-v2-owner-pains-audit-architecture-reference.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2 PR that adds a *case-ledger + provenance-graph + deterministic-validation* surface to the existing `audit_logs` SQLModel table.
2. First v2 PR that introduces a *Case + CaseEvidence + ProvenanceEdge + ValidationRule* SQLModel table set.
3. First v2 PR that adds an `/api/cases` + `/api/cases/<case_id>/evidence` + `/api/cases/<case_id>/provenance` + `/api/cases/<case_id>/validate` FastAPI endpoint set.
4. First v2 PR that adds a `case-ledger.html` + `provenance-graph.html` + `validation-rules.html` minimal-HTML/HTMX template set.
5. First v2 PR that introduces an *auditable-agent-workflow* surface (with charter §3.4 + §3.7 review).
6. First v2 PR that adds an `agent-case-graph` pip dependency to `requirements.txt`.
7. First v2 PR that adds an *accountant-facing-audit-export* surface (the *evidence-first + append-only-case-ledger* IS the §3.7 invariant applied to *accountant-facing-audit-export*).

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v2 surface wants to **extend the existing `audit_logs` SQLModel table with a case-ledger + provenance-graph + deterministic-validation + auditable-agent-workflow discipline** (e.g., a v2 surface that wants to give the owner a self-service audit-export with evidence-first + provenance-graph + deterministic-validation, or a v2 surface that wants to introduce a co-assistant LLM with auditable-agent-workflow discipline), the owner wants a known-good evidence-first+append-only-case-ledger+provenance-graph+deterministic-validation+auditable-agent-workflow-frontiers blueprint, but LE31 today has no case-ledger + no provenance-graph + no deterministic-validation + no auditable-agent-workflow, so that any future v2 extension has a documented reference."* — PASS (links to features 03 + 49 + 81 + 92 + 96 + 97 + 121 + 122 + 126 + 127 + 134 + 137 + 141 + 145 + 154 + 167 + 168 + 169 + 181 + 183 + 187 + 188 + 189 + 190 + 196 + 198 + 203 + 220 + 230 + 232 + 236 + 241 + 257 + 264 + 271; justifies a new pain).
2. **Viability** — Owner + accountant do not need to understand the implementation; they only see the *case-ledger + provenance-graph* outputs on the existing minimal-HTML/HTMX owner-dashboard or accountant-facing-audit-export. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 NOT triggered for customer-facing AI (no customer-facing surface; the *auditable-agent-workflow* is staff-tooling infrastructure, not customer-facing AI; the *deterministic-validation* is a NON-AI primitive); confidence **high** for vocabulary transferability, **low** for immediate LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling + staff-tooling only; §3.1 + §3.3 + §3.4 + §3.7 invariants preserved. PASS.
5. **Outcome, appetite, and scope** — **v2** outcome (cross-section to features 03+49+81+92+96+97+121+122+126+127+134+137+141+145+154+167+168+169+181+183+187+188+189+190+196+198+203+220+230+232+236+241+257+264). Appetite = zero today (parking-lot; v2 surfaces are explicitly parked until v1 is stable per charter §3.1 + §3.2). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = medium (~200-500 lines of SQLModel + FastAPI + agent-case-graph + JSONL code; 5-10 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/case.py` (new) — `Case` + `CaseEvidence` + `ProvenanceEdge` + `ValidationRule` SQLModel tables
- `le31/app/services/case.py` (new) — service layer for `create_case` + `add_evidence` + `link_provenance` + `validate_case` + `export_case_evidence` + `verify_case_ledger`
- `le31/app/hermes/hooks/case_recording.py` (new) — Hermes Agent hook integration that records every case-ledger-action as an immutable row in `audit_logs` (operator-tooling + staff-tooling only; **role-based-access-required per charter §3.7**)
- `le31/app/api/v2/cases.py` (new) — HTTP endpoints: `GET /api/cases` + `POST /api/cases` + `GET /api/cases/<case_id>` + `GET /api/cases/<case_id>/evidence` + `POST /api/cases/<case_id>/evidence` + `GET /api/cases/<case_id>/provenance` + `POST /api/cases/<case_id>/provenance` + `GET /api/cases/<case_id>/validate` + `POST /api/cases/<case_id>/validate` + `GET /api/cases/<case_id>/export` (accountant-facing-audit-export with non-repudiation)
- `le31/app/owner_dashboard/templates/case_ledger.html` (new) — minimal-HTML/HTMX template for case-ledger-view
- `le31/app/owner_dashboard/templates/provenance_graph.html` (new) — minimal-HTML/HTMX template for provenance-graph-view (the *graph-visualization* uses HTML/SVG; no JS toolchain)
- `le31/app/owner_dashboard/templates/validation_rules.html` (new) — minimal-HTML/HTMX template for validation-rules-view
- `le31/migrations/versions/<revision>_case.py` (new) — Alembic migration for the four new tables + the `case_id` + `case_evidence_jsonl_path` + `provenance_graph_id` + `validation_rule_id` columns on `audit_logs`
- `requirements.txt` (modified) — add `agent-case-graph` (the *evidence-first + append-only-case-ledger* IS the *pip-as-deployment* charter §3.1 invariant)
- `skills/le31-conventions/SKILL.md` — append the *evidence-first + append-only-case-ledger + provenance-graph + deterministic-validation + auditable-agent-workflow-frontiers* posture as a §3.1 + §3.3 + §3.4 + §3.7-aligned pattern; **append the §3.4 RIPGL_REVIEW requirement for any future v2-AI surface adopting the *auditable-agent-workflow* vocabulary**

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the four new tables + revert the four new `audit_logs` columns
- **Revert the case service** (remove the `le31/app/services/case.py` file + remove the import from `le31/app/services/__init__.py`)
- **Revert the Hermes Agent hook** (remove the `le31/app/hermes/hooks/case_recording.py` file + remove the hook registration from `le31/app/hermes/hooks/__init__.py`)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v2/cases.py` file + remove the import from `le31/app/api/v2/__init__.py`)
- **Revert the minimal-HTML/HTMX owner-dashboard templates** (remove the `case_ledger.html` + `provenance_graph.html` + `validation_rules.html` files)
- **Revert the `agent-case-graph` dependency** (remove `agent-case-graph` from `requirements.txt`)
- **No data loss** if the rollback happens BEFORE any case-row is written
- **Full data retention** if the rollback happens AFTER rows are written (the four tables are dropped but the case-ledger rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered; for v2 surfaces the v1-pattern still applies as the base)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)
- **charter §3.4 review** — mandatory for any future v2-AI surface adopting the *auditable-agent-workflow* vocabulary
- **charter §3.7 review** — mandatory for any future v2 surface adopting the *auditable-agent-workflow* vocabulary with operator-on-behalf-of-action

## Parent research issue

[linear: blocked — workspace plan-limit error 15th consecutive day; parent fallback at `/opt/data/le31-daily-research-2026-10-04.linear-fallback.json`]
