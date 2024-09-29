from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM

# Create your models here.


class ProductORM(BaseOidORM, BaseTimeORM):
    name = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    images = models.ImageField()



    
    