"""
게시판, 게시글 url
"""
from django.urls import path

from .views import BoardListView, PostDetailView, PostListView

app_name = "board"

urlpatterns = [
    path("", BoardListView.as_view()),
    path("all", BoardListView.as_view(), name="list"),
    path("<int:pk>", PostListView.as_view(), name="board"),
    path("post/<int:pk>", PostDetailView.as_view(), name="detail"),
]
