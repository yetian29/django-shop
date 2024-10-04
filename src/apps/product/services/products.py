


from dataclasses import dataclass
from src.apps.product.domain.entities import Product
from src.apps.product.domain.services import IProductService
from src.apps.product.infrastructure.repositories import IProductRepository

@dataclass
class ProductService(IProductService):
    repository: IProductRepository
    
    def get_by_id(self, oid: str) -> Product:
        dto = self.repository.get_by_id(oid=oid)
        return dto.to_entity()
    
    def find_many(
        self, 
        sort_field: str, 
        sort_order: int, 
        limit: int, 
        offset: int,
        search: str | None = None
        ) -> list[Product]:
        products = self.repository.find_many(
            sort_field=sort_field,
            sort_order=sort_order,
            limit=limit,
            offset=offset,
            search=search
        )
        return [product.to_entity() for product in products]
    
    def count_many(self, search: str | None = None) -> int:
        count = self.repository.count_many(search=search)
        return count
        