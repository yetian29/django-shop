

from dataclasses import dataclass
from src.apps.base.domain.entities import BaseOid, BaseTime

@dataclass
class User(BaseOid, BaseTime):
    email: str | None = None
    phone_number: str | None = None
    token: str | None = None
    is_active: bool = False
    
    