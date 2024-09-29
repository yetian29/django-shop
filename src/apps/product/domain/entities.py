

from dataclasses import dataclass
from src.apps.base.domain.entities import BaseDataField, BaseOid, BaseTime
from src.apps.product.domain.values_object import GenderEnum

@dataclass
class BaseProduct(BaseOid):
    name: str
    price: int
    
    
@dataclass
class CatalogProduct(BaseProduct):
    image: str
    sold: int
    place_sell: BaseDataField
    
@dataclass
class Product(BaseProduct):
    images: list[str]
    category: BaseDataField
    place_sell: BaseDataField
    brand: BaseDataField
    color: BaseDataField
    sizes: BaseDataField
    gender: GenderEnum
    quantity: int


    
    