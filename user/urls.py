"""
user 앱 urls
"""
from django.urls import path

from .views import (
    SigninView,
    SignoutView,
    SignupView,
)

app_name = "user"

urlpatterns = [
    path("signup", SignupView.as_view(), name="signup"),
    path("signout", SignoutView.as_view(), name="signout"),
    path("signin", SigninView.as_view(), name="signin"),
]
