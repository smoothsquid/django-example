"""
user앱의 views를 테스트합니다.
"""
import logging
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware

from .views import SignupView

logger = logging.getLogger(__name__)


def add_middleware_to_request(request, middleware_class):
    """
    request에 테스트를 위한 미들웨어를 추가합니다.
    """
    middleware = middleware_class()
    middleware.process_request(request)
    return request


class SignupViewTests(TestCase):
    """
    회원가입 뷰 테스트
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.signup_view = SignupView.as_view()
        self.signup_url = reverse("user:signup")
        self.wrong_username_user = {
            "username": "#$&@&^*",
            "password1": "783746asd",
            "password2": "783746asd",
        }

    def test_signup_page(self):
        """
        회원가입 페이지 접근 테스트
        """
        request = self.factory.get(self.signup_url)
        request.user = AnonymousUser()
        request = add_middleware_to_request(request, SessionMiddleware)

        response = self.signup_view(request)
        self.assertContains(response, "회원가입")

    def test_signup(self):
        """
        잘못된 아이디 입력 테스트
        """
        request = self.factory.post(
            self.signup_url,
            self.wrong_username_user,
        )
        request = add_middleware_to_request(request, SessionMiddleware)

        response = self.signup_view(request)
        self.assertEqual(response.status_code, 200)
