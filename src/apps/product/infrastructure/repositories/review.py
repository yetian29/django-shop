
from abc import ABC, abstractmethod

from src.apps.product.domain.entities.product import DetailProduct
from src.apps.product.domain.errors.review import ReviewAlreadyExistException, ReviewNotFoundException, ReviewNotFoundToDeleteException, ReviewNotFoundToUpdateException, ReviewsNotFoundException
from src.apps.product.infrastructure.models.review import ReviewORM
from src.apps.user.domain.entities import User
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
    def get_review_list(
        self, 
        product: DetailProduct,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int
        ) -> list[ReviewORM]:
        pass

    @abstractmethod
    def count_many(
        self,
        product: DetailProduct
    ) -> int:
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
        fail(ReviewAlreadyExistException)

    def update(self, review: ReviewORM) -> ReviewORM:
        dto = self.get_by_id(oid=review.oid)
        if dto:
            dto = ReviewORM.objects.update(
                rating=review.rating,
                content=review.content,
                updated_at=review.updated_at 
            )
            return dto
        fail(ReviewNotFoundToUpdateException)
            
    
    def delete(self, oid: str) -> None:
        try:
            ReviewORM.objects.delete(oid)
        except ReviewORM.DoesNotExist:
            fail(ReviewNotFoundToDeleteException)
        

    def get_review_list(
        self, 
        product: DetailProduct, 
        sort_field: str, 
        sort_order: int, 
        limit: int, 
        offset: int
        ) -> list[ReviewORM]:
        sort_direction = "-" if sort_order == -1 else ""
        order_by_field = f"{sort_direction}{sort_field}"

        
        try:
            reviews = ReviewORM.objects.filter(product).order_by(order_by_field)[offset: offset + limit]
        except ReviewORM.DoesNotExist:
            fail(ReviewsNotFoundException)
        
        else: 
            return list(reviews)


        

