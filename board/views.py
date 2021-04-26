"""
게시판 및 게시글 뷰
"""
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator

from .forms import PostCreationForm
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
    paginate_by = 5
    board_object = None
    board_pk_url_kwargs = "pk"

    def get_queryset(self):
        self.board_object = Board.objects.get(
            pk=self.kwargs[self.board_pk_url_kwargs],
        )
        return Post.objects.filter(board=self.board_object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["board_object"] = self.board_object
        return context


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


@method_decorator(login_required, name="dispatch")
class PostCreationView(CreateView):
    """
    게시글 등록 폼 및 등록
    """

    template_name = "board/form.html"
    model = Post
    form_class = PostCreationForm
    board_pk_url_kwargs = "board_pk"

    # @login_required
    # def dispatch(self, *args, **kwargs):
    #     super().dispatch(*args, **kwargs)

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
