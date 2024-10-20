from polyfactory.factories import DataclassFactory

from src.apps.user.domain.commands import AuthorizeUserCommand, LoginUserCommand
from src.apps.user.domain.entities import User


class UserFactory(DataclassFactory[User]):
    __model__ = User


class AuthorizeUserCommandFactory(DataclassFactory[AuthorizeUserCommand]):
    __model__ = AuthorizeUserCommand


class LoginUserCommandFactory(DataclassFactory[LoginUserCommand]):
    __model__ = LoginUserCommand
