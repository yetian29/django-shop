import punq
import pytest

from src.apps.product.domain.services.product import IProductService
from src.apps.product.domain.use_cases.product import (
    GetProductListUseCase,
    GetProductUseCase,
)
from src.apps.user.domain.services import ICodeService, ILoginService, ISendService, IUserService
from src.apps.user.domain.use_cases import AuthorizeUserUseCase, LoginUserUseCase
from test.mocks.services.product import DummyProductService
from test.mocks.services.user import DummyCodeService, DummyLoginService, DummySendService, DummyUserService


@pytest.fixture(scope="session")
def mock_test_container() -> punq.Container:
    container = punq.Container()

    container.register(IProductService, DummyProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    container.register(ICodeService, DummyCodeService, scope=punq.Scope.singleton)
    container.register(ISendService, DummySendService)
    container.register(ILoginService, DummyLoginService)
    container.register(IUserService, DummyUserService)
    container.register(AuthorizeUserUseCase)
    container.register(LoginUserUseCase)

    return container
