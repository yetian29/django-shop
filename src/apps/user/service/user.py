import random
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta

from django.core.cache import cache

from src.apps.user.domain.entities import User
from src.apps.user.domain.services import (
    ICodeService,
    ILoginService,
    ISendService,
    IUserService,
)
from src.apps.user.infrastructure.models import UserORM
from src.apps.user.infrastructure.repositories import IUserRepository
from src.apps.user.service.errors import (
    CachedDataNotExistException,
    CodeNotFoundException,
    EqualCodesException,
    ExpiredCodeException,
)


@dataclass
class CodeService(ICodeService):
    def generate_code(self, user: User) -> str:
        code = str(random.randint(100000, 999999))
        time_out = timedelta(seconds=1000)
        cached_data = {"code": code, "ttl": datetime.now() + time_out}
        if user.phone_number:
            cache.set(user.phone_number, cached_data, 1000)
        else:
            if user.email:
                cache.set(user.email, cached_data, 1000)
        return code

    def validate_code(self, user: User, code: str) -> None:
        if user.phone_number:
            try:
                cached_data = cache.get(user.phone_number)
            except:
                raise CachedDataNotExistException
            else:
                if not cached_data.get("code"):
                    cache.delete(user.phone_number)
                    raise CodeNotFoundException
                if datetime.now() > cached_data.get("ttl"):
                    cache.delete(user.phone_number)
                    raise ExpiredCodeException
                if code != cached_data.get("code"):
                    print(f"Code: {code}, {cached_data.get("code")}")
                    cache.delete(user.phone_number)
                    raise EqualCodesException

                cache.delete(user.phone_number)
        else:
            if user.email:
                try:
                    cached_data = cache.get(user.email)
                except:
                    raise CachedDataNotExistException
                else:
                    if not cached_data.get("code"):
                        cache.delete(user.email)
                        raise CodeNotFoundException
                    if datetime.now() > cached_data.get("ttl"):
                        cache.delete(user.email)
                        raise ExpiredCodeException
                    if code != cached_data.get("code"):
                        cache.delete(user.email)
                        raise EqualCodesException

                    cache.delete(user.email)


class SendService(ISendService):
    def send_code(self, user: User, code: str) -> None:
        if user.phone_number:
            print(
                f"The Code <{code}> has been sent to phone number: <{user.phone_number}>"
            )
        else:
            if user.email:
                print(f"The code <{code}> has been sent to email: <{user.email}>")


class LoginService(ILoginService):
    def active_and_genarate_token(self, user: User) -> uuid.UUID:
        user.token = uuid.uuid4()
        user.is_active = True
        return user.token


@dataclass
class UserService(IUserService):
    repository: IUserRepository

    def get_by_phone_number_or_email(self, phone_number: str, email: str) -> User:
        dto = self.repository.get_by_phone_number_or_email(phone_number=phone_number, email=email)
        return dto.to_entity()
    
    def get_or_create(self, user: User) -> User:
        dto = UserORM.from_entity(entity=user)
        dto = self.repository.get_or_create(user=dto)
        return dto.to_entity()
    
    def update(self, user: User) -> User:
        dto = UserORM.from_entity(entity=user)
        dto = self.repository.update(user=dto)
        return dto.to_entity()
