from src.helper.errors import BaseDomainException


class BaseUserException(BaseDomainException):
    pass


class UserNotFoundException(BaseUserException):
    pass


class UserCreatedNotSuccessException(BaseUserException):
    pass
