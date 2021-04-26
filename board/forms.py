"""
게시글 작성, 수정 폼
"""
from django import forms

from .models import Post


class PostCreationForm(forms.ModelForm):
    """
    게시글 작성 폼
    """

    class Meta:
        model = Post
        fields = ("board", "title", "content")
        widgets = {
            "board": forms.HiddenInput(),
            "title": forms.TextInput({"class": "form-control"}),
        }
