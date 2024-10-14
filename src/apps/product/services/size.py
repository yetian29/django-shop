from dataclasses import dataclass

from src.apps.base.domain.entities import BaseDataField
from src.apps.product.domain.services.size import ISizeService  # type: ignore
from src.apps.product.infrastructure.repositories.size import (  # type: ignore
    ISizeRepository,
)


@dataclass
class SizeService(ISizeService):
    repository: ISizeRepository

    def get_sizes(self) -> list[BaseDataField]:
        sizes = self.repository.get_sizes()
        return [size.to_entity() for size in sizes]
