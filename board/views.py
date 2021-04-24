"""
게시판 및 게시글 뷰
"""
from django.views.generic.list import ListView

from .models import Board


class BoardListView(ListView):
    """
    게시글 목록 뷰
    """

    template_name = "board/list.html"
    queryset = Board.objects.all()
