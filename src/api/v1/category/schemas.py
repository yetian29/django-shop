from uuid import UUID
from ninja import Schema
from src.apps.category.domain.entities import Category
from src.apps.category.domain.values_object import CategoryEnum # type: ignore



class CategoryOutSchema(Schema):
    oid: UUID
    category: CategoryEnum
    
    
    @staticmethod
    def from_entity(category: Category) -> "CategoryOutSchema":
        return CategoryOutSchema(
            oid=category.oid,
            category=category.catgory
        )