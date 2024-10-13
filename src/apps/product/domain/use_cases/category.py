from dataclasses import dataclass

from src.apps.product.domain.entities.category import Category
from src.apps.product.domain.services.category import ICategoryService


@dataclass
class GetCategoriesUseCase:
    service: ICategoryService

    def execute(self) -> list[Category]:
        return self.service.get_categories()
