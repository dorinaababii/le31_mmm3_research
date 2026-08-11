# Feature 56 — Walk-In Front-Desk Channel (Two-Way Telegram)

> **Priority**: P3 · **Effort**: L (≤5 days, includes charter revision) ·
> **Source**: brainstorm 2026-08-11 (cross-section pick B) · **Bucket**:
> **v2 owner-pains** (requires charter §5 revision; see Blockers)
> **One-line**: a two-way walk-in / customer-facing Telegram surface
> that extends the cook walk-in pin (33) into a customer-side chat
> channel whose every line is appended to LE31's existing append-only
> chain (OrderItem + a new `CustomerChatLine` table).

## Goal

LE31's existing **33-telegram-walkin-pin** is one-way: the cook (and
the owner) sees the pinned waitlist, but the customer does not see it
and cannot reply. Today, when the customer's guest count changes or
they want to add a name to the waitlist, the only route is a phone
call.

OpenAlex `WhatsApp as a service tool in hospitality` (W7197042220)
provides direct empirical evidence that **messaging channels *are* the
front desk in small hospitality operations**: guests chat to ask "is
there a table for 4 at 20:30?", staff reply, an order is placed or a
waitlist entry is recorded. This is the bigger operator pain than the
existing one-way pin.

The cross-section anchor is `djblack1209-coder/OpenClaw-Bot` (a multi-bot
Telegram ops stack in Python/FastAPI + Tauri/React) — it validates that
the **multi-bot Python/FastAPI + aiogram** stack supports two-way
customer chats while still keeping role-boundary (cook vs. customer)
clean. The competitive precedent is `indmdev/Free-Telegram-Store-Bot`
(146★) — which is what every restaurant is going to copy if LE31
doesn't ship first.

## Scope

**In scope (v2 owner-pains):**

- One new SQLModel table: `CustomerChatLine(id, channel_id,
  customer_handle, line_text, line_kind, ref_order_item_id,
  ref_walkin_pin_id, at, by_role)`. Append-only. `customer_handle` is
  the customer's Telegram @username (not phone number; no PII by
  default). `line_kind` in `('customer_msg', 'cook_reply',
  'system_note')`. `by_role` in `('customer', 'cook', 'system')`.
- One new SQLModel table: `CustomerChannel(id, cook_chat_id,
  opened_at, last_msg_at, status)`. `status` in `('open', 'closed',
  'escalated')`. Tracks the customer-side session.
- Two new Alembic migrations.
- A second aiogram bot (`cook_customer_bot.py`) registered under the
  same Telegram token via `Bot(token).token` rotation OR (preferred) a
  separate token `TELEGRAM_CUSTOMER_BOT_TOKEN` per LE31 deployment.
  The customer's bot is **read-only**: it sees only their own chat and
  cannot browse the menu / floor / owner data.
- A new bot command on the customer bot: `/start` — opens a
  `CustomerChannel` row if none is open; else resumes existing channel.
  Greets with a 1-line "Welcome — answer questions about the waitlist,
  menu, hours. Replies come from the cook in <2 min."
- A new `/menu` command on the customer bot — returns today's menu in
  text, sourced from the `MenuItem` table at request time. Read-only.
- A new `/waitlist` command on the customer bot — returns the
  customer's current position in the walk-list (the pin row from
  feature 33) if they are on it.
- A new `/close` command on the customer bot — closes the channel.
  Either party can issue it; closed channels are append-only after
  closure.
- A new cook-side bridge: when a customer sends `customer_msg`, the
  message is **appended** to `CustomerChatLine` (append-only), then
  forwarded to the cook bot (`cook_bot.py`) with a `[from customer
  @handle]` prefix. The cook replies with a normal Telegram reply; the
  reply is **appended** to `CustomerChatLine` with `by_role='cook'`
  and forwarded back to the customer.
- One new cook-side command `/walkin forward <pin_id> "your message"`
  — forwards a typed message to the customer's channel. Append-only.

**Out of scope (v2 owner-pains; gated by charter revision):**

- **Phone-number-keyed identity (PII)** — the LE31 charter §5 forbids
  PII in v1; v2 will require a charter revision **before** this feature
  ships. Until revised, the customer handle is the Telegram @username
  only; phone numbers are not collected, and `@`handles are not PII by
  GDPR Article 4(1) (pseudonymous data is still personal data but is
  processable under legitimate-interest grounds with documented
  minimisation).
- **Multi-restaurant routing** — single LE31 instance routes customer
  chats to its own cook.
