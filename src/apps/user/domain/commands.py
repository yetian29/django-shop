

from dataclasses import dataclass
from src.apps.user.domain.entities import User

@dataclass
class AuthozieUserCommand:
    user: User

@dataclass
class LoginUserCommand:
    code: str
    