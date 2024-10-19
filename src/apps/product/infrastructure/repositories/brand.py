from abc import ABC, abstractmethod

from src.apps.product.domain.errors.brand import BrandsNotFoundException  # type: ignore
from src.apps.product.infrastructure.models.brand import BrandORM
from src.helper.errors import fail


class IBrandRepository(ABC):
    @abstractmethod
    def get_brands(self) -> list[BrandORM]:
        pass


class PostgresBrandRepository(IBrandRepository):
    def get_brands(self) -> list[BrandORM]:
        try:
            brands = BrandORM.objects.all()
        except BrandORM.DoesNotExist:
            fail(BrandsNotFoundException)
        else:
            return list(brands)
