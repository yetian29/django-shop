from abc import ABC, abstractmethod

from src.apps.base.domain.entities import BaseDataField


class ISizeService(ABC):
    @abstractmethod
    def get_sizes(self) -> list[BaseDataField]:
        pass
