# Feature 291 — `Volcarone/badcop` v1 owner-supplier-payment-chasing-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v1 (attach to `le31 v1 — Core MVP` P-HMM-3 as the parent of the sub-issue, or to `le31 Research` P-HMM-1 if v1 project is reserved for already-spec'd work — see pipeline note)
> **Date:** 2026-10-07
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/291-Volcarone-badcop-mit-chase-unpaid-invoices-with-escalating-reminder-ladder-accounts-identity-csv-in-email-out-zero-dependencies-self-stay-good-cop-v1-owner-supplier-payment-chasing-vocab.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/291-Volcarone-badcop-mit-chase-unpaid-invoices-with-escalating-reminder-ladder-accounts-identity-csv-in-email-out-zero-dependencies-self-stay-good-cop-v1-owner-supplier-payment-chasing-vocab-HANDOFF.md`
> **Source daily brainstorm:** `/opt/data/le31-brainstorm-2026-10-07.md` (pass 70, pick B — **parent override** of subagent's `ALPHAMAN-0/burgerCodeEmployes` 5KB-tiny pick; `badcop` is 1218 KB substantial with 14 topics and stronger on-pattern alignment to LE31 supplier-orders + payment-tip-reconciliation cluster)
> **Parent-verified via:** direct GitHub API GET `/repos/Volcarone/badcop` at `/opt/data/le31-brainstorm-2026-10-07/verify_Volcarone_badcop.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed; v1 owner-supplier-payment-chasing reference is a future-extension signal)

## Goal

Surface a v1 owner-supplier-payment-chasing vocabulary reference for **escalating-reminder-ladder on unpaid invoices + separate-accounts-identity + CSV-in/email-out + zero-dependencies + self-stays-the-good-cop** as a forward-looking pattern for any future LE31 v1 surface that exposes owner-facing supplier-invoice-chasing discipline (escalating reminder ladder, separate identity to preserve customer relationship, deterministic scheduling, audit trail of who-said-what-when).

## Evidence / JTBD

**Evidence classification:** inferred. The *escalating-reminder-ladder + separate-accounts-identity + CSV-in/email-out + zero-dependencies* discipline is forward-looking for any future LE31 v1 owner-supplier-payment-chasing surface; no LE31 v1 surface today has supplier-invoice-chasing. **Confidence: high** (1★/0⑂ + 1218 KB modest + Python on-stack ✓ + 14-topic array including `accounts-receivable + automation + cli + dunning + freelance + invoice + invoice-reminder + invoicing + late-payment + payment-reminder + python + self-hosted + small-business + smtp` + 0 customer-facing AI + in-window by BOTH fields = strongest v1 owner-supplier-payment-chasing cross-section pick of the 70-pass series; **parent override** of subagent's `ALPHAMAN-0/burgerCodeEmployes` 5KB-tiny pick because `badcop` has 14 topics vs 10, 1218 KB vs 5 KB, and stronger on-pattern alignment to LE31's existing supplier-orders feature 16 + payment-tip-reconciliation feature 05).

**When** the LE31 owner wants to chase unpaid supplier invoices without losing the supplier relationship, **the owner wants to** send a polite first reminder, a firmer second reminder, a final-notice third reminder, all from a separate `accounts@` identity (so the supplier does not feel personally pressured by the owner), and a CSV-driven input + email-driven output with zero dependencies, **but struggles because** the existing v1 `SupplierOrder` SQLModel table is an order tracker with no payment-chasing surface, no reminder ladder, no separate-identity discipline, **so that** the owner either chases invoices personally (relationship-damaging) or forgets to chase them (cash-flow-damaging). The *escalating-reminder-ladder + separate-accounts-identity + CSV-in/email-out + zero-dependencies* discipline IS the *owner-facing-clarity + explicit-state-transition + non-AI-fallback* charter §3.1 + §3.4 invariant applied to the *supplier-payment-chasing* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *escalating-reminder-ladder + separate-accounts-identity + CSV-in/email-out + zero-dependencies + self-stays-the-good-cop* quintuple-primitive as a candidate vocabulary for any future LE31 v1 owner-supplier-payment-chasing surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres mapping for each primitive.
- Record the §3.1/§3.2/§3.3/§3.4/§3.7 alignment per `le31-conventions/SKILL.md`.

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No SMTP integration; v1 owner-supplier-payment-chasing is forward-looking.
- No reminder-ladder on the existing `SupplierOrder` SQLModel table.
- No separate-accounts-identity discipline on the existing v1 owner Telegram bot.

## Description

