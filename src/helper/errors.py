class BaseDomainException(Exception):
    pass


class BaseServiceException(Exception):
    pass


def fail(exc: Exception):
    raise exc
