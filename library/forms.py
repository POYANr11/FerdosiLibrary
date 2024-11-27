from django import forms
from .models import BookRequest


class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ['book_name', 'student_name', 'borrow_days']
        labels = {
            'book_name': 'نام کتاب',
            'student_name': 'نام دانش‌آموز',
            'borrow_days': 'تعداد روزها',
        }
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کتاب'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام دانش‌آموز'}),
            'borrow_days': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'تعداد روزها'}),
        }
