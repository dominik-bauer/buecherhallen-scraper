from models import BuechhallenAccount
from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings for the FastAPI app.

    Loads values from environment variables or a .env file.
    """

    url_login: AnyUrl = Field(  
        description="Login page URL for Buecherhallen service",
    )

    url_loans: AnyUrl = Field( 
        description="API endpoint URL returning the current loans as JSON",
    )

    ttl_minutes: int = Field(
        default=300,
        gt=0,
        description="Cache time-to-live in seconds (must be positive)",
    )

    requests_timeout_sec: int = Field(
        default=10,
        gt=0,
        le=60,
        description="HTTP request timeout in seconds (1–60)",
    )

    # --- Account configuration ---
    accounts: list[BuechhallenAccount] = Field( # pyright: ignore[reportUnknownVariableType]
        default_factory=list,
        description="List of Buecherhallen accounts for multi-account support",
    )

    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        validate_default=True,
    )


# Create a single global instance
CONF = Settings() # pyright: ignore[reportCallIssue]
