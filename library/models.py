from django.db import models
import pandas as pd
from django.contrib.auth.models import User
LOAN_STATUS = (
    ('m', 'Maintenance'),
    ('b', 'Borrowed'),
    ('a', 'Available'),
)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    year = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=LOAN_STATUS, default='a')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BookRequest(models.Model):
    book_name = models.CharField(max_length=255, verbose_name="نام کتاب")
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="دانش‌آموز", null=True)
    borrow_days = models.PositiveIntegerField(verbose_name="تعداد روزها")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ درخواست")

    def __str__(self):
        return f"{self.student.username} - {self.book_name}"


