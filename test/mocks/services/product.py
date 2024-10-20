import random

from src.apps.product.domain.commands.product import FilterQuery
from src.apps.product.domain.entities.product import CatalogProduct, DetailProduct
from src.apps.product.domain.services.product import IProductService
from test.mocks.factories.product import (
    CatalogProductFactory,
    DetailProductFactory,
)


class DummyProductService(IProductService):
    def get_by_id(self, oid: str) -> DetailProduct:
        return DetailProductFactory.build(oid=oid)

    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        filter: FilterQuery,
        search: str | None = None,
    ) -> list[CatalogProduct]:
        return [CatalogProductFactory.build() for _ in range(random.randint(0, limit))]

    def count_many(self, filter: FilterQuery, search: str | None = None) -> int:
        return random.randint(0, 1000)
