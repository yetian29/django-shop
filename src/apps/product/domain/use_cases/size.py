from dataclasses import dataclass

from src.apps.base.domain.entities import BaseDataField
from src.apps.product.domain.services.size import ISizeService # type: ignore


@dataclass
class GetSizesUseCase:
    service: ISizeService

    def execute(self) -> list[BaseDataField]:
        return self.service.get_sizes()
