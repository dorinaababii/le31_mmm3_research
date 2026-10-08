# Feature 294 — `quueli/yookassa-polling-payments` v1 payment-polling-without-webhook-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v1 (attach to `le31 v1 — Core MVP` P-HMM-3 as the parent of the sub-issue, or to `le31 Research` P-HMM-1 if v1 project is reserved for already-spec'd work — see pipeline note)
> **Date:** 2026-10-08
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/294-quueli-yookassa-polling-payments-mit-confirm-yookassa-payments-polling-api-without-public-webhook-domain-aiogram-telegram-bot-v1-payment-polling-without-webhook-vocabulary.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/294-quueli-yookassa-polling-payments-mit-confirm-yookassa-payments-polling-api-without-public-webhook-domain-aiogram-telegram-bot-v1-payment-polling-without-webhook-vocabulary-HANDOFF.md`
> **Source daily brainstorm:** `/opt/data/le31-brainstorm-2026-10-08.md` (pass 71, pick B)
> **Parent-verified via:** direct GitHub API GET `/repos/quueli/yookassa-polling-payments` at `/tmp/le31-brainstorm-2026-10-08/verify_parent/quueli_yookassa-polling-payments.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed; v1 payment-polling-without-webhook reference is a future-extension signal)
> **Parent-override evidence:** subagent's first-pass Pick A `alissonlittig/vitrine-erp` was off-domain multi-store retail; parent re-surfaced `quueli/yookassa-polling-payments` from `gh_telegram_bot_df.json` and parent-direct-GitHub-API-GET verified.

## Goal

