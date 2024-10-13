from abc import ABC, abstractmethod

from src.apps.product.domain.errors.color import ColorsNotFoundException # type: ignore
from src.apps.product.infrastructure.models.color import ColorORM


class IColorRepository(ABC):
    @abstractmethod
    def get_colors(self) -> list[ColorORM]:
        pass


class PostgresColorRepository(IColorRepository):
    def get_colors(self) -> list[ColorORM]:
        try:
            colors = ColorORM.objects.all()
        except ColorORM.DoesNotExist as error:
            raise ColorsNotFoundException from error
        else:
            return list(colors)
