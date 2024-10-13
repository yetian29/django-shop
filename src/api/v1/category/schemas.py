from uuid import UUID

from ninja import Schema

from src.apps.product.domain.entities.category import Category
from src.apps.product.domain.values_object.category import CategoryEnum


class CategoryOutSchema(Schema):
    oid: UUID
    category: CategoryEnum

    @staticmethod
    def from_entity(entity: Category) -> "CategoryOutSchema":
        return CategoryOutSchema(oid=entity.oid, category=entity.category)
