"""
게시판 및 게시글 뷰
"""
from django.http.response import HttpResponseRedirect
from board.forms import PostCreationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

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

    게시글 ID (board_pk)와 게시글 고유번호 (pk)로
    게시글 데이터를 반환합니다.
    """

    template_name = "board/detail.html"
    model = Post
    board_pk_url_kwargs = "board_pk"

    def get_queryset(self):
        board_pk = self.kwargs.get(self.board_pk_url_kwargs)
        return super().get_queryset().filter(board__pk=board_pk)


class PostCreationView(CreateView):
    """
    게시글 등록 폼 및 등록
    """

    template_name = "board/form.html"
    model = Post
    form_class = PostCreationForm
    board_pk_url_kwargs = "board_pk"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["board"].initial = Board.objects.get(
            pk=self.kwargs.get(self.board_pk_url_kwargs)
        )
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        # return HttpResponseRedirect(self.get_success_url())
        return super().form_valid(form)
