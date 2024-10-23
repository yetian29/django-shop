import random
from datetime import datetime, timedelta
from uuid import UUID, uuid4

from src.apps.user.domain.entities import User
from src.apps.user.domain.services import (
    ICodeService,
    ILoginService,
    ISendService,
    IUserService,
)
from src.apps.user.service.errors import (
    CachedDataNotExistException,
    CodeNotFoundException,
    EqualCodesException,
    ExpiredCodeException,
)
from src.helper.errors import fail
from test.mocks.factories.user import UserFactory


class DummyCodeService(ICodeService):
    cache = {}

    def generate_code(self, user: User) -> str:
        code = str(random.randint(100000, 999999))
        time_out = timedelta(milliseconds=1000)
        cached_data = {"code": code, "ttl": datetime.now() + time_out}
        if user.phone_number:
            self.cache[user.phone_number] = cached_data
        else:
            if user.email:
                self.cache[user.email] = cached_data
        return code

    def validate_code(self, user: User, code: str) -> None:
        if user.phone_number:
            cached_data = self.cache.get(user.phone_number)
            if not cached_data:
                fail(CachedDataNotExistException)
            if not cached_data.get("code"):
                del self.cache[user.phone_number]
                fail(CodeNotFoundException)

            if datetime.now() > cached_data.get("ttl"):
                del self.cache[user.phone_number]
                fail(ExpiredCodeException)

            if code != cached_data.get("code"):
                del self.cache[user.phone_number]
                fail(EqualCodesException)

            del self.cache[user.phone_number]
        else:
            if user.emal:
                cached_data = self.cache.get(user.email)
                if not cached_data:
                    fail(CachedDataNotExistException)

                if not cached_data.get("code"):
                    del self.cache[user.email]
                    fail(CodeNotFoundException)

                if datetime.now() > cached_data.get("ttl"):
                    del self.cache[user.email]
                    fail(ExpiredCodeException)

                if code != cached_data.get("code"):
                    del self.cache[user.email]
                    fail(EqualCodesException)

                del self.cache[user.email]


class DummySendService(ISendService):
    def send_code(self, user: User, code: str) -> None:
        if user.phone_number:
            print(
                f"The code <{code}> has been sent to phone number <{user.phone_number}>"
            )
        else:
            if user.email:
                print(f"The code <{user.email}> has been sent to email <{user.email}>")


class DummyLoginService(ILoginService):
    def active_and_genarate_token(self, user: User) -> UUID:
        user.is_active = True
        user.token = uuid4()
        return user.token


class DummyUserService(IUserService):
    def get_by_phone_number_or_email(self, phone_number: str, email: str) -> User:
        if phone_number:
            return UserFactory.build(phone_number=phone_number)
        else:
            if email:
                return UserFactory.build(email=email)

    def get_or_create(self, user: User) -> User:
        return UserFactory.build(
            oid=user.oid,
            phone_number=user.phone_number,
            email=user.email,
            is_active=user.is_active,
            token=user.token,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    def update(self, user: User) -> User:
        return UserFactory.build(
            oid=user.oid,
            phone_number=user.phone_number,
            email=user.email,
            is_active=user.is_active,
            token=user.token,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
