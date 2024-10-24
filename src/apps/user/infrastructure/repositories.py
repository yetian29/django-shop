from abc import ABC, abstractmethod

from django.db.models import Q

from src.apps.user.domain.errors import (
    UserCreatedNotSuccessException,
    UserNotFoundException,
    UserNotFoundToUpdateException,
)
from src.apps.user.infrastructure.models import UserORM
from src.helper.errors import fail
from django.core.exceptions import ObjectDoesNotExist

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
        except ObjectDoesNotExist:
            fail(UserNotFoundException)
        else:
            return dto

    def create(self, user: UserORM) -> UserORM:
        if user.phone_number:
            dto = UserORM.objects.create(phone_number=user.phone_number)
            if not dto: 
                fail(UserCreatedNotSuccessException)           
            return dto
        else:
            if user.email:
                dto = UserORM.objects.create(email=user.email)
                if not dto:
                    fail(UserCreatedNotSuccessException)
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
        dto = UserORM.objects.get(oid=user.oid)
        if not dto:
            fail(UserNotFoundToUpdateException)
        dto.is_active = user.is_active
        dto.token = user.token
        dto.save()
        return dto

