

from dataclasses import dataclass, field
from enum import Enum


@dataclass
class GetProductCommand:
    oid: str

class SortOrderEnum(int, Enum):
    asc = 1
    desc = -1

@dataclass
class SortQuery:
    sort_field: str = "oid"
    sort_order: SortOrderEnum = field(default_factory=SortOrderEnum)

@dataclass
class PaginationQuery:
    page: int = 0
    limit: int = 20
   
    @property 
    def offset(self) -> int:
        return self.page * self.limit
    
@dataclass
class GetProductListCommand:
    search: str | None = None
    sort: SortQuery = field(default_factory=SortQuery)
    pagination: PaginationQuery = field(default_factory=PaginationQuery)