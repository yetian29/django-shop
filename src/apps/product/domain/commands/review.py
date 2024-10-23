from dataclasses import dataclass
from uuid import UUID

from src.apps.product.domain.commands.product import PaginationQuery, SortQuery
from src.apps.product.domain.entities.product import DetailProduct
from src.apps.product.domain.entities.review import Review
from src.apps.user.domain.entities import User


@dataclass
class CreateReviewCommand:
    review: Review

@dataclass
class UpdateReviewCommand:
    review: Review

@dataclass
class DeleteReviewCommand:
    oid: UUID


@dataclass
class GetReviewListCommand:
    product: DetailProduct
    sort: SortQuery
    pagination: PaginationQuery
    