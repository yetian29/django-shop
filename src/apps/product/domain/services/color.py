from abc import ABC, abstractmethod

from src.apps.base.domain.entities import BaseDataField


class IColorService(ABC):
    @abstractmethod
    def get_colors(self) -> list[BaseDataField]:
        pass
