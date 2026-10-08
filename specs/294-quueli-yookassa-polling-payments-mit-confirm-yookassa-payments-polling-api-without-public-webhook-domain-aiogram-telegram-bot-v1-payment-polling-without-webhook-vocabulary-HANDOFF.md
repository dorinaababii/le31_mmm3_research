# HANDOFF — 294-quueli-yookassa-polling-payments-v1-payment-polling-without-webhook-vocabulary

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-08
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/294-quueli-yookassa-polling-payments-mit-confirm-yookassa-payments-polling-api-without-public-webhook-domain-aiogram-telegram-bot-v1-payment-polling-without-webhook-vocabulary.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; strongest v1 payment-polling-without-webhook cross-section pick of the 71-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window v1 payment-polling-without-webhook vocabulary reference (`quueli/yookassa-polling-payments`, MIT, 4★/0⑂, 40 KB modest, Python on-stack ✓, aiogram-on-stack ✓, 5-topic array, in-window by BOTH fields) for the next time the LE31 owner opens a v1 payment-confirmation surface window.

If the trigger condition (v1 payment-confirmation surface window opens) is met, the external coding agent should:

1. Read the active feature file in full.
2. Confirm the `quueli/yookassa-polling-payments` repo is still in-window (pushed within last 7 days from the trigger date) and the description is still the same.
3. Implement the `PaymentProvider + PaymentConfirmation + PaymentPollAttempt` SQLModel tables as described in the active feature's Data model section.
4. Implement the payment-poller service (FastAPI background task or separate cron job; polls the payment provider's API every N seconds; updates `PaymentConfirmation` rows; appends `PaymentPollAttempt` rows).
5. Implement the payment-parser service (parse the payment provider's response into `PaymentConfirmation` row fields).
6. Add a `/payment` Telegram command to the owner-bot that shows the latest payment-confirmations.
7. Run the v1 test suite + the new v1 payment-confirmation test suite.
8. Surface any test failures to the owner (LE31 v1 has no payment-confirmation today; the test suite will be green if `PaymentConfirmation` is empty, but the deterministic polling-pattern must be verified against a synthetic seed scenario).
9. Verify the v1 `audit_logs` SQLModel table is untouched (the v1 `PaymentConfirmation` table is NEW, not a migration of v1 `audit_logs`).
10. Verify the *amount_eur* + *currency* fields use `Decimal` per charter §3.6.

If the trigger condition is **not** met, do nothing. The defer artifact can be safely ignored until the owner opens a v1 payment-confirmation surface window.

## Mandatory inputs

- **Active feature**: `features/294-quueli-yookassa-polling-payments-mit-confirm-yookassa-payments-polling-api-without-public-webhook-domain-aiogram-telegram-bot-v1-payment-polling-without-webhook-vocabulary.md`
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-10-08.md` (pass 71, pick B)
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-08/gh_telegram_bot_df.json` (parent re-fetched the productive query) and `/tmp/le31-brainstorm-2026-10-08/verify_parent/quueli_yookassa-polling-payments.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 71-pass series**:
  - **Feature 293 — `quueli/shift-report-bot`** — v1 operator-text-to-structured-records (same author `quueli`; 4★/4★ pair; the 2-repo cluster is the *Telegram-bot + Python + aiogram* sextuple-primitive)
  - **Feature 295 — `23f3000434/CakeShopManagement`** — v1 in-domain bakery-POS
  - **Feature 166 — `median-labs/close-the-books`** — v1 AI-agent-human-review-gate (cross-section with payment-confirmation + human-gate)
  - **Feature 5 — `payment-tip-reconciliation`** — v1 customer-payment (cross-section with payment-confirmation)

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
- Add a YooKassa-Russian-specific integration to the v1 stack (YooKassa is off-domain for LE31 v1 EU/US market; substitute with Stripe / Mollie / local provider).
- Update or delete any `PaymentPollAttempt` rows (append-only §3.3 invariant).
- Send payment-confirmations to diners (operator-facing §3.4 invariant).
- Use binary floats for `amount_eur` (use `Decimal` per charter §3.6).
- Store the payment provider's API key in source (use env var per charter §3.2; not in `PaymentProvider` table; not in source).

## Frozen contract

The active feature file is the frozen contract. Do not silently change the slice, scope, or verification path. If new evidence requires a contract change, surface it to the user and patch the package before re-sending.

## Verification protocol

The external coding agent verifies:
1. Its read of the contract matches the recorded contract fields (`Goal`, `Evidence`, `Scope`, `Description`, `Data model`, `Implementation steps`, `Telegram interaction`, `Dependencies`, `Open questions`, `Why this matters`).
2. The slice does not require another skill, model, or migration outside the package.
3. The end-to-end acceptance path is executable in the configured environment.
4. The rollback or feature-removal path is present and reversible.

End-to-end acceptance path (when triggered):
- Customer pays €42.50 via the payment provider
- The payment-poller polls the provider's API and detects the payment
- A `PaymentConfirmation` row is created with `status=confirmed, amount_eur=42.50, currency=EUR`
- A `PaymentPollAttempt` row is appended with `response_status=200, response_body={...}`
- The owner opens the v1 owner-Telegram-bot
- The owner types `/payment` and sees the latest payment-confirmations
- The synthetic seed test verifies the polling-pattern is deterministic (same input = same output)

## Rollback path

- Delete the `PaymentProvider + PaymentConfirmation + PaymentPollAttempt` SQLModel tables (drop + alembic downgrade).
- Delete the `payment.py + payment_poller.py + payment_parser.py` service files.
- Remove the `/payment` command from `bot/commands.py`.
- The v1 `audit_logs` SQLModel table is untouched (NEW tables, not a migration).
- No data is lost (the `PaymentConfirmation + PaymentPollAttempt` tables are NEW; deleting the tables loses the cached payment-confirmations but not the source `audit_logs`).

## Sign-off gap

This is a defer artifact. The trigger condition is **the next time the LE31 owner opens a v1 payment-confirmation surface window** (estimated Q1 2027 based on the v1 roadmap; no current commitment).

The external coding agent must mirror back the frozen contract before implementing and stop if it cannot.

---

**LE31 charter alignment summary** (per `le31-conventions/SKILL.md`): §3.1 partial; §3.2 strictly-compatible; §3.3 ✓; §3.4 strong alignment; §3.6 ✓; §3.7 N/A.
