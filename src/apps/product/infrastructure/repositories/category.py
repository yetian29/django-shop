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
        categories = CategoryORM.objects.all()
        if not categories.exists(): 
            fail(CategoriesNotFoundException)
        return list(categories)
