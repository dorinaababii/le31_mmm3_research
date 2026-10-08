# HANDOFF — 293-quueli-shift-report-bot-v1-operator-text-to-structured-records-vocabulary

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-08
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/293-quueli-shift-report-bot-mit-parse-free-form-text-shift-reports-structured-records-timezone-aware-analytics-v1-operator-text-to-structured-records-vocabulary.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; strongest v1 operator-text-to-structured-records cross-section pick of the 71-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window v1 operator-text-to-structured-records vocabulary reference (`quueli/shift-report-bot`, MIT, 4★/0⑂, 43 KB modest, Python on-stack ✓, 5-topic array, in-window by BOTH fields) for the next time the LE31 owner opens a v1 operator-text-input surface window.

If the trigger condition (v1 operator-text-input surface window opens) is met, the external coding agent should:

1. Read the active feature file in full.
2. Confirm the `quueli/shift-report-bot` repo is still in-window (pushed within last 7 days from the trigger date) and the description is still the same.
3. Implement the `ShiftReport + ShiftReportEntry + ShiftPeriodRollup` SQLModel tables as described in the active feature's Data model section.
4. Implement the text-parser service (rule-based, deterministic, no LLM; use regex or finite-state-machine; the v1 reference would parse "Sold 87 schnitzels" → `entry_type=units_sold, entry_value=87, entry_unit=count`).
5. Implement the timezone-rollup service (compute `ShiftPeriodRollup` from `ShiftReportEntry` per period with Europe/Zurich timezone).
6. Add a `/shift` Telegram command to the cook-bot that captures raw text → creates a `ShiftReport` row.
7. Run the v1 test suite + the new v1 operator-text-input test suite.
8. Surface any test failures to the owner (LE31 v1 has no operator-text-input today; the test suite will be green if `ShiftReport` is empty, but the deterministic text-parser must be verified against a synthetic seed scenario).
9. Verify the v1 `audit_logs` SQLModel table is untouched (the v1 `ShiftReport` table is NEW, not a migration of v1 `audit_logs`).
10. Verify the *timezone-aware* discipline: every `ShiftReport.timezone` is a tzdata timezone string (e.g., `Europe/Zurich`).

If the trigger condition is **not** met, do nothing. The defer artifact can be safely ignored until the owner opens a v1 operator-text-input surface window.

## Mandatory inputs

- **Active feature**: `features/293-quueli-shift-report-bot-mit-parse-free-form-text-shift-reports-structured-records-timezone-aware-analytics-v1-operator-text-to-structured-records-vocabulary.md`
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-10-08.md` (pass 71, pick A)
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-08/gh_telegram_bot_df.json` (parent re-fetched the productive query) and `/tmp/le31-brainstorm-2026-10-08/verify_parent/quueli_shift-report-bot.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 71-pass series**:
  - **Feature 294 — `quueli/yookassa-polling-payments`** — v1 payment-polling-without-webhook (same author `quueli`; 4★/4★ pair; the 2-repo cluster is the *Telegram-bot + Python + aiogram* sextuple-primitive)
  - **Feature 295 — `23f3000434/CakeShopManagement`** — v1 in-domain bakery-POS
  - **Feature 286 — `gadyamedia/vocenya-mcp`** — v2-AI MCP-server-ai-receptionist
  - **Feature 254 — `OthmaneBlial/lightclaw`** — v2-AI telegram-bot-agent-supervision

## Mandatory LE31 skill list

The external coding agent **MUST** load these skills before implementing:
- `le31-conventions` — charter invariants and the seven-check feature gate
- `le31-v1-feature-pattern` — v1 feature contract shape, slicing rules, and DoD
- `le31-handoff-spec` — frozen contract discipline and verification protocol
- `development` — generic coding pipeline (specify → plan → tasks → implement)
- `speckit-specify` — feature spec writer
- `speckit-plan` — implementation plan writer
- `speckit-tasks` — dependency-ordered task list writer

The external coding agent **MUST NOT**:
- Add an LLM-based text-parser to the v1 stack without an explicit charter decision.
- Update or delete any `ShiftReport` or `ShiftReportEntry` rows (append-only §3.3 invariant).
- Send the parsed `ShiftReportEntry` rows to diners (operator-facing §3.4 invariant).
- Use binary floats for any numeric field (use `Decimal` per charter §3.6 if money; use `int` for non-money counts).

## Frozen contract

The active feature file is the frozen contract. Do not silently change the slice, scope, or verification path. If new evidence requires a contract change, surface it to the user and patch the package before re-sending.

## Verification protocol

The external coding agent verifies:
1. Its read of the contract matches the recorded contract fields (`Goal`, `Evidence`, `Scope`, `Description`, `Data model`, `Implementation steps`, `Telegram interaction`, `Dependencies`, `Open questions`, `Why this matters`).
2. The slice does not require another skill, model, or migration outside the package.
3. The end-to-end acceptance path is executable in the configured environment.
4. The rollback or feature-removal path is present and reversible.

End-to-end acceptance path (when triggered):
- Cook types `/shift Sold 87 schnitzels, 3 stockouts fries` in the cook-Telegram-bot
- The bot parses the text → creates a `ShiftReport` row + 2 `ShiftReportEntry` rows
- The owner opens the v1 owner-daily-recap surface
- The owner sees the parsed `ShiftReportEntry` rows + the `ShiftPeriodRollup` for the day
- The synthetic seed test verifies the text-parser is deterministic (same input = same output)

## Rollback path

- Delete the `ShiftReport + ShiftReportEntry + ShiftPeriodRollup` SQLModel tables (drop + alembic downgrade).
- Delete the `shift_report.py + text_parser.py + timezone_rollup.py` service files.
- Remove the `/shift` command from `bot/commands.py`.
- The v1 `audit_logs` SQLModel table is untouched (NEW tables, not a migration).
- No data is lost (the `ShiftReport + ShiftReportEntry` tables are NEW; deleting the tables loses the cached structured records but not the source `audit_logs`).

## Sign-off gap

This is a defer artifact. The trigger condition is **the next time the LE31 owner opens a v1 operator-text-input surface window** (estimated Q1 2027 based on the v1 roadmap; no current commitment).

The external coding agent must mirror back the frozen contract before implementing and stop if it cannot.

---

**LE31 charter alignment summary** (per `le31-conventions/SKILL.md`): §3.1 partial; §3.2 strictly-compatible; §3.3 ✓; §3.4 strong alignment; §3.6 N/A; §3.7 N/A.
