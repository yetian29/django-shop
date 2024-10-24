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
        brands = BrandORM.objects.all()
        if not brands.exists():
            fail(BrandsNotFoundException)
        return list(brands)
