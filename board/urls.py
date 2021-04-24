"""
게시판, 게시글 url
"""
from django.urls import path

from .views import BoardListView

app_name = "board"

urlpatterns = [
    path("", BoardListView.as_view()),
    path("all", BoardListView.as_view(), name="list"),
]
