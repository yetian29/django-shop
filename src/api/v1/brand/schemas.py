from uuid import UUID

from ninja import Schema  # type: ignore

from src.apps.base.domain.entities import BaseDataField


class BrandOutSchema(Schema):
    oid: UUID
    name: str

    @staticmethod
    def from_entity(entity: BaseDataField) -> "BrandOutSchema":
        return BrandOutSchema(oid=entity.oid, name=entity.name)
