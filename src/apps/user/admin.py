from django.contrib import admin

from src.apps.user.infrastructure.models import UserORM

# Register your models here.


class UserORMAdmin(admin.ModelAdmin):
    list_display = [
        "oid",
        "phone_number",
        "email",
        "token",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["oid", "phone_number", "email"]
    search_fields = ["phone_number", "email"]


admin.site.register(UserORM, UserORMAdmin)
