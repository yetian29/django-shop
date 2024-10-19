from dataclasses import dataclass

from src.apps.base.domain.entities import BaseOid, BaseTime


@dataclass
class User(BaseOid, BaseTime):
    phone_number: str | None
    email: str | None
    token: str | None
    is_active: bool
