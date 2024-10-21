

from src.helper.errors import BaseDomainException


class BaseReviewException(BaseDomainException):
    pass

class ReviewNotFoundException(BaseReviewException):
    pass