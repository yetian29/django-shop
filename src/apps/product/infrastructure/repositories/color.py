from abc import ABC, abstractmethod

from src.apps.product.domain.errors.color import ColorsNotFoundException  # type: ignore
from src.apps.product.infrastructure.models.color import ColorORM
from src.helper.errors import fail


class IColorRepository(ABC):
    @abstractmethod
    def get_colors(self) -> list[ColorORM]:
        pass


class PostgresColorRepository(IColorRepository):
    def get_colors(self) -> list[ColorORM]:
        colors = ColorORM.objects.all()
        if not colors.exists():
            fail(ColorsNotFoundException)
        return list(colors)
