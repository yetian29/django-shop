from abc import ABC, abstractmethod

from src.apps.product.domain.entities.category import Category



class ICategoryService(ABC):
    @abstractmethod
    def get_categories(self) -> list[Category]:
        pass