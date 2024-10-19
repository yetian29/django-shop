from abc import ABC, abstractmethod

from src.apps.product.domain.errors.category import CategoriesNotFoundException
from src.apps.product.infrastructure.models.category import CategoryORM
from src.helper.errors import fail


class ICategoryRepository(ABC):
    @abstractmethod
    def get_categories(self) -> list[CategoryORM]:
        pass


class PostgresCategoryRepository(ICategoryRepository):
    def get_categories(self) -> list[CategoryORM]:
        try:
            categories = CategoryORM.objects.all()
        except CategoryORM.DoesNotExist:
            fail(CategoriesNotFoundException)
        else:
            return list(categories)
