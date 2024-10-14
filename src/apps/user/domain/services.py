import uuid
from abc import ABC, abstractmethod

from src.apps.user.domain.entities import User  # type: ignore


class ICodeService(ABC):
    @abstractmethod
    def generate_code(self, user: User) -> str:
        pass

    @abstractmethod
    def validate_code(self, user: User, code: str) -> None:
        pass


class ISendService(ABC):
    @abstractmethod
    def send_code(self, user: User, code: str) -> None:
        pass


class ILoginService(ABC):
    @abstractmethod
    def active_and_genarate_token(self, user: User) -> uuid.UUID:
        pass


class IUserService(ABC):
    @abstractmethod
    def get_by_phone_number_or_email(self, user: User) -> User:
        pass
    
    @abstractmethod
    def create(self, user: User) -> User:
        pass
    
    @abstractmethod
    def get_or_create(self, user: User) -> User:
        pass
