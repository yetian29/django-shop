from src.helper.errors import BaseDomainException


class BaseBrandException(BaseDomainException):
    pass


class BrandsNotFoundException(BaseBrandException):
    pass
