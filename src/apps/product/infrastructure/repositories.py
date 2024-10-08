

from abc import ABC, abstractmethod

from src.apps.product.infrastructure.models import ProductORM

from django.db.models import Q


class IProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, oid: str) -> ProductORM:
        pass
    
    @abstractmethod
    def find_many(
        self,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
        search: str | None = None
    ) -> list[ProductORM]:
        pass
    
    @abstractmethod
    def count_many(
        self,
        search: str | None = None
    ) -> int:
        pass


class PostgresProductRepository(IProductRepository):
    def get_by_id(self, oid: str) -> ProductORM:
        doc = ProductORM.objects.get(oid=oid)
        return doc

    
    def _build_find_query(self, search: str | None = None) -> Q:
        query = Q()
        if search:
            search_query =  Q(name__icontains=search) | Q(description__icontains=search)
            query &= search_query
        return query
    
    
    def find_many(
        self,
        sort_field: str, 
        sort_order: int, 
        limit: int, 
        offset: int, 
        search: str | None = None
        ) -> list[ProductORM]:
        query = self._build_find_query(search)
        sort_direction = "-" if sort_order == -1 else ""
        order_by_field = f"{sort_direction}{sort_field}"
        
        products = (
            ProductORM.objects
            .filter(query)
            .order_by(order_by_field)
            [offset:offset+limit]
        )
        
        return list(products)
    
    def count_many(self, search: str | None = None) -> int:
        query = self._build_find_query(search=search)
        count = ProductORM.objects.filter(query).count()
        return count
        
        