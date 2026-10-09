# Pick C — `sattyamjjain/agent-audit-kit` — v2-AI MCP-agent-pipeline-static-scanner-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research/features/268-sattyamjjain-agent-audit-kit-apache-2-0-static-scanner-mcp-connected-ai-agent-pipelines-365-rules-14-categories-owasp-agentic-mcp-10-10-github-action-sarif-v2-ai-mcp-agent-pipeline-static-scanner-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2-AI PR that adds a `McpPipelineScan` SQLModel table (`scan_id, scan_pipeline_id, scan_started_at, scan_completed_at, scan_result_summary, recorded_at`).
2. First v2-AI PR that adds a `ComplianceRule` SQLModel table (`rule_id, rule_category, rule_framework, rule_severity, rule_description, rule_cve_ids, recorded_at`).
3. First v2-AI PR that adds a `CveToRuleLedger` SQLModel table (`cve_id, cve_severity, cve_description, cve_rule_ids, cve_first_seen, recorded_at`).
4. First v2-AI PR that adds a `ScanResult` SQLModel table (`result_id, scan_id, rule_id, result_status, result_payload, recorded_at`).
5. First v2-AI PR that adds a `ComplianceFramework` SQLModel table (`framework_id, framework_name, framework_version, framework_owasp_mapping, recorded_at`).
6. First v2-AI PR that extends the existing `audit_logs` table with `compliance_rule_id` + `compliance_framework` columns.
7. First v2-AI PR that adds a `/compliance scan <pipeline_id>` / `/compliance rule <rule_id>` / `/compliance cve <cve_id>` Telegram command set on the cook-bot (operator-tooling only; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**).
8. First v2-AI PR that adds a new GitHub Actions workflow that runs the *MCP-connected-AI-agent-pipeline-static-scanner + SARIF-export* on every PR.
9. First v2-AI PR that adds a Hermes Agent compliance-scanner-as-runtime-concern extension that exports SARIF + a public CVE-to-rule-ledger.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v2-AI surface (owner-AI assistance) wants to scan AI-agent-tool-invocations for compliance with the OWASP-Agentic-10-10 + MCP-10-10 frameworks, it wants a *static scanner for MCP-connected AI agent pipelines + 365 rules + 14 categories + 14 compliance frameworks + SARIF + public-CVE-to-rule-ledger*, but struggles because the current LE31 has no AI-agent-pipeline-compliance-scanner + no SARIF-export + no CVE-to-rule-ledger, so that the *compliance-framework-as-runtime-concern* primitive becomes a future-v2-AI surface-extension recipe."* — PASS (links to features 149 + 199 + 232 + 236 + 237 + 257 + 258 + 260 + 261 + 262 + 264; justifies a new pain).
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the *compliance-scan-output* + *CVE-rule-ledger-lineage* outputs. PASS.
3. **Practicability and confidence** — Apache-2.0 permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 not triggered (operator-tooling; no customer-facing AI); confidence **high** for vocabulary transferability, **low** for immediate LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling only; §3.1 explicit-state-transitions preserved; §3.2 Apache-2.0 permissive. PASS.
5. **Outcome, appetite, and scope** — **v2-AI** outcome (cross-section to features 149+199+232+236+237+257+258+260+261+262+264). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today (LE31 has no v2-AI surface yet); pain is forecast for v2-AI adoption era. Implementation cost = low-medium (~20-50 lines of SARIF-export + CVE-to-rule-ledger code; 1-2 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/mcp_pipeline_scan.py` (new) — `McpPipelineScan` + `ComplianceRule` + `CveToRuleLedger` + `ScanResult` + `ComplianceFramework` SQLModel tables
- `le31/app/services/mcp_pipeline_scan.py` (new) — service layer for `run_mcp_pipeline_scan` + `register_compliance_rule` + `lookup_cve_to_rule` + `export_scan_result_sarif`
- `le31/app/hermes/hooks/mcp_pipeline_scan.py` (new) — Hermes Agent compliance-scanner-as-runtime-concern extension that exports SARIF + a public CVE-to-rule-ledger
- `le31/app/api/v1/mcp_pipeline_scan.py` (new) — HTTP endpoints: `POST /api/mcp-pipeline-scan/run` + `GET /api/mcp-pipeline-scan/result/<scan_id>` + `GET /api/mcp-pipeline-scan/cve/<cve_id>` + `GET /api/mcp-pipeline-scan/rule/<rule_id>`
- `le31/app/cook_bot/handlers/mcp_pipeline_scan.py` (new) — Telegram command handlers: `/compliance scan <pipeline_id>` + `/compliance rule <rule_id>` + `/compliance cve <cve_id>` (operator-tooling only; NOT customer-facing)
- `le31/migrations/versions/<revision>_mcp_pipeline_scan.py` (new) — Alembic migration for the five new tables + the new `audit_logs` columns
- `.github/workflows/mcp-pipeline-scan.yml` (new) — GitHub Actions workflow that runs the *MCP-connected-AI-agent-pipeline-static-scanner + SARIF-export* on every PR
- `skills/le31-conventions/SKILL.md` — append the *MCP-connected-AI-agent-pipeline-static-scanner + 365-rules + 14-categories + 14-compliance-frameworks + OWASP-Agentic-10-10 + MCP-10-10 + GitHub-Action + SARIF + public-CVE-to-rule-ledger* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the five new tables + revert the new `audit_logs` columns
- **Revert the MCP-pipeline-scan service** (remove the `le31/app/services/mcp_pipeline_scan.py` file + remove the import from `le31/app/services/__init__.py`)
- **Revert the Hermes Agent hook** (remove the `le31/app/hermes/hooks/mcp_pipeline_scan.py` file + remove the hook registration from `le31/app/hermes/hooks/__init__.py`)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/mcp_pipeline_scan.py` file + remove the import from `le31/app/api/v1/__init__.py`)
- **Revert the Telegram command handlers** (remove the `le31/app/cook_bot/handlers/mcp_pipeline_scan.py` file + remove the registration from `le31/app/cook_bot/handlers/__init__.py`)
- **Revert the GitHub Actions workflow** (remove the `.github/workflows/mcp-pipeline-scan.yml` file)
- **No data loss** if the rollback happens BEFORE any `ScanResult` row is written
- **Full data retention** if the rollback happens AFTER rows are written (the five tables are dropped but the `ScanResult` rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked] (workspace plan-limit error — 14th consecutive day; verified today via `save_issue` write-probe with requestId `a449f6e6bc89bb71`; parent fallback at `/opt/data/le31-daily-research-2026-10-03.linear-fallback.json`)
