from dataclasses import dataclass

from src.apps.base.domain.entities import BaseDataField
from src.apps.product.domain.services.color import IColorService # type: ignore


@dataclass
class GetColorsUseCase:
    service: IColorService

    def execute(self) -> list[BaseDataField]:
        return self.service.get_colors()
