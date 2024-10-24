from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.product.domain.entities.product import DetailProduct
from src.apps.product.domain.entities.review import Review


class IReviewService(ABC):
    @abstractmethod
    def create_or_update(self,  review: Review) -> Review:
        pass

    @abstractmethod
    def delete(self, oid: UUID) -> None:
        pass

    @abstractmethod
    def get_review_list(
        self,
        product: DetailProduct,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
    ) -> list[Review]:
        pass

    @abstractmethod
    def count_many(self, product: DetailProduct) -> int:
        pass
