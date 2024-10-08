

from abc import ABC, abstractmethod
from src.apps.product.domain.entities import CatalogProduct, Product


class IProductService(ABC):
    @abstractmethod
    def get_by_id(self, oid: str) -> Product:
        pass
    
    @abstractmethod
    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: str | None = None      
    ) -> list[CatalogProduct]:
        pass

    @abstractmethod
    def count_many(
        self,
        search: str | None = None
    ) -> int:
        pass
        