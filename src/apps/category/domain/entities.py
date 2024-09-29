
from dataclasses import dataclass

from src.apps.base.domain.entities import BaseDataField
from src.apps.category.domain.values_object import CategoryEnum


@dataclass
class Category(BaseDataField):
    catgory: CategoryEnum
    