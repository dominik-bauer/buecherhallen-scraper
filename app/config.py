import json
from typing import Any, Optional

from models import BuechhallenAccount
from pydantic import AnyUrl, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings for the FastAPI app.

    Loads values from environment variables or a .env file.
    """

    # --- URL configuration ---
    url_login: AnyUrl = Field(  # type: ignore[assignment]
        default="https://www.buecherhallen.de/login.html",
        description="Login page URL for Buecherhallen service",
    )

    url_media: Optional[AnyUrl] = Field(
        default=None,
        description="Media page URL for accessing digital content",
    )

    url_logout: Optional[AnyUrl] = Field(
        default=None,
        description="Logout page URL for ending the session",
    )

    # --- Timeout configuration ---
    ttl_seconds: int = Field(
        default=300,
        gt=0,
        description="Session time-to-live in seconds (must be positive)",
    )

    requests_timeout_sec: int = Field(
        default=10,
        gt=0,
        le=60,
        description="HTTP request timeout in seconds (1–60)",
    )

    # --- Account configuration ---
    accounts: list[BuechhallenAccount] = Field(
        default_factory=list,
        description="List of Buecherhallen accounts for multi-account support",
    )

    # --- Custom validator for accounts ---
    @field_validator("accounts", mode="before")
    @classmethod
    def parse_accounts_json(cls, value: Any) -> Any:
        """
        Allow accounts to be provided as a JSON string in environment variables.

        Example:
            LOGIN_DATA_JSON='[{"displayname": "Dominik", "username": "23user12", "password": "secret"}]'
        """
        parsed = json.loads(value)
        return [BuechhallenAccount(**v) for v in parsed]

    # --- Model configuration ---
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        validate_default=True,
    )


# Create a single global instance
settings = Settings()
