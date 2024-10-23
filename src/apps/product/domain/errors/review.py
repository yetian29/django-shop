from src.helper.errors import BaseDomainException


class BaseReviewException(BaseDomainException):
    pass


class ReviewNotFoundException(BaseReviewException):
    pass


class ReviewAlreadyExistException(BaseReviewException):
    pass


class ReviewNotFoundToUpdateException(BaseReviewException):
    pass


class ReviewNotFoundToDeleteException(BaseReviewException):
    pass


class ReviewsNotFoundException(BaseReviewException):
    pass
