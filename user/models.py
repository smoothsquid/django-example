from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("사용자 이름"),
        max_length=20,
        unique=True,
        help_text=_("150자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다."),
        validators=[username_validator],
        error_messages={
            "unique": _("해당 사용자 이름은 이미 존재합니다."),
        },
    )
