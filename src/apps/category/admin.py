from django.contrib import admin

from src.apps.category.infrastructure.models import CategoryORM

# Register your models here.


class CategoryORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "category"]
    list_display_links = ["oid"]
    
admin.site.register(CategoryORM, CategoryORMAdmin)