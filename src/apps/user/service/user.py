

from dataclasses import dataclass
from datetime import datetime, timedelta
import random
import uuid

from src.apps.user.domain.entities import User
from src.apps.user.domain.services import ICodeService, ILoginService, ISendService, IUserService
from django.core.cache import cache

from src.apps.user.service.errors import CodeNotFoundException, EqualCodesException, ExpiredCodeException

@dataclass
class DummyCodeService(ICodeService):
    def generate_code(self, user: User) -> str:
        code = random.randint(100000, 999999)
        time_out = timedelta(seconds=1000)
        cached_data = {
            "code": code,
            "ttl": datetime.now() + time_out
        }
        if user.phone_number:
            cache.set(user.phone_number, cached_data, 1000)
        if user.email:
            cache.set(user.email, cached_data, 1000)
        return str(code)
    
    def validate_code(self, user: User, code: str) -> None:
        if user.phone_number:
            cached_data = cache.get(user.phone_number)
            if not cached_data.get("code"):
                cache.delete(user.phone_number)
                raise CodeNotFoundException
            if datetime.now() > cached_data.get("ttl"):
                cache.delete(user.phone_number)
                raise ExpiredCodeException
            if code != cached_data.get("code"):
                cache.delete(user.phone_number)
                raise EqualCodesException
                       
            cache.delete(user.phone_number)
            
        if user.email:
            cached_data = cache.get(user.email)
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

       
class DummySendService(ISendService):
    def send_code(self, user: User, code: str) -> None:
        if user.phone_number:
            print(f"The Code <{code}> has sent to phone number: <{user.phone_number}>")
        if user.email:
            print(f"The code <{code}> has sent to email: <{user.email}>")
            

class DummyLoginService(ILoginService):
    def active_and_genarate_token(self, user: User) -> uuid.UUID:
        user.token = uuid.uuid4()
        user.is_active = True
        return user.token        

class DummyUserService(IUserService):
    def get_by_phone_number_or_email(self, user: User) -> User:
        pass
     
    def get_or_create(self, user: User) -> User:
        pass