# Feature 293 — `quueli/shift-report-bot` v1 operator-text-to-structured-records-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v1 (attach to `le31 v1 — Core MVP` P-HMM-3 as the parent of the sub-issue, or to `le31 Research` P-HMM-1 if v1 project is reserved for already-spec'd work — see pipeline note)
> **Date:** 2026-10-08
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/293-quueli-shift-report-bot-mit-parse-free-form-text-shift-reports-structured-records-timezone-aware-analytics-v1-operator-text-to-structured-records-vocabulary.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/293-quueli-shift-report-bot-mit-parse-free-form-text-shift-reports-structured-records-timezone-aware-analytics-v1-operator-text-to-structured-records-vocabulary-HANDOFF.md`
> **Source daily brainstorm:** `/opt/data/le31-brainstorm-2026-10-08.md` (pass 71, pick A)
> **Parent-verified via:** direct GitHub API GET `/repos/quueli/shift-report-bot` at `/tmp/le31-brainstorm-2026-10-08/verify_parent/quueli_shift-report-bot.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed; v1 operator-text-to-structured-records reference is a future-extension signal)
> **Parent-override evidence:** subagent's first-pass Pick B `AlvaroVerona/prime-cost` was a 1-day-ago duplicate of feature 290 (2026-10-07); parent re-surfaced `quueli/shift-report-bot` from `gh_telegram_bot_df.json` and parent-direct-GitHub-API-GET verified.

## Goal

Surface a v1 operator-text-to-structured-records vocabulary reference for **free-form-text-shift-reports + structured-records + timezone-aware-analytics + telegram-bot + text-parsing** as a forward-looking pattern for any future LE31 v1 surface that exposes operator-text-input-to-structured-audit-logs (e.g., cook-end-of-shift text input → structured `ShiftReport + ShiftReportEntry` SQLModel tables with timezone-aware per-period analytics).

## Evidence / JTBD

**Evidence classification:** inferred. The *free-form-text + structured-records + timezone-aware-analytics + telegram-bot + text-parsing* discipline is forward-looking for any future LE31 v1 operator-text-input surface; no LE31 v1 surface today has free-form-text-input parsing. **Confidence: high** (4★/0⑂ + 43 KB modest + Python on-stack ✓ + 5-topic array including `analytics + parser + python + telegram-bot + text-parsing` + 0 customer-facing AI + in-window by BOTH fields = strongest v1 operator-text-to-structured-records cross-section pick of the 71-pass series).

**When** the LE31 cook or waiter wants to record an end-of-shift report by typing free-form text into a Telegram bot ("Sold 87 schnitzels, 3 stockouts on fries, 1 wrong-order refunded, 2 happy customers thanked chef"), **the cook wants to** see the text automatically parsed into a structured `ShiftReport + ShiftReportEntry` SQLModel table with `parsed_at + timezone` fields and per-period analytics rolled up, **but struggles because** the existing v1 `audit_logs` SQLModel table is event-source-only (manual structured rows) with no free-form-text-parsing surface, no timezone-aware per-period analytics, **so that** the cook cannot record shift-end notes without manually clicking structured-form fields in a web UI. The *free-form-text-shift-reports + structured-records + timezone-aware-analytics* discipline IS the *operator-facing* charter §3.4 invariant applied to the *text-to-structured-records* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *free-form-text-shift-reports + structured-records + timezone-aware-per-period-analytics + telegram-bot + text-parsing* quintuple-primitive as a candidate vocabulary for any future LE31 v1 operator-text-input surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres mapping for each primitive.
- Record the §3.1/§3.2/§3.3/§3.4/§3.7 alignment per `le31-conventions/SKILL.md`.
- Note the same-author (`quueli`) 4★/4★ pair: this is one of 2 picks today by the same author (the other is `quueli/yookassa-polling-payments` = Pick B); the 2-repo cluster is the *Telegram-bot + Python + aiogram* sextuple-primitive applied to the *operator-UX + payment-flow* dimension.

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No free-form-text-parsing service; v1 operator-text-input is forward-looking.
- No `ShiftReport + ShiftReportEntry` SQLModel tables today.
- No timezone-aware per-period analytics on the existing `audit_logs` SQLModel table.

