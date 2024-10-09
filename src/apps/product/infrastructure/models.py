from django.db import models

from src.apps.base.infrastructure.models import BaseDataFieldORM, BaseTimeORM
from src.apps.category.infrastructure.models import CategoryORM
from src.apps.product.domain.entities import CatalogProduct, DetailProduct
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
    # images = models.ImageField()
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
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

    
    def to_catalog_product_entity(self) -> CatalogProduct:
        return CatalogProduct(
            oid=self.oid,
            name=self.name,
            price=self.price,
            sold=self.sold,
            place_sell=self.place_sell
        )
        
    def to_detail_product_entity(self) -> DetailProduct:
        return DetailProduct(
            oid=self.oid,
            name=self.name,
            description=self.description,
            price=self.price,
            brand=self.brand,
            color=self.color,
            size=self.size,
            quantity=self.quantity
        )
    
    