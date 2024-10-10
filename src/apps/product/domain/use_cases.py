
from dataclasses import dataclass
from src.apps.product.domain.command import GetProductCommand, GetProductListCommand # type: ignore
from src.apps.product.domain.entities import CatalogProduct, DetailProduct
from src.apps.product.domain.services import IProductService

@dataclass
class GetProductUseCase:
    service: IProductService
    
    def execute(self, command: GetProductCommand) -> DetailProduct:
        return self.service.get_by_id(oid=command.oid)


@dataclass
class GetProductListUseCase:
    service: IProductService
    
    def execute(self, command: GetProductListCommand) -> tuple[list[CatalogProduct], int]:
        products = self.service.find_many(
            sort_field=command.sort.sort_field,
            sort_order=command.sort.sort_order,
            limit=command.pagination.limit,
            offset=command.pagination.offset,
            filter=command.filter,
            search=command.search
        )
        
        count = self.service.count_many(filter=command.filter, search=command.search)
        return products, count