## Description

`quueli/shift-report-bot` is a **Telegram-bot for parsing free-form-text shift reports into structured records with timezone-aware per-period analytics** with the following properties:
- **Parse free-form text shift reports into structured records** — the central discipline is the *parse-free-form-text + structured-records* pattern (input = raw text from operator; output = structured rows).
- **Timezone-aware per-period analytics** — the period analytics respects the operator's timezone (Europe/Zurich for LE31); per-period (hourly, daily, weekly) rollups.
- **Telegram-bot-adjacent** — the bot is Telegram-based, in-pattern with LE31 v1's existing `cook-Telegram-bot` surface (charter §3.1 invariant).
- **MIT permissive + 43 KB modest** — small enough to be a vocabulary reference, not a production codebase.
- **5-topic array** including `analytics + parser + python + telegram-bot + text-parsing` = the cleanest v1 operator-text-to-structured-records cross-section topic-coverage of the 71-pass series.

The vocabulary is a strong §3.4-alignment signal for any future LE31 v1 operator-text-input surface because:
- The *parse-free-form-text + structured-records* IS the §3.4 *operator-facing* charter invariant applied to the *text-to-structured-records* dimension.
- The *timezone-aware per-period analytics* IS the §3.1 *explicit-state-transition* charter invariant applied to the *timezone-aware* dimension.
- The *Telegram-bot + text-parsing* IS the §3.1 *Python + aiogram + Telegram-bot* charter invariant applied to the *operator-text-input* dimension.

## Data model

```
ShiftReport        (id, shift_start, shift_end, timezone, raw_text, parsed_at, parsed_by_telegram_user_id)  # NEW — input row
ShiftReportEntry   (id, shift_report_id, entry_type, entry_value, entry_unit, occurred_at, parsed_at)         # NEW — parsed structured rows
ShiftPeriodRollup  (id, period_start, period_end, timezone, total_entries, total_units, computed_at)          # NEW — derived view, append-only
```

The `ShiftReport + ShiftReportEntry` tables are the *input* layer (raw text + parsed rows). The `ShiftPeriodRollup` table is a **derived view** that computes per-period analytics from the `ShiftReportEntry` rows and writes a new row per period. It is append-only (the *period* is the primary-key component; recomputing a period writes a new row, never updates). The *timezone-aware* field on every table is the §3.1 *explicit-state-transition* invariant applied to the *timezone* dimension.

## Implementation steps

**This is a defer artifact. No code is written today.** When (and if) a future v1 PR adopts the *free-form-text-shift-reports + structured-records + timezone-aware-analytics* discipline, the following files would be touched:
- `/opt/data/le31_mmm3_research_work/backend/app/models/shift_report.py` — new SQLModel `ShiftReport + ShiftReportEntry + ShiftPeriodRollup` tables (append-only, §3.1 invariant).
- `/opt/data/le31_mmm3_research_work/backend/app/services/text_parser.py` — parse free-form text into structured rows (rule-based, deterministic, no LLM).
- `/opt/data/le31_mmm3_research_work/backend/app/services/timezone_rollup.py` — compute `ShiftPeriodRollup` from `ShiftReportEntry` per period with Europe/Zurich timezone.
- `/opt/data/le31_mmm3_research_work/backend/app/bot/commands.py` — add a `/shift` Telegram command that captures raw text → creates a `ShiftReport` row.
- (No other files expected to require changes for a vocabulary-only PR.)

## Telegram interaction

**None today** (defer artifact; no v1 build; vocabulary-only). If a future v1 operator-text-input surface is built, the cook-side Telegram bot could accept a free-form text shift report via the `/shift` command (e.g., cook types "/shift 87 schnitzels sold, 3 stockouts fries, 1 wrong-order refund, 2 happy customers thanked chef"). The bot would parse the text into `ShiftReportEntry` rows, persist them, and reply with a structured summary. The interaction is operator-facing per charter §3.4; not customer-facing.

## Dependencies

