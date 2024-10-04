from django.contrib import admin

from src.apps.product.infrastructure.models import BrandORM, ColorORM, PlaceSellORM, ProductORM, SizeORM

# Register your models here.

class PlaceSellORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name"]
    list_display_links = ["oid", "name"]

class BrandORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name"]
    list_display_links = ["oid", "name"]

class ColorORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name"]
    list_display_links = ["oid", "name"]

class SizeORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name"]
    list_display_links = ["oid", "name"]
    
class ProductORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name", "price", "category", "place_sell", "brand", "color", "size", "gender", "quantity"]
    list_display_links = ["oid", "name"]

admin.site.register(PlaceSellORM, PlaceSellORMAdmin)
admin.site.register(BrandORM, BrandORMAdmin)
admin.site.register(ColorORM, ColorORMAdmin)
admin.site.register(SizeORM, SizeORMAdmin)
admin.site.register(ProductORM, ProductORMAdmin)