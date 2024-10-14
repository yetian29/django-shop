from uuid import UUID

from ninja import Schema

from src.apps.base.domain.entities import BaseDataField


class ColorOutSchema(Schema):
    oid: UUID
    name: str

    @staticmethod
    def from_entity(entity: BaseDataField) -> "ColorOutSchema":
        return ColorOutSchema(oid=entity.oid, name=entity.name)
