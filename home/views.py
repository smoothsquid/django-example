"""
메인페이지와 메인페이지에 필요한 뷰
"""
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """
    메인페이지 템플릿 뷰
    """

    template_name = "home/index.html"
