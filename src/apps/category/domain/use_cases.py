

from dataclasses import dataclass
from src.apps.category.domain.entities import Category
from src.apps.category.domain.services import ICategoryService

@dataclass
class GetCategoriesUseCase:
    service: ICategoryService

    def execute(self) -> list[Category]:
        return self.service.get_categories()
    