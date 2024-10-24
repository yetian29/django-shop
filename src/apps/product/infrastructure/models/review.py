from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.product.domain.entities.review import Review
from src.apps.product.infrastructure.models.product import ProductORM
from src.apps.user.infrastructure.models import UserORM


class ReviewORM(BaseOidORM, BaseTimeORM):
    user = models.ForeignKey(UserORM, on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductORM, on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField(default=1)
    content = models.TextField(blank=True)


    def is_authenticated(self) -> bool:
        return self.user.token is not None 
    
    @staticmethod
    def from_entity(entity: Review) -> "ReviewORM":
        return ReviewORM(
            oid=entity.oid,
            user=entity.user,
            product=entity.product,
            rating=entity.rating,
            content=entity.content,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    def to_entity(self) -> Review:
        return Review(
            oid=self.oid,
            user=self.user,
            product=self.product,
            rating=self.rating,
            content=self.content,
            created_at=self.created_at,
            updated_at=self.updated_at 
        )