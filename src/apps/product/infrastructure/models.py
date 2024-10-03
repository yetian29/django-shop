from django.db import models

from src.apps.base.infrastructure.models import BaseDataFieldORM, BaseTimeORM
from src.apps.category.infrastructure.models import CategoryORM
from src.apps.product.domain.entities import Product
from src.apps.product.domain.values_object import GenderEnum


class ProductORM(BaseDataFieldORM, BaseTimeORM):
    price = models.PositiveIntegerField(default=0)
    # images = models.ImageField()
    category = models.ForeignKey(CategoryORM, on_delete=models.CASCADE, related_name="products")
    place_sell = models.ForeignKey(BaseDataFieldORM, on_delete=models.PROTECT, related_name="products_place_sell")
    brand = models.ForeignKey(BaseDataFieldORM, on_delete=models.PROTECT, related_name="products_brand")
    color = models.ForeignKey(BaseDataFieldORM, on_delete=models.PROTECT, related_name="products_color")
    size = models.ForeignKey(BaseDataFieldORM, on_delete=models.PROTECT, related_name="products_size")
    gender = models.CharField(max_length=16, choices=[(tag.value, tag.name) for tag in GenderEnum], default=GenderEnum.Unisex)
    quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name
    
    @staticmethod
    def from_entity(product: Product) -> "ProductORM":
        return ProductORM(
            oid=product.oid,
            name=product.name,
            price=product.price,
            category=product.category,
            place_sell=product.place_sell,
            brand=product.brand,
            color=product.color,
            size=product.size,
            gender=product.gender,
            quantity=product.quantity,
            created_at=product.created_at,
            updated_at=product.updated_at
        )
    
    def to_entity(self) -> Product:
        return Product(
            oid=self.oid,
            name=self.name,
            price=self.price,
            category=self.category,
            place_sell=self.place_sell,
            brand=self.brand,
            color=self.color,
            size=self.size,
            gender=self.gender,
            sold=self.sold,
            quantity=self.quantity
        )