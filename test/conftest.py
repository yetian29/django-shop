import punq
import pytest

from src.apps.product.domain.services.product import IProductService
from src.apps.product.domain.use_cases.product import (
    GetProductListUseCase,
    GetProductUseCase,
)
from test.mocks.product.serivces import DummyProductService


@pytest.fixture(scope="module")
def mock_test_container() -> punq.Container:
    container = punq.Container()

    container.register(IProductService, DummyProductService)
    container.register(GetProductUseCase)
    container.register(GetProductListUseCase)

    return container
