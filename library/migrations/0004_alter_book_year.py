# Generated by Django 5.1.3 on 2024-11-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0003_rename_genre_category_rename_genre_book_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="year",
            field=models.DateField(),
        ),
    ]