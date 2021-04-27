"""
게시판 관리자
"""
from django.contrib import admin

from .models import (
    Board,
    Post,
)


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    """
    게시판 추가 관리 삭제
    """

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "name",
                    "description",
                    "is_active",
                    "created",
                    "updated",
                )
            },
        ),
    )
    readonly_fields = (
        "id",
        "created",
        "updated",
    )
    list_display = (
        "id",
        "name",
        "description",
        "is_active",
        "created",
        "updated",
    )
    list_display_links = (
        "id",
        "name",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    게시글 확인 관리 삭제
    """

    list_display = (
        "id",
        "board",
        "title",
        "user",
        "deleted",
        "created",
        "updated",
    )
