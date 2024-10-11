from django.db import models

from src.apps.base.infrastructure.models import BaseDataFieldORM, BaseOidORM
from src.apps.category.domain.entities import Category
from src.apps.category.domain.values_object import CategoryEnum

# Create your models here.

    
class CategoryORM(BaseOidORM):
    category = models.CharField(max_length=16, choices=[(tag.value, tag.name) for tag in CategoryEnum], default=CategoryEnum.Cloth)

    
    def __str__(self):
        return self.category
    
    def to_entity(self) -> Category:
        return Category(
            oid=self.oid,
            catgory=self.category
        )