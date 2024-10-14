from uuid import uuid4
from django.db import models

from src.apps.base.infrastructure.models import BaseOidORM, BaseTimeORM

# Create your models here.


class UserORM(BaseOidORM, BaseTimeORM):
    email = models.EmailField(primary_key=32, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=16, unique=True, blank=True, null=True)
    token = models.UUIDField(unique=True, default=None, blank=True, null=True )
    is_active = models.BooleanField(default=False)