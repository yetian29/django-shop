from django.contrib import admin

from src.apps.product.infrastructure.models import ProductORM

# Register your models here.


class ProductORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name", "price", "category", "place_sell", "brand", "color", "size", "gender", "quantity"]
    list_display_links = ["oid", "name"]

admin.site.register(ProductORM, ProductORMAdmin)