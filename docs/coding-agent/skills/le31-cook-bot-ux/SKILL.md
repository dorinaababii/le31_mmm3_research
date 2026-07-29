---
name: le31-cook-bot-ux
description: Use whenever designing or reviewing the cook's Telegram bot flows. Defines short-message patterns, large tap targets, undo on the same message, and explicit French wording for non-technical operators.
version: 1.0.0
author: Hermes Agent (research side)
license: MIT
metadata:
  hermes:
    tags: [le31, bot, ux, telegram, nielsen, localisation]
    related_skills: [le31-conventions-coder, le31-arch-patterns, le31-data-correctness]
---

# LE31 Cook Bot UX

## Overview

The cook's Telegram surface is a working tool under time pressure. Optimise for **Visibility of System Status**, **Error Prevention**, **Recognition Rather than Recall**, and **Match the Real World** — Nielsen 10 heuristics #1, #5, #6, #2. (Nielsen, 1994, last reviewed 2024.)

## Standards anchor

- **Nielsen 10 heuristics** for operator UIs.
- **Telegram Bot API** design — `sendMessage`, `answerCallbackQuery`, `InlineKeyboardButton` for every state-changing action.
- **GOV.UK Service Standard** for plain-language operational UX.

## Voice rules

- Plain French, short sentences, second person (`tu` for instructions; `vous` for receipts).
- One message per state change. Never group three transitions.
- Lead with the verb (`Ajoute`, `Confirme`, `Annule`).
- Numbers in EU format (`12,50 €`, dates `dd/mm/yyyy`).
- Emojis only when they replace a redundant icon; one per line maximum.

## Tap interaction

- Every state change uses `InlineKeyboardButton`, never free-form chat.
- Tap targets are full width text on small phones.
- One main action per message. Secondary actions (`Annuler`, `Plus tard`) sit on a second row, single column.
- Confirmation messages include the new state in plain text **above** the buttons, not just inside the button label.

### Canonical templates

```text
3 × Croque-monsieur (prep)
10:42 · Paris

[ + 3 ]  [ − 3 ]  [ prêt ]  [ ↻ undo ]
```

```text
Croque-monsieur 7/10 restants
10:45 · Paris

[ marqué vendu? ]  [ annuler ]
```

`answerCallbackQuery` always returns a short toast that mirrors the new state, not a generic "OK".

## Explicit undo

Every action must be undoable for at least 5 minutes via the same message's "↻ undo" button. After 5 minutes, undo requires owner confirmation. Silent undo is forbidden — the cook must see the trace.

## Recovery from mistakes

- `Annuler` is always present on the message that triggered the action.
- `/status` shows every active batch in compact form, refreshed on demand.
- `Annuler tout` returns to idle and emits a single audit event for the session, not per-tap.

## Concurrency and spam

The cook may tap twice. Every callback handler is idempotent. Duplicate taps:

- run the action once
- show the resulting state in the toast
- do not create duplicate ledger rows

## Auth and allowlist

Restrict every handler to the configured `TELEGRAM_ALLOWED_USERS` set before any state mutation. Replies with a polite refused message otherwise.

## Localisation and accessibility

- Plain French and basic English.
- Numerical formats obey the EU.
- For the cook, never depend on colour; rely on plain text labels and button ordering.

## Anti-patterns (refuse)

- Long instructions in chat.
- Multi-tap wizards with FSM state hidden from the user.
- Auto-progressing stations after a timer.
- Free text commands for state mutation.
- Silent state changes (no toast, no follow-up message).

## Verification checklist

- [ ] Every state-changing action uses `InlineKeyboardButton`.
- [ ] Button labels are short, plain French.
- [ ] Confirmation message shows the new state in plain text.
- [ ] "Annuler" is present at the action site.
- [ ] Duplicate taps are idempotent (tested).
- [ ] Non-allowlisted chat IDs refused.
- [ ] Numeric formatting is EU in every visible message.
