from src.helper.errors import BaseDomainException  # type: ignore


class BaseProductException(BaseDomainException):
    pass


class ProductNotFoundException(BaseProductException):
    pass


class ProductsNotFoundException(BaseProductException):
    pass
