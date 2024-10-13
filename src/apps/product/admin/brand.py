from django.contrib import admin

from src.apps.product.infrastructure.models.brand import BrandORM


class BrandORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name"]
    list_display_links = ["oid", "name"]


admin.site.register(BrandORM, BrandORMAdmin)
