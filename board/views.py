"""
게시판 및 게시글 뷰
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Board, Post


class BoardListView(ListView):
    """
    전체 게시판 목록 뷰
    """

    template_name = "board/board_list.html"
    queryset = Board.objects.all()


class PostListView(ListView):
    """
    해당 게시판의 전체 게시글 뷰
    """

    template_name = "board/list.html"

    def get_queryset(self):
        return Post.objects.filter(board__id=self.kwargs["pk"])


class PostDetailView(DetailView):
    """
    게시글 상세 페이지
    """

    template_name = "board/detail.html"
    model = Post
