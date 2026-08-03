# Backend — Restaurant App (skeleton)

Python 3.11+ · FastAPI · SQLModel · aiogram · Postgres/SQLite

## Quick start (dev, SQLite)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # edit values if needed
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open:
- Mock-up: <http://localhost:8000/>
- API docs: <http://localhost:8000/docs>
- Health:  <http://localhost:8000/api/health>

## Layout

```
backend/
├── app/
│   ├── main.py             ← FastAPI app entry point
│   ├── config.py           ← Settings (pydantic-settings, reads .env)
│   ├── db.py               ← Engine, session, init_db()
│   ├── models.py           ← SQLModel classes (table=True)
│   ├── routers/
│   │   └── tables.py       ← /api/tables endpoints (feature 01)
│   └── bot/
│       └── cook_bot.py     ← aiogram bot stub (feature 04)
├── .env.example
├── requirements.txt
├── Dockerfile              ← TODO
└── README.md
```

## Schema

Models in `app/models.py` mirror the DDL sketch in
[`../research/09-recommended-stack.md`](../research/09-recommended-stack.md).
See that file for the full entity-relationship picture.

Key tables:
- `menu_item`, `batch`, `stock_entry` — the killer feature (prepared-item stock ledger)
- `table_`, `visit`, `order_item` — dining flow
- `bill`, `derived_tip`, `payment` — payment + tip
- `shift` — end-of-shift cash reconciliation

## Roadmap

What's done: skeleton, models, basic tables router, bot stub.

What to build next (priority order — see `../INDEX.md` for full list):
1. **Feature 02** — Order router: add/update/bump order items
2. **Feature 03** — Stock router: post StockEntry on order close, mark sold-out
3. **Feature 04** — Wire up menu photo OCR in `cook_bot.py`
4. **Feature 05** — Bill router + derived tip + shift close
5. **Feature 06** — Reports router (manager dashboard)
6. **Feature 07** — Forecast (simple 14-day average)

## Production notes

- **Replace `init_db()` with Alembic migrations** before going to prod.
- **Don't serve `index.html` from FastAPI** in prod — build a real frontend and serve it via nginx or behind a CDN.
- **Set a real `SECRET_KEY`** (long random string).
- **Restrict CORS origins** in `app/main.py`.
- **Lock down the bot** by populating `TELEGRAM_ALLOWED_USER_IDS`.