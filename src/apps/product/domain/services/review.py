

from abc import ABC, abstractmethod
from uuid import UUID

from src.apps.product.domain.entities.review import Review


class IReviewService(ABC):
    @abstractmethod
    def create_or_update(self, review: Review) -> Review:
        pass
    
    @abstractmethod
    def delete(self, oid: UUID) -> None:
        pass