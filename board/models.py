"""
게시판과 게시글 모델
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from config.settings import AUTH_USER_MODEL
from config.models import AbstractBasicInfo


class Board(AbstractBasicInfo):
    """
    게시판 정보
    """

    name = models.CharField(_("게시판 이름"), max_length=50)
    description = models.TextField(_("게시판 상세 설명"), null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = _("게시판")
        verbose_name_plural = _("게시판")


class Post(AbstractBasicInfo):
    """
    게시글
    """

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("작성자"),
        on_delete=models.CASCADE,
    )
    board = models.ForeignKey(
        "board.Board",
        verbose_name=_("게시판"),
        on_delete=models.CASCADE,
    )
    title = models.CharField(_("제목"), max_length=50)
    content = models.TextField(_("본문"))

    def get_absolute_url(self):
        return reverse(
            "board:post",
            kwargs={
                "board_pk": self.board.pk,
                "pk": self.pk,
            },
        )

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = _("게시글")
        verbose_name_plural = _("게시글")
