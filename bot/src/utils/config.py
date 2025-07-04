from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    DEEPSEEK_API_KEY: str

    model_config = SettingsConfigDict(env_file = '/app/.env')


settings = Settings()
