from dataclasses import dataclass
from uuid import UUID

from src.apps.product.domain.entities.review import Review


@dataclass
class CreateOrUpdateReviewCommand:
    review: Review


@dataclass
class DeleteReviewCommand:
    oid: UUID
