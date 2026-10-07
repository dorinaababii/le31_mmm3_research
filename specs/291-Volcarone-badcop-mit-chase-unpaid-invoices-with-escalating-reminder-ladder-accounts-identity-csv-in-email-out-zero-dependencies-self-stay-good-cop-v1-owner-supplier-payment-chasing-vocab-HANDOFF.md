# HANDOFF — 291-Volcarone-badcop-v1-owner-supplier-payment-chasing-vocab

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-07
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/291-Volcarone-badcop-mit-chase-unpaid-invoices-with-escalating-reminder-ladder-accounts-identity-csv-in-email-out-zero-dependencies-self-stay-good-cop-v1-owner-supplier-payment-chasing-vocab.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; strongest v1 owner-supplier-payment-chasing cross-section pick of the 70-pass series; **parent override** of subagent's `ALPHAMAN-0/burgerCodeEmployes` 5KB-tiny pick because `badcop` is 1218 KB substantial with 14 topics and stronger on-pattern alignment to LE31's existing supplier-orders feature 16 + payment-tip-reconciliation feature 05)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window v1 owner-supplier-payment-chasing vocabulary reference (`Volcarone/badcop`, MIT, 1★/0⑂, 1218 KB modest, Python on-stack ✓, 14-topic array, in-window by BOTH fields) for the next time the LE31 owner opens a v1 owner-supplier-payment-chasing surface window.

If the trigger condition (v1 owner-supplier-payment-chasing surface window opens) is met, the external coding agent should:

1. Read the active feature file in full.
2. Confirm the `Volcarone/badcop` repo is still in-window (pushed within last 7 days from the trigger date) and the description is still the same.
3. Implement the `SupplierInvoice + ReminderLadderStep + ReminderTemplate + ReminderAuditEntry` SQLModel tables as described in the active feature's Data model section.
4. Implement the reminder-ladder scheduler (pure-Python; no external scheduler dependency; uses a `cron` job + a deterministic state machine).
5. Implement the SMTP sender (pure-stdlib; uses `smtplib` from the standard library only; enforces the *separate-accounts-identity* discipline).
6. Implement the three reminder templates (`reminder_polite.txt + reminder_firmer.txt + reminder_final_notice.txt`; no PII in templates; placeholders only).
7. Run the v1 test suite + the new v1 owner-supplier-payment-chasing test suite.
8. Surface any test failures to the owner (LE31 v1 has no supplier-payment-chasing today; the test suite will be green if `SupplierOrder` is empty, but the *escalating-reminder-ladder* must be verified against a synthetic overdue-invoice scenario).
9. Verify the v1 `SupplierOrder` SQLModel table is extended (not replaced) with the `paid_at` field. The v1 *append-only StockEntry* invariant is preserved.
10. Verify the *separate-accounts-identity* discipline: the SMTP sender uses a `accounts@` credential, NOT the owner's personal email.

If the trigger condition is **not** met, do nothing. The defer artifact can be safely ignored until the owner opens a v1 owner-supplier-payment-chasing surface window.

## Mandatory inputs

- **Active feature**: `features/291-Volcarone-badcop-mit-chase-unpaid-invoices-with-escalating-reminder-ladder-accounts-identity-csv-in-email-out-zero-dependencies-self-stay-good-cop-v1-owner-supplier-payment-chasing-vocab.md`
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-10-07.md` (pass 70, pick B)
- **Raw fetches**: `/opt/data/le31-brainstorm-2026-10-07/gh_small_business_df.json` (parent re-fetched the productive query) and `/opt/data/le31-brainstorm-2026-10-07/verify_Volcarone_badcop.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 70-pass series**:
  - **Feature 16 — `supplier-orders`** — v1 supplier-order tracker
  - **Feature 05 — `payment-tip-reconciliation`** — v1 customer payment (mirror image of supplier payment)
  - **Feature 174 / 177 — `ilkinism/shiftwright`** — v2 owner-pains local-first-staff-rota
  - **Feature 246 — `mshykhov/expense-ledger-bot`** — v1 Telegram expense-ledger

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

- Use the owner's personal email as the `sender_identity` (separate-accounts-identity discipline).
- Add an external SMTP provider (SendGrid, Mailgun, SES) without an explicit charter decision (zero-external-dependencies discipline).
- Update or delete any `ReminderLadderStep` or `ReminderAuditEntry` rows (append-only §3.3 invariant).
- Send reminders to suppliers without an opt-out mechanism (GDPR §3.7 boundary).

## Frozen contract

The active feature file is the frozen contract. Do not silently change the slice, scope, or verification path. If new evidence requires a contract change, surface it to the user and patch the package before re-sending.

## Verification protocol

The external coding agent verifies:

1. Its read of the contract matches the recorded contract fields (`Goal`, `Evidence`, `Scope`, `Description`, `Data model`, `Implementation steps`, `Telegram interaction`, `Dependencies`, `Open questions`, `Why this matters`).
2. The slice does not require another skill, model, or migration outside the package.
3. The end-to-end acceptance path is executable in the configured environment.
4. The rollback or feature-removal path is present and reversible.

End-to-end acceptance path (when triggered):
- Owner creates a `SupplierOrder` with a 30-day payment term
- 30 days pass with no payment
- The reminder-ladder scheduler fires the polite reminder (day 30)
- 7 more days pass with no payment
- The reminder-ladder scheduler fires the firmer reminder (day 37)
- 7 more days pass with no payment
- The reminder-ladder scheduler fires the final-notice reminder (day 44)
- Supplier pays
- Owner marks the `SupplierInvoice` as `paid`
- The owner Telegram bot surfaces a "supplier paid" event
- The `ReminderAuditEntry` table has 3 rows (one per reminder sent)

## Rollback path

- Delete the `SupplierInvoice + ReminderLadderStep + ReminderTemplate + ReminderAuditEntry` SQLModel tables (drop + alembic downgrade).
- Delete the `reminder_ladder.py + smtp_sender.py` service files.
- Delete the `reminder_polite.txt + reminder_firmer.txt + reminder_final_notice.txt` template files.
- Revert the `paid_at` field addition to the existing `SupplierOrder` table (drop column + alembic downgrade).
- The v1 `StockEntry + audit_logs` SQLModel tables are untouched.
- No data is lost (the `SupplierOrder + StockEntry` data is preserved; only the *derived* reminder-ladder data is removed).

## Sign-off gap

This is a defer artifact. The trigger condition is **the next time the LE31 owner opens a v1 owner-supplier-payment-chasing surface window** (estimated Q1 2027 based on the v1 roadmap; no current commitment).

The external coding agent must mirror back the frozen contract before implementing and stop if it cannot.

---

**LE31 charter alignment summary** (per `le31-conventions/SKILL.md`): §3.1 partial (escalating-reminder-ladder + CSV-in/email-out ✓; separate-accounts-identity OFF-§3.1 = explicit charter-decision needed for v1); §3.2 strictly-compatible (MIT permissive + zero-external-dependencies); §3.3 ✓ (append-only `ReminderLadderStep + ReminderAuditEntry` = stronger than §3.3 raw `audit_logs`); §3.4 strong alignment (separate-accounts-identity + non-AI-fallback + observable-evidence + the owner stays the good cop); §3.7 partial (supplier opt-out + GDPR boundary = explicit charter-decision needed).
