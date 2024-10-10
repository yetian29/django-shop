

from dataclasses import dataclass, field
from enum import Enum

from src.apps.base.domain.entities import BaseOid
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
    category: list[str] = field(default_factory=list)
    brands: list[str] = field(default_factory=list)
    colors: list[str] = field(default_factory=list)
    sizes: list[str] = field(default_factory=list)
    gender: GenderEnum = GenderEnum.Unisex
    
@dataclass
class GetProductListCommand:
    search: str | None = None
    filter: FilterQuery = field(default_factory=FilterQuery)
    sort: SortQuery = field(default_factory=SortQuery)
    pagination: PaginationQuery = field(default_factory=PaginationQuery)