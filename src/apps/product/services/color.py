from dataclasses import dataclass

from src.apps.base.domain.entities import BaseDataField
from src.apps.product.domain.services.color import IColorService # type: ignore
from src.apps.product.infrastructure.repositories.color import ( # type: ignore
    IColorRepository
)


@dataclass
class ColorService(IColorService):
    repository: IColorRepository

    def get_colors(self) -> list[BaseDataField]:
        colors = self.repository.get_colors()
        return [color.to_entity() for color in colors]
