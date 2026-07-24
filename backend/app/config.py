"""Application settings, loaded from environment / .env file."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ───── App ─────
    app_name: str = "restaurant"
    debug: bool = True
    secret_key: str = "change-me-in-prod"

    # ───── Database ─────
    # Default to SQLite for dev. Override with: DATABASE_URL=postgresql+psycopg://user:pass@host:5432/dbname
    database_url: str = "sqlite:///./restaurant.db"

    # ───── Telegram bot ─────
    telegram_bot_token: str | None = None  # set via .env
    telegram_allowed_user_ids: list[int] = []  # cook + manager IDs

    # ───── LLM (for menu OCR post-processing) ─────
    llm_api_key: str | None = None
    llm_model: str = "gpt-4o-mini"  # or "claude-3-5-haiku-latest", "gemini-1.5-flash", etc.
    llm_base_url: str | None = None  # for OpenAI-compatible endpoints (e.g. local Ollama)


settings = Settings()