Surface a v1 payment-polling-without-webhook vocabulary reference for **yookassa-payments + aiogram + telegram-bot + python + polling-without-webhook** as a forward-looking pattern for any future LE31 v1 surface that exposes payment-confirmation-without-public-webhook (e.g., self-hosted payment confirmation that polls a payment provider's API instead of receiving webhook callbacks; useful for VPS deployments without a public domain).

## Evidence / JTBD

**Evidence classification:** inferred. The *polling-without-webhook + separate-accounts-identity + self-hosted-payment-confirmation* discipline is forward-looking for any future LE31 v1 payment-confirmation surface that runs on a VPS without a public domain. **Confidence: high** (4★/0⑂ + 40 KB modest + Python on-stack ✓ + aiogram-on-stack ✓ + 5-topic array including `aiogram + payments + python + telegram-bot + yookassa` + 0 customer-facing AI + in-window by BOTH fields = strongest v1 payment-polling-without-webhook cross-section pick of the 71-pass series).

**When** the LE31 owner wants to confirm a payment from a customer (e.g., a customer paid via a payment provider and the owner wants to confirm the payment without exposing a public webhook endpoint), **the owner wants to** poll the payment provider's API on a schedule (e.g., every 30 seconds) and update a `PaymentConfirmation` SQLModel table when the payment is confirmed, **but struggles because** the existing v1 `audit_logs` SQLModel table has no payment-confirmation surface, no payment-provider integration, no polling-pattern, **so that** the owner cannot confirm payments without a public webhook endpoint. The *polling-without-webhook-or-domain* posture IS the *self-hosted + zero-external-dependencies* charter §3.2 invariant applied to the *payment-confirmation* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *polling-without-webhook + separate-accounts-identity + self-hosted-payment-confirmation* triple-primitive as a candidate vocabulary for any future LE31 v1 payment-confirmation surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres+aiogram mapping for each primitive.
- Record the §3.1/§3.2/§3.3/§3.4/§3.6 alignment per `le31-conventions/SKILL.md`.
- Note the same-author (`quueli`) 4★/4★ pair: this is one of 2 picks today by the same author (the other is `quueli/shift-report-bot` = Pick A); the 2-repo cluster is the *Telegram-bot + Python + aiogram* sextuple-primitive applied to the *operator-UX + payment-flow* dimension.
- Note the YooKassa-Russian-specific off-domain status (YooKassa is a Russian payment provider; the *polling-pattern* is universal; a future PR would substitute the local payment provider).

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No YooKassa integration; v1 payment-confirmation is forward-looking.
- No `PaymentConfirmation + PaymentPollAttempt + PaymentProvider` SQLModel tables today.
- No polling-pattern on the existing `audit_logs` SQLModel table.

## Description

`quueli/yookassa-polling-payments` is a **Telegram-bot for confirming YooKassa payments by polling the API, without a public webhook or domain** with the following properties:
- **Confirm YooKassa payments by polling the API** — the central discipline is the *polling-the-payment-provider-API* pattern (a scheduled task polls the API every N seconds, checks if a payment is confirmed, and updates the local state).
- **Without a public webhook or domain** — the architecture assumes a VPS deployment without a public domain, so the polling pattern is the only way to receive payment-confirmation events.
- **Telegram-bot-adjacent** — the bot is Telegram-based, in-pattern with LE31 v1's existing `cook-Telegram-bot` surface (charter §3.1 invariant).
- **MIT permissive + 40 KB modest** — small enough to be a vocabulary reference, not a production codebase.
- **5-topic array** including `aiogram + payments + python + telegram-bot + yookassa` = the cleanest v1 payment-polling-without-webhook cross-section topic-coverage of the 71-pass series.

The vocabulary is a strong §3.2-alignment signal for any future LE31 v1 payment-confirmation surface because:
- The *polling-without-webhook-or-domain* IS the §3.2 *self-hosted + zero-external-dependencies* charter invariant applied to the *payment-confirmation* dimension.
- The *Telegram-bot + aiogram + payments* IS the §3.1 *Python + aiogram + Telegram-bot* charter invariant applied to the *payment-flow* dimension.
- The *payments* topic IS the §3.6 *Money: never use binary floats* charter invariant applied to the *payment-confirmation* dimension.

## Data model

```
PaymentProvider     (id, name, polling_url, polling_interval_seconds, api_key_env_var)  # NEW — provider config
PaymentConfirmation (id, payment_id, payment_provider_id, status, amount_eur, currency, confirmed_at, poll_count)  # NEW — confirmation row
PaymentPollAttempt  (id, payment_confirmation_id, attempted_at, response_status, response_body)  # NEW — append-only audit of every poll attempt
```

The `PaymentConfirmation` table is the *current state* (one row per payment, updated on each confirmation). The `PaymentPollAttempt` table is a **append-only audit log** of every poll attempt (charter §3.3 invariant). The `PaymentProvider` table is a *config* table (one row per provider; the v1 would have one row for the local payment provider; the `quueli/yookassa-polling-payments` reference uses YooKassa = Russian; the v1 would substitute Stripe / Mollie / local provider). The *amount_eur* + *currency* fields use `Decimal` (Python `decimal.Decimal` or pydantic `condecimal`) per the existing v1 EUR convention (charter §3.6).

## Implementation steps

**This is a defer artifact. No code is written today.** When (and if) a future v1 PR adopts the *polling-without-webhook + separate-accounts-identity + self-hosted-payment-confirmation* discipline, the following files would be touched:
- `/opt/data/le31_mmm3_research_work/backend/app/models/payment.py` — new SQLModel `PaymentProvider + PaymentConfirmation + PaymentPollAttempt` tables (append-only for `PaymentPollAttempt`, state-row for `PaymentConfirmation`).
- `/opt/data/le31_mmm3_research_work/backend/app/services/payment_poller.py` — scheduled task that polls the payment provider's API every N seconds and updates `PaymentConfirmation` rows.
- `/opt/data/le31_mmm3_research_work/backend/app/services/payment_parser.py` — parse the payment provider's response (status, amount, currency) into the `PaymentConfirmation` row.
- `/opt/data/le31_mmm3_research_work/backend/app/bot/commands.py` — add a `/payment` Telegram command that shows the latest payment-confirmations to the owner.
- (No other files expected to require changes for a vocabulary-only PR.)

## Telegram interaction

**None today** (defer artifact; no v1 build; vocabulary-only). If a future v1 payment-confirmation surface is built, the owner-side Telegram bot could accept a `/payment` command that shows the latest payment-confirmations (e.g., "/payment 3 pending, 1 confirmed, 1 failed"). The bot would also send a notification when a payment is confirmed (e.g., "Payment confirmed: €42.50 from customer A"). The interaction is operator-facing per charter §3.4; not customer-facing.

## Dependencies

- **Charter §3.1 (explicit-state-transition)**: existing `audit_logs` SQLModel table is the v1 precedent; the `PaymentConfirmation` table extends the same pattern to the *payment-confirmation* dimension with **append-only `PaymentPollAttempt` audit log + state-row `PaymentConfirmation`**.
- **Charter §3.2 (self-hosted + zero-external-dependencies)**: the *polling-without-webhook-or-domain* posture IS the *self-hosted* charter invariant applied to the *no-public-webhook-required* dimension; the v1 reference would substitute YooKassa with the local payment provider.
- **Charter §3.3 (audit-log-immutability)**: the `PaymentPollAttempt` table is append-only (charter §3.3 invariant); the `PaymentConfirmation` table is a state-row (updated on each confirmation).
- **Charter §3.4 (operator-facing)**: the *payment-confirmation* surface is operator-tooling per charter §3.4 invariant; the *polling-pattern* is a deterministic data-fetching primitive, not customer-facing AI.
- **Charter §3.6 (Money: never use binary floats)**: the *amount_eur + currency* fields use `Decimal` (Python `decimal.Decimal` or pydantic `condecimal`) per the existing v1 EUR convention. A future PR would need to specify the exact rounding rule (e.g., 2 decimal places for EUR, half-even rounding).
- **Stack note**: `quueli/yookassa-polling-payments` uses aiogram + Python + Telegram-bot; LE31 v1 already uses aiogram 3 + Python + Telegram-bot; the *polling-pattern* is on-stack (the v1 reference would use a FastAPI background task or a separate cron job).
- **No v1 dependencies today**: this is a v1 forward-looking surface; no v1 code depends on it.

## Open questions

1. **What is the payment provider?** A future PR would need to specify the payment provider (YooKassa = Russian; Stripe / Mollie / local = EU). The `quueli/yookassa-polling-payments` reference uses YooKassa; a future PR would substitute.
2. **What is the polling interval?** A future PR would need to specify the polling interval (e.g., 30 seconds, 5 minutes). A shorter interval is more responsive but uses more API quota.
3. **What is the payment-confirmation lifecycle?** A future PR would need to specify the lifecycle states (e.g., `pending, confirmed, failed, refunded`).
4. **What is the relationship between the v1 `audit_logs` SQLModel table and the v1 `PaymentConfirmation` SQLModel table?** The v1 `audit_logs` is a manual structured event log; the v1 `PaymentConfirmation` is a payment-provider-driven event log. A future PR would need to specify the relationship (e.g., do `PaymentConfirmation` rows auto-create `audit_logs` rows?).
5. **What is the security model?** A future PR would need to specify the API-key-storage (env var, per charter §3.2; not in `PaymentProvider` table; not in source).

## Why this matters

This is the **strongest v1 payment-polling-without-webhook cross-section pick of the 71-pass brainstorm series**. The *yookassa-payments + aiogram + telegram-bot + python + polling-without-webhook* quintuple-primitive maps 1:1 onto the *payment-confirmation* surface that a future v1 PR might add to extend the existing `audit_logs` SQLModel table. The Python + 5-topic + 4★/0⑂ + in-window-by-both-fields stack is **§3.1 + §3.2 + §3.3 + §3.4 + §3.6 ON-PATTERN** for LE31; the *aiogram + python + polling-API + no-public-webhook-required* discipline IS stack-adjacent.

The **polling-without-webhook** discipline extends the existing v1 event-sourcing pattern to the *payment-confirmation* dimension with a deterministic polling primitive. The **separate-accounts-identity** posture (the yookassa reference uses a separate YooKassa merchant account) is the *separate-accounts-identity* charter §3.4 invariant applied to the *owner-vs-payment-provider-relationship* dimension. The **self-hosted + zero-external-dependencies** discipline is the charter §3.2 invariant applied to the *VPS-deployment-without-public-domain* dimension.

**Charter alignment summary:** §3.1 partial (payment-confirmation + polling-pattern + aiogram-on-stack ✓); §3.2 strictly-compatible (polling-without-webhook = self-hosted + zero-external-dependencies); §3.3 ✓ (append-only `PaymentPollAttempt` audit log); §3.4 strong alignment (operator-facing + deterministic polling + non-AI-fallback + observable-evidence); §3.6 ✓ (amount_eur + currency = existing v1 EUR convention with `Decimal`); §3.7 N/A.

---

**LE31 charter alignment summary** (per `le31-conventions/SKILL.md`): §3.1 partial; §3.2 strictly-compatible; §3.3 ✓; §3.4 strong alignment; §3.6 ✓; §3.7 N/A.
