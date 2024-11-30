from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import BookRequest


class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ['book_name', 'borrow_days']
        labels = {
            'book_name': 'نام کتاب',
            'borrow_days': 'تعداد روزها',
        }
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کتاب'}),
            'borrow_days': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'تعداد روزها'}),
        }

    def clean_borrow_days(self):
        borrow_days = self.cleaned_data.get('borrow_days')
        if borrow_days and borrow_days < 1:
            raise forms.ValidationError('حداقل تعداد روزها باید ۱ باشد.')
        return borrow_days


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='شماره موبایل',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره موبایل',
        }),
    )
    password = forms.CharField(
        label='کد ملی',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'کد ملی',
        }),
    )

