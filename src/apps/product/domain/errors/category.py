

from src.helper.errors import BaseDomainException


class BaseCategoryException(BaseDomainException):
    pass

class CategoriesNotFoundException(BaseCategoryException):
    pass