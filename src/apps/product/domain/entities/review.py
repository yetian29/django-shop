from dataclasses import dataclass, field

from src.apps.base.domain.entities import BaseOid, BaseTime, NotLoaded
from src.apps.product.domain.entities.product import DetailProduct
from src.apps.user.domain.entities import User


@dataclass
class Review(BaseOid, BaseTime):
    rating: int
    content: str
    product: DetailProduct
    user: User | NotLoaded = field(default_factory=NotLoaded)
