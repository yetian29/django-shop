



from test.mocks.product.factories import GetPoruductCommandFactory, GetPoruductListCommandFactory

from src.apps.product.domain.use_cases.product import GetProductListUseCase, GetProductUseCase
import pytest



@pytest.fixture
def mock_get_by_id_use_case(mock_test_container):
    return mock_test_container.resolve(GetProductUseCase)


@pytest.fixture
def mock_find_many_use_case(mock_test_container):
    return mock_test_container.resolve(GetProductListUseCase)

def test_get_by_id_use_case(mock_get_by_id_use_case):
    command = GetPoruductCommandFactory.build()
    product = mock_get_by_id_use_case.execute(command=command)
    assert product.oid == command.oid

def test_find_many_use_case(mock_find_many_use_case):
    command = GetPoruductListCommandFactory.build()
    products, count = mock_find_many_use_case.execute(command=command)
    assert len(products) < command.pagination.limit
    assert count < 1000
    