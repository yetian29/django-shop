

from typing import Any, Generic, TypeVar
from ninja import Schema, Field
from typing import Generic, TypeVar


TData = TypeVar("TData")
TItem = TypeVar("TItem")

class PaginationOutSchema(Schema):
    page: int
    limit: int
    total: int
    

class PaginatedListResponse(Schema, Generic[TItem]):
    items: list[TItem]
    pagination: PaginationOutSchema
    
    
class ApiResponse(Schema, Generic[TData]):
    data: TData | list | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    error: list[Any] = Field(default_factory=list)
    
    