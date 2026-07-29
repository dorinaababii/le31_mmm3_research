"""Database engine, session, and SQLModel base.

Uses SQLModel (Pydantic + SQLAlchemy) so the same class is both a DB row
and a request/response model. Works with SQLite (dev) and Postgres (prod).
"""

from sqlmodel import SQLModel, Session, create_engine

from .config import settings

# `echo=False` keeps logs clean; flip to True to see every SQL statement.
engine = create_engine(
    settings.database_url,
    echo=False,
    # Required for SQLite (no-op for Postgres)
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {},
)


def init_db() -> None:
    """Create all tables. For real schema evolution use Alembic (see /db/migrations/)."""
    # Import models so SQLModel.metadata is populated before create_all.
    from . import models  # noqa: F401
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """FastAPI dependency that yields a per-request DB session."""
    with Session(engine) as session:
        yield session