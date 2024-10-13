from dataclasses import dataclass

from src.apps.base.domain.entities import BaseDataField
from src.apps.product.domain.services.brand import IBrandService
from src.apps.product.infrastructure.repositories.brand import (
    IBrandRepository,  # type: ignore
)


@dataclass
class BrandService(IBrandService):
    repository: IBrandRepository

    def get_brands(self) -> list[BaseDataField]:
        brands = self.repository.get_brands()
        return [brand.to_entity() for brand in brands]