`Volcarone/badcop` is a **small-business supplier-invoice-chasing reference** with the following properties:
- **Chase unpaid invoices with an escalating reminder ladder from a separate accounts@ identity** — the central discipline is the *escalating reminder ladder* (1st reminder = polite, 2nd = firmer, 3rd = final-notice) sent from a *separate identity* so the supplier does not feel personally pressured by the owner.
- **CSV in, email out, zero dependencies** — the input is a CSV of unpaid invoices, the output is SMTP-sent email, the runtime has zero Python dependencies (uses only the standard library).
- **You stay the good cop** — the explicit framing is that the *bad cop* (the automated reminder ladder) does the chasing so the *good cop* (the owner) preserves the supplier relationship.
- **MIT permissive + 1218 KB modest** — small enough to be a vocabulary reference, not a production codebase.
- **14-topic array** including `accounts-receivable + automation + cli + dunning + freelance + invoice + invoice-reminder + invoicing + late-payment + payment-reminder + python + self-hosted + small-business + smtp` = the strongest v1 owner-supplier-payment-chasing cross-section topic-coverage of the 70-pass series.

The vocabulary is a strong §3.4-alignment signal for any future LE31 v1 owner-supplier-payment-chasing surface because:
- The *escalating-reminder-ladder* IS the §3.1 *explicit-state-transition* charter invariant applied to the *supplier-payment* dimension (each reminder is an explicit state transition, not an automatic one).
- The *separate-accounts-identity* IS the §3.4 *non-AI-fallback* charter invariant applied to the *owner-vs-relationship* dimension (the owner stays the good cop; the bad cop is the deterministic reminder ladder).
- The *CSV-in/email-out + zero-dependencies* IS the §3.2 *self-hosted + zero-external-dependencies* charter invariant applied to the *supplier-payment-chasing* dimension.
- The *dunning + late-payment* posture IS the §3.7 *operator-decision-rationale-audit-trail* charter invariant applied to the *supplier-payment* dimension (every reminder sent is a record of why the owner is escalating).

## Data model

```
SupplierOrder          (id, supplier_id, items, total_eur, status, due_date, created_at)  # existing — feature 16
SupplierInvoice        (id, supplier_order_id, invoice_number, amount_eur, due_date, status, paid_at)  # NEW
ReminderLadderStep     (id, supplier_invoice_id, step_number, template_key, sent_at, sender_identity, recipient_email)  # NEW — append-only
ReminderTemplate       (id, template_key, subject, body_text, escalation_tone)  # NEW — references the existing 3 templates (polite, firmer, final-notice)
ReminderAuditEntry     (id, supplier_invoice_id, action, actor, occurred_at, metadata_json)  # NEW — append-only
```

