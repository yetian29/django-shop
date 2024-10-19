from src.helper.errors import BaseServiceException


class BaseCodeException(BaseServiceException):
    pass


class CodeNotFoundException(BaseCodeException):
    pass


class ExpiredCodeException(BaseCodeException):
    pass


class EqualCodesException(BaseCodeException):
    pass


class CachedDataNotExistException(BaseCodeException):
    pass
