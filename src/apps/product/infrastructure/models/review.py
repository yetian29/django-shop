from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.product.infrastructure.models.product import ProductORM
from src.apps.user.infrastructure.models import UserORM


class ReviewORM(BaseOidORM, BaseTimeORM):
    user = models.ForeignKey(UserORM, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductORM, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=1)
    content = models.TextField(blank=True)
