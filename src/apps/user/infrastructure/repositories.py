from abc import ABC, abstractmethod

from django.db.models import Q

from src.apps.user.domain.errors import (
    UserCreatedNotSuccessException,
    UserNotFoundException,
)
from src.apps.user.infrastructure.models import UserORM
from src.helper.errors import fail


class IUserRepository(ABC):
    @abstractmethod
    def get_by_phone_number_or_email(self, phone_number: str, email: str) -> UserORM:
        pass

    @abstractmethod
    def create(self, user: UserORM) -> UserORM:
        pass

    @abstractmethod
    def get_or_create(self, user: UserORM) -> UserORM:
        pass

    @abstractmethod
    def update(self, user: UserORM) -> UserORM:
        pass


class PostgresUserRepository(IUserRepository):
    def get_by_phone_number_or_email(self, phone_number: str, email: str) -> UserORM:
        try:
            dto = UserORM.objects.get(Q(phone_number=phone_number) | Q(email=email))
        except UserORM.DoesNotExist:
            fail(UserNotFoundException)
        else:
            return dto

    def create(self, user: UserORM) -> UserORM:
        if user.phone_number:
            try:
                dto = UserORM.objects.create(phone_number=user.phone_number)
            except UserORM.DoesNotExist:
                fail(UserCreatedNotSuccessException)
            else:
                return dto
        else:
            if user.email:
                try:
                    dto = UserORM.objects.create(email=user.email)
                except UserORM.DoesNotExist:
                    fail(UserCreatedNotSuccessException)
                else:
                    return dto

    def get_or_create(self, user: UserORM) -> UserORM:
        try:
            dto = self.get_by_phone_number_or_email(
                phone_number=user.phone_number, email=user.email
            )
        except UserNotFoundException:
            dto = self.create(user=user)
            return dto
        else:
            return dto

    def update(self, user: UserORM) -> UserORM:
        updated_count = UserORM.objects.filter(oid=user.oid).update(
            is_active=user.is_active, token=user.token
        )
        if updated_count == 0:
            fail(UserNotFoundException)
        dto = UserORM.objects.get(oid=user.oid)
        return dto
