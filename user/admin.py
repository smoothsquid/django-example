"""
user 앱 관리자 페이지
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
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
    readonly_fields = (
        "id",
        "date_joined",
    )

    # def save_model(self, request, obj: User, form, change) -> None:
    #     """
    #     사용자 데이터를 저장할 때 비밀번호를 암호화 합니다.
    #     """

    #     return super().save_model(request, obj, form, change)
