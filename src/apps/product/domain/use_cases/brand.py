from dataclasses import dataclass

from src.apps.base.domain.entities import BaseDataField
from src.apps.product.domain.services.brand import IBrandService


@dataclass
class GetBrandsUseCase:
    service: IBrandService

    def execute(self) -> list[BaseDataField]:
        return self.service.get_brands()
