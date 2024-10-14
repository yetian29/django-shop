from dataclasses import dataclass

from src.apps.base.domain.entities import BaseOid, BaseTime


@dataclass
class User(BaseOid, BaseTime):
    email: str | None
    phone_number: str | None
    token: str | None
    is_active: bool
