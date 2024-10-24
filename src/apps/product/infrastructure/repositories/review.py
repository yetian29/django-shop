from abc import ABC, abstractmethod

from src.apps.product.domain.entities.product import DetailProduct
from src.apps.product.domain.errors.review import ReviewsNotFoundException
from src.apps.product.infrastructure.models.review import ReviewORM
from src.apps.user.domain.errors import UserNotAuthenticatedException
from src.helper.errors import fail


class IReviewRepository(ABC):
    @abstractmethod
    def create_or_update(sef, review: ReviewORM) -> ReviewORM:
        pass

    @abstractmethod
    def delete(self, oid: str) -> None:
        pass

    @abstractmethod
    def get_by_id(self, oid: str) -> ReviewORM | None:
        pass

    @abstractmethod
    def get_review_list(
        self,
        product: DetailProduct,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
    ) -> list[ReviewORM]:
        pass

    @abstractmethod
    def count_many(self, product: DetailProduct) -> int:
        pass


class PostgresReviewRepository(IReviewRepository):
    def get_by_id(self, oid: str) -> ReviewORM | None:
        dto = ReviewORM.objects.get(oid)
        return dto

    def create_or_update(self, review: ReviewORM) -> ReviewORM:
        if not review.is_authenticated():
            fail(UserNotAuthenticatedException)

        dto = self.get_by_id(oid=review.oid)
        if not dto:
            dto = ReviewORM.objects.create(
                oid=review.oid,
                user=review.user,
                product=review.product,
                rating=review.rating,
                content=review.content,
            )

        else:
            dto.rating = review.rating
            dto.content = review.content
            dto.save()

        return dto

    def delete(self, oid: str) -> None:
        ReviewORM.objects.filter(id=oid).delete()

    def get_review_list(
        self,
        product: DetailProduct,
        sort_field: str,
        sort_order: int,
        limit: int,
        offset: int,
    ) -> list[ReviewORM]:
        sort_direction = "-" if sort_order == -1 else ""
        order_by_field = f"{sort_direction}{sort_field}"
        reviews = ReviewORM.objects.filter(id=product.oid).order_by(order_by_field)[
            offset : offset + limit
        ]
        if not reviews.exists:
            fail(ReviewsNotFoundException)
        return list(reviews)

    def count_many(self, product: DetailProduct) -> int:
        count = ReviewORM.objects.filter(id=product.oid).count()
        if not count:
            fail(ReviewsNotFoundException)
        return count
