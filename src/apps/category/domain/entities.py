
from dataclasses import dataclass

from src.apps.base.domain.entities import BaseOid
from src.apps.category.domain.values_object import CategoryEnum


@dataclass
class Category(BaseOid):
    catgory: CategoryEnum
    