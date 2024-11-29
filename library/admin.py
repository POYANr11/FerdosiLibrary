from django.contrib import admin
from .models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'year', 'status']
    ordering = ['title']
    list_filter = ['status', 'category', 'year']
    search_fields = ['title']
    list_editable = ['status', 'category']


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(BookRequest)
