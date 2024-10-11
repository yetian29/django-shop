

from abc import ABC, abstractmethod

from src.apps.category.infrastructure.models import CategoryORM


class ICategoryRepository(ABC):
    @abstractmethod
    def get_categories(self) -> list[CategoryORM]:
        pass


class PostgresCategoryRepository(ICategoryRepository):
    def get_categories(self) -> list[CategoryORM]:
        categories = CategoryORM.objects.all()
        return list(categories)