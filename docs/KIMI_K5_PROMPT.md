# Kimi K5 — Implementation Prompt

> **What this is**: a ready-to-paste prompt for handing off the implementation phase
> from Hermes (research) to Kimi K5 (coding). Read it before sending — feel free to
> add/remove context based on what Kimi needs.

---

## The prompt (paste everything below the line into Kimi K5)

---

You are picking up a restaurant-operations project after the research phase is
complete. **Read first, then code.** The repo is already cloned locally on your
machine.

## 1. Read these files in order — they are the contract

```
README.md                                         ← project pitch
docs/INDEX.md                                     ← master index, build order
docs/HANDOFF.md                                   ← ⭐ the document you must read first
docs/research/09-recommended-stack.md             ← architecture + DDL sketch
docs/research/00-landscape-overview.md            ← why we're building fresh
docs/features/02-order-taking.md                  ← Feature 02 spec
docs/features/03-kitchen-stock-tracker.md          ← Feature 03 spec (the killer one)
docs/features/04-menu-photo-bot.md                ← Feature 04 spec (OCR + Telegram)
docs/features/05-payment-tip-reconciliation.md    ← Feature 05 spec
docs/features/06-guest-demographics.md            ← Feature 06 spec
docs/features/07-demand-estimation.md             ← Feature 07 spec
backend/README.md                                 ← backend setup
backend/app/models.py                             ← existing SQLModel schema
backend/app/main.py                               ← existing FastAPI app
backend/app/routers/tables.py                     ← reference router (Feature 01 done)
backend/app/bot/cook_bot.py                       ← bot stub
```

## 2. What exists already

- A working static mock-up at `index.html` (open in browser, no server needed).
- A runnable FastAPI skeleton with one router (`tables`) and the full schema.
- A bot stub with FSM states defined but no OCR wiring.

## 3. What you build — in this order

The features are already prioritized in `docs/INDEX.md`. Build them in this order:

1. **Feature 02** — Order router (`backend/app/routers/orders.py`)
2. **Feature 03** — Stock router (`backend/app/routers/stock.py`) + wire into order close
3. **Feature 04** — Wire OCR into `backend/app/bot/cook_bot.py` (RapidOCR + LLM call)
4. **Feature 05** — Bills router (`backend/app/routers/bills.py`) with derived tip
5. **Feature 06** — Reports router (`backend/app/routers/reports.py`)
6. **Feature 07** — Forecast service (`backend/app/services/forecast.py`)

For each feature:
- Re-read its spec file in `docs/features/`.
- Implement end-to-end: model (if new) → router → bot integration (if applicable) → test manually with `curl` or the mock-up.
- Check it off in `docs/INDEX.md`.
- Commit & push to GitHub.

## 4. Hard constraints (do NOT violate)

| Constraint | Why |
|---|---|
| Build on the existing FastAPI app. Don't add a new framework. | Architecture decision from research. |
| `StockEntry` is append-only. Never UPDATE or DELETE rows. | The ledger pattern is the whole point. |
| Tip is **derived** as `total_paid − subtotal_items − subtotal_tax`. No manual entry. | The user wants this specifically. |
| v1 guest demographics: `party_size`, `adults`, `children` only. Skip gender. | Privacy + data-entry friction. |
| v1 menu: flat list per category. No modifiers UI. | Out of scope. |
| No multi-tenancy. | Single restaurant. |
| No tip pooling in v1. | Out of scope. |
| Use `Decimal` for money, never `float`. | Exact arithmetic. |

## 5. Conventions

- **Money** — `Decimal` from `decimal.Decimal`, with `max_digits=10, decimal_places=2` on the SQLModel field.
- **Time** — always UTC. Use `datetime.now(timezone.utc)`.
- **Timestamps in DB** — `DateTime(timezone=True)` columns.
- **HTTP errors** — raise `HTTPException(status_code, detail)`.
- **Pydantic** — use SQLModel classes (they ARE Pydantic) for request/response models.
- **Imports** — use `from app.x import y` style (not relative `from ..x import y`) for top-level app code; relative imports are fine inside the `app/` package.
- **Config** — read from `settings` (`app.config`); don't hard-code secrets.

## 6. Tools you have

- `git` for version control (push to `origin main` on the repo).
- `uvicorn` for running the API.
- `sqlite3` for dev DB inspection.
- `curl` + <http://localhost:8000/docs> for testing endpoints.
- The Telegram bot token is already in `.env` on this machine if you need it.

## 7. How to verify your work

For each feature:
1. Start the API: `uvicorn app.main:app --reload`
2. Open <http://localhost:8000/docs> — your new endpoints should appear.
3. Hit them with `curl` or through the OpenAPI "Try it out" UI.
4. If a feature has a UI impact, also click through `index.html`.
5. When green, commit with a message like `Feature 02: order router + visit close`.

## 8. When you're stuck

- **Re-read the spec file** — they're written as contracts, not suggestions.
- **Check `docs/research/`** — the architecture & rationale is documented.
- **Look at `backend/app/routers/tables.py`** — it shows the conventions for a working router.
- **Ask the user** the open questions in `docs/INDEX.md` only if a decision is blocking you. Otherwise use the defaults.

## 9. Don't

- Don't refactor the schema without a strong reason.
- Don't add new dependencies unless absolutely needed (justify in the commit message).
- Don't break the `index.html` mock-up.
- Don't write tests for trivial helpers; focus on end-to-end verification.

---

## Ready to send

Copy everything between the `---` markers and paste it into Kimi K5 as the system or first user message. If Kimi supports a project-files context, attach:

- `docs/HANDOFF.md`
- `docs/INDEX.md`
- `backend/README.md`

So it has the contract in front of it from turn 1.