# Generated by Django 5.1.3 on 2024-11-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "book_name",
                    models.CharField(max_length=255, verbose_name="نام کتاب"),
                ),
                (
                    "student_name",
                    models.CharField(max_length=255, verbose_name="نام دانش\u200cآموز"),
                ),
                (
                    "borrow_days",
                    models.PositiveIntegerField(verbose_name="تعداد روزها"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="تاریخ درخواست"
                    ),
                ),
            ],
        ),
    ]
