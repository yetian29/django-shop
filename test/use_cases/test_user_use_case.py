from uuid import UUID
import pytest
from src.apps.user.domain.use_cases import AuthorizeUserUseCase, LoginUserUseCase
from test.mocks.factories.user import AuthorizeUserCommandFactory, LoginUserCommandFactory

@pytest.fixture
def mock_authorize_user_use_case(mock_test_container):
    return mock_test_container.resolve(AuthorizeUserUseCase)


@pytest.fixture
def mock_login_user_use_case(mock_test_container):
    return mock_test_container.resolve(LoginUserUseCase)


def test_authorize_and_login_user_use_case(mock_authorize_user_use_case, mock_login_user_use_case):
    command1 = AuthorizeUserCommandFactory.build()
    code = mock_authorize_user_use_case.execute(command1)
    assert isinstance(code, str)
    assert code.isdigit() 
    assert len(code) == 6
    
    command2 = LoginUserCommandFactory.build(
        phone_number=command1.user.phone_number,
        email=command1.user.email,
        code=code
        
    )
    token = mock_login_user_use_case.execute(command2)
    assert isinstance(token, UUID)
    token = str(token)
    assert UUID(token, version=4)

    