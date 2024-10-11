
from abc import ABC, abstractmethod

from src.apps.category.domain.entities import Category


class ICategoryService(ABC):
    @abstractmethod
    def get_categories(self) -> list[Category]:
        pass