- **Spam filtering / abuse handling** — at the v2 v1 cut, abuse is
  handled by the `escalated` status and the cook's `/walkin block
  <handle>` command (closes the channel and freezes any new ones for 24
  hours for the same `@handle`).
- **Voice messages** — text only at v1.
- **Image attachments** — text only at v1.
- **Auto-translation** — single language at v1, defaulting to the
  cook's locale.

## Description

A walk-in customer opens the LE31 cook's public Telegram customer-bot
(`@le31customerbot`, say) and types `/start`. They see today's menu,
their current waitlist position, and the cook's median reply time. They
ask "is there a table for 4 at 20:30?". The bot appends the message to
the LE31 ledger (`CustomerChatLine` table) and forwards it to the cook.

The cook replies via the existing `cook_bot.py` interface (or a new
`/reply <handle> "text"` command). The reply is appended to the same
ledger (`by_role='cook'`) and forwarded to the customer.

Every line is in the ledger. The audit chain (features 30, 47, 49, 50)
extends seamlessly because the new table is append-only and integrates
with `VoidRationale` for any void-with-reason calls dispatched via this
channel (e.g. cook voids an item ordered via chat → `voided_via_chat`
column reference).

## Data model

```
CustomerChannel    (id, cook_chat_id, opened_at, last_msg_at, status)
                    -- status in ('open', 'closed', 'escalated')

CustomerChatLine   (id, channel_id, customer_handle, line_text,
                    line_kind, ref_order_item_id,
                    ref_walkin_pin_id, at, by_role)
                    -- append-only
                    -- line_kind in ('customer_msg', 'cook_reply', 'system_note')
                    -- by_role in ('customer', 'cook', 'system')
```

`customer_handle` is the Telegram @username (no PII, no phone, no
email). Identifiers are **pseudonymous** under GDPR Article 4(1).

## Implementation steps

1. **Charter revision (blocker)** — revise `PROJECT_CHARTER.md` §5 to
   add a v2 stance on customer-side `customer_handle` pseudonymity.
   Get signed off before code is written.
2. Add `CustomerChannel` and `CustomerChatLine` SQLModel tables to
   `backend/app/models.py`.
3. Add two Alembic migrations.
4. Add `backend/app/bot/customer_bot.py` (NEW) — minimal aiogram v3
   v1 that handles `/start`, `/menu`, `/waitlist`, `/close`. Uses
   `TELEGRAM_CUSTOMER_BOT_TOKEN`.
5. Add `backend/app/bot/customer_bridge.py` (NEW) — the bridge
   between customer_bot (Telegram inbound) and cook_bot (forwarded
   outbound). Appends to `CustomerChatLine` and triggers the forward.
6. Add a `/reply <handle>` command to `backend/app/bot/cook_bot.py` —
   the cook-side endpoint. Appends to `CustomerChatLine` and triggers
   the customer-side send.
7. Add `backend/scripts/list_open_customer_channels.py` — for the
   owner.
8. Add `backend/tests/test_customer_chat_line.py` — append-only tests.
9. Add `backend/tests/test_customer_bot_e2e.py` — bridge tests.
10. Update `backend/README.md` with the customer-bot onboarding
    (per-deployment `TELEGRAM_CUSTOMER_BOT_TOKEN` + customer handle
    allow-list policy).

## Telegram interaction if any

- Two new bots: cook-customer bot (customer-facing) and the existing
  cook-bot (with a new `/reply` and `/walkin forward` command).
- Customer bot commands: `/start`, `/menu`, `/waitlist`, `/close`.
- Cook bot commands added: `/reply <handle> "text"`, `/walkin forward
  <pin_id> "text"`, `/walkin block <handle>`.

## Dependencies

- **Feature 33** `telegram-walkin-pin` — pre-existing; this feature
  extends it.
- **Feature 39** `owner-daily-recap-telegram` — the recap can cite
  `CustomerChatLine` rows in the `evidence_link` extension (feature 55).
- **Feature 47** `decision-rationale-mixin` — `ref_walkin_pin_id`
  requires rationale columns.
- **charter §5 (TBD)** — privacy revision.

No new pip dependencies. aiogram v3 is already imported.

## Open questions

- One bot token or two? Two tokens (`TELEGRAM_BOT_TOKEN` + new
  `TELEGRAM_CUSTOMER_BOT_TOKEN`) is cleaner for permission boundaries;
  one token with role-based dispatcher is cheaper but riskier. Decision
  deferred to charter revision.
- Should the customer-bot allow `/menu` for non-restaurant-hours
  (auto-reply "we open at 18:30 — pre-order here: /reserve")? Decision
  deferred to scope.
- Should `cook_reply` lines be editable by the cook for 60 seconds
  (typical Telegram edit window) before lock-in? **No**: append-only
  is the moat; cook can send a corrected follow-up instead.

## Why this matters

LE31's moat today is the cook-bot + append-only ledger. The moat is
**invisible to the customer side** — the customer is on the phone or
on WhatsApp. The competitive set (`indmdev/Free-Telegram-Store-Bot`,
chat-based stores on Shopify, WhatsApp Business for hospitality) are
moving into this niche with depth we cannot beat by default. The only
defensible move for LE31 is to ship the two-way chat **and** keep the
audit chain — that is the combination no competitor has, and no
competitor can copy without rebuilding their ledger.

This is the **single most novel** of today's three picks. It is also
the one that requires a privacy conversation first; we ship that
conversation before we ship the code.

## Blockers

- **charter §5 revision (PII stance for customer chat)** — see Open
  questions. Without the revision, no code is written.
