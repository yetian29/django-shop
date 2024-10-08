

from dataclasses import dataclass, fields
from enum import Enum
from src.apps.base.domain.entities import BaseDataField, BaseTime
from src.apps.product.domain.values_object import GenderEnum

@dataclass
class BaseProduct(BaseDataField):
    price: int
    
    
@dataclass
class CatalogProduct(BaseProduct):
    # image: str
    sold: str
    place_sell: BaseDataField

    
    
@dataclass
class Product(BaseProduct, BaseTime):
    # images: list[str]
    category: BaseDataField
    brand: BaseDataField
    color: BaseDataField
    size: BaseDataField
    gender: GenderEnum
    quantity: int


CatalogProductSortFieldsEnum = Enum(
    "CatalogProductSortFieldsEnum",
    {field.name: field.name for field in fields(CatalogProduct)}
)

