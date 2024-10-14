from uuid import uuid4

from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM
from src.apps.user.domain.entities import User

# Create your models here.


class UserORM(BaseOidORM, BaseTimeORM):
    phone_number = models.CharField(
        max_length=16, unique=True, blank=True, null=True, default=None
    )
    email = models.EmailField(
        max_length=32, unique=True, blank=True, null=True, default=None
    )
    token = models.UUIDField(unique=True, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)

    @staticmethod
    def from_entity(entity: User) -> "UserORM":
        return UserORM(
            oid=entity.oid,
            phone_number=entity.phone_number,
            email=entity.email,
            token=entity.token,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self) -> User:
        return User(
            oid=self.oid,
            email=self.email,
            phone_number=self.phone_number,
            token=self.token,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
