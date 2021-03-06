"""
사용자 인증 및 페이지에 관련된 뷰
"""
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .forms import SignupForm


class SignupView(SuccessMessageMixin, CreateView):
    """
    회원 가입 뷰
    """

    template_name = "user/signup.html"
    form_class = SignupForm
    success_message = _("회원가입이 완료되었습니다.")
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.object:
            auth.login(request, self.object)
        return response


class SignoutView(LogoutView):
    """
    로그아웃 뷰
    """

    next_page = reverse_lazy("user:signin")


class SigninView(LoginView):
    """
    로그인 뷰
    """

    template_name = "user/signin.html"
