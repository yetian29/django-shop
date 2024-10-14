from abc import ABC, abstractmethod

from src.apps.user.domain.errors import (
    UserCreatedNotSuccessException,
    UserNotFoundException,
)
from src.apps.user.infrastructure.models import UserORM


class IUserRepository(ABC):
    @abstractmethod
    def get_by_phone_number_or_email(self, user: UserORM) -> UserORM:
        pass

    @abstractmethod
    def create(self, user: UserORM) -> UserORM:
        pass
    
    @abstractmethod
    def get_or_create(self, user: UserORM) -> UserORM:
        pass


class PostgresUserRepository(IUserRepository):
    def get_by_phone_number_or_email(self, user: UserORM) -> UserORM:
        if user.phone_number:
            try:
                dto = UserORM.objects.get(phone_number=user.phone_number)
            except UserORM.DoesNotExist as error:
                raise UserNotFoundException from error
            else:
                return dto
        else:
            if user.email:
                try:
                    dto = UserORM.objects.get(email=user.email)
                except UserORM.DoesNotExist as error:
                    raise UserNotFoundException from error
                else:
                    return dto
            
    def create(self, user: UserORM) -> UserORM:
        if user.phone_number:
            try:
                dto = UserORM.objects.create(phone_number=user.phone_number)
            except UserORM.DoesNotExist as error:
                raise UserCreatedNotSuccessException from error
            else:
                return dto
        else:        
            if user.email:
                try:
                    dto = UserORM.objects.create(email=user.email)
                except UserORM.DoesNotExist as error:
                    raise UserCreatedNotSuccessException from error
                else:
                    return dto
                        
    def get_or_create(self, user: UserORM) -> UserORM:
        try:
            dto = self.get_by_phone_number_or_email(user=user)
        except UserNotFoundException:
            dto = self.create(user=user)
            return dto
        else:
            return dto
        
