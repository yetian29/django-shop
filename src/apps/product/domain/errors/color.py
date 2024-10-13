from src.helper.errors import BaseDomainException


class BaseColorException(BaseDomainException):
    pass


class ColorsNotFoundException(BaseColorException):
    pass
