from pydantic_settings import BaseSettings, SettingsConfigDict

from typing import List

class Settings(BaseSettings):
    # DB
    DATABASE_URL: str
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str

    # sendgrid
    SENDGRID_API_KEY: str
    SENGRID_API_KEY_ID: str
    SENGRID_API_KEY_NAME: str

    FROM_EMAIL: str

    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str

    ALLOW_ORIGINS: List[str]

    KAFKA_BOOTSTRAP_SERVERS: str
    KAFKA_CLIENT_ID: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

