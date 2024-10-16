
from dataclasses import dataclass, field
from src.apps.base.domain.entities import BaseDataField, BaseOid, BaseTime, NotLoaded
from src.apps.user.domain.entities import User

@dataclass
class Review(BaseOid, BaseTime):
    rating: int
    content: str
    user: User | NotLoaded = field(default_factory=NotLoaded) 
    product: BaseDataField | NotLoaded = field(default_factory=NotLoaded)

    