The `ReminderLadderStep + ReminderAuditEntry` tables are **append-only** per charter §3.3. Every reminder sent is a new `ReminderLadderStep` row + a new `ReminderAuditEntry` row; never UPDATE or DELETE. The `sender_identity` column enforces the *separate-accounts-identity* discipline (the row can only be inserted with a `sender_identity` that is *not* the owner's personal identity; the v1 owner Telegram bot would need a separate SMTP credential for `accounts@restaurant.example`).

## Implementation steps

**This is a defer artifact. No code is written today.** When (and if) a future v1 PR adopts the *escalating-reminder-ladder + separate-accounts-identity* discipline, the following files would be touched:

- `/opt/data/le31_mmm3_research_work/backend/app/models/supplier_invoice.py` — new SQLModel `SupplierInvoice` + `ReminderLadderStep` + `ReminderTemplate` + `ReminderAuditEntry` tables.
- `/opt/data/le31_mmm3_research_work/backend/app/services/reminder_ladder.py` — pure-Python escalating-reminder-ladder scheduler (no external scheduler dependency; uses a `cron` job + a deterministic state machine).
- `/opt/data/le31_mmm3_research_work/backend/app/services/smtp_sender.py` — pure-stdlib SMTP sender with separate-accounts-identity discipline (uses `smtplib` from the standard library only).
- `/opt/data/le31_mmm3_research_work/backend/app/templates/reminder_polite.txt` + `reminder_firmer.txt` + `reminder_final_notice.txt` — three reminder templates (no PII in templates; placeholders only).
- (No other files expected to require changes for a vocabulary-only PR.)

## Telegram interaction

**None today** (defer artifact; no v1 build; vocabulary-only). If a future v1 owner-supplier-payment-chasing surface is built, the owner-side Telegram bot could surface reminder-ladder events with their state (e.g., "Reminder sent: supplier X invoice #1234 polite tone. Next reminder in 7 days. Sender: accounts@. Recipient: billing@supplier.com."). The bot surfaces *what was sent* but does NOT send the reminders directly (the SMTP sender is the *bad cop*; the Telegram bot is the *good-cop observer*).

## Dependencies

- **Charter §3.1 (explicit-state-transition)**: existing `SupplierOrder` SQLModel table (feature 16) is the v1 precedent; the `SupplierInvoice + ReminderLadderStep` tables extend the same pattern to the *supplier-payment* dimension with **append-only state transitions per reminder**.
- **Charter §3.3 (audit-log-immutability)**: existing `audit_logs` SQLModel table is the v1 append-only ledger; the `ReminderAuditEntry` table is a derived view that records every reminder-sent event.
- **Charter §3.4 (operator-facing)**: the *owner-supplier-payment-chasing* surface is operator-tooling per charter §3.4 invariant; the *separate-accounts-identity* discipline is the *non-AI-fallback* posture (no AI to escalate or de-escalate; the ladder is deterministic).
- **Stack note**: `smtplib` is in the Python standard library (LE31 v1 already uses it implicitly via `fastapi-mail` or similar). The discipline is *zero-external-dependencies* (no SendGrid, no Mailgun, no SES). A future PR would need to specify the SMTP provider (or self-hosted Postfix).
- **No v1 dependencies today**: this is a v1 forward-looking surface; no v1 code depends on it.

## Open questions

1. **What is the reminder-ladder schedule?** The discipline uses an *escalating reminder ladder* but the specific schedule (7 days, 14 days, 21 days?) is a policy decision. A future PR would need to specify the schedule.
2. **What is the supplier opt-out?** A supplier may reply "stop sending reminders; I have a payment plan." A future PR would need to specify the opt-out mechanism (reply-to with a magic link, an email address that auto-unsubscribes, etc).
3. **What is the relationship to existing v1 `StockEntry` event-sourcing?** The `SupplierOrder` (feature 16) has no `paid_at` field; a future PR would need to add it. The *append-only StockEntry* invariant would need to be extended to *append-only SupplierPayment* events.
4. **What is the relationship to the v1 payment-tip-reconciliation (feature 05)?** Feature 05 is *customer* payment (diner pays the restaurant); this is *supplier* payment (restaurant pays the supplier). They are mirror images but separate flows. A future PR would need to specify the relationship.
5. **What is the GDPR/privacy boundary?** A future PR that adopts the *separate-accounts-identity* discipline would need to ensure that the supplier email is used only for chasing, not for marketing. Per charter §3.7 *store only data needed for restaurant operations*, the supplier email is needed for chasing; it would not be used for any other purpose.

## Why this matters

This is the **strongest v1 owner-supplier-payment-chasing cross-section pick of the 70-pass brainstorm series** (and the **parent override** of the subagent's `ALPHAMAN-0/burgerCodeEmployes` 5KB-tiny pick — `badcop` is 1218 KB substantial with 14 topics, stronger on-pattern alignment to LE31's existing supplier-orders feature 16 + payment-tip-reconciliation feature 05, and a closer match to the *single-owner single-restaurant* charter §3.1 invariant). The *escalating-reminder-ladder + separate-accounts-identity + CSV-in/email-out + zero-dependencies + self-stays-the-good-cop* quintuple-primitive maps 1:1 onto the *owner-facing-clarity + non-AI-fallback + explicit-state-transition* surface that a future v1 PR might add to extend the existing `SupplierOrder` SQLModel table.

The **escalating-reminder-ladder** discipline extends the v1 explicit-operator-state-transition pattern to the *supplier-payment-chasing* dimension. The **separate-accounts-identity** discipline is the *non-AI-fallback* posture for owner-facing communication (the owner stays the *good cop*; the reminder ladder is the *bad cop*). The **CSV-in/email-out + zero-dependencies** discipline aligns with the v1 charter §3.2 *self-hosted + zero-external-dependencies* invariant. The **dunning + late-payment** posture is a classic accounts-receivable discipline that maps to the v1 `SupplierOrder.status` field.

**Charter alignment summary:** §3.1 partial (escalating-reminder-ladder + CSV-in/email-out ✓; separate-accounts-identity OFF-§3.1 = explicit charter-decision needed for v1); §3.2 strictly-compatible (MIT permissive + zero-external-dependencies); §3.3 ✓ (append-only `ReminderLadderStep + ReminderAuditEntry` = stronger than §3.3 raw `audit_logs`); §3.4 strong alignment (separate-accounts-identity + non-AI-fallback + observable-evidence + the owner stays the good cop); §3.7 partial (supplier opt-out + GDPR boundary = explicit charter-decision needed).
