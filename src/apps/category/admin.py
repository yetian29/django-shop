from django.contrib import admin

from src.apps.category.infrastructure.models import CategoryORM

# Register your models here.


class CategoryORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name", "category"]
    list_display_links = ["oid", "name"]
    
admin.site.register(CategoryORM, CategoryORMAdmin)