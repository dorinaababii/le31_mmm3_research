# LE31 mmm3 — Built (staging folder)

> Status: this directory is a **proposed repo's contents, staged for hand-off**. It is not a live repo yet.

LE31 is a two-role restaurant operations system for a single small restaurant:

- **Waiter web UI** (FastAPI + minimal HTML/HTMX)
- **Cook Telegram bot** (aiogram v3)
- **Append-only `StockEntry` ledger** as the source of truth for prepared-item stock

This folder bundles the building blocks that the new `le31_mmm3_built` repo will need on day 1.

## Contents

| Path | Purpose |
|---|---|
| `HANDOFF.md` | Build-side tour: where each thing lives, what to do next |
| `KIMI_K3_PROMPT.md` | Paste-in instructions for the coding agent |
| `backend/` | FastAPI app, SQLModel models, aiogram skeleton, .env.example, requirements.txt |
| `index.html` | Waiter/owner UI mock-up (place at repo root when copied) |
| `coding-agent/` | LE31 skill pack (drop into the build repo's `skills/le31-pack/` and gitignore it locally) |

## Hard rules for the build

- Stack: Python 3.13, FastAPI, SQLModel, Postgres in prod (SQLite for dev), aiogram v3.
- Single-currency EUR. No floats in money arithmetic. Use integer minor units.
- `StockEntry` is append-only. Database role revokes UPDATE/DELETE on posted rows in production.
- Time is `TIMESTAMPTZ`. Business dates render in `Europe/Paris`.
- v1 customer data: only `party_size`, `adults`, `children`. Identity is not stored.
- Telegram callbacks must be idempotent — duplicate taps do the work once.

For the full set of standards and gates, see the LE31 skill pack under `coding-agent/skills/`.

## How to create the new repo

1. Create `dorinaababii/le31_mmm3_built` on GitHub (public or private — your call).
2. Clone it locally.
3. Copy the four paths above into the root of the new repo:
   - `HANDOFF.md`
   - `KIMI_K3_PROMPT.md`
   - `backend/`
   - `index.html`
   - `coding-agent/` → rename or move into `skills/le31-pack/` and `.gitignore` locally.
4. Wire Hermes `config.yaml` `external_dirs` to the `skills/le31-pack/` folder.
5. Restart Hermes and run `hermes skills list | grep le31-` to confirm the pack is loaded.

For details, see `HANDOFF.md`.
