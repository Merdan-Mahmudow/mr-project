from abc import ABC, abstractmethod

class SettingsInterface(ABC):
    @abstractmethod
    def generate_postgres_url(self) -> str:
        pass
