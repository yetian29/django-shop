from uuid import UUID

from ninja import Schema  

from src.apps.base.domain.entities import BaseDataField


class SizeOutSchema(Schema):
    oid: UUID
    name: str

    @staticmethod
    def from_entity(entity: BaseDataField) -> "SizeOutSchema":
        return SizeOutSchema(oid=entity.oid, name=entity.name)