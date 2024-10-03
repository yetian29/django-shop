from django.db import models

from src.apps.base.infrastructure.models import BaseDataFieldORM
from src.apps.category.domain.values_object import CategoryEnum

# Create your models here.

    
class CategoryORM(BaseDataFieldORM):
    category = models.CharField(max_length=16, choices=[(tag.value, tag.name) for tag in CategoryEnum], default=CategoryEnum.Cloth)

    
    def __str__(self):
        return self.name