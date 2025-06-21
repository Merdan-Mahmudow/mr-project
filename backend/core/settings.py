from core.env import Environment
from interfaces.cores import SettingsInterface


class Settings(SettingsInterface):
    def __init__(self):
        self.env = Environment()

    def generate_postgres_url(self) -> str:
        return f"postgresql+asyncpg://{self.env.POSTGRES_USER}:{self.env.POSTGRES_PASS}@{self.env.POSTGRES_HOST}:{self.env.POSTGRES_PORT}/{self.env.POSTGRES_NAME}"