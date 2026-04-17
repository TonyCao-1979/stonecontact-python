from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "local"
    log_level: str = "INFO"
    sc_db_url: str = ""
    enable_scheduler: bool = False
    enable_file_service: bool = False
    enable_auth_integration: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_prefix="", extra="ignore")

