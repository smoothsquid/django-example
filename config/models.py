"""
프로젝트 전반적으로 사용하는 모델을 작성합니다.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractBasicInfo(models.Model):
    """
    생성 시간과 수정 시간을 갖는 추상 모델
    """

    # name = models.CharField(_("이름"), max_length=50)
    created = models.DateTimeField(_("생성 시간"), auto_now_add=True)
    updated = models.DateTimeField(_("변경 시간"), auto_now=True, null=True, blank=True)

    # 생성 시간과 변경 시간으로 할 수 있는 메서드 작성

    class Meta:
        abstract = True