from django.contrib import admin

from src.apps.product.infrastructure.models.review import ReviewORM


class ReviewORMAdmin(admin.ModelAdmin):
    list_display = ["oid", "user", "product", "rating", "content", "created_at", "updated_at"]
    list_display_links = ["oid"]
    

admin.site.register(ReviewORM, ReviewORMAdmin)