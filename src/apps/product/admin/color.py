from django.contrib import admin

from src.apps.product.infrastructure.models.color import ColorORM


class ColorORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name"]
    list_display_links = ["oid", "name"]


admin.site.register(ColorORM, ColorORMAdmin)
