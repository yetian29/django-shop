from dataclasses import dataclass

from src.apps.user.domain.entities import User


@dataclass
class AuthorizeUserCommand:
    user: User


@dataclass
class LoginUserCommand:
    phone_number: str
    email: str
    code: str
