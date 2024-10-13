from abc import ABC, abstractmethod

from src.apps.base.domain.entities import BaseDataField


class IBrandService(ABC):
    @abstractmethod
    def get_brands(self) -> BaseDataField:
        pass
