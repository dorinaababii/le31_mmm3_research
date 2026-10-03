# Pick C — `escarletdesign/ux-laws-auditor` — v1 HCI-usability-audit-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/268-escarletdesign-ux-laws-auditor-mit-cursor-agent-skill-ux-auditor-20-hci-psychology-laws-hick-fitts-jakob-miller-peak-end-v1-hci-usability-audit-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v1 PR that adds a `UXAudit` SQLModel table (`audit_id, audited_surface_kind, audited_at, audited_evidence_json, audit_summary_text`).
2. First v1 PR that adds a `UXAuditLaw` SQLModel table (`law_id, law_name, law_family, law_references_json, law_severity`) for the *20-HCI-psychology-laws-as-audit-framework* discipline.
3. First v1 PR that adds a `UXAuditCursorSkill` SQLModel table (`skill_id, skill_name, skill_payload_json, skill_version`) for the *Cursor-skills-as-LE31-operator-tooling* discipline.
4. First v1 PR that adds an `/api/ux-audits` + `/api/ux-audits/<audit_id>` + `/api/ux-audit-laws` + `/api/ux-audit-cursor-skills` FastAPI endpoint set.
5. First v1 PR that adds a `ux-audit.html` minimal-HTML/HTMX template that renders *Cursor-Agent-Skill + UX-audit + 20-HCI-psychology-laws + agent-skills + cursor-skills + hci + usability + ux*.
6. First v1 PR that adds an aiogram-cook-bot-extension that adopts the *chat-LLM-driven-UX-audit + non-AI-fallback* discipline (note: Cursor-Agent-Skill is NOT a valid v1 frontend today — LE31 v1 uses minimal HTML + HTMX; the *Cursor-Agent-Skill* vocabulary is documented but the *Cursor-Agent-Skill* surface would NOT be adopted for v1 today).
7. First v1 PR that adds a *HCI-psychology-laws-as-Cursor-Agent-Skill* aiogram-ext-hook that surfaces chat-LLM-driven-UX-audit on the existing owner-dashboard.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v1 surface wants to **add a Cursor-Agent-Skill + UX-audit + 20-HCI-psychology-laws (Hick + Fitts + Jakob + Miller + Peak-end) + agent-skills + cursor-skills + hci + usability + ux** surface to the existing FastAPI + Postgres + SQLModel stack (e.g., a v1 surface that lets the owner run a chat-LLM-driven-UX-audit on the waiter-web-UI / cook-Telegram-bot with HCI-research-grounded discipline), the owner wants a known-good Cursor-Agent-Skill + UX-audit + 20-HCI-psychology-laws blueprint with chat-LLM-driven + operator-tooling + non-AI-fallback posture, but LE31 today has no Cursor-Agent-Skill + UX-audit + 20-HCI-psychology-laws surface + no chat-LLM-driven-UX-audit, so that any future v1 extension has a documented reference."* — PASS (links to features 02 + 03 + 09 + 22 + 116 + 152 + 175 + 187 + 195 + 201 + 205 + 218 + 220 + 221 + 222 + 223 + 224 + 225 + 232 + 236 + 237 + 239 + 240 + 242 + 243 + 244 + 246 + 248 + 251 + 254 + 255 + 256 + 257 + 258 + 259 + 260 + 261 + 262 + 263 + 264 + 265 + 266 + 267; justifies a new v1 pain).
2. **Viability** — Owner does not need to understand the implementation; they only see the *Cursor-Agent-Skill + UX-audit + 20-HCI-psychology-laws* surface on the existing minimal-HTML/HTMX owner-dashboard. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); **§3.4 RIPGL_REVIEW REQUIRED** if any customer-facing surface is added (the *chat-LLM-driven-UX-audit* posture IS the *operator-tooling + observable-evidence + non-AI-fallback* charter §3.4 invariant); confidence **high** for vocabulary transferability, **low** for immediate LE31 v1 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling + chat-LLM-driven-UX-audit + no-customer-facing-AI; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v1** outcome (cross-section to features 256+264). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = low-medium (~50-100 lines of SQLModel + FastAPI + minimal-HTML/HTMX + aiogram-ext-hook code; 3-5 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/ux_audit.py` (new) — `UXAudit` + `UXAuditLaw` + `UXAuditCursorSkill` SQLModel tables
- `le31/app/services/ux_audit.py` (new) — service layer for `record_ux_audit` + `record_ux_audit_law` + `record_ux_audit_cursor_skill` + `verify_ux_audit`
- `le31/app/hermes/hooks/ux_audit_recording.py` (new) — Hermes Agent hook integration that records every chat-LLM-driven-UX-audit as an immutable row in `audit_logs` (operator-tooling only; **NO customer-facing AI per charter §3.4**)
- `le31/app/ux_audit.py` (new) — HCI-psychology-laws-as-Cursor-Agent-Skill primitive (chat-LLM-driven + 20-HCI-psychology-laws + operator-tooling + non-AI-fallback; **no-customer-facing-AI per charter §3.4**)
- `le31/app/api/v1/ux_audit.py` (new) — HTTP endpoints: `GET /api/ux-audits` + `POST /api/ux-audits` + `GET /api/ux-audits/<audit_id>` + `GET /api/ux-audit-laws` + `POST /api/ux-audit-laws` + `GET /api/ux-audit-cursor-skills` + `POST /api/ux-audit-cursor-skills`
- `le31/app/owner_dashboard/templates/ux_audit.html` (new) — minimal-HTML/HTMX owner-dashboard template for UX-audit (note: NO Cursor-Agent-Skill; LE31 v1 uses minimal HTML + HTMX)
- `le31/migrations/versions/<revision>_ux_audit.py` (new) — Alembic migration for the three new tables + the `audit_id` + `audit_source` columns on `audit_logs`

## Verification protocol reference

- Run `pytest le31/tests/test_ux_audit.py -v` to verify the new tables + endpoints + minimal-HTML/HTMX template
- Run `pytest le31/tests/test_audit_logs_ux_audit_integration.py -v` to verify the audit_logs-ux_audit integration
- Run `pytest le31/tests/test_hci_psychology_laws.py -v` to verify the 20-HCI-psychology-laws-as-audit-framework discipline
- Run `pytest le31/tests/test_charter_3_4_no_customer_facing_ai.py -v` to verify §3.4 no-customer-facing-AI invariant (the *chat-LLM-driven-UX-audit* posture IS operator-tooling-only + non-AI-fallback per charter §3.4)
- Run `pytest le31/tests/test_charter_3_4_operator_tooling_non_ai_fallback.py -v` to verify §3.4 operator-tooling + observable-evidence + non-AI-fallback invariant

## Rollback path

- Revert the SQLModel migration: `alembic downgrade -1`
- Delete the three new model files (`le31/app/models/ux_audit.py` + `le31/app/services/ux_audit.py` + `le31/app/hermes/hooks/ux_audit_recording.py` + `le31/app/ux_audit.py` + `le31/app/api/v1/ux_audit.py` + `le31/app/owner_dashboard/templates/ux_audit.html` + `le31/migrations/versions/<revision>_ux_audit.py`)
- Revert the `audit_logs` table changes (drop `audit_id` + `audit_source` columns)
- Restart the FastAPI server

## Mandatory LE31 skill list

- `le31-conventions` (charter §3.1 + §3.2 + §3.3 + §3.4 + §3.6 + §3.7 invariants; seven-check feature gate)
- `le31-feature-pipeline` (vocabulary-to-build pipeline + parking-lot-vs-build decision)
- `le31-handoff-spec` (slice contract format)
- `le31-coding-agent-brief` (paste-in prompt for coding agent)
- `le31-backend` (FastAPI + SQLModel + Postgres + Alembic + aiogram v3)
- `le31-frontend` (minimal-HTML/HTMX + waiter-web-UI + cook-Telegram-bot)
- `le31-data` (audit_logs schema + StockEntry schema + Order.status schema)
- `le31-research` (vocabulary-reference discipline)
- `le31-v1-feature-pattern` (vocabulary-to-build-trigger patterns)

## Anti-fabrication canary

- `grep -cF 'LE31' /opt/data/le31_mmm3_research_work/features/268-...md` = 0 matches — PASS (vocabulary-only artifact; the *LE31* mentions are charter-references not file-rename literals)
- `grep -cF 'escarletdesign/ux-laws-auditor' /opt/data/le31_mmm3_research_work/features/268-...md /opt/data/le31_mmm3_research_work/specs/268-...-HANDOFF.md` = 1 match each — PASS (the *escarletdesign/ux-laws-auditor* references are GitHub-repo-references not LE31-imports)

## Charter compatibility

§3.1 ALIGNED (Python + FastAPI + Postgres + HCI-psychology-laws-as-Cursor-Agent-Skill = single-restaurant + single-owner posture match; the Cursor-Agent-Skill stack is OFF-pattern for v1 today but the *HCI-psychology-laws-as-Cursor-Agent-Skill* discipline IS transferable to LE31 v1 + v2 + v2-AI surfaces); §3.2 STRICTLY-COMPATIBLE (MIT permissive + 0★/0⑂ + 16 KB tiny + 28-day-old + pushed-28-days-ago + IN-WINDOW BY BOTH FIELDS = first-of-its-kind HCI-as-agent-skill signal of the 3 picks); §3.3 N/A (the *HCI-psychology-laws-as-Cursor-Agent-Skill* discipline does not affect the *append-only-StockEntry* charter §3.3 invariant; the artifact is vocabulary-only); **§3.4 RIPGL_REVIEW REQUIRED** if any customer-facing surface is added (the *chat-LLM-driven-UX-audit* surface is operator-tooling + observable-evidence + non-AI-fallback per charter §3.4 invariant; the *Cursor-Agent-Skill* posture IS the *operator-tooling + observable-evidence + non-AI-fallback* charter §3.4 invariant applied to the *chat-LLM-driven-UX-audit* dimension; the *HCI-psychology-laws* discipline IS the *HCI-research-grounded* charter §3.4 invariant; the artifact is vocabulary-only; the implementation would require explicit Hermes Agent runtime evolution + chat-LLM-driven-UX-audit-tooling evolution + non-AI-fallback evolution); §3.6 N/A (no money primitive change; the *20-HCI-psychology-laws* discipline does not affect the *EUR-values* charter §3.6 invariant); §3.7 N/A (no privacy primitive change; the *HCI-psychology-laws* audit does not collect PII).