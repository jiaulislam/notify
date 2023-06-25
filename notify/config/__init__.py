from pydantic import BaseSettings, EmailStr, IPvAnyAddress


class Settings(BaseSettings):
    is_debug: bool
    smtp_server: IPvAnyAddress
    smtp_outgoing_port: int
    smtp_email: EmailStr
    smtp_password: str

    class Config(BaseSettings.Config):
        env_file = ".env", "prod.env"
        env_file_encoding = "utf-8"


configs = Settings()  # type: ignore
