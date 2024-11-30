# Generated by Django 5.1.3 on 2024-11-30 15:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0005_alter_book_year"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookrequest",
            name="student_name",
        ),
        migrations.AddField(
            model_name="bookrequest",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="دانش\u200cآموز",
            ),
        ),
    ]
