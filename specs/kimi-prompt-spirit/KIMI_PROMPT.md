# Kimi K3 Prompt — LE31 Spirit

Copy the block and paste it as the first user message.

---

You are building a restaurant operations app for a single small restaurant (≤40 seats). The whole system must do these six things well:

1. Waiter takes an order from a phone or tablet.
2. Cook receives the order on Telegram and knows what to prepare.
3. Cook confirms ready on Telegram. Waiter gets a Telegram notification.
4. Waiter brings the order, takes payment, the tip is derived (never typed in).
5. Owner opens one page and sees today's sales, tips, low-stock items, and forecasts.
6. When an item runs out, the waiter sees it immediately and can offer something else.

The killer feature is **stock that cannot be quietly edited**. Every slice sold, every gram wasted, every prep batch written — one row in an append-only `StockEntry` table. Current stock is the sum of entries. Never update posted rows. If the cook says he baked 8 pieces of cake, that promise is auditable.

Hard rules. No exceptions.

- Stack: Python 3.13, FastAPI, SQLModel, Postgres in prod (SQLite for dev), aiogram v3. Adding a dependency needs a checkpoint commit and a written reason.
- Money is integer cents (or Decimal). Never float.
- Time is `TIMESTAMPTZ`. Render business dates in `Europe/Paris`.
- v1 customer data is only `party_size`, `adults`, `children`. No identity.
- Closed orders and bills are immutable. Corrections are compensating events.
- Every operational state change is an explicit user action. No silent auto-progress.
- No customer-facing AI. All AI is owner- or operator-facing only.
- Telegram callbacks are idempotent. Duplicate taps do the work once.

Before you build anything, answer in one line each:

1. Which restaurant pain does it answer?
2. Can the non-technical owner run it without surprise?
3. Does it fit the fixed stack without new dependencies?
4. Does it violate any rule above?
5. Is it v1, v2, or v2-AI scope?
6. Build cost vs. daily pain avoided?
7. What evidence stops it? Can it be disabled? What does it cost to remove?

Decision: build, experiment, defer, or reject. State the failed checks first.

Read in this order before coding: `INDEX.md`, `PROJECT_CHARTER.md`, `HANDOFF.md`, `coding-agent/skills/le31-conventions-coder/SKILL.md`, the active feature contract under `features/`, the active slice `*-HANDOFF.md`. Then mirror back the slice ID, the files you will touch, the verification commands, the rollback path, and the human-approval triggers you will satisfy (money/stock schema, auth, new dependencies). Confirm or correct each. Then begin.

A feature is done only after the end-to-end waiter/cook/owner flow was actually run, the rows were inspected, reconciliation matched to zero, lint/SAST/dependency/secrets scans were clean, and a non-author reviewer signed off.

If a charter, feature file, or current code disagree, stop and report the exact conflict. Do not silently pick a side. If a source is blocked, label it blocked and propose an alternative. Never invent a number, a quote, or a source you did not read.
