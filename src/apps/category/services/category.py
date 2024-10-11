

from dataclasses import dataclass
from src.apps.category.domain.entities import Category
from src.apps.category.domain.services import ICategoryService
from src.apps.category.infrastructure.repositories import ICategoryRepository

@dataclass
class CategoryService(ICategoryService):
    repository: ICategoryRepository

    def get_categories(self) -> list[Category]:
        categories = self.repository.get_categories()
        return [cat.to_entity() for cat in categories]