- **Charter §3.1 (explicit-state-transition)**: existing `audit_logs` SQLModel table is the v1 precedent; the `ShiftReport + ShiftReportEntry` tables extend the same pattern to the *operator-text-input* dimension with **append-only timezone-aware structured records**.
- **Charter §3.3 (audit-log-immutability)**: existing `StockEntry` SQLModel table is the v1 append-only ledger; the `ShiftReport` table extends the pattern to the *operator-text-input* dimension.
- **Charter §3.4 (operator-facing)**: the *operator-text-input* surface is operator-tooling per charter §3.4 invariant; the *free-form-text-parsing* primitive is a deterministic text-parsing primitive, not customer-facing AI; the *Telegram-bot* posture is the v1 cook-Telegram-bot surface.
- **Stack note**: `quueli/shift-report-bot` uses Telegram-bot + Python + text-parsing; LE31 v1 already uses aiogram 3 + Python + Telegram-bot; the *text-parsing* discipline is on-stack (the v1 reference would use a rule-based parser; no LLM, no AI-agent).
- **No v1 dependencies today**: this is a v1 forward-looking surface; no v1 code depends on it.

## Open questions

1. **What is the parser discipline?** A future PR would need to specify the parser (rule-based with regex, LLM-based with prompt-engineering, or a hybrid). The `quueli/shift-report-bot` source (if readable) would inform the choice; a rule-based parser is the v1-alignment choice (deterministic + no LLM).
2. **What is the timezone convention?** The discipline uses *timezone* as a field; a future PR would need to specify the timezone (Europe/Zurich for LE31, per the existing v1 Paris/EU convention).
3. **What is the period granularity?** The discipline uses *period_start + period_end* as the primary-key component; a future PR would need to specify the period granularity (hourly, daily, weekly?). A daily rollup is the most common in restaurant operations.
4. **What is the entry_type vocabulary?** A future PR would need to specify the entry_type enum (e.g., `units_sold, stockout, wrong_order, customer_feedback`).
5. **What is the relationship between the v1 `StockEntry` SQLModel table and the v1 `ShiftReportEntry` SQLModel table?** The v1 `StockEntry` is a manual structured event log; the v1 `ShiftReportEntry` is a parsed text event log. A future PR would need to specify the relationship (e.g., do `ShiftReportEntry` rows auto-create `StockEntry` rows?).

## Why this matters

This is the **strongest v1 operator-text-to-structured-records cross-section pick of the 71-pass brainstorm series**. The *free-form-text-shift-reports + structured-records + timezone-aware-analytics + telegram-bot + text-parsing* quintuple-primitive maps 1:1 onto the *operator-text-input* surface that a future v1 PR might add to extend the existing `audit_logs` SQLModel table. The Python + 5-topic + 4★/0⑂ + in-window-by-both-fields stack is **§3.1 + §3.2 + §3.3 + §3.4 + §3.6 ON-PATTERN** for LE31; the *structured-records-from-free-form-text + timezone-aware-analytics + telegram-bot-adjacent* discipline IS stack-adjacent.

The **free-form-text + structured-records** discipline extends the existing v1 event-sourcing pattern to the *operator-text-input* dimension with a deterministic text-parsing primitive. The **timezone-aware per-period analytics** discipline extends the v1 `audit_logs` event-sourcing pattern to the *timezone* dimension. The **Telegram-bot + text-parsing** discipline extends the v1 cook-Telegram-bot pattern to the *text-input* dimension.

**Charter alignment summary:** §3.1 partial (operator-text-input + structured-records + timezone-aware ✓; rule-based text-parser discipline ✓); §3.2 strictly-compatible (MIT permissive); §3.3 ✓ (append-only `ShiftReport + ShiftReportEntry` = same pattern as v1 `StockEntry`); §3.4 strong alignment (operator-facing + deterministic text-parser + non-AI-fallback + observable-evidence); §3.6 N/A (no money primitives in this surface); §3.7 N/A.

---

**LE31 charter alignment summary** (per `le31-conventions/SKILL.md`): §3.1 partial; §3.2 strictly-compatible; §3.3 ✓; §3.4 strong alignment; §3.6 N/A; §3.7 N/A.
