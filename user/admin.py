"""
user 앱 관리자 페이지
"""
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User 모델 관리자 페이지
    """

    list_display = (
        "id",
        "email",
        "username",
        "is_active",
        "is_staff",
        "date_joined",
    )
    list_display_links = (
        "id",
        "email",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "email",
                    "username",
                    "password",
                    "is_active",
                    "is_staff",
                    "date_joined",
                ),
            },
        ),
    )
    readonly_fields = ("id",)
