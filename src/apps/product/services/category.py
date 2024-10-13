from dataclasses import dataclass

from src.apps.product.domain.entities.category import Category
from src.apps.product.domain.services.category import ICategoryService
from src.apps.product.infrastructure.repositories.category import ICategoryRepository


@dataclass
class CategoryService(ICategoryService):
    repository: ICategoryRepository

    def get_categories(self) -> list[Category]:
        categories = self.repository.get_categories()
        return [cat.to_entity() for cat in categories]
