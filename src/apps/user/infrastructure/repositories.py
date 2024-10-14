

from abc import ABC, abstractmethod

from src.apps.user.infrastructure.models import UserORM


class IUserRepository(ABC):
    @abstractmethod
    def get_by_phone_number_or_email(self, user: UserORM) -> UserORM:
        pass

    @abstractmethod
    def get_or_create(self, user: UserORM) -> UserORM:
        pass

class PostgresRepository(IUserRepository):
    def get_by_phone_number_or_email(self, user: UserORM) -> UserORM:
        if user.phone_number:
            try: 
                dto = UserORM.objects.get(phone_number=user.phone_number)
            except UserORM.DoesNotExist as error:
                raise UserNotFoundException from error
            else: 
                return dto
               
        if user.email:
            try:
                dto = UserORM.objects.get(email=user.email)
            except UserORM.DoesNotExist as error:
                raise UserNotFoundException from error
            else: 
                return dto
