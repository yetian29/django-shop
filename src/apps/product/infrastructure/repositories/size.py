from abc import ABC, abstractmethod

from src.apps.product.domain.errors.size import SizesNotFoundException  # type: ignore
from src.apps.product.infrastructure.models.size import SizeORM
from src.helper.errors import fail


class ISizeRepository(ABC):
    @abstractmethod
    def get_sizes(self) -> list[SizeORM]:
        pass


class PostgresSizeRepository(ISizeRepository):
    def get_sizes(self) -> list[SizeORM]:
        sizes = SizeORM.objects.all()
        if not sizes.exists():
            fail(SizesNotFoundException)
        return list(sizes)
