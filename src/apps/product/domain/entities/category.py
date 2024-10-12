 
from dataclasses import dataclass

from src.apps.base.domain.entities import BaseOid
from src.apps.product.domain.values_object.category import CategoryEnum


@dataclass
class Category(BaseOid):
    category: CategoryEnum
     
