# Generated by Django 3.2 on 2021-04-26 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("board", "0003_auto_20210424_1927"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="활성"),
        ),
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="작성자",
            ),
        ),
    ]