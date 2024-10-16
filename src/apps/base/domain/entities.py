from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class BaseOid:
    oid: UUID


@dataclass
class BaseTime:
    created_at: datetime
    updated_at: datetime 


@dataclass
class BaseDataField(BaseOid):
    name: str


class NotLoaded:
    def __bool__(self) -> bool:
        return False
    
    def __repr__(self) -> str:
        return "<NotLoaded>"