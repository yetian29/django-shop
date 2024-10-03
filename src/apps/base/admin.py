from django.contrib import admin

from src.apps.base.infrastructure.models import BaseDataFieldORM

# Register your models here.


class BaseDataFieldORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "name"]
    list_display_links = ["oid", "name"]


admin.site.register(BaseDataFieldORM, BaseDataFieldORMAdmin)