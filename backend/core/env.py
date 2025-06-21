from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import dotenv_values
import os

class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

    SECRET_KEY: str
    DEBUG: bool = True

    #БАЗА ДАННЫХ
    POSTGRES_HOST: str
    POSTGRES_PORT: str   
    POSTGRES_NAME: str   
    POSTGRES_USER: str   
    POSTGRES_PASS: str   

    def __init__(self, **kwargs):
        env_vars = dotenv_values("../.env")
        merged = {**env_vars, **kwargs}
        super().__init__(**merged)