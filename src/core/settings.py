# from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="src/core/.env", env_file_encoding="utf-8", extra="ignore"
    )

    # database_dsn: PostgresDsn
    # redis_dsn: RedisDsn
    database_url: str
    redis_url: str


settings = Settings()
