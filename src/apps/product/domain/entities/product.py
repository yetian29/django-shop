from dataclasses import dataclass, fields
from enum import Enum

from src.apps.base.domain.entities import BaseDataField, BaseTime


@dataclass
class BaseProduct(BaseDataField):
    price: int


@dataclass
class CatalogProduct(BaseProduct, BaseTime):
    # image: str
    sold: int
    places_sell: list[BaseDataField]


@dataclass
class DetailProduct(BaseProduct):
    # images: list[str]
    description: str
    brand: BaseDataField
    colors: list[BaseDataField]
    sizes: list[BaseDataField]
    quantity: int


CatalogProductSortFieldsEnum = Enum(
    "CatalogProductSortFieldsEnum",
    {field.name: field.name for field in fields(CatalogProduct)},
)
