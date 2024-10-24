from src.helper.errors import BaseDomainException


class BaseReviewException(BaseDomainException):
    pass


class ReviewsNotFoundException(BaseReviewException):
    pass
