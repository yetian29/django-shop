from django.contrib import admin

from src.apps.product.infrastructure.models.size import SizeORM


class SizeORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name"]
    list_display_links = ["oid", "name"]
    

admin.site.register(SizeORM, SizeORMAdmin)
