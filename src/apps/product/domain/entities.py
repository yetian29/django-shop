

from dataclasses import dataclass
from src.apps.base.domain.entities import BaseDataField, BaseTime
from src.apps.product.domain.values_object import GenderEnum

@dataclass
class BaseProduct(BaseDataField):
    price: int
    
    
@dataclass
class CatalogProduct(BaseProduct):
    image: str
    sold: int
    place_sell: BaseDataField
    
@dataclass
class Product(BaseProduct, BaseTime):
    images: list[str]
    category: BaseDataField
    place_sell: BaseDataField
    brand: BaseDataField
    color: BaseDataField
    size: BaseDataField
    gender: GenderEnum
    sold: int
    quantity: int


    
    