

from abc import ABC, abstractmethod
from src.apps.product.domain.commands import FilterQuery
from src.apps.product.domain.entities import CatalogProduct, DetailProduct


class IProductService(ABC):
    @abstractmethod
    def get_by_id(self, oid: str) -> DetailProduct:
        pass
    
    @abstractmethod
    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        filter: FilterQuery,
        search: str | None = None      
    ) -> list[CatalogProduct]:
        pass

    @abstractmethod
    def count_many(
        self,
        search: str | None = None
    ) -> int:
        pass
        