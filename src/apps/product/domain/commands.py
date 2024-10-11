

from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID

from src.apps.product.domain.values_object import GenderEnum


@dataclass
class GetProductCommand:
    oid: str

class SortOrderEnum(int, Enum):
    asc = 1
    desc = -1

@dataclass
class SortQuery:
    sort_field: str = "oid"
    sort_order: SortOrderEnum = SortOrderEnum.asc


@dataclass
class PaginationQuery:
    page: int = 0
    limit: int = 20
   
    @property 
    def offset(self) -> int:
        return self.page * self.limit
    
@dataclass
class FilterQuery:
    category: list[UUID] = field(default_factory=list)
    brands: list[UUID] = field(default_factory=list)
    colors: list[UUID] = field(default_factory=list)
    sizes: list[UUID] = field(default_factory=list)
    gender: GenderEnum | None = None
    
@dataclass
class GetProductListCommand:
    search: str | None = None
    filter: FilterQuery = field(default_factory=FilterQuery)
    sort: SortQuery = field(default_factory=SortQuery)
    pagination: PaginationQuery = field(default_factory=PaginationQuery)