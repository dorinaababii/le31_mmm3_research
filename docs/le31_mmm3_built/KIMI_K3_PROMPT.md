# Kimi K3 Paste-in Prompt

> Copy the block between the markers and paste it into the new agent's first user message.

---

You are picking up the LE31 restaurant operations project. This is a two-role system for one small restaurant: a waiter web UI (FastAPI + minimal HTML/HTMX) and a cook Telegram bot (aiogram v3). The killer feature is an append-only `StockEntry` ledger as the source of truth for prepared-item stock. Single-currency EUR. Owner is non-technical.

Read first, in this order:

1. `docs/PROJECT_CHARTER.md`
2. `docs/HANDOFF.md` (this repo)
3. `docs/features/<id>-<name>.md` for the active slice
4. `coding-agent/skills/le31-conventions-coder/SKILL.md`
5. `coding-agent/skills/le31-v1-feature-pattern/SKILL.md` (if present)
6. The active `*-HANDOFF.md` slice contract, if one exists.

Add the other `coding-agent/skills/` files only when the slice names them.

Hard constraints (any violation requires a written justification in the commit):

- Stack: Python 3.13, FastAPI, SQLModel, Postgres (SQLite for dev), aiogram v3. New dependency = checkpoint commit + named use + trade-off note.
- No float in money arithmetic. Use integer minor units or `Decimal`.
- Time is `TIMESTAMPTZ`. Business dates render in `Europe/Paris`.
- `StockEntry` and money event tables are append-only. UPDATE/DELETE revoked on the prod role.
- v1 customer data: only `party_size`, `adults`, `children`. No identity stored.
- Telegram callbacks are idempotent. Use `InlineKeyboardButton`, not free-text commands, for every state change.
- No customer-facing AI.

Before declaring a feature done:

- Run `ruff check .`, `mypy --strict app/`, `bandit -r app/ -ll`, `pip-audit --strict`, `gitleaks detect`.
- Migrations replay forward/back/forward with the app booting.
- Append-only is enforced at the DB role in production.
- Reconciliation: `SUM(stock_entry.qty_delta)` matches the derivation view, ±0 cents on money.
- Happy + failure paths recorded with evidence under `coding-agent/evidence/<slice-id>/`.

Stop and ask if:

- The read-first list is missing a needed file.
- Charter, feature file, or current code disagree and the resolution is not documented.
- The slice requires a new dependency, model, or migration outside the active contract.
- Verification fails twice on the same root cause.

Before coding, mirror back:

- The slice ID and goal.
- The files you intend to touch.
- The verification commands and the rollback path.
- The human-approval triggers you will satisfy (money/stock schema, auth, dependencies).

Then begin.
