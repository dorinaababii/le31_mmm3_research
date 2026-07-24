"""FastAPI application entry point.

Run (dev):
    cd backend
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Run (prod):
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 2

Then open http://localhost:8000/ for the mock-up, or
http://localhost:8000/docs for the auto-generated OpenAPI docs.
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import settings
from .db import init_db
from .routers import tables

app = FastAPI(
    title="Restaurant API",
    description="Dining-service side of the restaurant app. Cook side is the Telegram bot (see app/bot/).",
    version="0.0.1",
    debug=settings.debug,
)

# CORS — generous in dev, restrict in prod
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.debug else ["https://your-domain.example"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(tables.router)


@app.on_event("startup")
def on_startup() -> None:
    """Create DB tables on startup. Replace with Alembic for prod."""
    init_db()


@app.get("/api/health")
def health() -> dict:
    """Liveness probe."""
    return {"status": "ok", "app": settings.app_name, "version": app.version}


# ───── Serve the mock-up ─────
# The mock-up is at the repo root: ../index.html
# In production this would be a built React app at /static/.
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_STATIC_DIR = _REPO_ROOT / "index.html"
if _STATIC_DIR.exists():
    # Serve as a single-file static site at /
    app.mount("/", StaticFiles(directory=str(_STATIC_DIR.parent), html=True), name="ui")
else:
    @app.get("/")
    def root_fallback() -> dict:
        return {
            "message": "Mock-up not found. See /docs for the API or /api/health for liveness.",
            "hint": f"Expected {_STATIC_DIR}",
        }