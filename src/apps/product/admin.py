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
    list_display = ["oid", "name", "price", "category", "get_places_sell", "brand", "get_colors", "get_sizes", "gender", "quantity"]  
    list_display_links = ["oid", "name"]  

    def get_places_sell(self, obj):  
        return ", ".join([place.name for place in obj.place_sell.all()])  
    get_places_sell.short_description = 'Place Sell'  # Tiêu đề của cột trong admin  

    def get_colors(self, obj):  
        return ", ".join([color.name for color in obj.color.all()])  
    get_colors.short_description = 'Colors'  

    def get_sizes(self, obj):  
        return ", ".join([size.name for size in obj.size.all()])  
    get_sizes.short_description = 'Sizes'

admin.site.register(PlaceSellORM, PlaceSellORMAdmin)
admin.site.register(BrandORM, BrandORMAdmin)
admin.site.register(ColorORM, ColorORMAdmin)
admin.site.register(SizeORM, SizeORMAdmin)
admin.site.register(ProductORM, ProductORMAdmin)