from django.db import models

from src.apps.base.infrastructure.models import BaseDataFieldORM, BaseTimeORM
from src.apps.category.infrastructure.models import CategoryORM
from src.apps.product.domain.entities import CatalogProduct, Product
from src.apps.product.domain.values_object import GenderEnum


class PlaceSellORM(BaseDataFieldORM):
    def __str__(self):
        return self.name

class BrandORM(BaseDataFieldORM):
    def __str__(self):
        return self.name

class ColorORM(BaseDataFieldORM):
    def __str__(self):
        return self.name
    
class SizeORM(BaseDataFieldORM):
    def __str__(self):
        return self.name
    
class ProductORM(BaseDataFieldORM, BaseTimeORM):
    price = models.PositiveIntegerField(default=0)
    # images = models.ImageField()
    category = models.ForeignKey(CategoryORM, on_delete=models.CASCADE, related_name="products")
    place_sell = models.ForeignKey(PlaceSellORM, on_delete=models.PROTECT, related_name="products_place_sell")
    brand = models.ForeignKey(BrandORM, on_delete=models.PROTECT, related_name="products_brand")
    color = models.ForeignKey(ColorORM, on_delete=models.PROTECT, related_name="products_color")
    size = models.ForeignKey(SizeORM, on_delete=models.PROTECT, related_name="products_size")
    gender = models.CharField(max_length=16, choices=[(tag.value, tag.name) for tag in GenderEnum], default=GenderEnum.Unisex)
    quantity = models.PositiveIntegerField(default=0)
    sold = models.CharField(max_length=16)


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
    
    def to_catalog_product_entity(self) -> CatalogProduct:
        return CatalogProduct(
            oid=self.oid,
            name=self.name,
            price=self.price,
            sold=self.sold,
            place_sell=self.place_sell
        )
        
    def to_entity(self) -> Product:
        return Product(
            oid=self.oid,
            name=self.name,
            price=self.price,
            category=self.category,
            brand=self.brand,
            color=self.color,
            size=self.size,
            gender=self.gender,
            quantity=self.quantity
        )
    
    