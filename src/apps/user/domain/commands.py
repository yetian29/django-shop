from dataclasses import dataclass

from src.apps.user.domain.entities import User


@dataclass
class AuthorizeUserCommand:
    user: User


@dataclass
class LoginUserCommand:
    user: User
    code: str
