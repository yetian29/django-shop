from src.helper.errors import BaseDomainException


class BaseSizeException(BaseDomainException):
    pass


class SizesNotFoundException(BaseSizeException):
    pass
