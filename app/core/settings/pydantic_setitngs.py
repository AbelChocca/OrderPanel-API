from pydantic_settings import BaseSettings, SettingsConfigDict

from typing import List

class Settings(BaseSettings):
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str

    ALLOW_ORIGINS: List[str]

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

