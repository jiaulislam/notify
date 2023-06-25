from pydantic import BaseSettings


class Settings(BaseSettings):
    is_debug: bool

    class Config(BaseSettings.Config):
        env_file = ".env", "prod.env"
        env_file_encoding = "utf-8"


configs = Settings()  # type: ignore
