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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    게시글 확인 관리 삭제
    """
