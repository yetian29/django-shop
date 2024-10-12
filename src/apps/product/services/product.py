


from dataclasses import dataclass

from src.apps.product.domain.commands.product import FilterQuery
from src.apps.product.domain.entities.product import CatalogProduct, DetailProduct
from src.apps.product.domain.services.product import IProductService
from src.apps.product.infrastructure.repositories.product import IProductRepository

@dataclass
class ProductService(IProductService):
    repository: IProductRepository
    
    def get_by_id(self, oid: str) -> DetailProduct:
        dto = self.repository.get_by_id(oid=oid)
        return dto.to_detail_product_entity()
    
    def find_many(
        self, 
        sort_field: str, 
        sort_order: int, 
        limit: int, 
        offset: int,
        filter: FilterQuery,
        search: str | None = None
        ) -> list[CatalogProduct]:
        products = self.repository.find_many(
            sort_field=sort_field,
            sort_order=sort_order,
            limit=limit,
            offset=offset,
            filter=filter,
            search=search
        )
        return [product.to_catalog_product_entity() for product in products]
    
    def count_many(self, filter: FilterQuery, search: str | None = None) -> int:
        count = self.repository.count_many(filter, search)
        return count
        