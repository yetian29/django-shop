from polyfactory.factories import DataclassFactory

from src.apps.product.domain.commands.product import (
    GetProductCommand,
    GetProductListCommand,
)
from src.apps.product.domain.entities.product import CatalogProduct, DetailProduct
from src.apps.user.domain.commands import AuthorizeUserCommand, LoginUserCommand
from src.apps.user.domain.entities import User

# Product
class CatalogProductFactory(DataclassFactory[CatalogProduct]):
    __model__ = CatalogProduct


class DetailProductFactory(DataclassFactory[DetailProduct]):
    __model__ = DetailProduct


class GetPoruductCommandFactory(DataclassFactory[GetProductCommand]):
    __model__ = GetProductCommand


class GetPoruductListCommandFactory(DataclassFactory[GetProductListCommand]):
    __model__ = GetProductListCommand
    
# User

class UserFactory(DataclassFactory[User]):
    __model__ = User


class AuthorizeUserCommandFactory(DataclassFactory[AuthorizeUserCommand]):
    __model__ = AuthorizeUserCommand


class LoginUserCommandFactory(DataclassFactory[LoginUserCommand]):
    __model__ = LoginUserCommand
