"""
사용자 인증 관련 모델
"""
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    BaseUserManager을 상속받은 기본 사용자 매니저
    """

    def _create_user(self, email, password, **extra_fields):
        """
        사용자를 생성합니다.
        """
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user: User = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        일반 사용자를 생성합니다.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        모든 권한을 갖는 사용자를 생성합니다.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    사용자 모델
    email을 사용자이름으로 사용하는 사용자 모델
    """

    email = models.EmailField(
        _("이메일"),
        max_length=150,
        unique=True,
        help_text=_("이메일 주소를 입력해 주세요."),
        error_messages={
            "unique": _("해당 사용자 이름은 이미 존재합니다."),
        },
    )
    username = models.CharField(
        _("사용자 이름"),
        max_length=150,
        blank=True,
    )

    is_staff = models.BooleanField(
        _("스태프 권한"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("활성"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        _("가입일"),
        auto_now_add=True,
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.username or self.email

    class Meta:
        verbose_name = _("사용자")
        verbose_name_plural = _("사용자")
