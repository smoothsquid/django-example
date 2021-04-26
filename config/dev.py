"""
개발환경에서 사용할 설정 파일

python manage runserver --settings=config.dev
"""
from .settings import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATICFILES_DIRS = [
    BASE_DIR / "config" / "static",
]
