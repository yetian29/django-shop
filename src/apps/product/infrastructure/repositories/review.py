
from abc import ABC, abstractmethod

from src.apps.product.domain.errors.review import ReviewNotFoundException
from src.apps.product.infrastructure.models.review import ReviewORM
from src.helper.errors import fail


class IReviewRepository(ABC):
    @abstractmethod
    def create(sef, review: ReviewORM) -> ReviewORM:
        pass

    @abstractmethod
    def update(self, review: ReviewORM) -> ReviewORM:
        pass

    @abstractmethod
    def delete(self, oid: str) -> None:
        pass
    
    @abstractmethod
    def get_by_id(self, oid: str) -> ReviewORM:
        pass

    @abstractmethod
    def get_review_list_by_product(self) -> list[ReviewORM]:
        pass

class PostgresReviewRepository(IReviewRepository):
    def get_by_id(self, oid: str) -> ReviewORM:
        try:
            dto = ReviewORM.objects.get(oid)
        except ReviewORM.DoesNotExist:
            fail(ReviewNotFoundException)
        else:
            return dto

        
    def create(self, review: ReviewORM) -> ReviewORM:
        dto = self.get_by_id(oid=review.oid)
        if not dto:
            dto = ReviewORM.objects.create(
                oid=review.oid,
                user=review.user,
                product=review.product,
                rating=review.rating,
                content=review.content,
                created_at=review.created_at,
                updated_at=review.updated_at
                
            )
            return dto

    def update(self, review: ReviewORM) -> ReviewORM:
        dto = self.get_by_id(oid=review.oid)
        if dto:
            dto = ReviewORM.objects.update(
                rating=review.rating,
                content=review.content,
                updated_at=review.updated_at 
            )
            return dto
            
    
    def delete(self, oid: str) -> None:
        ReviewORM.objects.delete(oid)
        
