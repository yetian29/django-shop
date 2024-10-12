from django.contrib import admin

from src.apps.product.infrastructure.models.place_sell import PlaceSellORM


class PlaceSellORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name"]
    list_display_links = ["oid", "name"]


admin.site.register(PlaceSellORM, PlaceSellORMAdmin)
