from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
    )
    list_display_links = (
        "id",
        "username",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "username",
                    "password",
                ),
            },
        ),
    )
    readonly_fields = ("id",)
